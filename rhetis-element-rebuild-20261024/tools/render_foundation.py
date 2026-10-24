"""Render complete furniture fixtures as well as the contract seat fixture."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright
import json,threading,hashlib
from sheets import context,check_contrast
from PIL import Image
import io
R=Path('/workspace/work/rebuild')
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
def run(names):
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R)));threading.Thread(target=server.serve_forever,daemon=True).start()
 with sync_playwright()as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-breakpad']);pg=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for n in names:
   c=R/n/n;out=R/n/'review/foundation';out.mkdir(exist_ok=True);proof=[]
   for f in sorted((c/'foundation/fixtures').glob('*.html')):
    for mode in ['light','dark']:
     raw=f.read_text()
     if 'class="slide'not in raw:raw='<section class="slide"><div class="page"><div class="body">'+raw+'</div></div></section>'
     if mode=='dark':raw=raw.replace('class="slide','class="slide dark',1)
     html='<!doctype html><html lang="ko"><head><meta charset="utf-8"><link rel="stylesheet" href="../assets/fonts/fonts.css"><style>'+context(n)+'</style></head><body>'+raw+'</body></html>'
     path=out/(f.stem+'-'+mode+'.html');path.write_text(html);pg.goto(f'http://127.0.0.1:{server.server_port}/{n}/review/foundation/{path.name}');pg.evaluate('document.fonts.ready')
     checks=pg.evaluate('''()=>{let box=e=>{let r=e.getBoundingClientRect();return[r.x,r.y,r.width,r.height]},head=document.querySelector('.head'),body=document.querySelector('.body'),bad=[];for(let e of document.querySelectorAll('.slide *')){for(let t of e.childNodes){if(t.nodeType!==3||!t.textContent.trim())continue;let r=document.createRange();r.selectNodeContents(t);let q=r.getBoundingClientRect();if(q.width&&(q.left<-.5||q.top<-.5||q.right>1280.5||q.bottom>720.5))bad.push({text:t.textContent,box:[q.x,q.y,q.width,q.height]})}}return{size:box(document.querySelector('.slide')),head:head?box(head):null,body:body?box(body):null,textOutside:bad,fonts:[...document.fonts].filter(x=>x.status==='error').map(x=>x.family)}}''')
     shot=pg.locator('.slide').screenshot(path=str(path.with_suffix('.png')));texts=pg.evaluate('''()=>{let a=[],w=document.createTreeWalker(document.querySelector('.slide'),NodeFilter.SHOW_TEXT);while(w.nextNode()){let n=w.currentNode;if(!n.textContent.trim())continue;let c=getComputedStyle(n.parentElement),r=document.createRange();r.selectNodeContents(n);let cv=document.createElement('canvas');cv.width=cv.height=1;let cx=cv.getContext('2d');cx.fillStyle=c.color;cx.fillRect(0,0,1,1);let rgba=[...cx.getImageData(0,0,1,1).data];for(let q of r.getClientRects())if(q.width)a.push({text:n.textContent,rect:[q.x,q.y,q.width,q.height],font:parseFloat(c.fontSize),fg:rgba,opacity:1})}return a}''');checks['contrast']=check_contrast(Image.open(io.BytesIO(shot)).convert('RGB'),texts);checks.update(fixture=f.name,mode=mode,html_sha256=hashlib.sha256(path.read_bytes()).hexdigest());proof.append(checks)
   (R/n/'review/validation/foundation.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2));print(n,[(x['fixture'],x['mode'],len(x['textOutside']))for x in proof],flush=True)
  b.close()
 server.shutdown()
if __name__=='__main__':
 import sys
 run(sys.argv[1:]or list(json.loads((R/'profiles.json').read_text())))
