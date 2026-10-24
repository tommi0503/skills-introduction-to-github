# 검수 기록 — tide-tab

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

- 05: Three-way source comparison inspected at native size. Panel/tab sizes, title and body positions, U connector and hub geometry follow the frozen replica. Neutral image placeholders and numbered seats are intentional. Readable palette roles deepen captions/core and choose the palette on-colour for icons and tabs; these colour/contrast differences remain explicit.
- 06: Three-way source comparison inspected at native size. Panel/tab sizes, title and body positions, U connector and hub geometry follow the frozen replica. Neutral image placeholders and numbered seats are intentional. Readable palette roles deepen captions/core and choose the palette on-colour for icons and tabs; these colour/contrast differences remain explicit.
- 07: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 08: 원본·고정replica·조립본 직접 비교. 07 일정 패널의 역방향 화살표/외부 담당자/제목 래퍼,08 혼합 세 강조의 대제목은 계약 미지원으로 GAPS에 분리. 08 본문·inline hl은 소스 재구현. 6행 그리드 양자화로 마지막 callout의 세로 중심 약40px 하강하며 페이지별 CSS로 보정하지 않음.

## 담당 요소별 상세 기록

### review-charts

# Chart element review

## gauge — inferred, no replica instance

Measured grammar: replica05 panels are779x209, with0/21/21/21px corners and a pale shadow; the deck uses primary/secondary accents and a two-rank footer band. This new meter uses that panel silhouette, an inset supporting shadow to keep all paint inside its slot, a pale rounded rail and primary-to-secondary fill. Source gauge provenance is absent: this is an explicit inferred design, not a source base. Roles: panel --page; track --a1-1-soft; fill --a1/--a2; body --ink; figure --a1-7 for4.5+ contrast at small type. Figure font/weight follows the strong source hierarchy.

Three new business fixtures test0/64/100%, member text lengths and completion states. At2x2 the first render exposed100% overflowing its fixed field. The whole CSS was rewritten with an intrinsic figure width and a larger gap reserved from the name field. No number or name is hidden. All six final fixture rows and both native minimum atlases were viewed. Final60 cases: all seven QA metrics zero, including chip_alignment;3 fixtures copy audit zero. The2x2 minimum preserves22px figures and14px names; a single-column allocation cannot fit the name/figure hierarchy.

Final CSS SHA256: 16aeb228e6a41ccf8bce08a1cbbaa325f541de1c755770af344328a0fe46e5aa.

## bullet — inferred, no source instance

The replica05 page-panel grammar is adapted to an actual/target measure: three ordered primary-soft bands, a thinner actual a1 fill and an a2-8 target tick. The panel retains its square top-left and three rounded21px corners. This is a new semantic component, not a source base. Figure text uses a1-7, supporting copy n-7, panel page. Target notes are real Korean business sentences; no note, number or name is hidden. Single0/100 states use2x2 minima, the long note2x3, four members4x4. An initially proposed5x3 group passed automatic bounds but its note sat too close to the lower border, so it was rejected on visual comfort rather than retained as a passing minimum. All eight final fixture rows and both native minimum atlases viewed. Final70 cases: all nine QA metrics zero, including painted_outside; four fixtures copy audit zero.

Final CSS SHA256: 7374db7c7f8baf7542a9ffd7bab06949decb099f5cfb05fcf3057a4b76588289.

## Inferred sparkline
Source05's white0/21px panel, round carriers and thicker connector grammar supplies the axis-free sparkline; a new point line is not a mapped source plot. The point set owns every connector through scoped anchors. Bars use rounded tops and a pale-to-solid primary field. Semantic up/down uses good/bad roles. All80 final size/mode renders, every fixture row and native minima viewed; nine checks/copy scan zero. Short axis-free trends remain readable at1x1; twelve-point and24-bar fixtures use2x1.

Sparkline minimum refinement: both the12-point line and24-bar trend were tested at1x1 and remained distinct. Their declared minima were lowered from2x1 to1x1; all80 final renders and both updated minimum atlases were regenerated and viewed. This supersedes the earlier two minima only.

