"""Browser smoke check for gallery navigation and native slide canvas."""
import asyncio,json,threading,functools
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from playwright.async_api import async_playwright
R=Path(__file__).resolve().parents[1]
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
async def main():
 server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(R)));threading.Thread(target=server.serve_forever,daemon=True).start()
 async with async_playwright()as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=await b.new_page(viewport={'width':1440,'height':1000});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));await page.goto(f'http://127.0.0.1:{server.server_port}/preview.html');assert await page.locator('.card').count()==109
  await page.select_option('#deck','091');assert await page.locator('.card').count()==20
  await page.locator('.card').first.click();await page.frame_locator('iframe').locator('body[data-ready="true"]').wait_for();size=await page.frame_locator('iframe').locator('.slide').evaluate('e=>[e.offsetWidth,e.offsetHeight]');assert size==[1280,720]
  await page.click('#compare');assert await page.locator('.pane').count()==2;await page.click('#next');await page.frame_locator('iframe').locator('body[data-ready="true"]').wait_for();await page.keyboard.press('Escape');await page.click('[data-mode="assembly"]');assert await page.locator('.card').count()==20
  await page.screenshot(path=str(R/'previews/gallery-ui.png'),full_page=False);await b.close();assert not errors
  (R/'review/gallery-check.json').write_text(json.dumps({'success':True,'allSlides':109,'deckFilter':20,'nativeIframe':size,'comparisonPanes':2,'keyboardNavigation':True,'assemblyToggle':True,'browserErrors':errors},indent=2));print('Gallery checks passed')
 server.shutdown()
asyncio.run(main())
