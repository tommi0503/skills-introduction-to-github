from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import re,json
R=Path(__file__).parent;C=R.parent/'corner-signal';issues=[]
for f in (R/'library').glob('*.html'):f.write_text(f.read_text().replace('file:///workspace/work/ref/fonts/fonts.css','../../fonts/fonts.css'))
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for mode in ['light','dark']:
  page.goto('http://127.0.0.1:8765/corner-signal-review/library/'+mode+'.html');page.evaluate('document.fonts.ready')
  # Original standard preview remains intact; render one full-size fixture at a time.
  articles=page.locator('article');length=articles.count();sheets={};pdf=[]
  for i in range(length):
   a=articles.nth(i);label=a.locator(':scope > h2').inner_text();element=label.split(' / ')[0];fixture=label.split(' / ')[1].split(' min ')[0]
   page.evaluate("""i=>{document.querySelectorAll('article').forEach((a,n)=>a.style.display=n===i?'block':'none');document.body.style.cssText='margin:0;padding:0;display:block;background:white';let f=document.querySelectorAll('article')[i].querySelector('.frame');f.style.cssText='width:1280px;height:720px;overflow:hidden';f.firstElementChild.style.cssText='width:1280px;height:720px;transform:none;position:relative';document.querySelectorAll('article')[i].querySelector('h2').style.display='none'}""",i)
   data=page.screenshot();import io
   im=Image.open(io.BytesIO(data)).convert('RGB');pdf.append(im)
   sheets.setdefault(element,[]).append((fixture,im.copy()))
   # All descendant text and member bounds are checked geometrically.
   result=page.evaluate("""i=>{let s=document.querySelectorAll('article')[i].querySelector('.slide'),b=s.getBoundingClientRect(),out=[];s.querySelectorAll('[data-el]').forEach(e=>{let r=e.getBoundingClientRect();if(r.width&&r.height&&(r.left<b.left-1||r.top<b.top-1||r.right>b.right+1||r.bottom>b.bottom+1))out.push({el:e.dataset.el,w:r.width,h:r.height});});return {font:document.fonts.check('16px "Pretendard Variable"'),outside:out}}""",i)
   issues.append(dict(mode=mode,element=element,fixture=fixture,**result))
  for el,ims in sheets.items():
   out=R/'library'/el;out.mkdir(exist_ok=True);canvas=Image.new('RGB',(1280,720),'#e8e8ec');d=ImageDraw.Draw(canvas)
   cols=3 if len(ims)>4 else 2;rows=(len(ims)+cols-1)//cols;w=1280//cols;h=720//rows
   for j,(name,im) in enumerate(ims):
    im.thumbnail((w,h-18));x=(j%cols)*w;y=(j//cols)*h;canvas.paste(im,(x,y+18));d.text((x+5,y+2),name,fill='black')
   canvas.save(out/(mode+'.png'))
  pdf[0].save(R/'library'/('library-'+mode+'.pdf'),save_all=True,append_images=pdf[1:],resolution=96)
  print(mode,length,'fixtures',len(sheets),'sheets')
 b.close()
(R/'library-checks.json').write_text(json.dumps(issues,ensure_ascii=False,indent=2));print('outside',sum(bool(x['outside']) for x in issues))
