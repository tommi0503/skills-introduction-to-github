# Crossrail Round5 보고

2026-10-25. `ROUND5-USER.md`가 과거56개 완전성·단일디자인·폐쇄부품 규칙보다 우선한다. 원본 및 불변 replica 파일은 수정하지 않았다. 원본 문구는 조립 검증 페이지에서만 사용한다.

## 1. 새 디자인 폴더

- `card--numeric-capsule` ← 22쪽
- `card--open-rule` ← 12쪽
- `card--quiet-sheet` ← 05쪽
- `card--rank` ← 21쪽
- `card--tab` ← 11쪽
- `chart-bar--annotated` ← 23쪽
- `chart-donut--pie` ← 24쪽
- `chart-line--reference-columns` ← 22쪽
- `hub--orbit` ← 17쪽
- `hub--pentagon` ← 18쪽
- `hub--semicircle` ← 07쪽
- `pill--stacked` ← 27쪽
- `positioning--trajectory` ← 29쪽
- `prose--marked` ← 18쪽
- `steps--reverse` ← 14쪽
- `steps--separated` ← 14쪽
- `steps--vertical` ← 13쪽
- `table--calendar` ← 27쪽
- `table--row-focus` ← 20쪽, 29쪽

기존 `card`는09/21쪽의 수치·이름·아래 설명 형태로 새로 썼다. 백색 장문 시트05, 열린 큰 문자·규칙선12, 오른쪽 문구 탭11, 원형 순위 배지21은 각각 독립 디자인이다. 연결 쉐브론10은 한 루트가 모든 멤버와 노치를 소유하며, 수직 캡슐13·분리14·역방향14와 분리했다. 각 신규 파일은 완전한 CSS 원문으로 작성했다.

## 2. 패널과 페이지 장치

- 05: x502부터 시작하는 전체 높이 강조면은 foundation `vector.field-right`다.
- 07: 두 쌍의 ruled heading+paragraph 패널, 가운데 반원 peer 도해를 `panel.peers`로 조합했다.
- 11: 두 카드 스택 사이 연속 세로선은 `panel.columns` 소유다.
- 17: 네 enclosing panel과 가운데 orbit은 foundation `panel.quadrants`와 별도 도해 루트로 조합했다.
- 18: 연한 제목 띠, 단일 표시 문단, 오각형을 조합했다. 전체 실제 내용은 y226–655다. 이전260 시작 분류를 고쳐 `page.compact` body y226 및 `stack.offset`/`middle.tall` 비율로 재추출했다.
- 19: 두 제목 띠·연결 화살표·연한 본문판을 `panel.comparison`이 소유한다. 내부 pill/prose/list의 의미는 그대로다.
- 21: rank와 네 수치 카드를 `panel.summary`로 묶어 과거 정수 그리드 충돌을 없앴다.
- 27: 두 날짜 capsule 아래 pale heading+checklist는 `panel.schedule`이다.
- 30: 이미 지원하는 closing foundation을 유지한다.

`panel-peer-explanations.html`과 `panel-impact-comparison.html`은 새 업무 문구로 만든 독립 크기별 패널 fixture다. 패널은 페이지 전체를 요소로 숨긴 것이 아니라 foundation의 wrapping/layout이며 내부에는 독립 계약 요소가 있다.

## 3. 차트 확장과 데이터 판단

- 22: `chart-line--reference-columns`는 한 루트 안에 실제 선의7값/요일/제목/축과 두 연한 참고 기둥을 소유한다. 공개 max6000과5,000/4,500/4,000/5,000/4,800/5,000/5,200을 보존했다. 기둥은 실제 수치가 판독되지 않고 선의 축보다 크게 그려져 있다.7864 같은 역산값을 공개 막대 수치로 만들어 내지 않았다. 대신394px 높이 안의166px·302px을42.13%·76.65% private background height로 기록했다. 이 부분의 독립 데이터 scale은 불명확하다.
- 23: `chart-bar--annotated` 각 막대가 실제80/100, 외부 숫자 capsule, 이름, 설명을 소유한다. 제목 아이콘과 축 이름도 같은 루트 안이다. 큰 칸에서도 원형 label은 동일한 min(cqw,cqh) 지름을 쓴다.
- 24: `chart-donut--pie`는 five `.slice` 20/25/15/10/30 합100을 보존한다. 각 `--crossrail-slice-start`는 이전 `--v` 합이며 회전과 리더의 일반 수학 데이터다.0–100 정규화/연속 시작/합100을 검증한다. 조각 이름·값·중앙 문구·연결선을 한 루트가 그린다.
- 26: roadmap의 pale range는 해당 lane 내부 `.range`로 복구했다. 기존5개 bar의 from/to와 공개 문구는 유지했다.
- 27: 달력은 실제7열 table이다.15–20 선택 구간과 event part를 date cell이 소유한다. 기간 문구가 다음 칸의 바탕에 가려지던 paint-order 회귀를 z-index로 고친 뒤 native min PNG에서 전체 문구를 확인했다.
- 29: source trajectory는 positioning의 own part로 원 뒤에 그린다.

