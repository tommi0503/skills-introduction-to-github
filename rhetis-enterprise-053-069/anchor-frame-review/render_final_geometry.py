from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import fitz,json,io,re
B=Path(__file__).parent;AUDIT=(B/'render.py').read_text().split("AUDIT=r'''",1)[1].split("'''",1)[0];base='http://127.0.0.1:8765/anchor-frame-review/'
audit=json.loads((B/'browser-audit.json').read_text());changed={'cycle','hub','network','headline','tag','card'}
with sync_playwright() as w:
 b=w.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);p=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for mode in ['light','dark']:
  p.goto(base+'library/'+mode+'.html');p.evaluate('document.fonts.ready');p.add_style_tag(content='body{display:block;padding:0;margin:0}article{display:none}article.review-active{display:block}article.review-active>h2{display:none}.frame{width:1280px;height:720px;border-radius:0}.frame>.slide{transform:none}')
  groups={};pdf=fitz.open(B/f'library/library-{mode}.pdf')
  for idx in range(p.locator('article').count()):
   title=p.locator('article').nth(idx).locator(':scope > h2').inner_text();folder=title.split('/')[0].strip()
   if folder in changed:groups.setdefault(folder,[]).append((idx,title))
  for folder,items in groups.items():
   sheet=Image.new('RGB',(1280,len(items)*390),'#e5e8ec');draw=ImageDraw.Draw(sheet)
   for j,(idx,title) in enumerate(items):
    p.evaluate('(i)=>document.querySelectorAll("article").forEach((a,k)=>a.classList.toggle("review-active",i===k))',idx);label=title.split(' min ')[0];draw.text((10,j*390+4),label+' | full 12x6 (left) / minimum (right)',fill='black')
    shot=p.locator('article').nth(idx).locator('.slide').screenshot();im=Image.open(io.BytesIO(shot)).convert('RGB');im.thumbnail((630,354));sheet.paste(im,(4,j*390+30));audit['library'][mode+'/'+label+'/full']=p.evaluate(AUDIT)
    pdf.delete_page(idx);page=pdf.new_page(pno=idx,width=1280,height=720);page.insert_image(page.rect,stream=shot)
    minimum=re.search(r'min\s+(\d+)x(\d+)',title);c,r=map(int,minimum.groups()) if minimum else (12,6)
    p.evaluate('([i,c,r])=>{for(const n of document.querySelectorAll("article")[i].querySelectorAll(".body > *")){n.style.gridColumn="1 / span "+c;n.style.gridRow="1 / span "+r}}',[idx,c,r]);shot=p.locator('article').nth(idx).locator('.slide').screenshot();im=Image.open(io.BytesIO(shot)).convert('RGB');im.thumbnail((630,354));sheet.paste(im,(644,j*390+30));audit['library'][mode+'/'+label+'/min']=p.evaluate(AUDIT)
   sheet.save(B/f'library/{folder}/{mode}.png')
  pdf.save(B/f'library/library-{mode}-final.pdf',garbage=4,deflate=True);pdf.close();(B/f'library/library-{mode}-final.pdf').replace(B/f'library/library-{mode}.pdf')
 for kind in ['replica','reassembled']:
  f=B/kind/'slide_01.html';p.goto(base+kind+'/slide_01.html');p.evaluate('document.fonts.ready');p.screenshot(path=str(f.with_suffix('.png')));im=Image.open(f.with_suffix('.png')).convert('RGB');c=canvas.Canvas(str(B/kind/(kind+'.pdf')),pagesize=(1280,720));c.drawImage(ImageReader(im),0,0,width=1280,height=720);c.showPage();c.save();orig=Image.open('/workspace/work/deck/miricanvas_기업_selected/069_1l1vx_파란색_깔끔_비즈니스_프로젝트_제안_기획서/slide_01.png').convert('RGB');cmp=Image.new('RGB',(2560,720));cmp.paste(orig,(0,0));cmp.paste(im,(1280,0));cmp.save(B/('compare-'+kind)/'slide_01.png');audit['pages'][kind+'/slide_01']={'font':p.evaluate("document.fonts.check('800 76px \"Noto Sans KR\"')"),'overflow':p.evaluate(AUDIT),'size':[1280,720]}
 b.close()
(B/'browser-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2));print('final geometry / page rerenders complete; library fail cases',sum(bool(v) for v in audit['library'].values()))
