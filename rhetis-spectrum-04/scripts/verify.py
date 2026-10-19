from pathlib import Path
from PIL import Image
from pypdf import PdfReader
import json,re,hashlib
root=Path(__file__).resolve().parent.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def check(label,ok,details=None):
 checks.append({'check':label,'ok':bool(ok),'details':details})
 if not ok:raise AssertionError((label,details))
manifest=json.loads((root/'review/manifest.json').read_text());check('7 decks and 82 supplied slides',len(manifest)==7 and sum(x['count'] for x in manifest)==82)
lib=root/'collections/spectrum-04';taxonomy=json.loads((root/'contract/taxonomy.json').read_text());contracts={c['id'] for c in taxonomy['contracts']};actual=[]
for folder in sorted((lib/'elements').iterdir()):
 j=json.loads((folder/'element.json').read_text());actual.append(j['contract']);fixtures=list((folder/'fixtures').glob('*.html'))
 check(folder.name+' at least two fixtures',len(fixtures)>=2)
 check(folder.name+' fixture minimum declarations',all(f.read_text().startswith('<!-- min:') for f in fixtures))
 css=(folder/'element.css').read_text();check(folder.name+' no external resources',not re.search(r'@(?:import|font-face|keyframes)|url\(',css))
 sizes=re.findall(r'font-size\s*:\s*([^;}]+)',css);steps=json.loads((root/'contract/type-steps.json').read_text())
 check(folder.name+' discrete type steps',all(re.fullmatch(r'var\(--type-(\d+)\)',v.strip()) and int(re.fullmatch(r'var\(--type-(\d+)\)',v.strip())[1]) in steps for v in sizes),sizes)
 check(folder.name+' no hardcoded colors',not re.search(r'#[0-9a-fA-F]{3,8}\b|\brgba?\(',css))
 check(folder.name+' responsive rules','@container' in css)
check('31 correct element contracts',set(actual)==contracts and len(actual)==31)
kit=(lib/'kit/css/tokens.css').read_text();required=json.loads((root/'contract/kit-tokens.json').read_text())['tokens'];light,dark=kit.split('.slide.dark',1)
check('all shared tokens',all(k+':' in light for k in required))
check('all shared dark colors',all(k+':' in dark for k,t in required.items() if t=='color'))
check('image-free collection',not any(f.suffix.lower() in ['.png','.jpg','.svg','.jpeg','.webp','.woff','.woff2'] for f in lib.rglob('*')))
for mode in ['direct','assembled']:
 files=sorted((root/'renders'/mode/'final').glob('*.png'));check(mode+' 82 PNGs',len(files)==82)
 for d in manifest:
  audit=json.loads((root/'review'/mode/'final'/(d['id']+'.json')).read_text())
  check(mode+' '+d['id']+' no browser errors',not audit['errors'])
  for s in audit['slides']:
   check(mode+' '+d['id']+'/'+s['id']+' final render audit',not s['findings'] and s['imageCount']==0 and s['width']==1280 and s['height']==720,s['findings'])
   check(mode+' '+d['id']+'/'+s['id']+' final PNG hash',s['sha256']==sha(root/'renders'/mode/'final'/(d['id']+'-'+s['id']+'.png')))
library=json.loads((root/'review/library/audit.json').read_text());check('library full and minimum sizes in both modes',len(library)>=350 and all(not x['findings'] for x in library),{'states':len(library),'findings':sum(len(x['findings']) for x in library)})
pngs=list((root/'renders').glob('*/final/*.png'))+list((root/'renders/library').rglob('*.png'))+list((root/'sheets').rglob('*.png'));check('every final PNG is 1280x720',all(Image.open(f).size==(1280,720) for f in pngs),len(pngs))
differences=[]
for a in sorted((root/'renders/direct/final').glob('*.png')):
 b=root/'renders/assembled/final'/a.name
 if sha(a)!=sha(b):differences.append(a.name)
check('reassembled slides match direct renders pixel-for-pixel',not differences,differences)
for name,count in [('direct-slides',82),('assembled-slides',82),('direct-contact-sheets',21),('assembled-contact-sheets',21),('library-light',89),('library-dark',89)]:
 pdf=PdfReader(root/'pdf'/(name+'.pdf'));check(name+' PDF pages',len(pdf.pages)==count,len(pdf.pages));check(name+' all PDF pages have 16:9 canvas',all(abs(float(p.mediabox.width)-960)<1 and abs(float(p.mediabox.height)-540)<1 for p in pdf.pages))
fonts=root/'public/fonts/fonts.css';refs=re.findall(r'url\(([^)]+)\)',fonts.read_text());check('all font resources available',all((fonts.parent/r.strip("'\"")).exists() for r in refs),len(refs))
check('all 82 final comparisons',len(list((root/'comparisons/direct/final').glob('*.jpg')))==82)
report={'passed':True,'checks':len(checks),'decks':7,'slides':82,'elements':31,'fixtures':len(list(lib.rglob('fixtures/*.html'))),'libraryStates':len(library),'finalPngs':len(pngs),'checksDetail':checks}
(root/'review/verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='checksDetail'},ensure_ascii=False))
