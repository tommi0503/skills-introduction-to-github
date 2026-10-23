from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from playwright.sync_api import sync_playwright
R=Path('/workspace/output/cyanloop-review');s=ThreadingHTTPServer(('127.0.0.1',8864),partial(SimpleHTTPRequestHandler,directory=str(R)));Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);g=b.new_page(viewport={'width':1280,'height':720})
 for n in [6,9,14]:
  g.goto('http://127.0.0.1:8864/reassembled/slide_'+str(n).zfill(2)+'.html');g.evaluate('document.fonts.ready');print(n,g.locator('.head .title').evaluate('(e)=>[...e.children].map(x=>({cl:x.className,rect:JSON.stringify(x.getBoundingClientRect()),width:getComputedStyle(x).width,display:getComputedStyle(x).display}))'))
 b.close()
