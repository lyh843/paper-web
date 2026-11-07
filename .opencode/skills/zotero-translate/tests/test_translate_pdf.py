import argparse
import contextlib
import importlib.util
import io
import json
import os
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/translate_pdf.py'
spec = importlib.util.spec_from_file_location('translate_pdf', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

CONFIG = '''openaicompatible = true
[basic]
gui = true
debug = true
input_files = ["old.pdf"]
[translation]
qps = 4
[pdf]
no_mono = false
no_dual = true
pages = "2-3"
only_include_translated_page = true
use_alternating_pages_dual = true
[openaicompatible_detail]
openai_compatible_model = "test-model"
openai_compatible_api_key = "TEST-SECRET-DO-NOT-PRINT"
'''


class ConfigTests(unittest.TestCase):
    def test_default_is_full_bilingual_only_without_mutating_source(self):
        output, service = module.prepare_config(CONFIG)
        data = tomllib.loads(output)
        self.assertEqual(service, 'openaicompatible')
        self.assertTrue(data['pdf']['no_mono'])
        self.assertFalse(data['pdf']['no_dual'])
        self.assertEqual(data['pdf']['pages'], 'null')
        self.assertFalse(data['pdf']['use_alternating_pages_dual'])
        self.assertFalse(data['pdf']['only_include_translated_page'])
        self.assertFalse(data['basic']['gui'])
        self.assertFalse(data['basic']['debug'])
        self.assertEqual(data['openaicompatible_detail']['openai_compatible_model'], 'test-model')
        self.assertIn('pages = "2-3"', CONFIG)

    def test_explicit_pages_and_alternating_layout(self):
        output, _ = module.prepare_config(CONFIG, '1,3-5', 'alternating')
        data = tomllib.loads(output)
        self.assertEqual(data['pdf']['pages'], '1,3-5')
        self.assertTrue(data['pdf']['use_alternating_pages_dual'])

    def test_missing_tables_can_be_added(self):
        output, _ = module.prepare_config('google = true\n')
        self.assertTrue(tomllib.loads(output)['pdf']['no_mono'])

    def test_ambiguous_services_and_bad_pages_fail(self):
        for text, pages in [(CONFIG.replace('openaicompatible = true', 'openaicompatible = false'), None),
                            ('google = true\n' + CONFIG, None), (CONFIG, '0-3'), (CONFIG, 'oops')]:
            with self.assertRaises(ValueError):
                module.prepare_config(text, pages)

    def test_redaction(self):
        secrets = module.sensitive_values(tomllib.loads(CONFIG))
        text = module.redact('key=TEST-SECRET-DO-NOT-PRINT Bearer abcdef12345', secrets)
        self.assertNotIn('TEST-SECRET', text)
        self.assertNotIn('abcdef12345', text)

    def test_mock_engine_no_network_or_real_translation(self):
        try:
            import fitz
        except ImportError:
            self.skipTest('PyMuPDF required for the mock PDF integration test')
        with tempfile.TemporaryDirectory(dir='/tmp/opencode', prefix='test-translate-') as temp:
            root = Path(temp)
            source = root / 'input.pdf'
            doc = fitz.open()
            doc.new_page().insert_text((40, 50), 'Original fixture page')
            doc.save(source)
            doc.close()
            config = root / 'config.toml'
            config.write_text(CONFIG)
            engine = root / 'mock-engine'
            engine.write_text(f'#!{sys.executable}\n' + '''import sys, pathlib, tomllib, fitz
if '--help' in sys.argv:
    print('--config-file --no-mono --output --openaicompatible')
    raise SystemExit(0)
def arg(k): return sys.argv[sys.argv.index(k)+1]
private=pathlib.Path(arg('--config-file'))
assert private.stat().st_mode & 0o777 == 0o600
c=tomllib.loads(private.read_text())
assert c['pdf']['no_mono'] and not c['pdf']['no_dual']
assert c['pdf']['pages']=='null'
print(c['openaicompatible_detail']['openai_compatible_api_key'])
src=fitz.open(sys.argv[1]); out=fitz.open()
for i,p in enumerate(src):
    page=out.new_page(width=p.rect.width*2,height=p.rect.height)
    page.show_pdf_page(fitz.Rect(0,0,p.rect.width,p.rect.height),src,i)
    page.show_pdf_page(fitz.Rect(p.rect.width,0,p.rect.width*2,p.rect.height),src,i)
    page.insert_text((p.rect.width+40,80),'测试对照',fontname='china-s')
out.save(pathlib.Path(arg('--output'))/'fixture.dual.pdf')
''')
            engine.chmod(0o700)
            args = argparse.Namespace(input=str(source), output=str(root / 'result'), engine=str(engine),
                                      config=str(config), pages=None, layout='lr', timeout=60,
                                      source_lang='en', target_lang='zh-CN')
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                module.run(args)
            state = json.loads((root / 'result/translation-status.json').read_text())
            self.assertEqual(state['status'], 'checked-automatically-needs-visual-review')
            self.assertTrue(state['originalConfigUnchanged'])
            self.assertTrue(state['originalPDFUnchanged'])
            self.assertEqual(len(list((root / 'result').glob('*.pdf'))), 1)
            self.assertNotIn('TEST-SECRET-DO-NOT-PRINT', stdout.getvalue())
            self.assertNotIn('TEST-SECRET-DO-NOT-PRINT', (root / 'result/translation.log').read_text())
            self.assertEqual(config.read_text(), CONFIG)
            with self.assertRaises(FileExistsError):
                module.run(args)


if __name__ == '__main__':
    unittest.main()
