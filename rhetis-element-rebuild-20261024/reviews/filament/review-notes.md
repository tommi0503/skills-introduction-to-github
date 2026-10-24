# 검수 기록 — filament

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
- 03: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 05: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 02: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 08: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 04: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 06: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 07: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.

## 담당 요소별 상세 기록

### review-charts

# Chart element review

## gauge — inferred, no source instance

Source grammar: replica05 uses a250-weight large display, a broad primary surface and very fine accents on the open page. The inferred progress field uses a1px outline and an inset solid primary fill;0% leaves the outlined field fully empty. The value uses --figure-weight250, with body-weight supporting text. Body and outlines use --a1-8, fill --a1, empty field --page, preserving the source accent-text role in both palettes. Three realistic Korean business fixtures cover0/64/100% and long names. Minimum2x2; all six final rows and both native minima atlases viewed. Final60 cases: all eight QA counts zero, three fixtures copy audit zero. No image or new class is used and no part is hidden.

Final CSS SHA256: cb09df8b719caca507e8d71da272b099b97a204026ab2bc420b5ed9be4520b64.

## Inferred bullet
Source05 contributes the fine accent outline and light250-weight display; this target/range data contract has no mapped replica instance. The outlined qualitative field has a thin actual fill and an independent one-pixel target. All four fixture rows, both native minimum atlases, and all70 final size/mode renders were reviewed. Nine automated checks and the copied-source audit are zero. Minimum4x4 for four members retains full notes; long individual note requires2x3.

## Inferred sparkline
Source05's fine accent outlines over an open field translate to a0.7px line, hollow4px point carriers, and44%-width outlined mini bars. No source sparkline is claimed. Scoped point anchors own the connectors; up/down use semantic roles. All80 final renders, all eight mode/fixture rows and both native1x1 minimum atlases viewed; nine automated checks/copy audit zero. The24 narrow outlined bars remain distinct as fine marks at1x1.

## Inferred heatmap
Source05's fine accent outlines and open cream field inform a new outlined density matrix. Cell fills mix page toward the softer primary2 role while text remains the deep primary8 role; light250 figures retain the measured numerical grammar. The calendar variant keeps square outlined cells and concise week headings. All58 final renders, six mode/fixture rows and native minima reviewed; nine QA checks/copy audit zero. No source instance is claimed.

## Inferred waffle
Source05's fine accent outlines and light250 display hierarchy inform this new counted-share graphic. Uncounted units remain outlined page fields; counted/tone shares fill the same square matrix. Figures mode uses CSS people with fine outlined head carriers. All60 final size/mode renders, six fixture rows and native minima inspected; nine QA checks and source-copy audit zero. A100-unit matrix reads at1x2, while full two-share figures and person silhouettes require2x2. This is inferred, not a source instance.

## Inferred chart-line
Source05's fine accent outline and open cream language informs an inferred0.7px pure line with4px hollow carriers; its selected6px carrier fills the same deep primary role. Data labels use body weight while only genuine emphasis becomes strong, preserving the source's light/strong type contrast. All four showcase fixtures retain exact data/markup, plus new Korean periods and boundary data. All112 final renders, all twelve fixture/mode rows and native minima viewed; nine QA checks/source-copy audit zero, CDP custom fonts loaded without error. No source pure-line instance is claimed.

Chart-line contract correction: axis labels now use nowrap and count/width-based thinning, retaining every value and point. New boundary data follows0/28/67/100/93/86, satisfying the no-repeated-sawtooth requirement. Updated minima monthly12=3x2, six longer labels4x2, long periods4x2 supersede earlier minima. All116 final cases, twelve final mode/fixture rows and native minima regenerated and viewed; nine QA checks, copy fragments and font load errors zero.

Final chart-line:8px shared-token gutters keep value backplates off the L-axis and align the end-label insets. The final whole-file rewrite was rendered again; every light/dark fixture row and native minimum was viewed. All9 geometry/contrast/paint checks and copy checks are zero. Axis labels remain nowrap and are thinned at narrow sizes; all values and points remain.

