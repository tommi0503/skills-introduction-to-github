"""Stage only this rebuild under a new repository folder; preserve all older work."""
from pathlib import Path
from html import escape
import json,shutil,hashlib
from package_release import collect,NAMES,ROOT
DEST=Path('/workspace/work/publish/rhetis-element-rebuild-20261024')
DEST.mkdir(parents=True,exist_ok=True)
def cp(p,to):
 to.parent.mkdir(parents=True,exist_ok=True)
 if not to.exists() or hashlib.sha256(p.read_bytes()).digest()!=hashlib.sha256(to.read_bytes()).digest():shutil.copy2(p,to)
count=0
for n in NAMES:
 plans=collect(n)
 for archive,files in plans.items():
  for p,member in files:
   to=DEST/('reviews/'+n+'/'+member if archive.endswith('-review.zip')else'collections/'+member)
   cp(p,to);count+=1
for f in ROOT.joinpath('tools').glob('*.py'):cp(f,DEST/'tools'/f.name)
for f in ['profiles.json','replica-freeze.json','root-final-review.json','ORIGINS.md','GAPS-INDEX.md']:
 p=ROOT/f
 if p.exists():cp(p,DEST/f)
for p in ROOT.joinpath('dist').glob('*'):
 if p.is_file():cp(p,DEST/'dist'/p.name)
# Contract provenance is kept outside the importable collection ZIPs.
ref=Path('/workspace/work/reference')
cp(ref/'README.md',DEST/'reference'/'README.md')
for p in (ref/'contract').rglob('*'):
 if p.is_file():cp(p,DEST/'reference'/'contract'/p.relative_to(ref/'contract'))
rows=['# Replica 요소 단위 재제작','', '기존 7개 컬렉션과 동결 replica를 보존한 별도 결과다. 컬렉션마다56요소, 총392요소를 새 CSS로 작성했다. source base/계약 변형은 replica HTML의 실측에서 출발하고 나머지는 각 덱의 문법에서 추론했다.','', '**원본과100% 동일한 조립본은 아니다.** 계약에서 표현할 수 없는 장치·변형·멤버 수는 `GAPS-INDEX.md`와 각 review/GAPS.md에 이유·bbox·제안 마크업을 기록했다. 그 부분은 조립 비교에서 비어 있다.','', '| 덱 | 컬렉션 ZIP | 검수 ZIP | 소스 | 미리보기 |','|---|---|---|---|---|']
for deck,n in zip(['020','022','024','026','027','028','030'],NAMES):rows.append(f'| {deck} {n} | [{n}.zip](dist/{n}.zip) | [{n}-review.zip](dist/{n}-review.zip) | [컬렉션](collections/{n}) | [요소·페이지](reviews/{n}/index.html) |')
rows+=['','[요소별 출처:56개 요소×7컬렉션](ORIGINS.md) · [unexpressible 전체 목록](GAPS-INDEX.md) · [SHA-256](dist/SHA256SUMS) · [PNG 크기](dist/png-dimensions.json) · [검수 미리보기](index.html)','', '## 검사와 보존','', '- `dist/release-manifest.json`:14ZIP의 SHA-256/CRC,파일 목록과PNG 크기.','- `reviews/<collection>/validation/release-audit.json`:계약56개·모범fixture·최종의존성·min크기검수·font/raster·87페이지검사를 연결한 배포 검사.','- `root-final-review.json`:주 담당자가 직접 연 최종 요소 시트와 페이지 비교PNG의 해시.','- `replica-freeze.json`:이전 replica192파일의 고정 해시. 이번 ZIP은 replica를 다시 만들거나 포함하지 않는다. 이전 저장소 경로에서 보존한다.','- `reviews/*/html`, `reassembled`, `assets`:검수 HTML과글꼴·아이콘 자산. 내려받아HTTP서버로 열면 렌더할 수 있다.','- `tools`:측정·지도·시트·검사·패키징 도구. 원본 작업 환경의 `/workspace/work/reference`, `/workspace/work/delivery`, `/workspace/work/rebuild` 경로를 사용한다. 재실행 시 같은 구조로 준비하거나 도구의 ROOT 경로를 변경한다. bootstrap/foundation 생성기는 최초 골격 기록으로, 최종 요소 CSS에 다시 실행하지 않는다.','- 같은6자 문구 검사에서 계약 모범fixture의 한 일반문장과 충돌한 최소 문구 변경 등 예외는 required-fixture 감사에 명시한다.','']
(DEST/'README.md').write_text('\n'.join(rows))
items=[]
for n in NAMES:
 m=json.loads((ROOT/n/'review/map.json').read_text());g=sum(x['use']=='unexpressible'for x in m['instances']);ps=len(json.loads((ROOT/n/'build/source-dom.json').read_text()))
 items.append(f'<li><a href="reviews/{n}/index.html">{escape(n)}</a> — 56요소, {ps}페이지, 미지원 {g}개 · <a href="dist/{n}.zip">컬렉션 ZIP</a> · <a href="dist/{n}-review.zip">검수 ZIP</a></li>')
(DEST/'index.html').write_text('<!doctype html><html lang="ko"><meta charset="utf-8"><title>Rhetis 요소 검수</title><style>body{font:18px/1.7 system-ui;max-width:1100px;margin:48px auto;padding:0 24px;color:#17202a}li{margin:18px 0}a{color:#1352a4}</style><h1>Rhetis 요소 단위 재제작</h1><p>기존 replica 보존. 요소마다 라이트·다크 크기 시트와 source crop 비교를 확인할 수 있습니다. 계약 미지원 부분은 조립 비교의 빈 영역으로 남기고 목록에 기록했습니다.</p><ul>'+''.join(items)+'</ul><p><a href="ORIGINS.md">요소별 출처</a> · <a href="GAPS-INDEX.md">미지원 목록</a> · <a href="dist/release-manifest.json">검증 기록</a></p></html>')
print('Staged',count,'source/review files into',DEST)
