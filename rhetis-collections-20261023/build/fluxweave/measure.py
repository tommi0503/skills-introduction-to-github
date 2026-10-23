import asyncio,json
from playwright.async_api import async_playwright
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=await b.new_page(viewport={'width':1280,'height':720})
  for n in [5,7,11,18]:
   await pg.goto(f'http://127.0.0.1:8762/reassembled/slide_{n:02}.html');await pg.evaluate('document.fonts.ready');print(n,await pg.evaluate('''()=>[...document.querySelectorAll('.body,.body>.group,.tablebox,.tablebox th,.tablebox tr:first-child td,.frame,.frame>.seat,.card .parts>.name,.card .parts>.note,.track .stop')].map(x=>({t:x.className,text:x.textContent.slice(0,14),box:[x.getBoundingClientRect().x,x.getBoundingClientRect().y,x.getBoundingClientRect().width,x.getBoundingClientRect().height],display:getComputedStyle(x).display}))'''))
  await b.close()
asyncio.run(main())
