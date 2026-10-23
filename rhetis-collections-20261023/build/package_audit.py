from pathlib import Path
from PIL import Image
import json,hashlib,zipfile,re,sys
import fitz
BASE=Path('/workspace/output')
NAMES={'fluxweave':18,'cyanloop':18,'roundrise':24,'nightchamfer':18,'glasspulse':18}
results=[]
for name,expected in NAMES.items():
 if len(sys.argv)>1 and name not in sys.argv[1:]:continue
 root=BASE/(name+'-review'); d={'collection':name,'original_pages':expected,'errors':[],'pngs':[],'pdfs':[],'zips':[],'nonportable_refs':[]}
 for p in root.rglob('*.png'):
  im=Image.open(p);im.verify()
  with Image.open(p) as im:size=list(im.size)
  d['pngs'].append({'path':str(p.relative_to(root)),'size':size})
 for folder in ['replica','reassembled']:
  ps=[p for p in d['pngs'] if p['path'].startswith(folder+'/') and re.search(r'slide[-_]?\d+\.png$',p['path'])]
  if len(ps)!=expected:d['errors'].append(f'{folder}: expected {expected} page PNG, got {len(ps)}')
  for p in ps:
   if p['size']!=[1280,720]:d['errors'].append(p['path']+' not 1280x720')
 for folder in ['compare-replica','compare-reassembled']:
  ps=[p for p in d['pngs'] if p['path'].startswith(folder+'/')]
  if len(ps)!=expected:d['errors'].append(f'{folder}: expected {expected} comparison PNG, got {len(ps)}')
 library=[p for p in d['pngs'] if p['path'].startswith('library/')]
 d['library_png_count']=len(library)
 if len(library)<112:d['errors'].append('Expected >=112 element library PNGs')
 for element in sorted((BASE/name/'elements').iterdir()):
  if not element.is_dir():continue
  for mode in ['light','dark']:
   expected_png=root/'library'/element.name/(mode+'.png')
   if not expected_png.is_file() and not (root/'library'/'elements'/element.name/(mode+'.png')).is_file():d['errors'].append('Missing element sheet '+str(expected_png.relative_to(root)))
 for required in ['library/light.html','library/dark.html','design-language.md','review-notes.md']:
  if not (root/required).is_file():d['errors'].append('Missing '+required)
 for p in root.rglob('*.pdf'):
  doc=fitz.open(p);d['pdfs'].append({'path':str(p.relative_to(root)),'pages':len(doc)});doc.close()
 for folder in ['replica','reassembled']:
  pdfs=[p for p in d['pdfs'] if p['path']==folder+'/'+folder+'.pdf']
  if not pdfs or pdfs[0]['pages']!=expected:d['errors'].append(folder+' PDF count mismatch')
 for mode in ['light','dark']:
  if not any(Path(p['path']).name=='library-'+mode+'.pdf' for p in d['pdfs']):d['errors'].append('Missing library-'+mode+'.pdf')
 for p in root.rglob('*.html'):
  s=p.read_text()
  refs=re.findall(r'(?:src|href)=["\']([^"\']+)',s)+re.findall(r'url\(["\']?([^\)"\']+)',s)
  for ref in refs:
   if ref.startswith(('file:','/workspace','http://127.0.0.1','http://localhost')):d['nonportable_refs'].append({'file':str(p.relative_to(root)),'ref':ref})
 if d['nonportable_refs']:d['errors'].append('Nonportable review HTML references')
 for suffix in ['','.zip-review']:
  zpath=BASE/(name+('' if not suffix else '-review')+'.zip')
  if not zpath.exists():d['errors'].append('Missing '+zpath.name);continue
  with zipfile.ZipFile(zpath) as z:
   bad=z.testzip();names=z.namelist()
   source_root=BASE/(name+('' if not suffix else '-review'))
   expected_members={str(p.relative_to(BASE)) for p in source_root.rglob('*') if p.is_file()}
   actual_members={n for n in names if not n.endswith('/')}
   for missing in sorted(expected_members-actual_members):d['errors'].append('ZIP missing source file '+missing)
   for extra in sorted(actual_members-expected_members):d['errors'].append('ZIP obsolete or unexpected file '+extra)
   if bad:d['errors'].append('Corrupt member '+bad)
   for member in names:
    if member.endswith('/'):continue
    candidate=BASE/member
    if candidate.is_file() and hashlib.sha256(z.read(member)).digest()!=hashlib.sha256(candidate.read_bytes()).digest():d['errors'].append('Stale ZIP member '+member)
   if not suffix:
    if any(not n.startswith(name+'/') for n in names):d['errors'].append('Collection ZIP top folder mismatch')
    if any(Path(n).suffix not in {'.css','.json','.md','.html'} for n in names if not n.endswith('/')):d['errors'].append('Collection ZIP file type mismatch')
  d['zips'].append({'file':zpath.name,'size_bytes':zpath.stat().st_size,'sha256':hashlib.sha256(zpath.read_bytes()).hexdigest(),'members':len(names),'testzip':bad})
 print(name,len(d['pngs']),'png',len(library),'library',d['errors'])
 results.append(d)
Path('/workspace/work/integration/artifact-audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