## Inferred heatmap
Source05's0/21px white panel corners and pale accent carrier fields inform a new data-density matrix. Values remain ink on a page-to-primary-soft density mix; no source heatmap instance is claimed. Calendar cells retain square bounds, using the same three rounded corners. An initial calendar overflow exposed differing cqh references between the size-container root and its children: layout was rewritten as a column flex stack so all head/side measurements resolve in children against the same root. Final58 size/mode renders, every mode/fixture row and native minimum atlases were viewed; nine QA checks and source-copy audit zero. Minima were reduced by actual review to3x2 for the3x5 matrix,3x3 for long labels and2x3 for six weeks; shorter calendar heads use concise week labels to preserve the square matrix.

Heatmap calendar refinement: the small calendar cells now cap their three rounded corners at20% of their own side. The earlier21px arcs made tiny day cells too close to circles; square bounds alone were not enough to preserve the calendar contract visually. All58 final cases and all final rows/minima were regenerated and viewed; nine QA checks remain zero.

## Inferred waffle
Source05's round carriers, paired accent roles and prominent numerical hierarchy inform a new counted-share contract. Unit count10–100 determines a complete ten-column matrix, with square unit bounds fit to both slot dimensions. Figures mode uses actual head/torso/arm/leg CSS pictograms, not font symbols;20 people show12 counted members. All60 final renders, six fixture/mode rows and native minima viewed; nine QA checks/source-copy audit zero. The100-unit circle matrix remains distinct at1x2; two-share and person fixtures require2x2 to keep full figures/person shapes clear. No source waffle instance is claimed.

## Inferred chart-line
Source05's0/21px white panel, round carriers and pale thick connectors inform a new equal-step plot. The complete point set owns its3px line; selected points use the paired secondary carrier role. Mandatory four showcase fixtures preserve their exact data/markup. New Korean business periods and0/100 boundaries stress the same design. Visual/automatic review found three-line long labels outside the initial4x2 slot: their honest minimum became5x2, and ordinary month-label boxes gained a small amount of width to keep10–12월 intact. A tiny page backplate behind values prevents steep boundary segments from crossing glyphs. All112 final size/mode renders, all twelve fixture/mode rows and native minima inspected; nine QA checks/copy audit zero. CDP records actual custom Pretendard use with no load errors. This pure-line contract has no source instance.

Chart-line contract correction: README chart quality requires axis-label thinning rather than wrapping. Axis spans are now nowrap, with own-member-count-based sparse labels below700px; every value and point stays visible. The initial deliberately alternating boundary fixture was replaced with the natural0/28/67/100/93/86 business progression to satisfy the explicit no-repeating-sawtooth rule. New minima monthly12=3x2, six longer labels4x2 and long periods4x2 supersede earlier line minima. All116 final renders, twelve final mode/fixture rows and native minima were regenerated and viewed; nine QA checks, copied-source fragments and font load errors zero.

Final chart-line gutter: an8px shared-token inline plot inset keeps value backplates from breaking the L-axis and gives the first/last sparse axis labels the same alignment inset. All116 final cases, twelve mode/fixture rows and native minima regenerated and viewed; nine QA checks, copy fragments and font load errors remain zero.

Final chart-line:8px shared-token gutters keep value backplates off the L-axis and align the end-label insets. The final whole-file rewrite was rendered again; every light/dark fixture row and native minimum was viewed. All9 geometry/contrast/paint checks and copy checks are zero. Axis labels remain nowrap and are thinned at narrow sizes; all values and points remain.

Radar (inferred, no mapped base):CSS-only wedge sectors draw the full-axis concentric polygon grid, and each series owns its fill and vertex markers. Axis counts3/5/8 and series counts1/2/3 use new Korean business data. The first Tide draft passed geometry checks but its centred side labels crossed near outer vertices; a whole-file rewrite moved side labels outward and capped radius at25cqw/29cqh. Final48 cases, all6 light/dark fixture rows and native minima viewed;9 QA counts0/copy0/font load errors0. Minima2x3,3x3,4x4 reflect readable wrapped names without hiding axes or legends.