## 4. 지운 일반 요소

실제 원형이 없었던 일반 폴더:

`architecture`, `balance`, `bullet`, `callout`, `chart-area`, `chart-donut`, `chart-scatter`, `chart-stack`, `chart-waterfall`, `code`, `concentric`, `cycle`, `decision-tree`, `delta`, `flowchart`, `gauge`, `heatmap`, `hierarchy`, `hub`, `journey`, `logo-group`, `matrix`, `matrix-nine`, `mindmap`, `network`, `person`, `pricing`, `quote`, `radar`, `sankey`, `slope`, `sparkline`, `swimlane`, `treemap`, `venn`, `waffle`

기존 `metric`의 bare 수치 원형은 원본22의 capsule 카드로, `positioning`은 trajectory 디자인으로, `versus`는 실제 두 면과 제목을 묶는 foundation 패널로, `chart-line`은 reference-column 디자인으로 대체했다. 이는 원형 자체를 삭제한 것이 아니다. 기본16형과 독립 추가19형, 총35디자인을 남겼다. 카드의 미관측 icon-row 기본 예시, 미관측 수평 bar·수직 timeline·inline highlight 예시는 제거했다. 실제 source별 길이를 가진 fixture와 같은 디자인의 새 업무 문구만 검수한다. 공통 registry state는 선택이므로 과거 golden28을 필수인 것처럼 유지하지 않았다.

## 5. 잔여 GAP와 차이

진짜 계약 미표현 GAP는0이다. 과거34항목은 독립 디자인, 패널, 확장 데이터 또는 부모 부품으로 복구했다. 단일 marker5개는 `prose--marked`의 표시 부품이며 ignoredResidue에 과거 독립 분류를 기록했다. 측정983개는 한 번씩만 소유된다.

다음 차이는 GAP로 부풀리지 않는다.

- 12×6 body 정수 배치의 양자화로 일부 개별 root의 시작/폭이 수 px에서 수십 px 달라진다. 내부 기하는 해당 root 비율에 맞춰 반응형으로 변한다. 문구나 수치를 줄여 맞추지 않았다.
- Noto Sans KR의 허용 굵기·타입 스텝과 짧은 칸의 반응형 타이포 때문에 원본과 미세한 줄바꿈·ink 폭 차이가 있다. 불변 replica의 추정 오차도 그대로 보존한다.
- 원본 아이콘은 가까운 실제 Lucide로 대체했다. 사진·복잡한 그림은 원 요청대로 연회색 placeholder다.
- 참고 기둥22의 데이터 scale은 확정하지 않았다. 차트 눈금의 천 단위 쉼표 등 생성 눈금 서식은 읽힘을 유지하는 일반 수학 표기다.
- 외부 `assets/source-palette.css`는 원본의 색 자리를 공급한다. 공식 light/dark 시트는 이 파일을 사용하지 않는다. 원본의 낮은 대비(예:26쪽 중간톤+흰 글자,30쪽 회색 kicker)는 source 비교에서 기록하고, 공식 팔레트 검사는 별도로 통과한다.
- 머리말의 작은 해칭과 극히 미세한 선 끝·자간은 완전한 픽셀 동일을 주장하지 않는다.

## 6. 실제 확인한 출력

- `sheets/<35개 실제 폴더명>-light.png`, `-dark.png` 전부를 각각 열어 최소 칸부터 허용된 큰 칸까지 확인했다. 마지막 원형 회귀를 발견한 semicircle, annotated bar, calendar는 수정 후 양모드를 다시 열었다.
- `sheet-cells/table--calendar--monthly-window-1--light--6x4.png`에서 기간 문구 전체가 그려지는 것을 native로 확인했다. 길이가 긴 prose03와 quiet card05, 원형 도해, 연결 선·capsule의 source-sized native도 따로 확인했다.
- `panel-sheets/foundation-panels-light.png`, `-dark.png`를 열었다. 패널은 각 fixture/min을 만족하는 모든 크기의 실제 grid crop이다.
- `foundation-sheets/cover-{light,dark}.png`, `seat-{light,dark}.png`, `closing-{light,dark}.png` 및 패널 fixture 전체 페이지를 확인했다.
- `compare-reassembled/slide_01.png`부터 `slide_30.png`까지 각 original|immutable replica|assembly 비교를 각각 별도로 열었다. 마지막 수정 뒤의 최종 source FP 및 page HTML SHA 일치는 `round5-final-review.json`, `reassembly-checks.json`에 기록한다.