Radar (inferred, no mapped base):CSS-only wedge sectors draw the full-axis concentric polygon grid, and each series owns its fill and vertex markers. Axis counts3/5/8 and series counts1/2/3 use new Korean business data. The first Tide draft passed geometry checks but its centred side labels crossed near outer vertices; a whole-file rewrite moved side labels outward and capped radius at25cqw/29cqh. Final48 cases, all6 light/dark fixture rows and native minima viewed;9 QA counts0/copy0/font load errors0. Minima2x3,3x3,4x4 reflect readable wrapped names without hiding axes or legends.

Chart-bar inferred:6 exact mandatory fixtures plus0/100 and long names; all148 final light/dark cases,16 fixture rows and native minima viewed.9 QA counts0/copy0/font load errors0. Vertical labels are nowrap/thinned, all values stay visible; horizontal names wrap in a dedicated column with a separate value gutter. Filament uses genuinely thin outlined bars and palette-ranked outlines; its first draft ignored secondary outline tones, found visually and fixed by complete rewrite before final render. Portico uses measured66.8% bar-to-pitch width and straight1px plot rules. Existing grouped source plots remain gaps.

Chart-donut inferred:94% hole, fine deep-accent contour, open cream centre and light250-weight numerical type inferred from replica05. Exact5 mandatory fixtures plus2 new Korean business fixtures. Groups allocate width and height together; four members use2x2 at a narrow aspect ratio. All126 final light/dark cases,14 fixture rows and native minima viewed;9 QA counts0/copy0/font load errors0. Independent root:size; a donut owned by a donuts root is a normal member using the group container. All figures and names remain visible.

Chart-area inferred from replica05:.7px contours,4px hollow marks, deep accent type and open12% ranked fills retain its fine-outline language. All4 exact mandatory fixtures plus long3-series and0/100 boundaries.116 final light/dark cases,12 fixture rows and native minima reviewed;9 QA/copy/font errors0. No extra markup draws the area:full series own equal-step CSS wedges, cumulative layers reverse painting order, and shared boundary coverage is unioned without vertical seams. Dense axis labels thin without wrapping; every data value remains visible.


## Slope — final inferred design
Replica에 직접적인 paired-value 도표는 없어 각 덱의 실제 점·선·라벨 문법으로 새 설계했다. 원본 복합 플롯은 이 요소로 바꾸지 않았다. 각 pair 전체가 두 시점 연결선을 소유하며, dumbbell은 이전=open / 이후=solid 표식과 머리 키를 사용해 감소항목의 의미도 유지한다. 긴 이름 칸을 실제 두 줄이 읽히는 너비로 조정했다. 3·6개 변화, 0/100 경계, 긴 이름의 dumbbell 4개 fixture의 최종 라이트·다크 62칸 전행과 native 최소칸을 확인했다. 자동9항목0, 원문6자 일치0. 자동0은 시각적 동일성을 뜻하지 않는다.


## Scatter — final inferred design
Replica05의 가는 outline·크림 여백 문법을 적용한 신규 산점도. 실제좌표 점은 얇은 열린원, 강조는 깊은순위와 큰원, 버블은 면적비례의 연한채움/가는outline이다. 일반점 n5/보조순위와 한 주강조를 분리했다. 3/6/24점·0/100경계·버블·긴이름6fixture의 최종76칸 전행/native최소칸을 두모드에서 봤고 자동9항목0/원문일치0이다.


## Waterfall — final inferred design
Replica05의 가는선·연한 outline면으로 신규waterfall을 설계했다. 막대폭44%, .7px선, 낮은채도면을 사용하고 값/라벨은 깊은순위로대비를유지했다. 각move가실제from/to막대와to높이연결선을소유한다.5fixture 최종66칸 전행/native최소칸 양모드직접검수,9지표0/원문일치0.

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

### review-root-furniture

# 독립 장치와 읽기 방향 최종 대조

04의95px X와07의45px +를 소스의 띠 굵기와 좌표 그대로 foundation장치로 옮겼다. 07세로 기밀 표시는 원본 inline의180도 회전을 foundation의 일반 회전 데이터로 보존한다. 06깃털은 원본 사진의 회색 실루엣 자리이므로 독립 장식으로 오인하지 않고 frame의 윤곽 계약 부재를 GAPS에 기록했다.