Chart-bar inferred (not a mapped grouped chart):full fresh CSS uses source-derived bar end/width/plot-rule/type grammar, with value labels above vertical bars so zero and short bars remain readable. Horizontal variant reserves a real wrapping-name column and an external value gutter. All6 mandatory fixtures retain exact markup/data, plus0/100 and long Korean names. All148 final light/dark cases,16 fixture rows and native minima viewed;9 QA counts0/copy0/font load errors0. Vertical axes remain nowrap and thin dense category labels; no data values are hidden.

Chart-donut inferred from replica05:58% hole, broad ranked ring, pale track, deep percentage figure and white21px-ended carrier. Exact5 mandatory fixtures plus2 new Korean ones. Initial single-row groups passed geometry QA but long captions wrapped awkwardly; four members now become2x2 in a narrow-aspect slot, preserving the same markup. A second visual check found ring centres too small for figures after row allocation; source-like20px member gaps and a two-line row-caption reserve fixed this. Final126 light/dark cases,14 fixture rows and native minima viewed after the final whole-file write;9 QA counts0/copy0/font load errors0. Independent roots:size; group members:normal inherit their owning donuts query space, as approved for mapped donuts.

Chart-area inferred from replica05:white21px-ended plot panel,3px round-mark line, pale grid and ranked fill fading toward baseline. Four exact mandatory fixtures plus long3-series and natural0/100 boundaries. Initial2x2 multi-series minima passed QA but the four year labels visually joined and a legend word broke awkwardly; those fixtures now honestly start3x2. Axis labels remain nowrap, dense periods thin on their true grid columns, and all point values remain. All116 final cases,12 light/dark fixture rows and native minima viewed after whole-file correction;9 QA counts0/copy0/font errors0. No source chart is claimed as this inferred base.

Final area paint correction:adjacent wedges no longer leave vertical antialias seams. Each full series isolates its fill coverage; the rectangle extends1px beyond the original clip boundary, and plus-lighter combines only complementary edge coverage. Stacked opaque bands use a1px union overlap. Native crossing areas12x6 in both modes, all116 final cases/12 fixture rows and minima were re-viewed after this whole-file correction;9 QA/copy/font errors0. Data coordinates and deck-specific fading fills remain intact.

Slope inferred from replica05:white21px-ended field, round carriers and3px connectors with one4px accent emphasis. Full pairs own before/after lines and endpoint markers. Dumbbell names initially wrapped too narrowly despite QA0; semantic dumbbell variant now reserves a wider40cqw/max360px name column. Long names fit2lines; before values sit above and after values below their actual markers.62 final light/dark cases,8 rows and native minima reviewed;9 QA/copy/font errors0.0/100 and six crossing pairs remain data-faithful.


## Slope — final inferred design
Replica에 직접적인 paired-value 도표는 없어 각 덱의 실제 점·선·라벨 문법으로 새 설계했다. 원본 복합 플롯은 이 요소로 바꾸지 않았다. 각 pair 전체가 두 시점 연결선을 소유하며, dumbbell은 이전=open / 이후=solid 표식과 머리 키를 사용해 감소항목의 의미도 유지한다. 긴 이름 칸을 실제 두 줄이 읽히는 너비로 조정했다. 3·6개 변화, 0/100 경계, 긴 이름의 dumbbell 4개 fixture의 최종 라이트·다크 62칸 전행과 native 최소칸을 확인했다. 자동9항목0, 원문6자 일치0. 자동0은 시각적 동일성을 뜻하지 않는다.


## Scatter — final inferred design
원본에는 산점도/버블 도표가 없어 실제 플롯 점·선·라벨 문법으로 새 설계했다. 값축 두 개의 실제 좌표와 버블 면적 비율을 사용한다. 강조점 하나만 주 강조색, 일반 점은 중립·보조 순위로 조용하게 유지했다. 3/6/24점·0/100축 경계·버블·긴 실제 한국어 이름 총6fixture, 최종 라이트·다크76칸 전행과 native 최소칸을 봤다. 9자동검사0, 원문6자 일치0. 원본 복합 차트는 이 요소로 바꾸지 않는다.


