#!/usr/bin/env python3
"""Build the reference preview.sheet API outputs and inspect all fourteen pages.

This standard12x6 overview supplements the separately reviewed native size sheets.
It never changes collection sources or review/sheets/ files.
"""
from __future__ import annotations

import argparse
from functools import partial
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path
import threading
import time

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT.parent / 'reference'
NAMES = ('tide-tab', 'cutfield', 'filament', 'portico', 'toggle-grid', 'lamella', 'rulemark')


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inputs(name: str) -> dict[str, str]:
    collection = ROOT / name / name
    paths = sorted(p for p in collection.rglob('*') if p.is_file() and p.suffix in ('.css', '.json', '.html'))
    paths += [REFERENCE / 'tools/preview.py', REFERENCE / 'contract/type-steps.json',
              REFERENCE / 'contract/palette.json']
    paths += sorted((ROOT / name / 'review/assets/fonts').glob('*'))
    return {str(p): digest(p) for p in paths if p.is_file()}


def fixtures(name: str) -> list[str]:
    collection = ROOT / name / name
    folders = [('foundation', collection / 'foundation')]
    folders += [(p.name, p) for p in sorted((collection / 'elements').iterdir()) if p.is_dir()]
    return [f'{leaf} / {p.stem}' for leaf, folder in folders for p in sorted((folder / 'fixtures').glob('*.html'))]


def build(name: str, preview) -> dict:
    collection = ROOT / name / name
    review = ROOT / name / 'review'
    fonts = review / 'assets/fonts/fonts.css'
    if not fonts.is_file():
        raise RuntimeError(f'Missing local font sheet: {fonts}')
    steps = json.loads((REFERENCE / 'contract/type-steps.json').read_text())
    palette = json.loads((REFERENCE / 'contract/palette.json').read_text())
    snapshot = inputs(name)
    outputs = {}
    for mode in ('light', 'dark'):
        path = review / f'{mode}.html'
        html = preview.sheet(collection, steps, palette, dark=mode == 'dark', fonts_href='assets/fonts/fonts.css')
        path.write_text(html, encoding='utf-8', newline='\n')
        outputs[mode] = {'path': path, 'sha256': digest(path)}
    if inputs(name) != snapshot:
        raise RuntimeError(f'Source changed while building standard preview: {name}')
    return {'source_hashes': snapshot, 'outputs': outputs, 'fixtures': fixtures(name)}


INSPECT = r'''() => {
 const articles=[...document.querySelectorAll('body > article')];
 const titles=articles.map(a=>{
   let h=a.querySelector(':scope > h2').cloneNode(true);
   h.querySelectorAll('small').forEach(e=>e.remove());
   return h.textContent.trim();
 });
 const slides=[...document.querySelectorAll('article .frame > .slide')];
 const slideSizes=slides.map((s,i)=>{let c=getComputedStyle(s),r=s.getBoundingClientRect();
   return {fixture:titles[i],layout:[s.offsetWidth,s.offsetHeight],computed:[parseFloat(c.width),parseFloat(c.height)],
     displayed:[r.width,r.height],dark:s.classList.contains('dark')};});
 const fontGroups=new Map();
 const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
 while(walker.nextNode()){
   let n=walker.currentNode,e=n.parentElement,t=n.textContent.trim();
   if(!t||!e.closest('article .slide')||['SCRIPT','STYLE'].includes(e.tagName))continue;
   let s=getComputedStyle(e);
   if(s.display==='none'||s.visibility==='hidden'||!e.getClientRects().length)continue;
   let script=/[가-힣]/.test(t)?'ko':/[a-z]/i.test(t)?'latin':'other';
   let key=s.fontFamily+'|'+s.fontWeight+'|'+s.fontStyle+'|'+script;
   if(fontGroups.has(key))continue;
   const descriptor=s.fontStyle+' '+s.fontWeight+' '+s.fontSize+' '+s.fontFamily;
   fontGroups.set(key,{family:s.fontFamily,weight:s.fontWeight,style:s.fontStyle,script,
     sample:t.slice(0,80),descriptor,loaded:document.fonts.check(descriptor,t.slice(0,80))});
 }
 const fontFaces=[...document.fonts].map(f=>({family:f.family,status:f.status,weight:f.weight,style:f.style}));
 return {article_count:articles.length,slide_count:slides.length,titles,slides:slideSizes,
   size_errors:slideSizes.filter(s=>s.layout[0]!==1280||s.layout[1]!==720||s.computed[0]!==1280||s.computed[1]!==720),
   font_faces:fontFaces,font_checks:[...fontGroups.values()],
   font_load_errors:fontFaces.filter(f=>f.status==='error'),
   font_check_errors:[...fontGroups.values()].filter(f=>!f.loaded),
   fonts_href:document.querySelector('link[rel="stylesheet"]')?.getAttribute('href'),
   icons:[...document.querySelectorAll('.slide [data-icon]')].length};
}'''


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


