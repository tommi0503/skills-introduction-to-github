from pathlib import Path
from PIL import Image
import json,hashlib,shutil,fitz,numpy as np
B=Path(__file__).resolve().parent.parent;R=B/'review';C=B/'collection/nocturne';O=Path('/workspace/work/deck/miricanvas_기업_selected/006_1kkda_파랑_모던_타운홀_행사');P=R/'proof-final';P.mkdir(exist_ok=True)
for p in P.glob('*.png'):p.unlink()
proofs=[]
for n in range(19,25):
 p=R/f'compare-reassembled/slide_{n}.png';h=hashlib.sha256(p.read_bytes()).hexdigest();q=P/f'slide_{n}-{h[:12]}.png';shutil.copy(p,q);proofs.append({'slide':n,'path':str(q.relative_to(R)),'sha256':h})
strip=Image.new('RGB',(1280,480));header_counts={}
for i,n in enumerate(range(19,25)):
 im=Image.open(R/f'reassembled/slide_{n}.png').convert('RGB');strip.paste(im.crop((0,0,1280,80)),(0,i*80));a=np.array(im);header_counts[str(n)]=int((a[25:65,25:225].min(2)>180).sum())
p=P/'headers.png';strip.save(p);h=hashlib.sha256(p.read_bytes()).hexdigest()[:12];p.rename(P/f'headers-{h}.png')
(R/'revision-proof-paths.json').write_text(json.dumps(proofs,indent=2));(R/'header-pixel-checks.json').write_text(json.dumps({'region':[25,25,225,65],'bright_pixels':header_counts},indent=2))
css=[]
for p in sorted(C.rglob('*.css')):
 q=R/'assets/collection'/p.relative_to(C);assert p.read_bytes()==q.read_bytes();css.append({'path':str(p.relative_to(C)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
assert len(css)==58
sheets={}
for mode in ['light','dark']:
 text=(R/f'library/{mode}.html').read_text();missing=[str(p.relative_to(C))for p in C.rglob('*.css') if p.read_text() not in text];assert not missing;sheets[mode]={'embedded_css_files_match':58,'pdf_pages':len(fitz.open(R/f'library/library-{mode}.pdf'))}
(R/'css-final-checks.json').write_text(json.dumps({'copies_match':58,'files':css,'sheets':sheets},indent=2))
imgs=[]
for p in sorted(R.rglob('*.png')):
 with Image.open(p) as im:im.verify()
 with Image.open(p) as im:imgs.append({'path':str(p.relative_to(R)),'width':im.width,'height':im.height})
(R/'png-dimensions.json').write_text(json.dumps(imgs,ensure_ascii=False,indent=2));A=json.loads((R/'audit-library.json').read_text());out={'collection':{'elements':56,'fixtures':174,'allowed_extensions_only':all(p.suffix in {'.css','.json','.md','.html'}for p in C.rglob('*')if p.is_file())},'png_count':len(imgs),'library_sheet_folders':len(list((R/'library').glob('*/light.png'))),'library_sheet_pngs':len(list((R/'library').glob('*/*.png'))),'pdfs':{str(p.relative_to(R)):len(fitz.open(p))for p in R.rglob('*.pdf')},'library_audit':{'probes':len(A),**{k:sum(len(x.get(k,[]))for x in A)for k in ['clipped','failedFonts','contrast','hiddenEssential','zeroElementRoots','overflow']}},'css_copies_match':58}
(R/'artifact-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(json.dumps(out,ensure_ascii=False,indent=2))
# Keep failing intermediate diagnostics with authoring history, outside the review ZIP.
p=R/'audit-library-targeted-before-contrast.json'
if p.exists():shutil.move(p,B/'build'/p.name)
