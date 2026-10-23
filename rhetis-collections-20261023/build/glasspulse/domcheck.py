import http.server,functools,threading
from playwright.sync_api import sync_playwright
h=http.server.ThreadingHTTPServer(('127.0.0.1',8137),functools.partial(http.server.SimpleHTTPRequestHandler,directory='/workspace/output/glasspulse-review'));threading.Thread(target=h.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720});page.goto('http://127.0.0.1:8137/reassembled/slide-06.html');page.evaluate('document.fonts.ready');print(page.evaluate('''()=>Array.from(document.querySelectorAll('.body,.group,.card,.parts,.bars,.callout,.callout p')).map(x=>({class:x.className,r:x.getBoundingClientRect().toJSON(),f:getComputedStyle(x).fontSize,display:getComputedStyle(x).display,container:getComputedStyle(x).containerType}))'''));b.close()