def run(names: list[str]) -> list[dict]:
    spec = importlib.util.spec_from_file_location('rhetis_reference_preview', REFERENCE / 'tools/preview.py')
    preview = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(preview)
    built = {name: build(name, preview) for name in names}
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Quiet, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    reports = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path='/usr/bin/chromium', args=[
                '--no-sandbox', '--disable-crash-reporter', '--disable-breakpad'])
            for name in names:
                report = {'collection': name, 'generator': 'reference/tools/preview.py:sheet',
                          'font_href': 'assets/fonts/fonts.css', 'expected_fixtures': len(built[name]['fixtures']),
                          'source_hashes': built[name]['source_hashes'], 'modes': [], 'issues': []}
                for mode in ('light', 'dark'):
                    context = browser.new_context(viewport={'width': 1360, 'height': 900}, device_scale_factor=1)
                    page = context.new_page()
                    failures, bad_responses, errors, requests = [], [], [], []
                    page.on('requestfailed', lambda req: failures.append({'url': req.url, 'failure': req.failure}))
                    page.on('response', lambda res: bad_responses.append({'url': res.url, 'status': res.status}) if res.status >= 400 else None)
                    page.on('request', lambda req: requests.append(req.url))
                    page.on('pageerror', lambda err: errors.append(str(err)))
                    page.goto(f'http://127.0.0.1:{server.server_port}/{name}/review/{mode}.html?v={time.time_ns()}', wait_until='networkidle', timeout=120000)
                    page.evaluate('document.fonts.ready')
                    qa = page.evaluate(INSPECT)
                    qa.update(mode=mode, html_sha256=built[name]['outputs'][mode]['sha256'],
                              request_failures=failures, http_errors=bad_responses, script_errors=errors,
                              external_requests=[u for u in requests if not u.startswith(f'http://127.0.0.1:{server.server_port}/')])
                    if qa['titles'] != built[name]['fixtures']:
                        report['issues'].append(f'{mode}: fixture list/count mismatch')
                    if qa['slide_count'] != report['expected_fixtures']:
                        report['issues'].append(f'{mode}: slide count mismatch')
                    if qa['size_errors']:
                        report['issues'].append(f'{mode}: slides are not1280x720')
                    if qa['font_load_errors'] or qa['font_check_errors']:
                        report['issues'].append(f'{mode}: document.fonts failure')
                    if failures or bad_responses or errors or qa['external_requests']:
                        report['issues'].append(f'{mode}: browser/resource errors')
                    if any(s['dark'] != (mode == 'dark') for s in qa['slides']):
                        report['issues'].append(f'{mode}: mode class mismatch')
                    if qa['fonts_href'] != report['font_href']:
                        report['issues'].append(f'{mode}: nonportable font href')
                    report['modes'].append(qa)
                    context.close()
                if inputs(name) != built[name]['source_hashes']:
                    report['issues'].append('collection/shared source changed during browser validation')
                report['passed'] = not report['issues']
                out = ROOT / name / 'review/validation/standard-preview.json'
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
                reports.append(report)
                print(name, 'fixtures', report['expected_fixtures'], 'modes2', 'passed', report['passed'], report['issues'], flush=True)
            browser.close()
    finally:
        server.shutdown()
    return reports


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('collections', nargs='*', choices=NAMES)
    args = parser.parse_args()
    reports = run(args.collections or list(NAMES))
    raise SystemExit(0 if all(r['passed'] for r in reports) else 1)
