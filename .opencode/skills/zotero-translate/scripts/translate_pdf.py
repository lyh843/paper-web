#!/usr/bin/env python3
"""Run installed PDF2zh-next with an isolated config; never write to Zotero."""
import argparse
import hashlib
import importlib.metadata
import json
import os
import re
import shutil
import signal
import subprocess
import tempfile
import tomllib
from datetime import datetime, timezone
from pathlib import Path

SERVICES = (
    'siliconflowfree', 'openai', 'aliyundashscope', 'google', 'bing', 'deepl',
    'deepseek', 'ollama', 'xinference', 'azureopenai', 'modelscope', 'zhipu',
    'siliconflow', 'tencentmechinetranslation', 'gemini', 'azure', 'anythingllm',
    'dify', 'grok', 'groq', 'qwenmt', 'openaicompatible', 'claudecode', 'clitranslator',
)


def discover(home=None):
    home = Path(home or Path.home())
    desktop_files = []
    for directory in [home / '.local/share/applications', Path('/usr/share/applications')]:
        if directory.is_dir():
            for path in directory.glob('*.desktop'):
                text = path.read_text(errors='replace')
                if 'pdf2zh' in (path.name + text).lower():
                    desktop_files.append(str(path))
    engine_candidates = [shutil.which('pdf2zh_next'), str(home / 'miniconda3/envs/zotero-pdf2zh-next-venv/bin/pdf2zh_next')]
    engines = list(dict.fromkeys(str(Path(p).resolve()) for p in engine_candidates if p and Path(p).is_file()))
    config = home / 'zotero-pdf2zh/server/config/config.toml'
    return {'desktopFiles': desktop_files, 'engines': engines,
            'config': str(config) if config.is_file() else None,
            'launcher': str(home / '.local/bin/launch-zotero-pdf2zh') if (home / '.local/bin/launch-zotero-pdf2zh').is_file() else None}


def set_scalar(text, section, key, value):
    """Update a simple TOML table's scalar without rewriting other settings."""
    header = re.search(r'^\[' + re.escape(section) + r'\][ \t]*(?:#.*)?$', text, re.M)
    if not header:
        return text.rstrip() + f'\n\n[{section}]\n{key} = {value}\n'
    start = header.end()
    next_header = re.search(r'^\[', text[start:], re.M)
    end = start + next_header.start() if next_header else len(text)
    body = text[start:end]
    pattern = r'^[ \t]*' + re.escape(key) + r'[ \t]*=.*$'
    if re.search(pattern, body, re.M):
        body = re.sub(pattern, f'{key} = {value}', body, count=1, flags=re.M)
    else:
        body = body.rstrip() + f'\n{key} = {value}\n\n'
    return text[:start] + body + text[end:]


def prepare_config(text, pages=None, layout='lr'):
    parsed = tomllib.loads(text)
    active = [s for s in SERVICES if parsed.get(s) is True]
    if len(active) != 1:
        raise ValueError('Expected exactly one configured translation service; inspect the software configuration first.')
    if pages and not re.fullmatch(r'\d+(?:-\d*)?(?:,\d+(?:-\d*)?)*', pages):
        raise ValueError('Pages must use positive ranges such as 1,3-5 or 2-.')
    if pages and any(int(n) < 1 for n in re.findall(r'\d+', pages)):
        raise ValueError('Page numbers start at 1.')
    updates = {
        'basic': {'input_files': '[]', 'gui': 'false', 'debug': 'false', 'warmup': 'false',
                  'generate_offline_assets': '"null"', 'restore_offline_assets': '"null"'},
        'pdf': {'no_mono': 'true', 'no_dual': 'false', 'pages': json.dumps(pages or 'null'),
                'use_alternating_pages_dual': str(layout == 'alternating').lower(),
                'dual_translate_first': 'false', 'only_include_translated_page': 'false',
                'watermark_output_mode': '"no_watermark"'},
    }
    for section, values in updates.items():
        for key, value in values.items():
            text = set_scalar(text, section, key, value)
    # Some locally modified releases have put this switch in translation.
    if 'only_include_translated_page' in parsed.get('translation', {}):
        text = set_scalar(text, 'translation', 'only_include_translated_page', 'false')
    check = tomllib.loads(text)
    assert check['pdf']['no_mono'] is True and check['pdf']['no_dual'] is False
    return text, active[0]


