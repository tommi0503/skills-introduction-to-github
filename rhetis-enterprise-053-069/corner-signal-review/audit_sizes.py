from pathlib import Path
from playwright.sync_api import sync_playwright
import re,json,sys
R=Path(__file__).parent;selected=set(sys.argv[1:]);results=[]
if selected and (R/'size-audit.json').exists():results=[r for r in json.loads((R/'size-audit.json').read_text()) if r['fixture'].split(' / ')[0] not in selected]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);a=b.new_page(viewport={'width':1280,'height':720})
 for mode in ['light','dark']:
  a.goto(f'http://127.0.0.1:8765/corner-signal-review/library/{mode}.html');a.evaluate('document.fonts.ready');n=a.locator('article').count()
  for i in range(n):
   label=a.locator('article').nth(i).locator(':scope > h2').text_content();
   if selected and label.split(' / ')[0] not in selected:continue
   m=re.search(r'min\s+(\d+)x(\d+)',label);col,row=(int(m[1]),int(m[2])) if m else (6,3)
   # Group fixtures state minimum for an individual equal member.
   members=a.evaluate('i=>{let b=document.querySelectorAll("article")[i].querySelector(".body");let e=b?.firstElementChild;return e?.classList.contains("group")&&!e.classList.contains("col")?e.children.length:1}',i);col=min(12,col*members)
   for x,y in [(x,y) for x in range(col,13) for y in range(row,7)]:
    r=a.evaluate('''([i,c,r])=>{document.querySelectorAll('article').forEach((a,n)=>a.style.display=n===i?'block':'none');document.body.style.cssText='margin:0;padding:0;display:block';let a=document.querySelectorAll('article')[i];a.querySelector('h2').style.display='none';let f=a.querySelector('.frame');f.style.cssText='width:1280px;height:720px;overflow:hidden';let s=f.firstElementChild;s.style.cssText='width:1280px;height:720px;position:relative;transform:none';let body=s.querySelector('.body'),e=body?.firstElementChild;if(!e)return{skip:true};e.style.gridColumn='1 / span '+c;e.style.gridRow='1 / span '+r;let over=[];s.querySelectorAll('[data-el]').forEach(z=>{let b=z.getBoundingClientRect();if(b.width&&b.height&&(z.scrollWidth>z.clientWidth+2||z.scrollHeight>z.clientHeight+2))over.push({el:z.dataset.el,client:[z.clientWidth,z.clientHeight],scroll:[z.scrollWidth,z.scrollHeight]})});return{overflow:over,font:document.fonts.check('16px "Pretendard Variable"')}}''',[i,x,y]);results.append(dict(mode=mode,fixture=label,size=[x,y],**r))
 b.close()
(R/'size-audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));fail=[r for r in results if r.get('overflow')];print(len(results),'cases',len(fail),'overflow');print(json.dumps(fail[:20],ensure_ascii=False))
