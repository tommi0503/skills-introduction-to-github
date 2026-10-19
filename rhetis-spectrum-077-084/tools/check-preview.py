import asyncio,threading,functools,json
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from html.parser import HTMLParser
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
 def __init__(self):super().__init__();self.paths=[]
 def handle_starttag(self,t,attrs):
  d=dict(attrs)
  for k in ['href','src']:
   if k in d and not d[k].startswith(('#','https:','http:','data:')):self.paths.append(d[k])
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
async def main():
 doc=Links();doc.feed((ROOT/'preview.html').read_text());missing=[p for p in doc.paths if not(ROOT/p).exists()];server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT)));threading.Thread(target=server.serve_forever,daemon=True).start();base=f'http://127.0.0.1:{server.server_port}/';result={'missingLinks':missing,'localLinkCount':len(doc.paths),'browserErrors':[]}
 async with async_playwright()as pw:
  browser=await pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=await browser.new_page(viewport={'width':1280,'height':720});page.on('pageerror',lambda e:result['browserErrors'].append(str(e)))
  await page.goto(base+'preview.html');await page.evaluate("async()=>{for(const i of document.images)i.loading='eager';await Promise.all(Array.from(document.images).map(i=>i.decode()))}");result['gallery']=await page.evaluate("()=>({images:document.images.length,failed:Array.from(document.images).filter(i=>i.naturalWidth!==1280||i.naturalHeight!==720).map(i=>i.src)})")
  await page.locator('article a.image').first.click();await page.wait_for_selector('body[data-ready="true"]');result['openSlide']=await page.locator('.slide').evaluate('e=>({width:e.offsetWidth,height:e.offsetHeight})')
  for mode in ['light','dark']:
   await page.goto(base+f'build/library/{mode}.html');await page.evaluate('document.fonts.ready');result['library-'+mode]=await page.evaluate("()=>({fixtures:document.querySelectorAll('article').length,fontReady:document.fonts.check('700 20px Pretendard'),pageColor:getComputedStyle(document.querySelector('.slide')).getPropertyValue('--page').trim()})")
  await browser.close()
 server.shutdown();result['success']=not missing and not result['browserErrors'] and result['gallery']['images']==106 and not result['gallery']['failed'] and all(result['library-'+m]['fixtures']==sum(1 for _ in (ROOT/'collection/rhetis-spectrum').glob('**/fixtures/*.html')) and result['library-'+m]['fontReady']for m in ['light','dark']);(ROOT/'review/preview-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2));assert result['success']
asyncio.run(main())
