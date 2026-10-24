from pathlib import Path
import json
from playwright.sync_api import sync_playwright
P=Path(__file__).parent;report=[]
with sync_playwright() as q:
 b=q.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720})
 for n in range(1,31):
  page.goto(f'http://127.0.0.1:8875/crossrail-project/replica/slide_{n:02}.html');page.evaluate('document.fonts.ready');report.append({'page':n,'fragments':page.evaluate('''()=>[...document.querySelectorAll('.slide b,.slide strong,.slide span,.slide small')].filter(e=>e.textContent.trim()).map(e=>{let s=getComputedStyle(e),p=getComputedStyle(e.parentElement),r=e.getBoundingClientRect();return {tag:e.tagName,text:e.textContent.trim(),bbox:[r.x,r.y,r.width,r.height],font:s.fontFamily,size:s.fontSize,weight:s.fontWeight,parentSize:p.fontSize,parentWeight:p.fontWeight}}).filter(r=>r.bbox[2]>0&&r.bbox[3]>0&&(r.size!==r.parentSize||r.weight!==r.parentWeight))''')})
 b.close()
(P/'fragment-measurements.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('nested font fragments',sum(len(p['fragments']) for p in report));print([(p['page'],[(x['text'][:20],x['size'],x['parentSize']) for x in p['fragments']]) for p in report if p['page'] in [9,10,21,22]])
