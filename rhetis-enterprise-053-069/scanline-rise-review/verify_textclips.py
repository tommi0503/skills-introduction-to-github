from pathlib import Path
from playwright.sync_api import sync_playwright
import json
R=Path(__file__).parent;found=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);page=b.new_page(viewport={'width':1280,'height':720})
 for kind in ['replica','reassembled']:
  for i in range(1,19):
   page.goto(f'http://127.0.0.1:8765/scanline-rise-review/{kind}/slide-{i:02}.html?clips=1');page.evaluate('document.fonts.ready')
   a=page.evaluate('''()=>{let bad=[];for(let e of document.querySelectorAll('p,li,h1,h2,.name,.note,.fig')){if(!e.getClientRects().length||getComputedStyle(e).display==='none')continue;let r=document.createRange();r.selectNodeContents(e);let rects=[...r.getClientRects()];for(let x=e.parentElement;x;x=x.parentElement){let s=getComputedStyle(x);if(!['hidden','clip'].includes(s.overflowY)&&!['hidden','clip'].includes(s.overflowX))continue;let q=x.getBoundingClientRect();if(rects.some(t=>t.x<q.x-4||t.y<q.y-4||t.right>q.right+4||t.bottom>q.bottom+4)){bad.push({text:e.textContent.slice(0,90),class:e.className,ancestor:x.className});break;}}}return bad}''')
   found.append({'kind':kind,'page':i,'clips':a})
 b.close()
(R/'text-clipping-audit.json').write_text(json.dumps(found,ensure_ascii=False,indent=2));print([(a['kind'],a['page'],a['clips']) for a in found if a['clips']])
