# 검수 기록 — rulemark

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
- 05: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 03: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 04: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 06: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 07: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 08: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 09: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 10: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 11: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 12: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 02: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 13: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.

## 담당 요소별 상세 기록

### review-charts

# Chart element review

## gauge — inferred, no source instance

Replica11 uses a strict monochrome hierarchy, square fields and1px rules. The inferred meter frames its field with two thin rules, gives the empty rail a1px ink outline and draws the actual value in solid ink. It has no source gauge base. Figure weight700 and the firm body-name hierarchy remain consistent with the deck number/box labels. All foreground and data roles use --ink/--page, preserving the source neutral emphasis rather than introducing an accent hue. Three new business fixtures cover0/64/100% and long names at2x2 minima. All six final rows and both native minima atlases viewed. Final60 cases: all eight QA metrics zero; three fixtures copy audit zero. Intrinsic numeric widths preserve100%, and no text is hidden.

Final CSS SHA256: 2dd8afe557e4ab05328e3412aba74bebf520fd1cc2c377e9d4037a2c95c7cd2d.

## Inferred bullet
Source11's monochrome fields and thin straight rules inform this new range/target contract. The neutral1/3/5 qualitative bands retain an ink actual fill, ink target with page halo, outline and bottom rule. All70 final renders, every mode/fixture row and both native minimum atlases were inspected. Nine QA checks and normalized source-copy audit are zero; no source plot is claimed for this inferred leaf.

## Inferred sparkline
Source12 supplies square plot marks, monochrome values and straight rules: the new trend uses4px square carriers,2px ink connectors,76.25%-width mini bars and a thin unlabelled bottom frame. Up/down remain semantic good/bad variants. No source grouped chart is flattened or claimed as a mapped instance. All80 final renders, every fixture/mode row and native1x1 minima viewed; nine geometry/paint/contrast checks and source-copy audit zero.

## Inferred heatmap
Source11/12 monochrome fields, inverse headings and straight one-pixel rules inform this new density grid. The maximum density reaches neutral n5, matching the source's gray series role; an initial half-strength neutral mix was widened after visual review to make differences clear while retaining verified text contrast. Square calendar cells retain the same ink outline. All58 final renders, all six fixture/mode rows and native minima viewed; nine QA checks and source-copy audit zero. This is inferred, not a source plot mapping.

## Inferred waffle
Source11/12 monochrome fields and straight rules inform outlined square counted units with strong ink figures. The main counted share is ink; the second share explicitly uses source gray tone-1, so the two shares remain distinct. Visual review caught that tone-2 would equal the main ink share even though geometry QA was zero; the fixture was corrected to its genuine second data role. Figures mode draws CSS people. All60 final renders, six mode/fixture rows and native minima viewed; nine QA checks/source-copy audit zero. CDP actual font records confirm custom Pretendard Variable with no font load errors. No source waffle instance is claimed.

## Inferred chart-line
Source12's monochrome square marks,14px regular values and straight one-pixel rules inform a new pure-line chart. The2px ink line carries4px neutral squares and one6px ink emphasis. Four mandatory showcases preserve exact markup/data and their genuine .pt.on; the README showcase and chart quality clauses supplement the abbreviated table's missing .on wording (root confirmed this intake interpretation). Axis labels are nowrap and are thinned by own count/width below700px while all values/points stay visible. A natural0/28/67/100/93/86 fixture exercises boundaries without repeated sawteeth. Native review found page-backed values breaking the L-axis; an8px shared-token inline plot gutter now keeps them apart and aligns clamped end labels to the same gutter. All116 final cases, twelve fixture/mode rows and native minima inspected; nine QA checks, source-copy fragments and font load errors zero. No source pure-line instance is claimed.

Final chart-line:8px shared-token gutters keep value backplates off the L-axis and align the end-label insets. The final whole-file rewrite was rendered again; every light/dark fixture row and native minimum was viewed. All9 geometry/contrast/paint checks and copy checks are zero. Axis labels remain nowrap and are thinned at narrow sizes; all values and points remain.

Radar (inferred, no mapped base):own-axis CSS wedges draw spokes and concentric polygons; each series owns its filled polygon and actual vertex marks.3/5/8 axes and1/2/3 series use fresh Korean business content. Side axis labels align outward, protecting outer vertices; radius25cqw capped29cqh preserves space for legends. All48 final cases,6 light/dark rows and native minima viewed;9 QA counts0/copy0/font load errors0. Minima2x3,3x3,4x4 retain all labels. Deck-specific marker shape, grid weight and legend treatment follow measured source grammar.

