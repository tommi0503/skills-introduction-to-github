import asyncio,re,json
from pathlib import Path
from playwright.async_api import async_playwright
P=Path(__file__).parent
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'],headless=True)
  page=await b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  out=P/'local-review';out.mkdir(exist_ok=True)
  for i in range(1,22):
   await page.goto(f'http://127.0.0.1:8765/seedmark-project/reassembled/slide_{i:02}.html');await page.evaluate('document.fonts.ready');await page.screenshot(path=str(out/f'reassembled-{i:02}.png'))
  # single full-size representative fixtures at the original min and full allocation
  styles='<link rel="stylesheet" href="../../assets/fonts/fonts.css">'+''.join('<style>'+x.read_text()+'</style>' for x in [P/'seedmark/foundation/foundation.css',P/'seedmark/kit/css/tokens.css',P/'reassembled/type-steps.css',P/'assets/source-palette.css'])+''.join('<style>'+x.read_text()+'</style>'for x in(P/'seedmark/elements').glob('*/element.css'))
  for folder,fixture in [('chart-area','area-1'),('chart-line','lines-6'),('chart-donut','donuts-3'),('card','card-5-tone'),('card','card-3-on'),('radar',None)]:
   f=P/'seedmark/elements'/folder/'fixtures'/f'{fixture}.html'if fixture else next((P/'seedmark/elements'/folder/'fixtures').glob('*.html'))
   html='<!doctype html><meta charset="utf-8">'+styles+'<section class="slide"><div class="page"><div class="body">'+f.read_text()+'</div></div></section>'
   (P/f'local-review/{folder}-{f.stem}.html').write_text(html)
   await page.goto(f'http://127.0.0.1:8765/seedmark-project/local-review/{folder}-{f.stem}.html');await page.evaluate('document.fonts.ready');await page.screenshot(path=str(out/f'{folder}-{f.stem}.png'))
  await b.close()
asyncio.run(main())