### review-root-pages

주 담당자 개별 페이지 대조에서 02/03 소제목이 실제21px인데 foundation에서14px로 고정된 것을 발견했다. 선언된 측정 글꼴 변수로 바꾸고 공유 type20을 사용했다. foot/rail 굵기는 원문400에 맞춰 body-weight로 바꿨다. 단독 footer의 margin-left:auto가 원문 왼쪽 정렬을 오른쪽으로 이동시켜 dot 장식과 겹쳤으므로 정렬을 복구했다. 05 왼쪽 Portfolio는 source writing-mode:vertical-rl/rotate180을 foundation rail에 복구했다. 06의 대형 요소는 contract big 변형을 사용하며 공유 행간으로 약10px의 glyph 기준선 차이가 남는다.

### review-systems

# Systems element review

## table

{
  "replica_pages": [
    "03",
    "08"
  ],
  "source_css_reused": false,
  "final_render_cases": 38,
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
  "cell_text_outside": 0,
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/table/replica-03-dark-01.png",
    "build/native-review/table/replica-03-dark-02.png",
    "build/native-review/table/replica-03-dark-03.png",
    "build/native-review/table/replica-03-dark-04.png",
    "build/native-review/table/replica-03-dark-05.png",
    "build/native-review/table/replica-03-light-01.png",
    "build/native-review/table/replica-03-light-02.png",
    "build/native-review/table/replica-03-light-03.png",
    "build/native-review/table/replica-03-light-04.png",
    "build/native-review/table/replica-03-light-05.png",
    "build/native-review/table/replica-08-dark-01.png",
    "build/native-review/table/replica-08-dark-02.png",
    "build/native-review/table/replica-08-dark-03.png",
    "build/native-review/table/replica-08-dark-04.png",
    "build/native-review/table/replica-08-dark-05.png",
    "build/native-review/table/replica-08-light-01.png",
    "build/native-review/table/replica-08-light-02.png",
    "build/native-review/table/replica-08-light-03.png",
    "build/native-review/table/replica-08-light-04.png",
    "build/native-review/table/replica-08-light-05.png"
  ],
  "decisions": [
    "Intrinsic label column retains measured open pair layout without per-page86/98px overrides.",
    "Font scales per member row; contact source17px becomes17.85px at exact120px source height.",
    "Source six-row fixture has3×3 minimum, contact has3×1 minimum; all content remains visible.",
    "All source03/08 red body text uses accent1 depth8 consistently with the deck global role. Contract pick uses depth9 and stronger body emphasis. All38final native cases re-reviewed in both modes after role correction."
  ],
  "known_remaining_differences": [
    "Contact-row pitch is uniformly distributed rather than42/44px.",
    "Preview palette replaces the source colors as required.",
    "Fixture content is newly written Korean business copy."
  ],
  "corrections": [
    "Source-size comparison exposed a5.61px short label allocation at03. The base now preserves72/468minimum label plus26/468gutter,producing exactly98px value start. An actual full-row colspan retains the intrinsic contact-label structure."
  ],
  "differences": [
    "Contact08keeps88.125px intrinsic offset against source86px; no page-specific width rule is introduced."
  ],
  "source_size_comparison": [
    {
      "page": "03",
      "bbox": [
        738,
        340,
        468,
        242
      ],
      "comparison": "build/sourcebox-systems/table-03.png",
      "geometry_qa": {
        "outside": 0,
        "clipped": 0,
        "member_outside": 0,
        "overlaps": 0,
        "shape_clipped": 0,
        "painted_outside": 0
      },
      "source_palette_contrast_only": [],
      "css_sha256": "83868d8d4be50debae81f387381a139e86814850a9e83b573b316c986bc820ee"
    },
    {
      "page": "08",
      "bbox": [
        83,
        493,
        500,
        120
      ],
      "comparison": "build/sourcebox-systems/table-08.png",
      "geometry_qa": {
        "outside": 0,
        "clipped": 0,
        "member_outside": 0,
        "overlaps": 0,
        "shape_clipped": 0,
        "painted_outside": 0
      },
      "source_palette_contrast_only": [],
      "css_sha256": "83868d8d4be50debae81f387381a139e86814850a9e83b573b316c986bc820ee"
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
    "Absent from replica. Service-panel architecture extends replica07 178×121panels,12px rounds,14/15px insets,25px light upper names and17px bold lower labels.",
    "Module700bold uses body400×1.75, not the numeric figure token, so the source label hierarchy survives the corrected light numeral kit role.",
    "One accent face per layer, no boxed module cards; all labels remain visible.",
    "Three-layer minimum lowered to3×3after native review; five long layers pass6×4or3×6.",
    "All30final native cases directly inspected in both modes after the last full-file regeneration."
  ],
  "known_remaining_differences": [
    "Stacked architecture is inferred, not a mapped source instance.",
    "Module text is centered to satisfy chip semantics; source lower service labels align left.",
    "New Korean fixtures use loaded Pretendard rather than the source English Noto title words."
  ],
  "token_retarget_pngs_identical": 30,
  "token_retarget_proof": "review/validation/architecture-token-equivalence.json"
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
    "shape_clipped": 0,
    "painted_outside": 0
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
    "Inferred nine-cell matrix, not present in replica; source07 178×121 service faces supply 12/121 rounding, 14/178 side insets and light upper name/bold lower note hierarchy.",
    "Nine-cell notes require a continuous height guard while preserving 25:17 source hierarchy; new Korean business copy only.",
    "Tone4 uses a1-9 reading text because a1-8 fails dark palette contrast."
  ],
  "corrections": [
    "Dark tone4 contrast 4.32 corrected by semantic reading depth; whole file regenerated and every light/dark native cell re-rendered and inspected."
  ],
  "differences": [
    "Original service labels are brief English; matrix notes use Korean multiline business copy and token-based readability minima."
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
    "Inferred positioning retains source07 45px thin accent crosses for competitors,178:121 own service face,12px rounds,300-weight names and a1-8 reading accent.",
    "Names stay below cross markers; own name stays centered inside the measured service aspect ratio, not a generic circle."
  ],
  "corrections": [],
  "differences": [
    "No positioning contract occurs in Filament source; real endpoint axes and business labels are inferred."
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
    "Inferred roadmap keeps source07 178×121service-face grammar,12/121rounding,300-weight owner/period names and700-weight duration labels derived from400body role.",
    "One-accent soft tones preserve source red-only language; inverse on uses page face and accent8inset frame. Milestone uses the thin cross motif."
  ],
  "corrections": [
    "Milestone cross dimensions use chart width and12token maximum rather than inheriting page26px em, preventing tiny-slot decoration crowding."
  ],
  "differences": [
    "No duration roadmap occurs in Filament source; endpoint data and owner tracks are inferred."
  ],
  "supplemental_geometry": "roadmap-memberbounds.json:30cases0textOutsideOwnBarOrOwner"
}

