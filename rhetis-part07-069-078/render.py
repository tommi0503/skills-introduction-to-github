"""Render source-backed replicas, library sheets and reassemblies through Chromium.
Run with socket/network permission; the localhost server exposes only this project tree.
"""
from pathlib import Path
from urllib.parse import quote
import argparse,importlib.util,json,re,hashlib,time
from PIL import Image,ImageDraw
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
REF=Path('/workspace/work/reference') if Path('/workspace/work/reference').exists() else ROOT/'reference'
DECKS={'vectorbox':'069','seedmark':'072','crossrail':'073','meridian-deck':'074','onboard-docket':'078'}
HTTP='http://127.0.0.1:8765/'

def url(p):return HTTP+quote(str(Path(p).relative_to(ROOT)))
def browser(p):return p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
def ready(page):
 page.evaluate('document.fonts.ready');page.evaluate('()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))');page.wait_for_timeout(100)

def source_fingerprint(P,kid,stage):
 folders=[P/stage]
 if stage=='replica':folders+=[P/'assets']
 if stage in ['library','reassembled']:folders+=[P/kid,P/'assets']
 hashes={}
 for folder in folders:
  for f in sorted(folder.rglob('*')):
   if f.is_file() and f.suffix in ['.html','.css','.json','.woff','.woff2','.js'] and not (stage=='library' and folder==P/stage):hashes[str(f.relative_to(P))]=hashlib.sha256(f.read_bytes()).hexdigest()
 return hashlib.sha256(json.dumps(hashes,sort_keys=True).encode()).hexdigest()

