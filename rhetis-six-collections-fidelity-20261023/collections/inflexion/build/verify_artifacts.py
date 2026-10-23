from pathlib import Path
from collections import Counter
from PIL import Image
from pypdf import PdfReader
import json,hashlib,re
root=Path(__file__).resolve().parents[1];review=root/'review';collection=root/'collection/inflexion'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'collection':'inflexion','source_slides':20,'elements':len(list((collection/'elements').iterdir())),'element_fixtures':len(list((collection/'elements').glob('*/fixtures/*.html')))}
assert report['elements']==56 and report['element_fixtures']==172
assert all(p.suffix in {'.css','.json','.md','.html'} for p in collection.rglob('*') if p.is_file())
report['png']=[]
for p in sorted(review.rglob('*.png')):
 with Image.open(p) as im:
  im.verify()
 with Image.open(p) as im: size=list(im.size)
 if p.parent.name in {'replica','reassembled'}: assert size==[1280,720],(p,size)
 elif p.parent.name in {'compare-replica','compare-reassembled'}: assert size==[2560,720],(p,size)
 else: assert size[0]==1328,(p,size)
 report['png'].append({'file':str(p.relative_to(review)),'size':size,'sha256':sha(p)})
assert len(report['png'])==194,len(report['png'])
report['png_dimension_counts']={str(k):v for k,v in Counter(tuple(v['size']) for v in report['png']).items()}
report['pdf']=[]
for f,n in [('replica/replica.pdf',20),('reassembled/reassembled.pdf',20),('library/library-light.pdf',174),('library/library-dark.pdf',174)]:
 p=review/f;r=PdfReader(p);assert len(r.pages)==n,(f,len(r.pages));report['pdf'].append({'file':f,'pages':len(r.pages),'sha256':sha(p)})
report['audits']={}
for f,n in [('audit-library.json',700),('audit-replica.json',20),('audit-reassembled.json',20)]:
 d=json.loads((review/f).read_text());assert len(d)==n,(f,len(d));counts={k:sum(len(x.get(k,[])) for x in d) for k in ['clipped','overflow','contrast','zeroElementRoots','hiddenEssential','failedFonts','iconErrors','errors']};report['audits'][f]={'probes':len(d),**counts,'sha256':sha(review/f)}
 for k in ['zeroElementRoots','hiddenEssential','failedFonts','iconErrors','errors']:assert counts[k]==0,(f,k,counts[k])
 if f=='audit-library.json':
  assert counts['clipped']==0
  assert all(x.get('folder')=='chart-donut' for x in d if x.get('contrast')), 'Unexpected contrast outside separately checked pie pseudo-background'
 else:
  assert counts['clipped']==6,(f,counts['clipped'])
  assert all(x['file']=='slide_06.html' for x in d if x['clipped'])
  report['audits'][f]['intentional_source_crop']='P06: 500/50/17 and trillion units intentionally meet the image bottom, as in original.'
  report['audits'][f]['source_color_contrast_flags']=counts['contrast']
 if f!='audit-library.json':
  directory='replica' if f=='audit-replica.json' else 'reassembled'
  for row in d:assert row['sha256']==sha(review/directory/row['file']),row['file']
report['identical_css_mirrors']=[]
for p in collection.rglob('*.css'):
 mirror=review/'assets/collection'/p.relative_to(collection);assert p.read_bytes()==mirror.read_bytes(),p
 report['identical_css_mirrors'].append(str(p.relative_to(collection)))
assert len(report['identical_css_mirrors'])==58
# Every local HTML link is resolved in the standalone review tree.
report['local_html_links_checked']=0
for p in review.rglob('*.html'):
 for url in re.findall(r'(?:href|src)=["\']([^"\']+)',p.read_text()):
  if url.startswith(('https:','http:','data:','#')):continue
  assert (p.parent/url.split('#')[0]).exists(),(p,url)
  report['local_html_links_checked']+=1
(review/'artifact-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ['png','identical_css_mirrors']},ensure_ascii=False))
