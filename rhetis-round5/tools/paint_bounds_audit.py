"""Resolve DOM font-metric candidates by measuring actual whole-canvas paint.

No source is changed. A visibility-only paired screenshot isolates the complete
component, including its pseudo-elements, from the otherwise identical page.
This never resolves clipping, overlap, or any actually painted outside pixel.
"""
from pathlib import Path
import argparse,datetime,io,json,re,hashlib
from PIL import Image,ImageChops
from playwright.sync_api import sync_playwright
from sheets import ROOT,HTTP,style,fingerprint,minimum,sizing

def run(k,leaf,assembly=False):
 P=ROOT/(k+'-project');D=P/'paint-proofs';D.mkdir(exist_ok=True);rows=[]
 checks=json.loads((P/'sheets'/f'{leaf}-checks.json').read_text())
 fs=sorted((P/k/'elements'/leaf/'fixtures').glob('*.html'))
 url=HTTP+str((P/'sheet-runtime/paint-bounds-proof.html').relative_to(ROOT))
 skeleton='<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="../assets/fonts/fonts.css"><style>html,body{margin:0;width:1280px;height:720px}*{box-sizing:border-box}'+style(P,k)+'</style><section class="slide"><div class="page"><div class="body"></div></div></section>'
 with sync_playwright()as pw:
  browser=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);page=browser.new_page(viewport={'width':1280,'height':720})
  page.route(url,lambda route:route.fulfill(status=200,content_type='text/html',body=skeleton))
  cases=[(f,'original',None)for f in sorted((P/'reassembled').glob('slide_*.html'))if ('data-el="'+k+'-'+leaf+'"')in f.read_text()]if assembly else[(f,mode,sz)for f in fs for mode in['light','dark']for sz in sizing(minimum(f))]
  for f,mode,sz in cases:
   if assembly:page.goto(HTTP+str(f.relative_to(ROOT)))
   else:
    page.goto(url);page.locator('.slide').evaluate('(e,m)=>e.classList.toggle("dark",m==="dark")',mode)
    page.locator('.body').evaluate('(e,s)=>e.innerHTML=s',re.sub(r'^<!--.*?-->\s*','',f.read_text(),count=1,flags=re.S))
    page.locator('.body>*').evaluate('(e,s)=>{e.style.gridColumn="1 / span "+s[0];e.style.gridRow="1 / span "+s[1]}',sz)
   page.evaluate('document.fonts.ready');page.wait_for_timeout(70)
   roots=page.locator('[data-el="'+k+'-'+leaf+'"]')
   for i in range(roots.count()):
    el=roots.nth(i);rr=el.bounding_box();normal=page.screenshot();before=Image.open(io.BytesIO(normal)).convert('RGB');saved=el.get_attribute('style')
    el.evaluate('(e)=>e.style.setProperty("visibility","hidden","important")');base=Image.open(io.BytesIO(page.screenshot())).convert('RGB')
    el.evaluate('(e,s)=>s===null?e.removeAttribute("style"):e.setAttribute("style",s)',saved)
    mask=ImageChops.difference(before,base).convert('L').point(lambda x:255 if x>5 else 0);box=mask.getbbox()
    outside=box is None or box[0]<rr['x']-1 or box[1]<rr['y']-1 or box[2]>rr['x']+rr['width']+1 or box[3]>rr['y']+rr['height']+1
    row={'fixture':f.name,'mode':mode,'size':list(sz)if sz else None,'instance':i,'root':rr,'physicalPaintBounds':box,'actualOutside':bool(outside),'pageSize':[1280,720],'htmlSHA256':hashlib.sha256(f.read_bytes()).hexdigest()if assembly else None};rows.append(row)
    if assembly or sz==minimum(f):
     name=f'{leaf}--{f.stem}--{mode}'+('--assembly'if assembly else'--min')+'.png';(D/name).write_bytes(normal);row['screenshot']=name
  browser.close()
 report={'schema':'rhetis.painted-bounds/1','collection':k,'leaf':leaf,'scope':'assembly'if assembly else'fixture-matrix','generatedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sourceFingerprint':fingerprint(P,k,None if assembly else leaf),'method':'Paired whole1280x720 screenshots: component visibility hidden while all layout remains identical; difference luminance threshold5; one-pixel antialias tolerance. Raw DOM font metrics remain preserved. No clipping or overlap is resolved.','cases':rows,'actualOutside':sum(x['actualOutside']for x in rows)}
 out=D/(leaf+('-assembly'if assembly else'-matrix')+'.json');out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(k,leaf,report['scope'],len(rows),'cases',report['actualOutside'],'painted overflow')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('collection');a.add_argument('leaf');a.add_argument('--assembly',action='store_true');v=a.parse_args();run(v.collection,v.leaf,v.assembly)
