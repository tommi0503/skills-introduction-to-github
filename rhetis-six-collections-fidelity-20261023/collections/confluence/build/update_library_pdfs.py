from pathlib import Path
from playwright.sync_api import sync_playwright
import fitz,json
R=Path('/workspace/work/deliverables/confluence/review');targets={'chart-donut','waffle','matrix','person','radar','cycle','sankey','slope'}
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage']);page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for mode in ['light','dark']:
  page.goto('http://127.0.0.1:8020/review/library/'+mode+'.html');page.evaluate('document.fonts.ready')
  articles=page.locator('body>article').evaluate_all('(xs)=>xs.map(a=>({folder:a.querySelector("h2").textContent.split(" / ")[0],html:a.querySelector(".frame>.slide").outerHTML}))')
  old=fitz.open(R/'library'/f'library-{mode}.pdf');new=fitz.open();assert len(old)==len(articles),(len(old),len(articles))
  for i,a in enumerate(articles):
   folder=a['folder']
   if folder not in targets:new.insert_pdf(old,from_page=i,to_page=i);continue
   slide=a['html']
   page.evaluate('''html=>{document.body.innerHTML=html;Object.assign(document.body.style,{display:'block',margin:'0',padding:'0',width:'1280px',height:'720px',overflow:'hidden'});let s=document.querySelector('.slide');Object.assign(s.style,{transform:'none',width:'1280px',height:'720px',position:'absolute',left:'0',top:'0'});}''',slide)
   page.evaluate('document.fonts.ready');data=page.screenshot(clip={'x':0,'y':0,'width':1280,'height':720});pp=new.new_page(width=1280,height=720);pp.insert_image(pp.rect,stream=data)
  old.close();dst=R/'library'/f'library-{mode}.pdf';tmp=dst.with_suffix('.tmp.pdf');new.save(tmp,deflate=True);new.close();tmp.replace(dst)
 b.close()
old=json.loads((R.parent/'build/audit-library-round3-full.json').read_text());changed=json.loads((R/'audit-library.json').read_text());merged=[a for a in old if a['folder'] not in targets]+changed
merged.sort(key=lambda a:(a['mode'],a['folder'],a['fixture']));(R/'audit-library.json').write_text(json.dumps(merged,ensure_ascii=False,indent=2))
print('Updated library PDFs and merged audit:',len(merged),'probes')
