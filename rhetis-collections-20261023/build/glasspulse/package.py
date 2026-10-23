from pathlib import Path
from PIL import Image
import json,zipfile,hashlib,shutil,fitz
O=Path('/workspace/output');C=O/'glasspulse';R=O/'glasspulse-review'
allowed={'.css','.json','.md','.html'}
assert all(p.suffix in allowed for p in C.rglob('*') if p.is_file())
assert len(list(C.glob('elements/*/element.json')))==56
counts={};sizes={}
for kind,n,expected in [('replica',18,(1280,720)),('reassembled',18,(1280,720)),('compare-replica',18,(2560,720)),('compare-reassembled',18,(2560,720))]:
 fs=list((R/kind).glob('*.png'));assert len(fs)==n
 assert all(Image.open(p).size==expected for p in fs);counts[kind]=len(fs);sizes[kind]=list(expected)
assert len(list((R/'library').glob('*/light.png')))==57
assert len(list((R/'library').glob('*/dark.png')))==57
for mode in ['light','dark']:
 pdf=fitz.open(R/'library'/f'library-{mode}.pdf');assert len(pdf)==130
for kind in ['replica','reassembled']:
 data=json.load(open(R/kind/'checks.json'));assert all(x['font'] for x in data);assert all(not x.get('overflow') for x in data)
 # Compress existing PDFs with no image resampling.
 p=R/kind/(kind+'.pdf');d=fitz.open(p);tmp=p.with_name('compressed.pdf');d.save(tmp,garbage=4,deflate=True,deflate_images=True);d.close();tmp.replace(p)
T=R/'tools';T.mkdir(exist_ok=True)
for n in ['final-functional-three.py','fix-data-geometry.py','functional-polish.py','functional-proof.py','remove-layout-modifiers.py','fix-connectors.py','precision.py','precision-polish.py','last-details.py','fidelity-six.py','fidelity-rest.py','fidelity-extra.py','fidelity-polish.py','replica.py','collection.py','geometry.py','finalize_fixtures.py','reassemble.py','render_replica.py','render_library.py','patch_library.py']:
 shutil.copy2(Path('/workspace/work/glasspulse')/n,T/n)
(T/'README.md').write_text('최종 반입 원본은 collection 폴더의 CSS/JSON/HTML입니다. tools의 생성 스크립트는 제작 중간 기록이며 추가 검수 수정은 최종 CSS에 반영되어 있으므로 초안 생성 스크립트로 최종 CSS를 덮어쓰지 않습니다. 기존 최종 collection을 렌더할 때는 reassemble.py → README preview.py 두 모드(글꼴 링크를 ../assets/fonts.css로 교체) → render_library.py → render_replica.py reassembled 순서로 실행합니다. 스크립트는 제작 환경의 /workspace 경로를 사용하므로 다른 환경에서는 경로 상수를 해당 폴더에 맞춥니다. 폰트는 review/assets에 포함되어 있습니다. 최종 컬렉션 파일 자체가 반입을 위한 원본이며, 이 도구들은 별도 검수 자료입니다.\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'collection':'glasspulse','elements':56,'fixtures':130,'source_images':18,'counts':counts,'sizes':sizes,'library_element_sheets':112,'library_foundation_sheets':2,'font_failures':0,'page_text_outside':0,'pngs':[{'file':str(p.relative_to(R)),'size':list(Image.open(p).size),'sha256':sha(p)} for p in sorted(R.rglob('*.png'))],'pdfs':[{'file':str(p.relative_to(R)),'pages':len(fitz.open(p)),'bytes':p.stat().st_size} for p in sorted(R.rglob('*.pdf'))],'source_sha256':{str(p.relative_to(C)):sha(p) for p in sorted(C.rglob('*')) if p.is_file()}}
(R/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
for folder in [C,R]:
 zpath=O/(folder.name+'.zip')
 with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in sorted(folder.rglob('*')):
   if p.is_file():z.write(p,str(p.relative_to(O)))
 with zipfile.ZipFile(zpath) as z:
  assert z.testzip() is None
  assert {Path(n).parts[0] for n in z.namelist()}=={folder.name}
 print(zpath,zpath.stat().st_size,sha(zpath))