## Waterfall — final inferred design
Replica05의 흰21px면·둥근carrier·두꺼운연결선 문법으로 신규 누적증감차트를 설계했다. 매 move가 실제from/to 부유막대와 결과합계높이의 다음연결선을 소유하고 total은0에서시작한다. 축/숫자/단계이름을각각공간배정.3/6/10단계·0/100·긴이름5fixture 최종66칸 전행/native최소칸을양모드에서직접보았다.9항목0/원문일치0.
최종추가수정: 둥근막대의상단peak가 실제값인것을유지하며 연결선을막대중앙끼리연장했다. 면뒤에서가려지는구간을포함하므로둥근corner가결과연결선을끊어보이게하지않는다. 실제66칸을전부재렌더하고전행/native최소칸을다시봤다.

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

### review-systems

# Systems element review

## architecture

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
    "shape_clipped": 0
  },
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/architecture/layers-3-dark-01.png",
    "build/native-review/architecture/layers-3-dark-02.png",
    "build/native-review/architecture/layers-3-dark-03.png",
    "build/native-review/architecture/layers-3-light-01.png",
    "build/native-review/architecture/layers-3-light-02.png",
    "build/native-review/architecture/layers-3-light-03.png",
    "build/native-review/architecture/layers-5-long-modules-dark-01.png",
    "build/native-review/architecture/layers-5-long-modules-dark-02.png",
    "build/native-review/architecture/layers-5-long-modules-light-01.png",
    "build/native-review/architecture/layers-5-long-modules-light-02.png"
  ],
  "decisions": [
    "Absent from replica; inferred stacked architecture from replica05 colored235×52tab and white779×209panel,16/21corner geometry,28/16.1type ratio and49px panel air.",
    "Names expand intrinsically beyond the30.17%minimum tab width; layer counts and module counts drive proportions.",
    "Secondary text uses neutral7 instead of literal source gray to preserve readability in both canonical palettes.",
    "No labels are hidden; longer modules wrap inside equal module slots.",
    "White panel faces use neutral1 consistently with the deck global roles. All20native final cells re-reviewed in both modes after correction."
  ],
  "known_remaining_differences": [
    "Architecture is an inferred contract element, not an exact replica instance.",
    "Module chips and the internal shadow are inferred from the deck panel/tab language.",
    "Fixture content is newly written Korean business content."
  ]
}

## matrix-nine

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
    "Nine-box absent from replica. Inferred from replica05 235×52accent tabs,779×209neutral1 panels,16/21corner geometry and28/16.1type ratio.",
    "Cell body pseudo occupies the actual second grid row below its name; corner ratios use the individual cell height.",
    "Both axes retain three real labels; vertical low-to-high order rises upward. On reverses panel/tab emphasis and tone1–4use canonical quiet palette surfaces.",
    "Short fixture minimum3×3; long names and notes6×4or4×6. All30final native cells directly reviewed in both modes; all8metrics zero."
  ],
  "corrections": [
    "Initial fixed radii looked too round at3×3. Rebuilt body as an own-cell pseudo with proportional corners and moved its start below the intrinsic tab row."
  ],
  "known_remaining_differences": [
    "The nine-box is inferred and is not a mapped replica instance.",
    "Minimum14/12readable type limits override proportional shrinking at tiny sizes.",
    "Fixture content is newly written Korean business content."
  ]
}

