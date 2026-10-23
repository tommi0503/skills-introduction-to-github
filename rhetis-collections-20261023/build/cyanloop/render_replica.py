from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import json,threading,http.server,functools
server=http.server.ThreadingHTTPServer(('127.0.0.1',8768),functools.partial(http.server.SimpleHTTPRequestHandler,directory='/workspace/output/cyanloop-review'))
threading.Thread(target=server.serve_forever,daemon=True).start()
R=Path('/workspace/output/cyanloop-review');D=Path('/workspace/work/deck/miricanvas_기업_selected/003_1la0o_하늘색_모던_교육_자료')
report=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for f in sorted((R/'replica').glob('slide_*.html')):
  page.goto('http://127.0.0.1:8768/replica/'+f.name);page.evaluate('document.fonts.ready');page.screenshot(path=str(f.with_suffix('.png')))
  report.append({'page':f.stem,'size':page.evaluate('[innerWidth,innerHeight]'),'fonts':page.evaluate('document.fonts.check("20px Anton")'),'overflow':page.evaluate('Array.from(document.querySelectorAll(".t")).filter(e=>{let r=e.getBoundingClientRect();return r.right>1280||r.bottom>720||r.left<0||r.top<0}).map(e=>e.textContent)')})
  out=Image.new('RGB',(2560,720),'white');out.paste(Image.open(D/f.with_suffix('.png').name),(0,0));out.paste(Image.open(f.with_suffix('.png')),(1280,0));out.save(R/'compare-replica'/f.with_suffix('.png').name)
 b.close()
imgs=[Image.open(f).convert('RGB') for f in sorted((R/'replica').glob('slide_*.png'))];imgs[0].save(R/'replica'/'replica.pdf',save_all=True,append_images=imgs[1:],resolution=96)
(R/'replica'/'browser-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(report)
