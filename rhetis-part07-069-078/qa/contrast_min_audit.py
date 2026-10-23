"""Minimum-slot light/dark contrast, separate from full-sheet contrast report."""
import json,sys,hashlib,re,importlib.util
from playwright.sync_api import sync_playwright
from audit_css import BASE,REFERENCE,COLLECTIONS
s=importlib.util.spec_from_file_location('pv',REFERENCE/'tools/preview.py');pv=importlib.util.module_from_spec(s);s.loader.exec_module(pv)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page(viewport={'width':1360,'height':900});q.goto('http://127.0.0.1:8765/qa/probe.html')
 for k in sys.argv[1:] or COLLECTIONS:
  reports={}
  for dark in [False,True]:
   m=pv.sheet(BASE/(k+'-project')/k,json.loads((REFERENCE/'contract/type-steps.json').read_text()),json.loads((REFERENCE/'contract/palette.json').read_text()),dark=dark,fonts_href=f'/{k}-project/assets/fonts/fonts.css');q.set_content(m,wait_until='networkidle');q.evaluate('document.fonts.ready');allr=[]
   for phase in [0,1]:
    tested=0
    for a in q.locator('article').all():
     title=a.locator(':scope > h2').inner_text();sizes=[tuple(map(int,x)) for x in re.findall(r'(\d+)x(\d+)',title.split('min',1)[-1])]
     if not sizes:continue
     if phase>=len(sizes):a.evaluate("a=>a.style.display='none'");continue
     a.evaluate("a=>a.style.display=''");tested+=1
     a.evaluate('''(a,size)=>{let f=a.querySelector('.frame');f.style.width='1280px';f.style.height='720px';f.querySelector('.slide').style.transform='none';let body=a.querySelector('.body');if(body&&!a.querySelector(':scope>h2').textContent.startsWith('foundation /'))for(let e of body.children){e.style.gridColumn='1 / span '+size[0];e.style.gridRow='1 / span '+size[1]}}''',sizes[phase])
    if not tested:continue
    r=q.evaluate((BASE/'qa/contrast_engine.js').read_text());allr.append({'minimumIndex':phase,'testedFixtures':tested,**r})
   reports['dark' if dark else 'light']={'sourceSha256':hashlib.sha256(m.encode()).hexdigest(),'cases':allr,'candidates':[dict(x,minimumIndex=r['minimumIndex']) for r in allr for x in r['candidates']]}
  (BASE/'qa'/f'{k}-contrast-min-audit.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n');print(k,{mode:len(x['candidates']) for mode,x in reports.items()},flush=True)
 b.close()
