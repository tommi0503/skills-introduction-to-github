from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from playwright.sync_api import sync_playwright
import json
R=Path('/workspace/output/cyanloop-review');s=ThreadingHTTPServer(('127.0.0.1',8864),partial(SimpleHTTPRequestHandler,directory=str(R)));Thread(target=s.serve_forever,daemon=True).start()
js='''() => {const w=document.createTreeWalker(document.querySelector('.slide'),NodeFilter.SHOW_TEXT),bad=[];while(w.nextNode()){const n=w.currentNode,e=n.parentElement,s=getComputedStyle(e);if(!n.textContent.trim()||s.display==='none'||s.visibility==='hidden'||!e.getClientRects().length)continue;let z=document.createRange();z.selectNodeContents(n);let r=z.getBoundingClientRect();if(r.left < -1||r.top < -1||r.right>1281||r.bottom>721)bad.push({text:n.textContent,cls:e.className,rect:[r.x,r.y,r.width,r.height]});}return {size:[innerWidth,innerHeight],bad,fonts:[...document.fonts].filter(f=>f.status==='error').map(f=>f.family)};}'''
checks=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);g=b.new_page(viewport={'width':1280,'height':720})
 for n in range(1,19):
  g.goto('http://127.0.0.1:8864/reassembled/slide_'+str(n).zfill(2)+'.html');g.evaluate('document.fonts.ready');v=g.evaluate(js);checks.append(dict(page=n,**v))
 b.close()
(R/'reassembled/page-audit.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));print([(x['page'],x['bad']) for x in checks if x['bad']])