## matrix

{
  "replica_pages": [
    "07 (inferred language only)"
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
    "Source07178×121service faces supply12px rounds and25/300light heading versus17/700strong lower-copy hierarchy. A single accent supplies all faces; on reverses to the page with an inset accent8edge.",
    "Ordinary names anchor to the top inset and the strong notes to the lower inset,matching source service alignment. SWOT retains light letter/heading and independently scoped strong list contents."
  ],
  "corrections": [
    "The first centered text-block draft moved headings when one note wrapped. Whole-file rewrite restores source top-name/lower-copy alignment.",
    "Measured face insets are scaled against both member dimensions so wide low cells preserve their text area."
  ],
  "differences": [
    "No source matrix or SWOTexists. Four quadrants and axes are inferred contract structure."
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
    "Source-absent flowchart uses replica07 light25/300 headings,17/700 lower copy, and12px rounded accent service faces; the question is the open reading-accent state.",
    "Node content uses real b+p text structure with both ends visibly retained at every admitted size."
  ],
  "corrections": [],
  "differences": [
    "Inferred flowchart; no source scene is remapped. All18 native light/dark panels manually inspected; min6x3 six nodes and4x3 four nodes."
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
    "Absent owner-flow contract uses replica07 rounded accent service faces and300-weight light headings,while owner labels use700 reading-accent emphasis.",
    "Open question state retains the page plane and thin reading-accent outline; start/end retain solid accent surfaces."
  ],
  "corrections": [],
  "differences": [
    "Inferred swimlane; all14 final native panels inspected across both modes. Long owner labels and all four connector directions retained."
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
    "Absent decision tree uses replica07 accent service fields,source12-radius shared corners and300-weight light question/outcome hierarchy; condition labels use700 reading-accent emphasis.",
    "Maximum three-question depth has12x6 minimum; all semantic text and recursive branching stay visible."
  ],
  "corrections": [
    "Retained the shared source radius on small outcome boxes instead of shrinking their corners through an ancestor query."
  ],
  "differences": [
    "Inferred decision tree. All12 final native panels in both modes directly reviewed; min4x3 for the simple three-outcome fixture."
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
    "Absent journey derives source07 service-face radius12 and light300 name / strong700 copy contrast.",
    "Three-stage minimum4x3; seven-stage minimum8x4 retains every note and pain field.",
    "Mood0 and100 boundary points have four percent root clearance from the stage content."
  ],
  "corrections": [
    "Common segment layout retains one connected element and removes only the terminal segment through member count."
  ],
  "differences": [
    "No journey instance exists in this replica; data-driven curve is inferred using measured deck primitives."
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
    "Absent Sankey uses source07 radius12 service fields,300 light names and250 value figures.",
    "Actual readable minima are4x3 for six paths and6x3 for nested4+2; all notes/values remain visible.",
    "Direct source shares and local nested shares multiply on one terminal-row thickness unit;0% has no ribbon."
  ],
  "corrections": [
    "Separated name and figure by8% of the member height after actual text bounds overlapped under figure-line1.05.",
    "Reduced overly conservative initial minima after rendering every newly admitted smaller cell."
  ],
  "differences": [
    "No source Sankey; connected proportional flow geometry is inferred from measured deck primitives."
  ],
  "supplemental_geometry": "sankey-sharebounds.json:28cases0errors,share scale and all connections including0%"
}


