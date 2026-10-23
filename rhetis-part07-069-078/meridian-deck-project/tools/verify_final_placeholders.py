from pathlib import Path
import json,hashlib,importlib.util
from playwright.sync_api import sync_playwright
P=Path(__file__).parent;C=P/'meridian-deck';B=P.parent;R=Path('/workspace/work/reference')
def snapshot():return {str(f.relative_to(C)):hashlib.sha256(f.read_bytes()).hexdigest() for f in C.rglob('*') if f.is_file()}
start=snapshot();out={'pages':[],'generic':[]}
s=importlib.util.spec_from_file_location('pv',R/'tools/preview.py');pv=importlib.util.module_from_spec(s);s.loader.exec_module(pv)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page(viewport={'width':1280,'height':720})
 for n in range(1,31):
  q.goto(f'http://127.0.0.1:8765/meridian-deck-project/reassembled/slide_{n:02d}.html');q.evaluate('document.fonts.ready');seats=q.locator('[data-ph]').evaluate_all('es=>es.map(e=>({ph:e.dataset.ph,cl:e.className,before:getComputedStyle(e,"::before").content,after:getComputedStyle(e,"::after").content}))');bad=[x for x in seats if x['before'].strip('"')==x['ph'] or x['after'].strip('"')==x['ph']];out['pages'].append({'page':n,'placeholders':len(seats),'visibleIndices':bad})
  if n in [27,29]:q.screenshot(path=str(B/'qa'/f'meridian-placeholder-final-{n}.png'))
 for dark in [False,True]:
  q.goto('http://127.0.0.1:8765/qa/probe.html');m=pv.sheet(C,json.loads((R/'contract/type-steps.json').read_text()),json.loads((R/'contract/palette.json').read_text()),dark=dark,fonts_href='/meridian-deck-project/assets/fonts/fonts.css');q.set_content(m,wait_until='networkidle');q.evaluate('document.fonts.ready')
  result=q.evaluate('''()=>[...document.querySelectorAll('article')].filter(a=>/^(image-frame|person) \/ /.test(a.querySelector('h2').textContent)).flatMap(a=>[...a.querySelectorAll('[data-ph]')].map(e=>({fixture:a.querySelector('h2').textContent,ph:e.dataset.ph,before:getComputedStyle(e,'::before').content})))''');out['generic'].append({'mode':'dark' if dark else 'light','checks':result})
 b.close()
out['sourceUnchanged']=start==snapshot();out['sourceSha256']=hashlib.sha256(json.dumps(start,sort_keys=True).encode()).hexdigest();(B/'qa/meridian-deck-placeholder-final-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print('Source pages checked',len(out['pages']),'visible indices',sum(len(x['visibleIndices']) for x in out['pages']),'source unchanged',out['sourceUnchanged'],'SHA',out['sourceSha256']);print('Generic seat labels',out['generic'])
