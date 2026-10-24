# 검수 기록 — cutfield

## 범위와 보존

기존 replica HTML·CSS·PNG·PDF는 수정하지 않았다. `replica-freeze.json`의 SHA-256으로 보존 여부를 확인한다. 새 작업은 56개 요소의 전체 CSS, kit/foundation, 새 fixture, 요소 지도와 검수·조립 자료다. 원본 이미지나 replica를 통째로 배경에 깔지 않았다.

## 출처와 해석

- 직접 대응하는 요소의 페이지·bbox·측정 수치는 map.json에 있다. 없는 요소는 추론이라고 명시하며 출처를 꾸며내지 않는다.
- 사진·복잡한 일러스트·로고는 연한 회색 번호 자리로 둔다. 단순 벡터와 연결은 각 소유 요소 또는 foundation이 그린다.
- 이 작업에서 fixture 문구는 새 한국어 업무 내용으로 작성했다. 기존 replica의 판독·추정 문구는 보존했으며 새 원문으로 단정하지 않는다. 이번 작업에서 새로 지어낸 원본 문구는 없다.
- 색은 덱 전체의 역할을 고정해 팔레트 자리로 옮겼다. 기준 라이트/다크 시트는 README 팔레트를 쓰므로 원본의 고유 RGB와 다르다. 조립 비교에는 같은 역할에 원본 근접 팔레트를 공급한다.
- 낮은 대비의 원본 보조색은 읽을 수 있는 깊은 단계로 옮긴다. 밝은 강조면의 on 색은 대비가 높은 ink가 될 수 있어 원본의 흰 글자와 다르다.
- 고정 replica 자체의 글자 맞춤·원본과의 잔여 차이는 유지한다. 조립본의 12×6 양의 그리드 트랙은 bbox를 먼저 계산하며 여러 세로 경계를 여섯 행으로 담는 양자화 오차가 남을 수 있다. layout-before-render.json에 요소별 수치를 기록했다.
- 독립 행별 글꼴 크기·자간, 복합 제목 패널, 계약에 없는 다중 조각 파이 등은 GAPS.md에만 미지원으로 기록했다. 이를 임의의 새 클래스로 우회하지 않았다.

## 검사 방식과 수정

- 각 fixture의 min 이상 지정 크기와 min 자체를 두 모드에서 실제 1280×720 foundation에 배치하고 요소 칸을 여유 포함 잘라 한 줄로 묶었다.
- DOM/Range 경계·가림·멤버 교차·대비·chip 중앙·의사 요소 도형 경계를 검사하고, 실제 PNG를 빈 foundation과 비교해 그림자와 글리프의 칸 밖 픽셀도 검사했다.
- 글꼴은 로딩 상태만 확인하지 않고 실제 자손 및 생성 문자의 CDP 플랫폼 글꼴을 확인했다. Montserrat/Do Hyeon에 없는 한국어·중간점은 허용된 body 글꼴로 교정했다.
- 실제 픽셀 검사에서 발견한 Do Hyeon %의 1–2px 오른쪽 돌출, timeline 강조점·회색 note 면, list/quote 장식 여유를 해당 요소 CSS에서 수정했다.
- 모범 fixture의 데이터·마크업은 보존했다. 원문의 특수문자 별표 아이콘은 비어 있는 Lucide 아이콘으로, 6자 중복 금지와 충돌한 일반 문장 한 구절은 뜻을 유지한 최소 표현으로 바꾼 예외를 구조 감사에 명시했다.
- 담당자가 모든 최종 native 크기 칸을 확인하고 주 담당자가 통합 시트와 페이지 비교를 확인한다. 최종 해시는 validation과 root-final-review.json으로 연결한다.

## 통합 페이지 관찰

- 01: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 02: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 03: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 04: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 05: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 06: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 07: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 08: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 09: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 10: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 12: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 13: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 14: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 11: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.

## 담당 요소별 상세 기록

### review-charts

# Chart element review

## gauge — inferred, no source instance

Source grammar from replicas03/06:28px lower-right chamfers on square-start fields and large light numbers. The new progress rail applies the chamfer to both empty track and actual value, preserving a square start and diagonal finish. Numeric figures use the root-corrected --figure-weight250; small labels use body weight. Roles: --a1 actual, --n-3 remaining track, --ink text.0/64/100% business fixtures use long and short names and keep all text visible. Intrinsic figure width and a reserved name field prevent numeric overflow. Minimum2x2; smaller single-column space cannot sustain the name/figure hierarchy. All six final rows and both native minima atlases viewed. Final60 cases: all eight QA metrics zero, including shape_clipped/chip_alignment; three fixtures copy audit zero.

Final CSS SHA256: cedf506ef41a519a7850be1e1954cdbdda6c069dc5a1e234bb59c4dd11b7edb6.

## Source integration correction — replica04 legend

Direct DOM and native crop inspection found four year keys20XX, not three cost-category names.7x7 squares atx829/863/897/931 y164;8px/400 labels atx837/871/905/939 y159. Palette roles are a1-9/a2/a1/n8. The initial chart-to-text handoff supplied only a bbox, and the text map had mistakenly used the x-axis cost categories as legend keys. Both parent and text owner were told immediately; text owner confirmed and is correcting its map/CSS/fixture. The grouped chart itself remains a gap. The declared145px bbox spans the original35px label boxes; the painted glyph end is tighter. Future explicit chart tones use the corrected legend roles.

## Inferred bullet
Source03/06 supplies the lower-right chamfer and thin large figure. Three neutral qualitative ranges carry a thinner primary actual bar; a straight 1.5px target mark remains independent. The source has no bullet plot, so this is an inferred element rather than a claimed replica extraction. All four fixtures, 70 size/mode renders, both minimum atlases and every fixture row were inspected after the final CSS write. Nine automated geometry/paint/contrast checks and the normalized source-copy audit are zero. Honest minima: single short rows2x2, long note2x3, four-row group4x4; a shorter group row is intentionally unsupported to retain readable notes.

## Inferred sparkline
The source04 rectangular plot marks supply square3px carriers and82.7%-width mini bars; source03's fine straight ending language supplies the one-pixel line and baseline. The default plot uses source04's first deep series role a1-9, while semantic up/down use good/bad. No grouped source chart is flattened or claimed as a mapped sparkline. A smaller-cell probe showed even24 bars remain distinct at1x1; all fixtures therefore declare1x1. All80 final renders, eight fixture/mode rows and both native minima inspected after the palette-role correction. Nine QA checks/copy scan zero.

