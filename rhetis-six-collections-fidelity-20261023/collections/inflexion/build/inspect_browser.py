import asyncio,http.server,threading,functools,json
from playwright.async_api import async_playwright
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory='/workspace/work/deliverables/inflexion/review'));threading.Thread(target=server.serve_forever,daemon=True).start()
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);pg=await b.new_page(viewport={'width':1280,'height':720})
  for n,selectors in [('16',['.flowchart .node:first-child'])]:
   await pg.goto(f'http://127.0.0.1:{server.server_port}/reassembled/slide_{n}.html');await pg.evaluate('document.fonts.ready')
   print(await pg.locator('.node').first.evaluate("e=>{let c=getComputedStyle(e,'::after');return Object.fromEntries(['left','right','top','width','height','borderTop','borderRight','borderBottom','clipPath','transform','background','display','content','boxSizing'].map(k=>[k,c[k]]))}"))
  await b.close()
asyncio.run(main());server.shutdown()
