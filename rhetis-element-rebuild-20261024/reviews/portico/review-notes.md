# 검수 기록 — portico

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
- 04: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 05: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 07: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 08: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 09: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 10: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 11: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 12: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 13: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 03: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 06: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.

## 담당 요소별 상세 기록

### review-charts

# Chart element review

## chart-donut — replica 13

Source: four separate 172px rings; hole diameter 136px (79.06976744%); 40px bold percentage, 16px amount, 20px semibold name below. The library keeps each ring a separate single-donut element. Grouped mandatory fixtures apply the same geometry with member-count layout, not a four-sector chart.

The source has a two-line primary figure and separate currency amount. This is represented by `.fig > b + small`; ordinary inline percentage-unit markup in mandatory fixtures stays inline. This real formatting difference uses child-presence conditions only. Source reconstruction preserves the source's inconsistent ring shares (50/60/70/80) and visible figures (50/40/30/20); new fixtures use internally consistent values.

Roles: primary share --a1; empty track --n-3; hole --page; figure/name --ink; secondary amount --n-7. Review sheets use the canonical preview palette, so their orange/neutral colors intentionally differ from the source teal/sand palette.

Minimums: standalone and long-name fixtures 2x2; three members 4x3; four members 3x3. Smaller standalone 1-column or 1-row probes were visually cramped even where text-bounds checks passed. At accepted minima all numbers, units and names remain visible. Four members become 2x2 at narrow widths; three members stack only in sufficiently tall, narrow boxes.

Visual corrections made by full CSS replacement: preserve circular shape under flex shrink; reserve long-name height; align grouped rings and first name baselines independently of wrapped name length; keep currency amount beneath the whole percentage; adapt grouping at small widths. No secondary text is hidden.

Final review: all 10 fixture rows in light and dark viewed, all 20 row sheets; native minimum atlas in both modes viewed; replica | 12x6 | minimum comparison viewed. Final source-hash render: 194 cases, outside/clipped/hidden/member_outside/overlaps/contrast all zero. Copy audit: 10 fixtures, zero source phrase matches.

CSS SHA256: 410b7da41f3c9f3d9ed09fe719c3c5740e65f004a1003ec3ce2945f05b8fd7d5.

## gauge — inferred, no source instance

Replica11 phase fields use square bands, full-height compartments and1px rules. The inferred meter keeps a square n-3 remaining track, an a1 actual band, strong Montserrat figures, body-name weight and a fine cell divider. This is not a source gauge base. New0/64/100% business fixtures with long names use2x2 minima. The intrinsic figure field avoids cutting100%; names grow upward without colliding with it. All six final rows and both native minimum atlases viewed. Final60 cases: all eight QA metrics zero, three fixtures copy audit zero. No part is hidden.

Final CSS SHA256: 7a3c2574542fbd678468fc7046d8f134010c7f5302f46511f0794bbb37d258b1.

## Inferred bullet
Source11 square phase bands, strong Montserrat hierarchy and thin compartment rules inform this new target/range element. Three neutral range bands, a thinner actual fill, a target tick and a bottom divider remain distinct. This is inferred, not mapped to a source plot. All70 final renders, all eight mode/fixture rows and both minimum atlases reviewed; nine automatic checks and copy audit zero. Four-row group minimum4x4 preserves its explanatory notes.

## Inferred sparkline
Source09 contributes straight compartment marks and evenly spaced horizontal rules. The mini trend has square4px carriers,66.8%-width bars and thin unlabelled background rules; it contains no axis labels, scale ticks or text. Background rules are interpreted as deck framing rather than data axes. The grouped source plot remains unexpressible and is not flattened into this inferred contract. All80 final renders, eight mode/fixture rows and native1x1 minima viewed; nine QA checks/source-copy audit zero.

## Inferred heatmap
Source11's square phase bands, sand heading role n3 and one-pixel compartment rules inform this new density matrix. Strong Montserrat numbers, separate row names and straight header cells keep its structural hierarchy. Calendar mode retains square day cells and the same heading bands. All58 final renders, every fixture/mode row and native minima reviewed; nine QA checks/copy audit zero. This is inferred and not mapped to a source chart.

