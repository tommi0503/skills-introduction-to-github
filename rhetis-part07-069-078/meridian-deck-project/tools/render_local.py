import asyncio,json
from pathlib import Path
from PIL import Image
from playwright.async_api import async_playwright
P=Path(__file__).parent
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  page=await b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  out=P/'replica-pass1';out.mkdir(exist_ok=True)
  errors=[]
  for f in sorted((P/'replica').glob('slide_*.html')):
   await page.goto('http://127.0.0.1:8765/meridian-deck-project/replica/'+f.name);await page.evaluate('document.fonts.ready')
   await page.screenshot(path=str(out/f.with_suffix('.png').name))
   original=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('074*/'+f.with_suffix('.png').name))
   canvas=Image.new('RGB',(2560,720),'white');canvas.paste(Image.open(original),(0,0));canvas.paste(Image.open(out/f.with_suffix('.png').name),(1280,0));canvas.save(out/('compare-'+f.with_suffix('.png').name))
   bad=await page.evaluate('''()=>[...document.querySelectorAll('.txt')].filter(e=>{let r=e.getBoundingClientRect();return r.right>1281||r.bottom>721||r.left<0||r.top<0}).map(e=>e.textContent.slice(0,35))''')
   if bad:errors.append([f.name,bad])
  (P/'replica-pass1-checks.json').write_text(json.dumps(errors,ensure_ascii=False,indent=2));print('30 screenshots; overflows',errors)
  await b.close()
asyncio.run(main())
