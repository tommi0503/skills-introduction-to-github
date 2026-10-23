"""Targeted semantic and graphic-only QA; reports candidates for visual review."""
import json,sys,re,importlib.util,hashlib,argparse
from playwright.sync_api import sync_playwright
from audit_css import BASE,REFERENCE,COLLECTIONS
s=importlib.util.spec_from_file_location('pv',REFERENCE/'tools/preview.py');pv=importlib.util.module_from_spec(s);s.loader.exec_module(pv)
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('collections',nargs='*',default=COLLECTIONS);parser.add_argument('--types');parser.add_argument('--all',action='store_true');parser.add_argument('--dark',action='store_true');args=parser.parse_args();selected_types=set(args.types.split(',')) if args.types else {'foundation','chart-stack','chart-donut','balance','bullet','funnel','pyramid','heatmap','waffle','concentric','chart-scatter','person','image-frame','quote','callout','network','positioning','card'}
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page(viewport={'width':1360,'height':900});q.goto('http://127.0.0.1:8765/qa/probe.html')
  for k in (args.collections or COLLECTIONS):
   if args.all:selected_types={'foundation'}|{d.name for d in (BASE/(k+'-project')/k/'elements').iterdir() if d.is_dir()}
   m=pv.sheet(BASE/(k+'-project')/k,json.loads((REFERENCE/'contract/type-steps.json').read_text()),json.loads((REFERENCE/'contract/palette.json').read_text()),dark=args.dark,fonts_href=f'/{k}-project/assets/fonts/fonts.css');q.set_content(m,wait_until='networkidle');q.evaluate('document.fonts.ready');checks=[]
   for a in q.locator('article').all():
    title=a.locator(':scope > h2').inner_text();typ=title.split(' / ')[0]
    if typ not in selected_types:continue
    mins=[tuple(map(int,x)) for x in re.findall(r'(\d+)x(\d+)',title.split('min',1)[-1])];sizes=list(dict.fromkeys(mins+[(12,6)]))
    for c,r in sizes:
     a.evaluate('''(a,size)=>{let f=a.querySelector('.frame');f.style.width='1280px';f.style.height='720px';f.querySelector('.slide').style.transform='none';let b=a.querySelector('.body');if(b&&!a.querySelector(':scope > h2').textContent.startsWith('foundation /'))for(const e of b.children){e.style.gridColumn='1 / span '+size[0];e.style.gridRow='1 / span '+size[1]}}''',[c,r])
     checks.append({'fixture':title,'size':[c,r],**a.evaluate((BASE/'qa/functional.js').read_text())})
   keys=['stack','donut','balance','bullet','seats','graphics','polygonText'];counts={key:sum(len(x[key]) for x in checks) for key in keys};result={'collection':k,'sourceSha256':hashlib.sha256(m.encode()).hexdigest(),'counts':counts,'testedTypes':sorted(selected_types),'checks':checks,'limitations':'Graphic and polygon boxes are candidates; rotated graphic bounding rectangles can overestimate actual paint. Caption-border target cue requires manual review.'};(BASE/'qa'/(k+'-functional-'+('dark-' if args.dark else '')+('all-audit' if args.all else args.types.replace(',','-') if args.types else 'audit')+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(k,counts,flush=True)
  b.close()
