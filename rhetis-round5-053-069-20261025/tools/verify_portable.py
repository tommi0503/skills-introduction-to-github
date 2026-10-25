"""Render the extracted review ZIPs with only their packaged font families."""
from pathlib import Path
from zipfile import ZipFile
from PIL import Image,ImageChops
from playwright.async_api import async_playwright
import asyncio,functools,http.server,io,json,threading
ROOT=Path(__file__).resolve().parents[1]
TARGET=Path('/tmp/rhetis-round5-portable');TARGET.mkdir(exist_ok=True)
async def main():
 collections=json.loads((ROOT/'collections.json').read_text());report=[]
 for c in collections:
  out=TARGET/c['id'];out.mkdir(exist_ok=True)
  with ZipFile(ROOT/(c['id']+'-review.zip'))as z:z.extractall(out)
 server=http.server.ThreadingHTTPServer(('127.0.0.1',8768),functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(TARGET)));threading.Thread(target=server.serve_forever,daemon=True).start()
 async with async_playwright()as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);page=await browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for c in collections:
   errors=[];failed=[];page.on('pageerror',lambda e:errors.append(str(e)));page.on('requestfailed',lambda r:failed.append(r.url));count=0;previews=0
   for f in sorted((TARGET/c['id']/'reassembled').glob('*.html')):
    await page.goto('http://127.0.0.1:8768/'+c['id']+'/reassembled/'+f.name,wait_until='networkidle');await page.evaluate('document.fonts.ready')
    font=await page.evaluate("({status:document.fonts.status,errors:[...document.fonts].filter(f=>f.status==='error').map(f=>f.family)})");assert font['status']=='loaded'and not font['errors'],(c['id'],f.name,font)
    actual=Image.open(io.BytesIO(await page.screenshot())).convert('RGB');expected=Image.open(ROOT/(c['id']+'-review/reassembled')/f.with_suffix('.png').name).convert('RGB');assert ImageChops.difference(actual,expected).getbbox()is None,(c['id'],f.name,'portable render pixels differ');count+=1
   for mode in ['light','dark']:
    await page.goto('http://127.0.0.1:8768/'+c['id']+'/preview-'+mode+'.html',wait_until='networkidle');await page.evaluate('document.fonts.ready');font=await page.evaluate("({status:document.fonts.status,errors:[...document.fonts].filter(f=>f.status==='error').map(f=>f.family)})");assert font['status']=='loaded'and not font['errors'],(c['id'],mode,font);previews+=1
   assert not errors and not failed,(c['id'],errors,failed)
   report.append({'collection':c['id'],'extractedPagesPixelIdentical':count,'lightDarkPreviewsFontLoaded':previews,'fontErrors':[],'httpErrors':[]});print('Portable ZIP browser verified',c['id'],count,'pixel-identical pages; 2 previews font-loaded',flush=True);page.remove_all_listeners('pageerror');page.remove_all_listeners('requestfailed')
  await browser.close()
 server.shutdown();(ROOT/'publication-portable-verification.json').write_text(json.dumps({'method':'Actual extracted ZIP browser pages compared pixel-for-pixel against final canonical PNGs; all packaged preview font families loaded.','collections':report},ensure_ascii=False,indent=2))
if __name__=='__main__':asyncio.run(main())