## table

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
    "build/native-review/table/dispatch-3-dark-01.png",
    "build/native-review/table/dispatch-3-dark-02.png",
    "build/native-review/table/dispatch-3-dark-03.png",
    "build/native-review/table/dispatch-3-dark-04.png",
    "build/native-review/table/dispatch-3-dark-05.png",
    "build/native-review/table/dispatch-3-light-01.png",
    "build/native-review/table/dispatch-3-light-02.png",
    "build/native-review/table/dispatch-3-light-03.png",
    "build/native-review/table/dispatch-3-light-04.png",
    "build/native-review/table/dispatch-3-light-05.png",
    "build/native-review/table/week-4-long-notes-dark-01.png",
    "build/native-review/table/week-4-long-notes-dark-02.png",
    "build/native-review/table/week-4-long-notes-dark-03.png",
    "build/native-review/table/week-4-long-notes-light-01.png",
    "build/native-review/table/week-4-long-notes-light-02.png",
    "build/native-review/table/week-4-long-notes-light-03.png"
  ],
  "decisions": [
    "Inferred table from source05 accent tabs over white panels:16/21corner hierarchy,28:16.1type,n1 independent face,a1-1-soft ground,n3 fine record rules.",
    "Continuous semantic header band and pale point column adapt that language to the required table markup."
  ],
  "corrections": [],
  "differences": [
    "No table exists in the frozen replica; this is explicitly an inferred contract design."
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
    "Inferred endpoint positioning uses source06 271px hero circles,12px white rim,77:100 nested circle ratio and bold centered name hierarchy.",
    "Actual endpoint labels replace no missing source field; vertical high coordinates rise upward.",
    "Regular name backing uses a1-1-soft ground and intrinsic text width, masking only actual letters where an axis crosses."
  ],
  "corrections": [
    "Strong a1/a2 gradient with a1-on produced3.83–4.41contrast in reference palettes. Inferred own mark uses accent1/2 depth2-soft surfaces and ordinary ink; source06 remains frozen.",
    "Manual review removed excess white backing rectangles and excessive axis masking; all final30 light/dark native cells re-rendered and inspected."
  ],
  "differences": [
    "No positioning map occurs in Tide replica. New positioning axes and quiet two-accent gradient are inferred; original hero geometry remains the shape source."
  ],
  "supplemental_geometry": "positioning-memberbounds.json:30cases0markOutside/0notRound/0nameOutsideInnerCircle; final backing-only change leaves the same circle/text geometry."
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
    "Inferred durations borrow source07 white21px panel,36px bars at46px pitch,7px mid-height arrow tips and neutral5period heading. The actual full5-row source remains unexpressible for left arrows and external staff fields.",
    "Whole roadmap owns each full-period strip via duration-relative pseudo geometry; point tips stay within exclusive end periods.",
    "Two-to-six lane and one-to-four bar counts control tracks; milestone reserves an independent lower strip."
  ],
  "corrections": [
    "Manual review replaced oversized solid lane planes with source-ratio slim duration bars and full-period strip behind each bar.",
    "Bar height cap queries root at36/373height; only label/tip query the bar itself, so milestone padding does not alter bar height.",
    "Owner type now preserves source14/373height guard in wide-short slots; dense emphasized bars have a12-token×1.6minimum height to separate letters from2stroke inset."
  ],
  "differences": [
    "New endpoint-data durations are inferred. Original07 direction/staff fields remain a gap; no fragment is claimed as a mapped base."
  ],
  "supplemental_geometry": "roadmap-memberbounds.json:30cases0textOutsideOwnBarOrOwner"
}

## matrix

