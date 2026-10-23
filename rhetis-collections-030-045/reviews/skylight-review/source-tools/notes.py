from pathlib import Path
import json,collections,hashlib,re
from PIL import Image
import fitz
C=Path('/workspace/work/deliverables/skylight');R=Path('/workspace/work/deliverables/skylight-review')
# The parent will add repository commit/download verification after packaging.
refs={'card':('confetti',['card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone']),'callout':('annual',['callout','callout-icon','callout-stack']),'chart-area':('annual',['area-1','areas-2','areas-stacked-3','area-3pt']),'chart-bar':('confetti',['bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2']),'chart-donut':('amethyst',['donut','donuts-3','donuts-4','donut-0','donut-100']),'chart-line':('amethyst',['lines-12','lines-6','lines-3','lines-flat'])}
mandatory=[]
for f,(orig,fs) in refs.items():
 for n in fs:
  origtext=Path('/workspace/work/reference/samples',orig,'elements',f,'fixtures',n+'.html').read_text().replace(orig+'-','skylight-');now=(C/'elements'/f/'fixtures'/(n+'.html')).read_text();mandatory.append({'fixture':f+'/'+n,'equal':origtext==now})
report={'collection':'skylight','originalDeck':'038_1jp12','originalImageCount':21,'replicaPages':21,'reassembledPages':21,'elementCount':len(list((C/'elements').iterdir())),'elementFixtures':len(list(C.glob('elements/*/fixtures/*.html'))),'foundationFixtures':len(list(C.glob('foundation/fixtures/*.html'))),'mandatoryFixtureIdentity':mandatory,'allowedSourceExtensions':sorted(set(p.suffix for p in C.rglob('*') if p.is_file())),'pngDimensions':dict(collections.Counter(f'{Image.open(p).width}x{Image.open(p).height}' for p in R.rglob('*.png'))),'pdfPages':{p.relative_to(R).as_posix():len(fitz.open(p)) for p in R.rglob('*.pdf')},'pageBrowserChecks':json.load(open('/workspace/work/agents/038/page-final-checks.json')),'chipAlignmentChecks':json.load(open('/workspace/work/agents/038/chip-checks.json')),'elementGridStress':json.load(open('/workspace/work/agents/038/stress-library.json')),'sourceCSSAudit':json.load(open('/workspace/work/agents/038/css-audit.json')),'libraryBrowserChecks':{'slideModes':len(json.load(open('/workspace/work/agents/038/library-checks.json'))),'fontLoadingPassed':all(x['full']['font'] for x in json.load(open('/workspace/work/agents/038/library-checks.json'))),'overflow':sum(len(x['full']['overflow']) for x in json.load(open('/workspace/work/agents/038/library-checks.json')))},'pngSHA256':{p.relative_to(R).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in R.rglob('*.png')}}
(R/'automatic-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print('notes and checks saved',len(report['pngSHA256']),'PNGs')
