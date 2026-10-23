from playwright.sync_api import sync_playwright
from pathlib import Path
import json,math
res=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=b.new_page(viewport={'width':1280,'height':720});pg.goto('http://127.0.0.1:8760/flux-semantic-proof.html');pg.evaluate('document.fonts.ready');pg.add_style_tag(content='body{display:block;padding:0}article{display:none}article.active{display:block}h2{display:none}.frame:not([data-el]){width:1280px;height:720px;border-radius:0}.frame:not([data-el])>.slide{transform:none}')
 for k in ['network','slope','radar','heatmap','funnel','chart-waterfall']:
  arts=pg.locator('article').filter(has=pg.locator('h2').filter(has_text=k+' /'))
  for i in range(arts.count()):
   a=arts.nth(i);a.evaluate("n=>n.classList.add('active')");root=a.locator('[data-el="fluxweave-'+k+'"]').first
   for mode in ['light','dark']:
    a.locator('.slide').evaluate('(n,m)=>n.classList.toggle("dark",m==="dark")',mode)
    out=root.evaluate('''(e,k)=>{let r=e.getBoundingClientRect(),v={kind:k,mode:e.closest('.slide').className,w:r.width,h:r.height},num=x=>parseFloat(x)||0,pt=(el)=>{let q=el.getBoundingClientRect();return{x:q.x+q.width/2,y:q.y+q.height/2}};
     if(k==='network'){let nodes=[...e.querySelectorAll(':scope>.node')].map(pt);v.endpoint_errors=[...e.querySelectorAll(':scope>.link')].map(el=>{let s=getComputedStyle(el),a=num(s.rotate)*Math.PI/180,x=r.x+num(s.left),y=r.y+num(s.top)+num(s.height)/2,len=num(s.width),end={x:x+Math.cos(a)*len,y:y+Math.sin(a)*len};return{start:Math.min(...nodes.map(n=>Math.hypot(n.x-x,n.y-y))),end:Math.min(...nodes.map(n=>Math.hypot(n.x-end.x,n.y-end.y)))}});}
     if(k==='slope'&&!e.classList.contains('dumbbell')){v.endpoint_errors=[...e.querySelectorAll(':scope>.pair')].map(el=>{let q=el.getBoundingClientRect(),s=getComputedStyle(el,'::after'),a=num(s.rotate)*Math.PI/180,x=q.x+num(s.left),y=q.y+num(s.top)+num(s.height)/2,len=num(s.width),bs=el.querySelector('.b'),br=bs.getBoundingClientRect(),bcs=getComputedStyle(bs,'::after'),target={x:br.x+num(bcs.left)+num(bcs.width)/2,y:br.y+num(bcs.top)+num(bcs.height)/2};return Math.hypot(x+Math.cos(a)*len-target.x,y+Math.sin(a)*len-target.y)})}
     if(k==='radar'){v.axes=e.querySelectorAll(':scope>.axis').length;v.polygons=[...e.querySelectorAll(':scope>.series')].map(n=>getComputedStyle(n,'::before').clipPath);v.backgrounds=[...e.querySelectorAll(':scope>.series')].map(n=>getComputedStyle(n).backgroundColor);}
     if(k==='heatmap'&&e.classList.contains('calendar'))v.day_ratio_error=Math.max(...[...e.querySelectorAll('.cell')].map(n=>{let q=n.getBoundingClientRect();return Math.abs(q.width-q.height)}));
     if(k==='funnel'){v.band_ratio=[...e.children].map(n=>{let s=getComputedStyle(n),q=n.getBoundingClientRect();return{value:num(s.getPropertyValue('--v')),actual:num(getComputedStyle(n,'::before').width)/q.width*100}});}
     if(k==='chart-waterfall')v.connectors=[...e.querySelectorAll(':scope>.move:not(:last-child)')].map(n=>{let s=getComputedStyle(n,'::after');return{content:s.content,width:s.width,bottom:s.bottom}});
     return v}''',k)
    out['fixture']=a.locator('h2').inner_text();res.append(out)
   if k=='funnel' and i==0:
    stage=root.locator('.stage').first
    for value in [0,25,100]:
     stage.evaluate('(n,v)=>n.style.setProperty("--v",v)',value);actual=stage.evaluate('n=>parseFloat(getComputedStyle(n,"::before").width)/n.getBoundingClientRect().width*100');res.append({'kind':'funnel-edge','value':value,'actual':actual});assert abs(actual-value)<.1
   a.evaluate("n=>n.classList.remove('active')")
 b.close()
for r in res:
 if r['kind']=='network':assert all(max(x.values())<2 for x in r['endpoint_errors']),r
 if r['kind']=='slope' and 'endpoint_errors' in r:assert max(r['endpoint_errors'])<2,r
 if r['kind']=='radar':assert all(p!='none' and p.count(',')+1==r['axes'] for p in r['polygons']),r
 if 'day_ratio_error' in r:assert r['day_ratio_error']<.1,r
 if 'band_ratio' in r:assert all(abs(x['value']-x['actual'])<.1 for x in r['band_ratio']),r
Path('/workspace/output/fluxweave-review/audits/semantic-geometry.json').write_text(json.dumps({'checks':len(res),'errors':0,'records':res},indent=2,ensure_ascii=False))
print(len(res),'semantic geometry states passed')
