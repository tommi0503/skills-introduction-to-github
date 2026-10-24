from pathlib import Path
import json,re,subprocess,hashlib,time
from playwright.sync_api import sync_playwright
R=Path('/workspace/work/rhetis-elements-v2'); PRE=Path('/workspace/work/reference/tools/preview.py');STEPS=Path('/workspace/work/reference/contract/type-steps.json')
projects=[]
for P in sorted(R.glob('*-project')):
 K=next(x for x in P.iterdir() if x.is_dir() and (x/'kit/kit.json').exists()); k=K.name;projects.append((P,K,k))
 for mode in ['light','dark']:
  out=P/f'contract-preview-{mode}.html';cmd=['python',str(PRE),str(K),str(STEPS),'--fonts',str(P/'assets/fonts/fonts.css'),'--out',str(out)]
  if mode=='dark':cmd.append('--dark')
  subprocess.run(cmd,check=True,capture_output=True,text=True)
  s=out.read_text();s=re.sub(r'<link rel="stylesheet" href="[^"]+">','<link rel="stylesheet" href="assets/fonts/fonts.css">',s,count=1);out.write_text(s)
report={'generatedAtUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'generator':'reference/tools/preview.py CLI, official palette and type steps unchanged','generatorSHA256':hashlib.sha256(PRE.read_bytes()).hexdigest(),'onlyPostGenerationEdit':'font stylesheet href changed to relative assets/fonts/fonts.css','projects':[]}
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 for P,K,k in projects:
  pr={'collection':k,'modes':{}}
  for mode in ['light','dark']:
   ctx=browser.new_context(viewport={'width':1440,'height':900},device_scale_factor=1);page=ctx.new_page();errs=[];console=[];page.on('requestfailed',lambda req:errs.append({'url':req.url,'failure':req.failure}));page.on('pageerror',lambda e:console.append(str(e)));f=P/f'contract-preview-{mode}.html';url='http://127.0.0.1:8875/'+str(f.relative_to(R));response=page.goto(url,wait_until='networkidle');page.evaluate('document.fonts.ready');page.wait_for_timeout(250)
   d=page.evaluate('''()=>{const slides=[...document.querySelectorAll('.frame>.slide')];const faces=[...document.fonts].map(f=>({family:f.family.replaceAll('"','').replaceAll("'",''),status:f.status,weight:f.weight}));const used=new Map;for(const s of slides)for(const e of [s,...s.querySelectorAll('*')]){if(![...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim()))continue;const cs=getComputedStyle(e);if(cs.display==='none'||cs.visibility==='hidden')continue;const fam=cs.fontFamily.split(',')[0].trim().replaceAll('"','').replaceAll("'",'');const key=fam+'|'+cs.fontWeight;used.set(key,{family:fam,weight:cs.fontWeight,fontFaceDeclared:faces.some(f=>f.family===fam),loaded:faces.some(f=>f.family===fam&&f.status==='loaded'),browserCheck:document.fonts.check(cs.fontSize+' '+cs.fontFamily,e.textContent.slice(0,32)),example:e.textContent.trim().slice(0,32)})}return {fontStylesheet:[...document.querySelectorAll('link[rel=stylesheet]')].map(l=>l.getAttribute('href')),slides:slides.map((e,i)=>{let cs=getComputedStyle(e),r=e.getBoundingClientRect();return {index:i,label:e.closest('article').querySelector('h2').textContent,width:parseFloat(cs.width),height:parseFloat(cs.height),paintedWidth:r.width,paintedHeight:r.height,dark:e.classList.contains('dark')}}),usedFonts:[...used.values()],fontFaces:faces}}''')
   d.update(httpStatus=response.status if response else None,requestFailures=errs,javascriptErrors=console,url=url,htmlSHA256=hashlib.sha256(f.read_bytes()).hexdigest());d['slideSizeFailures']=[s for s in d['slides'] if s['width']!=1280 or s['height']!=720 or s['paintedWidth']!=640 or s['paintedHeight']!=360];d['modeFailures']=[s for s in d['slides'] if s['dark']!=(mode=='dark')];d['fontFailures']=[f for f in d['usedFonts'] if not(f['fontFaceDeclared'] and f['loaded'] and f['browserCheck'])];pr['modes'][mode]=d;ctx.close();print(k,mode,'slides',len(d['slides']),'size',len(d['slideSizeFailures']),'font',len(d['fontFailures']),'resource',len(errs),'js',len(console),flush=True)
  (P/'contract-preview-proof.json').write_text(json.dumps(pr,ensure_ascii=False,indent=2)+'\n');report['projects'].append(pr)
 browser.close()
(R/'contract-preview-proof.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
