from pathlib import Path
from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import threading,json
R=Path('/workspace/work/rebuild');OLD=Path('/workspace/work/delivery')
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(OLD)));threading.Thread(target=server.serve_forever,daemon=True).start()
JS='''()=>[...document.querySelectorAll('svg')].filter(s=>!s.closest('svg svg')).map((s,i)=>({index:i,classes:s.getAttribute('class'),bbox:(()=>{let r=s.getBoundingClientRect();return[r.x,r.y,r.width,r.height]})(),apparatus:(s.closest('.titleband,.rail,footer')?.className||s.closest('footer')?.tagName||null),html:s.outerHTML,hasText:!!s.querySelector('text'),parts:[...s.querySelectorAll('path,rect,line,circle,ellipse,polygon,polyline')].filter(e=>!e.closest('defs,clipPath,mask,marker')).map(e=>{let r=e.getBoundingClientRect(),c=getComputedStyle(e);return {tag:e.tagName,bbox:[r.x,r.y,r.width,r.height],html:e.outerHTML,fill:c.fill,stroke:c.stroke,width:c.strokeWidth,opacity:c.opacity}})}))'''
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-breakpad']);pg=b.new_page(viewport={'width':1280,'height':720});pg.route('**/*',lambda r:r.continue_())
 for d in R.iterdir():
  if not(d/'build/source-dom.json').exists():continue
  out={}
  for page in json.loads((d/'build/source-dom.json').read_text()):
   pg.goto(f'http://127.0.0.1:{server.server_port}/{d.name}/review/replica/slide_{page}.html');pg.evaluate('document.fonts.ready');out[page]=pg.evaluate(JS)
  (d/'build/source-vector-dom.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(d.name,len(out),flush=True)
 b.close()
server.shutdown()
