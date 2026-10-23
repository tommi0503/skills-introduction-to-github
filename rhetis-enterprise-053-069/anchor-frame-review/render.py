from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import subprocess,json,re,io,html
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
BASE=Path(__file__).resolve().parent.parent;C=BASE/'anchor-frame';R=BASE/'anchor-frame-review';REF=Path('/workspace/work/ref'); URL='http://127.0.0.1:8765/'; prefix='anchor-frame-review/'
for d in ['library','reassembled','compare-reassembled','compare-replica']: (R/d).mkdir(exist_ok=True)
for mode in ['light','dark']:
 args=['python',str(REF/'tools/preview.py'),str(C),str(REF/'contract/type-steps.json'),'--out',str(R/f'library/{mode}.html')]
 if mode=='dark':args+=['--dark']
 subprocess.run(args,check=True,capture_output=True)
 p=R/f'library/{mode}.html';p.write_text(p.read_text().replace((REF/'fonts/fonts.css').as_uri(),'../../fonts/fonts.css'))
AUDIT=r'''() => {
 const all=[]; for(const root of document.querySelectorAll('[data-el]')){
 const box=root.getBoundingClientRect();if(!box.width||!box.height)continue;
 for(const n of root.querySelectorAll('*')){const st=getComputedStyle(n);if(st.visibility==='hidden'||st.display==='none'||n.querySelector('[data-el]'))continue;
 if(n.childNodes.length&&[...n.childNodes].some(x=>x.nodeType===3&&x.textContent.trim())){const range=document.createRange();range.selectNodeContents(n);const r=range.getBoundingClientRect();if(r.width&&r.height&&(r.left<box.left-2||r.right>box.right+2||r.top<box.top-2||r.bottom>box.bottom+2))all.push({root:root.dataset.el,part:n.className,text:n.textContent.slice(0,50),rootBox:[box.x,box.y,box.width,box.height],box:[r.x,r.y,r.width,r.height]})}
 }
 } return all;
}'''
audit={'pages':{},'library':{},'browser':'Chromium /usr/bin/chromium','viewport':[1280,720]}
with sync_playwright() as w:
 b=w.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);p=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 for kind in ['replica','reassembled']:
  pdf=canvas.Canvas(str(R/kind/(kind+'.pdf')),pagesize=(1280,720))
  for f in sorted((R/kind).glob('slide_*.html')):
   p.goto(URL+prefix+kind+'/'+f.name);p.evaluate('document.fonts.ready');p.screenshot(path=str(f.with_suffix('.png')))
   audit['pages'][kind+'/'+f.stem]={'font':p.evaluate("document.fonts.check('800 76px \"Noto Sans KR\"')"),'overflow':p.evaluate(AUDIT),'size':[1280,720]}
   im=Image.open(f.with_suffix('.png')).convert('RGB');pdf.drawImage(ImageReader(im),0,0,width=1280,height=720);pdf.showPage()
   orig=Image.open('/workspace/work/deck/miricanvas_기업_selected/069_1l1vx_파란색_깔끔_비즈니스_프로젝트_제안_기획서/'+f.with_suffix('.png').name).convert('RGB');cmp=Image.new('RGB',(2560,720));cmp.paste(orig,(0,0));cmp.paste(im,(1280,0));cmp.save(R/('compare-'+kind)/(f.stem+'.png'))
  pdf.save()
 for mode in ['light','dark']:
  p.goto(URL+prefix+'library/'+mode+'.html');p.evaluate('document.fonts.ready')
  # Full sheet HTML remains exactly preview.py output; review images add minimum-size observations.
  p.add_style_tag(content='body{display:block;padding:0;margin:0}article{display:none}article.review-active{display:block}article.review-active>h2{display:none}.frame{width:1280px;height:720px;border-radius:0}.frame>.slide{transform:none}')
  count=p.locator('article').count();groups={}
  for idx in range(count):
   title=p.locator('article').nth(idx).locator(':scope > h2').inner_text();folder=title.split('/')[0].strip();groups.setdefault(folder,[]).append((idx,title))
  pdf=canvas.Canvas(str(R/f'library/library-{mode}.pdf'),pagesize=(1280,720))
  for folder,items in groups.items():
   sheet=Image.new('RGB',(1280,len(items)*390),'#e5e8ec');draw=ImageDraw.Draw(sheet)
   for j,(idx,title) in enumerate(items):
    p.evaluate('''(i)=>{document.querySelectorAll('article').forEach((a,k)=>a.classList.toggle('review-active',i===k))}''',idx)
    label=title.split(' min ')[0];draw.text((10,j*390+4),label+' | full 12x6 (left) / minimum (right)',fill='black')
    shot=p.locator('article').nth(idx).locator('.slide').screenshot();im=Image.open(io.BytesIO(shot)).convert('RGB');im.thumbnail((630,354));sheet.paste(im,(4,j*390+30))
    pdf.drawImage(ImageReader(Image.open(io.BytesIO(shot))),0,0,width=1280,height=720);pdf.showPage()
    errs=p.evaluate(AUDIT);audit['library'][mode+'/'+label+'/full']=errs
    minimum=re.search(r'min\s+(\d+)x(\d+)',title)
    c,r=map(int,minimum.groups()) if minimum else (12,6)
    p.evaluate('''([i,c,r])=>{for(const n of document.querySelectorAll('article')[i].querySelectorAll('.body > *')){n.style.gridColumn='1 / span '+c;n.style.gridRow='1 / span '+r}}''',[idx,c,r])
    shot=p.locator('article').nth(idx).locator('.slide').screenshot();im=Image.open(io.BytesIO(shot)).convert('RGB');im.thumbnail((630,354));sheet.paste(im,(644,j*390+30));audit['library'][mode+'/'+label+'/min']=p.evaluate(AUDIT)
   (R/f'library/{folder}').mkdir(exist_ok=True);sheet.save(R/f'library/{folder}/{mode}.png')
  pdf.save()
 b.close()
(R/'browser-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2));print('audited',len(audit['library']),'library cases; text boundary failures',sum(bool(v) for v in audit['library'].values()))
