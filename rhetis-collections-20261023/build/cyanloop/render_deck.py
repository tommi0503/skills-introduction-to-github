from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from playwright.sync_api import sync_playwright
from PIL import Image
import fitz,json
R=Path('/workspace/output/cyanloop-review');D=Path('/workspace/work/deck/miricanvas_기업_selected/003_1la0o_하늘색_모던_교육_자료')
s=ThreadingHTTPServer(('127.0.0.1',8863),partial(SimpleHTTPRequestHandler,directory=str(R)));Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=b.new_page(viewport={'width':1280,'height':720});doc=fitz.open();checks=[]
 for f in sorted((R/'reassembled').glob('slide_*.html')):
  pg.goto('http://127.0.0.1:8863/reassembled/'+f.name);pg.evaluate('document.fonts.ready');blob=pg.screenshot();f.with_suffix('.png').write_bytes(blob)
  page=doc.new_page(width=960,height=540);page.insert_image(page.rect,stream=blob)
  im=Image.new('RGB',(2560,720),'white');im.paste(Image.open(D/f.with_suffix('.png').name),(0,0));im.paste(Image.open(f.with_suffix('.png')),(1280,0));im.save(R/'compare-reassembled'/f.with_suffix('.png').name)
  checks.append({'page':f.stem,'fontErrors':pg.evaluate('Array.from(document.fonts).filter(f=>f.status==="error").map(f=>f.family)'),'size':[1280,720]})
 doc.save(R/'reassembled/reassembled.pdf',garbage=4,deflate=True,deflate_images=True);doc.close();b.close()
(R/'reassembled/browser-checks.json').write_text(json.dumps(checks,indent=2));print('deck rendered')