## Inferred waffle
Source13's square funding compartments and strong numerical hierarchy inform the new counted-share matrix. Straight neutral outlines separate all units; bold Montserrat figures and strong names preserve the deck hierarchy. Figures mode uses CSS people while retaining the same unit-count logic. All60 final renders, all six fixture/mode rows and native minima viewed; nine QA checks/source-copy audit zero. This is inferred, not a replacement for the mapped funding donuts.

## Inferred chart-line
Source09's square plot compartments, one-pixel horizontal rules and13px labels inform a new equal-step line chart. Square4px carriers and a7px selected carrier preserve its precise rectilinear rhythm; axis labels sit beneath their own thin compartment rules. Grouped source bars and its growth overlay remain gaps, rather than being flattened into this inferred line. All four mandatory showcases retain exact data/markup. All112 final renders, twelve fixture/mode rows and native minima viewed; nine QA checks/source-copy audit zero, actual custom fonts loaded without error.

Chart-line guide refinement: horizontal rules now have an explicit lower stacking level than the data connectors, preserving uninterrupted foreground strokes where a point segment crosses a guide. All112 final cases, twelve mode/fixture rows and native minima regenerated and viewed; nine QA checks and font load errors remain zero.

Chart-line contract correction: axis labels remain nowrap and use count/width-based thinning for dense narrow plots, preserving every value and marker. New boundary data follows0/28/67/100/93/86 rather than repeated extremes. Updated minima monthly12=3x2, six longer labels4x2, long periods4x2. All116 final cases, twelve mode/fixture rows and native minima regenerated and viewed; nine QA checks, copied-source fragments and font load errors zero. Guides remain behind the data strokes.

Final chart-line:8px shared-token gutters keep value backplates off the L-axis and align the end-label insets. The final whole-file rewrite was rendered again; every light/dark fixture row and native minimum was viewed. All9 geometry/contrast/paint checks and copy checks are zero. Axis labels remain nowrap and are thinned at narrow sizes; all values and points remain.

Radar (inferred, no mapped base):own-axis CSS wedges draw spokes and concentric polygons; each series owns its filled polygon and actual vertex marks.3/5/8 axes and1/2/3 series use fresh Korean business content. Side axis labels align outward, protecting outer vertices; radius25cqw capped29cqh preserves space for legends. All48 final cases,6 light/dark rows and native minima viewed;9 QA counts0/copy0/font load errors0. Minima2x3,3x3,4x4 retain all labels. Deck-specific marker shape, grid weight and legend treatment follow measured source grammar.

Chart-bar inferred:6 exact mandatory fixtures plus0/100 and long names; all148 final light/dark cases,16 fixture rows and native minima viewed.9 QA counts0/copy0/font load errors0. Vertical labels are nowrap/thinned, all values stay visible; horizontal names wrap in a dedicated column with a separate value gutter. Filament uses genuinely thin outlined bars and palette-ranked outlines; its first draft ignored secondary outline tones, found visually and fixed by complete rewrite before final render. Portico uses measured66.8% bar-to-pitch width and straight1px plot rules. Existing grouped source plots remain gaps.

Final actual-font correction for waffle:figure font-family is now display followed by body. CDP child-glyph inspection had found that Montserrat lacked 명/중 and used system Noto Sans CJK KR. All60 cases were rerendered,9 QA/copy0; changed people20 fixture rows in both modes and native2x2 were reviewed. Font probe v2 now reports only custom Montserrat(5 glyphs) and custom Pretendard(3 glyphs) for that mixed figure. Numerical Montserrat identity stays intact.

Chart-area inferred from replica09:square4px marks,1px rules,30% ranked fills and padded neutral legend bands. All4 exact mandatory fixtures plus2 new Korean cases. An initial QA0 minimum showed the last long legend surface covering the top of value93; own-series-count>=3 now reserves96px/18cqh header space, and stacked3 begins honestly3x3 so five numerical ticks retain spacing. All114 final light/dark cases,12 fixture rows and native minima reviewed;9 QA/copy/font errors0. Transparent wedge boundaries union coverage without seams; cumulative opaque bands reverse layer order. The original grouped source chart remains a gap.


