import sys,json
from pathlib import Path
sys.path.insert(0,'/workspace/work/tools');import render_review as rr
from playwright.sync_api import sync_playwright
B=Path('/workspace/work/deliverables/nocturne');out=[]
with sync_playwright() as p:
 b=rr.browser(p);pg=b.new_page(viewport={'width':1280,'height':720})
 for kind in ['replica','reassembled']:
  for n in range(19,25):
   rr.load(pg,B/f'review/{kind}/slide_{n}.html');out.append({'kind':kind,'slide':n,'rects':pg.evaluate('''()=>[...document.querySelectorAll('.brand,.year,.top,.kicker,.head,.title,.headline,.headline h2,.callout,.callout p,.stats,.stat,.stat .name,.stat .fig,.chips,.chip,.pill,.values,.value,.value h2,.panel,.panel p,.list,.list .item,.list .name,.qa,.qa-line,.note,.cover .lead,.lockup,.deco,.meta,.seat.back,.body')].map(e=>{let r=e.getBoundingClientRect(),s=getComputedStyle(e);return {class:e.className,text:e.innerText?.slice(0,60),x:r.x,y:r.y,w:r.width,h:r.height,size:s.fontSize,weight:s.fontWeight,display:s.display,z:s.zIndex}})''')})
 b.close()
(B/'review/revision-measurements-before.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(json.dumps(out,ensure_ascii=False))
