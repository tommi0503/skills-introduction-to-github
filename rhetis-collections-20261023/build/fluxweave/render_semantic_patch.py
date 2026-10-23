import asyncio,math
from pathlib import Path
from PIL import Image,ImageDraw
import fitz
from playwright.async_api import async_playwright
W=Path('/workspace/output/fluxweave-review');TMP=Path('/workspace/work/fluxweave/render')
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=await b.new_page(viewport={'width':1280,'height':720})
  for mode in ['light','dark']:
   await pg.goto('http://127.0.0.1:8762/library/'+mode+'.html');await pg.evaluate('document.fonts.ready');await pg.add_style_tag(content='body{display:block;padding:0;background:white}article{display:none}article.active{display:block}article>h2{display:none}.frame{width:1280px;height:720px;border-radius:0}.frame>.slide{transform:none}')
   entries=await pg.locator('article>h2').all_text_contents();groups={};wanted={'slope','image-frame','concentric'}
   for i,title in enumerate(entries):
    if title.split('/')[0].strip() not in wanted:continue
    await pg.evaluate('''i=>document.querySelectorAll('article').forEach((e,j)=>e.classList.toggle('active',i===j))''',i);fn=TMP/f'{mode}-{i:03}.png';await pg.screenshot(path=str(fn));groups.setdefault(title.split('/')[0].strip(),[]).append((title,fn))
   for elem,items in groups.items():
    im=Image.new('RGB',(1280,math.ceil(len(items)/2)*390),'#e8e8ec');dr=ImageDraw.Draw(im)
    for i,(title,fn) in enumerate(items):
     x=(i%2)*640;y=(i//2)*390;im.paste(Image.open(fn).resize((640,360)),(x,y+30));dr.text((x+10,y+8),title[:70],fill='#333')
    im.save(W/'library'/elem/f'{mode}.png')
   doc=fitz.open()
   for i in range(len(entries)):
    page=doc.new_page(width=960,height=540);page.insert_image(page.rect,filename=str(TMP/f'{mode}-{i:03}.png'))
   doc.save(W/'library'/f'library-{mode}.pdf',garbage=4,deflate=True,deflate_images=True);doc.close();print(mode,len(entries),flush=True)
  await b.close()
asyncio.run(main())
