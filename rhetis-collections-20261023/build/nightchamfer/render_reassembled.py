from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import fitz,json,threading,http.server,functools
R=Path('/workspace/output/nightchamfer-review');D=Path('/workspace/work/deck/miricanvas_기업_selected/005_1kqlf_검정_모던_사업_계획_설명회_홍보')
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',8768),functools.partial(Quiet,directory=str(R)));threading.Thread(target=server.serve_forever,daemon=True).start()
report=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for i in range(1,19):
  src=R/'reassembled'/f'slide_{i:02}.html';page.goto('http://127.0.0.1:8768/reassembled/'+src.name);page.evaluate('document.fonts.ready');page.screenshot(path=str(src.with_suffix('.png')))
  report.append({'page':i,'font':page.evaluate("document.fonts.check('20px \"Pretendard Variable\"')"),'size':page.locator('section').bounding_box(),'overflow':page.evaluate('''()=>[...document.querySelectorAll('.slide *')].filter(e=>{let r=e.getBoundingClientRect(),s=getComputedStyle(e);return r.width>0&&r.height>0&&s.display!=='none'&&(r.left<-1||r.top<-1||r.right>1281||r.bottom>721)}).map(e=>({class:e.className,text:e.innerText?.slice(0,70)}))''')})
  o=Image.open(D/f'slide_{i:02}.png').convert('RGB');r=Image.open(src.with_suffix('.png')).convert('RGB');im=Image.new('RGB',(2560,720));im.paste(o,(0,0));im.paste(r,(1280,0));im.save(R/'compare-reassembled'/f'slide_{i:02}.png')
 b.close()
doc=fitz.open()
for i in range(1,19):
 pg=doc.new_page(width=1280,height=720);pg.insert_image(pg.rect,filename=str(R/'reassembled'/f'slide_{i:02}.png'))
doc.save(R/'reassembled'/'reassembled.pdf',deflate=True)
(R/'reassembled'/'checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('pages',len(report),'overflow',sum(bool(x['overflow'])for x in report))
