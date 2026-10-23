from pathlib import Path
import asyncio,json
from playwright.async_api import async_playwright
from PIL import Image
B=Path(__file__).parent
ORIG=Path('/workspace/work/deck/miricanvas_기업_selected/054_1lfjn_검정_모던_회사소개서_기획서')
async def render(kind='replica'):
 report=[]
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  page=await browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for f in sorted((B/kind).glob('slide_*.html')):
   await page.goto('http://127.0.0.1:8765/cinder-pulse-review/'+kind+'/'+f.name)
   await page.evaluate('document.fonts.ready');await page.wait_for_timeout(80)
   await page.screenshot(path=str(f.with_suffix('.png')))
   result=await page.evaluate('''() => ({font:document.fonts.check('16px "Pretendard Variable"'), width:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,overflow:[...document.querySelectorAll('.text')].filter(e=>e.scrollHeight>e.clientHeight+1&&e.clientHeight>0).length})''')
   report.append(dict(page=f.name,**result))
   compare=B/('compare-'+kind);compare.mkdir(exist_ok=True)
   a=Image.open(ORIG/(f.stem+'.png')).convert('RGB');b=Image.open(f.with_suffix('.png')).convert('RGB');c=Image.new('RGB',(2560,720));c.paste(a,(0,0));c.paste(b,(1280,0));c.save(compare/(f.stem+'.png'))
  await browser.close()
 ims=[Image.open(f).convert('RGB') for f in sorted((B/kind).glob('slide_*.png'))];ims[0].save(B/kind/(kind+'.pdf'),save_all=True,append_images=ims[1:],resolution=96)
 (B/(kind+'-audit.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':
 import sys;asyncio.run(render(sys.argv[1] if len(sys.argv)>1 else 'replica'))
