from pathlib import Path
from PIL import Image
import json,hashlib,zipfile,fitz
build=json.loads(Path('dist/build-state.json').read_text());state=build['source']['hash'];issues=[];counts={};fonts=0;chips=0
for mode in ['clone','assembly']:
 ps=list(Path(f'renders/final/{mode}').glob('*.png'));counts[mode]=len(ps)
 if len(ps)!=76:issues.append(f'{mode}: PNG count {len(ps)}')
 reports=sorted(Path('review/captures').glob(f'*-final-{mode}.json'))
 if len(reports)!=6:issues.append(f'{mode}: missing deck reports')
 audited=0
 for p in reports:
  r=json.loads(p.read_text());audited+=len(r['slides'])
  if not r.get('production'):issues.append(f'{p}: not production')
  if r.get('sourceHash')!=state:issues.append(f'{p}: stale hash')
  if r['errors']:issues.append(f'{p}: browser errors {r["errors"]}')
  for s in r['slides']:
   if s['findings']:issues.append(f'{p}/{s["id"]}: {s["findings"]}')
   if s['canvas']!=[1280,720]:issues.append(f'{p}/{s["id"]}: canvas size')
   if s['fontStatus']!='loaded' or not all(f['available'] for f in s['fonts']):issues.append(f'{p}/{s["id"]}: font')
   if s['embeddedRaster']:issues.append(f'{p}/{s["id"]}: raster')
   if not s['placeholdersValid']:issues.append(f'{p}/{s["id"]}: placeholder')
   fonts+=len(s['fonts']);chips+=len(s['chips'])
 if audited!=76:issues.append(f'{mode}: audited {audited}')
 for p in ps:
  with Image.open(p) as im:
   if im.size!=(1280,720):issues.append(f'{p}: wrong dimensions {im.size}')
for mode in ['light','dark']:
 ps=list(Path(f'renders/library/{mode}').glob('*.png'));counts['library-'+mode]=len(ps)
 if len(ps)!=89:issues.append(f'library-{mode}: {len(ps)}')
 for p in ps:
  if Image.open(p).size!=(1280,720):issues.append(f'{p}: dimensions')
lib=json.loads(Path('review/library-captures.json').read_text())
for r in lib:
 if r['issues']:issues.append(f'library {r["mode"]}/{r["label"]}: {r["issues"]}')
minimum=json.loads(Path('review/library-min-check.json').read_text())
if minimum['status']!='passed':issues.append('library minimum audit failed')
for mode in ['light','dark']:
 current=hashlib.sha256(Path(mode+'.html').read_bytes()).hexdigest()
 if minimum['sheets'][mode]!=current:issues.append('stale minimum sheet '+mode)
comparisons=list(Path('comparisons/final').glob('*.jpg'));counts['comparisons']=len(comparisons)
if len(comparisons)!=76:issues.append('comparison count')
contract=json.loads(Path('review/contract-check.json').read_text())
if contract['status']!='passed' or contract['elements']!=31:issues.append('contract check')
report={'status':'passed' if not issues else 'failed','sourceHash':state,'counts':counts,'renderPngTotal':sum(v for k,v in counts.items() if k!='comparisons'),'canvas':[1280,720],'fontChecks':fonts,'chipChecks':chips,'librarySizeCombinations':minimum['summary']['cases'],'issues':issues}
Path('review/final-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2));assert not issues
