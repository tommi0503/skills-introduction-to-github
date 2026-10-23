from playwright.sync_api import sync_playwright
from pathlib import Path
import json,re
R=Path(__file__).parent
AUD=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720})
 for mode in ['light','dark']:
  page.goto(f'http://127.0.0.1:8765/halo-field-review/library/{mode}.html');page.evaluate('document.fonts.ready')
  result=page.evaluate('''()=>{const out=[];for(const a of document.querySelectorAll('article')){const name=a.querySelector('h2').textContent,body=a.querySelector('.body');if(!body)continue;const root=body.firstElementChild;const ms=[...name.matchAll(/(\\d+)x(\\d+)/g)].map(m=>[+m[1],+m[2]]);for(const [w,h]of [...ms,[12,6]]){root.style.gridColumn='1 / span '+w;root.style.gridRow='1 / span '+h;void root.offsetHeight;const bad=[...root.querySelectorAll('[data-el]'),...(root.matches('[data-el]')?[root]:[])].filter(e=>e.clientHeight>0&&e.clientWidth>0&&(e.scrollWidth>e.clientWidth+3||e.scrollHeight>e.clientHeight+3)).map(e=>({element:e.dataset.el,c:[e.clientWidth,e.clientHeight],s:[e.scrollWidth,e.scrollHeight]}));out.push({fixture:name,grid:[w,h],bad});}root.style.gridColumn='1 / span 12';root.style.gridRow='1 / span 6';}return out}''')
  AUD.extend(dict(mode=mode,**x) for x in result)
 b.close()
(R/'minimum-audit.json').write_text(json.dumps(AUD,ensure_ascii=False,indent=2));print('tests',len(AUD),'overflow cases',sum(bool(a['bad']) for a in AUD))
for a in AUD:
 if a['bad']:print(a['mode'],a['fixture'],a['grid'],a['bad'][:2])