{
  "replica_pages": [
    "05 (inferred language only)"
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
    "Attached235/779tab proportion and rounded white body derive from source05. All4heading tabs attach directly to their own body rather than floating inside it.",
    "SWOT uses the same tab/body planes with independently scoped list contracts. Its initial nested-list shadow and wide164pxchildpadding were corrected by the list owner; final text remains clearly readable."
  ],
  "corrections": [
    "The first draft centered the tab in the white body. Whole-file rewrite binds the white pseudo face to the note/list grid row and the heading to its attached upper row.",
    "Ordinary fixture min4x3is honest:3x3made the4-character vertical endpoint labels4lines."
  ],
  "differences": [
    "No quadrant matrix appears in the replica. Axes and SWOT letters are inferred contract structure; the surface and type grammar come from05."
  ]
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
    "Inferred connected-node contract from replica05 attached tab and white rounded field. Actual sources remain mapped to their original contracts.",
    "Four and six node counts choose2 or3 columns; node grid coordinates and explicit directions retain literal process meaning."
  ],
  "corrections": [
    "Unified all four arrowheads to shared stroke*8 width and equal16% shafts after manual review found vertical/horizontal thickness inconsistency."
  ],
  "differences": [
    "No source flowchart exists. All18 native light/dark panels manually inspected; min6x3 for six nodes,4x3 for four; no hidden text."
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
    "Source-absent owner lanes use replica05 attached tabs and rounded white faces on pale accent ground. Literal contract column1 remains column1 without a hidden owner column.",
    "Top40%of each row is reserved for owner names,with max45%of first column width to protect vertical connectors; nodes use50%row height and arrows bridge the remaining50%."
  ],
  "corrections": [
    "Added a long operational owner name and constrained its height-sensitive type to keep its three lines clear of both node faces and vertical arrows."
  ],
  "differences": [
    "Inferred swimlane; all14 final native panels manually reviewed across both modes. Minimum6x3 for2owners/3cols,8x4 for3owners/4cols,no text hidden."
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
    "Absent decision tree uses replica05 rounded white faces,accent top-tab emphasis and pale ground; recommended outcomes use the second accent role.",
    "Left-to-right recursive options retain all questions,conditions and outcomes. Three-question depth has honest12x6 minimum; simpler three-outcome tree admits4x3."
  ],
  "corrections": [
    "Widened plain outcome answer columns to30%so the deepest two-character answers remain on one line; branching question columns retain their independent structural layout."
  ],
  "differences": [
    "Inferred decision tree. All12 final native light/dark panels manually reviewed; no question depth or text is hidden."
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
    "Absent journey extends replica05 attached accent tabs and16/21 rounded white fields. Mood0/100 endpoints are real fixture data,with the graph mapped to10–40%height and stage content starting44%to protect the lowest point.",
    "Each stage owns one point and outgoing CSS segment; terminal removal uses only actual3–7member counts,not fixture-specific selectors."
  ],
  "corrections": [
    "Removed the note stacking context that let its plane cover title tabs.",
    "Added boundary mood0/100 and separated the graph area from content by4%height."
  ],
  "differences": [
    "Inferred journey. All16 final native light/dark panels manually inspected;3stage min4x3,7stage min8x4; names,notes and optional pain points remain visible."
  ]
}

## sankey

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
    "build/native-review/sankey/routes-6-light-01.png",
    "build/native-review/sankey/routes-6-light-02.png",
    "build/native-review/sankey/routes-6-light-03.png",
    "build/native-review/sankey/routes-6-light-04.png"
  ],
  "decisions": [
    "Absent Sankey uses source05 rounded white faces, accent source and pale ground.",
    "Actual minima6x3 for flat and nested fixtures preserve every name and figure;0% has no band.",
    "One terminal-row height unit determines direct share and nested local-share product thickness."
  ],
  "corrections": [
    "Reduced conservative initial minima after checking every new small cell.",
    "Nested ribbons extend underneath the parent face and paint behind it, so the original rounded corner remains intact while its flow stays connected at short heights.",
    "Unit glyph uses shared type clamp with matching rendered size."
  ],
  "differences": [
    "No source Sankey; proportional connected topology is inferred from measured deck primitives."
  ],
  "supplemental_geometry": "sankey-sharebounds.json:24cases0errors;share scale,zero band and actual overlapping parent joins"
}


### review-text-transfer-source-owner

# 재인수 추론 요소 최종 검수

사람 소개는 원본에 없다. 기존 범용 프로필 초안을 덧붙이지 않고 CSS 전체를 새로 썼다. replica05의235×52 탭,779×261 흰 면,21px 모서리와18.67px 본문 문법에서 이름 탭·사진·소개문 구조를 추론했다. 흰 raised 면은n1, 이름 탭은a1/a1-on, 사진은neutral 자리다. 페이지 그라데이션은 foundation이 맡고 요소는 그리지 않는다.

1명과2명은3x2,3명은4x3을 최소 칸으로 채택했다. 3명3x3에서는 직함이3–4행, 소개문이7–8행으로 잘게 나뉘어 제외했다. 3명4x2는 실제 글자가 칸을 넘으므로 제외했다. 4x3의 여러 줄 이름·본문은 실제 크기로 읽었다. 탭의 배경 면과 글자는 중앙이며 사진과 긴 설명은 같은 흰 면에 들어간다.

