import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image
P=Path(__file__).parent
S=next(Path('/workspace/work/deck').glob('*/*072*'))
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  page=await b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for f in sorted((P/'replica').glob('slide_*.html')):
   await page.goto('http://127.0.0.1:8765/seedmark-project/replica/'+f.name)
   await page.evaluate('document.fonts.ready');await page.screenshot(path=str(f.with_suffix('.png')))
   with Image.open(S/f.with_suffix('.png').name) as src,Image.open(f.with_suffix('.png'))as rep:
    out=Image.new('RGB',(2560,720),'white');out.paste(src,(0,0));out.paste(rep,(1280,0));(P/'compare-replica').mkdir(exist_ok=True);out.save(P/'compare-replica'/f.with_suffix('.png').name)
  await b.close()
asyncio.run(main())
