import asyncio,json
from playwright.async_api import async_playwright
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=await b.new_page();await page.goto('http://127.0.0.1:8765/cinder-pulse-review/library/chart-line-light.html')
  print(await page.evaluate('''()=>[...document.querySelectorAll('.lines')][0].outerHTML'''))
  print(await page.evaluate('''()=>[...document.querySelectorAll('.lines')][0].querySelector('.pt:nth-child(2)').getBoundingClientRect().toJSON()'''))
  print(await page.evaluate('''()=>[...document.querySelectorAll('.lines')][0].querySelector('.pt:nth-child(2) b').getBoundingClientRect().toJSON()'''))
  print(await page.evaluate('''()=>{const e=[...document.querySelectorAll('.lines')][0].querySelector('.pt:nth-child(2)');const s=getComputedStyle(e,'::after');return Object.fromEntries(['left','right','top','bottom','width','height','background','content'].map(k=>[k,s.getPropertyValue(k)]))}'''))
  await b.close()
asyncio.run(main())
