from pathlib import Path
from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
import json
R=Path('/workspace/output/cyanloop-review');C=Path('/workspace/output/cyanloop')
s=ThreadingHTTPServer(('127.0.0.1',8769),partial(SimpleHTTPRequestHandler,directory=str(R)));Thread(target=s.serve_forever,daemon=True).start()
body=(C/'elements/chart-area/fixtures/areas-2.html').read_text()
f=R/'library/debug.html';f.write_text('<html><link rel="stylesheet" href="runtime.css"><section class="slide"><div class="page"><div class="body">'+body+'</div></div></section></html>')
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=b.new_page(viewport={'width':1280,'height':720});pg.goto('http://127.0.0.1:8769/library/debug.html');print(pg.locator('.series').evaluate_all('(es)=>es.map(e=>({outer:e.outerHTML,clip:getComputedStyle(e,"::before").clipPath,bg:getComputedStyle(e,"::before").background,vars:Array.from({length:6},(_,i)=>getComputedStyle(e).getPropertyValue("--cyanloop-p"+(i+1)))}))'))
 b.close()
f.unlink()
