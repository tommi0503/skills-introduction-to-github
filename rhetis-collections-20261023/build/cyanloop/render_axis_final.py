from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw,ImageFont
import json,http.server,functools,threading,subprocess,fitz,re
C=Path('/workspace/output/cyanloop');R=Path('/workspace/output/cyanloop-review');D=Path('/workspace/work/deck/miricanvas_기업_selected/003_1la0o_하늘색_모던_교육_자료');W=Path('/workspace/work/cyanloop');REF=Path('/workspace/work/reference')
for dark in (False,True):
 cmd=['python',str(REF/'tools/preview.py'),str(C),str(REF/'contract/type-steps.json'),'--out',str(R/'library'/('dark.html' if dark else 'light.html'))]
 if dark:cmd.insert(4,'--dark')
 subprocess.run(cmd,check=True)
 f=R/'library'/('dark.html' if dark else 'light.html');f.write_text(re.sub(r'href="file:[^"]+"','href="../fonts/fonts.css"',f.read_text()))
server=http.server.ThreadingHTTPServer(('127.0.0.1',8763),functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(R)));threading.Thread(target=server.serve_forever,daemon=True).start()
reports=[]
previous=json.loads((R/'library/browser-checks.json').read_text()) if (R/'library/browser-checks.json').exists() else []
selected={'chart-bar'}
reports=[r for r in previous if r.get('mode') in ('light','dark') and r.get('fixture','').split(' / ')[0] not in selected]
check="""() => {let roots=[...document.querySelectorAll('[data-el]')];return roots.flatMap(root=>{let rr=root.getBoundingClientRect();return [...root.querySelectorAll('.name,.fig,.note')].filter(e=>getComputedStyle(e).display!=='none').flatMap(e=>{let r=e.getBoundingClientRect();return r.right>rr.right+2||r.bottom>rr.bottom+2||r.left<rr.left-2||r.top<rr.top-2?[{root:root.dataset.el,text:e.textContent.slice(0,90),r:[r.x,r.y,r.width,r.height],rr:[rr.x,rr.y,rr.width,rr.height]}]:[];});});}"""
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for mode in ('light','dark'):
  doc=fitz.open(R/'library'/f'library-{mode}.pdf');page.goto(f'http://127.0.0.1:8763/library/{mode}.html');page.evaluate('document.fonts.ready')
  # Browser-built source sheet is retained; each article is then rendered at native slide dimensions.
  arts=page.locator('article');raw=[]
  for i in range(arts.count()):raw.append((arts.nth(i).locator('h2').first.inner_text(),arts.nth(i).locator('.slide').evaluate('(e)=>e.outerHTML')))
  by={}
  for i,(label,body) in enumerate(raw):
   name=label.split(' / ')[0]
   if name not in selected:continue
   base='<html lang="ko"><head><meta charset="utf-8"><link rel="stylesheet" href="../fonts/fonts.css"><link rel="stylesheet" href="runtime.css"></head><body style="margin:0">'+body+'</body></html>'
   temp=R/'library'/'_render.html';temp.write_text(base)
   page.goto(f'http://127.0.0.1:8763/library/_render.html?v={mode}-{i}');page.evaluate('document.fonts.ready');blob=page.screenshot()
   tmp=W/f'{mode}-{i:03}.png';tmp.write_bytes(blob);by.setdefault(name,[]).append((label,tmp))
   pg=doc[i];pg.insert_image(pg.rect,stream=blob)
   issues=page.evaluate(check);reports.append({'mode':mode,'fixture':label,'fonts':page.evaluate('document.fonts.check("20px \\\"Pretendard Variable\\\"") && document.fonts.check("20px \\\"Do Hyeon\\\"")'),'issues':issues})
  pdfpath=R/'library'/f'library-{mode}.pdf';tmppdf=pdfpath.with_suffix('.tmp.pdf');doc.save(tmppdf,deflate=True);doc.close();tmppdf.replace(pdfpath)
  for name,items in by.items():
   cols=2;rows=(len(items)+1)//2;im=Image.new('RGB',(1280,rows*388),'#ddd');dr=ImageDraw.Draw(im)
   for j,(label,tmp) in enumerate(items):
    x=j%2*640;y=j//2*388;thumb=Image.open(tmp);thumb.thumbnail((640,360));im.paste(thumb,(x,y+28));dr.text((x+10,y+8),label.split(' / ')[1],fill='#222')
   (R/'library'/name).mkdir(exist_ok=True);im.save(R/'library'/name/f'{mode}.png')
  (R/'library'/'_render.html').unlink(missing_ok=True)
 for folder,compare,pdfname in [('reassembled','compare-reassembled','reassembled.pdf')]:
  doc=fitz.open()
  for f in sorted((R/folder).glob('slide_*.html')):
   page.goto(f'http://127.0.0.1:8763/{folder}/{f.name}');page.evaluate('document.fonts.ready');blob=page.screenshot();f.with_suffix('.png').write_bytes(blob)
   pg=doc.new_page(width=960,height=540);pg.insert_image(pg.rect,stream=blob)
   im=Image.new('RGB',(2560,720),'white');im.paste(Image.open(D/f.with_suffix('.png').name),(0,0));im.paste(Image.open(f.with_suffix('.png')),(1280,0));im.save(R/compare/f.with_suffix('.png').name)
   reports.append({'mode':folder,'page':f.name,'size':page.evaluate('[innerWidth,innerHeight]'),'issues':page.evaluate(check)})
  doc.save(R/folder/pdfname,deflate=True)
 b.close()
(R/'library/browser-checks.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2));print('RENDERED',len(reports),'pages;',sum(len(i['issues']) for i in reports),'bounding issues')
