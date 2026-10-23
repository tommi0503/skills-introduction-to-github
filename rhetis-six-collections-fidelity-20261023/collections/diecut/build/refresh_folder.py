"""Refresh a frozen collection folder without discarding other review evidence or PDF pages."""
from pathlib import Path
import sys,json,subprocess,shutil,importlib.util
import fitz
sys.path.insert(0,'/workspace/work/tools');import render_review as rr
from playwright.sync_api import sync_playwright
R=Path('/workspace/work/deliverables/diecut');C=R/'collection/diecut';V=R/'review';names=set(sys.argv[1].split(','))
reportpath=V/'audit-library.json';old=json.load(open(reportpath))
cmd=['python','/workspace/work/tools/render_review.py','library','--root',str(R),'--name','diecut','--only',','.join(names)]
subprocess.run(cmd,check=True)
part=json.load(open(reportpath));reportpath.write_text(json.dumps([x for x in old if x['folder']not in names]+part,ensure_ascii=False,indent=2))
# Existing PDFs contain each fixture in deterministic foundation/element order.
folders=[('foundation',C/'foundation')]+[(p.name,p)for p in sorted((C/'elements').iterdir())if p.is_dir()]
index=[]
for name,folder in folders:
 for fixture in sorted((folder/'fixtures').glob('*.html')):index.append((name,fixture))
with sync_playwright() as p:
 b=rr.browser(p);pg=b.new_page(viewport={'width':1280,'height':720})
 for mode in ['light','dark']:
  htmlpath=V/'library'/f'{mode}.html';rr.load(pg,htmlpath)
  head=pg.locator('head').inner_html()
  articles=pg.locator('body>article').all();contents=[x.locator('.slide').first.evaluate('(e)=>e.outerHTML')for x in articles]
  doc=fitz.open(V/'library'/f'library-{mode}.pdf')
  assert len(contents)==len(index)==len(doc)
  pg.add_style_tag(content='body{display:block;margin:0;padding:0;width:1280px;height:720px;overflow:hidden}body>.slide{width:1280px;height:720px;transform:none;position:relative}')
  for i,(name,fixture)in enumerate(index):
   if name not in names:continue
   pg.evaluate('(x)=>document.body.innerHTML=x',contents[i]);pg.evaluate('document.fonts.ready')
   data=pg.screenshot(clip={'x':0,'y':0,'width':1280,'height':720});doc[i].insert_image(doc[i].rect,stream=data,overlay=True)
  temp=V/'library'/f'.refreshed-{mode}.pdf';doc.save(temp,deflate=True);doc.close();temp.replace(V/'library'/f'library-{mode}.pdf')
 b.close()
shutil.copytree(C,V/'assets/collection',dirs_exist_ok=True)
print('Updated folders, audit evidence, standalone sheets, and complete PDFs:',','.join(names))
