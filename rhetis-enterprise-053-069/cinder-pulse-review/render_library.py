from pathlib import Path
import asyncio,json,re
from PIL import Image
from playwright.async_api import async_playwright
B=Path(__file__).parent;L=B/'library'
async def run():
 report=[]
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  page=await b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for f in sorted(L.glob('*.html')):
   if f.stem in ['light','dark']:continue
   await page.goto('http://127.0.0.1:8765/cinder-pulse-review/library/'+f.name);await page.evaluate('document.fonts.ready')
   await page.screenshot(path=str(f.with_suffix('.png')))
   data=await page.evaluate('''()=>({fonts:document.fonts.check('18px "Pretendard Variable"'),slides:[...document.querySelectorAll('.slide')].map(e=>({width:e.offsetWidth,height:e.offsetHeight})),textOverflow:[...document.querySelectorAll('[data-el] .name,[data-el] .note,[data-el] .fig')].filter(e=>e.clientHeight>0&&e.scrollHeight>e.clientHeight+2).map(e=>e.className)})''')
   report.append(dict(sheet=f.stem,**data))
  await b.close()
 for mode in ['light','dark']:
  ims=[Image.open(f).convert('RGB') for f in sorted(L.glob('*-'+mode+'.png'))];ims[0].save(L/f'library-{mode}.pdf',save_all=True,append_images=ims[1:],resolution=96)
 (B/'library-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 print('rendered sheets',len(report))
asyncio.run(run())
