from pathlib import Path
import shutil,json,hashlib
ROOT=Path('/workspace');OUT=ROOT/'output';REPO=ROOT/'skills-introduction-to-github';DEST=REPO/'rhetis-collections-20261023'
NAMES={'fluxweave':('002','기업소개서',18),'cyanloop':('003','교육 자료',18),'roundrise':('004','기업행사 안내',24),'nightchamfer':('005','사업 계획',18),'glasspulse':('006','타운홀',18)}
if DEST.exists():raise SystemExit('Destination exists; inspect before updating')
DEST.mkdir()
for n in NAMES:
 for suffix in ['', '-review']:
  shutil.copytree(OUT/(n+suffix),DEST/(n+suffix))
  shutil.copy2(OUT/(n+suffix+'.zip'),DEST/(n+suffix+'.zip'))
shutil.copy2(OUT/'inventory.md',DEST/'inventory.md')
ref=DEST/'reference';ref.mkdir()
for item in ['contract','fonts','tools']:
 shutil.copytree(ROOT/'work/reference'/item,ref/item)
shutil.copy2(ROOT/'work/reference/README.md',ref/'README.md')
# The reference fixtures are kept only to make the required DOM/data comparison inspectable.
for folder,sample in {'card':'confetti','callout':'annual','chart-area':'annual','chart-bar':'confetti','chart-donut':'amethyst','chart-line':'amethyst'}.items():
 src=ROOT/'work/reference/samples'/sample/'elements'/folder/'fixtures'
 shutil.copytree(src,ref/'samples'/sample/'elements'/folder/'fixtures')
build=DEST/'build';build.mkdir()
for n in NAMES:
 target=build/n;target.mkdir()
 for p in (ROOT/'work'/n).glob('*.py'):shutil.copy2(p,target/p.name)
val=DEST/'validation';val.mkdir()
for p in (ROOT/'work/integration').glob('*.json'):shutil.copy2(p,val/p.name)
for p in (ROOT/'work/integration').glob('*.py'):shutil.copy2(p,build/p.name)
# Preview images are copies of final files, not a new render or an older build.
prev=DEST/'previews';prev.mkdir()
rows=[]
for n,(number,title,count) in NAMES.items():
 candidates=sorted((DEST/(n+'-review')/'compare-reassembled').glob('*.png'))
 selected=next((p for p in candidates if '06' in p.name),candidates[0])
 shutil.copy2(selected,prev/(n+'.png'))
 rows.append(f'| {number} {title} | {count} | [{n}.zip]({n}.zip) | [검수 ZIP]({n}-review.zip) | [컬렉션 소스]({n}/) · [검수 소스]({n}-review/) |')
readme=['# Rhetis 디자인 컬렉션 5종','', '원본 96장으로부터 만든 별도 컬렉션 5종입니다. 각 컬렉션은 kit, foundation, 계약 요소 56개를 포함합니다.','', '| 덱 | 원본 장수 | 반입용 ZIP | 검수 ZIP | 소스 |','|---|---:|---|---|---|',*rows,'', '[전체 이미지 목록과 계약 대응](inventory.md) · [검증 결과](validation/)','', '검수 ZIP에는 원본 재현 HTML·PNG·PDF, 원본 비교 이미지, 라이트·다크 요소 시트와 PDF, 컬렉션만으로 재조립한 페이지, 디자인 언어와 차이·결정 기록을 담았습니다. 사진·복잡한 3D·그래픽 배경은 요청에 따라 회색 자리로 대체했습니다. 나머지 차이는 각 검수 폴더의 review-notes.md에 기록했습니다.','', '## 최종 재조립 비교 미리보기','']
for n,(_,title,_) in NAMES.items():readme += [f'### {title} · {n}','',f'![원본과 재조립 비교 — {n}](previews/{n}.png)','']
readme += ['## 파일 검증','', '컬렉션 ZIP은 최상위 폴더 하나만 포함하고 CSS·JSON·MD·HTML만 담습니다. 페이지 PNG는 1280×720입니다. 비교 이미지와 요소별 시트의 크기는 validation/artifact-audit.json에 파일별로 기록했습니다. ZIP의 SHA-256 및 재다운로드 검증 결과는 verification.json을 참고하세요.','', '## 로컬 미리보기','', '브라우저 파일 접근 정책에 따라 이 폴더에서 로컬 HTTP 서버를 실행하고 review 폴더의 HTML을 여세요. 라이브러리 시트 재생성은 다음 명령으로 할 수 있습니다.','', '```sh','python reference/tools/preview.py fluxweave reference/contract/type-steps.json --out light.html','python reference/tools/preview.py fluxweave reference/contract/type-steps.json --dark --out dark.html','```','', 'build/에는 작업에 사용한 생성·렌더·검수 스크립트를 보존했습니다. 스크립트의 /workspace 경로는 제작 환경을 기준으로 하므로 다른 환경에서는 해당 경로를 조정해야 합니다.']
(DEST/'README.md').write_text('\n'.join(readme)+'\n')
manifest=[]
for p in DEST.rglob('*'):
 if p.is_file():manifest.append({'path':str(p.relative_to(DEST)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(DEST/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(DEST,len(manifest),'files',sum(x['bytes'] for x in manifest),'bytes')
large=[x for x in manifest if x['bytes']>=100*1024*1024]
if large:raise SystemExit('Oversized GitHub files: '+str(large))
