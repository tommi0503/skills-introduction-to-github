from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import json,fitz,threading,http.server,functools,io
R=Path('/workspace/output/glasspulse-review')
class H(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',8139),functools.partial(H,directory=R));threading.Thread(target=server.serve_forever,daemon=True).start()
import sys
targets=sys.argv[1:] or ['matrix','tag','delta','gauge','pill','card','list','pricing','versus','person']
checks=json.load(open(R/'library/checks.json'))
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1320,'height':780},device_scale_factor=1)
 for mode in ['light','dark']:
  page.goto(f'http://127.0.0.1:8139/library/{mode}.html');page.evaluate('document.fonts.ready');page.add_style_tag(content='body{display:block;padding:0}article{width:1280px;margin:0}.frame{width:1280px;height:720px;border-radius:0}.frame>.slide{transform:none}article>h2{display:none}')
  groups={};doc=fitz.open(R/'library'/f'library-{mode}.pdf');arts=page.locator('article')
  for i in range(arts.count()):
   art=arts.nth(i);name=art.locator(':scope > h2').inner_text().split(' / ');folder=name[0];fixture=name[1].split(' min ')[0]
   if folder not in targets:continue
   art.scroll_into_view_if_needed();png=art.locator(':scope > .frame').screenshot();groups.setdefault(folder,[]).append((fixture,Image.open(io.BytesIO(png)).convert('RGB')))
   one=fitz.open();pg=one.new_page(width=1280,height=720);pg.insert_image(pg.rect,stream=png);doc.delete_page(i);doc.insert_pdf(one,start_at=i)
   issues=art.evaluate('''a=>{let o=[];for(let e of a.querySelectorAll('[data-el]'))if(e.scrollWidth>e.clientWidth+3||e.scrollHeight>e.clientHeight+3)o.push({name:e.className,text:e.innerText.slice(0,60),x:e.scrollWidth-e.clientWidth,y:e.scrollHeight-e.clientHeight});return o}''')
   for c in checks:
    if c['mode']==mode and c['element']==folder and c['fixture']==fixture:c['issues']=issues
  tmp=R/'library'/f'patched-{mode}.pdf';doc.save(tmp,garbage=4,deflate=True,deflate_images=True);doc.close();tmp.replace(R/'library'/f'library-{mode}.pdf')
  for folder,ims in groups.items():
   out=Image.new('RGB',(1280,390*((len(ims)+1)//2)),'#ddd');d=ImageDraw.Draw(out)
   for k,(f,im) in enumerate(ims):
    x=k%2*640;y=k//2*390;out.paste(im.resize((640,360)),(x,y+30));d.text((x+12,y+8),f,fill='#222')
   out.save(R/'library'/folder/f'{mode}.png')
 b.close()
(R/'library/checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));print('patched matrix,tag,delta,gauge,pill')