마지막 수정 뒤 라이트·다크 전체 시트를 다시 렌더했다. 모든 칸의 텍스트를 원래 픽셀 크기의 조각으로 읽었고, 전체 시트에서 정렬·면·사진 자리를 함께 확인했다. 모든9 QA0, 실제 raster 칸 밖 번짐0, 실제 로드된 Pretendard 글리프 확인. 원본7덱과6자 이상 같은 문구 자동 검사283 fixture에서0건이다. 이5개는 원본 인스턴스 재현을 주장하지 않으며 기존 source38 동결은 변경하지 않았다.

- person: 56칸 / min team-three=4x3, profile-one=3x2, team-two=3x2

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
    "build/native-review/agenda/agenda-five-light-01.png",
    "build/native-review/agenda/agenda-five-light-02.png",
    "build/native-review/agenda/agenda-four-dark-01.png",
    "build/native-review/agenda/agenda-four-dark-02.png",
    "build/native-review/agenda/agenda-four-dark-03.png",
    "build/native-review/agenda/agenda-four-light-01.png",
    "build/native-review/agenda/agenda-four-light-02.png",
    "build/native-review/agenda/agenda-four-light-03.png"
  ],
  "decisions": [
    "No agenda source; source05 measured779x261 attached label/body composite independently supplies235x52 label,16/21 corners,42/54 body inset and30/16.1 typography.",
    "Each entry owns its size container; source9/8 shadow remains inside root shared padding.",
    "Four entries minimum6x4 or4x6; five entries8x5 or6x6."
  ],
  "corrections": [
    "Replaced the generic rounded number-card arrangement with the actual attached-tab grammar.",
    "Replaced every pre-truncated ellipsis note with a complete newly written business sentence; added a long business heading.",
    "Uses existing neutral3 role for the pale source shadow."
  ],
  "differences": [
    "Inferred contents list; no direct replica agenda exists."
  ],
  "supplemental_geometry": "agenda-transfer-raster.json:20cases0visiblebleed; all20cells/10nativepanels personally reviewed"
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
    "Bare metric contract precludes source05 card face. Source08 centered53.333/400 declaration,source05 30/700 heading and18.67 body inform the typography. Stats row gets actual-count dividers and own member containers."
  ],
  "corrections": [
    "Replaced generic unboxed stack with actual centered declaration hierarchy. Added three-member stats contract fixture. Unit text uses type12 minimum clamp.",
    "Final divider painter stops at last real division to prevent rounding-induced edge line. Final stats10 cases rerendered and directly reviewed;34 unchanged nonstats PNG hashes match previously reviewed images."
  ],
  "differences": [
    "No bare metric exists in source, so the source hierarchy is explicitly inferred without adding containing surfaces."
  ],
  "supplemental_geometry": "44 final cases9QA0/raster0/copy0;28 native panels directly reviewed, final10 stats cases re-reviewed,34 nonstats exact PNG identity."
}


### review-text-transfer

# Transferred inferred elements — final review

headline: source05/08 inference 유지. 어절단위 줄바꿈으로고립문자수정, big추가. min3x3/4x3,50칸.
list: source05 둥근표식/순위강조 유지,check추가·icon칸정사각. min3x4/4x6,32칸.
pill: source05 21px끝모서리 문법. 한줄nowrap,세로padding12cqh로넘침해결,line/quiet/on추가. min3x1/4x1,78칸.
quote: source05면/08서술타입 추론. 사진없는by의빈column제거. min4x4/5x4,20칸.
모두최종전행/native최소칸양모드직접검수,9QA0/원문6자0/폰트로드0.

### review-text

# Text element provenance and review decisions

The fixed replicas were read as evidence and were never edited. Sample HTML supplies mandatory data/markup only; no sample element CSS was read or reused.

## Per-leaf provenance

- card: 05:base, 05:variant:.tone-2.
- pill: inferred; no independently expressible source instance.
- callout: 08:base.
- tag: 08:base.
- list: inferred; no independently expressible source instance.
- quote: inferred; no independently expressible source instance.
- headline: inferred; no independently expressible source instance.
- prose: 08:base.
- metric: inferred; no independently expressible source instance.
- agenda: inferred; no independently expressible source instance.
- person: inferred; no independently expressible source instance.

