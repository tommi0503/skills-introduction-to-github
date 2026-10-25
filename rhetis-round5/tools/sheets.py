"""Actual 1280x720 grid renders, native cropped cells, size matrices and replica comparisons."""
from pathlib import Path
import argparse, json, re, hashlib, time, io, html, sys, importlib.util
from collections import Counter
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
REF=ROOT/'reference'
SIZES=[(12,6),(12,3),(9,4),(8,6),(6,6),(6,3),(4,4),(4,3),(3,3)]
HTTP='http://127.0.0.1:8876/'
RENDERER_VERSION='round5-design-folders-1'
RENDERER_HASH=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

def fingerprint(P,k,leaf=None):
 folders=[P/k,P/'assets']
 if leaf:
  dependencies={leaf};todo=[leaf]
  while todo:
   current=todo.pop()
   for fixture in (P/k/'elements'/current/'fixtures').glob('*.html'):
    for dep in re.findall(r'data-el=["\']'+re.escape(k)+r'-([^"\']+)',fixture.read_text()):
     if dep not in dependencies:dependencies.add(dep);todo.append(dep)
  folders=[P/k/'kit',P/k/'foundation',P/'assets/fonts']+[P/k/'elements'/d for d in sorted(dependencies)]
 files={str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for folder in folders for f in sorted(folder.rglob('*')) if f.is_file() and f.suffix in ['.css','.html','.json','.js','.woff','.woff2']}
 return hashlib.sha256(json.dumps(files,sort_keys=True).encode()).hexdigest()

def style(P,k):
 K=P/k; kit=json.loads((K/'kit/kit.json').read_text());out=(K/'kit'/kit['tokens']).read_text()
 for folder,kind in [(K/'foundation','foundation')]+[(f,'element') for f in sorted((K/'elements').glob('*')) if f.is_dir()]:
  if not (folder/(kind+'.css')).exists():continue
  meta=json.loads((folder/(kind+'.json')).read_text());out+='\n'+''.join(meta.get('registrations',{}).values())+'\n'+(folder/(kind+'.css')).read_text()
  out+='\n.slide{'+''.join(f'{a}:{b};' for a,b in meta.get('tokenDefaults',{}).items())+'}'
 pal=json.loads((REF/'contract/palette.json').read_text())
 for mode,d in pal.items():out+='\n.slide'+('.dark' if mode=='dark' else '')+'{'+''.join(f'{a}:{b};' for a,b in d.items())+'}'
 out+='\n.slide{'+''.join(f'--type-{n}:{n}px;' for n in json.loads((REF/'contract/type-steps.json').read_text()))+'--radius-lg:var(--radius);}'
 return out

def minimum(f):
 m=re.match(r'<!--\s*min:\s*(\d+)x(\d+)',f.read_text());assert m,('missing honest minimum',f)
 return tuple(map(int,m.groups()))

def sizing(mini):return [s for s in SIZES if s[0]>=mini[0] and s[1]>=mini[1]]+([] if mini in SIZES else [mini])

