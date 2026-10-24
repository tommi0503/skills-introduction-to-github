"""Render fixture rows × grid-size columns, both modes, plus frozen-replica crops.
Each sample is a true 1280x720 slide, with only the fixture's grid spans changed.
Only the allocated slot (with a six-pixel safety margin) enters the element sheet.
Text-background contrast uses a second browser image with glyph fill transparent.
"""
from pathlib import Path
from lxml import html,etree
from PIL import Image,ImageDraw,ImageFont,ImageChops
from playwright.async_api import async_playwright
import argparse,asyncio,json,re,io,math,hashlib,time
ROOT=Path(__file__).resolve().parents[1]
ENGINE_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
SIZES=[(12,6),(12,3),(9,4),(8,6),(6,6),(6,3),(4,4),(4,3),(3,3)]
PALETTE=json.loads((ROOT/'contract/palette.json').read_text())
FONT=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16)
def load_css(c):
 css=[];defaults={}
 def read(f):
  value=f.read_text();css.append('/* source-sha256:'+str(f.relative_to(ROOT))+':'+hashlib.sha256(value.encode()).hexdigest()+' */');return value
 for f in [c/'foundation/foundation.json',*sorted((c/'elements').glob('*/element.json'))]:
  if f.exists():
   d=json.loads(read(f));defaults.update(d.get('tokenDefaults',{}));css.extend(d.get('registrations',{}).values())
 css.append(read(c/'kit/css/tokens.css'));css.append('.slide{'+''.join(f'--type-{n}:{n}px;'for n in json.loads((ROOT/'contract/type-steps.json').read_text()))+'--radius-lg:var(--radius)}');css.append('.slide{'+''.join(k+':'+str(v)+';'for k,v in defaults.items())+'}')
 css.append(read(c/'foundation/foundation.css'))
 for f in sorted((c/'elements').glob('*/element.css')):css.append(read(f))
 return '\n'.join(css)
def fixture(s,c,r):
 s=re.sub(r'<!--.*?-->','',s,flags=re.S).strip();e=html.fragment_fromstring(s)
 style=re.sub(r'grid-(column|row)\s*:[^;]+;?','',e.get('style',''))
 e.set('style',style+f';grid-column:1 / span {c};grid-row:1 / span {r}')
 return etree.tostring(e,encoding='unicode',method='html')