## Recorded corrections and decisions

- 08 mixed headline colors/weights cannot be represented by headline b alone and remain a gap. The three body paragraphs are now source-backed prose with real b plus nested tag.inline hl, with no paragraph-order color rule.
- Native source card779×261 is excluded from the compact≤650px-wide shallow stage, preserving its30px name and16.1px note. Padding reference is52px tab+42px title inset.
- The source shadow is0 9px 8px #d9dfeb66, not an ink-colored short negative-spread edge. It is now the a2-1-muted role at40% transparency. The map includes8px lateral/17px lower paint guards, preserving the actual779×261 face.
- Root semantic review resolved the former3-paragraph gap: prose b carries blue a2-8, and the independently meaningful teal phrase uses a real tag.inline hl at a1-8. Prose18.67px/1.28/−.06em and23/24px paragraph gaps were rebuilt from the source; the tag label root remains inferred from05 attached-tab language.

## Inferred elements

pill, list, quote, headline, metric, agenda, person. Each has its own build/inferred-spec-<leaf>.json citing this deck’s measured source primitive, an inferred description and fresh business fixtures. These files never claim a source base.

## Validation state

Browser sheets and probes are recorded in review/validation and build/probes. A zero automated result alone is insufficient: native source-box comparisons found and corrected font, gap, shape, padding-reference, missing-avatar and quotation collisions. Each final proof must match the latest source hashes. Final fixture minima are selected after native smaller-candidate review; initial conservative comments are not final evidence.

### 주 담당자 페이지 대조 기록


- 최종 확인: Filament04의 오른쪽 Confidential 레일은 동결 replica 자체가 붉은 글자를 붉은 면에 놓아 보이지 않는다. 동결본의 색 역할을 보존했으며 원본의 흰 레일과 차이를 남긴다. Cutfield13 밝은 tone 면의 글자와 icon은 대비를 위해 palette on 역할로 바뀌며 원본 흰 글자와 다르다. Toggle06의 12×6 행 양자화는 사진 3개 사이의 세로 공백을 줄인다.

- Portico02: 10개 목차는 계약 agenda 최대8개와 충돌하여 전체 인스턴스를 미지원으로 기록했다. 8+2개의 다른 요소로 쪼개 겉모양을 속이지 않는다. 빈 조립 영역은 누락 사고가 아닌 명시된 계약 한계다.
- Portico03/04: 넓은 수평 사진띠는 frame의 seat 종횡비 제한과 충돌해 미지원으로 기록했다. source gray 사진 자리를 임의의 가로 왜곡 frame으로 대체하지 않았다.03/04의 작은 방사형 도상은 계약 mark의 단순별로 근사해 원본6점과 다른 잔차가 있다.
- Portico05: 각 사진 자리의 번호는 계약 독립 frame이 자기 seat부터1로 센다. 여러 요소 사이 전역 순번1·2·3은 계약 데이터 슬롯이 없어3개1로 보인다.

- Lamella07: 위쪽 오른쪽 한 모서리만 휜 흰 cap 둘은 양 모서리가 휜 headline base와 달라 계약 변형에 대응하지 못한다. 그림은 임의 변형으로 우회하지 않고 GAPS에 기록했다. 본문과 독립 가로 괘선은 source 수치·반전 문맥을 복구했다.

- 최종 통합:392요소의양모드크기시트와87페이지비교PNG를주담당자가모두열어확인했다. 최종source문구추출정정후Rule13의3개카드본문은source의3줄구조를되찾았다. Lam18의1개quote본문3→4줄은독립tracking차이로잔차를명시했다.
- 최종grid검사:87페이지/231개최상위요소/543쌍에서source분리요소의신규교차0,정수span과양수12×6tracks오류0. Lam23의5.68e-14px중복경계를1e-6px허용오차로합쳐양수트랙을복구했다. 원본에이미있던교차11건은구별해기록했다.