### review-text-transfer-source-owner

# 재인수 추론 요소 최종 검수

사람 소개와 callout은 원본에 없는 추론 설계다. source07의178×121 서비스 판,12px 모서리,25px/300 경량 제목과17px/700 굵은 하단 설명에서 설계했다. person은 사진 아래 하나의 연속 강조 면에 경량 이름과 굵은 설명을 담는다. 작은 칸에서도 이름/설명 사이에 흰 틈을 끼우지 않도록 gap0을 유지한다. callout은 같은 연속 강조 면과12px 반경,source04의16px/1.4 본문 리듬을 쓰고 핵심 구절만700으로 바꾼다. 면은a1/a1-on이며 원본 색 리터럴은 없다.

person1명3x2,2명3x3,3명4x3이 최종 min이다. 처음2명3x2는9개 DOM 검사는 통과했지만 실제 raster 검사에서 붉은 설명 면이 아래로11px 넘쳤다. CSS/페이지/bbox를 늘려 숨기지 않고 min을3x3으로 올린 뒤 전체54칸을 다시 렌더했다. 최종 raster154칸(person54+callout100)에서 넘침0이다. 3명4x2는 글자가 넘어서 제외했다. callout5개는3x1에서 실제 문장을 읽고 min을 정했다. 의무 fixture 데이터/마크업은 유지했다.

마지막 수정 뒤 라이트·다크 전체 시트를 다시 렌더했다. 모든 칸의 텍스트를 원래 픽셀 크기의 조각으로 읽었고, 전체 시트에서 정렬·면·사진 자리를 함께 확인했다. 모든9 QA0, 실제 raster 칸 밖 번짐0, 실제 로드된 Pretendard 글리프 확인. 원본7덱과6자 이상 같은 문구 자동 검사283 fixture에서0건이다. 이5개는 원본 인스턴스 재현을 주장하지 않으며 기존 source38 동결은 변경하지 않았다.

