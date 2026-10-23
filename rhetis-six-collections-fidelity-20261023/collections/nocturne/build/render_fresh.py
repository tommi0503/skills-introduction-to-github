"""Shared, source-preserving Chromium review renderer. Run with network-enabled execution permissions.
Commands: pages --root WORKER --kind replica|reassembled --original-dir DIR
          library --root WORKER --name COLLECTION [--only element,element]
All diagnostic CSS is confined to review HTML; collection source is never changed.
"""
from pathlib import Path
import argparse,json,re,sys,shutil,subprocess,hashlib,importlib.util,time,threading
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from urllib.parse import quote
from functools import partial
_SERVER=None
def serve_url(path):
 global _SERVER
 if _SERVER is None:
  class Quiet(SimpleHTTPRequestHandler):
   def log_message(self,*args):pass
   def copyfile(self,source,outputfile):
    try:super().copyfile(source,outputfile)
    except (BrokenPipeError,ConnectionResetError):pass
  _SERVER=ThreadingHTTPServer(("127.0.0.1",0),partial(Quiet,directory="/workspace"))
  threading.Thread(target=_SERVER.serve_forever,daemon=True).start()
 return "http://127.0.0.1:"+str(_SERVER.server_port)+"/"+quote(str(Path(path).resolve().relative_to("/workspace")))
from PIL import Image
import fitz
from playwright.sync_api import sync_playwright
REF=Path('/workspace/work/reference')
AUDIT_JS=r'''() => {
 const visible=e=>{let s=getComputedStyle(e),r=e.getBoundingClientRect();return s.visibility!=='hidden'&&s.display!=='none'&&Number(s.opacity)!==0&&r.width>0&&r.height>0};
 const rect=r=>({x:+r.x.toFixed(2),y:+r.y.toFixed(2),width:+r.width.toFixed(2),height:+r.height.toFixed(2)});
 const textRects=[],clipped=[],overflow=[],chips=[],contrast=[];
 const canvas=document.createElement('canvas');canvas.width=canvas.height=1;const ctx=canvas.getContext('2d',{willReadFrequently:true});
 const rgba=c=>{ctx.clearRect(0,0,1,1);ctx.fillStyle=c;ctx.fillRect(0,0,1,1);return [...ctx.getImageData(0,0,1,1).data].map((v,i)=>i===3?v/255:v/255)};
 const composite=(fg,bg)=>{let a=fg[3]+bg[3]*(1-fg[3]);return [0,1,2].map(i=>(fg[i]*fg[3]+bg[i]*bg[3]*(1-fg[3]))/Math.max(a,.0001)).concat(a)};
 const lum=c=>c.slice(0,3).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((a,v,i)=>a+v*[.2126,.7152,.0722][i],0);
 const ratio=(a,b)=>{let x=lum(a),y=lum(b);return(Math.max(x,y)+.05)/(Math.min(x,y)+.05)};
 const root=document.querySelector('.slide')||document.body;
 const rr=root.getBoundingClientRect();
 for(const el of root.querySelectorAll('*')) {
  if(!visible(el))continue;
  let s=getComputedStyle(el),r=el.getBoundingClientRect();
  if(el.scrollWidth>el.clientWidth+2 && el.clientWidth>0 && !['svg','path'].includes(el.tagName.toLowerCase())) overflow.push({selector:el.className?.baseVal??el.className,text:el.innerText?.slice(0,70),axis:'x',excess:el.scrollWidth-el.clientWidth});
  if(el.scrollHeight>el.clientHeight+3 && el.clientHeight>0 && !['svg','path'].includes(el.tagName.toLowerCase())) overflow.push({selector:el.className?.baseVal??el.className,text:el.innerText?.slice(0,70),axis:'y',excess:el.scrollHeight-el.clientHeight});
  for(const n of el.childNodes)if(n.nodeType===Node.TEXT_NODE && n.textContent.trim()){
   let range=document.createRange();range.selectNodeContents(n);
   for(const tr of range.getClientRects())if(tr.width>0&&tr.height>0){
    const item={text:n.textContent.trim().slice(0,90),selector:el.className?.baseVal??el.className,rect:rect(tr),size:s.fontSize};textRects.push(item);
    let stack=[],ap=el,gradient=false;while(ap){let bs=getComputedStyle(ap),base=rgba(bs.backgroundColor),colors=[base];
     if(bs.backgroundImage!=='none'){gradient=true;let stops=bs.backgroundImage.match(/(?:oklch|oklab|rgba?|hsla?|color)\([^)]*\)/g);if(stops?.length)colors=stops.map(c=>composite(rgba(c),base));}
     stack.unshift(colors);ap=ap.parentElement;
    }
    let bgs=[[1,1,1,1]];for(let options of stack){bgs=bgs.flatMap(bg=>options.map(c=>composite(c,bg)));if(bgs.length>2){bgs.sort((a,b)=>lum(a)-lum(b));bgs=[bgs[0],bgs.at(-1)];}}
    let fgColor=rgba(s.color),cr=Math.min(...bgs.map(bg=>ratio(composite(fgColor,bg),bg))),limit=parseFloat(s.fontSize)>=28?3:4.5;
    if(cr<limit-.05)contrast.push({...item,ratio:+cr.toFixed(2),required:limit,gradientNeedsVisualCheck:gradient});
    let a=el;while(a){let as=getComputedStyle(a),ar=a.getBoundingClientRect();
     if(['hidden','clip','auto','scroll'].includes(as.overflowX)||['hidden','clip','auto','scroll'].includes(as.overflowY)){
      if(tr.left<ar.left-2||tr.right>ar.right+2||tr.top<ar.top-4||tr.bottom>ar.bottom+4){clipped.push({...item,clipBy:a.className?.baseVal??a.className});break;}
     }a=a.parentElement;
    }
   }
  }
  if(el.matches('.chip,.tag,.pill,.mark,.meta button,button')){
   const cr=el.getBoundingClientRect();let range=document.createRange();range.selectNodeContents(el);let tr=range.getBoundingClientRect();
   if(tr.width&&tr.height&&el.childElementCount===0)chips.push({text:el.textContent.trim(),selector:el.className,offsetX:+((tr.left+tr.right-cr.left-cr.right)/2).toFixed(2),offsetY:+((tr.top+tr.bottom-cr.top-cr.bottom)/2).toFixed(2),display:s.display,align:s.alignItems,justify:s.justifyContent});
  }
 }
 const fonts=[...document.fonts].map(f=>({family:f.family,status:f.status,weight:f.weight}));
 return {viewport:{width:innerWidth,height:innerHeight},document:{width:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight},slide:rect(rr),fonts,failedFonts:fonts.filter(f=>f.status==='error'),clipped,overflow,chips,contrast,zeroElementRoots:[...root.querySelectorAll("[data-el]")].filter(e=>{let s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=="contents"&&s.display!=="none"&&(r.width<1||r.height<1)}).map(e=>({element:e.dataset.el,class:e.className})),iconErrors:[...root.querySelectorAll("[data-icon-error]")].map(e=>e.dataset.icon),hiddenEssential:[...root.querySelectorAll(".name,.fig")].filter(e=>e.textContent.trim()&&!visible(e)).map(e=>({text:e.textContent.trim().slice(0,70),selector:e.className})),textNodes:textRects.length};
}'''
def browser(p):return p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu','--allow-file-access-from-files'])
def pdf_from_pngs(paths,out):
 doc=fitz.open()
 for p in paths:
  im=Image.open(p);page=doc.new_page(width=1280,height=720);page.insert_image(page.rect,filename=str(p))
 doc.save(out,deflate=True);doc.close()
