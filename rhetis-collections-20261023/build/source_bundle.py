from pathlib import Path
import argparse,hashlib,html,json,re,shutil,zipfile
NAMES={'fluxweave':18,'cyanloop':18,'roundrise':24,'nightchamfer':18,'glasspulse':18}
ROOT_NAME='rhetis-all-collections-source';RENDER={'.png','.jpg','.jpeg','.webp','.pdf','.zip'}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def copy_filtered(src,dst):
 for p in src.rglob('*'):
  if p.is_file() and p.suffix.lower() not in RENDER and '__pycache__' not in p.parts and p.suffix!='.pyc':
   q=dst/p.relative_to(src);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
def build(root,work):
 stage=work/ROOT_NAME;assert not stage.exists(),'Inspect an existing stage before rebuilding';stage.mkdir(parents=True)
 records=[]
 for name,count in NAMES.items():
  copy_filtered(root/name,stage/name);source=root/(name+'-review');dest=stage/(name+'-review')
  for folder in ['replica','reassembled','library','assets','fonts','tools','audits']:
   if (source/folder).is_dir():copy_filtered(source/folder,dest/folder)
  for p in source.iterdir():
   if p.is_file() and p.suffix in ['.md','.json']:
    q=dest/p.name;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
  elements=len(list((stage/name/'elements').glob('*/element.json')))
  replica=sorted((dest/'replica').glob('slide*.html'));reassembled=sorted((dest/'reassembled').glob('slide*.html'))
  assert elements==56 and len(replica)==count and len(reassembled)==count,(name,elements,len(replica),len(reassembled))
  records.append({'collection':name,'elements':elements,'replica_pages':len(replica),'reassembled_pages':len(reassembled)})
 for folder in ['reference','build','validation']:copy_filtered(root/folder,stage/folder)
 shutil.copy2(root/'inventory.md',stage/'inventory.md')
 for folder in ['element-review-pdfs','slide-comparison-pdfs']:
  d=stage/folder;d.mkdir();shutil.copy2(root/folder/'build_pdfs.py',d/'build_pdfs.py')
  (d/'README.md').write_text('이 폴더는 PDF 생성 코드를 보존합니다. 실행 시에는 생성된 비교/요소 시트 PNG가 필요합니다. 원래 렌더 결과와 검수 PDF는 GitHub의 같은 폴더에서 받을 수 있습니다.\n')
 (stage/'README.md').write_text('''# Rhetis 전체 컬렉션·복제본 통합 소스

5개 컬렉션(각56요소), 원본96장에 대한 replica HTML96개, 라이브러리 조립 HTML96개, 실행용 폰트·아이콘·스타일, 라이트·다크 라이브러리 HTML, 계약과 미리보기 도구를 묶었습니다.

## 실행

압축을 풀고 이 README가 있는 폴더에서 실행하세요.

```sh
python -m http.server 8000 --bind 127.0.0.1
```

브라우저에서 `http://127.0.0.1:8000/index.html`을 열면 각 덱의 모든 replica·조립본과 요소 시트로 이동할 수 있습니다.

## 구성

- `fluxweave/`, `cyanloop/`, `roundrise/`, `nightchamfer/`, `glasspulse/`: kit·foundation·전체56요소·fixture. Rhetis 반입 대상은 각 컬렉션 폴더입니다.
- `<collection>-review/replica/`: 원본을 재현한 HTML·CSS와 필요한 자산.
- `<collection>-review/reassembled/`: 해당 컬렉션의 foundation·요소로 조립한 HTML과 실행 CSS.
- `<collection>-review/library/`: 라이트·다크 미리보기 HTML과 공용 CSS.
- `<collection>-review/assets/`, `fonts/`, `replica/assets/`: 폰트·아이콘 등 실행 자산. 상대 경로를 유지했습니다.
- `reference/`: README 계약·taxonomy·palette·type steps·글꼴·preview.py·모범 fixture.
- `build/`: 제작·렌더·검수에 사용한 코드. 작업 환경의 `/workspace` 절대 경로는 실행 환경에 맞게 조정하세요.
- `element-review-pdfs/`, `slide-comparison-pdfs/`: 추가 PDF 생성 코드.
- `inventory.md`, 각 review 폴더의 `design-language.md`·`review-notes.md`: 범위·디자인 규칙·차이와 판단 기록.

시트 재생성 예:

```sh
python reference/tools/preview.py fluxweave reference/contract/type-steps.json --out light.html
python reference/tools/preview.py fluxweave reference/contract/type-steps.json --dark --out dark.html
```

이 ZIP은 코드와 실행 자산을 모은 소스 패키지입니다. 렌더 PNG·PDF와 개별 컬렉션 ZIP은 기존 GitHub 제출물에서 별도로 받을 수 있습니다. PDF 생성 코드는 해당 렌더 PNG를 입력으로 사용합니다. 기존 원본/카피 비교나 요소 디자인은 수정하지 않았습니다.
''')
 sections=[]
 for name,count in NAMES.items():
  review=stage/(name+'-review');rows=[]
  for a,b in zip(sorted((review/'replica').glob('slide*.html')),sorted((review/'reassembled').glob('slide*.html'))):
   rows.append('<tr><td>'+re.search(r'(\d+)\.html$',a.name)[1]+'</td><td><a href="'+str(a.relative_to(stage))+'">replica HTML</a></td><td><a href="'+str(b.relative_to(stage))+'">라이브러리 조립 HTML</a></td></tr>')
  sections.append(f'<section><h2>{name} <small>{count}장 / 56요소</small></h2><p><a href="{name}/">컬렉션 소스</a> · <a href="{name}-review/library/light.html">라이트 요소 시트</a> · <a href="{name}-review/library/dark.html">다크 요소 시트</a> · <a href="{name}-review/design-language.md">디자인 언어</a> · <a href="{name}-review/review-notes.md">검수 기록</a></p><details><summary>페이지 목록</summary><table><thead><tr><th>페이지</th><th>원본 재현</th><th>컬렉션 조립</th></tr></thead><tbody>'+''.join(rows)+'</tbody></table></details></section>')
 (stage/'index.html').write_text('<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Rhetis 통합 소스</title><style>body{font:16px/1.6 system-ui,sans-serif;max-width:1100px;margin:40px auto;padding:0 24px;background:#f5f6f8;color:#17202b}h1{font-size:30px}section{background:white;padding:20px 28px;border:1px solid #dce1e7;border-radius:12px;margin:20px 0}h2{margin:0}small{font-size:14px;font-weight:400;color:#586474}a{color:#1251ab}table{border-collapse:collapse;width:100%;margin-top:16px}td,th{text-align:left;padding:8px;border-bottom:1px solid #e1e5eb}summary{cursor:pointer}</style><h1>Rhetis 전체 컬렉션·복제본 코드</h1><p>5개 컬렉션 · 전체280요소 · replica96장 · 라이브러리 조립96장</p>'+''.join(sections)+'</html>')
 copied=[]
 for p in stage.rglob('*'):
  if p.is_file():
   rel=p.relative_to(stage);original=root/rel
   if original.is_file() and p.name not in ['README.md','index.html']:assert digest(p)==digest(original),str(rel)
   copied.append({'path':str(rel),'bytes':p.stat().st_size,'sha256':digest(p)})
 (stage/'source-manifest.json').write_text(json.dumps(copied,ensure_ascii=False,indent=2)+'\n')
 (stage/'bundle-info.json').write_text(json.dumps({'source_root':str(root),'collections':records,'elements':280,'replica_pages':96,'reassembled_pages':96,'copied_files_before_manifests':len(copied)},ensure_ascii=False,indent=2)+'\n')
 print(stage,len(copied),'files',sum(r['bytes'] for r in copied),'bytes',flush=True)
 return stage
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--work',type=Path,required=True);a=p.parse_args();build(a.root,a.work)
