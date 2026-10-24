"""Render every fixture at the requested grid sizes, never resizing a slide.
PNG rows = fixtures, columns = eligible sizes; each crop has a 6px safety margin.
"""
from pathlib import Path
import argparse,json,re,hashlib,shutil,sys,html,io,math
from PIL import Image,ImageDraw,ImageFont
from playwright.sync_api import sync_playwright
sys.path.insert(0,str(Path(__file__).resolve().parent))
from pixel_contrast import audit as contrast_audit
from active_render_proof import equivalent as active_equivalent
sys.path.insert(0,'/workspace/work/tools')
from render_review import browser,serve_url,AUDIT_JS
BASE=Path('/workspace/work/rebuild-20261024');REF=Path('/workspace/work/reference');OLD=Path('/workspace/work/deliverables')
SIZES=[(12,6),(12,3),(9,4),(8,6),(6,6),(6,3),(4,4),(4,3),(3,3)]
MIN_RE=re.compile(r'\A<!--\s*min:\s*([^>]+)-->\s*')
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT=next(iter(Path('/usr/share/fonts').rglob('DejaVuSans.ttf')),None)
LABEL=ImageFont.truetype(str(FONT),18) if FONT else ImageFont.load_default()
def paths(name):
 w=BASE/name;return w,w/'collection'/name,w/'review'
def source_hash(c):
 h=hashlib.sha256()
 for p in sorted(x for x in c.rglob('*') if x.is_file()):h.update(str(p.relative_to(c)).encode());h.update(p.read_bytes())
 return h.hexdigest()
def assets(name):
 w,c,r=paths(name);a=r/'assets';a.mkdir(exist_ok=True)
 if not (a/'fonts/fonts.css').exists():shutil.copytree(REF/'fonts',a/'fonts',dirs_exist_ok=True)
 shutil.copytree(c,a/'collection',dirs_exist_ok=True)
 return a

def stylesheet(c,mode='light',host=False):
 kit=json.loads((c/'kit/kit.json').read_text());css=(c/'kit'/kit['tokens']).read_text()
 css+='\n'+(c/'foundation/foundation.css').read_text();defaults={};regs={}
 for p in sorted((c/'elements').glob('*/element.css')):
  css+='\n'+p.read_text();j=p.with_suffix('.json')
  if j.exists():d=json.loads(j.read_text());defaults.update(d.get('tokenDefaults',{}));regs.update(d.get('registrations',{}))
 steps=json.loads((REF/'contract/type-steps.json').read_text());palette=json.loads((REF/'contract/palette.json').read_text())
 if host and (c.parents[1]/'review/source-palette.json').exists():palette=json.loads((c.parents[1]/'review/source-palette.json').read_text())
 css+='\n.slide{'+''.join(f'--type-{v}:{v}px;'for v in steps)+''.join(f'{k}:{v};'for k,v in defaults.items())+'}'
 for m,vals in palette.items():css+='\n'+('.slide.dark' if m=='dark' else '.slide')+'{'+''.join(k+':'+v+';'for k,v in vals.items())+'}'
 css='\n'.join(regs.values())+css
 css+='\n.slide [data-icon]:empty::after{content:"";display:block;width:100%;height:100%;box-sizing:border-box;border:1.5px dashed currentColor;border-radius:50%;opacity:.7}'
 return css

def document(c,body,mode='light',host=False,title='Size probe'):
 return '<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=1280"><title>'+html.escape(title)+'</title><link rel="stylesheet" href="../assets/fonts/fonts.css"><style>html,body{margin:0;width:1280px;height:720px;overflow:hidden}'+stylesheet(c,mode,host)+'</style></head><body>'+body+'</body></html>'

def wrapper(fixture,c,r,mode):
 # Change placement only, preserving data variables on the fixture root.
 m=MIN_RE.match(fixture);fixture=fixture[m.end():] if m else fixture
 return '<section class="slide'+(' dark'if mode=='dark'else'')+'"><div class="page"><div class="body">'+fixture+'</div></div></section>'