AUDIT=r'''root=>{
 const rr=root.getBoundingClientRect(),B=r=>[r.x,r.y,r.width,r.height].map(x=>+x.toFixed(2));
 const out={root:B(rr),outside:[],clipped:[],overlaps:[],fonts:[],chips:[],contrast:[],outsideComponent:[],outsideParts:[]};let texts=[];
 const ctx=document.createElement('canvas').getContext('2d',{willReadFrequently:true}),colorCache=new Map();
 const rgb=c=>{if(colorCache.has(c))return colorCache.get(c);ctx.clearRect(0,0,1,1);ctx.fillStyle=c;ctx.fillRect(0,0,1,1);const p=[...ctx.getImageData(0,0,1,1).data];p[3]/=255;colorCache.set(c,p);return p;};
 const over=(a,b)=>{const alpha=a.length>3?a[3]:1;return a.slice(0,3).map((x,i)=>x*alpha+b[i]*(1-alpha))};
 const lum=c=>c.map(x=>x/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4).reduce((v,x,i)=>v+x*[.2126,.7152,.0722][i],0);
 const back=e=>{let chain=[];for(let a=e;a;a=a.parentElement)chain.push(a);let bg=[255,255,255],gradient=false;for(const a of chain.reverse()){const st=getComputedStyle(a);bg=over(rgb(st.backgroundColor),bg);if(st.backgroundImage!=='none')gradient=true;}return {bg,gradient}};

 for(const e of [root,...root.querySelectorAll('*')]){
  const s=getComputedStyle(e),r=e.getBoundingClientRect();if(!r.width||!r.height||s.display==='none'||s.visibility==='hidden'||+s.opacity===0)continue;
  if(e.matches('[data-icon],.seat,.mark')&&(r.left<rr.left-2||r.right>rr.right+2||r.top<rr.top-2||r.bottom>rr.bottom+2))out.outsideParts.push({tag:e.tagName,class:e.className,box:B(r)});
  const direct=[...e.childNodes].filter(n=>n.nodeType===3&&n.textContent.trim());if(!direct.length)continue;
  const rng=document.createRange();rng.selectNodeContents(e);const tr=rng.getBoundingClientRect();
  if(s.clipPath!=='none'&&r.width<=2&&r.height<=2)continue;
  const info={tag:e.tagName,class:e.className,text:e.textContent.trim().slice(0,100),box:B(r),ink:B(tr)};
  if(tr.left<rr.left-2||tr.right>rr.right+2||tr.top<rr.top-2||tr.bottom>rr.bottom+2)out.outside.push(info);
  let a=e;while(a&&a!==root.parentElement){const as=getComputedStyle(a),ar=a.getBoundingClientRect();if(['hidden','clip','scroll','auto'].includes(as.overflowX)||['hidden','clip','scroll','auto'].includes(as.overflowY)){
   if(tr.left<ar.left-2||tr.right>ar.right+2||tr.top<ar.top-2||tr.bottom>ar.bottom+2){out.clipped.push({...info,ancestor:a.className});break}}
   a=a.parentElement;}
  const component=e.closest('[data-el]');if(component&&component!==root){const cr=component.getBoundingClientRect();if(tr.left<cr.left-2||tr.right>cr.right+2||tr.top<cr.top-2||tr.bottom>cr.bottom+2)out.outsideComponent.push({...info,component:component.getAttribute('data-el'),componentBox:B(cr)})}
  const bg=back(e),fg=over(rgb(s.color),bg.bg),l1=lum(fg),l2=lum(bg.bg),ratio=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05),threshold=parseFloat(s.fontSize)>=28?3:4.5;
  if(ratio<threshold-.01)out.contrast.push({...info,color:s.color,background:bg.bg,ratio:+ratio.toFixed(2),threshold,gradient:bg.gradient,foregroundRGB:fg});
  const first=s.fontFamily.split(',')[0],plain=first.replace(/[\"']/g,'').trim(),faces=[...document.fonts].filter(f=>f.family.replace(/[\"']/g,'').trim()===plain);
  out.fonts.push({family:s.fontFamily,declared:faces.length>0,loaded:faces.some(f=>f.status==='loaded')&&document.fonts.check(s.fontSize+' '+first)});texts.push({e,r:tr,info});
  if(e.matches('.tag,.mark,.chip')||e.matches('.name')&&e.closest('.pill'))out.chips.push({...info,dx:+(tr.x+tr.width/2-r.x-r.width/2).toFixed(2),dy:+(tr.y+tr.height/2-r.y-r.height/2).toFixed(2)});
 }
 for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){const a=texts[i],b=texts[j];if(a.e.contains(b.e)||b.e.contains(a.e))continue;const w=Math.min(a.r.right,b.r.right)-Math.max(a.r.left,b.r.left),h=Math.min(a.r.bottom,b.r.bottom)-Math.max(a.r.top,b.r.top);if(w>3&&h>3&&w*h>Math.min(a.r.width*a.r.height,b.r.width*b.r.height)*.2)out.overlaps.push([a.info,b.info]);}
 return out;
}'''

def raster_contrast(diag,im,clip):
 # The dominant painted colour inside a text ink box also sees ancestor pseudo-surfaces.
 # DOM contrast remains preserved; near-foreground antialias pixels are excluded.
 diag['contrastDOM']=diag['contrast'];diag['contrast']=[];diag['contrastPaintResolved']=[]
 def luminance(c):
  q=[v/255 for v in c];q=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in q]
  return sum(a*b for a,b in zip(q,[.2126,.7152,.0722]))
 for candidate in diag['contrastDOM']:
  x,y,w,h=candidate['ink'];rect=(max(0,int(x-clip['x'])),max(0,int(y-clip['y'])),min(im.width,int(x+w-clip['x']+.5)),min(im.height,int(y+h-clip['y']+.5)))
  fg=candidate['foregroundRGB'];pixels=Counter(im.crop(rect).convert('RGB').getdata()) if rect[2]>rect[0] and rect[3]>rect[1] else Counter()
  backgrounds=[(c,n) for c,n in pixels.most_common(12) if sum((a-b)**2 for a,b in zip(c,fg))>1200]
  if not backgrounds:diag['contrast'].append(candidate);continue
  bg,n=backgrounds[0];a,b=luminance(fg),luminance(bg);ratio=(max(a,b)+.05)/(min(a,b)+.05)
  q={**candidate,'paintedBackgroundRGB':bg,'paintedRatio':round(ratio,2),'paintMethod':'dominant non-foreground pixel inside text ink box'}
  (diag['contrastPaintResolved'] if ratio>=candidate['threshold']-.01 else diag['contrast']).append(q)

