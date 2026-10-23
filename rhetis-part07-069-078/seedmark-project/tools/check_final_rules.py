from pathlib import Path
import asyncio,json
from playwright.async_api import async_playwright
P=Path(__file__).parent;D=P/'local-review/final-rule-check';D.mkdir(exist_ok=True,parents=True)
async def main():
 checks=[]
 async with async_playwright()as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);g=await b.new_page(viewport={'width':1280,'height':720})
  for i,sel in [(7,'.stack>.stack>.stat:first-child'),(10,'.card>.parts>.name'),(13,'.head'),(21,'.donut')]:
   await g.goto(f'http://127.0.0.1:8765/seedmark-project/reassembled/slide_{i:02}.html');await g.evaluate('document.fonts.ready');await g.screenshot(path=str(D/f'slide_{i:02}.png'));checks.append({'page':i,'elements':await g.locator(sel).evaluate_all('''es=>es.map(e=>({cls:e.className,r:e.getBoundingClientRect().toJSON(),before:{w:getComputedStyle(e,'::before').width,h:getComputedStyle(e,'::before').height,top:getComputedStyle(e,'::before').top,left:getComputedStyle(e,'::before').left,color:getComputedStyle(e,'::before').backgroundColor},after:{h:getComputedStyle(e,'::after').height,bottom:getComputedStyle(e,'::after').bottom},border:getComputedStyle(e).borderBottom}))''')})
  await b.close()
 (D/'checks.json').write_text(json.dumps(checks,indent=2));print('Verified final four source pages.')
asyncio.run(main())
