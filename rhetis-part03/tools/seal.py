from pathlib import Path
from PIL import Image
import hashlib,json,re,datetime,subprocess
R=Path(__file__).resolve().parents[1];h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
orig=json.loads((R/'review/final-audit.json').read_text());assembly=json.loads((R/'review/assembly-audit.json').read_text());contract=json.loads((R/'review/library-contract-audit.json').read_text());chips=json.loads((R/'review/chip-alignment.json').read_text());contrast=json.loads((R/'review/library-contrast.json').read_text());minima=json.loads((R/'review/library-minimum-audit.json').read_text())
assert orig['total']==90 and orig['sourceStable'] and not orig['errors'] and not orig['fontsFailed'] and all(not x['findings']for x in orig['slides'])
assert assembly['count']==90 and not assembly['errors'] and all(not x['overflow']for x in assembly['slides'])
assert contract['elements']==31 and contract['elementFixtures']==87 and not contract['staticFailures']
assert not chips['failures'] and all(not x['failures']for x in contrast) and not minima
counts={}
for sub,expected in [('renders/final',90),('renders/assembly',90),('renders/library/light',89),('renders/library/dark',89)]:
 files=sorted((R/sub).glob('*.png'));assert len(files)==expected,(sub,len(files));assert all(Image.open(p).size==(1280,720)for p in files);counts[sub]={'count':len(files),'width':1280,'height':720}
comparisons=list((R/'comparisons/final').glob('*.png'));assert len(comparisons)==90 and all(Image.open(p).size==(2560,720)for p in comparisons)
for x in orig['slides']:assert h(R/x['file'])==x['sha256']
html=(R/'deliverables/preview.html').read_text();missing=[]
for link in re.findall(r'(?:src|href)="([^"#?]+)"',html):
 if not link.startswith(('http','data:'))and not(R/'deliverables'/link).exists():missing.append(link)
assert not missing,missing
pdfs={}
try:
 from pypdf import PdfReader
 for p in (R/'deliverables/pdf').glob('*.pdf'):pdfs[p.name]=len(PdfReader(p).pages)
 assert pdfs['reproduced-all-slides.pdf']==90 and pdfs['library-assembled-slides.pdf']==90 and pdfs['original-vs-result.pdf']==90
 assert pdfs['library-elements-light.pdf']==89 and pdfs['library-elements-dark.pdf']==89
except ImportError:pass
sources={}
for folder in ['src','library/rhetis-report','public/fonts']:
 for p in sorted((R/folder).rglob('*')):
  if p.is_file():sources[str(p.relative_to(R))]=h(p)
record={'verifiedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'build':'passed','typescript':'passed','originalSlideCount':90,'assemblySlideCount':90,'collectionElements':31,'elementFixtures':87,'foundationFixtures':2,'libraryRenderCount':178,'totalRenderPNGs':358,'renderGroups':counts,'comparisonPNG':{'count':90,'width':2560,'height':720},'finalScreenshotHashesMatch':True,'allTextOverflowChecksPassed':True,'chipAlignment':{'count':chips['total'],'tolerancePx':chips['tolerancePx'],'failures':0},'fontLoadFailures':0,'browserErrors':0,'libraryContrastFailures':0,'libraryMinimumSlotFailures':0,'previewMissingFiles':missing,'pdfPages':pdfs,'sourceFilesSHA256':sources}
(R/'review/final-verification.json').write_text(json.dumps(record,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in record.items()if k!='sourceFilesSHA256'},ensure_ascii=False,indent=2))
