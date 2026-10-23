import asyncio,json
from playwright.async_api import async_playwright
async def main():
 async with async_playwright()as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);g=await b.new_page(viewport={'width':1280,'height':720})
  for i,selector in [(7,'.stat,.stat .note'),(13,'.card,.card>.parts,.bars,.legend'),(14,'.body>.group>.stack,.areas,.lines,.bars,.prose'),(15,'.body>.stack,.headline,.list,.list>.item'),(16,'.venn,.venn>.set,.venn>.core'),(17,'.track,.tag'),(18,'.prose,.prose>p')]:
   await g.goto(f'http://127.0.0.1:8765/seedmark-project/reassembled/slide_{i:02}.html');await g.evaluate('document.fonts.ready');print(i,json.dumps(await g.locator(selector).evaluate_all('''es=>es.map(e=>({cl:e.className,text:e.innerText.slice(0,60),x:e.getBoundingClientRect().x,y:e.getBoundingClientRect().y,w:e.getBoundingClientRect().width,h:e.getBoundingClientRect().height,font:getComputedStyle(e).fontSize,line:getComputedStyle(e).lineHeight,pad:getComputedStyle(e).padding,flex:getComputedStyle(e).flex}))'''),ensure_ascii=False))
  await b.close()
asyncio.run(main())
