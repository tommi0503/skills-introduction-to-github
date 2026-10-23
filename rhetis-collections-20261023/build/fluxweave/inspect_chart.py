import asyncio,json
from playwright.async_api import async_playwright
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=await b.new_page(viewport={'width':1280,'height':720});await pg.goto('http://127.0.0.1:8762/library/light.html')
  print(await pg.locator('[data-el="fluxweave-chart-line"]').first.locator('.pt').evaluate_all('''es=>es.slice(0,4).map(e=>{let a=getComputedStyle(e.querySelector('b'),'::before'),b=getComputedStyle(e,'::after');return {v:e.style.getPropertyValue('--v'),before:[a.left,a.right,a.top,a.bottom,a.height,a.backgroundImage],after:[b.left,b.right,b.top,b.bottom,b.height]}})'''))
  await b.close()
asyncio.run(main())
