from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import fitz
import json,re,sys
R=Path('/workspace/output/roundrise-review');L=R/'library'
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);pg=b.new_page(viewport={'width':1328,'height':900},device_scale_factor=1)
 for mode in ['light','dark']:
  pg.goto('http://127.0.0.1:8767/library/'+mode+'.html');pg.evaluate('document.fonts.ready')
  groups={};checks=[]
  for i,a in enumerate(pg.locator('article').all()):
   name=a.locator(':scope > h2').inner_text().split(' / ')[0]
   if len(sys.argv)>1 and name not in sys.argv[1].split(','):continue
   groups.setdefault(name,[])
   file=L/'fixtures'/mode/f'{i:03}.png';file.parent.mkdir(parents=True,exist_ok=True);a.screenshot(path=str(file));groups[name].append(file)
  # Each element sheet holds all its fixtures in a two-column board; full PDFs have one fixture per page.
  for name,files in groups.items():
   out=L/name;out.mkdir(exist_ok=True);ims=[Image.open(f).convert('RGB') for f in files];w=1280;h=((len(ims)+1)//2)*400
   board=Image.new('RGB',(w,h),'#e8e8ec');dr=ImageDraw.Draw(board)
   for j,im in enumerate(ims):
    im.thumbnail((632,390));board.paste(im,((j%2)*640,(j//2)*400))
   board.save(out/f'{mode}.png')
  # Full sized slide PDF generated directly by Chromium, every fixture its own 16:9 sheet.
  pg.add_style_tag(content='''@page{size:1280px 720px;margin:0}body{display:block;padding:0;margin:0;background:white}article{width:1280px;height:720px;break-after:page;overflow:hidden}article>h2{display:none}.frame{width:1280px;height:720px;border-radius:0;overflow:hidden}.frame>.slide{transform:none;width:1280px;height:720px}''')
  doc=fitz.open()
  for j,a in enumerate(pg.locator('article').all()):
   frame=a.locator('.slide');raw=frame.screenshot();page=doc.new_page(width=1280,height=720);page.insert_image(page.rect,stream=raw)
  doc.save(str(L/f'library-{mode}.pdf'),deflate=True,deflate_images=True);doc.close()
  print(mode,'rendered',len(groups),'element/foundation sheets',flush=True)
 b.close()