Chart-bar inferred from replica12:measured76.25% bar-to-pitch width,14px-body hierarchy, straight axes and source neutral-series roles. All6 mandatory fixtures retain exact data; new fixtures use quiet neutral ranks around one ink emphasis. The first new fixtures repeated tone2 ink beside .on ink, so those authored secondary members were changed to different neutral ranks; source mandatory fixtures stayed exact. All148 final light/dark cases,16 fixture rows and native minima reviewed after that correction;9 QA counts0/copy0/font errors0. The source grouped two-series plot remains unexpressible.

Chart-donut inferred from replica11/12:62% hole, ink share/neutral track, strong figures and straight ruled captions. All5 mandatory fixture markup/data preserved plus2 new Korean business cases. Group4 becomes2x2 in narrow-aspect slots.126 final light/dark cases,14 fixture rows and native minima viewed;9 QA counts0/copy0/font errors0. Independent root:size; nested donut members share the owning donuts container without introducing new markup.

Chart-area inferred:monochrome ranked fills,4px square data marks,2px contours and strong ruled legends. All4 mandatory fixtures stay exact plus2 new Korean data fixtures.116 final light/dark cases,12 fixture rows and native minima viewed;9 QA/copy/font errors0. Every full series owns its continuous fill and lines, with antialias coverage unioned at adjacent wedge boundaries. Axis labels stay nowrap and thin at narrow sizes; names and values remain. Series ranks use source n5/ink then quiet n3.


## Slope — final inferred design
Replica에 직접적인 paired-value 도표는 없어 각 덱의 실제 점·선·라벨 문법으로 새 설계했다. 원본 복합 플롯은 이 요소로 바꾸지 않았다. 각 pair 전체가 두 시점 연결선을 소유하며, dumbbell은 이전=open / 이후=solid 표식과 머리 키를 사용해 감소항목의 의미도 유지한다. 긴 이름 칸을 실제 두 줄이 읽히는 너비로 조정했다. 3·6개 변화, 0/100 경계, 긴 이름의 dumbbell 4개 fixture의 최종 라이트·다크 62칸 전행과 native 최소칸을 확인했다. 자동9항목0, 원문6자 일치0. 자동0은 시각적 동일성을 뜻하지 않는다.


## Scatter — final inferred design
원본12의1px ink 축과 square mark, 무채색 단계 문법으로 신규 scatter를 설계했다. 일반점n5/n3, 강조점ink/12px로 하나만 명확히 구별한다. bubble도 같은 무채색과outline을 사용한다. sourcegrouped는gap유지.6fixture 최종76칸 전행/native최소칸 양모드직접확인,9지표0/원문일치0.


## Waterfall — final inferred design
Replica12의 직각흑백plot·1px ink축·무채색단계에서신규waterfall을설계했다. n5증가/n3감소/ink total 역할을덱전체순위에맞췄다. sourcegrouped는gap유지.5fixture 최종66칸 전행/native최소칸양모드검수,9지표0/원문일치0.

### review-foundation-title-track

# Rulemark foundation title tracking

The immutable source common `.title` is actual custom Pretendard Variable48/750 with60px line-height and−.04em (−1.92px) tracking. The collection kit title token is−.015em; the existing foundation head title clause now multiplies that shared token by2.6666666667. The kit, cover typography, body elements, and map remain unchanged. The same existing generator clause is mirrored without running the generator. No nowrap rule was added.

Native browser source04 and foundation both render 핵심 요소 as one line with167.265625px text width and normal white-space. CDP reports the actual custom Pretendard Variable font with no loading errors. The existing map origin is y144 while the source title block starts y143; this pre-existing1px origin difference is recorded and was outside the requested tracking repair.

Final standard previews contain179 fixtures in each of light and dark and pass. All six foundation PNGs were rendered and directly viewed at1280×720 with zero text-outside, contrast, or font-load failures. The completed shared56 element proof refresh covers2506 size cases: all nine QA totals are zero, no proof is stale, and all native PNG pixels are identical to the previously inspected versions.

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

## table

