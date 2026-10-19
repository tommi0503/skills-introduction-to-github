from pathlib import Path
import zipfile,json,hashlib,shutil
R=Path(__file__).resolve().parents[1];O=R/'downloads';O.mkdir(exist_ok=True)
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def zwrite(name,pairs):
 out=O/name
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6)as z:
  for p,n in pairs:z.write(p,n)
 with zipfile.ZipFile(out)as z:assert z.testzip()is None;count=len(z.namelist());roots=sorted({n.split('/')[0]for n in z.namelist()})
 assert out.stat().st_size<100*1024*1024,(name,out.stat().st_size)
 return{'file':name,'bytes':out.stat().st_size,'sha256':h(out),'entries':count,'roots':roots,'crcVerified':True}
def files(d):return sorted(p for p in d.rglob('*')if p.is_file())
collection=R/'library/rhetis-report';report=[];report.append(zwrite('rhetis-report-collection.zip',[(p,'rhetis-report/'+str(p.relative_to(collection)))for p in files(collection)]))
source=[]
for folder in ['src','tools','contract','library','public','review']:
 for p in files(R/folder):
  if p.name=='github-download-verification.json':continue
  source.append((p,'rhetis-part03/'+str(p.relative_to(R))))
for f in ['README.md','package.json','tsconfig.json','index.html','assembly.html','.gitignore']:source.append((R/f,'rhetis-part03/'+f))
report.append(zwrite('rhetis-part03-source.zip',source))
review=[]
for folder in ['renders/final','renders/assembly','renders/library','deliverables','library','public/fonts','review']:
 for p in files(R/folder):
  if p.name=='github-download-verification.json':continue
  review.append((p,'rhetis-part03/'+str(p.relative_to(R))))
for p in sorted((R/'comparisons/final').glob('*.png')):review.append((p,'rhetis-part03/'+str(p.relative_to(R))))
review.append((R/'assembly.html','rhetis-part03/assembly.html'))
readme=R/'deliverables/README-REVIEW.md';readme.write_text('# Rhetis Part 03 검수 결과\n\n`deliverables/preview.html`을 열어 전체90개 화면을 확인하세요. 원본 비교와 라이브러리 조립본 토글이 있습니다. 파일 접근이 제한된 브라우저에서는 이 폴더에서 `python -m http.server 8000` 실행 후 접속하세요.\n\n- `renders/final/`: 재현90장 PNG\n- `renders/assembly/`: 재조립90장 PNG\n- `renders/library/`:89fixture ×2모드 =178장 PNG\n- `comparisons/final/`: 원본/재현 비교90장 PNG\n- `deliverables/pdf/`: 전체·덱별·비교·시트·라이브러리 PDF\n- `library/rhetis-report/`:31개 요소 컬렉션과 light/dark 미리보기\n- `review/summary.md`: 검수·수정·해석·차이 기록\n\n슬라이드 PNG358개는1280×720이며 비교PNG90개는2560×720입니다. source ZIP은 별도 제공합니다.\n')
review.append((readme,'rhetis-part03/README-REVIEW.md'))
report.append(zwrite('rhetis-part03-review.zip',review))
(O/'manifest.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
# Optionally copy deliverables to a caller-selected writable export folder.
import os
export_dir=os.environ.get('RHETIS_EXPORT_DIR')
if export_dir:
 output=Path(export_dir);output.mkdir(parents=True,exist_ok=True)
 for p in O.glob('*'):shutil.copyfile(p,output/p.name)
 shutil.copyfile(R/'deliverables/preview/overview.jpg',output/'rhetis-part03-overview.jpg')
