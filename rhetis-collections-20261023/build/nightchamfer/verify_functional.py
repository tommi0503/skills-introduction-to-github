from pathlib import Path
import json,re,threading,http.server,functools
from playwright.sync_api import sync_playwright
W=Path('/workspace/work/nightchamfer');C=Path('/workspace/output/nightchamfer');R=Path('/workspace/output/nightchamfer-review');PUB=W/'public'
p=PUB/'nightchamfer-audit.html';(PUB/'functional-audit.html').write_text(p.read_text().replace('http://127.0.0.1:8765/fonts/fonts.css','fonts/fonts.css'))
class Q(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',18765),functools.partial(Q,directory=str(PUB)));threading.Thread(target=server.serve_forever,daemon=True).start()
report={'checks':[],'errors':[]}
with sync_playwright()as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page(viewport={'width':1280,'height':720});q.goto('http://127.0.0.1:18765/functional-audit.html');q.evaluate('document.fonts.ready')
 for typ,fixture,sizes in [('funnel','funnel/fixtures/funnel-6.html',[(6,4),(12,6)]),('hierarchy','hierarchy/fixtures/org-2.html',[(4,3),(4,6),(12,6)]),('spark','sparkline/fixtures/spark-in-stat.html',[(3,2),(12,6)])]:
  raw=re.sub(r'<!--.*?-->','',(C/'elements'/fixture).read_text(),flags=re.S)
  q.evaluate('(h)=>document.body.innerHTML=h','<section class="slide"><div class="page"><div class="body">'+raw+'</div></div></section>')
  q.evaluate('document.fonts.ready')
  for c,r in sizes:
   data=q.evaluate('''([typ,c,r])=>{let root=document.querySelector('.body').firstElementChild;root.style.gridColumn='1 / span '+c;root.style.gridRow='1 / span '+r;let box=root.getBoundingClientRect();if(typ==='funnel'){let gs=getComputedStyle(root),w=box.width-parseFloat(gs.paddingLeft)-parseFloat(gs.paddingRight),stage=root.querySelector('.stage');return[0,1,24,100].map(v=>{stage.style.setProperty('--v',v);return{v,width:stage.getBoundingClientRect().width,expected:w*v/100}})}if(typ==='hierarchy'){let cir=root.querySelector('.root'),b=cir.getBoundingClientRect(),g=getComputedStyle(cir),a=getComputedStyle(cir,'::after'),br=root.querySelector('.branch'),bg=br.getBoundingClientRect(),rail=getComputedStyle(br,'::after');return{rootDiameter:b.width,rootHeight:b.height,rootBottom:b.bottom,stemTop:b.top+parseFloat(g.borderTopWidth)+parseFloat(a.top),border:g.borderTopWidth,afterTop:a.top,afterHeight:a.height,containerHeight:box.height,branchTop:bg.top,railOffset:rail.top,stemBottom:b.top+parseFloat(g.borderTopWidth)+parseFloat(a.top)+parseFloat(a.height),railTop:bg.top+parseFloat(rail.top)}}let spark=root.querySelector('.spark'),points=[...spark.children].map(e=>e.getBoundingClientRect().y),s=spark.getBoundingClientRect();return{sparkWidth:s.width,sparkHeight:s.height,yRange:Math.max(...points)-Math.min(...points)}}''',[typ,c,r])
   rec={'type':typ,'grid':[c,r],'measurement':data};report['checks'].append(rec)
   bad=any(abs(v['width']-v['expected'])>.1 for v in data)if typ=='funnel'else(abs(data['stemBottom']-data['railTop'])>1 if typ=='hierarchy'else data['yRange']<10)
   if bad:report['errors'].append(rec)
 q.goto('http://127.0.0.1:18765/nightchamfer-review/reassembled/slide_14.html');q.evaluate('document.fonts.ready')
 report['source_page14']=q.evaluate('''()=>{let root=document.querySelector('[data-el="nightchamfer-hierarchy"]'),cir=root.querySelector('.root'),b=cir.getBoundingClientRect(),g=getComputedStyle(cir),a=getComputedStyle(cir,'::after'),br=root.querySelector('.branch'),bg=br.getBoundingClientRect(),rail=getComputedStyle(br,'::after');return{rootBottom:b.bottom,stemTop:b.top+parseFloat(g.borderTopWidth)+parseFloat(a.top),stemBottom:b.top+parseFloat(g.borderTopWidth)+parseFloat(a.top)+parseFloat(a.height),railTop:bg.top+parseFloat(rail.top)}}''')
 assert abs(report['source_page14']['rootBottom']-report['source_page14']['stemTop'])<.1
 assert abs(report['source_page14']['stemBottom']-report['source_page14']['railTop'])<.1
 b.close()
(R/'library'/'functional-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False));assert not report['errors']
