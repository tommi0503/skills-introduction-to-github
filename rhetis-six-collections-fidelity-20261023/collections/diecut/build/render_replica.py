import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image
import fitz
R=Path('/workspace/work/deliverables/diecut');D=Path('/workspace/work/deck/miricanvas_기업_selected/012_1k9n1_은색_미니멀_협동로봇_솔루션_제안서')
async def main():
 out=[]
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
  page=await browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for n in range(1,20):
   f=R/'review/replica'/f'slide-{n:02}.html';await page.goto(f.as_uri());await page.evaluate('document.fonts.ready');await page.screenshot(path=str(f.with_suffix('.png')))
   issues=await page.evaluate('''()=>({font:document.fonts.check('20px p'),size:[document.documentElement.clientWidth,document.documentElement.clientHeight],overflow:[...document.querySelectorAll('.tx')].filter(e=>e.scrollHeight>e.clientHeight+1 || e.scrollWidth>e.clientWidth+1).map(e=>e.textContent.slice(0,80))})''');out.append({'page':n,**issues})
   a=Image.open(D/f'slide_{n:02}.png').convert('RGB');b=Image.open(f.with_suffix('.png')).convert('RGB');c=Image.new('RGB',(2560,720));c.paste(a,(0,0));c.paste(b,(1280,0));c.save(R/'review/compare-replica'/f'slide-{n:02}.png')
  await browser.close()
 (R/'review/replica/automated-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
 doc=fitz.open()
 for n in range(1,20):
  p=doc.new_page(width=1280,height=720);p.insert_image(p.rect,filename=str(R/'review/replica'/f'slide-{n:02}.png'))
 doc.save(R/'review/replica/replica.pdf')
 print(json.dumps(out,ensure_ascii=False))
asyncio.run(main())
