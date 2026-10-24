"""Non-mutating frontier probes: source fixtures/CSS are never modified."""
from pathlib import Path
from http.server import ThreadingHTTPServer
from functools import partial
from playwright.sync_api import sync_playwright
from PIL import Image
import json,threading,io,sys,math
from sheets import ROOT,Quiet,context,minparse,JS,check_contrast

def probe(n,leaf,sizes):
 C=ROOT/n/n;D=ROOT/n/'build/probes'/leaf;D.mkdir(parents=True,exist_ok=True);V=ROOT/n/'review';sty=context(n);results=[]
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)));threading.Thread(target=server.serve_forever,daemon=True).start()
 with sync_playwright()as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-breakpad']);pg=b.new_page(viewport={'width':1280,'height':720})
  for f in sorted((C/'elements'/leaf/'fixtures').glob('*.html')):
   _,markup=minparse(f.read_text())
   for mode in ['light','dark']:
    dest=D/(f.stem+'-'+mode+'.html');dest.write_text('<!doctype html><html lang="ko"><head><meta charset="utf-8"><link rel="stylesheet" href="../../../review/assets/fonts/fonts.css"><style>'+sty+'</style></head><body><section class="slide'+(' dark'if mode=='dark'else'')+'"><div class="page"><div class="body">'+markup+'</div></div></section></body></html>');pg.goto(f'http://127.0.0.1:{server.server_port}/{n}/build/probes/{leaf}/{dest.name}');pg.evaluate('document.fonts.ready')
    for x,y in sizes:
     pg.locator('.body>:first-child').evaluate('(e,s)=>{e.style.gridColumn="1 / span "+s[0];e.style.gridRow="1 / span "+s[1]}',[x,y]);a=pg.evaluate(JS);im=Image.open(io.BytesIO(pg.screenshot())).convert('RGB');a['contrast']=check_contrast(im,a['texts']);a.pop('texts');a.update(fixture=f.stem,mode=mode,grid=[x,y]);results.append(a);xx,yy,w,h=a['bbox'];im.crop((max(0,math.floor(xx)-12),max(0,math.floor(yy)-12),min(1280,math.ceil(xx+w)+12),min(720,math.ceil(yy+h)+12))).save(D/f'{f.stem}-{mode}-{x}x{y}.png')
  b.close()
 server.shutdown();(D/'probe.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
 for a in results:
  errs={k:len(a[k])for k in ['outside','clipped','hidden','member_outside','overlaps','contrast','chip_alignment','shape_clipped','painted_outside']if a[k]};print(n,leaf,a['fixture'],a['mode'],a['grid'],errs)
 return results
if __name__=='__main__':probe(sys.argv[1],sys.argv[2],[tuple(map(int,s.split('x')))for s in sys.argv[3:]])
