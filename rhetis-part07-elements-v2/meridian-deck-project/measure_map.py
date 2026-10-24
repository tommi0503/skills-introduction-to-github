from pathlib import Path
from playwright.sync_api import sync_playwright
import json
P=Path(__file__).parent
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page(viewport={'width':1280,'height':720});pages=[]
 for n in range(1,31):
  q.goto(f'http://127.0.0.1:8875/meridian-deck-project/replica/slide_{n:02d}.html');q.evaluate('document.fonts.ready')
  items=q.locator('main.slide').evaluate('''main=>[...main.children].map((e,i)=>{let r=e.getBoundingClientRect(),s=getComputedStyle(e);let ink=null;if(e.classList.contains('txt')){let z=document.createRange();z.selectNodeContents(e);let rs=[...z.getClientRects()].filter(r=>r.width&&r.height);if(rs.length){let x=Math.min(...rs.map(r=>r.x)),y=Math.min(...rs.map(r=>r.y)),right=Math.max(...rs.map(r=>r.right)),bottom=Math.max(...rs.map(r=>r.bottom));ink={x,y,w:right-x,h:bottom-y}}}return {index:i+1,tag:e.tagName.toLowerCase(),classes:e.className.baseVal||e.className,bbox:{x:r.x,y:r.y,w:r.width,h:r.height},inkBBox:ink,text:e.textContent.trim().replace(/\\s+/g,' '),html:e.outerHTML,font:{family:s.fontFamily,size:s.fontSize,weight:s.fontWeight,lineHeight:s.lineHeight,tracking:s.letterSpacing},paint:{background:s.backgroundColor,color:s.color,border:s.border,borderRadius:s.borderRadius},style:e.getAttribute('style')}})''')
  for x in items:
   x['id']=f'p{n:02d}-part-{x["index"]:02d}'
   for field in ['bbox','inkBBox']:
    if x[field]:x[field]={k:round(v,2) for k,v in x[field].items()}
  pages.append({'page':n,'source':f'replica/slide_{n:02d}.html','parts':items})
 b.close()
(P/'map-measurements.json').write_text(json.dumps({'canvas':{'w':1280,'h':720},'pages':pages},ensure_ascii=False,indent=2))
for p in pages:
 print('\nPAGE',p['page'])
 for x in p['parts']:print(x['index'],x['tag'],x['classes'],str(x['bbox']),x['text'][:80])