MEASURE=r'''([cols,rows]) => {
 const slot=document.querySelector('.slide>.page>.body')?.firstElementChild;
 if(!slot)return {error:'missing fixture root'};
 let r=slot.getBoundingClientRect(),grid=document.querySelector('.slide>.page>.body'),gr=grid.getBoundingClientRect(),gs=getComputedStyle(grid),cw=gs.gridTemplateColumns.split(' ').map(parseFloat),rh=gs.gridTemplateRows.split(' ').map(parseFloat),slotRect={x:gr.x,y:gr.y,width:cw.slice(0,cols).reduce((a,b)=>a+b,0)+(cols-1)*parseFloat(gs.columnGap),height:rh.slice(0,rows).reduce((a,b)=>a+b,0)+(rows-1)*parseFloat(gs.rowGap)},rangeErrors=[],outside=[],overlap=[];
 const visible=e=>{let s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&+s.opacity>0&&r.width>0&&r.height>0};
 const texts=[];for(let e of [slot,...slot.querySelectorAll('*')])if(visible(e))for(let n of e.childNodes)if(n.nodeType===3&&n.textContent.trim()){
  let q=document.createRange();q.selectNodeContents(n);for(let z of q.getClientRects())if(z.width&&z.height){let t={text:n.textContent.trim(),selector:e.className?.baseVal??e.className,x:z.x,y:z.y,w:z.width,h:z.height};texts.push({e,rect:z,t});if(z.left<r.left-2||z.right>r.right+2||z.top<r.top-3||z.bottom>r.bottom+3)outside.push(t)}
 }
 for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){let a=texts[i],b=texts[j];if(a.e===b.e||a.e.contains(b.e)||b.e.contains(a.e)||a.e.closest('p,h1,h2,h3,b')===b.e.closest('p,h1,h2,h3,b')&&a.e.closest('p,h1,h2,h3,b'))continue;let w=Math.min(a.rect.right,b.rect.right)-Math.max(a.rect.left,b.rect.left),h=Math.min(a.rect.bottom,b.rect.bottom)-Math.max(a.rect.top,b.rect.top);if(w>3&&h>3&&w*h>15)overlap.push([a.t,b.t]);}
 const chips=[...slot.querySelectorAll('.pill,.tag,.mark,.chip')].filter(visible).filter(e=>!e.querySelector('.name,.note,.parts')).map(e=>{let a=e.getBoundingClientRect(),q=document.createRange();q.selectNodeContents(e);let b=q.getBoundingClientRect();return {text:e.textContent.trim(),x:((b.left+b.right-a.left-a.right)/2),y:((b.top+b.bottom-a.top-a.bottom)/2)}});
 return {slotRect,rect:{x:r.x,y:r.y,width:r.width,height:r.height},outsideText:outside,overlap,chipCenters:chips,textCount:texts.length};
}'''