{
  "replica_pages": [
    "05"
  ],
  "source_css_reused": false,
  "final_render_cases": 36,
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
    "build/native-review/table/groups-3-pick-dark-01.png",
    "build/native-review/table/groups-3-pick-dark-02.png",
    "build/native-review/table/groups-3-pick-dark-03.png",
    "build/native-review/table/groups-3-pick-dark-04.png",
    "build/native-review/table/groups-3-pick-dark-05.png",
    "build/native-review/table/groups-3-pick-light-01.png",
    "build/native-review/table/groups-3-pick-light-02.png",
    "build/native-review/table/groups-3-pick-light-03.png",
    "build/native-review/table/groups-3-pick-light-04.png",
    "build/native-review/table/groups-3-pick-light-05.png",
    "build/native-review/table/replica-05-dark-01.png",
    "build/native-review/table/replica-05-dark-02.png",
    "build/native-review/table/replica-05-dark-03.png",
    "build/native-review/table/replica-05-dark-04.png",
    "build/native-review/table/replica-05-dark-05.png",
    "build/native-review/table/replica-05-dark-06.png",
    "build/native-review/table/replica-05-light-01.png",
    "build/native-review/table/replica-05-light-02.png",
    "build/native-review/table/replica-05-light-03.png",
    "build/native-review/table/replica-05-light-04.png",
    "build/native-review/table/replica-05-light-05.png",
    "build/native-review/table/replica-05-light-06.png"
  ],
  "decisions": [
    "Merged first-column groups retain the source grouping. 2×3 minimum for short source-shaped copy; 4×3 for a5-column long-copy fixture. Width caps reduce tall/narrow text; no copy hidden."
  ],
  "replica_unchanged": true,
  "known_remaining_differences": [
    "Fixture copy is newly written Korean business content.",
    "Palette is supplied by the preview style and intentionally differs from source colors.",
    "Responsive type is capped at large slot sizes and wraps at narrow sizes."
  ],
  "source_size_comparison": [
    {
      "page": "05",
      "bbox": [
        640,
        254,
        574,
        400
      ],
      "comparison": "build/sourcebox-systems/table-05.png",
      "geometry_qa": {
        "outside": 0,
        "clipped": 0,
        "member_outside": 0,
        "overlaps": 0,
        "shape_clipped": 0,
        "painted_outside": 0
      },
      "source_palette_contrast_only": [],
      "css_sha256": "2b31fba0677b10bbe082feaee45a912396dc763d9eb758f8d09c6cadf8fe6406"
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
    "Architecture absent from replica. Inferred from05grouped table574×400,57px ink header,171px group height,20/17px hierarchy and1.3px closed rules.",
    "Each layer uses a full-width ink name over equal pale module compartments, square corners and no invented ornament.",
    "Three-layer minimum3×3; five long layers4×4or3×6. All30final native cases directly reviewed in both modes.",
    "Line heights use shared name/body tokens; final PNGs are byte-identical to their prior computed-value render."
  ],
  "known_remaining_differences": [
    "Stacked architecture is inferred, not a mapped replica instance.",
    "Canonical palette ink/page roles invert in dark mode.",
    "Fixture text is newly written Korean business content."
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
    "Inferred nine-box takes source05 square1.3px closed rules,57px ink head bands,20:17 type hierarchy,neutral1 grouping plane.",
    "Ink/page inversion expresses on; four neutral tones preserve monochrome design. Both actual three-label axes remain visible."
  ],
  "corrections": [],
  "differences": [
    "Source05 is a grouped table, not a nine-box. Slim gutters separate inferred matrix cells rather than faking collapsed-table markup."
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
    "Inferred positioning keeps source05 square ink fields,1.3px ink axes and700-weight name hierarchy; own marker is an inverse page square with2.6px frame.",
    "Both endpoints are real low/high contract labels, high-y upward. No colored accent is introduced into this monochrome grammar."
  ],
  "corrections": [],
  "differences": [
    "No positioning map occurs in Rulemark replica; new marks and Korean logistics labels are inferred."
  ]
}

## roadmap

{
  "replica_pages": [
    "05 (inferred language only)"
  ],
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
    "Source05closed1.3px rules and57px ink headings supply a closed duration table. Owners retain the neutral1merged-cell role,with20/17copyhierarchy.",
    "An on path reverses ink/page roles. Neutral band levels remain monochrome."
  ],
  "corrections": [],
  "differences": [
    "No source roadmap exists. Period coordinates and duration lanes are contract structure inferred through the measured table language."
  ]
}

