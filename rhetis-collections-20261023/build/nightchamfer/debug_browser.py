from pathlib import Path
import http.server,threading,functools
from playwright.sync_api import sync_playwright
R=Path('/workspace/output/nightchamfer-review');server=http.server.ThreadingHTTPServer(('127.0.0.1',18765),functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(R)));threading.Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright()as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720});page.goto('http://127.0.0.1:18765/reassembled/slide_12.html');page.evaluate('document.fonts.ready')
 print(page.locator('[data-el="nightchamfer-timeline"],.stop,.stop>.kick').evaluate_all('(els)=>els.map(e=>({cl:e.className,rect:e.getBoundingClientRect().toJSON(),pos:getComputedStyle(e).position,top:getComputedStyle(e).top,height:getComputedStyle(e).height,bt:getComputedStyle(e).bottom}))'))
 b.close()
server.shutdown()