AUDIT=r'''() => {
 let result=[];const cc=document.createElement('canvas'),ctx=cc.getContext('2d');
 function rgba(v){ctx.clearRect(0,0,1,1);ctx.fillStyle=v;ctx.fillRect(0,0,1,1);return [...ctx.getImageData(0,0,1,1).data]}
 function foreground(e,s){let c=rgba(s.color),opacity=1;for(let p=e;p;p=p.parentElement)opacity*=parseFloat(getComputedStyle(p).opacity);c[3]*=opacity;return c}
 for(const article of document.querySelectorAll('article')){
  const slide=article.querySelector('.slide'),body=slide.querySelector('.body'),root=body.firstElementChild;
  let box=root.getBoundingClientRect(),sb=slide.getBoundingClientRect(),out=[],overlap=[],text=[],hidden=[],chips=[];
  const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let n;
  while(n=walker.nextNode()){
   let value=n.textContent.trim();if(!value)continue;let e=n.parentElement,s=getComputedStyle(e);if(['STYLE','SCRIPT'].includes(e.tagName)||s.visibility==='hidden')continue;
   let range=document.createRange();range.selectNodeContents(n);
   for(const b of range.getClientRects()){
    if(b.width<.5||b.height<.5)continue;
    let owner=e.closest('[data-el]')||root,ob=owner.getBoundingClientRect();
    const item={text:value.slice(0,120),x:b.x,y:b.y+window.scrollY,w:b.width,h:b.height,color:foreground(e,s),fontSize:parseFloat(s.fontSize),root:owner.dataset?.el||'group'};text.push(item);
    if(b.left<ob.left-1.5||b.right>ob.right+1.5||b.top<ob.top-1.5||b.bottom>ob.bottom+1.5)out.push(item);
    let p=e;
    while(p&&p!==root){let ps=getComputedStyle(p),pb=p.getBoundingClientRect();if(['hidden','clip'].includes(ps.overflowX)||['hidden','clip'].includes(ps.overflowY)){
     if(b.left<pb.left-2||b.right>pb.right+2||b.top<pb.top-2||b.bottom>pb.bottom+2)out.push({...item,clippedBy:p.className});break;}p=p.parentElement;}
   }
  }
  for(let i=0;i<text.length;i++)for(let j=i+1;j<text.length;j++){
   let a=text[i],b=text[j],w=Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x),h=Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y);
   if(w>3&&h>Math.min(a.h,b.h)*.42&&w*h>Math.min(a.w*a.h,b.w*b.h)*.25)overlap.push({a:a.text,b:b.text,w,h});
  }
  for(const e of root.querySelectorAll('.fig,.name'))if(e.textContent.trim()&&!e.getBoundingClientRect().width)hidden.push(e.textContent.trim().slice(0,80));
  for(const e of root.querySelectorAll('.pill,.tag,.chip')){
   let b=e.getBoundingClientRect();if(!b.width||b.height>100||!e.textContent.trim())continue;let range=document.createRange();range.selectNodeContents(e);let t=range.getBoundingClientRect();
   const cs=getComputedStyle(e),ownFace=rgba(cs.backgroundColor)[3]>0||cs.backgroundImage!=='none',ownBox=['Top','Right','Bottom','Left'].every(side=>parseFloat(cs['border'+side+'Width'])>0);
   chips.push({text:e.textContent.trim().slice(0,70),dx:t.x+t.width/2-b.x-b.width/2,dy:t.y+t.height/2-b.y-b.height/2,box:[b.x,b.y+window.scrollY,b.width,b.height],plain:!e.querySelector('.icon,.mark,.seat'),centeringRequired:e.matches('.pill,.tag')||ownFace||ownBox});
  }
  result.push({fixtureDOM:article.dataset.fixture,size:article.dataset.size,minimum:article.dataset.minimum==='1',slot:{x:box.x,y:box.y+window.scrollY,w:box.width,h:box.height},canvas:{x:sb.x,y:sb.y+window.scrollY,w:sb.width,h:sb.height},overflow:out,textOverlap:overlap,hiddenNameFig:hidden,chips,text});
 }
 return {fontStatus:document.fonts.status,loadedFonts:[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family),fontErrors:[...document.fonts].filter(f=>f.status==='error').map(f=>f.family),states:result};
}'''
def luminance(c):
 v=[x/255 for x in c[:3]];v=[x/12.92 if x<=.04045 else((x+.055)/1.055)**2.4 for x in v];return .2126*v[0]+.7152*v[1]+.0722*v[2]
def ratio(fg,bg):
 alpha=fg[3]/255;f=[fg[i]*alpha+bg[i]*(1-alpha)for i in range(3)];a,b=sorted([luminance(f),luminance(bg)]);return (b+.05)/(a+.05)
def source_png(cid,number):
 data=next(x for x in json.loads((ROOT/'collections.json').read_text())if x['id']==cid);d=ROOT/'reference/replica-html-render'/cid
 if not d.exists():d=ROOT/'reference/frozen'/(cid+'-review')/'replica'
 if not d.exists():d=Path(data['replica'])
 return next((p for p in d.glob('*.png')if re.search(r'(\d+)\.png$',p.name)[1].zfill(2)==str(number).zfill(2)),None)
