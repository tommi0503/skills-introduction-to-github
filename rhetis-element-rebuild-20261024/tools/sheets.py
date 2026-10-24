"""Per-element native-resolution size matrix, source comparison and browser QA.
Usage: python sheets.py COLLECTION LEAF [--fixture STEM] [--no-compare]
Each fixture is rendered in an actual1280x720 foundation; only its slot +12px bleed is cropped.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw,ImageFont
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from glyph_qa import JS as GLYPH_JS
from shape_qa import JS as SHAPE_JS
from paint_qa import JS as PAINT_JS
import argparse,threading,json,re,io,hashlib,math,collections,time
ROOT=Path('/workspace/work/rebuild');REF=Path('/workspace/work/reference');OLD=Path('/workspace/work/delivery')
SIZES=[(12,6),(12,3),(9,4),(8,6),(6,6),(6,3),(4,4),(4,3),(3,3)]
FONT=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
JS='''() => {let root=document.querySelector('.body').firstElementChild;let frame=root.getBoundingClientRect();let rect=r=>[r.x,r.y,r.width,r.height];let rgba=c=>{let q=document.createElement('canvas');q.width=q.height=1;let z=q.getContext('2d');z.fillStyle=c;z.fillRect(0,0,1,1);return [...z.getImageData(0,0,1,1).data]};let texts=[],outside=[],clipped=[],hidden=[],member_outside=[];for(let e of root.querySelectorAll('.name,.fig')){if(e.textContent.trim()&&(getComputedStyle(e).display==='none'||!e.getClientRects().length))hidden.push(e.className+':'+e.textContent)}let tw=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);while(tw.nextNode()){let n=tw.currentNode,e=n.parentElement,t=n.textContent.trim();if(!t||['STYLE','SCRIPT'].includes(e.tagName))continue;let s=getComputedStyle(e);if(s.display==='none'||s.visibility==='hidden'||!e.getClientRects().length)continue;let owner=e.closest('[data-el]')||root,ob=owner.getBoundingClientRect();let block=e.closest('p,h1,h2,h3,h4,blockquote,li,td,th,.name,.fig,.note,.kick,.mark,.chip,.key,.bar,.pt,.step,.stop')||e;let rr=document.createRange();rr.selectNodeContents(n);let opacity=1;for(let a=e;a;a=a.parentElement)opacity*=parseFloat(getComputedStyle(a).opacity);for(let r of rr.getClientRects()){if(r.width<.2||r.height<.2)continue;let member=e.closest('.spoke,.core,.step,.stop,.side,.plan,.person,.layer,.item,.opt,.end,.level,.stage,.from,.to');if(member&&member!==root&&e.closest('.name,.note,.fig,.kick,.from,.to')){let mb=member.getBoundingClientRect();if(mb.width>1&&mb.height>1&&(r.left<mb.left-1||r.right>mb.right+1||r.top<mb.top-1||r.bottom>mb.bottom+1))member_outside.push({member:member.className,text:t.slice(0,150),rect:rect(r),memberRect:rect(mb)})}let text={text:t.slice(0,150),rect:rect(r),font:parseFloat(s.fontSize),weight:parseFloat(s.fontWeight),fg:rgba(s.color),opacity,block:[...root.querySelectorAll('*')].indexOf(block)};texts.push(text);if(r.left<ob.left-1||r.right>ob.right+1||r.top<ob.top-1||r.bottom>ob.bottom+1||r.left<frame.left-1||r.right>frame.right+1||r.top<frame.top-1||r.bottom>frame.bottom+1)outside.push(text);for(let a=e;a&&a!==root.parentElement;a=a.parentElement){let c=getComputedStyle(a);if(c.overflowX==='hidden'||c.overflowX==='clip'||c.overflowY==='hidden'||c.overflowY==='clip'){let b=a.getBoundingClientRect();if(r.left<b.left-1||r.right>b.right+1||r.top<b.top-1||r.bottom>b.bottom+1){clipped.push(text);break}}}}}let overlaps=[];for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){let a=texts[i],b=texts[j];if(a.block===b.block)continue;let ar=a.rect,br=b.rect;let w=Math.min(ar[0]+ar[2],br[0]+br[2])-Math.max(ar[0],br[0]),h=Math.min(ar[1]+ar[3],br[1]+br[3])-Math.max(ar[1],br[1]);if(w>2&&h>2&&w*h>Math.min(ar[2]*ar[3],br[2]*br[3])*.08)overlaps.push([a.text,b.text,[w,h]])}return {bbox:rect(frame),texts,outside,clipped,hidden,member_outside,overlaps,fonts:[...document.fonts].map(f=>({family:f.family,status:f.status})),page:[document.documentElement.scrollWidth,document.documentElement.scrollHeight]}}'''
JS=JS.replace('return {bbox:rect(frame)',GLYPH_JS+SHAPE_JS+PAINT_JS+'return {painted_outside,shape_clipped,chip_alignment,bbox:rect(frame)')

def lum(rgb):
 a=[v/255 for v in rgb];a=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in a];return .2126*a[0]+.7152*a[1]+.0722*a[2]
def contrast(f,b):
 x,y=sorted([lum(f),lum(b)]);return (y+.05)/(x+.05)
def check_contrast(im,texts):
 failures=[]
 for t in texts:
  x,y,w,h=t['rect'];box=(max(0,math.floor(x)),max(0,math.floor(y)),min(1280,math.ceil(x+w)),min(720,math.ceil(y+h)))
  if box[0]>=box[2] or box[1]>=box[3]:continue
  colors=collections.Counter((r//8*8+4,g//8*8+4,b//8*8+4) for r,g,b in im.crop(box).getdata());fg=t['fg'][:3]
  candidates=[(count,c) for c,count in colors.items() if sum((c[k]-fg[k])**2 for k in range(3))>35**2]
  bg=max(candidates)[1] if candidates else colors.most_common(1)[0][0];opacity=t['opacity']*t['fg'][3]/255;actual=[fg[k]*opacity+bg[k]*(1-opacity) for k in range(3)];ratio=contrast(actual,bg);threshold=3 if t['font']>=28 else 4.5
  if ratio<threshold-.06:failures.append({'text':t['text'],'ratio':round(ratio,2),'required':threshold,'foreground':fg,'background':bg,'rect':t['rect']})
 return failures

def context(name,leaves=None):
 C=ROOT/name/name;R=ROOT/name/'review';defaults={};regs={};css=[]
 for path,kind in [(C/'foundation','foundation')]+[(p,'element') for p in sorted((C/'elements').iterdir()) if p.is_dir()and(leaves is None or p.name in leaves)]:
  meta=path/(kind+'.json');style=path/(kind+'.css')
  if meta.exists():d=json.loads(meta.read_text());defaults.update(d.get('tokenDefaults',{}));regs.update(d.get('registrations',{}))
  if style.exists():css.append(style.read_text())
 kit=json.loads((C/'kit/kit.json').read_text());tokens=(C/'kit'/kit['tokens']).read_text();palette=json.loads((R/'assets/palette.json').read_text());steps=json.loads((REF/'contract/type-steps.json').read_text());preview='.slide{'+''.join(f'--type-{s}:{s}px;' for s in steps)+'--radius-lg:var(--radius);}'
 for k,v in kit.get('extensions',{}).items():
  if isinstance(v,dict) and 'default'in v:defaults.setdefault(k,v['default'])
 defaultsCss='.slide{'+''.join(k+':'+str(v)+';' for k,v in defaults.items())+'}'
 pc=''.join(('.slide.dark' if mode=='dark' else '.slide')+'{'+''.join(k+':'+str(v)+';' for k,v in entries.items())+'}' for mode,entries in palette.items())
 shell='html,body{margin:0;padding:0;width:1280px;height:720px;overflow:hidden} [data-icon]:empty::after{content:"";display:block;width:100%;height:100%;box-sizing:border-box;border:1.5px dashed currentColor;border-radius:50%;opacity:.7}'
 return ''.join(regs.values())+tokens+''.join(css)+pc+preview+defaultsCss+shell

def minparse(text):
 m=re.match(r'\s*<!--\s*min:\s*(.*?)\s*-->',text)
 if not m:raise ValueError('Fixture has no honest min')
 sizes=[tuple(map(int,a)) for a in re.findall(r'(\d+)x(\d+)',m[1])]
 if not sizes or any(not(1<=a<=12 and 1<=b<=6) for a,b in sizes):raise ValueError('Bad minimum')
 return sizes,text[m.end():].strip()

def render(name,leaf,fixture=None,no_compare=False):
 C=ROOT/name/name;R=ROOT/name/'review';D=ROOT/name/'build';styles=context(name);F=C/'elements'/leaf/'fixtures';fs=sorted(F.glob('*.html'))
 if fixture:fs=[f for f in fs if f.stem==fixture]
 if not fs:raise RuntimeError('No fixtures for '+leaf)
 htmlDir=R/'html'/leaf;htmlDir.mkdir(parents=True,exist_ok=True);cellDir=D/'cells'/leaf;cellDir.mkdir(parents=True,exist_ok=True);(R/'validation').mkdir(exist_ok=True);(R/'sheets').mkdir(exist_ok=True)
 if not fixture:
  for stale in cellDir.glob('*.png'):stale.unlink()
 dependencies={leaf}
 for f in fs:
  dependencies.update(re.findall(r'data-el=[\'"]'+re.escape(name)+r'-([\w-]+)[\'"]',f.read_text()))
 sourceFiles=[C/'kit/kit.json',C/'kit/css/tokens.css',C/'foundation/foundation.json',C/'foundation/foundation.css']+fs
 for dependency in sorted(dependencies):
  sourceFiles.extend([C/'elements'/dependency/'element.css',C/'elements'/dependency/'element.json'])
 proof={'collection':name,'leaf':leaf,'paint_members_revision':2,'source_hashes':{str(f.relative_to(C)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sourceFiles},'cases':[],'sheet_rows':{},'font_checks':[]}
 proof['shared_render_hashes']={str(f):hashlib.sha256(f.read_bytes()).hexdigest()for f in [R/'assets/palette.json',REF/'contract/type-steps.json',R/'assets/fonts/fonts.css']}
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)));threading.Thread(target=server.serve_forever,daemon=True).start();cached={}
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-crash-reporter','--disable-breakpad']);pg=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1);pg.route('**/*',lambda route:route.continue_())
  cdp=pg.context.new_cdp_session(pg);cdp.send('DOM.enable');cdp.send('CSS.enable')
  for mode in ['light','dark']:
   rows=[]
   for f in fs:
    mins,markup=minparse(f.read_text());sizes=[s for s in SIZES if any(s[0]>=m[0] and s[1]>=m[1] for m in mins)];sizes+= [m for m in mins if m not in sizes];shots=[]
    doc='<!doctype html><html lang="ko"><head><meta charset="utf-8"><link rel="stylesheet" href="../../assets/fonts/fonts.css"><style>'+styles+'</style></head><body><section class="slide'+(' dark' if mode=='dark' else '')+'"><div class="page"><div class="body">'+markup+'</div></div></section></body></html>'
    hf=htmlDir/(f.stem+'-'+mode+'.html');hf.write_text(doc);pg.goto(f'http://127.0.0.1:{server.server_port}/{name}/review/html/{leaf}/{hf.name}?v={time.time_ns()}');pg.evaluate('document.fonts.ready')
    from font_qa import actual_fonts
    font_proof=actual_fonts(pg,cdp);font_proof.update(fixture=f.stem,mode=mode,html_sha256=hashlib.sha256(hf.read_bytes()).hexdigest());proof['font_checks'].append(font_proof)
    for a,bb in sizes:
     pg.locator('.body > :first-child').evaluate('(e,v)=>{e.style.gridColumn="1 / span "+v[0];e.style.gridRow="1 / span "+v[1]}',[a,bb]);pg.evaluate('document.fonts.ready');qa=pg.evaluate(JS);im=Image.open(io.BytesIO(pg.screenshot())).convert('RGB');qa['contrast']=check_contrast(im,qa['texts']);qa.update({'fixture':f.stem,'mode':mode,'grid':[a,bb],'minimum':(a,bb) in mins});qa.pop('texts');proof['cases'].append(qa)
     x,y,w,h=qa['bbox'];clip=(max(0,math.floor(x)-12),max(0,math.floor(y)-12),min(1280,math.ceil(x+w)+12),min(720,math.ceil(y+h)+12));crop=im.crop(clip);cp=cellDir/f'{f.stem}-{mode}-{a}x{bb}.png';crop.save(cp,optimize=True);shots.append((f'{a}x{bb}'+(' MIN' if(a,bb)in mins else ''),crop,qa));cached[(f.stem,mode,(a,bb))]=crop
    rows.append((f.stem,shots))
   labelWidth=240;maxWidth=max(sum(i.width+16 for _,i,_ in shots) for _,shots in rows)+labelWidth+16;maxHeight=sum(max(i.height for _,i,_ in shots)+64 for _,shots in rows)+16;sheet=Image.new('RGB',(maxWidth,maxHeight),'#e6e8ec');draw=ImageDraw.Draw(sheet);y=16;rowBounds=[]
   for fn,shots in rows:
    draw.text((12,y+25),fn,fill='#111111',font=FONT);x=labelWidth;rh=max(i.height for _,i,_ in shots)+64
    for lab,im,qa in shots:
     draw.text((x+4,y+3),lab,fill='#155b29' if qa['minimum'] else '#333333',font=FONT);sheet.paste(im,(x,y+30));draw.rectangle((x,y+30,x+im.width-1,y+30+im.height-1),outline='#8b919c');x+=im.width+16
    rowBounds.append({'fixture':fn,'y':y,'height':rh,'cells':len(shots)});y+=rh
   out=R/'sheets'/f'{leaf}-{mode}.png';sheet.save(out,optimize=True);proof['sheet_rows'][mode]=rowBounds
  b.close()
 server.shutdown()
 if not no_compare:
  mp=R/'map.json';parts=list(D.glob('map-*.json'));maps=[i for m in parts for i in json.loads(m.read_text()).get('instances',[])] if parts else json.loads(mp.read_text())['instances']
  selected=[i for i in maps if i.get('leaf')==leaf and (i.get('use')=='base' or str(i.get('use','')).startswith(('variant:','same-as:')))]
  comparisons=[]
  for inst in selected:
   page=str(inst['page']).zfill(2);stem=inst.get('fixture','replica-'+page).replace('.html','');match=next((f for f in fs if f.stem==stem),None)
   if match is None:continue
   mins,_=minparse(match.read_text());full=cached.get((stem,'light',(12,6)));small=cached.get((stem,'light',mins[0]));src=Image.open(OLD/name/'review/replica'/f'slide_{page}.png').convert('RGB');x,y,w,h=inst['bbox'];source=src.crop((max(0,round(x)),max(0,round(y)),min(1280,round(x+w)),min(720,round(y+h))))
   if full is not None and small is not None:comparisons.append((page,source,full,small))
  if comparisons:
   width=max(sum(im.width+20 for im in [s,f,m])+20 for _,s,f,m in comparisons);height=sum(max(s.height,f.height,m.height)+52 for _,s,f,m in comparisons)+16;comp=Image.new('RGB',(width,height),'#e8e8ec');draw=ImageDraw.Draw(comp);yy=16
   for page,s,f,m in comparisons:
    xx=16
    for label,im in [('replica '+page,s),('12x6',f),('min',m)]:draw.text((xx,yy),label,fill='#222222',font=FONT);comp.paste(im,(xx,yy+28));xx+=im.width+20
    yy+=max(s.height,f.height,m.height)+52
   comp.save(R/'sheets'/f'{leaf}-replica.png',optimize=True)
 proof['counts']={k:sum(len(c[k]) for c in proof['cases']) for k in ['outside','clipped','hidden','member_outside','overlaps','contrast','chip_alignment','shape_clipped','painted_outside']};proof['pngs']={str(p.relative_to(R)):list(Image.open(p).size) for p in (R/'sheets').glob(leaf+'-*.png')};(R/'validation'/f'{leaf}.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2));print(name,leaf,len(proof['cases']),'cases',proof['counts'],flush=True)
 return proof
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('collection');a.add_argument('leaf');a.add_argument('--fixture');a.add_argument('--no-compare',action='store_true');v=a.parse_args();render(v.collection,v.leaf,v.fixture,v.no_compare)
