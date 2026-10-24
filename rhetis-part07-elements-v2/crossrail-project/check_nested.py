from pathlib import Path
import sys,json,re
from playwright.sync_api import sync_playwright
sys.path.insert(0,'/workspace/work/rhetis-elements-v2/tools');import sheets
P=Path(__file__).parent;K=P/'crossrail';out=[]
(P/'nested-runtime.html').write_text('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="assets/fonts/fonts.css"><style>'+sheets.style(P,'crossrail')+'</style></head><body><section class="slide"><div class="page"><div class="body"></div></div></section></body></html>')
with sync_playwright() as q:
 b=q.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720});page.goto('http://127.0.0.1:8875/crossrail-project/nested-runtime.html');page.evaluate('document.fonts.ready')
 for f in sorted((K/'elements').glob('*/fixtures/*.html')):
  for size in {sheets.minimum(f),(12,6)}:
   for dark in [False,True]:
    data={'html':f.read_text(),'cols':size[0],'rows':size[1],'dark':dark}
    bad=page.evaluate('''d=>{document.querySelector('.slide').className='slide'+(d.dark?' dark':'');let body=document.querySelector('.body');body.innerHTML=d.html;let r=body.firstElementChild;r.style.gridColumn='1/span '+d.cols;r.style.gridRow='1/span '+d.rows;return [...body.querySelectorAll('[data-el],.seat,.mark,.icon,.bullet,.donut,.stat')].filter(x=>getComputedStyle(x).display!=='none').map(x=>({cls:x.className,box:[x.offsetWidth,x.offsetHeight]})).filter(x=>x.box[0]<1||x.box[1]<1)}''',data)
    if bad:out.append({'fixture':str(f.relative_to(K)),'size':size,'dark':dark,'zero':bad})
 b.close()
(P/'nested-root-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('zero nested roots/parts',len(out))
