import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=await b.new_page(viewport={'width':1280,'height':720})
  await pg.goto('http://127.0.0.1:8762/library/light.html');await pg.evaluate('document.fonts.ready')
  await pg.add_style_tag(content='body{display:block;padding:0}article{display:none}article.active{display:block}article>h2{display:none}.frame{width:1280px;height:720px}.frame>.slide{transform:none}')
  for f in ['slope / dumbbell','timeline / track-alt','flowchart / flowchart','swimlane / swimlane','hub / hub-6','venn / venn-3','concentric / orbit-3']:
   await pg.evaluate("s=>document.querySelectorAll('article').forEach(a=>a.classList.toggle('active',a.querySelector('h2').textContent.startsWith(s)))",f)
   await pg.screenshot(path='/workspace/work/fluxweave/'+f.split(' / ')[0]+'-test.png')
  await b.close()
asyncio.run(main())
