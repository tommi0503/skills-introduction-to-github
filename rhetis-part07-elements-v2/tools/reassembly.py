"""Render existing contract-only assemblies; never modify or re-render immutable replicas."""
from pathlib import Path
import argparse,json,re,hashlib,time
from lxml import html
from PIL import Image
from playwright.sync_api import sync_playwright
from sheets import ROOT,REF,HTTP,AUDIT,fingerprint

DECKS={'vectorbox':'069','seedmark':'072','crossrail':'073','meridian-deck':'074','onboard-docket':'078'}
ORIGINALS=Path('/workspace/work/deck/miricanvas_기업_selected')

def platform(k):
 P=ROOT/(k+'-project');K=P/k
 css='/* Host reset, official type steps and JSON registrations/defaults only. No design rules. */\nhtml,body{margin:0;padding:0;width:1280px;height:720px;}\n.slide{'+''.join(f'--type-{n}:{n}px;'for n in json.loads((REF/'contract/type-steps.json').read_text()))+'}\n'
 for f in [K/'foundation/foundation.json']+sorted((K/'elements').glob('*/element.json')):
  meta=json.loads(f.read_text());css+='\n'+''.join(meta.get('registrations',{}).values())
  if meta.get('tokenDefaults'):css+='\n.slide{'+''.join(f'{a}:{b};'for a,b in meta['tokenDefaults'].items())+'}'
 target=P/'assets/v2-platform.css';target.write_text(css)
 return target

def run(k,pages=None):
 P=ROOT/(k+'-project');D=P/'reassembled';C=P/'compare-reassembled';C.mkdir(exist_ok=True);platform(k)
 originals=next(ORIGINALS.glob(DECKS[k]+'_*'))
 files=sorted(D.glob('slide_*.html'));assert files,('no fresh reassembly source',k)
 if pages:files=[f for f in files if f.stem.removeprefix('slide_') in pages]
 results=[]
 with sync_playwright() as pw:
  browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
  for f in files:
   # A new isolated context prevents Chromium's variable-font glyph-cache
   # regression across navigations (computed style may be correct but ink absent).
   page=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
   # A shared host stylesheet supplies the defaults the Rhetis runtime normally installs.
   s=f.read_text()
   if '../assets/v2-platform.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="../assets/v2-platform.css"></head>');f.write_text(s)
   doc=html.fromstring(s);assert not doc.xpath('//style'),('page CSS forbidden',f)
   forbidden=[]
   for e in doc.xpath('//*[@style]'):
    for prop,value in re.findall(r'([\w-]+)\s*:\s*([^;]+)',e.get('style')):
     if prop not in ['grid-column','grid-row'] and not prop.startswith('--'):forbidden.append((prop,value))
   assert not forbidden,('page style forbidden',f,forbidden)
   failed=[]
   def fail(r):failed.append({'url':r.url,'failure':r.failure})
   page.on('requestfailed',fail);response=page.goto(HTTP+str(f.relative_to(ROOT)),wait_until='networkidle');assert response.status==200
   page.evaluate('document.fonts.ready');page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
   # Chromium can defer font rasterisation after layout/font readiness.
   page.wait_for_timeout(250)
   slide=page.locator('.slide');assert slide.count()==1
   box=slide.bounding_box();assert abs(box['width']-1280)<.1 and abs(box['height']-720)<.1,(f,box)
   diag=slide.evaluate(AUDIT);diag['page']=f.stem;diag['requestFailures']=failed
   diag['sourceFingerprint']=fingerprint(P,k);diag['htmlSHA256']=hashlib.sha256(f.read_bytes()).hexdigest()
   slide.screenshot(path=str(D/(f.stem+'.png')),animations='disabled');page.remove_listener('requestfailed',fail)
   original=Image.open(originals/(f.stem+'.png')).convert('RGB');replica=Image.open(P/'replica'/(f.stem+'.png')).convert('RGB');assembled=Image.open(D/(f.stem+'.png')).convert('RGB')
   assert original.size==replica.size==assembled.size==(1280,720)
   triple=Image.new('RGB',(3840,720));triple.paste(original,(0,0));triple.paste(replica,(1280,0));triple.paste(assembled,(2560,0));triple.save(C/(f.stem+'.png'))
   results.append(diag);page.close();print(k,f.stem,'rendered',flush=True)
  browser.close()
 (P/'reassembly-checks.json').write_text(json.dumps({'collection':k,'generatedAtUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'isolatedContextPerPage':True,'paintSettleMilliseconds':250,'rendererSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'columnOrder':['original','immutable replica','contract assembly'],'pages':results},ensure_ascii=False,indent=2))

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('collection');ap.add_argument('--pages',nargs='+');a=ap.parse_args();run(a.collection,a.pages)
