"""Detect visible paint outside the allocated element rectangle, including shadows."""
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from sheets import context
import numpy as np
import json,threading,math,sys,hashlib
R=Path('/workspace/work/rebuild')
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass

def run(names,all_cases=False):
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R)));threading.Thread(target=server.serve_forever,daemon=True).start()
 with sync_playwright()as p:
  browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=browser.new_page(viewport={'width':1280,'height':720})
  for n in names:
   issues=[];checked=0;expected=0;missing=[];inputs={};v=R/n/'review';b=R/n/'build';base={}
   for mode in ['light','dark']:
    f=b/('paint-baseline-'+mode+'.html');f.write_text('<!doctype html><html><head><style>'+context(n)+'</style></head><body><section class="slide'+(' dark'if mode=='dark'else'')+'"><div class="page"><div class="body"></div></div></section></body></html>');page.goto(f'http://127.0.0.1:{server.server_port}/{n}/build/{f.name}');page.screenshot(path=str(f.with_suffix('.png')));base[mode]=Image.open(f.with_suffix('.png')).convert('RGB')
   for proof in sorted((v/'validation').glob('*.json')):
    if not (R/n/n/'elements'/proof.stem/'element.css').exists():continue
    q=json.loads(proof.read_text())
    if not isinstance(q,dict)or not isinstance(q.get('cases'),list)or'source_hashes'not in q:continue
    deps=[R/n/n/f for f in q['source_hashes']if f.endswith('.css')and f.startswith('elements/')]
    if not all_cases and not any(p.exists()and'box-shadow'in p.read_text()for p in deps):continue
    inputs[proof.stem]=q['source_hashes'];expected+=len(q['cases'])
    for a in q['cases']:
     gx,gy=a['grid'];f=b/'cells'/proof.stem/f"{a['fixture']}-{a['mode']}-{gx}x{gy}.png"
     if not f.exists():missing.append(str(f));continue
     x,y,w,h=a['bbox'];clip=(max(0,math.floor(x)-12),max(0,math.floor(y)-12),min(1280,math.ceil(x+w)+12),min(720,math.ceil(y+h)+12));im=Image.open(f).convert('RGB');bg=base[a['mode']].crop(clip)
     if im.size!=bg.size:continue
     arr=np.max(np.abs(np.asarray(im,dtype=np.int16)-np.asarray(bg,dtype=np.int16)),axis=2);xx=np.arange(im.width)+clip[0];yy=np.arange(im.height)+clip[1];outside=(xx[None,:]<math.floor(x)-1)|(xx[None,:]>=math.ceil(x+w)+1)|(yy[:,None]<math.floor(y)-1)|(yy[:,None]>=math.ceil(y+h)+1);bad=(arr>=4)&outside;checked+=1
     if bad.sum()>3:
      ys,xs=np.where(bad);issues.append({'leaf':proof.stem,'fixture':a['fixture'],'mode':a['mode'],'grid':a['grid'],'visible_pixels':int(bad.sum()),'max_delta':int(arr[bad].max()),'outside_paint_bbox':[int(xs.min()+clip[0]),int(ys.min()+clip[1]),int(xs.max()-xs.min()+1),int(ys.max()-ys.min()+1)],'element_bbox':a['bbox'],'cell_sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
   report={'collection':n,'all_cases':all_cases,'expected_cases':expected,'missing_cells':missing,'source_hashes_by_leaf':inputs,'threshold':'4/255 channel difference outside a1px antialias margin; >3 pixels','checked_shadow_cases':checked,'issues':issues};(v/'validation/raster-paint-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(n,'shadow cases',checked,'visible bleed',len(issues),flush=True)
  browser.close()
 server.shutdown()
if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument('collections',nargs='*');parser.add_argument('--all',action='store_true');args=parser.parse_args();run(args.collections or list(json.loads((R/'profiles.json').read_text())),args.all)
