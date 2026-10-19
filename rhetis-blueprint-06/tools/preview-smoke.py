import asyncio,threading,functools,json
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
class Q(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
async def main():
 srv=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Q,directory=str(ROOT)));threading.Thread(target=srv.serve_forever,daemon=True).start();base='http://127.0.0.1:'+str(srv.server_port)+'/'
 errors=[];checks=[]
 async with async_playwright() as pw:
  b=await pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);p=await b.new_page(viewport={'width':1600,'height':1000});p.on('pageerror',lambda e:errors.append(str(e)));p.on('response',lambda r:errors.append(str(r.status)+' '+r.url) if r.status>=400 else None)
  await p.goto(base+'index.html');await p.locator('iframe').wait_for();await p.wait_for_timeout(200)
  for deck in ['042','044','045','046','047','048']:
   await p.select_option('#deck',deck);count=await p.locator('#slides button').count();checks.append({'deck':deck,'slides':count})
   for mode in ['assembly','reference','replica']:
    await p.click('[data-mode="'+mode+'"]');await p.wait_for_timeout(120)
   await p.keyboard.press('ArrowRight');await p.wait_for_timeout(120)
  await p.click('#pair');await p.locator('#compare img').wait_for();await p.locator('#compare img').evaluate('i=>i.decode()');await p.screenshot(path=str(ROOT/'review/preview-browser.jpg'))
  for mode in ['light','dark']:
   await p.goto(base+'build/library/'+mode+'.html');await p.evaluate('document.fonts.ready');checks.append({'library':mode,'fixtures':await p.locator('article').count()})
  await b.close()
 srv.shutdown();out={'success':not errors,'errors':errors,'checks':checks};(ROOT/'review/preview-smoke.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(json.dumps(out,ensure_ascii=False,indent=2))
asyncio.run(main())
