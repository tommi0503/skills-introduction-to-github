from pathlib import Path
import importlib.util,json,re
from playwright.sync_api import sync_playwright
P=Path(__file__).parent;R=P.parent
spec=importlib.util.spec_from_file_location('preview','/workspace/work/reference/tools/preview.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
Q=P/'qa-final-visual';Q.mkdir(exist_ok=True)
names=['bullet','balance','chart-donut','chart-line','chart-stack','concentric','hierarchy','mindmap','journey','flowchart','cycle','funnel','person','positioning','slope','swimlane','timeline','venn','image-frame','radar','foundation','card','callout','waffle','pyramid']
checks=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);page=b.new_page(viewport={'width':1360,'height':900})
 for dark in [False,True]:
  mode='dark' if dark else 'light';f=Q/(mode+'.html');f.write_text(m.sheet(P/'onboard-docket',json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text()),json.loads(Path('/workspace/work/reference/contract/palette.json').read_text()),dark=dark,fonts_href='../assets/fonts/fonts.css'))
  page.goto('http://127.0.0.1:8765/onboard-docket-project/qa-final-visual/'+f.name,wait_until='networkidle');page.evaluate('document.fonts.ready')
  for n in names:
   page.evaluate('n=>{for(const a of document.querySelectorAll("article"))a.style.display=a.querySelector("h2").textContent.startsWith(n+" / ")?"":"none"}',n)
   page.screenshot(path=str(Q/(n+'-'+mode+'.png')),full_page=True)
   checks.append({'element':n,'mode':mode,'root':page.locator('article:visible .body').first.evaluate('e=>{let r=e.getBoundingClientRect();return [r.width,r.height]}')})
  page.evaluate('()=>{for(const a of document.querySelectorAll("article"))a.style.display=""}')
  # Existing contract fixtures resized to minima, text ancestor clipping and nontext geometry remain inspectable.
  for a in page.locator('article').all():
   title=a.locator(':scope > h2').inner_text();n=title.split(' / ')[0]
   if n not in names or n=='foundation':continue
   mat=re.search(r'min (\d+)x(\d+)',title)
   if not mat:continue
   c,r=map(int,mat.groups());a.evaluate('(a,s)=>{a.querySelector(".frame").style.cssText="width:1280px;height:720px";a.querySelector(".frame>.slide").style.transform="none";for(const e of a.querySelector(".body").children){e.style.gridColumn="1 / span "+s[0];e.style.gridRow="1 / span "+s[1]}}',[c,r])
   errors=a.evaluate('''a=>{let out=[];for(const e of a.querySelectorAll('.body *')){if(e.children.length||!e.textContent.trim())continue;let s=getComputedStyle(e);if(s.visibility==='hidden'||s.display==='none')continue;let r=document.createRange();r.selectNodeContents(e);let t=r.getBoundingClientRect();for(let p=e.parentElement;p&&p!==a;p=p.parentElement){let z=getComputedStyle(p),b=p.getBoundingClientRect();if((z.overflowX==='hidden'||z.overflowY==='hidden')&&(t.right>b.right+2||t.bottom>b.bottom+3||t.left<b.left-2||t.top<b.top-3)){out.push(e.textContent.trim().slice(0,70));break}}}return out}''')
   if errors:checks.append({'fixture':title,'mode':mode,'clipping':errors})
  page.set_viewport_size({'width':1360,'height':900})
 b.close()
(Q/'checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));print('Affected sheets',len(names)*2,'clipping',sum('clipping'in x for x in checks))
