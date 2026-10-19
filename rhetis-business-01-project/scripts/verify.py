from pathlib import Path
from PIL import Image
from pypdf import PdfReader
import json,hashlib,sys,zipfile
P=Path(__file__).resolve().parents[1];checks=[];errors=[]
def check(condition,label):
 checks.append({'check':label,'pass':bool(condition)})
 if not condition:errors.append(label)
manifest=json.loads((P/'public/reference/manifest.json').read_text());expected=sum(len(d['slides']) for d in manifest)
for mode in ['clone','assembled']:
 report=json.loads((P/f'review/final/{mode}-all.json').read_text());check(not report['errors'],mode+' browser console/network')
 files=sorted((P/f'renders/final/{mode}').glob('*.png'));check(len(files)==expected,mode+' PNG count = '+str(expected))
 for s in report['slides']:
  p=P/s['file'];check(Image.open(p).size==(1280,720),mode+' dimensions '+p.stem);check(hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256'],mode+' final render hash '+p.stem);check(not s['issues'],mode+' text/font/chip bounds '+p.stem)
  check(all(f['loaded'] for f in s['fontChecks']),mode+' fonts '+p.stem)
 pdf=P/f'deliverables/{mode}-slides.pdf';reader=PdfReader(pdf);check(len(reader.pages)==expected,mode+' PDF page count')
 for i,p in enumerate(reader.pages):check(abs(float(p.mediabox.width)-960)<.1 and abs(float(p.mediabox.height)-540)<.1,mode+f' PDF 1280x720px page {i+1}')
check(len(list((P/'comparisons/final').glob('*.jpg')))==expected,'105 individual comparisons')
for d in manifest:
 for s in d['slides']:check(hashlib.sha256((P/'public/reference'/s['file']).read_bytes()).hexdigest()==s['sha256'],'reference provenance '+s['file'])
collection=json.loads((P/'review/collection-contract.json').read_text());check(collection['passed'],'collection contract validator')
primary=json.loads((P/'review/main-review.json').read_text());check(len(primary['slides'])==expected,'primary visual review 105 individual slides')
for name,digest in json.loads((P/'review/final-source-hashes.json').read_text()).items():check(hashlib.sha256((P/name).read_bytes()).hexdigest()==digest,'final source snapshot '+name)
fixtures=sorted((P/'review/collection').glob('*.png'));check(len(fixtures)==158,'158 library PNG')
for p in fixtures:check(Image.open(p).size==(1280,720),'library PNG dimensions '+p.stem)
slots=json.loads((P/'review/collection-render.json').read_text());check(len(slots)==316 and all(not s['issues'] and s['fontLoaded'] for s in slots),'316 library full/min light/dark checks')
for mode in ['light','dark']:
 reader=PdfReader(P/f'deliverables/pdf/library-{mode}.pdf');check(len(reader.pages)==79,mode+' library PDF 79 pages')
 for p in reader.pages:check(abs(float(p.mediabox.width)-960)<.1 and abs(float(p.mediabox.height)-540)<.1,mode+' library PDF page size')
for p in (P/'deliverables').glob('*.zip'):
 with zipfile.ZipFile(p) as z:
  check(z.testzip() is None,'ZIP integrity '+p.name)
  if p.name=='rhetis-business-01.zip':check(set(n.split('/')[0] for n in z.namelist())=={'rhetis-business-01'},'collection ZIP single root')
result={'success':not errors,'imageCountPerMode':expected,'libraryPngCount':158,'totalPngCount':368,'allPngSize':[1280,720],'checks':len(checks),'errors':errors,'details':checks}
(P/'review/verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='details'},ensure_ascii=False,indent=2));sys.exit(bool(errors))
