"""Artifact-only offline browser checks; does not run gameplay or paid APIs."""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
result = {}
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    page = browser.new_page(viewport={'width': 1280, 'height': 900}, device_scale_factor=1)
    errors, remote = [], []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.on('request', lambda req: remote.append(req.url) if req.url.startswith(('http:', 'https:')) else None)
    page.goto((root / 'index.html').as_uri())
    page.locator('img').evaluate_all("imgs=>imgs.forEach(i=>i.loading='eager')")
    page.wait_for_function('Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)')
    assert page.locator('h2').count() == 13
    assert page.locator('.katex-error').count() == 0
    assert page.locator('.katex').count() > 0
    assert not page.evaluate('document.body.innerText.includes("$$")')
    assert not page.evaluate('document.documentElement.scrollWidth>innerWidth')
    for href in page.locator('.toc a').evaluate_all('xs=>xs.map(x=>x.getAttribute("href"))'):
        assert page.locator(href).count() == 1, href
    result['desktop'] = {'width': 1280, 'chapters': 13, 'images': 3, 'math_nodes': page.locator('.katex').count(), 'overflow': False}
    source = page.locator('.source-ref').first
    assert not source.is_visible()
    page.locator('label[for="show-sources"]').click()
    assert source.is_visible()
    page.locator('label[for="show-sources"]').click()
    assert not source.is_visible()
    result['source_toggle'] = 'pass'
    page.screenshot(path='/tmp/opencode/lm-fight-desktop.png')
    page.locator('.archify-disclosure > summary').click()
    frame = page.frame_locator('iframe')
    frame.locator('#model').select_option('q72')
    frame.locator('#opponent').select_option('q32')
    assert '2.5%' in frame.locator('#match-card').inner_text()
    frame.locator('#model').select_option('claude')
    assert '38.3%' in frame.locator('#match-card').inner_text()
    assert '冲突' in frame.locator('#match-card').inner_text()
    frame.locator('#opponent').select_option('claude')
    assert '没有同一模型' in frame.locator('#match-card').inner_text()
    frame.locator('#opponent').select_option('gemini')
    assert '70.8%' in frame.locator('#match-card').inner_text()
    frame.locator('#next').click()
    assert '视觉支路' in frame.locator('#step-card').inner_text()
    frame.locator('#next').focus()
    page.keyboard.press('Enter')
    assert '内存与历史支路' in frame.locator('#step-card').inner_text()
    frame.locator('#step').select_option('4')
    assert '持键' in frame.locator('#step-card').inner_text()
    frame.locator('#model').focus()
    page.keyboard.press('End')
    page.keyboard.press('Enter')
    assert frame.locator('#model').input_value() == 'gpt'
    page.keyboard.press('Escape')
    frame.locator('#next').focus()
    result['interaction'] = {'pair_values_and_conflicts': 'pass', 'same_model_guard': 'pass', 'pointer_and_keyboard': 'pass', 'six_steps': 6}
    page.locator('iframe').scroll_into_view_if_needed()
    page.screenshot(path='/tmp/opencode/lm-fight-explorer.png')
    page.set_viewport_size({'width': 390, 'height': 844})
    assert not page.evaluate('document.documentElement.scrollWidth>innerWidth')
    child = page.frames[1]
    assert not child.evaluate('document.documentElement.scrollWidth>innerWidth')
    frame.locator('#opponent').select_option('q72')
    assert '68.3%' in frame.locator('#match-card').inner_text()
    page.locator('iframe').scroll_into_view_if_needed()
    page.screenshot(path='/tmp/opencode/lm-fight-mobile.png')
    result['mobile'] = {'width': 390, 'document_overflow': False, 'iframe_overflow': False, 'controls': 'pass'}
    page.emulate_media(media='print')
    assert page.locator('h2').count() == 13
    result['print'] = {'core_chapters_present': 13, 'interactive_table': 'visible in expanded tested view'}
    page.pdf(path='/tmp/opencode/lm-fight-print.pdf', format='A4', print_background=True)
    context = browser.new_context(java_script_enabled=False, viewport={'width': 390, 'height': 844})
    nojs = context.new_page()
    nojs.goto((root / 'index.html').as_uri())
    assert nojs.locator('h2').count() == 13
    assert '本文未给出核心理论推导' in nojs.locator('body').inner_text()
    assert '9/15' in nojs.locator('body').inner_text()
    assert not nojs.evaluate('document.documentElement.scrollWidth>innerWidth')
    result['without_javascript'] = 'all core chapters and evidence readable'
    result['uncaught_errors'] = errors
    result['external_resource_requests'] = remote
    assert not errors, errors
    assert not remote, remote
    browser.close()
print(json.dumps(result, ensure_ascii=False, indent=2))
