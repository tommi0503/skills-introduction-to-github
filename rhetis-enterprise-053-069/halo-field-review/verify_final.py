from pathlib import Path
from PIL import Image
import json,collections,hashlib,fitz
R=Path(__file__).parent;C=R.parent/'halo-field'
files=list(R.rglob('*.png'));sizes=collections.Counter(Image.open(p).size for p in files)
a=json.load(open(R/'browser-audit.json'));m=json.load(open(R/'minimum-audit.json'))
summary={'collection':'halo-field','source_images':15,'replica_pages':len(list((R/'replica').glob('slide*.png'))),'reassembled_pages':len(list((R/'reassembled').glob('slide*.png'))),'png_count':len(files),'png_sizes':{str(k):v for k,v in sizes.items()},'elements':len(list((C/'elements').iterdir())),'element_sheet_light':len(list((R/'library').glob('*/light.png'))),'element_sheet_dark':len(list((R/'library').glob('*/dark.png'))),'font_failures':sum(x.get('font') is False for x in a),'reassembled_overflow':sum(bool(x.get('overflow')) for x in a),'minimum_tests':len(m),'minimum_overflow':sum(bool(x['bad']) for x in m),'collection_extensions':sorted(set(p.suffix for p in C.rglob('*') if p.is_file())),'source_css_sha256':hashlib.sha256(''.join(p.read_text() for p in sorted(C.rglob('*.css'))).encode()).hexdigest(),'pdf_pages':{str(p.relative_to(R)):fitz.open(p).page_count for p in R.rglob('*.pdf')}}
assert summary['replica_pages']==summary['reassembled_pages']==15
assert summary['elements']==56
assert summary['element_sheet_light']==summary['element_sheet_dark']==57
assert summary['font_failures']==summary['reassembled_overflow']==summary['minimum_overflow']==0
assert set(sizes)=={(1280,720),(2560,720)}
assert summary['collection_extensions']==['.css','.html','.json','.md']
(R/'verification.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