def load(page,path):
 page.goto(serve_url(path),wait_until='load');page.evaluate('document.fonts.ready');page.evaluate('() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))');page.wait_for_timeout(80)
def pages(a):
 root=Path(a.root).resolve();folder=root/'review'/a.kind;original=Path(a.original_dir).resolve();folder.mkdir(parents=True,exist_ok=True)
 files=sorted(p for p in folder.glob('*.html') if p.stem not in ['index','preview'])
 if not files:raise ValueError(f'No page HTML in {folder}')
 report=[];pngs=[]
 compare=root/'review'/f'compare-{a.kind}';compare.mkdir(exist_ok=True)
 with sync_playwright() as p:
  b=browser(p)
  for f in files:
   page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
   errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   load(page,f);page.evaluate("() => new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))");page.wait_for_timeout(100);audit=page.evaluate(AUDIT_JS);audit.update(file=f.name,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),errors=errors)
   png=f.with_suffix('.png');page.screenshot(path=str(png),clip={'x':0,'y':0,'width':1280,'height':720},animations='disabled');pngs.append(png)
   match=re.search(r'(\d+)$',f.stem);num=int(match[1]) if match else None
   src=original/f'{f.stem}.png'
   if not src.exists() and num is not None:
    candidates=list(original.glob(f'*_{num:02}.png'))+list(original.glob(f'*_{num}.png'))
    if candidates:src=candidates[0]
   if src.exists():
    orig=Image.open(src).convert('RGB');rendered=Image.open(png).convert('RGB');im=Image.new('RGB',(2560,720));im.paste(orig,(0,0));im.paste(rendered,(1280,0));im.save(compare/(f.stem+'.png'))
   else:audit['missing_original']=str(src)
   report.append(audit);page.close()
  b.close()
 pdf_from_pngs(pngs,folder/f'{a.kind}.pdf')
 (root/'review'/f'audit-{a.kind}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 print(json.dumps({'pages':len(files),'size':[1280,720],'clipped':sum(len(x['clipped']) for x in report),'overflow':sum(len(x['overflow']) for x in report),'fontFailures':sum(len(x['failedFonts']) for x in report)},ensure_ascii=False))
def library(a):
 root=Path(a.root).resolve();collection=root/'collection'/a.name;review=root/'review';lib=review/'library';lib.mkdir(parents=True,exist_ok=True)
 assets=review/'assets'/'fonts';shutil.copytree(REF/'fonts',assets,dirs_exist_ok=True)
 spec=importlib.util.spec_from_file_location('rhetis_preview',REF/'tools'/'preview.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 steps=json.loads((REF/'contract'/'type-steps.json').read_text());palette=json.loads((REF/'contract'/'palette.json').read_text())
 report=[];only=set(a.only.split(',')) if a.only else None
 with sync_playwright() as p:
  b=browser(p);context=b.new_context(viewport={'width':1328,'height':900},device_scale_factor=1);page=context.new_page();probe=context.new_page();probe.set_viewport_size({'width':1280,'height':720})
  for dark in [False,True]:
   mode='dark' if dark else 'light';sheet=module.sheet(collection,steps,palette,dark=dark,fonts_href='../assets/fonts/fonts.css')
   file=lib/f'{mode}.html';file.write_text(sheet)
   load(page,file)
   load(probe,file)
   probe.add_style_tag(content='body{display:block;margin:0;padding:0;width:1280px;height:720px;overflow:hidden}body>.slide{width:1280px;height:720px;transform:none;position:relative}')
   # Browser constructs independent full + minimum slots directly from unchanged fixtures.
   page.evaluate('''() => {let original=[...document.querySelectorAll('body>article')];let all=[];for(let a of original){
    let t=a.querySelector('h2').textContent;let m=[...t.matchAll(/(\\d+)x(\\d+)/g)].map(x=>[+x[1],+x[2]]);let sizes=[[12,6],...m.filter(([c,r])=>c!==12||r!==6)];
    for(let [c,r] of sizes){let clone=a.cloneNode(true);clone.dataset.folder=t.split(' / ')[0];clone.dataset.fixture=t.split(' / ')[1]?.split(' min ')[0];clone.dataset.cols=c;clone.dataset.rows=r;
     clone.querySelector('h2').textContent=t.split(' min ')[0]+' · '+c+'×'+r;
     let root=clone.querySelector('.body')?.firstElementChild;
     if(root){root.style.gridColumn='1 / span '+c;root.style.gridRow='1 / span '+r;}
     all.push(clone);
    }
   }document.body.replaceChildren(...all);document.body.style.gridTemplateColumns='repeat(2,640px)';document.body.style.width='1280px';}''')
   folders=page.locator('body>article').evaluate_all('(xs)=>[...new Set(xs.map(x=>x.dataset.folder))]')
   # Store a portable expanded review sheet, with relative font href.
   expanded=lib/f'{mode}-sizes.html';expanded.write_text(page.content())
   pdf=fitz.open()
   for folder in folders:
    if only and folder not in only:continue
    group=lib/folder;group.mkdir(exist_ok=True)
    page.evaluate('(folder)=>{for(let e of document.querySelectorAll("body>article"))e.style.display=e.dataset.folder===folder?"block":"none"}',folder)
    page.wait_for_timeout(20)
    height=page.evaluate('document.documentElement.scrollHeight');page.screenshot(path=str(group/f'{mode}.png'),full_page=True,animations='disabled')
    # Inspect every fixture at full device resolution, including all declared minimums.
    items=page.locator('body>article[data-folder="'+folder+'"]').all()
    for idx,item in enumerate(items):
     if item.get_attribute('data-folder')!=folder:continue
     title=item.locator(':scope > h2').inner_text();slide=item.locator('.slide').first
     # Use isolated content at full scale to get valid 1280x720 measurement.
     html=slide.evaluate('(e)=>e.outerHTML');head=page.locator('head').inner_html()
     probe.evaluate('(html)=>document.body.innerHTML=html',html)
     probe.evaluate('document.fonts.ready')
     audit=probe.evaluate(AUDIT_JS);audit.update(mode=mode,folder=folder,fixture=title)
     report.append(audit)
     # All fixtures at max size in the complete PDF; minimums appear in element sheets.
     if item.get_attribute('data-cols')=='12' and item.get_attribute('data-rows')=='6':
      data=probe.screenshot(clip={'x':0,'y':0,'width':1280,'height':720},animations='disabled');pp=pdf.new_page(width=1280,height=720);pp.insert_image(pp.rect,stream=data)
    print(f'{a.name} {mode} {folder}',flush=True)
   if not only:pdf.save(lib/f'library-{mode}.pdf',deflate=True)
   pdf.close()
  b.close()
 (review/'audit-library.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 print(json.dumps({'probes':len(report),'clipped':sum(len(x['clipped']) for x in report),'overflow':sum(len(x['overflow']) for x in report),'failedFonts':sum(len(x['failedFonts']) for x in report)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();s=p.add_subparsers(dest='command',required=True)
 x=s.add_parser('pages');x.add_argument('--root',required=True);x.add_argument('--kind',choices=['replica','reassembled'],required=True);x.add_argument('--original-dir',required=True);x.set_defaults(func=pages)
 x=s.add_parser('library');x.add_argument('--root',required=True);x.add_argument('--name',required=True);x.add_argument('--only');x.set_defaults(func=library)
 a=p.parse_args();a.func(a)
