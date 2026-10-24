from pathlib import Path
from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import threading,json
R=Path('/workspace/work/rebuild');OLD=Path('/workspace/work/delivery')
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(OLD)));threading.Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=b.new_page(viewport={'width':1280,'height':720})
 for n in json.loads((R/'profiles.json').read_text()):
  out={}
  for f in sorted((OLD/n/'review/replica').glob('slide_*.html')):
   pg.goto(f'http://127.0.0.1:{server.server_port}/{n}/review/replica/{f.name}');pg.evaluate('document.fonts.ready')
   out[f.stem[-2:]]=pg.evaluate('''()=>[...document.body.querySelectorAll('*')].filter(e=>e instanceof HTMLElement&&!e.textContent.trim()).map(e=>{let r=e.getBoundingClientRect(),s=getComputedStyle(e);return {bbox:[r.x,r.y,r.width,r.height],background:s.background,html:e.outerHTML.slice(0,1000)}}).filter(x=>x.background.indexOf('rgba(0, 0, 0, 0)')<0&&((x.bbox[2]>=1279&&x.bbox[3]>=200&&Math.abs(x.bbox[0])<1)||(x.bbox[3]>=719&&x.bbox[2]>=64&&(Math.abs(x.bbox[0])<1||Math.abs(x.bbox[0]+x.bbox[2]-1280)<1))))''')
  (R/n/'build/source-planes.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(n,sum(map(len,out.values())),flush=True)
 b.close()
server.shutdown()