## Inferred heatmap
Source03/06's bottom-right chamfer, fine straight rules and light250 figures inform this new density contract. The cells use a palette-soft density field and retain actual numerical values; square calendar bounds preserve the chamfered ending. No source heatmap is claimed. All58 final renders, all six fixture/mode rows and native minima viewed; nine QA checks and source-copy audit zero. Smallest reviewed clean minima:3x2 numeric matrix,3x3 long row labels,2x3 six-week calendar.

Heatmap calendar refinement: its lower-right chamfer now occupies15% of each square day cell. The original general-field12px chamfer was too large on20px calendar units. All58 final cases, all final rows and native minima were regenerated and viewed; nine QA checks zero. General matrix chamfers are unchanged.

## Inferred waffle
Source03/06's lower-right chamfer and light250 numerical hierarchy translate to18%-chamfered counted units and a thin centred figure. The complete10–100 unit count determines a ten-column matrix; figures mode draws actual person silhouettes. Explicit series tones follow the corrected source04 legend roles, while the counted main share uses the deck's primary emphasis role. All60 final renders, six mode/fixture rows and native minima viewed; nine QA checks/source-copy audit zero. No source waffle instance is claimed.

## Inferred chart-line
Source04's straight square plot marks, fine rules and13px/650-weight value labels inform a new pure-line contract. The inferred3px square points and one-pixel deep-primary9 line remain separate from the original grouped bars, which stay unexpressible. Values use650 data-label weight rather than the250 headline-figure weight. Mandatory four showcase fixtures retain exact data/markup; new long-period and boundary cases exercise the same layout. All112 final renders, twelve mode/fixture rows and native minima inspected; nine QA checks/copy audit zero, CDP custom fonts loaded without error.

Chart-line contract correction: axis labels now remain nowrap and are thinned solely by own point count and slot width, as README chart quality requires. All point/value data remain visible. The boundary fixture uses the realistic0/28/67/100/93/86 progression, replacing the initial repeating extremes. Updated minima monthly12=3x2, six longer month labels4x2 and long periods4x2. All116 final cases, twelve final mode/fixture rows and native minima regenerated and viewed; nine QA checks, copied fragments and font load errors zero.

Final chart-line:8px shared-token gutters keep value backplates off the L-axis and align the end-label insets. The final whole-file rewrite was rendered again; every light/dark fixture row and native minimum was viewed. All9 geometry/contrast/paint checks and copy checks are zero. Axis labels remain nowrap and are thinned at narrow sizes; all values and points remain.

Radar (inferred, no mapped base):CSS-only wedge sectors draw the full-axis concentric polygon grid, and each series owns its fill and vertex markers. Axis counts3/5/8 and series counts1/2/3 use new Korean business data. The first Tide draft passed geometry checks but its centred side labels crossed near outer vertices; a whole-file rewrite moved side labels outward and capped radius at25cqw/29cqh. Final48 cases, all6 light/dark fixture rows and native minima viewed;9 QA counts0/copy0/font load errors0. Minima2x3,3x3,4x4 reflect readable wrapped names without hiding axes or legends.

Chart-bar inferred (not a mapped grouped chart):full fresh CSS uses source-derived bar end/width/plot-rule/type grammar, with value labels above vertical bars so zero and short bars remain readable. Horizontal variant reserves a real wrapping-name column and an external value gutter. All6 mandatory fixtures retain exact markup/data, plus0/100 and long Korean names. All148 final light/dark cases,16 fixture rows and native minima viewed;9 QA counts0/copy0/font load errors0. Vertical axes remain nowrap and thin dense category labels; no data values are hidden.

Chart-donut inferred:86% hole, thin large figure, deep first accent and straight ruled captions inferred from replica03/06. Exact5 mandatory fixtures plus2 new Korean business fixtures. Groups allocate width and height together; four members use2x2 at a narrow aspect ratio. All126 final light/dark cases,14 fixture rows and native minima viewed;9 QA counts0/copy0/font load errors0. Independent root:size; a donut owned by a donuts root is a normal member using the group container. All figures and names remain visible.

Chart-area inferred from replica04 plot grammar:square3px marks,1px strokes,650-weight values and restrained20% ranked fill. The grouped source plot remains a gap. Four exact mandatory fixtures plus long names and0/100 boundaries;116 final cases,12 light/dark fixture rows/native minima and native crossing/stacked12x6 viewed. Geometry/copy/font checks0. A native-scale visual review found vertical seams where separately clipped wedges met. Opaque stacked wedges now overlap1px; translucent fills isolate each full series and add edge coverage with plus-lighter, expanding only the rectangle while retaining original point boundaries in the polygon. This removes double antialiasing without changing data positions or opacity. Temporary single-fixture proof was replaced by the full116-case final proof.


## Slope — final inferred design
Replica에 직접적인 paired-value 도표는 없어 각 덱의 실제 점·선·라벨 문법으로 새 설계했다. 원본 복합 플롯은 이 요소로 바꾸지 않았다. 각 pair 전체가 두 시점 연결선을 소유하며, dumbbell은 이전=open / 이후=solid 표식과 머리 키를 사용해 감소항목의 의미도 유지한다. 긴 이름 칸을 실제 두 줄이 읽히는 너비로 조정했다. 3·6개 변화, 0/100 경계, 긴 이름의 dumbbell 4개 fixture의 최종 라이트·다크 62칸 전행과 native 최소칸을 확인했다. 자동9항목0, 원문6자 일치0. 자동0은 시각적 동일성을 뜻하지 않는다.


## Scatter — final inferred design
원본에는 산점도/버블 도표가 없어 실제 플롯 점·선·라벨 문법으로 새 설계했다. 값축 두 개의 실제 좌표와 버블 면적 비율을 사용한다. 강조점 하나만 주 강조색, 일반 점은 중립·보조 순위로 조용하게 유지했다. 3/6/24점·0/100축 경계·버블·긴 실제 한국어 이름 총6fixture, 최종 라이트·다크76칸 전행과 native 최소칸을 봤다. 9자동검사0, 원문6자 일치0. 원본 복합 차트는 이 요소로 바꾸지 않는다.


