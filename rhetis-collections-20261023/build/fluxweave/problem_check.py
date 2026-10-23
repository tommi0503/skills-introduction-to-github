import asyncio,json,re
from pathlib import Path
from playwright.async_api import async_playwright
O=Path('/workspace/output/fluxweave')
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=await b.new_page(viewport={'width':1280,'height':720});await pg.goto('http://127.0.0.1:8762/library/light.html');await pg.add_style_tag(content=''.join(x.read_text() for x in O.glob('elements/*/element.css')))
  for f in ['matrix/fixtures/swot.html','person/fixtures/person.html','tag/fixtures/extended.html']:
   raw=(O/'elements'/f).read_text();await pg.evaluate('s=>document.body.innerHTML=s','<section class="slide"><div class="page"><div class="body">'+raw+'</div></div></section>')
   print(f,await pg.locator('.body *').evaluate_all('''es=>es.map(e=>{let r=e.getBoundingClientRect(),c=getComputedStyle(e);return {cls:e.className,w:r.width,h:r.height,x:r.x,y:r.y,display:c.display,align:c.alignSelf,cols:c.gridTemplateColumns}})'''))
  await b.close()
asyncio.run(main())
