from pathlib import Path
from PIL import Image
import json,hashlib,zipfile,fitz,shutil
C=Path('/workspace/output/cyanloop');R=Path('/workspace/output/cyanloop-review');W=Path('/workspace/work/cyanloop');I=Path('/workspace/work/integration')
# Keep the exact audit results with the portable review.
for src,dst in [('cyanloop-browser-audit.json','grid-audit.json'),('cyanloop-contrast-audit.json','contrast-audit.json'),('cyanloop-chip-audit.json','chip-audit.json')]:
 p=I/src
 if p.exists():shutil.copyfile(p,R/'library'/dst)
ns={};exec((I/'strict_fixture_audit.py').read_text().split('\nreports=')[0],ns);strict=ns['audit']('cyanloop');assert not strict['errors'],strict['errors'];(R/'library/strict-fixture-audit.json').write_text(json.dumps(strict,ensure_ascii=False,indent=2))
grid=json.loads((R/'library/grid-audit.json').read_text());assert grid['issues_count']==0,grid['issues'][:3];assert grid['fonts']==[],grid['fonts'];assert grid['resources']==[],grid['resources']
for rel,sha in grid['source_sha256'].items():assert hashlib.sha256((C/rel).read_bytes()).hexdigest()==sha,rel
browser=json.loads((R/'library/browser-checks.json').read_text());assert all(not r['issues'] for r in browser)
pageaudit=json.loads((R/'reassembled/page-audit.json').read_text());assert all(not r['bad'] and not r['fonts'] and r['size']==[1280,720] for r in pageaudit);contrast=json.loads((R/'library/contrast-audit.json').read_text());assert not contrast;chips=json.loads((R/'library/chip-audit.json').read_text());assert not chips['alignment_candidates'];functional=json.loads((R/'library/functional-audit.json').read_text());assert not functional['errors']
pngs={};counts={};sizes={}
for group in ['replica','compare-replica','library','reassembled','compare-reassembled']:
 paths=sorted((R/group).rglob('*.png'));counts[group]=len(paths);sizes[group]=sorted(set(Image.open(p).size for p in paths))
 for p in paths:
  im=Image.open(p);im.verify();size=Image.open(p).size
  if group in ['replica','reassembled']:assert size==(1280,720),(p,size)
  elif group.startswith('compare'):assert size==(2560,720),(p,size)
  else:assert size[0]==1280 and size[1]%388==0,(p,size)
assert all(counts[g]==18 for g in ['replica','compare-replica','reassembled','compare-reassembled']),counts
assert counts['library']==114,counts
pdfs={}
for p in sorted(R.rglob('*.pdf')):
 d=fitz.open(p);pdfs[str(p.relative_to(R))]={'pages':len(d),'bytes':p.stat().st_size};d.close();assert p.stat().st_size<100*1024*1024
assert pdfs['library/library-light.pdf']['pages']==218
assert pdfs['library/library-dark.pdf']['pages']==218
for p in C.rglob('*'):
 if p.is_file():assert p.suffix in ['.css','.json','.md','.html'],p
report={'collection':'cyanloop','original_images':18,'elements':56,'element_fixtures':212,'foundation_fixtures':6,'canonical_fixtures':28,'png_count':sum(counts.values()),'png_counts':counts,'png_sizes':sizes,'pdfs':pdfs,'browser_states':grid['tested_states'],'geometry_issues':grid['issues_count'],'font_errors':grid['fonts'],'failed_resources':grid['resources'],'rendered_screens':len(browser),'render_issues':sum(len(r['issues']) for r in browser),'source_hashes_match_grid_audit':True,'strict_fixture_errors':len(strict['errors']),'contrast_fixture_concerns':len(contrast),'chip_centers_checked':chips['checked'],'chip_alignment_candidates':len(chips['alignment_candidates']),'functional_states':len(functional['checks']),'functional_errors':len(functional['errors']),'portable_local_resources':True,'build_commands':['python tools/preview.py cyanloop contract/type-steps.json --out light.html','python tools/preview.py cyanloop contract/type-steps.json --dark --out dark.html']}
(R/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
archives=[]
for root in [C,R]:
 dest=root.with_suffix('.zip')
 with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in sorted(root.rglob('*')):
   if p.is_file():z.write(p,p.relative_to(root.parent))
 with zipfile.ZipFile(dest) as z:
  assert z.testzip() is None
  tops={p.split('/')[0] for p in z.namelist()};assert tops=={root.name},tops
  archives.append({'file':dest.name,'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'crc_integrity':True,'entries':len(z.namelist()),'top_level':[root.name]})
(W/'package-verification.json').write_text(json.dumps(archives,ensure_ascii=False,indent=2));print(json.dumps({'verification':report,'archives':archives},ensure_ascii=False,indent=2))
