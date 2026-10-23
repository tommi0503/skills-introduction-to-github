from pathlib import Path
from PIL import Image
import json,hashlib,collections,re
import fitz
B=Path(__file__).resolve().parents[1];spec=[('053','rise-block',2),('054','cinder-pulse',20),('055','current-fold',18),('056','scanline-rise',18),('058','halo-field',15),('067','corner-signal',21),('069','anchor-frame',1)];out={'collections':[],'total_original_pages':95,'errors':[]}
for no,cid,n in spec:
 C=B/cid;R=B/(cid+'-review');row={'deck':no,'collection':cid,'expected_pages':n,'elements':len(list((C/'elements').iterdir())),'fixtures':len(list((C/'elements').glob('*/fixtures/*.html'))),'png':{},'pdf':{},'source_sha256':{},'notes':str(R/'review-notes.md')}
 assert row['elements']==56
 for kind in ['replica','reassembled','compare-replica','compare-reassembled','library']:
  files=sorted((R/kind).rglob('*.png'));dims=collections.Counter()
  for f in files:
   im=Image.open(f);im.verify();dims['x'.join(map(str,Image.open(f).size))]+=1
  row['png'][kind]={'count':len(files),'dimensions':dict(dims)}
  expected='2560x720' if kind.startswith('compare') else '1280x720'
  if any(k!=expected for k in dims):out['errors'].append(cid+' '+kind+' incorrect dimension '+str(dict(dims)))
  if kind!='library' and len(files)!=n:out['errors'].append(cid+' '+kind+' wrong page count')
  if kind=='library' and len(files)!=114:out['errors'].append(cid+' library sheet count '+str(len(files)))
 for p in sorted(R.rglob('*.pdf')):
  d=fitz.open(p);row['pdf'][p.relative_to(R).as_posix()]={'pages':len(d),'sizes':sorted(set(tuple(round(x,2) for x in page.rect[2:]) for page in d))};d.close()
 for f in sorted(C.rglob('*')):
  if f.is_file():row['source_sha256'][f.relative_to(C).as_posix()]=hashlib.sha256(f.read_bytes()).hexdigest()
 if not (R/'review-notes.md').exists():out['errors'].append(cid+' missing notes')
 out['collections'].append(row)
out['total_elements']=sum(r['elements'] for r in out['collections']);out['total_png']=sum(s['count'] for r in out['collections'] for s in r['png'].values());out['total_pdf']=sum(len(r['pdf']) for r in out['collections']);out['formal_intake_executed']=False
(B/'final-verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print('elements',out['total_elements'],'png',out['total_png'],'pdf',out['total_pdf'],'errors',out['errors'])