def sensitive_values(value):
    result = []
    if isinstance(value, dict):
        for key, item in value.items():
            if any(x in key.lower() for x in ('key', 'token', 'secret', 'password', 'auth')):
                if isinstance(item, str) and item not in ('', 'null', 'None'):
                    result.append(item)
            else:
                result.extend(sensitive_values(item))
    elif isinstance(value, list):
        for item in value:
            result.extend(sensitive_values(item))
    return result


def redact(text, secrets):
    for secret in sorted(secrets, key=len, reverse=True):
        text = text.replace(secret, '[REDACTED]')
    text = re.sub(r'(?i)bearer\s+[A-Za-z0-9._~+/=-]+', 'Bearer [REDACTED]', text)
    return re.sub(r'\x1b\[[0-?]*[ -/]*[@-~]', '', text)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def inspect_outputs(paths, source, layout, pages, target_lang):
    try:
        import fitz
    except ImportError:
        return {'status': 'generated-unverified', 'reason': 'Run in the engine Python environment with PyMuPDF for PDF checks.'}
    with fitz.open(source) as src:
        result = {'status': 'checked-automatically-needs-visual-review', 'sourcePages': len(src), 'documents': []}
        for path in paths:
            with fitz.open(path) as doc:
                chinese = [len(re.findall(r'[\u3400-\u9fff]', p.get_text())) for p in doc]
                info = {'file': path.name, 'pages': len(doc), 'chineseCharactersByPage': chinese,
                        'imagePlacements': sum(len(p.get_images()) for p in doc)}
                if target_lang.lower().startswith('zh') and not sum(chinese):
                    result['status'] = 'generated-needs-investigation'
                if not pages:
                    expected = len(src) * (2 if layout == 'alternating' else 1)
                    info['pageCountMatches'] = len(doc) == expected
                    if not info['pageCountMatches']:
                        result['status'] = 'generated-needs-investigation'
                if layout == 'lr' and not pages and len(doc) == len(src):
                    def norm(s):
                        import unicodedata
                        return re.sub(r'\s+', '', unicodedata.normalize('NFKC', s))
                    info['originalTextUnchangedByPage'] = [
                        norm(page.get_text(clip=fitz.Rect(0, 0, page.rect.width / 2, page.rect.height))) == norm(src[i].get_text())
                        for i, page in enumerate(doc)
                    ]
                    if not all(info['originalTextUnchangedByPage']):
                        result['status'] = 'generated-needs-investigation'
                if paths and path == paths[0] and len(doc):
                    doc[0].get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False).save(path.parent / 'preview-first-page.png')
                result['documents'].append(info)
        return result


