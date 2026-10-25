"""Render the actual foundation fixtures in both official palette modes."""
from pathlib import Path
import sys,json,re,time,hashlib
from playwright.sync_api import sync_playwright
from sheets import ROOT,HTTP,style,AUDIT,fingerprint,raster_contrast
from PIL import Image

def run(k):
 p=ROOT/(k+'-project');out=p/'foundation-sheets';out.mkdir(exist_ok=True)
 runtime=p/'foundation-runtime';runtime.mkdir(exist_ok=True);fn=runtime/'stage.html';results=[]
 css='html,body{margin:0;width:1280px;height:720px}*{box-sizing:border-box}'+style(p,k)+'[data-icon]:empty::after{content:"";display:block;width:100%;height:100%;border:1.5px dashed currentColor;border-radius:50%;box-sizing:border-box}'
 with sync_playwright() as pw:
  b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);page=b.new_page(viewport={'width':1280,'height':720})
  for f in sorted((p/k/'foundation/fixtures').glob('*.html')):
   markup=re.sub(r'^<!--.*?-->\s*','',f.read_text(),count=1,flags=re.S)
   if not re.search(r'class=[\"\'][^\"\']*\bslide\b',markup):markup='<section class="slide"><div class="page"><div class="body">'+markup+'</div></div></section>'
   fn.write_text('<!doctype html><html lang="ko"><meta charset="utf-8"><link rel="stylesheet" href="../assets/fonts/fonts.css"><style>'+css+'</style><body>'+markup+'</body></html>')
   for mode in ['light','dark']:
    page.goto(HTTP+str(fn.relative_to(ROOT)),wait_until='networkidle');page.locator('.slide').evaluate('(e,m)=>e.classList.toggle("dark",m==="dark")',mode);page.evaluate('document.fonts.ready');page.wait_for_timeout(250)
    slide=page.locator('.slide');assert slide.count()==1
    file=out/(f.stem+'-'+mode+'.png');slide.screenshot(path=str(file),animations='disabled');im=Image.open(file);assert im.size==(1280,720)
    d=slide.evaluate(AUDIT);raster_contrast(d,im,{'x':0,'y':0});d.update(fixture=f.name,mode=mode,png=str(file.relative_to(p)),pngSHA256=hashlib.sha256(file.read_bytes()).hexdigest());results.append(d)
  b.close()
 (p/'foundation-checks.json').write_text(json.dumps({'collection':k,'sourceFingerprint':fingerprint(p,k),'generatedAtUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'fixtures':results},ensure_ascii=False,indent=2));print(k,len(results),'foundation renders')
if __name__=='__main__':
 for k in sys.argv[1:]:run(k)
