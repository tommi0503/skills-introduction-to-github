from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import json,re,io,math,sys
B=Path(__file__).parent;C=B.parent/'current-fold';L=B/'library';audit=[]
with sync_playwright() as p:
 br=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=br.new_page(viewport={'width':1400,'height':1000},device_scale_factor=1)
 for mode in ['light','dark']:
  page.goto('http://127.0.0.1:8765/current-fold-review/library/'+mode+'.html');page.evaluate('document.fonts.ready');page.add_style_tag(content='body{display:block;padding:0;margin:0}article{display:none}article.active{display:block}.frame{width:1280px;height:720px;overflow:hidden;border-radius:0}.frame>.slide{transform:none}h2{display:none}')
  arts=page.locator('article');groups={}
  for i in range(arts.count()):
   a=arts.nth(i);name=a.locator(':scope > h2').inner_text().split(' / ')[0];groups.setdefault(name,[]).append(i)
  for name,indexes in groups.items():
   if len(sys.argv)>1 and name!=sys.argv[1]:continue
   ims=[];labels=[]
   for i in indexes:
    page.evaluate('''i=>{document.querySelectorAll('article').forEach(e=>e.classList.remove('active'));document.querySelectorAll('article')[i].classList.add('active')}''',i)
    a=arts.nth(i);title=a.locator(':scope > h2').inner_text();sl=a.locator('.slide').first
    ims.append(Image.open(io.BytesIO(sl.screenshot())).convert('RGB'));labels.append(title.split(' / ')[-1].split(' min ')[0]+' · 12×6')
    entry={'mode':mode,'element':name,'fixture':title,'font':page.evaluate('document.fonts.check(\'16px "Pretendard Variable"\')'),'errors':[],'sizes':0}
    # inspect grid allocation at every supported size from declared minimum, with screenshots at minimum too
    froot=a.locator('.body > *').first
    if froot.count() and name!='foundation':
     mins=re.findall(r'(\d+)x(\d+)',title);mc,mr=map(int,mins[0]) if mins else (12,6)
     minshot=None
     check=froot.evaluate("""(e,mins)=>{let errors=[],count=0;for(let co=mins[0];co<=12;co++){for(let ro=mins[1];ro<=6;ro++){e.style.gridColumn='1 / span '+co;e.style.gridRow='1 / span '+ro;count++;let b=e.getBoundingClientRect();let err=[...e.querySelectorAll('.name,.fig,.note,.kick,h2,p,td,th')].filter(x=>{if(getComputedStyle(x).display==='none')return false;let r=x.getBoundingClientRect();return r.right>b.right+3||r.bottom>b.bottom+3||r.left<b.left-3||r.top<b.top-3||x.scrollHeight>x.clientHeight+3||x.scrollWidth>x.clientWidth+3}).map(x=>x.textContent.slice(0,45));if(err.length&&errors.length<4)errors.push({size:[co,ro],text:err.slice(0,4)})}}e.style.gridColumn='1 / span '+mins[0];e.style.gridRow='1 / span '+mins[1];return{errors:errors,sizes:count}}""",[mc,mr]);entry.update(check)
     minshot=Image.open(io.BytesIO(sl.screenshot())).convert('RGB')
     if minshot is not None and i==indexes[0]:ims.append(minshot);labels.append(f'최소 {mc}×{mr}')
     froot.evaluate('(e)=>{e.style.gridColumn="1 / span 12";e.style.gridRow="1 / span 6"}')
    audit.append(entry)
   # Each element owns one full-size 1280x720 review sheet, all fixtures plus the declared minimum view.
   n=len(ims);cols=2 if n<=4 else 3;rows=math.ceil(n/cols);cw=1280//cols;ch=720//rows
   sheet=Image.new('RGB',(1280,720),'#e6e8eb');draw=ImageDraw.Draw(sheet)
   for j,(im,label) in enumerate(zip(ims,labels)):
    im.thumbnail((cw-8,ch-25));x=(j%cols)*cw+(cw-im.width)//2;y=(j//cols)*ch+23;sheet.paste(im,(x,y));draw.text(((j%cols)*cw+6,(j//cols)*ch+5),label[:65],fill='black')
   (L/name).mkdir(exist_ok=True);sheet.save(L/name/(mode+'.png'))
  imgs=[Image.open(L/k/(mode+'.png')).convert('RGB') for k in groups]
  imgs[0].save(L/('library-'+mode+'.pdf'),save_all=True,append_images=imgs[1:],resolution=96)
 br.close()

if len(sys.argv)>1:
 old=json.load(open(B/'library-audit.json'));audit=[a for a in old if a['element']!=sys.argv[1]]+audit
(B/'library-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
print('audited',len(audit),'fixtures; with overflow',sum(bool(x['errors']) for x in audit))