async def render_leaf(page,cid,leaf,css,args):
 C=ROOT/cid;R=ROOT/(cid+'-review');E=C/'elements'/leaf;out=R/'sheets';out.mkdir(exist_ok=True)
 files=sorted((E/'fixtures').glob('*.html'));records=[];all_modes={};deps={leaf}
 for f in files:
  deps.update(re.findall(r'data-el=[\"\']'+re.escape(cid)+r'-([^\"\']+)',f.read_text()))
 inputs=[C/'kit/css/tokens.css',C/'foundation/foundation.css',C/'foundation/foundation.json',ROOT/'contract/palette.json',ROOT/'contract/type-steps.json',ROOT/'fonts/fonts.css',*files]
 inputs += [C/'elements'/dep/name for dep in sorted(deps) for name in ['element.css','element.json'] if (C/'elements'/dep/name).exists()]
 mapfile=R/'map.json';maps=json.loads(mapfile.read_text())if mapfile.exists()else{'instances':[]}
 mapped=[x for x in maps['instances']if x.get('leaf')==leaf and x.get('use')not in ['unexpressible','furniture','background']]
 map_signature=[{k:x.get(k)for k in ['page','bbox','use','fixture']}for x in mapped]
 engine=ENGINE_SHA
 fingerprint=hashlib.sha256((''.join(str(f.relative_to(ROOT))+f.read_text()for f in inputs)+json.dumps(map_signature,sort_keys=True)+engine).encode()).hexdigest()
 prior=R/'audits'/(leaf+'.json')
 if getattr(args,'skip_current',False) and prior.exists():
  old=json.loads(prior.read_text())
  required=[out/(leaf+'-light.png'),out/(leaf+'-dark.png')]+([out/(leaf+'-replica.png')]if mapped else[])
  if old.get('sourceSha256')==fingerprint and not old.get('quick') and not old.get('staleDuringRender') and all(x.exists()for x in required):
   print(cid,leaf,'current, unchanged',flush=True);return
 if not files:return
 for mode in ['light','dark']:
  rows=[]
  for f in files:
   raw=f.read_text();m=re.search(r'<!--\s*min:\s*(\d+)x(\d+)',raw)
   if not m:raise ValueError('min missing '+str(f))
   minimum=(int(m[1]),int(m[2]));sizes=[s for s in SIZES if s[0]>=minimum[0]and s[1]>=minimum[1]]
   if minimum not in sizes:sizes.append(minimum)
   if args.quick:sizes=list(dict.fromkeys([(12,6),minimum]))
   stages=[]
   for c,r in sizes:
    stages.append(f'<article data-fixture="{f.stem}" data-size="{c}x{r}" data-minimum="{int((c,r)==minimum)}"><section class="slide {"dark" if mode=="dark" else ""}"><div class="page"><div class="body">{fixture(raw,c,r)}</div></div></section></article>')
   palette=('.slide.dark{'if mode=='dark'else'.slide{')+''.join(k+':'+v+';'for k,v in PALETTE[mode].items())+'}'
   helper='html,body{margin:0;padding:0;width:1280px;background:#e5e7eb}article{position:relative;width:1280px;height:728px;overflow:visible}.icon{outline:1px dashed currentColor;outline-offset:-1px;border-radius:50%}.icon:empty{display:inline-flex}'
   doc='<!doctype html><html><meta charset="utf-8"><link rel="stylesheet" href="../fonts/fonts.css"><style>'+css+'\n'+palette+'\n'+helper+'</style><body>'+''.join(stages)+'</body></html>'
   # Serve generated workbench under the dedicated project root, never the filesystem root.
   tmp=ROOT/'.sheet-work';tmp.mkdir(exist_ok=True);htmlfile=tmp/(cid+'-'+leaf+'-'+mode+'.html');htmlfile.write_text(doc)
   await page.goto(args.url+'/.sheet-work/'+htmlfile.name+'?nonce='+str(time.time_ns()),wait_until='load');await page.evaluate('document.fonts.ready');await page.evaluate('window.scrollTo(0,0)');assert await page.locator('.slide').first.evaluate("e=>getComputedStyle(e).getPropertyValue('--type-12').trim()")=='12px','type tokens not loaded'
   audit=await page.evaluate(AUDIT);raw_image=await page.screenshot(full_page=True);normal=Image.open(io.BytesIO(raw_image)).convert('RGB')
   await page.add_style_tag(content='article *{-webkit-text-fill-color:transparent!important;text-shadow:none!important}article svg text{fill:transparent!important}')
   background=Image.open(io.BytesIO(await page.screenshot(full_page=True))).convert('RGB')
   await page.add_style_tag(content='article .body>*{visibility:hidden!important}')
   empty=Image.open(io.BytesIO(await page.screenshot(full_page=True))).convert('RGB')
   cells={}
   for state in audit['states']:
    assert state['fixtureDOM']==f.stem,('stale fixture',f.stem,state['fixtureDOM'])
    rect=state['slot'];pad=6;coords=[math.floor(rect['x']-pad),math.floor(rect['y']-pad),math.ceil(rect['x']+rect['w']+pad),math.ceil(rect['y']+rect['h']+pad)]
    crop=normal.crop(tuple(coords));cells[state['size']]=crop
    bad=[]
    for t in state.pop('text'):
     samples=[]
     for xx in [.25,.5,.75]:
      px=min(background.width-1,max(0,round(t['x']+t['w']*xx)));py=min(background.height-1,max(0,round(t['y']+t['h']*.5)));samples.append(background.getpixel((px,py)))
     cr=min(ratio(t['color'],bg)for bg in samples);threshold=3 if t['fontSize']>=28 else 4.5
     if cr+.02<threshold:bad.append({'text':t['text'],'ratio':round(cr,2),'min':threshold,'fontSize':t['fontSize'],'foreground':t['color'],'background':samples})
    state['contrastFailures']=bad;state['fixture']=f.stem;state['mode']=mode;state['fontStatus']=audit['fontStatus'];state['fontErrors']=audit['fontErrors'];state['loadedFonts']=audit['loadedFonts'];records.append(state)
   for state in audit['states']:
    canvas=state['canvas'];slot=state['slot'];sx=round(canvas['x']);sy=round(canvas['y']);stage=(sx,sy,sx+round(canvas['w']),sy+round(canvas['h']))
    diff=ImageChops.difference(normal.crop(stage),empty.crop(stage));channels=diff.split();mask=ImageChops.lighter(ImageChops.lighter(channels[0],channels[1]),channels[2]).point(lambda v:255 if v>24 else 0)
    ImageDraw.Draw(mask).rectangle((math.floor(slot['x']-sx-1.5),math.floor(slot['y']-sy-1.5),math.ceil(slot['x']-sx+slot['w']+1.5),math.ceil(slot['y']-sy+slot['h']+1.5)),fill=0)
    ink=mask.getbbox();pixels=mask.histogram()[255]
    state['paintOverflow']=({'box':[ink[0]+sx,ink[1]+sy,ink[2]-ink[0],ink[3]-ink[1]],'pixels':pixels}if ink and pixels>8 else None)
    for chip in state['chips']:
     x,y,w,h=chip['box'];bounds=(max(0,int(x)),max(0,int(y)),min(normal.width,math.ceil(x+w)),min(normal.height,math.ceil(y+h)))
     if bounds[2]<=bounds[0]or bounds[3]<=bounds[1]:continue
     delta=ImageChops.difference(normal.crop(bounds),background.crop(bounds));channels=delta.split();mask=ImageChops.lighter(ImageChops.lighter(channels[0],channels[1]),channels[2]).point(lambda v:255 if v>24 else 0)
     ink=mask.getbbox()
     if ink:
      chip['inkBox']=list(ink);chip['inkDX']=round(bounds[0]+(ink[0]+ink[2])/2-x-w/2,3);chip['inkDY']=round(bounds[1]+(ink[1]+ink[3])/2-y-h/2,3)
    state['chipAlignmentFailures']=[x for x in state['chips']if x['plain']and x['centeringRequired']and(abs(x.get('inkDX',0))>2.5 or abs(x.get('inkDY',0))>2.5)]
   rows.append({'fixture':f.stem,'min':str(minimum[0])+'x'+str(minimum[1]),'cells':cells})
  # Fixed columns for the advertised size list, plus any honest min that is not in it.
  cols=[str(c)+'x'+str(r)for c,r in SIZES];cols+=sorted({k for row in rows for k in row['cells']if k not in cols})
  widths={k:max([im.width for row in rows for n,im in row['cells'].items()if n==k]or[80])for k in cols}
  heights=[max(im.height for im in row['cells'].values())+38 for row in rows];labelw=210;W=labelw+sum(widths.values())+12*len(cols);H=40+sum(heights)
  sheet=Image.new('RGB',(W,H),'#e6e8ed');draw=ImageDraw.Draw(sheet);draw.text((10,10),cid+' / '+leaf+' / '+mode,font=FONT,fill='#1b2433')
  y=40
  for row,rh in zip(rows,heights):
   draw.text((8,y+8),row['fixture'],font=FONT,fill='#1b2433');draw.text((8,y+30),'min '+row['min'],font=FONT,fill='#5d6470');x=labelw
   for size in cols:
    if size in row['cells']:
     im=row['cells'][size];draw.text((x+5,y+4),size+('  MIN'if size==row['min']else''),font=FONT,fill='#151e2e');sheet.paste(im,(x,y+28));draw.rectangle((x+6,y+34,x+im.width-7,y+28+im.height-7),outline='#9ba4b2',width=1)
    x+=widths[size]+12
   y+=rh
  path=out/(leaf+'-'+mode+'.png');sheet.save(path);all_modes[mode]=rows
 # Visible base/variant replicas are cropped using the frozen map bbox exactly.
 mapfile=R/'map.json';maps=json.loads(mapfile.read_text())if mapfile.exists()else{'instances':[]}
 instances=[x for x in maps['instances']if x.get('leaf')==leaf and x.get('use')not in ['unexpressible','furniture','background']]
 comparison=[];reference_hashes=[]
 for inst in instances:
  num=inst['page'];f=source_png(cid,num)
  if f is None:continue
  reference_hashes.append({'page':num,'path':str(f.relative_to(ROOT)) if f.is_relative_to(ROOT)else str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
  bb=inst['bbox'];original=Image.open(f).convert('RGB');bounds=(round(bb[0]),round(bb[1]),round(bb[0]+bb[2]),round(bb[1]+bb[3]));ref=Image.new('RGB',(max(1,bounds[2]-bounds[0]),max(1,bounds[3]-bounds[1])),original.getpixel((0,0)));clipped=(max(0,bounds[0]),max(0,bounds[1]),min(original.width,bounds[2]),min(original.height,bounds[3]));ref.paste(original.crop(clipped),(clipped[0]-bounds[0],clipped[1]-bounds[1]))
  rows=all_modes['light'];row=next((r for r in rows if r['fixture']==Path(inst.get('fixture','')).stem),None)or next((r for r in rows if r['fixture']==f'replica-{str(num).zfill(2)}'),None)or next((r for r in rows if r['fixture'].startswith('replica-')),rows[0])
  twelve=row['cells'].get('12x6')or next(iter(row['cells'].values()));small=row['cells'].get(row['min'])or next(iter(row['cells'].values()))
  comparison.append((num,inst.get('use'),ref,twelve,small))
 if comparison:
  colw=1280;rowheights=[max(min(im.height,720)for im in row[2:])+36 for row in comparison];sheet=Image.new('RGB',(colw*3,sum(rowheights)),'#e6e8ed');d=ImageDraw.Draw(sheet);y=0
  for item,rh in zip(comparison,rowheights):
   n,use,*ims=item
   for k,(label,im) in enumerate(zip(['replica '+str(n)+' '+str(use),'12x6','min'],ims)):
    d.text((k*colw+8,y+6),label,font=FONT,fill='#152033');im=im.copy();im.thumbnail((colw,720));sheet.paste(im,(k*colw+(colw-im.width)//2,y+30))
   y+=rh
  sheet.save(out/(leaf+'-replica.png'))
 auditpath=R/'audits';auditpath.mkdir(exist_ok=True);data={'collection':cid,'leaf':leaf,'createdUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'sourceSha256':fingerprint,'quick':args.quick,'fixtureCount':len(files),'replicaReferences':reference_hashes,'states':records}
 data['engineSha256']=engine
 actual_sources=dict(re.findall(r'/\* source-sha256:([^:]+):([0-9a-f]{64}) \*/',css))
 expected_sources={str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest()for f in inputs}
 mismatches=[name for name,value in actual_sources.items()if name in expected_sources and expected_sources[name]!=value]
 final_fingerprint=hashlib.sha256((''.join(str(f.relative_to(ROOT))+f.read_text()for f in inputs)+json.dumps(map_signature,sort_keys=True)+engine).encode()).hexdigest()
 data['renderedCssSha256']=hashlib.sha256(css.encode()).hexdigest();data['staleDuringRender']=bool(mismatches or final_fingerprint!=fingerprint);data['sourceMismatches']=mismatches
 output_files=[out/(leaf+'-light.png'),out/(leaf+'-dark.png')]+([out/(leaf+'-replica.png')]if comparison else[])
 data['outputs']={str(f.relative_to(R)):hashlib.sha256(f.read_bytes()).hexdigest()for f in output_files}
 (auditpath/(leaf+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 failures=sum(bool(x['overflow']or x['textOverlap']or x['hiddenNameFig']or x['contrastFailures']or x.get('paintOverflow')or x.get('chipAlignmentFailures')or x.get('fontErrors'))for x in records)
 print(cid,leaf,len(records),'states;',failures,'flagged;',len(comparison),'replica crops',flush=True)
async def main(args):
 async with async_playwright()as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);page=await browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for cid in args.collections:
   C=ROOT/cid;leaves=args.leaf or [f.name for f in sorted((C/'elements').iterdir())if f.is_dir()]
   for leaf in leaves:await render_leaf(page,cid,leaf,load_css(C),args)
  await browser.close()
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('collections',nargs='+');parser.add_argument('--leaf',action='append');parser.add_argument('--url',default='http://127.0.0.1:8766');parser.add_argument('--quick',action='store_true');parser.add_argument('--skip-current',action='store_true');asyncio.run(main(parser.parse_args()))
