from pathlib import Path
import json,importlib.util,fitz,hashlib
from playwright.sync_api import sync_playwright
B=Path('/workspace/work/deliverables/inflexion');R=B/'review';L=R/'library'
spec=importlib.util.spec_from_file_location('shared','/workspace/work/tools/render_review.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
report=[]
with sync_playwright() as p:
 b=m.browser(p);pg=b.new_page(viewport={'width':1328,'height':900});probe=b.new_page(viewport={'width':1280,'height':720})
 for mode in ['light','dark']:
  m.load(pg,L/f'{mode}-sizes.html');m.load(probe,L/f'{mode}.html');probe.add_style_tag(content='body{display:block;margin:0;padding:0;width:1280px;height:720px;overflow:hidden}body>.slide{width:1280px;height:720px;transform:none;position:relative}')
  items=pg.locator('body>article[data-cols="12"][data-rows="6"]').all();updates={}
  for i,a in enumerate(items):
   if a.get_attribute('data-folder')!='headline':continue
   probe.evaluate('(h)=>document.body.innerHTML=h',a.locator('.slide').evaluate('(e)=>e.outerHTML'));probe.evaluate('document.fonts.ready');probe.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
   updates[i]=probe.screenshot(clip={'x':0,'y':0,'width':1280,'height':720},animations='disabled')
  src=fitz.open(L/f'library-{mode}.pdf');dst=fitz.open();assert len(src)==len(items)==174
  for i in range(len(src)):
   if i in updates:page=dst.new_page(width=1280,height=720);page.insert_image(page.rect,stream=updates[i])
   else:dst.insert_pdf(src,from_page=i,to_page=i)
  tmp=L/f'library-{mode}-updated.pdf';dst.save(tmp,deflate=True);dst.close();src.close();tmp.replace(L/f'library-{mode}.pdf');report.append({'mode':mode,'updatedHeadlinePages':[i+1 for i in updates],'totalPages':len(items)})
 b.close()
old=json.loads((R/'audit-library-before-headline-compact.json').read_text());new=json.loads((R/'audit-library.json').read_text());merged=[x for x in old if x['folder']!='headline']+new;assert len(merged)==700;(R/'audit-library.json').write_text(json.dumps(merged,ensure_ascii=False,indent=2));(R/'audit-headline-pdf-update.json').write_text(json.dumps(report,indent=2));print(json.dumps(report))
