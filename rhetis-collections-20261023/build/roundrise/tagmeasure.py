from playwright.sync_api import sync_playwright
from pathlib import Path
import re
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);g=b.new_page(viewport={'width':1280,'height':720});g.goto('http://127.0.0.1:8760/roundrise-audit.html');h=re.sub('<!--.*?-->','',Path('output/roundrise/elements/tag/fixtures/extended.html').read_text(),flags=re.S);g.evaluate('(h)=>document.body.innerHTML=h','<section class="slide dark"><div class="page"><div class="body">'+h+'</div></div></section>');print(g.evaluate('''()=>{let e=document.querySelector('.tag'),r=e.getBoundingClientRect(),q=document.createRange();q.selectNodeContents(e);let tr=q.getBoundingClientRect(),s=getComputedStyle(e);return [s.backgroundColor,s.color,s.display,s.height,[r.x,r.y,r.width,r.height],[tr.x,tr.y,tr.width,tr.height]]}'''));b.close()
