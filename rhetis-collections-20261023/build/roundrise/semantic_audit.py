from pathlib import Path
import json
from playwright.sync_api import sync_playwright
R=Path('/workspace/output/roundrise-review')
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);pg=b.new_page(viewport={'width':1328,'height':900});pg.goto('http://127.0.0.1:8767/library/light.html');pg.evaluate('document.fonts.ready')
 result=pg.evaluate('''()=>{
 let out={journey:[],sankey:[],funnel:[],cycle:[],sparkline:[]};
 for(let root of document.querySelectorAll('.journey[data-el="roundrise-journey"]')){
  let stages=[...root.children];let max=0;
  for(let i=0;i<stages.length-1;i++){
   let a=stages[i],n=stages[i+1],ra=a.getBoundingClientRect(),rn=n.getBoundingClientRect(),p=getComputedStyle(a,'::before'),pn=getComputedStyle(n,'::before'),l=getComputedStyle(a,'::after'),m=new DOMMatrix(l.transform),scale=ra.width/a.offsetWidth;
   let ax=ra.left+parseFloat(p.left)*scale,ay=ra.bottom-parseFloat(p.bottom)*scale,nx=rn.left+parseFloat(pn.left)*scale,ny=rn.bottom-parseFloat(pn.bottom)*scale;
   let ex=ax+parseFloat(l.width)*m.a*scale,ey=ay+parseFloat(l.width)*m.b*scale;max=Math.max(max,Math.hypot(nx-ex,ny-ey)/scale);
  }out.journey.push({stages:stages.length,max_endpoint_error_px:+max.toFixed(2)});
 }
 for(let root of document.querySelectorAll('.sankey[data-el="roundrise-sankey"]')){
  for(let parent of [root,...root.querySelectorAll(':scope>.branch:has(>.branch)')]){
   let branches=[...parent.children].filter(x=>x.matches('.branch')),ratios=branches.map(x=>x.getBoundingClientRect().height/parseFloat(getComputedStyle(x).getPropertyValue('--v')));
   out.sankey.push({branches:branches.length,ratio_spread:+(Math.max(...ratios)-Math.min(...ratios)).toFixed(3)});
  }
 }
 let funnel=document.querySelector('.funnel[data-el="roundrise-funnel"]'),stage=funnel.firstElementChild;
 for(let v of [0,24,100]){stage.style.setProperty('--v',v);let s=getComputedStyle(stage),q=getComputedStyle(stage,'::before');out.funnel.push({v,width_px:parseFloat(q.width),expected_px:parseFloat(s.width)*v/100});}
 for(let c of document.querySelectorAll('.cycle[data-el="roundrise-cycle"]'))out.cycle.push({nodes:c.querySelectorAll(':scope>.node').length,arrows:[...c.querySelectorAll(':scope>.node')].filter(n=>getComputedStyle(n,'::after').content!=='none').length});
 for(let c of document.querySelectorAll('.spark[data-el="roundrise-sparkline"]'))out.sparkline.push({bars:c.classList.contains('bars'),points:c.children.length,segment_shape:c.classList.contains('bars')?'bar':getComputedStyle(c.children[1],'::before').clipPath});return out;
 }''')
 b.close()
(R/'semantic-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False))
assert all(x['max_endpoint_error_px']<2 for x in result['journey'])
assert all(x['ratio_spread']<.01 for x in result['sankey'])
assert all(abs(x['width_px']-x['expected_px'])<.1 for x in result['funnel'])

assert all(x["segment_shape"].startswith("polygon(") for x in result["sparkline"] if not x["bars"])
assert all(x["nodes"]==x["arrows"] for x in result["cycle"])