def label(draw,xy,text,fill='#202732'):draw.text(xy,text,fill=fill)

def run(k,leaves=None,modes=('light','dark')):
 P=ROOT/(k+'-project');K=P/k;D=P/'sheets';D.mkdir(exist_ok=True);cache=P/'sheet-cells';cache.mkdir(exist_ok=True);tmp=P/'sheet-runtime';tmp.mkdir(exist_ok=True)
 css=style(P,k)
 skeleton='<!doctype html><html lang="ko"><meta charset="utf-8"><link rel="stylesheet" href="../assets/fonts/fonts.css"><style>html,body{margin:0;padding:0;width:1280px;height:720px;overflow:hidden}*{box-sizing:border-box}'+css+'\n[data-icon]:empty::after{content:"";display:block;width:100%;height:100%;border:1.5px dashed currentColor;border-radius:50%;box-sizing:border-box;opacity:.7}</style><body><section class="slide"><div class="page"><div class="body"></div></div></section></body></html>'
 fn=tmp/'stage.html';fn.write_text(skeleton)
 mapping=json.loads((P/'map.json').read_text()) if (P/'map.json').exists() else {'instances':[]}
 leaves=leaves or [p.name for p in sorted((K/'elements').iterdir()) if p.is_dir()]
 with sync_playwright() as pw:
  browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage']);page=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for leaf in leaves:
   fn=tmp/('stage-'+leaf+'.html')
   initial=fingerprint(P,k,leaf)
   fn.write_text(skeleton.replace(css,style(P,k),1))
   folder=K/'elements'/leaf;fixtures=sorted((folder/'fixtures').glob('*.html'));assert len(fixtures)>=2,(leaf,'at least 2 fixtures')
   report={'rendererVersion':RENDERER_VERSION,'rendererSHA256':RENDERER_HASH,'collection':k,'leaf':leaf,'sourceFingerprint':initial,'generatedAtUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'modes':{}}
   for mode in modes:
    page.goto(HTTP+str(fn.relative_to(ROOT)),wait_until='load');page.evaluate('document.fonts.ready');page.locator('.slide').evaluate('(e,m)=>e.classList.toggle("dark",m==="dark")',mode)
    rows=[];checks=[];cells={}
    for fixture in fixtures:
     mini=minimum(fixture);sizes=sizing(mini);pics=[]
     markup=re.sub(r'^<!--.*?-->\s*','',fixture.read_text(),count=1,flags=re.S)
     for c,r in sizes:
      page.locator('.body').evaluate('(e,s)=>{e.innerHTML=s}',markup)
      root=page.locator('.body > *');assert root.count()==1,(fixture,'fixture must have one body child')
      root.evaluate('(e,s)=>{e.style.gridColumn="1 / span "+s[0];e.style.gridRow="1 / span "+s[1]}',[c,r])
      page.evaluate('document.fonts.ready');page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
      diag=root.evaluate(AUDIT);diag.update({'fixture':fixture.name,'size':[c,r],'isMin':(c,r)==mini});checks.append(diag)
      diag['slot']=page.locator('.body').evaluate('(e,s)=>{const r=e.getBoundingClientRect(),st=getComputedStyle(e),gx=parseFloat(st.columnGap),gy=parseFloat(st.rowGap),w=(r.width-gx*11)/12,h=(r.height-gy*5)/6;return [r.x,r.y,w*s[0]+gx*(s[0]-1),h*s[1]+gy*(s[1]-1)]}',[c,r])
      x,y,w,h=diag['slot'];assert w>0 and h>0,(leaf,fixture.name,c,r,diag['root'])
      pad=6;clip={'x':max(0,x-pad),'y':max(0,y-pad),'width':min(1280,max(0,x-pad)+w+pad*2)-max(0,x-pad),'height':min(720,max(0,y-pad)+h+pad*2)-max(0,y-pad)}
      # Clip is in the actual 1280x720 page; retain native pixel scale.
      clip['width']=min(1280-clip['x'],w+pad*2);clip['height']=min(720-clip['y'],h+pad*2)
      raw=page.screenshot(clip=clip,animations='disabled');target=cache/(leaf+'--'+fixture.stem+'--'+mode+f'--{c}x{r}.png');target.write_bytes(raw)
      pic=Image.open(io.BytesIO(raw)).convert('RGB');raster_contrast(diag,pic,clip);pics.append(((c,r),pic));cells[(fixture.name,(c,r))]=pic
     rows.append((fixture.name,mini,pics))
    rowheights=[max(p.height for _,p in pics)+60 for _,_,pics in rows];width=max(sum(p.width+14 for _,p in pics)+220 for _,_,pics in rows)
    canvas=Image.new('RGB',(width,48+sum(rowheights)),('#151a22' if mode=='dark' else '#e9edf2'));draw=ImageDraw.Draw(canvas);fg='#f2f4f7' if mode=='dark' else '#202732';label(draw,(14,15),f'{k} / {leaf} / {mode} | actual 1280x720 grid crops; 6px gutter',fg)
    yy=48
    for (name,mini,pics),rh in zip(rows,rowheights):
     label(draw,(12,yy+30),name,fg);label(draw,(12,yy+48),f'min {mini[0]}x{mini[1]}',fg);xx=210
     for size,pic in pics:
      label(draw,(xx,yy+5),f'{size[0]}x{size[1]}'+(' [MIN]' if size==mini else ''),fg);canvas.paste(pic,(xx,yy+26));draw.rectangle((xx-1,yy+25,xx+pic.width,yy+26+pic.height),outline='#4b80ba' if size==mini else '#7e8996');xx+=pic.width+14
     yy+=rh
    canvas.save(D/(leaf+'-'+mode+'.png'));report['modes'][mode]=checks
    if mode=='light':
     sources=[i for i in mapping['instances'] if i.get('leaf')==leaf and i.get('use') in ['base'] or i.get('leaf')==leaf and str(i.get('use','')).startswith('variant:')]
     comparisons=[]
     for inst in sources:
      fixture_name=Path(inst.get('fixture','')).name
      if not fixture_name:fixture_name='replica-'+str(inst['page']).zfill(2)+'.html'
      f=folder/'fixtures'/fixture_name
      if not f.exists():continue
      mini=minimum(f);full=cells.get((fixture_name,(12,6)));small=cells.get((fixture_name,mini));assert full is not None and small is not None,(leaf,fixture_name,'comparison cells missing')
      source=P/'replica'/('slide_'+str(inst['page']).zfill(2)+'.png');assert source.exists(),source
      x,y,w,h=inst['bbox'];assert x>=0 and y>=0 and x+w<=1281 and y+h<=721,(leaf,inst['bbox'])
      crop=Image.open(source).convert('RGB').crop((int(x),int(y),int(x+w+.5),int(y+h+.5)));comparisons.append((inst,crop,full,small))
     if comparisons:
      widths=[sum(p.width for p in row[1:])+68 for row in comparisons];heights=[max(p.height for p in row[1:])+65 for row in comparisons];im=Image.new('RGB',(max(widths),sum(heights)),'#e9edf2');dr=ImageDraw.Draw(im);yy=0
      for (inst,*pics),rh in zip(comparisons,heights):
       xx=12;label(dr,(12,yy+4),f"page {inst['page']} / {inst['use']} / bbox {inst['bbox']}")
       for title,pic in zip(['replica','12x6','min'],pics):label(dr,(xx,yy+22),title);im.paste(pic,(xx,yy+42));xx+=pic.width+20
       yy+=rh
      im.save(D/(leaf+'-replica.png'))
   (D/(leaf+'-checks.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2));assert fingerprint(P,k,leaf)==initial,('source changed during sheet build',leaf)
   print(k,leaf,'fixtures',len(fixtures),'cells',sum(len(x) for x in report['modes'].values()),'sheet complete',flush=True)
  browser.close()

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('collection');ap.add_argument('--leaf',nargs='+');ap.add_argument('--mode',choices=['light','dark']);a=ap.parse_args();run(a.collection,a.leaf,(a.mode,) if a.mode else ('light','dark'))
