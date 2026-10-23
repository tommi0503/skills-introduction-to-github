from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import json, fitz
R=Path('/workspace/output/glasspulse-review'); orig=Path('/workspace/work/deck/miricanvas_기업_selected/006_1kkda_파랑_모던_타운홀_행사')
import threading, http.server, functools
server=http.server.ThreadingHTTPServer(('127.0.0.1',8138),functools.partial(http.server.SimpleHTTPRequestHandler,directory='/workspace/output/glasspulse-review'))
threading.Thread(target=server.serve_forever,daemon=True).start()
import sys
kind=sys.argv[1] if len(sys.argv)>1 else 'replica'
checks=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for h in sorted((R/kind).glob('slide-*.html')):
  page.goto('http://127.0.0.1:8138/'+str(h.relative_to(R)));page.evaluate('document.fonts.ready');page.screenshot(path=str(h.with_suffix('.png')))
  checks.append({'file':h.name,'size':page.locator('.slide').bounding_box(),'overflow':page.evaluate('''()=>{let r=document.querySelector('.slide').getBoundingClientRect(),out=[];for(let el of document.querySelectorAll('.slide *'))if(el.childNodes.length&&Array.from(el.childNodes).some(n=>n.nodeType===3&&n.textContent.trim())){let b=el.getBoundingClientRect();if(b.left<r.left-2||b.right>r.right+2||b.top<r.top-2||b.bottom>r.bottom+2)out.push(el.textContent.slice(0,60))}return out}'''),'font':page.evaluate('document.fonts.check("700 24px \\\"Pretendard Variable\\\"")')})
  n=h.stem[-2:];im=Image.new('RGB',(2560,720));im.paste(Image.open(orig/f'slide_{n}.png'),(0,0));im.paste(Image.open(h.with_suffix('.png')),(1280,0));im.save(R/('compare-'+kind)/f'slide-{n}.png')
 b.close()
doc=fitz.open()
for im in sorted((R/kind).glob('slide-*.png')):
 pg=doc.new_page(width=1280,height=720);pg.insert_image(pg.rect,filename=str(im))
doc.save(R/kind/(kind+'.pdf'),garbage=4,deflate=True,deflate_images=True);(R/kind/'checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
