from pathlib import Path
from playwright.sync_api import sync_playwright
import json,re,subprocess
B=Path(__file__).parent;R=B;C=B.parent/'anchor-frame';REF=Path('/workspace/work/ref')
# Import only the audit string without running the full renderer.
s=(B/'render.py').read_text();AUDIT=s.split("AUDIT=r'''",1)[1].split("'''",1)[0]
for mode in ['light','dark']:
 args=['python',str(REF/'tools/preview.py'),str(C),str(REF/'contract/type-steps.json'),'--out',str(B/f'library/{mode}.html')]
 if mode=='dark':args+=['--dark']
 subprocess.run(args,check=True,capture_output=True);f=B/f'library/{mode}.html';f.write_text(f.read_text().replace((REF/'fonts/fonts.css').as_uri(),'../../fonts/fonts.css'))
a={}
with sync_playwright() as w:
 b=w.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);p=b.new_page(viewport={'width':1280,'height':720})
 for mode in ['light','dark']:
  p.goto('http://127.0.0.1:8765/anchor-frame-review/library/'+mode+'.html');p.evaluate('document.fonts.ready');p.add_style_tag(content='body{display:block;padding:0;margin:0}article{display:none}article.review-active{display:block}article.review-active>h2{display:none}.frame{width:1280px;height:720px;border-radius:0}.frame>.slide{transform:none}')
  count=p.locator('article').count()
  for idx in range(count):
   p.evaluate('(i)=>document.querySelectorAll("article").forEach((a,k)=>a.classList.toggle("review-active",i===k))',idx)
   title=p.locator('article').nth(idx).locator(':scope > h2').inner_text()
   a[mode+'/'+title+'/full']=p.evaluate(AUDIT)
   minimum=re.search(r'min\s+(\d+)x(\d+)',title);c,r=map(int,minimum.groups()) if minimum else (12,6)
   p.evaluate('([i,c,r])=>{for(const n of document.querySelectorAll("article")[i].querySelectorAll(".body > *")){n.style.gridColumn="1 / span "+c;n.style.gridRow="1 / span "+r}}',[idx,c,r]);a[mode+'/'+title+'/min']=p.evaluate(AUDIT)
 b.close()
(B/'audit-fast.json').write_text(json.dumps(a,ensure_ascii=False,indent=2));bad={k:v for k,v in a.items() if v};print('cases',len(a),'failures',len(bad))
for k,v in bad.items():
 if k.startswith('light'):print(k,str(v)[:400])
