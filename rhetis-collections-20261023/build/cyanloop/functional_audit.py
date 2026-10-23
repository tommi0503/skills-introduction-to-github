from pathlib import Path
from playwright.sync_api import sync_playwright
import http.server,threading,functools,re,json
C=Path('/workspace/output/cyanloop');R=Path('/workspace/output/cyanloop-review')
server=http.server.ThreadingHTTPServer(('127.0.0.1',8865),functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(R)));threading.Thread(target=server.serve_forever,daemon=True).start()
checks=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720})
 for folder in ['journey','slope','chart-area','hub','waffle','funnel']:
  for f in sorted((C/'elements'/folder/'fixtures').glob('*.html')):
   if folder=='hub' and f.stem not in ['hub-3','hub-4','hub-6']:continue
   raw=f.read_text();mins=re.findall(r'(\d+)x(\d+)',raw.split('-->')[0]);mi=tuple(map(int,mins[0]))
   for w,h in [mi,(12,6)]:
    body=re.sub(r'<!--.*?-->','',raw,flags=re.S)
    html='<!doctype html><html><meta charset="utf-8"><link rel="stylesheet" href="../fonts/fonts.css"><link rel="stylesheet" href="runtime.css"><body style="margin:0"><section class="slide"><div class="page"><div class="body">'+body+'</div></div></section></body></html>'
    temp=R/'library/_functional.html';temp.write_text(html);page.goto('http://127.0.0.1:8865/library/_functional.html?'+f.stem+f'{w}{h}');page.evaluate('document.fonts.ready');page.locator('.body').first.locator(':scope > *').evaluate('(e,d)=>{e.style.gridColumn="1/span "+d[0];e.style.gridRow="1/span "+d[1]}',[w,h])
    result=page.evaluate('''folder=>{
     const result=[];const B=e=>e.getBoundingClientRect(), S=(e,p)=>getComputedStyle(e,p), pt=(e,p)=>{let b=B(e),s=S(e,p);return[b.x+parseFloat(s.left),b.y+parseFloat(s.top)]};
     if(folder==='journey')for(let e of document.querySelectorAll('.stage:not(:last-child)')){let a=pt(e,'::after'),s=S(e,'::after'),m=new DOMMatrix(s.transform),len=parseFloat(s.width),n=pt(e.nextElementSibling,'::before');result.push({name:'emotion-segment-endpoint',error:Math.hypot(a[0]+m.a*len-n[0],a[1]+1+m.b*len-n[1])});}
     if(folder==='hub'){let c=B(document.querySelector('.core'));for(let e of document.querySelectorAll('.spoke')){let a=pt(e,'::before'),s=S(e,'::before'),m=new DOMMatrix(s.transform),len=parseFloat(s.width);result.push({name:'hub-core-endpoint',error:Math.hypot(a[0]+m.a*len-(c.x+c.width/2),a[1]+.5+m.b*len-(c.y+c.height/2))});}}
     if(folder==='slope'&&!document.querySelector('.slope').classList.contains('dumbbell'))for(let e of document.querySelectorAll('.pair')){let a=pt(e,'::before'),s=S(e,'::before'),m=new DOMMatrix(s.transform),len=parseFloat(s.width),q=B(e.querySelector('.b'));result.push({name:'slope-value-endpoint',error:Math.hypot(a[0]+m.a*len-q.x-q.width/2,a[1]+1+m.b*len-q.y-q.height/2)});}
     if(folder==='chart-area'){let labels=[...document.querySelectorAll('.axis span')];for(let series of document.querySelectorAll('.series'))for(let [i,e] of [...series.querySelectorAll('.pt')].entries()){let q=B(e),l=B(labels[i]);result.push({name:'area-point-axis-x',error:Math.abs(q.x-(l.x+l.width/2))});}}
     if(folder==='funnel'){let root=document.querySelector('.funnel'),box=B(root),rs=S(root),inner=box.width-parseFloat(rs.paddingLeft)-parseFloat(rs.paddingRight);for(let e of root.querySelectorAll('.stage')){let old=e.style.getPropertyValue('--v');for(let v of [parseFloat(old),0,1,24,100]){e.style.setProperty('--v',v);let q=B(e);result.push({name:'funnel-coloured-stage-width',value:v,expected:inner*v/100,actual:q.width,error:Math.abs(q.width-inner*v/100)});}e.style.setProperty('--v',old);let a=B(e.querySelector('.name')),b=B(e.querySelector('.fig'));result.push({name:'funnel-label-centres',error:Math.abs(a.y+a.height/2-b.y-b.height/2)});}}
     if(folder==='waffle')for(let e of document.querySelectorAll('.waffle')){let units=[...e.querySelectorAll('.u')],sizes=units.map(e=>B(e));result.push({name:'counted-units-visible',count:units.length,on:units.filter(e=>e.classList.contains('on')).length,minWidth:Math.min(...sizes.map(r=>r.width)),minHeight:Math.min(...sizes.map(r=>r.height)),error:sizes.some(r=>r.width<.5||r.height<.5)?100:0});}
     return result;
    }''',folder)
    checks.append({'fixture':str(f.relative_to(C)),'size':[w,h],'checks':result})
 b.close();temp.unlink(missing_ok=True)
report={'method':'Actual rendered endpoints against data point/axis/core centres; counted unit visible boxes at minimum and 12x6. 2px geometry tolerance.','checks':checks,'errors':[{'fixture':r['fixture'],'size':r['size'],'check':c} for r in checks for c in r['checks'] if c['error']>2]}
(R/'library/functional-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('Functional fixtures/states',len(checks),'errors',len(report['errors']));print(json.dumps(report['errors'][:15],ensure_ascii=False,indent=2))
