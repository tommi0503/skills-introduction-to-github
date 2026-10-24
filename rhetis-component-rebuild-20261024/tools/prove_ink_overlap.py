"""Confirm that the six SUITE line-box intersections contain no painted glyph pixels."""
from pathlib import Path
import json,io,sys,math
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright
sys.path.insert(0,str(Path(__file__).parent))
from size_review import paths,assets,document,wrapper,browser,serve_url,MEASURE
n='diecut';w,c,r=paths(n);assets(n);a=json.loads((r/'sheets/tag-audit.json').read_text());cases=[x for x in a['cases']if x['textOverlaps']];rows=[]
with sync_playwright()as pw:
 b=browser(pw)
 for case in cases:
  content=(c/'elements/tag/fixtures'/(case['fixture']+'.html')).read_text();co,ro=map(int,case['size'].split('x'));f=r/'probes/tag-ink-proof.html';f.write_text(document(c,wrapper(content,co,ro,case['mode']),case['mode']));p=b.new_page(viewport={'width':1280,'height':720});p.goto(serve_url(f));p.evaluate('document.fonts.ready');p.evaluate('([a,b])=>{let e=document.querySelector(".body").firstElementChild;e.style.gridColumn="1/span "+a;e.style.gridRow="1/span "+b}',[co,ro]);p.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');m=p.evaluate(MEASURE,[co,ro]);fg=np.asarray(Image.open(io.BytesIO(p.screenshot())).convert('RGB')).astype(int);h=p.add_style_tag(content='.slide *{-webkit-text-fill-color:transparent!important;text-shadow:none!important}');bg=np.asarray(Image.open(io.BytesIO(p.screenshot())).convert('RGB')).astype(int);h.evaluate('e=>e.remove()');mask=np.max(np.abs(fg-bg),axis=2)>8
  for x,y in m['overlap']:
   left=max(x['x'],y['x']);top=max(x['y'],y['y']);right=min(x['x']+x['w'],y['x']+y['w']);bottom=min(x['y']+x['h'],y['y']+y['h']);count=int(mask[math.ceil(top):math.floor(bottom),math.ceil(left):math.floor(right)].sum());rows.append({'fixture':case['fixture'],'mode':case['mode'],'size':case['size'],'rangeIntersection':[left,top,right-left,bottom-top],'glyphPixelsInIntersection':count})
  p.close()
 b.close()
result={'method':'Screenshot minus an identical second screenshot with glyph fill hidden, sampled strictly inside each Range intersection. Empty strips prove line-box overlap without any actual painted text overlap.','cases':rows,'allInkClear':all(x['glyphPixelsInIntersection']==0 for x in rows)};(r/'ink-overlap-proof.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False))
