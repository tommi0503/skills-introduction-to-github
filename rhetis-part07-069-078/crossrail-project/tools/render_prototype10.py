from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import json
p=Path(__file__).parent
with sync_playwright() as w:
 b=w.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);g=b.new_page(viewport={'width':1280,'height':720})
 for stage in ['replica','reassembled']:
  g.goto(f'http://127.0.0.1:8765/crossrail-project/{stage}/slide_10.html');g.evaluate('document.fonts.ready');g.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');g.wait_for_timeout(100);g.screenshot(path=str(p/'qa'/f'prototype10-{stage}.png'))
  if stage=='reassembled':
   d=g.evaluate('''()=>Object.fromEntries(['.kicker','.title','.no','[data-el="crossrail-headline"] h2','.steps','.step .mark','.step .name','.step .icon','.step .note'].map(s=>{let e=document.querySelector(s),r=e.getBoundingClientRect(),c=getComputedStyle(e);return[s,{bbox:[r.x,r.y,r.width,r.height],font:c.fontFamily,size:c.fontSize,line:c.lineHeight,text:e.textContent}]}))''');(p/'qa/prototype10-geometry.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
 b.close()
orig=Image.open(p/'qa/original-10.png');r=Image.open(p/'qa/prototype10-reassembled.png');x=Image.new('RGB',(2560,720));x.paste(orig);x.paste(r,(1280,0));x.save(p/'qa/prototype10-compare.png')
print('prototype rendered')