## matrix

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
    "Source-absent quadrants extend replica05 closed table rules, inverse heading band, and20/17 hierarchy; SWOT keeps real kick/name/list contract slots.",
    "The axes remain explicit and minima are4x3 ordinary and6x4 or4x6 SWOT."
  ],
  "corrections": [],
  "differences": [
    "Inferred matrix; not a direct source instance. All16 native light/dark panels were inspected with no visible clipping, collisions or broken rules."
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
    "Source-absent flowchart follows replica05 inverse headings,closed1.3stroke boxes,20/17 hierarchy and neutral question field.",
    "Whole node set and all explicit directional links belong to one root; member-count conditions alone select two or three columns."
  ],
  "corrections": [],
  "differences": [
    "Inferred flowchart. All18 native panels inspected in light and dark; min6x3 six nodes and4x3 four nodes."
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
    "Absent swimlane extends replica05 closed1.3stroke fields,inverse black owner labels and700-weight hierarchy; questions retain neutral1 plane.",
    "Node column coordinates and all explicit directional arrows remain literal,with protected long owner labels above their faces."
  ],
  "corrections": [],
  "differences": [
    "Inferred contract. All14 native light/dark panels reviewed,including both owner counts,all states and6x3/8x4 minima."
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
    "Absent recursive tree extends replica05 inverse black question planes,closed1.3stroke outcome boxes and700-weight hierarchy.",
    "Actual member size containers preserve readable12-plus shared type at deepest outcomes; maximum three-question depth remains present at min12x6."
  ],
  "corrections": [],
  "differences": [
    "Inferred decision tree. All12 native light/dark panels directly inspected; simple3outcome tree min4x3 and no branches hidden."
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
    "Absent journey uses source05 closed1.3 rules, inverse title bands,20/17 hierarchy and neutral1 emphasized field.",
    "Honest minima4x3 and8x4 retain every touchpoint note and pain line."
  ],
  "corrections": [],
  "differences": [
    "No mapped journey exists; emotion data and continuous curve are inferred from measured deck primitives."
  ]
}

## sankey

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
    "build/native-review/sankey/nested-4-2-dark-01.png",
    "build/native-review/sankey/nested-4-2-dark-02.png",
    "build/native-review/sankey/nested-4-2-dark-03.png",
    "build/native-review/sankey/nested-4-2-light-01.png",
    "build/native-review/sankey/nested-4-2-light-02.png",
    "build/native-review/sankey/nested-4-2-light-03.png",
    "build/native-review/sankey/routes-6-dark-01.png",
    "build/native-review/sankey/routes-6-dark-02.png",
    "build/native-review/sankey/routes-6-dark-03.png",
    "build/native-review/sankey/routes-6-light-01.png",
    "build/native-review/sankey/routes-6-light-02.png",
    "build/native-review/sankey/routes-6-light-03.png"
  ],
  "decisions": [
    "Absent Sankey uses source05 closed1.3 rules, inverse20/17 heading hierarchy and neutral1 main-path face.",
    "Preserves padded inverse labels and figure clearance with minima6x4 flat /8x4 nested.",
    "Source0/100 and nested4/2 retain every value and actual proportional band thickness."
  ],
  "corrections": [],
  "differences": [
    "No source Sankey; flow topology is inferred from measured deck primitives."
  ],
  "supplemental_geometry": "sankey-sharebounds.json:18cases0errors,consistent share scale and all connections"
}


### review-text-final-exceptions

최종 줄 구조 정정과 검수

13 카드.note는 실제 plain span3개+br2개의 원본줄 구조다. map의 가짜 leading newline이 factory에서 첫br로 발명되고, keep-all/pretty가 source강제줄에 추가감김을 만들어5–6줄로 늘어났다. 실제세줄 sourceMarkup을 plain span/br로 보존하고 가짜 첫newline을 제거했다. 카드.note는normal/wrap, 직접span은pre이며320px 아래에서는normal로 돌아간다. br없는 자연 한국어 문장만 keep-all/pretty로 단어를 보존한다. source13 새 fixture도 원본 문구를 쓰지 않은 실제한국어3줄 형태다.

원본은 줄마다 tracking을 개별로 맞췄으나, 계약에 없는 inline추적값은 전달하지 않았다. 공통공유 tracking 때문에 실제자폭에 미세한 잔차가 있으나 source13 세 개 모두3줄/좌표/타입 위계를 직접 확인했다.02 agenda의 본문18개가 실제white인 것을 다시 확인해foundation_context:on을 지도에 추가했다.

60cases9지표0/raster0/font load0, 마지막native12패널/source3개모두직접확인했다.289개소유fixture 원본6자 중복0.

### review-text-transfer-diagrams

# Callout transfer review

