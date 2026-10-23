from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import json,fitz,threading,http.server,functools,io
R=Path('/workspace/output/glasspulse-review')
class Handler(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',8136),functools.partial(Handler,directory=R))
threading.Thread(target=server.serve_forever,daemon=True).start()
check=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1320,'height':780},device_scale_factor=1)
 for mode in ['light','dark']:
  page.goto(f'http://127.0.0.1:8136/library/{mode}.html');page.evaluate('document.fonts.ready')
  page.add_style_tag(content='body{display:block;padding:0}article{width:1280px;margin:0}.frame{width:1280px;height:720px;border-radius:0}.frame>.slide{transform:none}article>h2{display:none}')
  groups={};doc=fitz.open()
  arts=page.locator('article');n=arts.count()
  for i in range(n):
   art=arts.nth(i);name=art.locator(':scope > h2').inner_text().split(' / ');folder=name[0];fixture=name[1].split(' min ')[0]
   art.scroll_into_view_if_needed();frame=art.locator(':scope > .frame');png=frame.screenshot();im=Image.open(io.BytesIO(png)).convert('RGB');groups.setdefault(folder,[]).append((fixture,im))
   pg=doc.new_page(width=1280,height=720);pg.insert_image(pg.rect,stream=png)
   check.append({'mode':mode,'element':folder,'fixture':fixture,'font':page.evaluate('document.fonts.check("700 24px \\\"Pretendard Variable\\\"")'),'bounds':art.locator(':scope > .frame > .slide').bounding_box(),'issues':art.evaluate('''a=>{let issues=[];for(let el of a.querySelectorAll('[data-el]')){let r=el.getBoundingClientRect();if(el.scrollWidth>el.clientWidth+3||el.scrollHeight>el.clientHeight+3)issues.push({name:el.className,text:el.innerText.slice(0,60),x:el.scrollWidth-el.clientWidth,y:el.scrollHeight-el.clientHeight})}return issues}''')})
  doc.save(R/'library'/f'library-{mode}.pdf',garbage=4,deflate=True,deflate_images=True)
  for folder,ims in groups.items():
   rows=(len(ims)+1)//2;out=Image.new('RGB',(1280,rows*390),'#ddd');d=ImageDraw.Draw(out)
   for k,(f,im) in enumerate(ims):
    x=k%2*640;y=k//2*390;im=im.resize((640,360));out.paste(im,(x,y+30));d.text((x+12,y+8),f,fill='#222')
   dest=R/'library'/folder;dest.mkdir(exist_ok=True);out.save(dest/f'{mode}.png')
 b.close()
(R/'library'/'checks.json').write_text(json.dumps(check,ensure_ascii=False,indent=2));print('fixtures',len(check),'issues',sum(bool(c['issues']) for c in check))
