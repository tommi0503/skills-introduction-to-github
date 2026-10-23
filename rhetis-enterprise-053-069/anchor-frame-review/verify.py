from pathlib import Path
from PIL import Image
import json,hashlib,fitz
B=Path(__file__).parent;C=B.parent/'anchor-frame';ref=Path('/workspace/work/ref');files=list(C.rglob('*'));fixtures=list(C.glob('elements/*/fixtures/*.html'))
report={'collection':'anchor-frame','element_count':len(list((C/'elements').iterdir())),'fixture_count':len(fixtures),'file_kinds':sorted({p.suffix for p in files if p.is_file()}),'pngs':{},'pdfs':{},'source_sha256':{str(p.relative_to(C)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files if p.is_file()}}
for p in B.rglob('*.png'):
 if p.parent==B:continue
 report['pngs'][str(p.relative_to(B))]=list(Image.open(p).size)
for p in B.rglob('*.pdf'):
 with fitz.open(p) as d:report['pdfs'][str(p.relative_to(B))]={'pages':len(d),'first_page_size':[d[0].rect.width,d[0].rect.height]}
assert report['element_count']==56
assert report['file_kinds']==['.css','.html','.json','.md']
assert all(len(list((p/'fixtures').glob('*.html')))>=2 for p in (C/'elements').iterdir())
for kind in ['replica','reassembled']:
 assert report['pngs'][kind+'/slide_01.png']==[1280,720]
for mode in ['light','dark']:
 assert all((B/f'library/{p.name}/{mode}.png').is_file() for p in (C/'elements').iterdir())
(B/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print({k:v for k,v in report.items() if k not in ['pngs','pdfs','source_sha256']});print('PNGs',len(report['pngs']),'PDFs',report['pdfs'])
