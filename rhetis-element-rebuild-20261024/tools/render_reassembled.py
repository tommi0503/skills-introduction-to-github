from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw,ImageFont
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import threading,json,io,sys,hashlib
from sheets import JS,check_contrast
R=Path('/workspace/work/rebuild');OLD=Path('/workspace/work/delivery');MAN=json.loads(Path('/workspace/work/image-manifest.json').read_text());DECKS=dict(zip(['tide-tab','cutfield','filament','portico','toggle-grid','lamella','rulemark'],['020','022','024','026','027','028','030']))
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R)));threading.Thread(target=server.serve_forever,daemon=True).start()
FONT=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',18)
def run(name,only=None):
 V=R/name/'review';o=V/'compare-reassembled';o.mkdir(exist_ok=True);qa=[];D=V/'reassembled';files=sorted(D.glob('slide_*.html'))
 if only:files=[f for f in files if f.stem[-2:]in only]
 with sync_playwright()as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-breakpad']);pg=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1);pg.route('**/*',lambda r:r.continue_())
  for f in files:
   page=f.stem[-2:];pg.goto(f'http://127.0.0.1:{server.server_port}/{name}/review/reassembled/{f.name}');pg.evaluate('document.fonts.ready');pg.wait_for_timeout(60)
   dims=pg.locator('.slide').bounding_box();checks=pg.evaluate('''()=>({size:[document.querySelector('.slide').offsetWidth,document.querySelector('.slide').offsetHeight],fontChecks:[...new Set([...document.querySelectorAll('.slide *')].filter(e=>e.textContent.trim()).map(e=>{let s=getComputedStyle(e);return s.fontSize+' '+s.fontFamily}))].map(f=>({font:f,loaded:document.fonts.check(f)})),elementBoxes:[...document.querySelectorAll('.body>[data-el]')].map(e=>{let r=e.getBoundingClientRect();return {el:e.dataset.el,bbox:[r.x,r.y,r.width,r.height]}}),textOutsidePage:[...document.querySelectorAll('.slide *')].filter(e=>e.childNodes.length&&[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim())).flatMap(e=>{let r=e.getBoundingClientRect();return r.left<-.5||r.top<-.5||r.right>1280.5||r.bottom>720.5?[{text:e.textContent.slice(0,80),bbox:[r.x,r.y,r.width,r.height]}]:[]})})''')
   shot=Image.open(io.BytesIO(pg.locator('.slide').screenshot())).convert('RGB');shot.save(D/(f.stem+'.png'),optimize=True);assert shot.size==(1280,720)
   orig=next(x for x in MAN if x['deck'].startswith(DECKS[name])and x['file']=='slide_'+page+'.png');original=Image.open(Path('/workspace')/orig['path']).convert('RGB');rep=Image.open(OLD/name/'review/replica'/('slide_'+page+'.png')).convert('RGB')
   comp=Image.new('RGB',(3840,752),'#e7e7ea');draw=ImageDraw.Draw(comp)
   for k,(label,im)in enumerate([('Original',original),('Frozen replica',rep),('Contract reassembly',shot)]):draw.text((k*1280+12,6),label,fill='#151515',font=FONT);comp.paste(im,(k*1280,32))
   comp.save(o/(f.stem+'.png'),optimize=True);checks.update({'page':page,'source_html_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'png_size':list(shot.size),'comparison_size':list(comp.size)});qa.append(checks);print(name,page,checks['size'],'fontfail',sum(not f['loaded']for f in checks['fontChecks']),flush=True)
  b.close()
 old=V/'validation/reassembled.json'
 if only and old.exists():
  olddata=json.loads(old.read_text());qa=[x for x in olddata['pages']if x['page']not in only]+qa
 old.write_text(json.dumps({'collection':name,'pages':qa},ensure_ascii=False,indent=2))
if __name__=='__main__':
 names=sys.argv[1:]or list(DECKS)
 for n in names:run(n)
 server.shutdown()
