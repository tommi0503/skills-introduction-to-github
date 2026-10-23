from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
import json
P=Path(__file__).parent;Q=P/'qa-fidelity-targets';Q.mkdir(exist_ok=True);src=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('078*'));results=[]
with sync_playwright()as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);q=b.new_page(viewport={'width':1280,'height':720})
 for n in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]:
  q.goto('http://127.0.0.1:8765/onboard-docket-project/reassembled/slide_'+str(n).zfill(2)+'.html',wait_until='networkidle');q.evaluate('document.fonts.ready');q.screenshot(path=str(Q/f'assembly_{n:02}.png'))
  im=Image.new('RGB',(2560,720));im.paste(Image.open(src/f'slide_{n:02}.png').convert('RGB'),(0,0));im.paste(Image.open(Q/f'assembly_{n:02}.png').convert('RGB'),(1280,0));im.save(Q/f'slide_{n:02}.png')
  data=q.evaluate('''()=>({viewport:[document.documentElement.scrollWidth,document.documentElement.scrollHeight],fonts:[...document.fonts].map(f=>[f.family,f.status]),head:[...document.querySelectorAll('.head .title')].map(e=>{let r=e.getBoundingClientRect();return [r.x,r.y,r.width,r.height]})})''');results.append({'slide':n,**data})
 b.close()
(Q/'checks.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print('Fresh comparison pairs',len(results))
