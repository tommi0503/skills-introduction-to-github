"""Package the current published Round 5 text sources, excluding binary outputs."""
from pathlib import Path,PurePosixPath
from collections import Counter
from datetime import datetime
from zoneinfo import ZoneInfo
import base64,hashlib,io,json,zipfile
from publish_api import ROOT,REPO,PREFIX,api,current,oid
ALLOWED={'.css','.json','.md','.html','.js','.mjs','.cjs','.ts','.tsx','.jsx','.py','.txt','.yml','.yaml','.toml','.sh'}
NAMES={'.gitignore','SHA256SUMS','LICENSE','Makefile','Dockerfile'}
OUTPUT_NAMES={'SOURCE-ONLY.md','SOURCE-ONLY-MANIFEST.json','source-only-manifest.json','source-only-archive.json','source-only-publication.json','source-only-download-verification.json','source-only-publication-proof.json'}
def wanted(path):
 p=PurePosixPath(path)
 return '..'not in p.parts and not p.is_absolute()and not any(s in {'__pycache__','.git','.sheet-work','.pytest_cache','node_modules'}for s in p.parts)and p.name not in OUTPUT_NAMES and(p.suffix.lower()in ALLOWED or p.name in NAMES)
def main():
 commit=current();head=api('GET','/git/commits/'+commit);root=api('GET','/git/trees/'+head['tree']['sha']);folder=next(x for x in root['tree']if x['path']==PREFIX);tree=api('GET','/git/trees/'+folder['sha']+'?recursive=1');assert not tree.get('truncated')
 selected=[r for r in tree['tree']if r['type']=='blob'and wanted(r['path'])];records=[];payload={};cached=0;fetched=0
 for row in selected:
  rel=row['path'];local=ROOT/rel;data=local.read_bytes()if local.is_file()else None
  if data is not None and oid(data)==row['sha']:cached+=1
  else:
   blob=api('GET','/git/blobs/'+row['sha']);assert blob['encoding']=='base64';data=base64.b64decode(blob['content']);fetched+=1
  assert oid(data)==row['sha'],rel;data.decode('utf-8');assert b'\0'not in data,rel+' is not text';payload[rel]=data;records.append({'path':rel,'bytes':len(data),'gitBlobSHA':row['sha'],'sha256':hashlib.sha256(data).hexdigest(),'origin':'published-source'})
 # Include this packager and a clear explanation of the intentionally absent assets.
 rel='tools/package_source_only.py';data=Path(__file__).read_bytes();payload[rel]=data;records=[r for r in records if r['path']!=rel];records.append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'origin':'packager-added'})
 archive_name=PREFIX+'-source-only.zip'
 note='\n'.join(['# 소스 전용 ZIP','','[소스 ZIP 다운로드]('+archive_name+')','','대상 저장소: `'+REPO+'`','소스 기준 커밋: `'+commit+'`','','7개 컬렉션의 CSS·JSON·HTML·설명, foundation·fixture, replica/reassembled HTML, 계약 문서, JavaScript·Python 도구와 검수 메타데이터를 담았습니다.','','제외: 이미지 파일(PNG/JPG/SVG 등), PDF, 폰트 바이너리(WOFF/TTF 등), 기존 ZIP, 실행 캐시와 로그. HTML/CSS 내부의 SVG 마크업은 소스 코드로 유지합니다.','','폰트 파일은 제외했으므로 실제 화면을 같은 글꼴로 렌더하려면 원래 저장소의 fonts/ 바이너리가 필요합니다. 일부 검수·PDF 생성 도구도 제외된 PNG를 입력으로 사용합니다.','','압축 내부 최상위 폴더는 `'+PREFIX+'/` 하나입니다. 파일별 출처·SHA-256은 `SOURCE-ONLY-MANIFEST.json`에 있습니다.',''])
 payload['SOURCE-ONLY.md']=note.encode();records.append({'path':'SOURCE-ONLY.md','bytes':len(note.encode()),'sha256':hashlib.sha256(note.encode()).hexdigest(),'origin':'archive-note-added'})
 manifest={'repository':REPO,'sourceCommit':commit,'sourcePrefix':PREFIX,'createdKST':datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),'allowedExtensions':sorted(ALLOWED),'exclusions':['images including SVG','PDF','font binaries','existing ZIPs','caches','logs'],'files':sorted(records,key=lambda r:r['path'])};manifest_data=json.dumps(manifest,ensure_ascii=False,indent=2).encode();payload['SOURCE-ONLY-MANIFEST.json']=manifest_data
 out=ROOT/archive_name
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
  for name,data in sorted(payload.items()):
   assert wanted(name)or name in {'SOURCE-ONLY.md','SOURCE-ONLY-MANIFEST.json'}
   info=zipfile.ZipInfo(PREFIX+'/'+name,date_time=(2026,10,25,0,0,0));info.external_attr=0o100644<<16;info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,data,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
 with zipfile.ZipFile(out)as z:
  assert z.testzip()is None;assert {n.split('/')[0]for n in z.namelist()}=={PREFIX};assert len(z.namelist())==len(payload)
  for name in z.namelist():
   assert not name.startswith('/')and'..'not in PurePosixPath(name).parts;assert PurePosixPath(name).suffix.lower()in ALLOWED or PurePosixPath(name).name in NAMES
   data=z.read(name);data.decode('utf-8');assert b'\0'not in data
  for row in records:assert hashlib.sha256(z.read(PREFIX+'/'+row['path'])).hexdigest()==row['sha256']
 report={'name':archive_name,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'files':len(payload),'sourceCommit':commit,'repository':REPO,'topLevelFolder':PREFIX,'extensions':dict(sorted(Counter(PurePosixPath(n).suffix.lower()or'(extensionless)'for n in payload).items())),'verification':{'zipCRC':'pass','allEntriesUTF8Text':'pass','fileHashes':'pass','images':0,'pdfs':0,'fontBinaries':0,'nestedZIPs':0},'sourceFilesReadFromLocalMatchingGitBlob':cached,'sourceFilesFetchedFromGitHub':fetched}
 (ROOT/'SOURCE-ONLY.md').write_text(note);(ROOT/'source-only-manifest.json').write_bytes(manifest_data);(ROOT/'source-only-archive.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2),flush=True)
if __name__=='__main__':main()
