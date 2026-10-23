from pathlib import Path
import fitz
from playwright.sync_api import sync_playwright
R=Path('/workspace/output/roundrise-review')
for mode in ['replica','reassembled']:
 doc=fitz.open()
 for f in sorted((R/mode).glob('slide_*.png')):
  p=doc.new_page(width=1280,height=720);p.insert_image(p.rect,filename=str(f))
 doc.save(str(R/mode/f'{mode}.pdf'),deflate=True,deflate_images=True);doc.close()
 print(mode,'lossless24',flush=True)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);pg=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for mode in ['light','dark']:
  pg.goto('http://127.0.0.1:8767/library/'+mode+'.html');pg.evaluate('document.fonts.ready');pg.add_style_tag(content='body{display:block;padding:0;margin:0}article{width:1280px;height:720px;overflow:hidden}article>h2{display:none}.frame{width:1280px;height:720px;border-radius:0;overflow:hidden}.frame>.slide{transform:none;width:1280px;height:720px}')
  doc=fitz.open()
  for a in pg.locator('article').all():
   raw=a.locator('.slide').screenshot();page=doc.new_page(width=1280,height=720);page.insert_image(page.rect,stream=raw)
  doc.save(str(R/'library'/f'library-{mode}.pdf'),deflate=True,deflate_images=True);doc.close();print(mode,'lossless177',flush=True)
 b.close()
