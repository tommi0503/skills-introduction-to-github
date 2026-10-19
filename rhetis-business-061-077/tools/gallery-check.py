import asyncio,functools,json,threading
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
async def main():
 server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT)));threading.Thread(target=server.serve_forever,daemon=True).start()
 async with async_playwright() as pw:
  browser=await pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=await browser.new_page(viewport={'width':1280,'height':720});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  await page.goto(f'http://127.0.0.1:{server.server_port}/preview.html')
  count=await page.locator('.tile').count();assert count==117
  await page.select_option('select','077');assert await page.locator('.tile:visible').count()==2
  await page.click('[data-mode="assembly"]');await page.locator('.tile:visible').first.click();assert await page.locator('dialog').evaluate('(d)=>d.open')
  await page.keyboard.press('ArrowRight');assert 'slide_02' in await page.locator('dialog .bar span').inner_text()
  await page.keyboard.press('ArrowRight');assert 'slide_01' in await page.locator('dialog .bar span').inner_text()
  await page.keyboard.press('Escape');assert not await page.locator('dialog').evaluate('(d)=>d.open')
  await page.click('[data-mode="comparison"]');await page.locator('.tile:visible').first.click();await page.wait_for_function('document.querySelector("dialog img").complete && document.querySelector("dialog img").naturalWidth===2560')
  assert not errors
  (ROOT/'review/gallery-check.json').write_text(json.dumps({'tiles':count,'deck077Visible':2,'modeSwitch':True,'dialog':True,'keyboardFilteredWrap':True,'comparisonNaturalWidth':2560,'errors':errors},indent=2))
  print('Gallery checks passed');await browser.close()
 server.shutdown()
asyncio.run(main())
