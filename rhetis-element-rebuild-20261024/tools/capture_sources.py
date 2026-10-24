from pathlib import Path
from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import threading,json
SRC=Path('/workspace/work/delivery');DEST=Path('/workspace/work/rebuild')
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(SRC)));threading.Thread(target=server.serve_forever,daemon=True).start()
JS='''() => {let root=document.querySelector('.slide')||document.body;let box=e=>{let r=e.getBoundingClientRect();return [r.x,r.y,r.width,r.height].map(v=>Math.round(v*100)/100)};let style=e=>{let s=getComputedStyle(e);return {font:s.fontFamily,size:s.fontSize,weight:s.fontWeight,line:s.lineHeight,tracking:s.letterSpacing,color:s.color,background:s.background,border:s.border,borderRadius:s.borderRadius,display:s.display,position:s.position}};let selector=e=>{let a=[];for(let k=e;k&&k!==root;k=k.parentElement){let v=k.tagName.toLowerCase();if(k.id)v+='#'+k.id;else if(k.classList.length)v+='.'+[...k.classList].join('.');let par=k.parentElement;if(par){let peers=[...par.children].filter(x=>x.tagName===k.tagName);if(peers.length>1)v+=':nth-of-type('+(peers.indexOf(k)+1)+')'}a.unshift(v)}return '.slide > '+a.join(' > ')};let nodes=[...root.children].map(e=>({tag:e.tagName,classes:e.getAttribute('class'),selector:selector(e),bbox:box(e),text:(e.innerText||e.textContent||'').trim().slice(0,1800),style:style(e),html:e.outerHTML.slice(0,10000)}));let texts=[];let tw=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);while(tw.nextNode()){let n=tw.currentNode,e=n.parentElement,t=n.textContent.trim();if(!t||['SCRIPT','STYLE','TITLE'].includes(e.tagName))continue;let st=getComputedStyle(e);if(st.display==='none'||st.visibility==='hidden')continue;let r=document.createRange();r.selectNodeContents(n);let q=r.getBoundingClientRect();if(q.width<.1||q.height<.1)continue;texts.push({text:t,bbox:[q.x,q.y,q.width,q.height].map(v=>Math.round(v*100)/100),selector:selector(e),style:style(e)})}return {pageSize:box(root),background:style(root),nodes,texts,fonts:[...document.fonts].map(f=>({family:f.family,status:f.status}))}}'''
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-crash-reporter','--disable-breakpad']);pg=b.new_page(viewport={'width':1280,'height':720});pg.route('**/*',lambda route:route.continue_())
 for name in ['tide-tab','cutfield','filament','portico','toggle-grid','lamella','rulemark']:
  if (DEST/name/'build/source-dom.json').exists():continue
  data={}
  for f in sorted((SRC/name/'review/replica').glob('slide_*.html')):
   pg.goto(f'http://127.0.0.1:{server.server_port}/{name}/review/replica/{f.name}');pg.evaluate('document.fonts.ready');pg.wait_for_timeout(120);data[f.stem[-2:]]=pg.evaluate(JS)
  (DEST/name/'build/source-dom.json').write_text(json.dumps(data,ensure_ascii=False,indent=2));print(name,len(data),'source pages inspected',flush=True)
 b.close()
server.shutdown()