## Waterfall — final inferred design
Replica04의43/52 막대폭비·직각plot·650weight수치 문법에서 absent waterfall을 설계했다. grouped source는gap유지. 실제누적결과에서 다음부유막대까지얇은연결선을그리고 total은0에서시작하며더깊은순위를쓴다. 5fixture 최종66칸 전행/native최소칸양모드검수,9지표0/원문일치0.

### review-readme-quality

# README 품질 기준 확인

- 잘림·겹침: fixture별 정직한 min 이상 지정 크기와 min 자체를 두 모드로 검사했다. DOM/문자 Range·가림·멤버 교차·그려진 픽셀을 확인하고 현재 해시의 9개 QA 집계를 release-audit에 연결한다.
- 대비: 실제 색·배경을 계산해 일반 글자4.5, 큰 글자3 기준을 확인했다. 원본의 흐린 글자나 흰 글자가 기준을 넘지 못하면 팔레트의 깊이 또는 명암 역할을 선택했다. 그러므로 원본 RGB와 일부 on 글자색은 다르다.
- 아이콘: 원/배지 안의 아이콘은 중간 크기(통상50~60%)로 두고 실제 native min에서 확인했다. 텍스트/번호 자체를 icon으로 취급하지 않았다.
- 정렬: 같은 행의 멤버 기준선을 일치시키고 큰 칸과 작은 칸의 콘텐츠 무게 중심을 대조했다. source 자체의 비대칭 배치는 그대로 비율화했다.
- 남은 장식: 연결선은 모든 멤버를 소유하는 요소 안에서 그렸다. 페이지 독립 장식은 foundation으로 분리했다. 장식의 칸 밖 픽셀과 본문 교차를 검사했다.
- 차트: 축/라벨/범례/데이터 표식과 줄바꿈을 native 크기에서 확인했다. 작은 칸에서는 보조 라벨을 솎거나 줄이고 강조를 분명히 했다. 계약이 허용하지 않는 다중 조각 pie를 여러 donut으로 바꾸지 않고 GAPS에 기록했다.
- 한 디자인: 직접 측정한 base/계약 변형을 먼저 만들고, 나머지 계약은 같은 덱의 선·모서리·면·타입 규칙으로 추론했다. 직접 출처와 추론은 ORIGINS에 구별했다.
- 다크 모드: 독립 라이트·다크 팔레트로 모든 최종 크기를 다시 렌더했다. 단순 이미지 반전을 사용하지 않았다.
- 중복 금지: samples의 클래스·구조와 mandatory fixture 형식만 사용했다. 기존 sample의 디자인 CSS를 가져오지 않았고 7개 덱의 독립 소스 수치를 element.css 첫 주석과 description에 연결했다.

