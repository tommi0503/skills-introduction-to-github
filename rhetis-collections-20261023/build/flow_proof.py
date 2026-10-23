import asyncio,re,json
from pathlib import Path
from playwright.async_api import async_playwright
BASE=Path('/workspace/output/fluxweave/elements');DEST=Path('/workspace/work/integration/flow-proof');DEST.mkdir(exist_ok=True)
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=await browser.new_page(viewport={'width':1280,'height':720})
  await page.goto('http://127.0.0.1:8760/fluxweave-audit.html')
  for kind in ['cycle','journey','sankey']:
   for fixture in sorted((BASE/kind/'fixtures').glob('*.html')):
    raw=fixture.read_text();m=re.search(r'min:\s*(\d+)x(\d+)',raw);minimum=[int(x) for x in m.groups()] if m else [12,6];body=re.sub(r'<!--.*?-->','',raw,flags=re.S).strip()
    for size in [minimum,[12,6]]:
     for dark in [False,True]:
      await page.evaluate('(html)=>document.body.innerHTML=html','<section class="slide'+(' dark' if dark else '')+'"><div class="page"><div class="body">'+body+'</div></div></section>')
      await page.locator('.body').evaluate('(el,s)=>{el.firstElementChild.style.gridColumn="1/span "+s[0];el.firstElementChild.style.gridRow="1/span "+s[1]}',size)
      await page.evaluate('document.fonts.ready');await page.screenshot(path=str(DEST/f'{fixture.stem}-{size[0]}x{size[1]}-{dark}.png'))
  await browser.close()
asyncio.run(main())
