from pathlib import Path
import json,hashlib,fitz,html
from PIL import Image
B=Path(__file__).resolve().parents[1];R=B/'review';C=B/'collection'/'afterglow'
originals=Path('/workspace/work/deck/miricanvas_기업_selected/015_1a53x_검정과_파랑의_심플한_서비스_소개서')
triples=R/'compare-three';triples.mkdir(exist_ok=True)
for i in range(1,10):
 n=f'slide_{i:02}.png';imgs=[Image.open(originals/n).convert('RGB'),Image.open(R/'replica'/n).convert('RGB'),Image.open(R/'reassembled'/n).convert('RGB')]
 im=Image.new('RGB',(3840,720))
 for j,img in enumerate(imgs):im.paste(img,(1280*j,0))
 im.save(triples/n)
# Reproducible source and final render checks.
errors=[];sizes=[]
for kind in ['replica','reassembled']:
 files=sorted((R/kind).glob('slide*.png'))
 if len(files)!=9:errors.append(kind+' image count')
 for p in files:
  size=Image.open(p).size;sizes.append({'path':str(p.relative_to(R)),'size':size})
  if size!=(1280,720):errors.append(str(p)+' size')
 doc=fitz.open(R/kind/(kind+'.pdf'))
 if len(doc)!=9:errors.append(kind+' PDF count')
 for p in doc:
  if tuple(p.rect[2:])!=(1280,720):errors.append(kind+' PDF dimensions')
 doc.close()
for kind in ['compare-replica','compare-reassembled']:
 files=list((R/kind).glob('*.png'))
 if len(files)!=9:errors.append(kind+' count')
 for p in files:
  size=Image.open(p).size;sizes.append({'path':str(p.relative_to(R)),'size':size})
  if size!=(2560,720):errors.append(kind+' size')
for el in (C/'elements').iterdir():
 for mode in ['light','dark']:
  p=R/'library'/el.name/(mode+'.png')
  if not p.exists():errors.append('Missing sheet '+str(p))
  else:sizes.append({'path':str(p.relative_to(R)),'size':Image.open(p).size})
collection_files=[p for p in C.rglob('*') if p.is_file()]
if any(p.suffix not in ['.css','.json','.md','.html'] for p in collection_files):errors.append('disallowed extension')
copy=R/'assets/collection/afterglow'
if not all((copy/p.relative_to(C)).read_bytes()==p.read_bytes() for p in collection_files):errors.append('review CSS copy mismatch')
hashes={str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in collection_files+list((R/'replica').glob('*.html'))+list((R/'reassembled').glob('*.html'))}
audits={}
for n in ['replica','library','reassembled']:
 a=json.loads((R/f'audit-{n}.json').read_text());audits[n]={'probes':len(a),'clipped':sum(len(x['clipped']) for x in a),'overflow':sum(len(x['overflow']) for x in a),'failedFonts':sum(len(x['failedFonts']) for x in a),'contrastWarnings':sum(len(x.get('contrast',[])) for x in a)}
 for x in a:
  if x['failedFonts']:errors.append(n+' font failure')
  if x['clipped']:errors.append(n+' text clipping '+x.get('file',x.get('fixture','')))
  if n!='library' and x.get('sha256')!=hashlib.sha256((R/n/x['file']).read_bytes()).hexdigest():errors.append(n+' stale HTML '+x['file'])
report={'collection':'afterglow','sourceDeck':'015','images':9,'elements':56,'fixtures':sum(len(list((p/'fixtures').glob('*.html'))) for p in (C/'elements').iterdir()),'errors':errors,'auditSummary':audits,'pngDimensions':sizes,'sourceSha256':hashes,'note':'Library element sheets are multi-row contact sheets, comparison PNGs are 2560x720, three-way comparisons 3840x720. Slide PNGs and PDF pages are 1280x720. Scroll diagnostics include internal chart labels, anchors, pseudo-element connections and numeric glyph line boxes.'}
(R/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
links=''.join(f'<li><b>{i:02}</b> <a href="replica/slide_{i:02}.html">Replica HTML</a> · <a href="reassembled/slide_{i:02}.html">Reassembled HTML</a> · <a href="compare-three/slide_{i:02}.png">Original | Replica | Reassembled</a><img loading="lazy" src="compare-reassembled/slide_{i:02}.png" alt="원본과 재조립본 {i}"></li>' for i in range(1,10))
elinks=''.join(f'<li>{p.name}: <a href="library/{p.name}/light.png">Light</a> · <a href="library/{p.name}/dark.png">Dark</a></li>' for p in sorted((C/'elements').iterdir()))
page='''<!doctype html><html lang="ko"><meta charset="utf-8"><title>Afterglow Review</title><style>@font-face{font-family:Review;src:url('assets/PretendardVariable.woff2')}body{margin:0;background:#111;color:#eee;font:16px Review,sans-serif;padding:40px}main{max-width:1400px;margin:auto}a{color:#8ebcff}h1{font-size:48px;font-weight:400}p{line-height:1.6}li{margin:16px 0}img{display:block;width:100%;height:auto;margin-top:12px}ul{padding-left:20px}.elements{columns:3}</style><main><h1>Afterglow</h1><p>015 서비스 소개 덱 · 9장 · 56개 요소<br>검정 프레임 화면, 하단 광선, 원형 목차와 밝은 서비스 카드.</p><p><a href="design-language.md">Design language</a> · <a href="review-notes.md">Review notes</a> · <a href="image-inventory.md">Image inventory</a> · <a href="verification.json">Verification</a></p><p><a href="replica/replica.pdf">Replica PDF</a> · <a href="reassembled/reassembled.pdf">Reassembled PDF</a> · <a href="library/light.html">Light sheet HTML</a> · <a href="library/dark.html">Dark sheet HTML</a> · <a href="library/library-light.pdf">Light PDF</a> · <a href="library/library-dark.pdf">Dark PDF</a></p><h2>Pages</h2><ul>'''+links+'</ul><h2>Elements</h2><ul class="elements">'+elinks+'</ul></main></html>'
(R/'index.html').write_text(page)
print(json.dumps({'errors':errors,'elements':56,'fixtures':report['fixtures'],'audit':audits},ensure_ascii=False))
