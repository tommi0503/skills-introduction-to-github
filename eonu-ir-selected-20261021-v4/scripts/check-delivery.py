from pathlib import Path
import json, hashlib, re
ROOT=Path(__file__).resolve().parent.parent
checks=[]
def check(name,ok):
 checks.append({'name':name,'passed':bool(ok)})
 if not ok:print('FAIL',name)
hashes=json.loads((ROOT/'review/render-sources.json').read_text())
for name,expected in hashes.items():check('Rendered source unchanged: '+name,hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==expected)
for c in ['final']:
 report=json.loads((ROOT/f'review/{c}-render.json').read_text())
 check(c+' source checks',not report['errors'])
 check(c+' 24 slide renders',len(report['pages'])==24)
 for p in report['pages']:
  label=f"{c}/{p['mode']}/{p['page']}"
  check(label+' bounds/font/placeholder checks',not p['issues'])
  check(label+' text overlap check',not p['possibleTextOverlaps'])
  img=ROOT/f"concepts/{c}/previews/{p['mode']}/{p['page']}.png"
  check(label+' screenshot matches render',hashlib.sha256(img.read_bytes()).hexdigest()==p['sha256'])
 for i in range(1,13):
  a=next(p for p in report['pages'] if p['page']==f'{i:02}' and p['mode']=='design')
  b=next(p for p in report['pages'] if p['page']==f'{i:02}' and p['mode']=='wireframe')
  check(f'{c}/{i:02} wireframe geometry',a['section']==b['section'] and a['heading']==b['heading'] and a['placeholders']==b['placeholders'])
for p in list(ROOT.rglob('*.html'))+list(ROOT.rglob('*.css')):
 txt=p.read_text();rel=str(p.relative_to(ROOT))
 odd=[n for n in re.findall(r'(-?\d*\.?\d+)px\b',txt) if float(n)%2]
 check('2px fixed scale: '+rel,not odd)
 if p.suffix=='.html':
  for attr in re.findall(r'(?:src|href)=["\']([^"\']+)["\']',txt):
   if attr.startswith(('#','data:','http:','https:','mailto:')):continue
   target=(p.parent/attr.split('#')[0].split('?')[0])
   check('Local link '+rel+' → '+attr,target.exists())
viewer=json.loads((ROOT/'review/viewer-checks.json').read_text())
check('Viewer functional checks passed',viewer['status']=='passed')
pdfs=json.loads((ROOT/'review/pdf-checks.json').read_text())
check('Two vector text PDFs checked',len(pdfs)==2 and all(x['pages']==12 and x['textExtractable'] for x in pdfs))
selection=json.loads((ROOT/'review/selection-checks.json').read_text())
check('User selection mapped exactly with full talks and notes',selection['status']=='passed')
fail=[c for c in checks if not c['passed']]
out={'status':'passed' if not fail else 'failed','checks':len(checks),'failures':fail,'canvas':[1280,720],'concepts':1,'designSlides':12,'wireframeSlides':12,'results':checks}
(ROOT/'review/final-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(out['status'],len(checks),'checks;',len(fail),'failures')
raise SystemExit(bool(fail))
