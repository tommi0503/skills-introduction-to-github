from pathlib import Path
from playwright.sync_api import sync_playwright
import json
R=Path(__file__).parent
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);page=b.new_page(viewport={'width':1280,'height':720});data=[]
 for mode in ['light','dark']:
  page.goto('http://127.0.0.1:8765/scanline-rise-review/library/'+mode+'.html');page.evaluate('document.fonts.ready')
  a=page.evaluate('''()=>{let a=[];for(let e of document.querySelectorAll('[data-el].pill,[data-el].tag,[data-el] .chip,[data-el] .mark')){if(!e.getClientRects().length||e.querySelector('.icon,.seat'))continue;let st=getComputedStyle(e);if(st.display==='none')continue;let r=e.getBoundingClientRect(),range=document.createRange();range.selectNodeContents(e);let t=range.getBoundingClientRect();if(!t.width||!r.height)continue;let dx=Math.abs(t.x+t.width/2-r.x-r.width/2),dy=Math.abs(t.y+t.height/2-r.y-r.height/2);a.push({class:e.className,text:e.textContent.slice(0,40),dx:Math.round(dx*100)/100,dy:Math.round(dy*100)/100,inside:t.x>=r.x-1&&t.y>=r.y-1&&t.right<=r.right+1&&t.bottom<=r.bottom+1});}return{font:document.fonts.check('16px "Pretendard Variable"'),codeFont:document.fonts.check('16px "Nanum Gothic Coding"'),chipAudit:a}}''');a['mode']=mode;data.append(a)
 b.close()
(R/'visual-alignment-audit.json').write_text(json.dumps(data,ensure_ascii=False,indent=2));print([(a['mode'],len(a['chipAudit']),sum(not x['inside'] for x in a['chipAudit'])) for a in data])
