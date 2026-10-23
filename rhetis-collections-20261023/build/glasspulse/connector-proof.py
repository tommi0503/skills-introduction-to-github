import http.server,functools,threading
from playwright.sync_api import sync_playwright
R='/workspace/output/glasspulse-review'
class H(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
h=http.server.ThreadingHTTPServer(('127.0.0.1',8139),functools.partial(H,directory=R));threading.Thread(target=h.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=b.new_page(viewport={'width':1280,'height':720});pg.goto('http://127.0.0.1:8139/library/light.html');pg.evaluate('document.fonts.ready');html='<section class="slide"><div class="page"><div class="body"><div class="flowchart" data-el="glasspulse-flowchart" style="grid-column:1/span 12;grid-row:1/span 6"><div class="node ask to-r to-d to-l to-u" style="grid-column:3;grid-row:2"><b class="name">네 방향 동시 분기</b></div>'+''.join(f'<div class="node end" style="grid-column:{c};grid-row:{r}"><b class="name">{t}</b></div>' for c,r,t in [(2,2,'왼쪽'),(4,2,'오른쪽'),(3,1,'위쪽'),(3,3,'아래쪽')])+'</div></div></div></section>';pg.evaluate('(h)=>document.body.innerHTML=h',html);pg.add_style_tag(content='body{margin:0;padding:0;display:block}');pg.screenshot(path='/workspace/work/glasspulse/directions-proof.png');b.close()
