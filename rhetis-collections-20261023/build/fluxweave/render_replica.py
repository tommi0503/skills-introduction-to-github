import asyncio,json
from pathlib import Path
from PIL import Image,ImageDraw
from playwright.async_api import async_playwright
W=Path('/workspace/output/fluxweave-review'); D=Path('/workspace/work/deck/miricanvas_기업_selected/002_1leen_파랑_미니멀_기업소개서_기획서')
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']); page=await b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  checks=[]
  for f in sorted((W/'replica').glob('slide_*.html')):
   await page.goto('http://127.0.0.1:8762/'+str(f.relative_to(W)));await page.evaluate('document.fonts.ready');await page.screenshot(path=str(f.with_suffix('.png')))
   checks.append({'page':f.name,'font':await page.evaluate("document.fonts.check('16px \"Pretendard Variable\"')"),'size':await page.locator('.slide').bounding_box()})
   out=Image.new('RGB',(2560,720),'white');out.paste(Image.open(D/f.with_suffix('.png').name),(0,0));out.paste(Image.open(f.with_suffix('.png')),(1280,0));out.save(W/'compare-replica'/f.with_suffix('.png').name)
  await b.close()
 (W/'replica-checks.json').write_text(json.dumps(checks,indent=2))
 ims=[Image.open(f).convert('RGB') for f in sorted((W/'replica').glob('slide_*.png'))];ims[0].save(W/'replica'/'replica.pdf',save_all=True,append_images=ims[1:],resolution=96)
asyncio.run(main())