def render(name,leaves=None,pixel=False,resume=False):
 w,c,r=paths(name);assets(name);(r/'sheets').mkdir(exist_ok=True);(r/'probes').mkdir(exist_ok=True)
 before=source_hash(c);all_reports=[]
 dirs=sorted(p for p in (c/'elements').iterdir() if p.is_dir() and (not leaves or p.name in leaves))
 with sync_playwright() as pw:
  b=browser(pw)
  for leafdir in dirs:
   leaf=leafdir.name;fixtures=sorted((leafdir/'fixtures').glob('*.html'));leaf_reports=[]
   cached=r/'sheets'/f'{leaf}-audit.json'
   if resume and cached.exists():
    d=json.loads(cached.read_text())
    if d.get('sourceSHA256')==before and d.get('sourceUnchanged') and all((r/'sheets'/f'{leaf}-{m}.png').exists()for m in ['light','dark']) and (not pixel or all(x.get('pixelContrast')is not None for x in d['cases'])):
     all_reports.extend(d['cases']);print(name,leaf,'verified cache',len(d['cases']),flush=True);continue
    proof=active_equivalent(b,c,r,leaf,fixtures,d,stylesheet(c),pixel)
    if proof:
     proof['currentSourceSHA256']=before;(r/'render-reuse').mkdir(exist_ok=True);(r/'render-reuse'/(leaf+'.json')).write_text(json.dumps(proof,ensure_ascii=False,indent=2));all_reports.extend(d['cases']);print(name,leaf,'active CSS equivalent cache',len(d['cases']),flush=True);continue
   for mode in ['light','dark']:
    rows=[];rowlabels=[]
    probe=r/'probes'/f'{leaf}-{mode}.html';probe.write_text(document(c,wrapper('<div></div>',12,6,mode),mode,title=name+' / '+leaf+' / '+mode))
    page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1);page.goto(serve_url(probe),wait_until='load');page.evaluate('document.fonts.ready')
    runtime_errors=[];page.on('pageerror',lambda e:runtime_errors.append(str(e)))
    for fix in fixtures:
     content=fix.read_text();m=MIN_RE.match(content);mins=[tuple(map(int,x)) for x in re.findall(r'(\d+)x(\d+)',m.group(1) if m else '')]
     if not mins:raise ValueError(str(fix)+' missing minimum')
     eligible=[x for x in SIZES if any(x[0]>=a and x[1]>=z for a,z in mins)]
     for mn in mins:
      if mn not in eligible:eligible.append(mn)
     rendered=[]
     body=content[m.end():] if m else content
     for cols,rs in eligible:
      page.evaluate('(html)=>document.querySelector(".slide>.page>.body").innerHTML=html',body)
      page.evaluate('([c,r])=>{let e=document.querySelector(".slide>.page>.body").firstElementChild;e.style.gridColumn="1 / span "+c;e.style.gridRow="1 / span "+r}',[cols,rs])
      page.evaluate('document.fonts.ready');page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
      a=page.evaluate(AUDIT_JS);geom=page.evaluate(MEASURE,[cols,rs]);rect=geom['slotRect'];pad=6
      x=max(0,math.floor(rect['x'])-pad);y=max(0,math.floor(rect['y'])-pad);ww=min(1280-x,math.ceil(rect['width'])+pad*2);hh=min(720-y,math.ceil(rect['height'])+pad*2)
      png=page.screenshot(clip={'x':x,'y':y,'width':ww,'height':hh},animations='disabled');im=Image.open(io.BytesIO(png)).convert('RGB')
      pixel_result=contrast_audit(page,png,{'x':x,'y':y,'width':ww,'height':hh}) if pixel else None
      label=f'{cols}x{rs}'+('  MIN' if (cols,rs) in mins else '')
      panel=Image.new('RGB',(im.width,im.height+30),'#dfe9ee' if (cols,rs) in mins else '#f0f0f0');ImageDraw.Draw(panel).text((6,5),label,font=LABEL,fill='#111111');panel.paste(im,(0,30));rendered.append(panel)
      record={'fixture':fix.stem,'fixtureSHA256':hashlib.sha256(content.encode()).hexdigest(),'mode':mode,'size':f'{cols}x{rs}','minimum':(cols,rs) in mins,'rect':rect,'elementRect':geom['rect'],'outsideText':geom['outsideText'],'textOverlaps':geom['overlap'],'clipped':a['clipped'],'rawOverflow':a['overflow'],'rawContrast':a['contrast'],'fontFailures':a['failedFonts'],'hiddenEssential':a['hiddenEssential'],'zeroRoots':a['zeroElementRoots'],'chipCenters':geom['chipCenters'],'scriptErrors':runtime_errors.copy(),'pixelContrast':pixel_result}
      leaf_reports.append(record)
      if (cols,rs)==(12,6) or (cols,rs)==mins[0]:
       extra=r/'probes'/f'{leaf}--{fix.stem}--{mode}--{cols}x{rs}.png';im.save(extra,compress_level=3)
     rw=sum(i.width for i in rendered)+12*(len(rendered)-1)+230;rh=max(i.height for i in rendered)+18;row=Image.new('RGB',(rw,rh),'#e8e8ec');draw=ImageDraw.Draw(row);draw.text((8,12),fix.stem,font=LABEL,fill='#111111');x=230
     for im in rendered:row.paste(im,(x,8));x+=im.width+12
     rows.append(row)
    page.close()
    if not rows:raise ValueError('No fixtures: '+leaf)
    sheet=Image.new('RGB',(max(x.width for x in rows),sum(x.height for x in rows)+38),'#e8e8ec');ImageDraw.Draw(sheet).text((10,8),name+' / '+leaf+' / '+mode,font=LABEL,fill='#111111');y=38
    for im in rows:sheet.paste(im,(0,y));y+=im.height
    sheet.save(r/'sheets'/f'{leaf}-{mode}.png',compress_level=3)
    # The paired HTML preserves the true-size rendered cells for convenient browser zoom/review.
   result={'collection':name,'leaf':leaf,'sourceSHA256':before,'sourceUnchanged':before==source_hash(c),'cases':leaf_reports}
   (r/'sheets'/f'{leaf}-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));all_reports.extend(leaf_reports)
   print(name,leaf,'cases',len(leaf_reports),'outside',sum(bool(x['outsideText']) for x in leaf_reports),'overlaps',sum(bool(x['textOverlaps']) for x in leaf_reports),'clip',sum(bool(x['clipped'])for x in leaf_reports),flush=True)
  b.close()
 result={'collection':name,'leaves':[x.name for x in dirs],'sourceSHA256':before,'sourceUnchanged':before==source_hash(c),'cases':len(all_reports),'outsideCases':sum(bool(x['outsideText'])for x in all_reports),'overlapCases':sum(bool(x['textOverlaps'])for x in all_reports),'clipCases':sum(bool(x['clipped'])for x in all_reports),'fontFailureCases':sum(bool(x['fontFailures'])for x in all_reports),'hiddenCases':sum(bool(x['hiddenEssential'])for x in all_reports),'zeroCases':sum(bool(x['zeroRoots'])for x in all_reports),'pixelFailureCases':sum(bool((x.get('pixelContrast')or{}).get('failures'))for x in all_reports)}
 (r/('size-summary-'+('-'.join(leaves)if leaves else'all')+'.json')).write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('name');a.add_argument('--only');a.add_argument('--contrast',action='store_true');a.add_argument('--resume',action='store_true');x=a.parse_args();render(x.name,set(x.only.split(','))if x.only else None,x.contrast,x.resume)
