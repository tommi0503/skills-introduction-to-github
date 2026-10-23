from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import fitz,json,threading,http.server,functools
server=http.server.ThreadingHTTPServer(("127.0.0.1",18765),functools.partial(http.server.SimpleHTTPRequestHandler,directory="/workspace/output/nightchamfer-review"));threading.Thread(target=server.serve_forever,daemon=True).start()
R=Path('/workspace/output/nightchamfer-review'); D=Path('/workspace/work/deck/miricanvas_기업_selected/005_1kqlf_검정_모던_사업_계획_설명회_홍보')
report=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']); page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for i in range(1,19):
  src=R/'replica'/f'slide_{i:02}.html';page.goto("http://127.0.0.1:18765/"+str(src.relative_to(R)));page.evaluate('document.fonts.ready');page.screenshot(path=str(src.with_suffix('.png')))
  report.append({'page':i,'fonts':page.evaluate("document.fonts.check('20px \"Pretendard Variable\"')"),'size':page.locator('section').bounding_box()})
  o=Image.open(D/f'slide_{i:02}.png').convert('RGB');r=Image.open(src.with_suffix('.png')).convert('RGB');im=Image.new('RGB',(2560,720));im.paste(o,(0,0));im.paste(r,(1280,0));im.save(R/'compare-replica'/f'slide_{i:02}.png')
 b.close()
doc=fitz.open()
for i in range(1,19):
 pg=doc.new_page(width=1280,height=720);pg.insert_image(pg.rect,filename=str(R/'replica'/f'slide_{i:02}.png'))
doc.save(R/'replica'/'replica.pdf')
(R/'replica'/'checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
