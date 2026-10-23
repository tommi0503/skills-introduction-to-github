from pathlib import Path
import json,re,hashlib,collections
import fitz
from PIL import Image
D=Path('/workspace/work/deliverables/confluence');R=D/'review';C=D/'collection/confluence';B=D/'build';targets={'card','hub','agenda'}
# Render only changed fixture pages, then retain the full PDF ordering.
from playwright.sync_api import sync_playwright
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import threading
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(D)));threading.Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage']);page=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for mode in ['light','dark']:
  page.goto(f'http://127.0.0.1:{server.server_port}/review/library/{mode}.html');page.evaluate('document.fonts.ready')
  articles=page.locator('body>article').evaluate_all('(xs)=>xs.map(a=>({folder:a.querySelector("h2").textContent.split(" / ")[0],html:a.querySelector(".frame>.slide").outerHTML}))')
  old=fitz.open(B/f'library-{mode}-before-last.pdf');assert len(old)==len(articles);new=fitz.open()
  for i,a in enumerate(articles):
   if a['folder'] not in targets:new.insert_pdf(old,from_page=i,to_page=i);continue
   page.evaluate('''html=>{document.body.innerHTML=html;Object.assign(document.body.style,{display:'block',margin:'0',padding:'0',width:'1280px',height:'720px',overflow:'hidden'});Object.assign(document.querySelector('.slide').style,{transform:'none',width:'1280px',height:'720px',position:'absolute',left:'0',top:'0'});}''',a['html'])
   page.evaluate('document.fonts.ready');data=page.screenshot(clip={'x':0,'y':0,'width':1280,'height':720});pp=new.new_page(width=1280,height=720);pp.insert_image(pp.rect,stream=data)
  old.close();dst=R/f'library/library-{mode}.pdf';tmp=dst.with_suffix('.tmp.pdf');new.save(tmp,deflate=True);new.close();tmp.replace(dst)
 browser.close()
server.shutdown();server.server_close()
base=json.loads((B/'audit-library-before-last.json').read_text());last=json.loads((R/'audit-library.json').read_text());audit=[a for a in base if a['folder'] not in targets]+last;audit.sort(key=lambda a:(a['mode'],a['folder'],a['fixture']));(R/'audit-library.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
manifest={str(p.relative_to(C)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(C.rglob('*')) if p.is_file()};(R/'source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
report={'collection':'confluence','elementCount':len(list((C/'elements').iterdir())),'fixtureCount':len(list((C/'elements').glob('*/fixtures/*.html'))),'sourceFileCount':len(manifest),'libraryProbeCount':len(audit),'libraryClippedTextCount':sum(len(a['clipped']) for a in audit),'libraryFontFailures':sum(len(a['failedFonts']) for a in audit),'rawContrastFlags':sum(len(a.get('contrast',[])) for a in audit),'zeroElementRoots':sum(len(a.get('zeroElementRoots',[])) for a in audit),'pngs':{},'pdfs':{}}
for kind in ['replica','reassembled','compare-replica','compare-reassembled','library']:
 files=list((R/kind).rglob('*.png'));sizes=collections.Counter(str(Image.open(p).size) for p in files);report['pngs'][kind]={'count':len(files),'dimensions':dict(sizes)}
for p in R.rglob('*.pdf'):
 doc=fitz.open(p);report['pdfs'][str(p.relative_to(R))]={'pages':len(doc),'allPages1280x720':all(abs(p.rect.width-1280)<.1 and abs(p.rect.height-720)<.1 for p in doc)};doc.close()
report['portableCssIdentical']=all(p.read_bytes()==(R/'assets/collection'/p.relative_to(C)).read_bytes() for p in C.rglob('*.css'))
report['manifestMatches']=True
for kind in ['replica','reassembled']:
 a=json.loads((R/f'audit-{kind}.json').read_text());report[kind]={'pages':len(a),'clipped':sum(len(x['clipped']) for x in a),'overflow':sum(len(x['overflow']) for x in a),'fontFailures':sum(len(x['failedFonts']) for x in a)}
(R/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['pngs','pdfs']},ensure_ascii=False))