The absent concluding callout combines replica03 measured41-unit black circle and20-unit medium lead with one-unit rules from02/05 and the source bold heading weight. The conclusion stays open on the page instead of adding a filled card. A seven-unit optical shift aligns the icon with the text beneath its fourteen-unit top-rule inset. The optional icon occupies56% of its circular carrier. The element owns only the paragraph and optional icon. It is a size container in a grid slot and reserves a compact flexible caption share when placed after a seat in the mandatory foundation stack.

Final cases: 80; all nine QA counts, strict containment, copy matches and raster bleed: 0.

All final native cells directly opened at original resolution in lossless panels, or verified identical to earlier directly opened cells. Both modes and all actual minima inspected. Mandatory showcase markup/data preserved.

Own paragraph and optional icon only; no invented state or ancestor condition. Compact flex basis reserves sentence caption share in mandatory stack; grid retains allocated size. New Korean long business copy replaces source-independent generic six-character common phrasing to keep the conservative copy audit at zero.

### review-text-transfer-systems

# Systems element review

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
    "Source13 actual40/750 left-aligned evidence figure,28/367 horizontal inset and18px/26.666667 copy provide the hierarchy. Bare contract removes containing card surface."
  ],
  "corrections": [
    "Fresh source-based typography replaces generic bottom rule. Actual source left alignment retained rather than inferred centered alignment. Added stats3 fixture with own member containers and bounded dividers."
  ],
  "differences": [
    "No bare metric instance exists; title/figure/note composition is inferred from source evidence typography without a containing face."
  ],
  "supplemental_geometry": "44 final cases9QA0/raster0/copy0; all28 native panels directly reviewed."
}


### review-text-transfer

# Transferred inferred elements — final review

person: 03/13의 직각 칸·얇은 괘선·흑백 위계에서 추론. 첫 초안은 note 길이에 따라 사진/이름 높이가 달라져 자동9QA가 0이어도 직접 검수에서 거절. fresh grid 40%/12%/잔여 트랙으로 다시 작성하여 1·2·3명 및 자기 자식 list가 있는 변형을 맞춤. optional list는 실제 계약 data-el의 중첩 요소이며 다른 담당 list CSS는 수정하지 않음. min4x4/4x6/6x4,38칸.
pill: 03/13의 네모 면과 흑백 반전 문법으로 추론. on은 ink/page, 기본·line·quiet는 중립 역할. 높이 비례 padding과 nowrap으로 한줄 표식 유지. min3x1/4x1,78칸.
quote: 03/13의 흰 면·하단 가는 괘선·굵은 검정 강조를 인용 계약에 적용한 추론. 작은 author와 선택 avatar 유지, 빈 avatar열 제거. min4x4/5x4,20칸.
tag: 03/13의 회색 단계·검정 괘선을 inline 문구에 적용. tag 전체 nowrap, highlight n-2/ink로 단색 역할 유지. min3x1,40칸.

이 항목들은 replica의 특정 요소를 직접 옮긴 base가 아니라 명시적으로 추론한 계약 요소다. 최종 수정 뒤 모든 fixture·모든 허용 크기·light/dark의 native 칸을 직접 보았고, 9QA·6자 원문 중복·실제 폰트 fallback·raster 초과를 별도 감사했다.

추가 실제 픽셀 검수: tag의 작은 글자 행 위쪽 회색 면이 1px 넘어간 24칸을 9QA와 별도로 검출. inline의 세로 padding을 0으로 바꾸고 가로 padding·밑괘선은 유지하여 원인을 제거했다. 마지막 전체 재렌더 뒤 실제 raster 검사를 반복한다.

### review-text

# Text element provenance and review decisions

The fixed replicas were read as evidence and were never edited. Sample HTML supplies mandatory data/markup only; no sample element CSS was read or reused.

## Per-leaf provenance

- card: 13:base, 13:same-as:13, 06:variant:.quiet, 08:same-as:06.
- pill: inferred; no independently expressible source instance.
- callout: inferred; no independently expressible source instance.
- tag: inferred; no independently expressible source instance.
- list: 03:variant:.num, 05:same-as:03, 12:same-as:03.
- quote: inferred; no independently expressible source instance.
- headline: 03:variant:.big, 05:base, 07:same-as:05, 09:same-as:05, 11:same-as:05, 12:same-as:05.
- prose: 07:variant:.cols.
- metric: inferred; no independently expressible source instance.
- agenda: 02:base.
- person: inferred; no independently expressible source instance.

## Recorded corrections and decisions