각 항목의 최종 상태는 validation/release-audit.json, 요소별 validation/*.json, raster-paint-audit.json 및 실제 sheets PNG를 함께 확인한다. 이 체크리스트는 100% 픽셀 동일성을 뜻하지 않으며 계약 미지원과 공유 글꼴·그리드 차이는 GAPS/review-notes에 남긴다.

### review-root-pages

주 담당자 최종 개별 페이지 대조에서 11의 하단 진한 독립 면 누락을 발견했다. bbox 중심 포함 여부 대신 전체 상자 포함 여부로 수정하여 배경을 foundation에 복구했다. 원본의 흰 timeline 전경은 기존 group.on 계약으로 지정했다. 04/09/11/14의 작은 독립 절단 삼각형은 페이지 장식으로 옮겼으며 중복 corner 장식 목록은 제거했다. 13의 이미지 아이콘은 공식 Lucide handshake, badge-dollar-sign, scan-face로 대체되어 원본과 선 두께/윤곽이 다르다.

### review-systems

# Systems element review

## table

{
  "replica_pages": [
    "09"
  ],
  "source_css_reused": false,
  "final_render_cases": 28,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0
  },
  "cell_text_outside": 0,
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/table/regional-4-pick-num-dark-01.png",
    "build/native-review/table/regional-4-pick-num-dark-02.png",
    "build/native-review/table/regional-4-pick-num-dark-03.png",
    "build/native-review/table/regional-4-pick-num-light-01.png",
    "build/native-review/table/regional-4-pick-num-light-02.png",
    "build/native-review/table/regional-4-pick-num-light-03.png",
    "build/native-review/table/replica-09-dark-01.png",
    "build/native-review/table/replica-09-dark-02.png",
    "build/native-review/table/replica-09-dark-03.png",
    "build/native-review/table/replica-09-dark-04.png",
    "build/native-review/table/replica-09-dark-05.png",
    "build/native-review/table/replica-09-light-01.png",
    "build/native-review/table/replica-09-light-02.png",
    "build/native-review/table/replica-09-light-03.png",
    "build/native-review/table/replica-09-light-04.png",
    "build/native-review/table/replica-09-light-05.png"
  ],
  "decisions": [
    "The source lime header maps to a2 through point-column .pick; the mint header maps to a1. Point body stays page-colored. Explicit empty corner, measured narrow labels, value top inset and open horizontal rules retained. Long narrow text wraps to3lines rather than disappearing."
  ],
  "replica_unchanged": true,
  "known_remaining_differences": [
    "Fixture copy is newly written Korean business content.",
    "Palette is supplied by the preview style and intentionally differs from source colors.",
    "Responsive type is capped at large slot sizes and wraps at narrow sizes."
  ],
  "source_size_comparison": [
    {
      "page": "09",
      "bbox": [
        43,
        367,
        572,
        256
      ],
      "comparison": "build/sourcebox-systems/table-09.png",
      "geometry_qa": {
        "outside": 0,
        "clipped": 0,
        "member_outside": 0,
        "overlaps": 0,
        "shape_clipped": 0,
        "painted_outside": 0
      },
      "source_palette_contrast_only": [],
      "css_sha256": "0337ad2a9d3d65085961234813c7b0700ab16198c5d5d0c8a8cec026ad9f1c09"
    }
  ]
}

## architecture

{
  "replica_pages": [],
  "final_render_cases": 30,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/architecture/layers-3-dark-01.png",
    "build/native-review/architecture/layers-3-dark-02.png",
    "build/native-review/architecture/layers-3-dark-03.png",
    "build/native-review/architecture/layers-3-dark-04.png",
    "build/native-review/architecture/layers-3-dark-05.png",
    "build/native-review/architecture/layers-3-light-01.png",
    "build/native-review/architecture/layers-3-light-02.png",
    "build/native-review/architecture/layers-3-light-03.png",
    "build/native-review/architecture/layers-3-light-04.png",
    "build/native-review/architecture/layers-3-light-05.png",
    "build/native-review/architecture/layers-5-long-modules-dark-01.png",
    "build/native-review/architecture/layers-5-long-modules-dark-02.png",
    "build/native-review/architecture/layers-5-long-modules-dark-03.png",
    "build/native-review/architecture/layers-5-long-modules-light-01.png",
    "build/native-review/architecture/layers-5-long-modules-light-02.png",
    "build/native-review/architecture/layers-5-long-modules-light-03.png"
  ],
  "decisions": [
    "Absent from replica. Stack derives268px panels,28px diagonal cuts and29px gaps from replica05.",
    "The cut is on a layer-owned pseudo surface, so cqh measures the individual layer rather than the full stack;45-degree geometry stays proportional.",
    "The last module reserves one layer-relative cut depth. Character Range corners are checked against the diagonal equation in a supplemental browser audit.",
    "Three-layer fixture minimum3×3; five long layers4×4or3×6. All30final native cases inspected in both modes."
  ],
  "corrections": [
    "Smaller slots exposed a corner intrusion missed by root overflow metrics.",
    "Moved clip from layer to its pseudo face to fix container-unit scope; reserved corner space in the last module."
  ],
  "outside_cut_surface": 0,
  "known_remaining_differences": [
    "Stacked architecture and left name bands are inferred; source05 has square future-state cards.",
    "Palette roles replace original hues; fixtures contain new Korean business text."
  ],
  "token_retarget_pngs_identical": 30,
  "token_retarget_proof": "review/validation/architecture-token-equivalence.json"
}

## matrix-nine

{
  "replica_pages": [],
  "final_render_cases": 28,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/matrix-nine/allocation-9-dark-01.png",
    "build/native-review/matrix-nine/allocation-9-dark-02.png",
    "build/native-review/matrix-nine/allocation-9-dark-03.png",
    "build/native-review/matrix-nine/allocation-9-dark-04.png",
    "build/native-review/matrix-nine/allocation-9-dark-05.png",
    "build/native-review/matrix-nine/allocation-9-light-01.png",
    "build/native-review/matrix-nine/allocation-9-light-02.png",
    "build/native-review/matrix-nine/allocation-9-light-03.png",
    "build/native-review/matrix-nine/allocation-9-light-04.png",
    "build/native-review/matrix-nine/allocation-9-light-05.png",
    "build/native-review/matrix-nine/regions-9-long-notes-dark-01.png",
    "build/native-review/matrix-nine/regions-9-long-notes-dark-02.png",
    "build/native-review/matrix-nine/regions-9-long-notes-dark-03.png",
    "build/native-review/matrix-nine/regions-9-long-notes-light-01.png",
    "build/native-review/matrix-nine/regions-9-long-notes-light-02.png",
    "build/native-review/matrix-nine/regions-9-long-notes-light-03.png"
  ],
  "decisions": [
    "Nine-box absent from replica. Inferred from05s268px cut-corner cards,28px45-degree cuts,29px gaps,28/24px insets and18/16px hierarchy.",
    "Cell-owned pseudo measures cut depth from the smaller cell dimension. Character Range corners checked against the diagonal surface equation in28cases, zero failures.",
    "A deep accent9 ground preserves the source white-face contrast relationship; page-colored axis labels remain readable in both palettes.",
    "Three real labels on each axis; y increases upward. Short minimum3×3; long minimum9×4or4×6. All28native cases directly inspected in both modes."
  ],
  "corrections": [
    "Initial white faces merged into the white foundation. Restored the deep contrast ground and a shared small inner inset without adding furniture or classes."
  ],
  "outside_cut_surface": 0,
  "known_remaining_differences": [
    "The nine-box is inferred and has no source instance; source05 contains future-state cards.",
    "Source ordinal numerals are not invented inside this name/note contract.",
    "Fixture text is newly written Korean business content; small type stops at14/12."
  ]
}

## positioning

{
  "replica_pages": [],
  "final_render_cases": 30,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/positioning/regions-6-long-logo-dark-01.png",
    "build/native-review/positioning/regions-6-long-logo-dark-02.png",
    "build/native-review/positioning/regions-6-long-logo-dark-03.png",
    "build/native-review/positioning/regions-6-long-logo-light-01.png",
    "build/native-review/positioning/regions-6-long-logo-light-02.png",
    "build/native-review/positioning/regions-6-long-logo-light-03.png",
    "build/native-review/positioning/route-4-dark-01.png",
    "build/native-review/positioning/route-4-dark-02.png",
    "build/native-review/positioning/route-4-dark-03.png",
    "build/native-review/positioning/route-4-dark-04.png",
    "build/native-review/positioning/route-4-dark-05.png",
    "build/native-review/positioning/route-4-light-01.png",
    "build/native-review/positioning/route-4-light-02.png",
    "build/native-review/positioning/route-4-light-03.png",
    "build/native-review/positioning/route-4-light-04.png",
    "build/native-review/positioning/route-4-light-05.png"
  ],
  "decisions": [
    "Inferred contract positioning borrows source09 60px competitor circles,86px deep own circle and14px external labels; source09 named axes remain unexpressible.",
    "Both actual low/high endpoint fields are provided with upward high-y coordinates, no ghost axis labels."
  ],
  "corrections": [
    "The short12x3 axis label exceeded its8%-height region by a fraction; width-and-height type guard corrected this. Final30cases all native sizes visually reviewed."
  ],
  "differences": [
    "Actual09 names each axis once, so it cannot map to this endpoint-label contract. New fixture content is independent Korean logistics data; this is an inferred element, not a source replacement."
  ]
}

## roadmap

{
  "replica_pages": [],
  "final_render_cases": 30,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/roadmap/handoff-2-dark-01.png",
    "build/native-review/roadmap/handoff-2-dark-02.png",
    "build/native-review/roadmap/handoff-2-dark-03.png",
    "build/native-review/roadmap/handoff-2-dark-04.png",
    "build/native-review/roadmap/handoff-2-dark-05.png",
    "build/native-review/roadmap/handoff-2-light-01.png",
    "build/native-review/roadmap/handoff-2-light-02.png",
    "build/native-review/roadmap/handoff-2-light-03.png",
    "build/native-review/roadmap/handoff-2-light-04.png",
    "build/native-review/roadmap/handoff-2-light-05.png",
    "build/native-review/roadmap/handoff-4-long-notes-dark-01.png",
    "build/native-review/roadmap/handoff-4-long-notes-dark-02.png",
    "build/native-review/roadmap/handoff-4-long-notes-dark-03.png",
    "build/native-review/roadmap/handoff-4-long-notes-light-01.png",
    "build/native-review/roadmap/handoff-4-long-notes-light-02.png",
    "build/native-review/roadmap/handoff-4-long-notes-light-03.png"
  ],
  "decisions": [
    "Inferred duration surfaces use source05 28/268bottom-right45degree cut,deep a1-9ground and page faces; source12 stepped strategy is not reinterpreted as a roadmap.",
    "Period divisions and milestones are owned by the whole element;18:16label-body hierarchy becomes coupled width/height type guards."
  ],
  "corrections": [
    "Tone1duration text now explicitly uses a1-on rather than inherited ordinary ink; dark reference contrast failure2.4 corrected, then all30cases re-rendered and native cells reviewed."
  ],
  "differences": [
    "No complete roadmap contract exists in Cutfield source. New duration data and owner labels are inferred; source12 strategy layout remains a separate unsupported design."
  ]
}

## matrix

{
  "replica_pages": [
    "05 (inferred language only)",
    "06 (nested list)"
  ],
  "final_render_cases": 28,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/matrix/dispatch-4-dark-01.png",
    "build/native-review/matrix/dispatch-4-dark-02.png",
    "build/native-review/matrix/dispatch-4-dark-03.png",
    "build/native-review/matrix/dispatch-4-dark-04.png",
    "build/native-review/matrix/dispatch-4-dark-05.png",
    "build/native-review/matrix/dispatch-4-light-01.png",
    "build/native-review/matrix/dispatch-4-light-02.png",
    "build/native-review/matrix/dispatch-4-light-03.png",
    "build/native-review/matrix/dispatch-4-light-04.png",
    "build/native-review/matrix/dispatch-4-light-05.png",
    "build/native-review/matrix/swot-dispatch-dark-01.png",
    "build/native-review/matrix/swot-dispatch-dark-02.png",
    "build/native-review/matrix/swot-dispatch-dark-03.png",
    "build/native-review/matrix/swot-dispatch-light-01.png",
    "build/native-review/matrix/swot-dispatch-light-02.png",
    "build/native-review/matrix/swot-dispatch-light-03.png"
  ],
  "decisions": [
    "Source05square268planes,28diagonal notch and18/16hierarchy supply the new quadrant faces. Padding follows28/268of each member shorter side; the cell-content query conversion28/212preserves the notch.",
    "Nested SWOT lists retain the source06thin diagonal arrows and inherit the actual parent reading color."
  ],
  "corrections": [
    "Width-only outer padding consumed the list height in9x4; it now follows the shorter side.",
    "A source-owned list ink override failed on the dark strong fill; the list owner changed unfilled lists to inherit color.",
    "The parent SWOTheading height guard was too strong and made body type larger than the heading at9x4. The Cut SWOTvariant now preserves width scale with a relaxed own-height guard."
  ],
  "differences": [
    "No source quadrant or SWOTexists; axes and semantic4cellstructure are inferred."
  ],
  "supplemental_geometry": "review/validation/matrix-cutbounds.json:28cases0outside-cut glyph bounds"
}

## flowchart

{
  "replica_pages": [],
  "final_render_cases": 28,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/flowchart/dispatch-6-dark-01.png",
    "build/native-review/flowchart/dispatch-6-dark-02.png",
    "build/native-review/flowchart/dispatch-6-dark-03.png",
    "build/native-review/flowchart/dispatch-6-dark-04.png",
    "build/native-review/flowchart/dispatch-6-light-01.png",
    "build/native-review/flowchart/dispatch-6-light-02.png",
    "build/native-review/flowchart/dispatch-6-light-03.png",
    "build/native-review/flowchart/dispatch-6-light-04.png",
    "build/native-review/flowchart/review-loop-4-dark-01.png",
    "build/native-review/flowchart/review-loop-4-dark-02.png",
    "build/native-review/flowchart/review-loop-4-dark-03.png",
    "build/native-review/flowchart/review-loop-4-dark-04.png",
    "build/native-review/flowchart/review-loop-4-dark-05.png",
    "build/native-review/flowchart/review-loop-4-light-01.png",
    "build/native-review/flowchart/review-loop-4-light-02.png",
    "build/native-review/flowchart/review-loop-4-light-03.png",
    "build/native-review/flowchart/review-loop-4-light-04.png",
    "build/native-review/flowchart/review-loop-4-light-05.png"
  ],
  "decisions": [
    "Source-absent flowchart extends replica05 white diagonal-cut faces over a deep accent ground; a2 question state remains the second accent role.",
    "Explicit grid coordinates and all four directional connectors are owned by one root; count changes only2/3 column geometry."
  ],
  "corrections": [
    "Changed the notch from independent13% width/height to equal short-content-side lengths, preserving45-degree cuts at wide-short and narrow-tall ratios."
  ],
  "differences": [
    "Inferred flowchart; source scenes remain unchanged. All18 native panels reviewed after the notch correction; no text hidden."
  ]
}

## swimlane

{
  "replica_pages": [],
  "final_render_cases": 20,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/swimlane/dispatch-3-dark-01.png",
    "build/native-review/swimlane/dispatch-3-dark-02.png",
    "build/native-review/swimlane/dispatch-3-dark-03.png",
    "build/native-review/swimlane/dispatch-3-light-01.png",
    "build/native-review/swimlane/dispatch-3-light-02.png",
    "build/native-review/swimlane/dispatch-3-light-03.png",
    "build/native-review/swimlane/handover-2-dark-01.png",
    "build/native-review/swimlane/handover-2-dark-02.png",
    "build/native-review/swimlane/handover-2-dark-03.png",
    "build/native-review/swimlane/handover-2-dark-04.png",
    "build/native-review/swimlane/handover-2-light-01.png",
    "build/native-review/swimlane/handover-2-light-02.png",
    "build/native-review/swimlane/handover-2-light-03.png",
    "build/native-review/swimlane/handover-2-light-04.png"
  ],
  "decisions": [
    "Inferred swimlane extends replica05 clipped white faces on a deep accent ground,with a2 question and a1 start/end states.",
    "Equal short-content-side corner cuts preserve45-degree geometry; headers reserve40%row height and all explicit arrows share one owning element."
  ],
  "corrections": [],
  "differences": [
    "No source swimlane. All14 final light/dark native panels reviewed; long owner names are retained at8x4 minimum."
  ]
}

## decision-tree

{
  "replica_pages": [],
  "final_render_cases": 18,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/decision-tree/approval-depth-3-dark-01.png",
    "build/native-review/decision-tree/approval-depth-3-light-01.png",
    "build/native-review/decision-tree/route-3-dark-01.png",
    "build/native-review/decision-tree/route-3-dark-02.png",
    "build/native-review/decision-tree/route-3-dark-03.png",
    "build/native-review/decision-tree/route-3-dark-04.png",
    "build/native-review/decision-tree/route-3-dark-05.png",
    "build/native-review/decision-tree/route-3-light-01.png",
    "build/native-review/decision-tree/route-3-light-02.png",
    "build/native-review/decision-tree/route-3-light-03.png",
    "build/native-review/decision-tree/route-3-light-04.png",
    "build/native-review/decision-tree/route-3-light-05.png"
  ],
  "decisions": [
    "Absent recursive tree uses replica05 equal-side diagonal cuts,deep ground,white outcomes,a2 questions and a1 recommendation plane.",
    "Three-question depth honestly requires12x6; simpler three-outcome fixture supports4x3. All answer branches remain literal contract data."
  ],
  "corrections": [
    "Made every question/outcome an own size container so its notch uses its own shorter content side; re-scaled its shared-token type to preserve the intended hierarchy."
  ],
  "differences": [
    "Inferred decision tree. All12 final native light/dark panels directly reviewed; no depth or label hidden."
  ]
}

## journey

{
  "replica_pages": [],
  "final_render_cases": 24,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/journey/intake-3-dark-01.png",
    "build/native-review/journey/intake-3-dark-02.png",
    "build/native-review/journey/intake-3-dark-03.png",
    "build/native-review/journey/intake-3-dark-04.png",
    "build/native-review/journey/intake-3-dark-05.png",
    "build/native-review/journey/intake-3-light-01.png",
    "build/native-review/journey/intake-3-light-02.png",
    "build/native-review/journey/intake-3-light-03.png",
    "build/native-review/journey/intake-3-light-04.png",
    "build/native-review/journey/intake-3-light-05.png",
    "build/native-review/journey/retention-7-dark-01.png",
    "build/native-review/journey/retention-7-dark-02.png",
    "build/native-review/journey/retention-7-dark-03.png",
    "build/native-review/journey/retention-7-light-01.png",
    "build/native-review/journey/retention-7-light-02.png",
    "build/native-review/journey/retention-7-light-03.png"
  ],
  "decisions": [
    "Inferred journey uses source 05 short-side 28/268 diagonal cuts, deep field, white stage planes, and shared emphasis role; no direct journey source exists.",
    "Mood range 0–100 maps to 40–10% of root height; stage content starts at 44%, preserving clearance at the minimum mood.",
    "Seven-stage fixture requires 8x4; all note and pain fields remain visible."
  ],
  "corrections": [
    "Removed note stacking context that caused stage backgrounds to cover names.",
    "Added safe bottom padding before the diagonal cut and retained equal-axis notch dimensions."
  ],
  "differences": [
    "Journey chart is inferred from deck primitives, not a mapped replica element."
  ]
}

## sankey

{
  "replica_pages": [],
  "final_render_cases": 28,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/sankey/nested-4-2-dark-01.png",
    "build/native-review/sankey/nested-4-2-dark-02.png",
    "build/native-review/sankey/nested-4-2-dark-03.png",
    "build/native-review/sankey/nested-4-2-dark-04.png",
    "build/native-review/sankey/nested-4-2-light-01.png",
    "build/native-review/sankey/nested-4-2-light-02.png",
    "build/native-review/sankey/nested-4-2-light-03.png",
    "build/native-review/sankey/nested-4-2-light-04.png",
    "build/native-review/sankey/routes-6-dark-01.png",
    "build/native-review/sankey/routes-6-dark-02.png",
    "build/native-review/sankey/routes-6-dark-03.png",
    "build/native-review/sankey/routes-6-dark-04.png",
    "build/native-review/sankey/routes-6-dark-05.png",
    "build/native-review/sankey/routes-6-light-01.png",
    "build/native-review/sankey/routes-6-light-02.png",
    "build/native-review/sankey/routes-6-light-03.png",
    "build/native-review/sankey/routes-6-light-04.png",
    "build/native-review/sankey/routes-6-light-05.png"
  ],
  "decisions": [
    "Absent Sankey uses source05 exact28/268 short-side notches, deep ground and measured18/16 hierarchy.",
    "Actual minima4x3 flat /6x3 nested retain all fields with thin250 value figures.",
    "Direct and local nested shares multiply on one terminal-row height unit;0% keeps its label without a band."
  ],
  "corrections": [
    "Parent split face spans its full row so the source diagonal cut cannot sever the final outgoing band.",
    "Reduced conservative initial minima after viewing every newly admitted small cell.",
    "Unit glyph uses shared type clamp."
  ],
  "differences": [
    "No source Sankey; proportional flow topology is inferred from measured deck primitives."
  ],
  "supplemental_geometry": "sankey-sharebounds.json:28cases0errors,including exact diagonal-join boundary"
}


### review-text-final-exceptions

최종 지도 문맥/상자 정정

06-prose-1의 실제본문은white이므로foundation_context:on을 추가했다.14 quote는본문ink·저자white의 혼합구조이므로 전체를inverse로 바꾸지 않았다.06-gap-1은frozenHTML의 .block.cut style left795/top205/width389/height411을 읽어 기존근사bbox[801,237,381,380]을[795,205,389,411]로 정정했다. CSS/원본은 변경하지 않았다.

### review-text-transfer-source-owner

# 재인수 추론 요소 최종 검수

사람 소개와 마무리 callout은 원본에 없는 추론 설계다. 두 파일은 기존 범용 초안을 덧붙이지 않고 통째로 다시 썼다. replica05의268px 판과28px 하단 오른쪽 절단,18px/650 이름·16px/1.45 본문 위계를 사용한다. person은 사진에도 같은 절단을 적용하고 왼쪽 이름/설명을 둔다. callout은 같은 흰 면과 절단을 쓰되 단문 결론을 왼쪽에 둔다. 선택 아이콘의9:7 비율은 source13의90×70 기호 비례에서 왔다. 면은page, 읽는 강조는a1-7이다.

person1/2명3x2,3명4x3을 최소 칸으로 결정했다. 3명4x2는 글자가 넘고3x3은 이름·문장이 지나치게 잘게 나뉘어 제외했다. callout은 의무3개와 새 비즈니스 문장2개 전부3x1에서 실제로 읽혀 min을3x1로 정정했다. 의무 fixture는 데이터/마크업을 유지하고 min만 실측으로 바꿨다.

마지막 수정 뒤 라이트·다크 전체 시트를 다시 렌더했다. 모든 칸의 텍스트를 원래 픽셀 크기의 조각으로 읽었고, 전체 시트에서 정렬·면·사진 자리를 함께 확인했다. 모든9 QA0, 실제 raster 칸 밖 번짐0, 실제 로드된 Pretendard 글리프 확인. 원본7덱과6자 이상 같은 문구 자동 검사283 fixture에서0건이다. 이5개는 원본 인스턴스 재현을 주장하지 않으며 기존 source38 동결은 변경하지 않았다.

- person: 56칸 / min team-three=4x3, profile-one=3x2, team-two=3x2
- callout: 100칸 / min callout-icon=3x1, callout=3x1, review-icon=3x1, decision-long=3x1, callout-stack=3x1

### review-text-transfer-systems

# Systems element review

## agenda

{
  "replica_pages": [],
  "final_render_cases": 20,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/agenda/agenda-five-dark-01.png",
    "build/native-review/agenda/agenda-five-dark-02.png",
    "build/native-review/agenda/agenda-five-dark-03.png",
    "build/native-review/agenda/agenda-five-light-01.png",
    "build/native-review/agenda/agenda-five-light-02.png",
    "build/native-review/agenda/agenda-five-light-03.png",
    "build/native-review/agenda/agenda-four-dark-01.png",
    "build/native-review/agenda/agenda-four-dark-02.png",
    "build/native-review/agenda/agenda-four-dark-03.png",
    "build/native-review/agenda/agenda-four-light-01.png",
    "build/native-review/agenda/agenda-four-light-02.png",
    "build/native-review/agenda/agenda-four-light-03.png"
  ],
  "decisions": [
    "No agenda source; source05 supplies268-square28-cut cards,54/250 index at34/28 inset and18/650 plus16/400 lower text.",
    "The actual source lower text group remains bottom aligned below the upper index; cut follows the member short side.",
    "Full new business notes remain visible at minima6x4|4x6 and8x5|6x6."
  ],
  "corrections": [
    "Replaced generic centered number/text rows and fixed28px notch with source-based whole-file CSS.",
    "Replaced truncated ellipses with complete new sentences and included one long heading."
  ],
  "differences": [
    "Inferred agenda; original has no direct contents list."
  ],
  "supplemental_geometry": "agenda-transfer-raster.json:20cases0visiblebleed; all20cells/12nativepanels personally reviewed"
}

## metric

{
  "replica_pages": [],
  "final_render_cases": 44,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0,
    "chip_alignment": 0,
    "shape_clipped": 0,
    "painted_outside": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/metric/metric-bare-dark-01.png",
    "build/native-review/metric/metric-bare-dark-02.png",
    "build/native-review/metric/metric-bare-dark-03.png",
    "build/native-review/metric/metric-bare-dark-04.png",
    "build/native-review/metric/metric-bare-dark-05.png",
    "build/native-review/metric/metric-bare-light-01.png",
    "build/native-review/metric/metric-bare-light-02.png",
    "build/native-review/metric/metric-bare-light-03.png",
    "build/native-review/metric/metric-bare-light-04.png",
    "build/native-review/metric/metric-bare-light-05.png",
    "build/native-review/metric/metric-extended-dark-01.png",
    "build/native-review/metric/metric-extended-dark-02.png",
    "build/native-review/metric/metric-extended-dark-03.png",
    "build/native-review/metric/metric-extended-dark-04.png",
    "build/native-review/metric/metric-extended-dark-05.png",
    "build/native-review/metric/metric-extended-light-01.png",
    "build/native-review/metric/metric-extended-light-02.png",
    "build/native-review/metric/metric-extended-light-03.png",
    "build/native-review/metric/metric-extended-light-04.png",
    "build/native-review/metric/metric-extended-light-05.png",
    "build/native-review/metric/metrics-three-dark-01.png",
    "build/native-review/metric/metrics-three-dark-02.png",
    "build/native-review/metric/metrics-three-dark-03.png",
    "build/native-review/metric/metrics-three-dark-04.png",
    "build/native-review/metric/metrics-three-light-01.png",
    "build/native-review/metric/metrics-three-light-02.png",
    "build/native-review/metric/metrics-three-light-03.png",
    "build/native-review/metric/metrics-three-light-04.png"
  ],
  "decisions": [
    "Source03 measured100px evidence figures are300 weight, not250. Names17/650 and notes17/400. Preserve horizontal hierarchy with36.40625% index region; actual stat under400px becomes vertical."
  ],
  "corrections": [
    "Fresh bare implementation removes card/chamfer assumptions; added stats3 fixture and actual-member containers/dividers. All full copy remains.",
    "Final divider painter stops at last real division to prevent rounding-induced edge line. Final stats10 cases rerendered and directly reviewed;34 unchanged nonstats PNG hashes match previously reviewed images."
  ],
  "differences": [
    "Bare contract has no containing colored face; source evidence tile is therefore a typography/layout reference only."
  ],
  "supplemental_geometry": "44 final cases9QA0/raster0/copy0;28 native panels directly reviewed, final10 stats cases re-reviewed,34 nonstats exact PNG identity."
}


### review-text-transfer

# Transferred inferred elements — final review

pill: source05 chamfer를 작은캡슐의하우측14~16px사선과직접그린경계선으로옮겼다. 한줄nowrap/높이비례padding. min3x1/4x1,78칸전행/native최소칸양모드검수,9QA0/원문6자0/폰트로드0.
tag: 실제prose 안의 inline/hl이므로 자연폭span과 box-decoration-break를유지했다. inline의size containment는브라우저상비활성이나선언은유지하며부모prose의size컨텍스트를사용한다. min2x1까지정직하게검증,40칸9QA0/원문6자0.

tag 최종: 짧은 라벨 전체를 nowrap으로 유지하여 chamfer deck의 간결한 표식이 줄 사이에서 분리되지 않게 함. 본문의 highlight는 자연 줄바꿈 유지.

### review-text

# Text element provenance and review decisions

The fixed replicas were read as evidence and were never edited. Sample HTML supplies mandatory data/markup only; no sample element CSS was read or reused.

## Per-leaf provenance

- card: 05:base, 05:variant:.on, 05:variant:.tone-2, 05:variant:.quiet, 03:same-as:05, 08:same-as:05, 13:same-as:05.
- pill: inferred; no independently expressible source instance.
- callout: inferred; no independently expressible source instance.
- tag: inferred; no independently expressible source instance.
- list: 06:base.
- quote: 14:base.
- headline: 02:base, 04:variant:.center, 06:same-as:02, 13:variant:.big.
- prose: 02:base, 03:same-as:02, 04:same-as:02, 05:same-as:02, 06:same-as:02, 07:same-as:02, 08:same-as:02, 09:same-as:02, 10:same-as:02, 11:same-as:02, 12:same-as:02, 13:same-as:02.
- metric: inferred; no independently expressible source instance.
- agenda: inferred; no independently expressible source instance.
- person: inferred; no independently expressible source instance.

## Recorded corrections and decisions

- Source06 arrow was initially interpreted as a filled diagonal marker; actual CSS38px box/37×1.5px stem/26px open head now directly redraws that shape.
- Source04 legend was initially confused with the x-axis three categories. Actual source has four20XX keys,7px squares,8px type,-.45px tracking,34px pitch. Palette ranks:a1-9,a2,a1,n8; extension5n5. Bbox145px includes the35px DOM label boxes throughx974.
- Quote14 original93×64 Q-curve quotation is drawn with percentage CSS shape(), with no URL.49px/400 text,35px square image,26px attribution,2px rule and17px split contact are owned by quote. The first SVG-mask draft violated the no-url rule and was replaced before completion.
- The quotation scales against width and height so its sign cannot cover the first line in12x6.
- Headline02 actual SVG type42.391/550 on50px lines,−3.428px tracking;26px statement on28.6px lines and11.48px gap now reconstructs native positions to0.04px.04/06 are39.474px;13 big has source42.857/41.489px fitted lines, represented by42.173px mean with the small residual disclosed. Reading emphasis is a1-7 for palette contrast.
- Source03 common figure panel follows the actual middle band:fig left42/top63,100px type;name left275/top75 and note top101 at17px. The irregular first+23/last+5px metadata offsets and the next-band chamfer underlays are explicit partial gaps, not ordinal CSS.
- Checked lists have their own compact transparent variant. Actual source06 arrow geometry and base spacing remain unchanged; low nested cells use12px normal leading and inherited inverse color.

## Inferred elements

pill, callout, tag, metric, agenda, person. Each has its own build/inferred-spec-<leaf>.json citing this deck’s measured source primitive, an inferred description and fresh business fixtures. These files never claim a source base.

## Validation state

Browser sheets and probes are recorded in review/validation and build/probes. A zero automated result alone is insufficient: native source-box comparisons found and corrected font, gap, shape, padding-reference, missing-avatar and quotation collisions. Each final proof must match the latest source hashes. Final fixture minima are selected after native smaller-candidate review; initial conservative comments are not final evidence.

True inline tag/hl boxes keep natural text width. Declared container-type:size is inert on a non-atomic inline by browser definition; shared type steps and the enclosing real prose paragraph provide context. This explicit functional limitation is not hidden with an invented fixed8em box.

### Final integration corrections
- Checked-list rotated ticks were translated within their own marker carrier to remove actual raster paint beyond the left cell boundary; text, palette roles and minimum cells are unchanged.
- Quote attribution in350–480px tall cells anchors6px above the bottom, preserving the actual taller source14 layout and preventing glyph paint beyond9x4.

### 주 담당자 페이지 대조 기록


- 최종 확인: Filament04의 오른쪽 Confidential 레일은 동결 replica 자체가 붉은 글자를 붉은 면에 놓아 보이지 않는다. 동결본의 색 역할을 보존했으며 원본의 흰 레일과 차이를 남긴다. Cutfield13 밝은 tone 면의 글자와 icon은 대비를 위해 palette on 역할로 바뀌며 원본 흰 글자와 다르다. Toggle06의 12×6 행 양자화는 사진 3개 사이의 세로 공백을 줄인다.

- Portico02: 10개 목차는 계약 agenda 최대8개와 충돌하여 전체 인스턴스를 미지원으로 기록했다. 8+2개의 다른 요소로 쪼개 겉모양을 속이지 않는다. 빈 조립 영역은 누락 사고가 아닌 명시된 계약 한계다.
- Portico03/04: 넓은 수평 사진띠는 frame의 seat 종횡비 제한과 충돌해 미지원으로 기록했다. source gray 사진 자리를 임의의 가로 왜곡 frame으로 대체하지 않았다.03/04의 작은 방사형 도상은 계약 mark의 단순별로 근사해 원본6점과 다른 잔차가 있다.
- Portico05: 각 사진 자리의 번호는 계약 독립 frame이 자기 seat부터1로 센다. 여러 요소 사이 전역 순번1·2·3은 계약 데이터 슬롯이 없어3개1로 보인다.

- Lamella07: 위쪽 오른쪽 한 모서리만 휜 흰 cap 둘은 양 모서리가 휜 headline base와 달라 계약 변형에 대응하지 못한다. 그림은 임의 변형으로 우회하지 않고 GAPS에 기록했다. 본문과 독립 가로 괘선은 source 수치·반전 문맥을 복구했다.

- 최종 통합:392요소의양모드크기시트와87페이지비교PNG를주담당자가모두열어확인했다. 최종source문구추출정정후Rule13의3개카드본문은source의3줄구조를되찾았다. Lam18의1개quote본문3→4줄은독립tracking차이로잔차를명시했다.
- 최종grid검사:87페이지/231개최상위요소/543쌍에서source분리요소의신규교차0,정수span과양수12×6tracks오류0. Lam23의5.68e-14px중복경계를1e-6px허용오차로합쳐양수트랙을복구했다. 원본에이미있던교차11건은구별해기록했다.

