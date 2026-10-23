from pathlib import Path
import json,re,threading,http.server,functools
from playwright.sync_api import sync_playwright
W=Path('/workspace/work/nightchamfer');C=Path('/workspace/output/nightchamfer');R=Path('/workspace/output/nightchamfer-review');PUB=W/'public'
p=PUB/'nightchamfer-audit.html';s=p.read_text().replace('http://127.0.0.1:8765/fonts/fonts.css','fonts/fonts.css');(PUB/'shape-audit.html').write_text(s)
class Q(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',18765),functools.partial(Q,directory=str(PUB)));threading.Thread(target=server.serve_forever,daemon=True).start()
report={'states':[],'errors':[]}
with sync_playwright()as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page(viewport={'width':1280,'height':720});q.goto('http://127.0.0.1:18765/shape-audit.html');q.evaluate('document.fonts.ready')
 for typ,fixture,minc,minr in [('venn','venn/fixtures/venn-3.html',6,4),('calendar','heatmap/fixtures/calendar-12.html',6,3)]:
  raw=re.sub(r'<!--.*?-->','',(C/'elements'/fixture).read_text(),flags=re.S)
  q.evaluate('(h)=>document.body.innerHTML=h','<section class="slide"><div class="page"><div class="body">'+raw+'</div></div></section>')
  for dark in [False,True]:
   for c in range(minc,13):
    for r in range(minr,7):
     dat=q.evaluate('''([typ,c,r,dark])=>{let root=document.querySelector('.body').firstElementChild;root.style.gridColumn='1 / span '+c;root.style.gridRow='1 / span '+r;document.querySelector('.slide').classList.toggle('dark',dark);let dims=[...root.querySelectorAll(typ==='calendar'?'.cell':'.set')].map(e=>{let b=e.getBoundingClientRect();return{x:b.x,y:b.y,w:b.width,h:b.height}});let bounds=root.getBoundingClientRect();let triple=typ==='venn'?dims.every(b=>Math.hypot(bounds.x+bounds.width*.5-b.x-b.w/2,bounds.y+bounds.height*.51-b.y-b.h/2)<b.w/2):null;let labelExclusive=typ==='venn'?[...root.querySelectorAll('.set>.name')].every((e,i)=>{let b=e.getBoundingClientRect(),x=b.x+b.width/2,y=b.y+b.height/2;return dims.every((s,j)=>i===j||Math.hypot(x-s.x-s.w/2,y-s.y-s.h/2)>s.w/2)}):null;return{typ,c,r,dark,count:dims.length,maxSquareDelta:Math.max(...dims.map(b=>Math.abs(b.w-b.h))),width:dims[0].w,height:dims[0].h,tripleIntersection:triple,labelExclusive}}''',[typ,c,r,dark])
     report['states'].append(dat)
     if dat['maxSquareDelta']>.1 or typ=='venn' and(not dat['tripleIntersection']or not dat['labelExclusive']):report['errors'].append(dat)
 b.close()
(R/'library'/'shape-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(len(report['states']),'states',len(report['errors']),'errors');print(report['states'][20]);assert not report['errors']