- Agenda02 initial42px/17px/233px-height estimate was corrected to40px/700 index,18px title/14px Latin note and bbox298,325,916,259. Source columns248px separated86px and rows110px separated39px.
- Card13 fig40px/750 and note18px/26.667px supersede initial34px/17px estimates. Native figure top84px, explanation top172px and quiet06 kick/name/note hierarchy are separately measured.
- Numbered list is the only mapped source list variant. Its dot/check base treatments are inferred. Legend ranks are monochrome:n5,ink,n3,n7,n9, consistent with chart owner.
- Headline03 is25px/500,37.5px lines; all05/07/09/11/12 body statements are20px/500,30px lines.05 is the honest base and03 the big variant. Earlier proportional850px type40.9 was wrong.
- Numbered list actual source is18px/400 on27.9px lines,16px750 ordinal,18px marker column,16px gutter,10px gap. Earlier17px/1.6 estimates and wide-shallow12px query were removed.03/05/12 native positions now match and outside0.
- Notice07 retains source2/10/2/7 span line boundaries and complete first/third bold paragraphs.49px column gap,5.111px paragraph gap and automatic fill restore x297/x781 and y312/y373.984, with outside0. Uniform−.28px tracking replaces source line-specific fitted tracking, leaving small line-end differences without page CSS.

## Inferred elements

pill, callout, tag, quote, metric, person. Each has its own build/inferred-spec-<leaf>.json citing this deck’s measured source primitive, an inferred description and fresh business fixtures. These files never claim a source base.

## Validation state

Browser sheets and probes are recorded in review/validation and build/probes. A zero automated result alone is insufficient: native source-box comparisons found and corrected font, gap, shape, padding-reference, missing-avatar and quotation collisions. Each final proof must match the latest source hashes. Final fixture minima are selected after native smaller-candidate review; initial conservative comments are not final evidence.

True inline tag/hl boxes keep natural text width. Declared container-type:size is inert on a non-atomic inline by browser definition; shared type steps and the enclosing real prose paragraph provide context. This explicit functional limitation is not hidden with an invented fixed8em box.

### Final integration corrections
- Checked-list rotated ticks were translated within their own marker carrier to remove actual raster paint beyond the left cell boundary; text, palette roles and minimum cells are unchanged.

### 주 담당자 페이지 대조 기록


- 최종 확인: Filament04의 오른쪽 Confidential 레일은 동결 replica 자체가 붉은 글자를 붉은 면에 놓아 보이지 않는다. 동결본의 색 역할을 보존했으며 원본의 흰 레일과 차이를 남긴다. Cutfield13 밝은 tone 면의 글자와 icon은 대비를 위해 palette on 역할로 바뀌며 원본 흰 글자와 다르다. Toggle06의 12×6 행 양자화는 사진 3개 사이의 세로 공백을 줄인다.

- Portico02: 10개 목차는 계약 agenda 최대8개와 충돌하여 전체 인스턴스를 미지원으로 기록했다. 8+2개의 다른 요소로 쪼개 겉모양을 속이지 않는다. 빈 조립 영역은 누락 사고가 아닌 명시된 계약 한계다.
- Portico03/04: 넓은 수평 사진띠는 frame의 seat 종횡비 제한과 충돌해 미지원으로 기록했다. source gray 사진 자리를 임의의 가로 왜곡 frame으로 대체하지 않았다.03/04의 작은 방사형 도상은 계약 mark의 단순별로 근사해 원본6점과 다른 잔차가 있다.
- Portico05: 각 사진 자리의 번호는 계약 독립 frame이 자기 seat부터1로 센다. 여러 요소 사이 전역 순번1·2·3은 계약 데이터 슬롯이 없어3개1로 보인다.

- Lamella07: 위쪽 오른쪽 한 모서리만 휜 흰 cap 둘은 양 모서리가 휜 headline base와 달라 계약 변형에 대응하지 못한다. 그림은 임의 변형으로 우회하지 않고 GAPS에 기록했다. 본문과 독립 가로 괘선은 source 수치·반전 문맥을 복구했다.

- 최종 통합:392요소의양모드크기시트와87페이지비교PNG를주담당자가모두열어확인했다. 최종source문구추출정정후Rule13의3개카드본문은source의3줄구조를되찾았다. Lam18의1개quote본문3→4줄은독립tracking차이로잔차를명시했다.
- 최종grid검사:87페이지/231개최상위요소/543쌍에서source분리요소의신규교차0,정수span과양수12×6tracks오류0. Lam23의5.68e-14px중복경계를1e-6px허용오차로합쳐양수트랙을복구했다. 원본에이미있던교차11건은구별해기록했다.