모든 native PNG를 개별 수동으로 읽었다고 주장하지 않는다. 전35 양모드 매트릭스를 직접 보고, 자동 검사 및 실제 source/native 표본을 결합했다. 최종 자동 수량과 SHA는 `round5-final-review.json`이 기준이다.

### 마지막 원본 조립 실물에서 바로잡은 항목

- 05의 원본 white sheet는 y98–622, body는 [95,98,1090,524]다. 이전 정상 head/body의 y260 시작에 넣었던 최초 foundation 분류 오류로 원문이 바닥을 넘쳤다. 페이지 장치 `page.side-heading`을 정의하여 헤더와 독립된 동시 상단 본문을 받게 했고, 기존 정수 열3/6/9는 유지했다. quiet-sheet의 여백과 타이포는275×524 실제 원형에서30.2% kicker/44.1% name/62% note로 다시 추출했다. 별도 foundation fixture도 추가했다.
- 11의 넓은 오른쪽 문구 탭은 `card--tab`,12의 큰 문자와 가로 규칙선은 `card--open-rule`다. 마지막 원본 대조에서 두 요소의 소유가 뒤바뀌어 있음을 발견해 map/fixture/data-el을 바로잡았다. 원문·처음 grid는 보존했다.
- 13 수직 steps의 이름·순번은 inverse 바탕에서 페이지 잉크를 상속하며, 흰 아이콘 면의 기호만 accent 잉크를 쓴다. navy 잉크 강제로 원문 일부가 바탕에 묻힌 회귀를 제거했다.
- 위 수정 후05/11/12/13 비교 PNG를 다시 각각 열어 확인했고, 전체 retained 시트와30장 및 foundation/panel을 같은 최종 fingerprint로 다시 렌더했다.

추가 foundation `side-heading-{light,dark}.png`를 별도로 확인했다. closing kicker는 page 역할을 쓰도록 선택자 우선순위를 교정했다(기존 sidebar kicker의 n3 override를 제거한 것이며 새 색은 없다). 최종 기초12장/패널8칸/요소35형과 조립30장은 같은 최종 fingerprint로 갱신했다.

최종 own-root 자동 확인에서 원문17의3행 문단이2px 위로 넘어가는 glyph,23의둘째주석열22px 초과,29의마지막표행18px 초과를 추가로 발견했다. 작은높이prose의일반폰트상한,annotated source column48.3/74.3%,표높이에따른padding으로보정했다. 페이지grid·원문·수치·부품수는그대로다.

section cover25의 원형 진행 표시는 source 측정(1160,592,37,37)과 그 내부 chevron을 소유한 foundation `deco`의 두 pseudo로 복구했다. 좌측 세로 rail 역시 같은 section-cover page 장치다. 원본 없는 새 문구의 section foundation fixture를 추가해 이 장치도 양모드 실제 출력 검수에 넣었다. 최종 foundation은7fixtures×2=14장이다.

09/21의 기본 수치 card는 width 비례만 적용하면 같은 높이의 넓은 카드에서40/26/18px 원본 타이포가53/35/24로 커졌다. own height 비례 상한21.3/13.83/9.57cqh를 함께 적용해 같은 높이의 두 원형을 보존했다.

최종확정 FP: `eb1a60b74fb695f2aa7c3f322f52c3995a36a9634241b505b2a587e7d46389ba`.35디자인/152fixture/2178요소칸/14foundation/8panel/30조립이모두현재다. 요소·기초·패널의자동후보는모두0이며조립은폰트/요청/영역초과/잘림/겹침0이다. 조립sourcepalette의낮은대비90후보는원본색재현조건으로별도보존한다. 원문568누락0,replicaSHA불변.

최종 출처 계약 마감:35개 element.css 첫 주석을 각각 실제 replica 페이지와 디자인 설명으로 맞췄다. 시각 선언 본문SHA35개 및 브라우저 CSSOM664규칙은 완전히 동일하다. 재렌더한 조립60 PNG/기초14/패널2는 이전PNG SHA와 모두 같다. 전체2359개 현행PNG 중2348개 SHA는 동일하며,캡슐native8개와그매트릭스3장의byte SHA는다르다. 해당8개native를각각열어본문·형태·정렬변화없음을확인했고,별도반복legend시험에서외곽AA1픽셀변동을관측했다. 이전baseline은SHA만보존했으므로11개전부의정확한이전pixel차이를안다고주장하지않는다. 증거는comment-only-source-change.json/comment-only-cssom-proof.json/comment-only-visual-proof.json이다. 삭제디자인chart-bar--combo의고아시트2개는/tmp에보존이동했다.
