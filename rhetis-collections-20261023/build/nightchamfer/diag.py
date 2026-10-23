from pathlib import Path
import threading,http.server,functools,json
from playwright.sync_api import sync_playwright
R=Path('/workspace/output/nightchamfer-review')
class Q(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
sv=http.server.ThreadingHTTPServer(('127.0.0.1',8765),functools.partial(Q,directory=str(R)));threading.Thread(target=sv.serve_forever,daemon=True).start()
with sync_playwright()as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=b.new_page(viewport={'width':1280,'height':720});pg.goto('http://127.0.0.1:8765/library/light.html');pg.evaluate('document.fonts.ready')
 print(pg.evaluate('''()=>{let r=[...document.querySelectorAll('article')].find(e=>e.innerText.includes('chart-area / area-3pt'));let s=r.querySelector('.series');return {parent:s.getBoundingClientRect().toJSON(),pts:[...s.querySelectorAll('.pt')].map(e=>({v:e.style.getPropertyValue('--v'),rect:e.getBoundingClientRect().toJSON(),margin:getComputedStyle(e).marginTop,vh:getComputedStyle(e).getPropertyValue('--nightchamfer-vh'),before:{top:getComputedStyle(e,'::before').top,bottom:getComputedStyle(e,'::before').bottom,clip:getComputedStyle(e,'::before').clipPath},after:{top:getComputedStyle(e,'::after').top,bottom:getComputedStyle(e,'::after').bottom,clip:getComputedStyle(e,'::after').clipPath}}))}}'''))
 b.close()
