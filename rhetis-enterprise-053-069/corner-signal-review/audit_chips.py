from pathlib import Path
from playwright.sync_api import sync_playwright
import json
R=Path(__file__).parent;results=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);a=b.new_page(viewport={'width':1280,'height':720})
 for mode in ['light','dark']:
  a.goto(f'http://127.0.0.1:8765/corner-signal-review/library/{mode}.html');a.evaluate('document.fonts.ready')
  rs=a.evaluate('''()=>[...document.querySelectorAll('.pill[data-el="corner-signal-pill"],.tag[data-el="corner-signal-tag"]')].map(e=>{let b=e.getBoundingClientRect(),s=getComputedStyle(e),t=e.querySelector('.parts')||e,r=t.getBoundingClientRect();return {el:e.dataset.el,text:e.innerText,box:[b.width,b.height],contentCenter:[(r.left+r.right-b.left-b.right)/2,(r.top+r.bottom-b.top-b.bottom)/2],align:s.alignItems,justify:s.justifyContent,overflow:e.scrollWidth>e.clientWidth+2||e.scrollHeight>e.clientHeight+2}})''')
  results.extend(dict(mode=mode,**r) for r in rs)
 b.close()
(R/'chip-audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print(len(results),'chips',sum(x['overflow'] for x in results),'overflow')