- person: 54칸 / min team-three=4x3, profile-one=3x2, team-two=3x3
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
    "No source agenda; source07 178x121 service fields supply12px corners,300-weight names and700-weight footer. Source06 supplies250-weight figures. Own entry size queries preserve all full note text at small sizes."
  ],
  "corrections": [
    "Replaced generic ruled index-row styling with actual service-face grammar. Replaced truncated notes with complete new Korean business copy."
  ],
  "differences": [
    "Inferred agenda combines service fields and source index figures; not claimed as source instance."
  ],
  "supplemental_geometry": "20 raster cases zero outside pixels; all12 native panels personally reviewed after final CSS."
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
    "Source06 actual90/250 display,.98 line,-.015em tracking pairs with20/650 caption and16/1.4 body. Bare metric has no service-card surface."
  ],
  "corrections": [
    "Fresh implementation preserves light left-aligned large figures. Added actual-column-size stats3 fixture/dividers, complete Korean copy and type12 unit floor.",
    "Final divider painter stops at last real division to prevent rounding-induced edge line. Final stats10 cases rerendered and directly reviewed;34 unchanged nonstats PNG hashes match previously reviewed images."
  ],
  "differences": [
    "No bare metric source instance exists; typography is inferred from display and caption grammar."
  ],
  "supplemental_geometry": "44 final cases9QA0/raster0/copy0;28 native panels directly reviewed, final10 stats cases re-reviewed,34 nonstats exact PNG identity."
}


### review-text-transfer

# Transferred inferred elements — final review

quote: source의 면/가는선/문자강조 문법을 유지하며 사진없는by의빈column을제거했다. min4x4/5x4,20칸 전행/native최소칸 양모드직접검수,9QA0/원문6자0/폰트로드0.
list: 07의 작은둥근사각표식/가는순위글자 유지,check추가·mark칸정사각. min3x4/4x6,32칸. pill: 07의12px모서리 유지,한줄nowrap와세로높이비례padding,line/quiet/on포함,min3x1/4x1,78칸. 모두전행/native최소칸양모드검수,9QA0/원문6자0.

소유 CSS/fixture 최종 동결. 주 에이전트가 Filament foundation의 외부 footer/kicker 수정 뒤 shared-only 증거를 갱신 중이다. 해당 56개 leaf의 이미지 변경 CHANGED0 보고를 받았으며, 공유 의존 해시 freeze는 pending으로 기록한다. 주 에이전트의 전체7덱 최종 의존성/raster/CDP 감사로 확정한다.

### review-text

# Text element provenance and review decisions

The fixed replicas were read as evidence and were never edited. Sample HTML supplies mandatory data/markup only; no sample element CSS was read or reused.

## Per-leaf provenance

- card: 07:variant:.on.
- pill: inferred; no independently expressible source instance.
- callout: inferred; no independently expressible source instance.
- tag: 04:base, 04:same-as:04.
- list: inferred; no independently expressible source instance.
- quote: inferred; no independently expressible source instance.
- headline: 06:base, 06:same-as:06, 05:variant:.big, 05:same-as:06.
- prose: 04:base, 02:variant:.lead, 02:same-as:04, 05:same-as:04, 06:same-as:04, 08:same-as:04.
- metric: inferred; no independently expressible source instance.
- agenda: inferred; no independently expressible source instance.
- person: inferred; no independently expressible source instance.

## Recorded corrections and decisions

- Service07 corner radius is12px, not the initial5px estimate. Actual25px/300 Noto name uses --filament-service-font kit font extension, approved by root from the allowed Noto Sans family. The immutable source WOFF2 is copied only into review assets; the library contains no font binary or URL.
- Native178×121 reports24.9998px name/24.5px line,15px left/14px top,17px note. Chromium platformFonts confirms custom Noto Sans actually renders Latin test glyphs. The generic shallow stage was restricted by width to avoid shrinking this real native source to17.8px.
- All source body paragraphs are16px; only source02 lead is18px/650. Earlier width-proportional18.9/21px output was corrected to their shared source steps.
- Project05 uses actual97px/250,−5.82px tracking. Its DOM box y196,h100 excludes glyph paint; immutable-source Range metrics give y186,h115. The map now includes this true painted box and native outside0.
- Tag04 is a bare white13px caption, not an accent-filled inferred badge. Its manifest entry was corrected to source-backed; shared14px differs by1px and color inherits the real foundation inverse field.

