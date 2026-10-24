from pathlib import Path
from playwright.sync_api import sync_playwright
import json,hashlib
P=Path(__file__).parent
rows=[]
with sync_playwright() as w:
 b=w.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);g=b.new_page(viewport={'width':1280,'height':720})
 for n in range(1,31):
  f=P/f'replica/slide_{n:02}.html';g.goto(f'http://127.0.0.1:8875/crossrail-project/replica/slide_{n:02}.html');g.evaluate('document.fonts.ready');g.wait_for_timeout(20)
  parts=g.evaluate('''()=>[...document.querySelector('.slide').children].map((e,i)=>{let r=e.getBoundingClientRect(),c=getComputedStyle(e);return {id:'source-'+(i+1),selector:'.slide > :nth-child('+(i+1)+')',tag:e.tagName.toLowerCase(),bbox:[r.x,r.y,r.width,r.height].map(v=>Math.round(v*100)/100),text:e.innerText||e.textContent||'',style:e.getAttribute('style')||'',typography:{family:c.fontFamily,size:c.fontSize,weight:c.fontWeight,lineHeight:c.lineHeight,tracking:c.letterSpacing},paint:{background:c.background,border:c.border,color:c.color},visible:c.display!=='none'&&c.visibility!=='hidden'&&r.width>0&&r.height>0}})''')
  rows.append({'page':n,'source':f'replica/slide_{n:02}.html','sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'parts':parts})
 b.close()
(P/'source-measurements.json').write_text(json.dumps({'viewport':[1280,720],'pages':rows},ensure_ascii=False,indent=2)+'\n')
print('pages',len(rows),'visible components',sum(sum(x['visible'] for x in r['parts']) for r in rows))
