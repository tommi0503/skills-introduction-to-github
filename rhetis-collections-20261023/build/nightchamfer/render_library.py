from pathlib import Path
import os,re,json,threading,http.server,functools,math
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import fitz
R=Path('/workspace/output/nightchamfer-review');C=Path('/workspace/output/nightchamfer');W=Path('/workspace/work/nightchamfer');(W/'captures').mkdir(exist_ok=True)
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',8765),functools.partial(Quiet,directory=str(R)));threading.Thread(target=server.serve_forever,daemon=True).start()
checks=[]
only=os.environ.get("NC_ONLY")
oldchecks={ (x["mode"],x["fixture"]):x for x in json.loads((R/"library"/"checks.json").read_text())} if (R/"library"/"checks.json").exists() else {}
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for mode in ['light','dark']:
  page.goto(f'http://127.0.0.1:8765/library/{mode}.html');page.evaluate('document.fonts.ready');
  # Render the exact preview.py sheet, one complete fixture at a time at its native scale.
  page.add_style_tag(content='body{display:block!important;margin:0!important;padding:0!important;background:white!important}article{display:none!important}article.active{display:block!important}article>h2{display:none!important}article > .frame{width:1280px!important;height:720px!important;border-radius:0!important}article > .frame>.slide{transform:none!important}')
  count=page.locator('article').count();doc=fitz.open();groups={}
  for i in range(count):
   art=page.locator('article').nth(i);page.evaluate('(i)=>{document.querySelectorAll("article").forEach((a,j)=>a.classList.toggle("active",i===j))}',i)
   title=art.locator(':scope > h2').inner_text();name=title.split(' / ')[0];stem=title.split(' / ')[1].split(' min ')[0];(W/'captures'/mode/name).mkdir(parents=True,exist_ok=True)
   png=W/'captures'/mode/name/f'{stem}.png';
   if not only or name in only.split(","):page.screenshot(path=str(png))
   groups.setdefault(name,[]).append(png)
   pg=doc.new_page(width=1280,height=720);pg.insert_image(pg.rect,filename=str(png))
   issues=page.evaluate('''()=>{let root=document.querySelector('article.active .slide');return [...root.querySelectorAll('*')].filter(e=>{let s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0&&(r.left<-1||r.top<-1||r.right>1281||r.bottom>721)}).map(e=>({tag:e.tagName,cls:e.className,text:e.innerText?.slice(0,60)})).slice(0,15)}''')
   checks.append({'mode':mode,'fixture':title,'font':page.evaluate("document.fonts.check('20px \"Pretendard Variable\"')"),'bounds':issues})
  doc.save(R/'library'/f'library-{mode}.pdf',deflate=True)
  for name,files in groups.items():
   folder=R/'library'/'elements'/name;folder.mkdir(parents=True,exist_ok=True)
   cols=2 if len(files)>1 else 1;rows=math.ceil(len(files)/cols);cellw=1280//cols;cellh=min(720//rows,cellw*720//1280);image=Image.new('RGB',(1280,720),'#e5e5e5');draw=ImageDraw.Draw(image)
   for j,f in enumerate(files):
    im=Image.open(f).convert('RGB');im.thumbnail((cellw,cellh-18));x=(j%cols)*cellw;y=(j//cols)*cellh
    draw.text((x+6,y+3),f.stem,fill='#333');image.paste(im,(x,y+18))
   image.save(folder/f'{mode}.png')
 b.close()
(R/'library'/'checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
print('fixture renders',len(checks),'issues',sum(bool(x['bounds'])for x in checks))
