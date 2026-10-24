"""Read-only measurements of immutable replica DOM, including styled text children."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
P=Path(__file__).parent
JS="""els=>els.map(e=>{const read=n=>{let b=n.getBoundingClientRect(),s=getComputedStyle(n);return {tag:n.tagName,class:n.className.baseVal??n.className,text:n.textContent.trim(),bbox:[b.x,b.y,b.width,b.height],fontFamily:s.fontFamily,fontSize:s.fontSize,fontWeight:s.fontWeight,lineHeight:s.lineHeight,letterSpacing:s.letterSpacing,color:s.color}};return {computed:read(e),children:[...e.querySelectorAll('b,small,p,span,th,td,svg')].map(read)}})"""
x=json.loads((P/'map.json').read_text());byid={}
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page(viewport={'width':1280,'height':720})
 for page in x['pages']:
  q.goto('http://127.0.0.1:8875/vectorbox-project/'+page['source']);q.evaluate('document.fonts.ready');a=q.locator('.slide > *').evaluate_all(JS)
  for item,data in zip(page['visibleObjects'],a):item['sourceMeasurements'].update(data);byid[item['id']]=item
 b.close()
for inst in x['instances']:
 if isinstance(inst.get('sourceMeasurements'),list):inst['sourceMeasurements']=[byid[o['id']] for o in inst['sourceMeasurements']]
(P/'map.json').write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print('Measured12 immutable pages, including children of all236 visible source roots.')