def record_fingerprint(P,kid,stage):
 f=P/'render-fingerprints.json';data=json.loads(f.read_text()) if f.exists() else {};data[stage]={'sha256':source_fingerprint(P,kid,stage),'timeUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())};f.write_text(json.dumps(data,indent=2))

def diagnostics(page):
 return page.evaluate('''() => {
 const box=e=>{let r=e.getBoundingClientRect();return {x:+r.x.toFixed(2),y:+r.y.toFixed(2),w:+r.width.toFixed(2),h:+r.height.toFixed(2)}};
 const out={viewport:[innerWidth,innerHeight],doc:[document.documentElement.scrollWidth,document.documentElement.scrollHeight],fonts:[...document.fonts].map(f=>({family:f.family,status:f.status})),overflow:[],clippedText:[],chips:[]};
 for(const el of document.querySelectorAll('body *')){
  const s=getComputedStyle(el),r=el.getBoundingClientRect();if(!r.width||!r.height||s.display==='none'||s.visibility==='hidden')continue;
  if(el.children.length===0&&el.textContent.trim()&&!['SCRIPT','STYLE','SPAN','I','B'].includes(el.tagName)){
   if(el.scrollWidth>el.clientWidth+2||el.scrollHeight>el.clientHeight+3)out.overflow.push({el:el.tagName+'.'+el.className,text:el.textContent.trim().slice(0,90),box:box(el),scroll:[el.scrollWidth,el.scrollHeight]});
  }
  if(el.children.length===0&&el.textContent.trim()&&['P','H1','H2','H3','B','SPAN','TD','TH','SMALL'].includes(el.tagName)){
   const ra=document.createRange();ra.selectNodeContents(el);const tr=ra.getBoundingClientRect();
   if(tr.width>r.width+3||tr.height>r.height+4)out.clippedText.push({el:el.tagName+'.'+el.className,text:el.textContent.trim().slice(0,90),box:box(el),textBox:{w:tr.width,h:tr.height}});
  }
  if(el.matches('.chip,.tag,.pill,.mark')&&el.textContent.trim()&&el.children.length===0){
   const ra=document.createRange();ra.selectNodeContents(el);const tr=ra.getBoundingClientRect();out.chips.push({text:el.textContent.trim().slice(0,30),dx:+((tr.x+tr.width/2)-(r.x+r.width/2)).toFixed(2),dy:+((tr.y+tr.height/2)-(r.y+r.height/2)).toFixed(2),box:box(el)});
  }
 }
 return out;
}''')

def slide_stage(kid,stage,page):
 P=ROOT/(kid+'-project');folder=P/stage;matches=list(Path('/workspace/work/deck/miricanvas_기업_selected').glob(DECKS[kid]+'*'));src=matches[0] if matches else None
 files=sorted(folder.glob('slide*.html'));assert files,(kid,stage)
 comp=P/('compare-'+stage);comp.mkdir(exist_ok=True)
 results=[];pdfs=[]
 for f in files:
  failed=[];bad=[]
  def fail(req):failed.append(req.url)
  def response(res):
   if res.status>=400:bad.append([res.status,res.url])
  page.on('requestfailed',fail);page.on('response',response)
  page.set_viewport_size({'width':1280,'height':720});page.goto(url(f),wait_until='networkidle');ready(page)
  diag=diagnostics(page);diag.update({'file':f.name,'failedResources':failed,'badResources':bad,'sourceSha256':hashlib.sha256(f.read_bytes()).hexdigest()})
  target=f.with_suffix('.png');page.screenshot(path=str(target),animations='disabled');im=Image.open(target);assert im.size==(1280,720)
  original=(src/(f.stem+'.png')) if src else None
  if original is not None and not original.exists():
   match=re.search(r'(\d+)$',f.stem);original=src/('slide_'+match.group(1).zfill(2)+'.png')
  if original is not None:
   assert original.exists(),original
   original_im=Image.open(original).convert('RGB')
  else:
   fallback=P/'compare-replica'/(f.stem+'.png');original_im=Image.open(fallback).crop((0,0,1280,720)).convert('RGB')
  side=Image.new('RGB',(2560,720));side.paste(original_im,(0,0));side.paste(im,(1280,0));side.save(comp/target.name)
  page.pdf(path=str(folder/(f.stem+'.pdf')),width='1280px',height='720px',print_background=True,prefer_css_page_size=False,margin={'top':'0','bottom':'0','left':'0','right':'0'})
  pdfs.append(folder/(f.stem+'.pdf'));results.append(diag)
  page.remove_listener('requestfailed',fail);page.remove_listener('response',response)
 import fitz
 doc=fitz.open()
 for p in pdfs:
  with fitz.open(p) as q:doc.insert_pdf(q)
  p.unlink()
 doc.save(folder/(stage+'.pdf'),deflate=True);doc.close()
 (P/(stage+'-render-checks.json')).write_text(json.dumps(results,ensure_ascii=False,indent=2))
 record_fingerprint(P,kid,stage)
 print(kid,stage,len(files),'pages',flush=True)

def library(kid,page):
 P=ROOT/(kid+'-project');out=P/'library';out.mkdir(exist_ok=True)
 s=importlib.util.spec_from_file_location('rhetis_preview',REF/'tools/preview.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
 steps=json.loads((REF/'contract/type-steps.json').read_text());palette=json.loads((REF/'contract/palette.json').read_text())
 allchecks={}
 for dark in [False,True]:
  mode='dark' if dark else 'light';html=m.sheet(P/kid,steps,palette,dark=dark,fonts_href='../assets/fonts/fonts.css');f=out/(mode+'.html');f.write_text(html)
  page.set_viewport_size({'width':1360,'height':900});page.goto(url(f),wait_until='networkidle');ready(page)
  # All-fixture PDF, each fixture occupies a 1280 x 720 physical page.
  page.add_style_tag(content='@media print{html,body{margin:0!important;padding:0!important;display:block!important;background:none!important}article{margin:0!important;padding:0!important;width:1280px!important;height:720px!important;break-after:page;overflow:hidden}article>h2{display:none!important}.frame{width:1280px!important;height:720px!important;border-radius:0!important;overflow:hidden!important}.frame>.slide{transform:none!important;position:relative!important}}')
  page.pdf(path=str(out/('library-'+mode+'.pdf')),width='1280px',height='720px',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'})
  # Screenshot each element's fixtures as a separate sheet.
  names=['foundation']+sorted(p.name for p in (P/kid/'elements').iterdir() if p.is_dir())
  for name in names:
   page.evaluate('''name=>{for(const a of document.querySelectorAll('article'))a.style.display=a.querySelector('h2').textContent.startsWith(name+' / ')?'':'none'}''',name)
   page.screenshot(path=str(out/(name+'-'+mode+'.png')),full_page=True,animations='disabled')
  page.evaluate("()=>{for(const a of document.querySelectorAll('article'))a.style.display=''}")
  # Actual full-size fixture boxes; measure at declared minimum, 6x3 and 12x6.
  checks=[]
  count=page.locator('article').count()
  for i in range(count):
   a=page.locator('article').nth(i);title=a.locator(':scope > h2').inner_text();minmatch=re.search(r'min\s+(\d+)x(\d+)',title)
   sizes=[(12,6)]
   if minmatch:sizes.insert(0,(int(minmatch.group(1)),int(minmatch.group(2))))
   if minmatch:
    mid=((int(minmatch.group(1))+13)//2,(int(minmatch.group(2))+7)//2)
    if mid not in sizes:sizes.insert(-1,mid)
   # Widths are measured unscaled in the real 12x6 body grid.
   a.evaluate("a=>{let f=a.querySelector('.frame');f.style.width='1280px';f.style.height='720px';let s=f.querySelector('.slide');s.style.transform='none'}")
   for c,r in sizes:
    a.evaluate('''(a,s)=>{let b=a.querySelector('.body');if(b&&!a.querySelector(':scope > h2').textContent.startsWith('foundation /'))for(let el of b.children){el.style.gridColumn='1 / span '+s[0];el.style.gridRow='1 / span '+s[1]}}''',[c,r])
    info=a.evaluate('''a=>{const issues=[];for(const e of a.querySelectorAll('.body *')){let s=getComputedStyle(e),r=e.getBoundingClientRect();if(!r.width||!r.height||s.display==='none'||e.children.length||!e.textContent.trim())continue;if(e.matches('b')&&e.closest('.bars.quiet')&&s.position==='absolute'&&r.width<=2&&r.height<=2&&s.clipPath!=='none')continue;if(e.scrollWidth>e.clientWidth+3||e.scrollHeight>e.clientHeight+4)issues.push({class:e.className,text:e.textContent.slice(0,80),client:[e.clientWidth,e.clientHeight],scroll:[e.scrollWidth,e.scrollHeight]})}return issues}''')
    checks.append({'fixture':title,'size':[c,r],'overflowCandidates':info})
   a.evaluate("a=>{let f=a.querySelector('.frame');f.style.width='';f.style.height='';f.querySelector('.slide').style.transform=''}")
  allchecks[mode]={'sizeChecks':checks,'contrast':page.evaluate((ROOT/'contrast.js').read_text())}
  print(kid,'library',mode,count,'fixtures',flush=True)
 (P/'library-render-checks.json').write_text(json.dumps(allchecks,ensure_ascii=False,indent=2))
 record_fingerprint(P,kid,'library')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('collection',choices=DECKS);ap.add_argument('stage',choices=['replica','library','reassembled','all']);a=ap.parse_args()
 with sync_playwright() as p:
  b=browser(p);page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for stage in (['replica','library','reassembled'] if a.stage=='all' else [a.stage]):
   if stage=='library':library(a.collection,page)
   else:slide_stage(a.collection,stage,page)
  b.close()