## Inferred elements

pill, callout, list, quote, metric, agenda, person. Each has its own build/inferred-spec-<leaf>.json citing this deck’s measured source primitive, an inferred description and fresh business fixtures. These files never claim a source base.

## Validation state

Browser sheets and probes are recorded in review/validation and build/probes. A zero automated result alone is insufficient: native source-box comparisons found and corrected font, gap, shape, padding-reference, missing-avatar and quotation collisions. Each final proof must match the latest source hashes. Final fixture minima are selected after native smaller-candidate review; initial conservative comments are not final evidence.

### Final integration corrections
- Headline base is the actual05 caption24px/650;90–97px ultra-light statements use `.big`. The former short-height substitution was removed. Common `.big` fit yields92.78px vs90px source in450×110, and retains shared−.015em statement tracking vs Project−.06em. Source-sized comparison records that Present/Future glyphs sit about10px below the frozen original; no page or fixture condition hides this residual.

- Actual minimum-cell inspection rejected4x4 for multi-card fixtures despite0 automatic bounds errors: Korean words fragmented to single syllables. Keep-all/pretty text wrapping was added; two quiet cards require6x4, three cards6x3 and four cards8x3. Member data and source service178×121 design stay intact.

### 주 담당자 페이지 대조 기록


- 최종 확인: Filament04의 오른쪽 Confidential 레일은 동결 replica 자체가 붉은 글자를 붉은 면에 놓아 보이지 않는다. 동결본의 색 역할을 보존했으며 원본의 흰 레일과 차이를 남긴다. Cutfield13 밝은 tone 면의 글자와 icon은 대비를 위해 palette on 역할로 바뀌며 원본 흰 글자와 다르다. Toggle06의 12×6 행 양자화는 사진 3개 사이의 세로 공백을 줄인다.

- Portico02: 10개 목차는 계약 agenda 최대8개와 충돌하여 전체 인스턴스를 미지원으로 기록했다. 8+2개의 다른 요소로 쪼개 겉모양을 속이지 않는다. 빈 조립 영역은 누락 사고가 아닌 명시된 계약 한계다.
- Portico03/04: 넓은 수평 사진띠는 frame의 seat 종횡비 제한과 충돌해 미지원으로 기록했다. source gray 사진 자리를 임의의 가로 왜곡 frame으로 대체하지 않았다.03/04의 작은 방사형 도상은 계약 mark의 단순별로 근사해 원본6점과 다른 잔차가 있다.
- Portico05: 각 사진 자리의 번호는 계약 독립 frame이 자기 seat부터1로 센다. 여러 요소 사이 전역 순번1·2·3은 계약 데이터 슬롯이 없어3개1로 보인다.

- Lamella07: 위쪽 오른쪽 한 모서리만 휜 흰 cap 둘은 양 모서리가 휜 headline base와 달라 계약 변형에 대응하지 못한다. 그림은 임의 변형으로 우회하지 않고 GAPS에 기록했다. 본문과 독립 가로 괘선은 source 수치·반전 문맥을 복구했다.

- 최종 통합:392요소의양모드크기시트와87페이지비교PNG를주담당자가모두열어확인했다. 최종source문구추출정정후Rule13의3개카드본문은source의3줄구조를되찾았다. Lam18의1개quote본문3→4줄은독립tracking차이로잔차를명시했다.
- 최종grid검사:87페이지/231개최상위요소/543쌍에서source분리요소의신규교차0,정수span과양수12×6tracks오류0. Lam23의5.68e-14px중복경계를1e-6px허용오차로합쳐양수트랙을복구했다. 원본에이미있던교차11건은구별해기록했다.