## Slope — final inferred design
Replica에 직접적인 paired-value 도표는 없어 각 덱의 실제 점·선·라벨 문법으로 새 설계했다. 원본 복합 플롯은 이 요소로 바꾸지 않았다. 각 pair 전체가 두 시점 연결선을 소유하며, dumbbell은 이전=open / 이후=solid 표식과 머리 키를 사용해 감소항목의 의미도 유지한다. 긴 이름 칸을 실제 두 줄이 읽히는 너비로 조정했다. 3·6개 변화, 0/100 경계, 긴 이름의 dumbbell 4개 fixture의 최종 라이트·다크 62칸 전행과 native 최소칸을 확인했다. 자동9항목0, 원문6자 일치0. 자동0은 시각적 동일성을 뜻하지 않는다.


## Scatter — final inferred design
원본09의 square mark·1px plot compartment·sand neutral(n3)label band 문법으로 absent scatter를 새 설계했다. 차트 점 이름에는 가는 밑줄, 두 축 이름에는 직각중립면을 사용하고 실제값은 자체axis에 비례한다. 원본grouped는gap유지. 3/6/24점·버블·0/100축경계·긴이름6fixture 최종76칸 전행/native최소칸 양모드직접확인, 9지표0/원문일치0.


## Waterfall — final inferred design
Replica09의 직각bar·1px괘선·정확한칸분리 문법에서 신규waterfall을설계했다. 막대폭66.8%와 단계label위1px룰을 사용했다. 원본grouped는gap유지했다. 각move가실제from/to막대와to높이연결선을소유한다.5fixture 최종66칸 전행/native최소칸 양모드직접검수,9지표0/원문일치0.

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

주 담당자가13페이지를개별대조하는중 확인한 차이: 긴 가로 사진띠(03/04)는 image-frame의 비율 계약 밖이라 GAPS로 남겨 회색 배너를 임의의 요소로 만들지 않았다. 06 라벨만 있는 비포함 타원 묶음,09 grouped bar+단독원형 강조는 계약지원 없음으로 GAPS. 공식 Lucide 별/plus의 선은 replica의 채운방사별과 다르다. on 대비를위해 얕은색의 name/role/note는ink로 바뀔수있다. 12×6 좌표양자화로 카드·사진 상자 위치와행간에 차이가남는다. 03 세로구분선 누락은 foundation furniture로 보완검토중이다. 06 card fig굵기/열분할은 실제비교에서결함을발견해수정담당자에게돌렸다.

### review-systems

# Systems element review

## flowchart

