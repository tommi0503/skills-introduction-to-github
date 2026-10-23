from pathlib import Path
import json,hashlib,collections
from PIL import Image
import fitz
R=Path('/workspace/work/deliverables/dockside');V=R/'review';C=R/'collection/dockside'
a={}
for k in ['replica','reassembled','library']:
 x=json.loads((V/f'audit-{k}.json').read_text());a[k]={'probes':len(x),**{s:sum(len(z.get(s,[])) for z in x) for s in ['clipped','overflow','contrast','failedFonts','hiddenEssential','iconErrors']}}
assets={str(p.relative_to(C)):hashlib.sha256(p.read_bytes()).hexdigest() for p in C.rglob('*.css')};copies=all((V/'assets/collection'/n).read_bytes()==(C/n).read_bytes() for n in assets)
pngs={str(p.relative_to(V)):list(Image.open(p).size) for p in V.rglob('*.png')}
pdfs={str(p.relative_to(V)):len(fitz.open(p)) for p in V.rglob('*.pdf')}
page_checks={k:{'count':len(list((V/k).glob('slide_*.png'))),'sizeOK':all(Image.open(p).size==((2560,720) if k.startswith('compare') else (1280,720)) for p in (V/k).glob('slide_*.png'))} for k in ['replica','reassembled','compare-replica','compare-reassembled']}
out={'collection':'dockside','status':'source-frozen-after-reopened-fidelity-review','elements':56,'fixtures':len(list(C.glob('elements/*/fixtures/*.html'))),'audit':a,'pageChecks':page_checks,'librarySheetFolders':len([p for p in (V/'library').iterdir() if p.is_dir()]),'cssCopiesByteIdentical':copies,'cssHashes':assets,'pngDimensions':pngs,'pdfPageCounts':pdfs,'sourceHTMLHashes':{str(p.relative_to(V)):hashlib.sha256(p.read_bytes()).hexdigest() for k in ['replica','reassembled'] for p in (V/k).glob('*.html')}}
(V/'audit-build.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(json.dumps({k:out[k] for k in ['elements','fixtures','audit','pageChecks','librarySheetFolders','cssCopiesByteIdentical','pdfPageCounts']},ensure_ascii=False))
notes='''# Dockside 검수 기록

## 범위와 제작 경과

016 아이디어 피칭 기획서 원본 30장, 모두 1280×720. 문서·슬라이드 문구는 자료로 취급했다. README 전체 220줄과 계약 JSON을 확인했다. 최초 replica → 디자인 언어 → 56요소 → 시트 → 재조립 순서로 제작했으며, 최초 세 차례 검수 후 사용자의 원본 충실도 재작업 요구에 따라 새로운 검수 라운드를 열었다.

새 라운드에서는 초기의 도형 정규화 결정을 철회했다. 05 채움 버블과 성장 막대, 07 동심원, 17 아래로 잘리는 채움 원과 네 설명판, 18 가로 상세 띠, 22 원형 단계, 23 계단, 24 다섯 위성 관계도, 27 조직도, 28 굽은 가지를 실제 원본 기하로 복원했다. 원본 팔레트는 review의 host에서 공급하고 컬렉션에는 색의 자리만 유지했다.

원본과 replica, 원본과 조립본 비교 PNG를 30장씩 개별로 열어 확인했다. 마지막에는 주 에이전트의 개별 화면 검수 지적을 받아 02 요약/키워드 −14px, 03 이중 구분선 삭제, 11 파란 띠 본문 좌측 정렬, 14 사진 아래 점과 꺾인 연결선을 반영했다. 추가 미세 변경을 멈추고 전체 30장을 다시 렌더했다.

## 소스와 재현 방식

- 조립본은 foundation의 12×6 .body와 계약 클래스/data-el만 사용한다. 페이지별 새 CSS는 없다. 원본의 고정 기하를 표현하는 요소 CSS는 모두 컬렉션 안에 있다.
- review/assets/collection의 CSS 58개는 최종 컬렉션과 동일 바이트 복사다. 검토 ZIP만 풀어도 조립본을 열 수 있다.
- 최초 replica의 자유 배치 소스도 신규 검수에서 개선한 원본 좌표와 줄바꿈으로 동기화했다. 최종 replica는 독립 replica.css에 그리기 규칙을 고정하여 컬렉션 경로에 의존하지 않는다. 두 최종 결과는 공통으로 검증한 원본 기하를 사용한다. 최초 및 신규 검수 중간 이미지 일부는 round2에 보관했다.
- 실제 Pretendard Variable 파일을 로드한다. 부모의 글꼴 마스크 비교 결과에 따라 제목은 60px/600/−1.5px를 사용했다. 원본 측정값 59.4px는 계약의 60px 단계로 옮겼다. 본문은 16·18·22px 단계와 공유 tracking 토큰을 사용했다.
- 화면을 회전하거나 비율을 늘리지 않았다. 원본 이미지를 배경으로 깔지 않았다. 사진·3D아이콘·기기 화면·복잡한 그림은 회색 단색 seat로 바꿨다. 단순 선·도형·차트·Lucide 아이콘은 실제 구현했다.

## 남는 차이와 판독 불가

| 페이지 | 남는 차이 또는 판단 |
|---|---|
| 01–03,30 | 로고 이미지 및 3D 도크 아이콘은 회색 번호 자리. 도크의 확대 항목과 장별 활성 표시 위치는 구현했다. |
| 전 페이지 | 원본 배경의 단순 반투명 대각 밴드와 넓은 빛의 변화는 CSS gradient/mask로 직접 그렸다. JPEG 노이즈·종이 질감·미세 색 번짐은 재현되지 않는다. 밴드의 부드러움과 경계가 원본과 완전히 같지는 않다. |
| 01–30 | 원본 폰트 파일을 확정할 수 없어 계약 폰트 중 실측이 가장 가까운 Pretendard Variable을 사용했다. 일부 글자 폭·획·행간과 1–수 px 좌표 차이가 남는다. 픽셀 100% 일치 판정은 하지 않는다. |
| 06,08,13,18,23 | 작은 설명 일부는 완전 전사가 아닌 문맥에 맞는 한국어 보완이다. 08의 세 인사이트 설명, 13 기능 설명, 23 단계 활동 설명은 원문 동일성을 보증하지 않는다. |
| 10–16,19,24–28 | 제품/앱/인물/복잡한 3D 그림의 회색 영역이 원본과 가장 크게 다르다. 25의 복잡한 배경 그림도 회색 자리로 처리했다. |
| 20,23,29,30 | 읽을 수 있는 단순 아이콘은 Lucide의 가장 가까운 의미로 구현했다. 원본의 세부 stroke나 채움이 동일하지 않은 경우가 있다. |
| 17 | 원본처럼 큰 중앙 원과 외부 점선이 페이지 아래로 의도적으로 잘린다. 라이브러리 fixture에서는 더 높은 기준선을 사용해 큰 점선까지 영역 안에 둔다. |
| 06 | 원본처럼 세 번째 패널의 일부만 오른쪽 가장자리에 보인다. 영역 밖의 불필요한 설명 문구는 넣지 않았다. |

초기 버전의 ‘05 도넛·07 허브·22/23 수평 단계로 바꾸어도 된다’는 판단은 최종 버전에 적용되지 않는다. 재조립의 원본 팔레트를 기준 팔레트로 바꾼 초기 결정도 철회했다.

## 라이브러리 검수와 계약 결정

56개 요소, 요소 fixture 183개와 foundation fixture 2개를 포함한다. README 모범 fixture 28개는 data-el 접두사만 바꾸고 원본 마크업/데이터를 보존했다. 해당 원본의 group/stack wrapper, 일부 row 배치, 문자 아이콘은 일반 규칙과 충돌해도 사용자 지시의 동일 fixture 보존을 우선했다.

원본에 없는 요소도 밝은 림, inset 면, 작은 진한 캡슐, 도크의 활성 강조 문법으로 설계했다. 기본 fixture 외에 원본의 성장 버블·키워드 동심원·차별화 허브·원형/계단 단계·페르소나·조직도·팀 맵을 직접 검수하는 fixture 8개를 추가했다. 고정 원본 stage의 해당 구성은 min 12×6으로 선언하고 더 낮은 전체 시트의 기준선을 조정했다.

모든 fixture를 12×6과 선언한 최소 칸으로 렌더했다. 원본 전용 selector가 기본 모범 카드·일반 동심원·일반 사람 카드·목록에 적용되는 충돌을 구조 조건/계약 변형으로 분리했다. source 버블의 글자색은 a1-on을 쓰고, 다크에서는 gradient가 어두운 바탕 단계까지 내려가지 않도록 별도 설계했다. 시트의 전역 frame/small 스타일 침범도 scoped CSS로 방어했다. code에는 실제 Nanum Gothic Coding을 사용한다.

## 자동 검사 해석

새 Chromium page, document.fonts.ready, 2회의 animation frame, 600ms 대기 후 캡처했다. 초기 80ms 대기에서는 드물게 제목이 DOM에 있으나 PNG에서 빠지는 현상이 있어 최종 전수 캡처에는 사용하지 않았다.

최종 수치는 다음과 같다. 원시 audit JSON을 삭제하거나 0으로 정리하지 않았다.

'''
for k,v in a.items():notes+='- '+k+': '+', '.join(f'{n}={z}' for n,z in v.items())+'\n'
notes+='''
라이브러리 기준 팔레트의 대비 검사는 통과했다. 원본 host에서 발생하는 contrast 경고는 원본의 연한 설명·파랑·각주 및 gradient 전체의 최악값 계산을 포함한다. 원본 충실도를 위해 전체를 진한 색으로 바꾸지는 않았다. 원본 host 대비를 전부 통과했다고 주장하지 않는다.

scrollWidth/Height 경고는 외부 연결선 pseudo, 동심원, 차트 라벨과 의도된 원본 도형의 외부 확장에서 발생한다. 자동 텍스트 잘림 0과 별도로 기록했다. chip은 가운데 정렬을 확인했고, agenda의 숫자는 chip이 아닌 왼쪽 시작선 표식으로 보았다.

replica/조립본 PNG는 각30장 모두1280×720, 비교 PNG는 각30장 모두2560×720. 요소별 시트는 foundation 포함57폴더×2모드=114 PNG다. 전체 라이브러리 PDF는 모드별185쪽, replica/조립 PDF는 각각30쪽이다. 실제 크기·페이지 수·CSS 동일 바이트·소스 hash는 audit-build.json에 기록한다. ZIP/Git 원격 검증은 상위 통합 작업에서 수행한다.
'''
(V/'review-notes.md').write_text(notes)
