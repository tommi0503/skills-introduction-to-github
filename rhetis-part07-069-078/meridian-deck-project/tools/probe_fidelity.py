from playwright.sync_api import sync_playwright
import sys,json
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720})
 for n,sel in [(7,'.body>.stack>*'),(17,'.head,.head .title,.head .kicker'),(18,'.head,.hub>.spoke>.note')]:
  page.goto(f'http://127.0.0.1:8765/meridian-deck-project/reassembled/slide_{n:02d}.html');page.evaluate('document.fonts.ready');print('hit',n,page.evaluate('document.elementsFromPoint(150,120).map(e=>e.className)'));print(n,json.dumps(page.locator(sel).evaluate_all('(es)=>es.map(e=>{let r=e.getBoundingClientRect(),s=getComputedStyle(e);return {cl:e.className,text:e.textContent.slice(0,40),x:r.x,y:r.y,w:r.width,h:r.height,display:s.display,visibility:s.visibility,rotate:s.rotate,transform:s.transform,translate:s.translate,flex:s.flex,padding:s.padding}})'),ensure_ascii=False))
 b.close()