{
  "replica_pages": [
    "08"
  ],
  "final_render_cases": 34,
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
  "node_text_outside": 0,
  "pseudo_shape_outside": 0,
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/flowchart/replica-08-dark-01.png",
    "build/native-review/flowchart/replica-08-dark-02.png",
    "build/native-review/flowchart/replica-08-dark-03.png",
    "build/native-review/flowchart/replica-08-dark-04.png",
    "build/native-review/flowchart/replica-08-light-01.png",
    "build/native-review/flowchart/replica-08-light-02.png",
    "build/native-review/flowchart/replica-08-light-03.png",
    "build/native-review/flowchart/replica-08-light-04.png",
    "build/native-review/flowchart/routing-4-nodes-turns-dark-01.png",
    "build/native-review/flowchart/routing-4-nodes-turns-dark-02.png",
    "build/native-review/flowchart/routing-4-nodes-turns-dark-03.png",
    "build/native-review/flowchart/routing-4-nodes-turns-dark-04.png",
    "build/native-review/flowchart/routing-4-nodes-turns-dark-05.png",
    "build/native-review/flowchart/routing-4-nodes-turns-light-01.png",
    "build/native-review/flowchart/routing-4-nodes-turns-light-02.png",
    "build/native-review/flowchart/routing-4-nodes-turns-light-03.png",
    "build/native-review/flowchart/routing-4-nodes-turns-light-04.png",
    "build/native-review/flowchart/routing-4-nodes-turns-light-05.png"
  ],
  "decisions": [
    "All three independent source/charge pairs remain one element; no six-step sequence is invented.",
    "Root-approved standard b+p matches the actual source heading/paragraph hierarchy without adding a class.",
    "Source21/16/23px hierarchy,6px gap,20px indent,95px circles and arrow path geometry become own-box ratios.",
    "Accent text uses a1-7 because a1 fails supplied light-style contrast2.58.",
    "White source circles become neutral1 and faint arrows neutral5 because white-on-cream brightness cannot be preserved literally in canonical roles.",
    "Six-ray ornament size is bounded by text size and box width; it stays within narrow slots.",
    "A four-node inferred loop demonstrates all four connector directions and a quiet question panel.",
    "Source08 #d8d2bb fine row/ask rules use neutral4 consistently with global roles; neutral3 remains the different #dcd3b9sand header role. All34final native cases re-reviewed in both modes after correction."
  ],
  "corrections": [
    "Contrast depth correction.",
    "Ornament bound in narrow and wide-low slots.",
    "Width900px caps prevent long two-row result labels from becoming four giant lines.",
    "Exact-source-size comparison found paragraph width280px against source300px. Explicit real paragraph width100% preserves its20pxindent without reducing the300pxcopy field; the original second row returns to2lines and its title restores source height. All34native light/darkcases were rerendered and manually inspected after the correction."
  ],
  "known_remaining_differences": [
    "Canonical palette replaces source hues and the circle brightness relationship.",
    "Widths and row heights drive type caps and wrapping in small slots.",
    "New Korean fixtures do not repeat source phrases.",
    "Question node and turning/returning connectors are inferred from the same fine-rule/circle-arrow grammar."
  ],
  "source_size_comparison": [
    {
      "page": "08",
      "bbox": [
        397,
        155,
        795,
        565
      ],
      "comparison": "build/sourcebox-systems/flowchart-08.png",
      "geometry_qa": {
        "outside": 0,
        "clipped": 0,
        "member_outside": 0,
        "overlaps": 0,
        "shape_clipped": 0,
        "painted_outside": 0
      },
      "source_palette_contrast_only": [
        {
          "text": "Basic: 월 10만 원",
          "ratio": 3.23,
          "required": 4.5,
          "foreground": [
            151,
            141,
            97
          ],
          "background": [
            252,
            252,
            244
          ],
          "rect": [
            949.125,
            221,
            166.75,
            28
          ]
        },
        {
          "text": "Pro: 월 50만 원",
          "ratio": 3.23,
          "required": 4.5,
          "foreground": [
            151,
            141,
            97
          ],
          "background": [
            252,
            252,
            244
          ],
          "rect": [
            958.421875,
            252.046875,
            148.15625,
            28
          ]
        },
        {
          "text": "거래액의",
          "ratio": 3.23,
          "required": 4.5,
          "foreground": [
            151,
            141,
            97
          ],
          "background": [
            252,
            252,
            244
          ],
          "rect": [
            992.734375,
            409.328125,
            79.515625,
            28
          ]
        },
        {
          "text": "5~10%",
          "ratio": 3.23,
          "required": 4.5,
          "foreground": [
            151,
            141,
            97
          ],
          "background": [
            252,
            252,
            244
          ],
          "rect": [
            993.75,
            440.375,
            77.484375,
            28
          ]
        },
        {
          "text": "리포트 건당/",
          "ratio": 3.23,
          "required": 4.5,
          "foreground": [
            151,
            141,
            97
          ],
          "background": [
            252,
            252,
            244
          ],
          "rect": [
            975.875,
            597.65625,
            113.25,
            28
          ]
        },
        {
          "text": "API 호출당 과금",
          "ratio": 3.23,
          "required": 4.5,
          "foreground": [
            151,
            141,
            97
          ],
          "background": [
            252,
            252,
            244
          ],
          "rect": [
            959,
            628.703125,
            146.984375,
            28
          ]
        }
      ],
      "css_sha256": "332a717ffa59f1aca3570a0617ea585be712f0206642e444c733bf7c82b71e87"
    }
  ]
}

## positioning

