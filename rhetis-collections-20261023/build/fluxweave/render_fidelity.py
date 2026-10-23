import asyncio
from pathlib import Path
from PIL import Image
from playwright.async_api import async_playwright
W=Path('/workspace/output/fluxweave-review');D=Path('/workspace/work/deck/miricanvas_기업_selected/002_1leen_파랑_미니멀_기업소개서_기획서')
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=await b.new_page(viewport={'width':1280,'height':720})
  for n in list(range(1,19)):
   f=f'slide_{n:02}.html';await pg.goto('http://127.0.0.1:8762/reassembled/'+f);await pg.evaluate('document.fonts.ready');out=W/'reassembled'/f.replace('.html','.png');await pg.screenshot(path=str(out));im=Image.new('RGB',(2560,720),'white');im.paste(Image.open(D/out.name),(0,0));im.paste(Image.open(out),(1280,0));im.save(W/'compare-reassembled'/out.name)
   print(n,flush=True)
  await b.close()
asyncio.run(main())