def run(args):
    source = Path(args.input).expanduser().resolve(strict=True)
    config_path = Path(args.config).expanduser().resolve(strict=True)
    engine = Path(args.engine).expanduser().resolve(strict=True)
    if source.suffix.lower() != '.pdf':
        raise ValueError('Input must be a verified PDF.')
    original_config = config_path.read_bytes()
    temporary_text, service = prepare_config(original_config.decode(), args.pages, args.layout)
    help_result = subprocess.run([str(engine), '--help'], capture_output=True, text=True, timeout=60)
    for flag in ('--config-file', '--no-mono', '--output', '--' + service):
        if help_result.returncode != 0 or flag not in help_result.stdout:
            raise ValueError(f'Installed engine does not advertise {flag}; inspect its version before adapting.')
    out = Path(args.output).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=False)
    record = {'status': 'running', 'source': str(source), 'sourceSha256': sha(source),
              'software': 'Zotero PDF2zh / PDF2zh-next', 'service': service,
              'sourceLanguage': args.source_lang, 'targetLanguage': args.target_lang,
              'layout': args.layout, 'pages': args.pages or 'all', 'onlyBilingual': True,
              'zoteroModified': False, 'startedAt': datetime.now(timezone.utc).isoformat()}
    try:
        record['engineVersionInCurrentPython'] = importlib.metadata.version('pdf2zh_next')
    except importlib.metadata.PackageNotFoundError:
        record['engineVersionInCurrentPython'] = None
    status_path = out / 'translation-status.json'
    def save():
        status_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
    save()
    try:
        temp_root = Path('/tmp/opencode')
        temp_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='zotero-translate-', dir=temp_root) as temp:
            private = Path(temp) / 'config.toml'
            private.touch(mode=0o600)
            private.write_text(temporary_text, encoding='utf-8')
            input_copy = Path(temp) / source.name
            shutil.copyfile(source, input_copy)
            cmd = [str(engine), str(input_copy), '--config-file', str(private), '--' + service,
                   '--output', str(out), '--lang-in', args.source_lang, '--lang-out', args.target_lang,
                   '--no-mono', '--watermark-output-mode', 'no_watermark']
            if args.pages:
                cmd.extend(['--pages', args.pages])
            if args.layout == 'alternating':
                cmd.append('--use-alternating-pages-dual')
            with (Path(temp) / 'engine.log').open('w') as log:
                process = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
                try:
                    code = process.wait(timeout=args.timeout)
                except (subprocess.TimeoutExpired, KeyboardInterrupt):
                    os.killpg(process.pid, signal.SIGTERM)
                    try:
                        process.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        os.killpg(process.pid, signal.SIGKILL)
                        process.wait()
                    raise RuntimeError('Translation stopped or timed out; no automatic retry was made.') from None
                finally:
                    log.flush()
                    safe = redact((Path(temp) / 'engine.log').read_text(errors='replace'), sensitive_values(tomllib.loads(temporary_text)))
                    (out / 'translation.log').write_text(safe, encoding='utf-8')
            record['exitCode'] = code
            if code:
                raise RuntimeError('Translation failed; see the redacted translation.log. Do not blindly retry.')
        outputs = sorted(p for p in out.glob('*.pdf') if 'dual' in p.name.lower())
        unexpected = [p.name for p in out.glob('*.pdf') if p not in outputs]
        if not outputs or unexpected:
            raise RuntimeError('Expected only bilingual PDF output; inspect the generated files before delivery.')
        record['outputs'] = [{'file': p.name, 'bytes': p.stat().st_size, 'sha256': sha(p)} for p in outputs]
        checks = inspect_outputs(outputs, source, args.layout, args.pages, args.target_lang)
        record['verification'] = checks
        record['status'] = checks['status']
    except Exception as exc:
        record['status'] = 'failed'
        record['error'] = redact(str(exc), sensitive_values(tomllib.loads(temporary_text)))
        raise
    finally:
        record['originalConfigUnchanged'] = config_path.read_bytes() == original_config
        record['originalPDFUnchanged'] = sha(source) == record['sourceSha256']
        record['finishedAt'] = datetime.now(timezone.utc).isoformat()
        save()
    print(json.dumps(record, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('discover', help='List related registrations and known engine/config paths; print no credentials.')
    task = commands.add_parser('run', help='Translate with an isolated existing config; bilingual only.')
    task.add_argument('--input', required=True)
    task.add_argument('--output', required=True)
    task.add_argument('--engine', required=True)
    task.add_argument('--config', required=True)
    task.add_argument('--source-lang', default='en')
    task.add_argument('--target-lang', default='zh-CN')
    task.add_argument('--pages')
    task.add_argument('--layout', choices=['lr', 'alternating'], default='lr')
    task.add_argument('--timeout', type=int, default=3600)
    args = parser.parse_args()
    if args.command == 'discover':
        print(json.dumps(discover(), ensure_ascii=False, indent=2))
    else:
        try:
            run(args)
        except Exception as exc:
            # Never print arbitrary exception payloads from credential-bearing config parsing.
            parser.exit(1, f'{type(exc).__name__}: Translation could not complete. Check inputs and the redacted status/log if created.\n')


if __name__ == '__main__':
    main()