{
  "replica_pages": [
    "10"
  ],
  "final_render_cases": 34,
  "automatic": {
    "outside": 0,
    "clipped": 0,
    "hidden": 0,
    "member_outside": 0,
    "overlaps": 0,
    "contrast": 0
  },
  "outside_mark": 0,
  "not_round": 0,
  "name_outside_inner_circle": 0,
  "all_native_cells_visually_reviewed": true,
  "native_panels": [
    "build/native-review/positioning/regional-6-long-logo-dark-01.png",
    "build/native-review/positioning/regional-6-long-logo-dark-02.png",
    "build/native-review/positioning/regional-6-long-logo-dark-03.png",
    "build/native-review/positioning/regional-6-long-logo-dark-04.png",
    "build/native-review/positioning/regional-6-long-logo-dark-05.png",
    "build/native-review/positioning/regional-6-long-logo-light-01.png",
    "build/native-review/positioning/regional-6-long-logo-light-02.png",
    "build/native-review/positioning/regional-6-long-logo-light-03.png",
    "build/native-review/positioning/regional-6-long-logo-light-04.png",
    "build/native-review/positioning/regional-6-long-logo-light-05.png",
    "build/native-review/positioning/replica-10-dark-01.png",
    "build/native-review/positioning/replica-10-dark-02.png",
    "build/native-review/positioning/replica-10-dark-03.png",
    "build/native-review/positioning/replica-10-dark-04.png",
    "build/native-review/positioning/replica-10-dark-05.png",
    "build/native-review/positioning/replica-10-light-01.png",
    "build/native-review/positioning/replica-10-light-02.png",
    "build/native-review/positioning/replica-10-light-03.png",
    "build/native-review/positioning/replica-10-light-04.png",
    "build/native-review/positioning/replica-10-light-05.png"
  ],
  "decisions": [
    "634×489envelope and562×401plot,27px dots,168px own circle,15px ring and30px ornament derive from source.",
    "Preserves the source11.5px rightward regular-name offset and7px gap below a dot.",
    "Four endpoint labels remain real fields; y increases downward as the source cost axis.",
    "Circle diameters use the smaller available width/height scale and edge distance.",
    "Page-backed labels keep axis rules out of text; endpoint label widths may expand or shift in small slots.",
    "A muted circular logo placeholder is inferred from the ring grammar; on-logo size is55%of its circle."
  ],
  "known_remaining_differences": [
    "Source endpoint label container widths may shrink at source size without changing visible text positions, to keep boxes inside the mapped visible envelope.",
    "Canonical palette replaces original olive/teal hues.",
    "Fixture content is new Korean business text; long names wrap at small widths.",
    "Logo representation is inferred because source10 has text names only."
  ],
  "source_size_comparison": [
    {
      "page": "10",
      "bbox": [
        24,
        200,
        634,
        489
      ],
      "comparison": "build/sourcebox-systems/positioning-10.png",
      "geometry_qa": {
        "outside": 0,
        "clipped": 0,
        "member_outside": 0,
        "overlaps": 0,
        "shape_clipped": 0,
        "painted_outside": 0
      },
      "source_palette_contrast_only": [],
      "css_sha256": "7d51f9ca5749205ab316ebe4b666225a0a3bf87112204b5241923299e94654f2"
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
    "Absent from replica. Inferred from replica07 282×239feature cells,26px pill labels,12px pill insets,16px body type and1px sand rules.",
    "Compact a1/on pills identify each architecture layer; unfilled module columns remain separated by n3 rules.",
    "Three layers pass3×3; five long layers pass4×4or3×6. Larger original provisional minima were lowered after inspecting smaller slots.",
    "All30final native cases in both palettes visually inspected; chip_alignment and six other metrics zero.",
    "Fine source07 partition lines use neutral4 consistently with global roles; neutral3 remains the separate sand header role. Final all30native cases re-reviewed after role correction."
  ],
  "known_remaining_differences": [
    "Stacked architecture is inferred and is not a mapped source instance.",
    "Palette roles replace literal source hues; fixture content is new Korean business text."
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
    "Inferred nine-box from source07 open 282×239 feature regions, 20/16 title-body hierarchy, fine n4 partitions; no source nine-box claim.",
    "Nine-box density reduces broad feature-region insets; both axes remain visible."
  ],
  "corrections": [
    "Neutral3 tone changed title from accent7 to ordinary ink after 4.27/4.26 contrast failure; final30 native cases re-rendered and visually reviewed."
  ],
  "differences": [
    "The deck has four broad feature blocks rather than nine cells; the semantic matrix is inferred without adding unsupported pills or keyword slots."
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
    "Inferred table uses source07 20:16 hierarchy,cream ground,n4 warm fine partitions and shared n3sand header strip role.",
    "Point heading uses a1/on,point body a1-1-soft, row-label reading uses a1-7. Open square outer boundaries preserve the deck language."
  ],
  "corrections": [],
  "differences": [
    "No table occurs in the frozen replica; this is an inferred contract element."
  ]
}

## roadmap

{
  "replica_pages": [
    "11 (inferred language only)"
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
    "The source54px Phase band over298px fields supplies a54/422root-height guard and24/650centered hierarchy. The real strategy remains a timeline.",
    "Sand period strip,neutral4fine partitions and neutral7quiet bands preserve shared deck roles."
  ],
  "corrections": [],
  "differences": [
    "No source roadmap exists. This duration contract is inferred from source11 bands; its duration tracks are new contract structure."
  ],
  "supplemental_geometry": "review/validation/roadmap-memberbounds.json:30cases0failures"
}

## matrix

{
  "replica_pages": [
    "07 (inferred language only)",
    "10 (nested list)"
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
    "Source07open282×239feature fields supply square unfilled planes,neutral4fine divisions and20/16strong/bodytype hierarchy.",
    "Ordinary headings share a fixed relative start and notes follow their own row,so note wrapping cannot move the heading. The cadence is inferred for the absent quadrant contract.",
    "SWOT retains the same open divisions and the independently scoped source10circle-plus list. Accent reading uses shared depth7and strong on uses accent/on."
  ],
  "corrections": [
    "The first height coefficients counted the member border box although the size query reports its content box. Source20/16ratios now use the actual content reference234×191.",
    "An upper-pinned draft left the short-text full fixture unbalanced; the ordinary quadrant uses a fixed relative title/body cadence at all sizes."
  ],
  "differences": [
    "No source quadrant or SWOTexists. Axis structure and title/body cadence are inferred; no source scene is claimed for these2×2fields."
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
    "Source-absent swimlane extends replica07 open service fields,neutral4 fine divisions,20/700 heading hierarchy,neutral3 owner stripes and a1-7 reading emphasis.",
    "Contract column coordinates remain literal; owner headings occupy a protected first-column fraction above the node faces."
  ],
  "corrections": [],
  "differences": [
    "Inferred owner-flow diagram; original source08 remains its mapped pair-flowchart. All14 native light/dark panels directly reviewed."
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
    "Absent tree extends replica07 open planes and neutral4 rules; questions use the neutral3 header role with ink,while open outcomes use a1-7 reading accent.",
    "Question/outcome own size containers keep their nested typography responsive; maximum three-question depth requires12x6."
  ],
  "corrections": [
    "Fixed38 contrast failures caused by accent reading text on neutral3,using the established neutral-header ink role.",
    "Reduced the deepest question type from ancestor dimensions to own-member dimensions to restore internal white space."
  ],
  "differences": [
    "Inferred tree. All12 final native light/dark panels inspected; simple three-outcome fixture admits4x3 and retains all branches."
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
    "Absent journey uses source07 open column faces, neutral4 right/bottom rules,20/16 hierarchy and emphasis reading a1-7.",
    "Each stage preserves all note and pain fields; minima4x3 and8x4 follow actual readable stage counts."
  ],
  "corrections": [],
  "differences": [
    "No direct journey source; emotion data and connected curve are inferred from measured open-face grammar."
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
    "Absent Sankey uses source07 open faces with neutral4 right/bottom rules, sand source band and20/16 hierarchy.",
    "Strong source value uses shared a1-7 reading emphasis; its smaller unit uses ink for normal-text contrast.",
    "Both fixtures have honest6x3 minimum and preserve all fields;0/100 and nested4/2 branches remain semantic."
  ],
  "corrections": [
    "Small source unit failed4.5 contrast on sand at4.27; ink role restores contrast without changing palette or value emphasis."
  ],
  "differences": [
    "No source Sankey; proportional connected flows are inferred using measured deck primitives."
  ],
  "supplemental_geometry": "sankey-sharebounds.json:24cases0errors;consistent direct/nested share scale and all connections"
}


### review-text-final-exceptions

최종 예외 정정과 검수

카드06의 권위는 고정 replica HTML이다. map의18/11 추정은20/15로 정정했고, 숫자는40/700이다.727px 상자에서 fig x74, 이름/본문x207의 비율을 직접 구현했다. 이름20px/28px 행간, 본문15px/21.75px 행간을 공유 type clamp로 보존했다. 수치 블록은 실제 .fig 자식 조건으로만 분기하며 카드용으로 정의되지 않은 .h 클래스는 만들지 않았다.

카드03.on은18/14px, icon22px·이름x33의 실측으로 복구했고,04는 icon15px·이름x20·본문x21/y51을 복구했다. 실제 높이140/145/171px를 잘못 축소하던250px query를100px로 낮췄다.10.quiet는42/38 padding,20/16px,12px 간격과 오른쪽7점 장식을 복구했다. headline06/08/11/13은 ink와 실제 Pretendard,07은 의미에 맞는 .big.center의 강조색으로 분리했다.

02 agenda10개는 계약2–8개 범위를 벗어나 원본 전체를GAP으로 전환했다. 원본을 잘라8개라고 주장하지 않았으며 새 한국어8항목 fixture만 남겼다. min3x3은 양모드 실제 읽힘으로 확인했다.

card176 + headline58 + agenda34 =268cases의9지표0, raster0, font load0. native35패널과 source22개 실제 크기3패널을 마지막 수정 후 직접 확인했다. 사진/타원형 등의 기존GAP는 유지한다. sourcecheck 아이콘의 점선 원은 preview 대역이므로 실제 Lucide 모양과 다른 점을 남긴다.

### review-text-transfer-diagrams

# Callout transfer review

The source has no concluding callout. Replica11 measured54-unit sharp matte headings with28-unit insets become a neutral sand sentence band and one-unit primary rule. Sixteen-unit regular copy and twenty-unit bold emphasis preserve the source text hierarchy. The unfilled icon is derived from03/cover measured22/35-unit open stars; it introduces no circular badge or rounded card. The element owns only the paragraph and optional icon. It is a size container in a grid slot and reserves a compact flexible caption share when placed after a seat in the mandatory foundation stack.

Final cases: 80; all nine QA counts, strict containment, copy matches and raster bleed: 0.

All final native cells directly opened at original resolution in lossless panels, or verified identical to earlier directly opened cells. Both modes and all actual minima inspected. Mandatory showcase markup/data preserved.

Own paragraph and optional icon only; no invented state or ancestor condition. Compact flex basis reserves sentence caption share in mandatory stack; grid retains allocated size. New Korean long business copy replaces source-independent generic six-character common phrasing to keep the conservative copy audit at zero.

### review-text-transfer

# Transferred inferred elements — final review

quote: source의 면/가는선/문자강조 문법을 유지하며 사진없는by의빈column을제거했다. min4x4/5x4,20칸 전행/native최소칸 양모드직접검수,9QA0/원문6자0/폰트로드0.

### review-text

# Text element provenance and review decisions

The fixed replicas were read as evidence and were never edited. Sample HTML supplies mandatory data/markup only; no sample element CSS was read or reused.

## Per-leaf provenance

- card: 04:base, 04:same-as:04, 03:variant:.on, 05:same-as:04, 07:same-as:04, 10:variant:.quiet, 06:variant:.on, 06:variant:.quiet, 06:same-as:04.
- pill: 05:base, 05:same-as:05, 07:same-as:05.
- callout: inferred; no independently expressible source instance.
- tag: 07:base, 07:same-as:07.
- list: 10:variant:.divided.
- quote: inferred; no independently expressible source instance.
- headline: 06:base, 11:same-as:06, 07:variant:.center, 13:variant:.center, 08:same-as:06.
- prose: 06:base, 11:same-as:06.
- metric: 09:base, 09:same-as:09.
- agenda: 02:base.
- person: 12:base.

## Recorded corrections and decisions

- 08 name/note/charge nodes belong to the complete systems.flowchart3pair element. Three card and three prose overlays were removed from the text map; the left304×185 headline remains independent.
- 08 actual heading is23px/700, not the initial28px description. In304×185 native the heading has2×31.05px lines, its note4×23.2px at16px, with30px gap. Own.note presence selects the measured intro form. Center07 is30px/40.5px in380×81; center13 is20px/28px in495×28.
- 09 metric initial18px/40px/dotted-leader narrative was wrong. Actual stat is20px name at58/42,16px note at58/74,50px figure right50/top35,15px star, bottom rule and no leader. The name star is an allowed Lucide asterisk seat rather than a new class.
- Person12 initial root cqw padding referenced its people parent and shrank the content. Padding was removed from the size container, with43px/32px native inset transferred to actual child margins. Source20px name/15px bio/18px role/118px portrait ratios are restored.
- Root approved regular own-people zebra for every member count; standalone people stay transparent. Even-member n2 faces use n3/ink image placeholders so the picture outline remains visible in both modes.
- Pill/card-kick roundness cannot derive from the zero radius token; their actual26px carrier is derived from shared pad24px at26/24, retaining source13px-or-larger capsule corners.
- Card05/07 nested pill formerly had zero intrinsic width because size containment removed its contribution. A real26px-high kick slot and the left-anchored natural pill surface preserve the nested contract. Native card05 name253.469/source253.5, note303.453/source303.5;07 name238.547/source238.5,note284.531/source284.5,keywords374.094/source374.06.
- The capsule is teal/cream with11px type,12px inset and26px height. The keyword surface is near-white n1 with n7 text; earlier white capsule/sand keyword assumptions were wrong.
- The source08 left title was ink; the common reading-emphasis a1-7 role is a deliberate palette-position decision, not a source RGB claim.
- Mandatory3-KPI min4x4 split primary numerals;6x4 is the verified correction. Four-card headings use balanced text to avoid isolated one-character endings; agenda also balances complete words at verified3x3 minima.

## Inferred elements

callout, quote. Each has its own build/inferred-spec-<leaf>.json citing this deck’s measured source primitive, an inferred description and fresh business fixtures. These files never claim a source base.

## Validation state

Browser sheets and probes are recorded in review/validation and build/probes. A zero automated result alone is insufficient: native source-box comparisons found and corrected font, gap, shape, padding-reference, missing-avatar and quotation collisions. Each final proof must match the latest source hashes. Final fixture minima are selected after native smaller-candidate review; initial conservative comments are not final evidence.

True inline tag/hl boxes keep natural text width. Declared container-type:size is inert on a non-atomic inline by browser definition; shared type steps and the enclosing real prose paragraph provide context. This explicit functional limitation is not hidden with an invented fixed8em box.

### Final integration corrections
- Checked-list rotated ticks were translated within their own marker carrier to remove actual raster paint beyond the left cell boundary; text, palette roles and minimum cells are unchanged.
- An inline tag has natural width but its painted padding needs a taller host line box. Only paragraphs actually containing the contracted tag reserve its line+padding height in prose and card notes. Agenda uses zero-minimum grid rows and entries to prevent min-content border expansion at3x3.

### 주 담당자 페이지 대조 기록


- 최종 확인: Filament04의 오른쪽 Confidential 레일은 동결 replica 자체가 붉은 글자를 붉은 면에 놓아 보이지 않는다. 동결본의 색 역할을 보존했으며 원본의 흰 레일과 차이를 남긴다. Cutfield13 밝은 tone 면의 글자와 icon은 대비를 위해 palette on 역할로 바뀌며 원본 흰 글자와 다르다. Toggle06의 12×6 행 양자화는 사진 3개 사이의 세로 공백을 줄인다.

- Portico02: 10개 목차는 계약 agenda 최대8개와 충돌하여 전체 인스턴스를 미지원으로 기록했다. 8+2개의 다른 요소로 쪼개 겉모양을 속이지 않는다. 빈 조립 영역은 누락 사고가 아닌 명시된 계약 한계다.
- Portico03/04: 넓은 수평 사진띠는 frame의 seat 종횡비 제한과 충돌해 미지원으로 기록했다. source gray 사진 자리를 임의의 가로 왜곡 frame으로 대체하지 않았다.03/04의 작은 방사형 도상은 계약 mark의 단순별로 근사해 원본6점과 다른 잔차가 있다.
- Portico05: 각 사진 자리의 번호는 계약 독립 frame이 자기 seat부터1로 센다. 여러 요소 사이 전역 순번1·2·3은 계약 데이터 슬롯이 없어3개1로 보인다.

- Lamella07: 위쪽 오른쪽 한 모서리만 휜 흰 cap 둘은 양 모서리가 휜 headline base와 달라 계약 변형에 대응하지 못한다. 그림은 임의 변형으로 우회하지 않고 GAPS에 기록했다. 본문과 독립 가로 괘선은 source 수치·반전 문맥을 복구했다.

- 최종 통합:392요소의양모드크기시트와87페이지비교PNG를주담당자가모두열어확인했다. 최종source문구추출정정후Rule13의3개카드본문은source의3줄구조를되찾았다. Lam18의1개quote본문3→4줄은독립tracking차이로잔차를명시했다.
- 최종grid검사:87페이지/231개최상위요소/543쌍에서source분리요소의신규교차0,정수span과양수12×6tracks오류0. Lam23의5.68e-14px중복경계를1e-6px허용오차로합쳐양수트랙을복구했다. 원본에이미있던교차11건은구별해기록했다.

