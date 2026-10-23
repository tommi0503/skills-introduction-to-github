from pathlib import Path
import asyncio,json,sys
from playwright.async_api import async_playwright
from PIL import Image
P=Path(__file__).parent;D=P/'local-review'/('fidelity-'+(sys.argv[1]if len(sys.argv)>1 else'1'));D.mkdir(parents=True,exist_ok=True)
async def main():
 checks=[]
 async with async_playwright()as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=await b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for f in sorted((P/'reassembled').glob('slide_*.html')):
   await page.goto('http://127.0.0.1:8765/seedmark-project/reassembled/'+f.name);await page.evaluate('document.fonts.ready');await page.screenshot(path=str(D/(f.stem+'.png')))
   checks.append({'page':f.name,**await page.evaluate('''()=>({size:[document.documentElement.scrollWidth,document.documentElement.scrollHeight],font:document.fonts.check('18px "Noto Sans KR"'),overflow:[...document.querySelectorAll('[data-el]')].flatMap(e=>[...e.querySelectorAll('.name,.note,.fig')].filter(q=>q.scrollWidth>q.clientWidth+3&&q.clientWidth>0).map(q=>({el:e.dataset.el,text:q.textContent,w:q.clientWidth,scroll:q.scrollWidth})))})''')})
   im=Image.new('RGB',(2560,720),'white');im.paste(Image.open(P/'replica'/(f.stem+'.png')),(0,0));im.paste(Image.open(D/(f.stem+'.png')),(1280,0));im.save(D/(f.stem+'-compare.png'))
  await b.close()
 (D/'checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));print('Rendered',len(checks),'reassembled pages')
asyncio.run(main())
