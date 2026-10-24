# 검수 기록 — toggle-grid

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
- 06: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 07: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 08: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 09: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 10: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 11: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 12: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.
- 03: 주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.

## 담당 요소별 상세 기록

### review-charts

# Chart element review

## gauge — inferred, no source instance

Replica02 has a111x43 ink capsule with a36x37 primary carrier and3px top inset. The inferred progress field preserves a rounded ink rail and an86%-height inner primary fill, with condensed Do Hyeon figures and lighter body labels. This adapts the switch grammar to actual progress fill; it does not introduce draggable interaction. Roles are --ink track/text and --a1 actual.0% initially left an unwanted vertical border at the capsule start despite automatic0; native review found it, so the entire CSS was rewritten without a border on the zero-width actual fill. The7% inset matches the measured3/43 source ratio, and zero now paints no actual segment. Three new0/64/100% business fixtures use2x2 minima. All six final rows and both native minimum atlases viewed after that fix. Final60 cases: all eight QA metrics zero; three fixtures copy audit zero. No number or name is hidden.

Final CSS SHA256: 8c25394e658b97789bb107979fe32bede72f2d8b03c5cd9cceed4801f8044206.

## Inferred bullet
Source02's thin ink capsule and condensed figure language supplies the new target/range geometry. Three neutral bands sit inside an ink outline; a thinner accent actual fill crosses them and an independent target tick uses a page halo. This is an inferred contract, not a source capsule relabelled as a chart. Four fixtures,70 final renders, all eight rows and both native minimum atlases inspected; nine QA checks and source-copy scan zero. Notes remain visible at the honest2x2/2x3/4x4 minima.

## Inferred sparkline
Source02's thin ink outline and accent circular carrier translate into a framed trend with ink-ringed6px points and outlined round-top mini bars. This is inferred, not a source plot. The1x1 probe exposed a real visual limitation: a24-bar row's ink borders consumed the accent fill despite automatic geometry checks staying zero. Its honest minimum is2x1; other fixtures remain1x1. The final80 renders, all eight fixture/mode rows and native minima were inspected after raising that minimum. Nine QA checks/source-copy audit zero.

## Inferred heatmap
Source02's thin ink outlines, inverse heading bands and circular carriers inform this new density matrix. Each numeric datum sits in a centred page-filled ink-outline circle over a square density field; condensed display type preserves the source emphasis language. Calendar mode has no numerical carriers and retains square day cells. This is inferred, not a mapped source chart. All58 final renders, all six fixture/mode rows and native minima inspected; nine QA checks/source-copy audit zero.

## Inferred waffle
Source02's ink-outline circles and condensed figures inform this new counted-share matrix. Every round unit retains an ink ring, including the uncounted share; actual and secondary shares remain filled palette roles. People are real CSS silhouettes with the same ringed head carrier. All60 final renders, six fixture/mode rows and native minima inspected; nine QA checks/copy audit zero. A1x2 probe preserves visible fill inside tiny ringed units; person and two-share fixtures use2x2. No source instance is claimed.

## Inferred chart-line
Source02's thin ink capsules, circular accent carriers and condensed numbers inform this new pure-line plot. Each value sits in its own centred capsule above its orange point; selection inverts that capsule to ink/page. The connected point set owns all lines and stays intact at boundary values. All four mandatory fixtures preserve exact data/markup. All112 final renders, twelve fixture/mode rows and native minima inspected, including capsule optical alignment; nine QA checks/copy audit zero and actual custom fonts loaded without error. No source pure-line instance is claimed.

Chart-line contract correction: axis labels remain nowrap and use own-count/width-based thinning, preserving all values/points. New boundary data follows0/28/67/100/93/86 instead of repeating extremes. Visual review caught touching44/44 capsule borders at3x2 even though text QA was zero: the monthly12 fixture therefore honestly requires4x2. Six longer labels and long business periods also use4x2; other minima remain2x2/3x2. All114 final cases, twelve mode/fixture rows and native minima regenerated and inspected, including capsule alignment; nine QA checks/copy fragments/font load errors zero.

Final chart-line:8px shared-token gutters preserve the L-axis and protect capsule/value bounds. All114 final light/dark cases,12 fixture rows and native minima reviewed; all9 QA counts and copy matches0. Dense12-point fixture honestly begins4x2 because its outlined value carriers touch at3x2.

Radar (inferred, no mapped base):own-axis CSS wedges draw spokes and concentric polygons; each series owns its filled polygon and actual vertex marks.3/5/8 axes and1/2/3 series use fresh Korean business content. Side axis labels align outward, protecting outer vertices; radius25cqw capped29cqh preserves space for legends. All48 final cases,6 light/dark rows and native minima viewed;9 QA counts0/copy0/font load errors0. Minima2x3,3x3,4x4 retain all labels. Deck-specific marker shape, grid weight and legend treatment follow measured source grammar.

Chart-bar inferred from replica02:thin ink outlines, rounded bar ends and condensed value capsules retain its circular-label grammar. The .on value is inverse ink/page. All6 mandatory fixtures plus zero/full and long names retain every value.144 final light/dark cases,16 fixture rows and native minima viewed;9 QA counts0/copy0/font errors0. Dense12-point and6-point charts honestly begin4x2 because bordered capsules need more width than plain labels.

Chart-donut inferred:64% hole, thin ink outlines on both ring edges, condensed figures and bordered caption capsules inferred from replica02. Exact5 mandatory fixtures plus2 new Korean business fixtures. Groups allocate width and height together; four members use2x2 at a narrow aspect ratio. All126 final light/dark cases,14 fixture rows and native minima viewed;9 QA counts0/copy0/font load errors0. Independent root:size; a donut owned by a donuts root is a normal member using the group container. All figures and names remain visible.

Final waffle font correction:figure family now explicitly lists display then body. Do Hyeon lacks the middle dot in40% ·30%; CDP v2 confirms its one dot glyph now comes from custom Pretendard, while8 glyphs stay custom Do Hyeon, with no system font. All60 cases rerendered,9 QA/copy0; changed share fixture rows in both modes and native2x2 were rechecked.

Final donut font correction:display figures and capsule captions explicitly fall back to body. Required caption 호남·충청권 신규 매장 contains a dot missing in Do Hyeon. All126 cases rerendered; changed four-member rows in both modes and native4x3 reviewed,9 QA/copy0. A direct CDP query of the second caption (not only the representative first caption) confirms11 custom Do Hyeon glyphs and1 custom Pretendard glyph in both modes; see chart-donut-punctuation-font-audit.json.

Chart-area inferred:ink-outline6px circular data marks,1.5px lines and centred capsule legends with inline rank circles. All4 mandatory fixtures stay exact plus2 new Korean data fixtures.116 final light/dark cases,12 fixture rows and native minima viewed;9 QA/copy/font errors0. Every full series owns its continuous fill and lines, with antialias coverage unioned at adjacent wedge boundaries. Axis labels stay nowrap and thin at narrow sizes; names and values remain. Initial capsule legends touched, so an8px per-member gutter and centred label/mark were added before final rerender.

Final bullet raster correction:root paint comparison found30 cases with1–2px outside paint from the large Do Hyeon percentage glyph, despite DOM geometry QA0. The glyph sat above the track, identifying figure overhang rather than target/outline. Figure right inset now adds shared gap-sm8px. All70 cases rerendered;8 final rows/native minima re-viewed,9 QA/copy0. Actual raster-paint audit now644 checked shadow cases and0 visible bleeds for the full collection.


## Slope — final inferred design
Replica에 직접적인 paired-value 도표는 없어 각 덱의 실제 점·선·라벨 문법으로 새 설계했다. 원본 복합 플롯은 이 요소로 바꾸지 않았다. 각 pair 전체가 두 시점 연결선을 소유하며, dumbbell은 이전=open / 이후=solid 표식과 머리 키를 사용해 감소항목의 의미도 유지한다. 긴 이름 칸을 실제 두 줄이 읽히는 너비로 조정했다. 3·6개 변화, 0/100 경계, 긴 이름의 dumbbell 4개 fixture의 최종 라이트·다크 62칸 전행과 native 최소칸을 확인했다. 자동9항목0, 원문6자 일치0. 자동0은 시각적 동일성을 뜻하지 않는다.


## Gauge raster repair
Do Hyeon 대형 % glyph는 DOM 상자보다 오른쪽으로 실제 잉크가 약2px 돌출했다. gauge fig에도 실제8px 우측 여유를 주고 body fallback을 명시했다. 60칸 최종 재렌더 후 전6행과 native 최소칸을 확인했고 9항목0/원문일치0이다.
전체 cached PNG2,068칸 raster검사에서 gauge/bullet 실제 칸 밖 페인트0을 확인했다. 다른 담당 list/timeline12개 이슈는 주 에이전트에게 전달했다.


## Scatter — final inferred design
Replica02의 얇은 ink outline 원·캡슐·응축형 글자 문법으로 신규 산점도 설계. 실제점은 원, 이름은 얇은 capsule, 강조이름은 ink/page 역상이며 display 뒤 body fallback을 명시했다. 점24개도 한점만 primary로 강조한다. 3/6/24점·버블·0/100축경계·긴이름6fixture 최종76칸 전행/native최소칸 양모드직접확인,9지표0/원문일치0.


## Waterfall — final inferred design
Replica02의 thin ink outline·수치capsule·응축형type로 신규waterfall 설계. 첫렌더의 큰아치는 실제to높이연결선과면끝을떨어뜨려보여서 직각plot막대로 다시썼다. 수치capsule·강조total역상은유지했다. 5fixture 최종66칸 전행/native최소칸양모드검수,9지표0/원문일치0.

### review-foundation-toggle

# Toggle foundation source review

Read-only source DOM and CDP font evidence covers all twelve immutable replica pages. All six final fixtures were viewed in light and dark at native 1280×720. All twelve source apparatus comparisons were viewed individually; complete page comparisons remain the main agent's integration review.

The cover now uses the actual Pretendard Variable source family, separate 52/850 and 122/900 title roles, source line-height/tracking, and real kicker/title/lead child structure. Topline fields remain plain text with hairlines. Numbered and wide footer child structures restore separate typography, source coordinates, and the text-free brand icon. Source05 hard line break is preserved. Header badge placement is declared source-node token data rather than a page selector.

Oswald is actually loaded by the source but absent from the README whitelist. The allowed fallback is a real Noto Sans variable font at native width75%; no transform, family alias, or synthesized width is used. Width probe BRAND STRATEGY GRID is source730.171875px versus fallback741.546875px at79/700, compared with887.296875px for Noto normal width. Actual ink-height/contour differences remain visible and are recorded as ten unexpressible font instances with proposed markup.

Inverse small muted text uses palette-only color-mix(page60%,ink) to approximate source150gray while passing both light and dark contrast; n6 had failed. Regular footer weights remain300. Final native fixture checks report no text outside or contrast failures, and the full collection six-character source-copy audit reports zero matches across174 fixtures.

A source02 direct comparison exposed the shared SVG recolorer replacing already valid palette variables with currentColor, hiding the accent switch circle. The main agent corrected that renderer; all twelve source apparatus pages were re-rendered and passed with zero text-outside or actual-font load errors. Source02 accent switch and source05 explicit two-line explanation were directly rechecked after the fix. Final standard previews contain174 fixtures in each of two modes and pass all requested page/font/resource checks.

CSS is frozen. Generator mirrors preserve the same Toggle helper and the parent's Lamella top/Filament rail changes. The global generator was not run.

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
    "09",
    "08",
    "11"
  ],
  "final_render_cases": 58,
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
    "build/native-review/table/replica-08-dark-01.png",
    "build/native-review/table/replica-08-dark-02.png",
    "build/native-review/table/replica-08-dark-03.png",
    "build/native-review/table/replica-08-dark-04.png",
    "build/native-review/table/replica-08-dark-05.png",
    "build/native-review/table/replica-08-light-01.png",
    "build/native-review/table/replica-08-light-02.png",
    "build/native-review/table/replica-08-light-03.png",
    "build/native-review/table/replica-08-light-04.png",
    "build/native-review/table/replica-08-light-05.png",
    "build/native-review/table/replica-09-dark-01.png",
    "build/native-review/table/replica-09-dark-02.png",
    "build/native-review/table/replica-09-dark-03.png",
    "build/native-review/table/replica-09-dark-04.png",
    "build/native-review/table/replica-09-dark-05.png",
    "build/native-review/table/replica-09-light-01.png",
    "build/native-review/table/replica-09-light-02.png",
    "build/native-review/table/replica-09-light-03.png",
    "build/native-review/table/replica-09-light-04.png",
    "build/native-review/table/replica-09-light-05.png",
    "build/native-review/table/replica-11-dark-01.png",
    "build/native-review/table/replica-11-dark-02.png",
    "build/native-review/table/replica-11-dark-03.png",
    "build/native-review/table/replica-11-dark-04.png",
    "build/native-review/table/replica-11-dark-05.png",
    "build/native-review/table/replica-11-light-01.png",
    "build/native-review/table/replica-11-light-02.png",
    "build/native-review/table/replica-11-light-03.png",
    "build/native-review/table/replica-11-light-04.png",
    "build/native-review/table/replica-11-light-05.png"
  ],
  "corrections": [
    "Changed fixed table layout to source auto layout after manual inspection found a50% label column instead of25%.",
    "Explicit member-count-based row heights retain equal rows when longer labels wrap."
  ],
  "decisions": [
    "Neutral5 represents source gray rules (#777); ink represents solid label panels.",
    "Empty thead is kept and headerless values center only when no header row is present.",
    "Source09 bold text and source11 hard line break are retained in source reconstruction markup, with equivalent emphasis in new Korean fixtures."
  ],
  "known_remaining_differences": [
    "Preview palette replaces original colors.",
    "Width caps reduce text size in narrow tall slots.",
    "Source phrases occur only in map/reassembled data."
  ],
  "source_size_comparison": [
    {
      "page": "09",
      "bbox": [
        139,
        308,
        1060,
        277
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
      "css_sha256": "ba4ed9211dbe2ebf87447c951b27c7e52a3ed566eddf31ebdb82cafa637418ca"
    },
    {
      "page": "08",
      "bbox": [
        139,
        308,
        1060,
        277
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
      "css_sha256": "ba4ed9211dbe2ebf87447c951b27c7e52a3ed566eddf31ebdb82cafa637418ca"
    },
    {
      "page": "11",
      "bbox": [
        139,
        308,
        1060,
        277
      ],
      "comparison": "build/sourcebox-systems/table-11.png",
      "geometry_qa": {
        "outside": 0,
        "clipped": 0,
        "member_outside": 0,
        "overlaps": 0,
        "shape_clipped": 0,
        "painted_outside": 0
      },
      "source_palette_contrast_only": [],
      "css_sha256": "ba4ed9211dbe2ebf87447c951b27c7e52a3ed566eddf31ebdb82cafa637418ca"
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
    "Inferred architecture from replica12 definition-band language:102px bands,8px gaps,36.5%ink labels,24/19px type and sharp neutral5rules.",
    "Contract module counts divide the quiet body into actual columns, retaining one strong left name per layer.",
    "Three-layer minimum3×3; long five-layer minimum4×4or3×6.",
    "All30native cases reviewed in both modes; all8current automatic metrics zero.",
    "Replica12 gray body uses neutral2 consistently with the shared gray-box role. All30final native cells re-reviewed in both modes after correction."
  ],
  "known_remaining_differences": [
    "This architecture is inferred; the unsupported replica12 definition table remains unexpressible in the map.",
    "Palette ink/page roles invert in dark mode; literal source black is not fixed in element CSS.",
    "Module chips center text, whereas source definition prose is left aligned."
  ]
}

## matrix-nine

{
  "replica_pages": [],
  "final_render_cases": 26,
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
    "Inferred nine-box uses source12 102px row,36.5% black label field,24:19 type and8px row air; source12 unsupported table remains a gap.",
    "Below220px cell width label moves above body; root width775px sets intrinsic header grid row, preserving geometry without self-container-query misuse."
  ],
  "corrections": [
    "Replaced undefined type19 cap with valid type20; continuous source-ratio sizing remains.",
    "Manual review found automatic0 but a blank half-row below narrow-cell labels; intrinsic header row corrected it. Final26 cases re-rendered and all native cells reviewed."
  ],
  "differences": [
    "The source has separated two-field definition rows; inferred nine-box combines this grammar with three actual labels on each axis."
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
    "Inferred positioning keeps square black device fields,medium500labels and neutral5fine axes from09/12; own mark uses a1with a doubled ink border.",
    "No rounded card shell or image marker is introduced. Neutral logo seats retain square geometry."
  ],
  "corrections": [],
  "differences": [
    "The source has no competitor positioning map; actual low/high endpoint fields and new logistics copy are inferred."
  ]
}

## roadmap

{
  "replica_pages": [
    "09/12 (inferred language only)"
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
    "The sharp orange heading,ink owner strip,neutral2body and neutral5fine rules derive from the46px heading and102px/8px definition rows.",
    "All durations retain their actual endpoints; no source table is reinterpreted as duration data."
  ],
  "corrections": [],
  "differences": [
    "This contract is absent from the replica. The19%owner allocation belongs to the duration contract rather than the original36.5%definition-column allocation."
  ]
}

## matrix

{
  "replica_pages": [
    "12 (inferred language only)",
    "03 (nested list)"
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
    "Source12supplies the36.5%ink label field,neutral2body,sharp edges and24/19hierarchy. Each quadrant retains the left label and right definition instead of turning them into generic top-heading cards.",
    "SWOTplaces its letter and name in the same left label field,and the independently scoped source03gray list in the right field. The letter/name halves share the field center; on highlights only the label field."
  ],
  "corrections": [
    "The first top-heading draft did not preserve the source left-label grammar. The whole CSS was rewritten around the36.5:63.5split.",
    "Height guards now use24/102and19/102source ratios; narrow field widths still limit the text.",
    "Natural spaces in the new Korean activity names avoid isolated trailing syllables at4x3/4x4."
  ],
  "differences": [
    "No source matrix or SWOTexists. Source12table remains unsupported in the map; this is an inferred matrix contract with no claim that the original definition panel is expressed."
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
    "Source-absent flowchart uses replica09 sharp label/body separation,orange start/end bands,black question/work headings,gray definition surfaces and neutral5 fine rules.",
    "All arrows remain one element-owned explicit directional connection; no semantic state is hidden."
  ],
  "corrections": [],
  "differences": [
    "Inferred process nodes,not a mapped replica scene. All18 native panels manually reviewed,including min6x3 and4x3."
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
    "Absent swimlane extends replica09 sharp black owner labels,neutral2 fields,neutral5 rules and a1 start/end planes; questions use inverse ink.",
    "Owners occupy protected header fractions; literal node columns and all explicit connector directions are retained."
  ],
  "corrections": [],
  "differences": [
    "Inferred owner flow. All14 final native panels across light/dark manually reviewed with long owner names,all states and both owner counts."
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
    "Absent recursive tree extends replica09 sharp inverse black question planes,neutral2 outcome fields,neutral5 borders and accent recommended outcomes.",
    "Each actual question/outcome queries its own size for shared-token type; all answer conditions and maximum three-question depth are preserved."
  ],
  "corrections": [],
  "differences": [
    "Inferred tree. All12 final native light/dark panels directly inspected; min4x3 simple and12x6 maximum-depth fixture."
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
    "Absent journey uses source09 sharp inverse heading bands, neutral2 fields, neutral5 rules and24/19 typography relation.",
    "Minimum4x3 for three stages and8x4 for seven retains all semantic content."
  ],
  "corrections": [],
  "differences": [
    "The curve is inferred because this replica has no journey; original deck primitives determine field and hierarchy."
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
    "Absent Sankey uses source09 inverse heading bands, sharp neutral2 planes and neutral5 rules.",
    "Preserved actual heading padding and figure clearance; honest minima6x4 flat /8x4 nested.",
    "0/100 source shares and4/2 local splits use one consistent ribbon thickness scale without hiding labels."
  ],
  "corrections": [
    "Manual review found tight unpadded title bands despite automatic0; added real padding and value clearance, then raised minimum to preserve them."
  ],
  "differences": [
    "No source Sankey exists; proportional connected flows are inferred from measured deck primitives."
  ],
  "supplemental_geometry": "sankey-sharebounds.json:18cases0errors,share scale and every connection"
}


### review-text-final-exceptions

최종 cardinality 정정과 검수

03의세번째 목록은 실제1개 item이며 계약2–8개를 위반한다. 본문의 줄을 임의 항목으로 분해하지 않고 원본1item 전체를GAP으로 전환했다. replica-03-one fixture를 삭제하고 실제 같은 새 한국어2문단 list-two-long-inferred로 바꿨다. min3x3을 실제 두 모드에서 확인했다. 원본이 아닌 추론 fixture라는 사실을 설명에 명시했다.

CSS에서는 지원하지 않는 count1 전용 dead rule만 제거했다. 유효한2개 이상 source목록/중첩.check의 형태는 그대로다.60cases9지표0/raster0/font load0, native3패널 전부 확인,289개 소유 fixture의 원본6자 중복0.

### review-text-transfer-diagrams

# Callout transfer review

The absent callout extends replica12 measured43-unit black capsules and40-unit orange circular marks. A sharp thin-bordered black sentence band contains a compact rounded accent emphasis in condensed Do Hyeon, with regular body copy around it. Three-unit optical top padding centers that condensed emphasis. The optional circle carries an icon at60% of its diameter. The element owns only the paragraph and optional icon. It is a size container in a grid slot and reserves a compact flexible caption share when placed after a seat in the mandatory foundation stack.

Final cases: 80; all nine QA counts, strict containment, copy matches and raster bleed: 0.

All final native cells directly opened at original resolution in lossless panels, or verified identical to earlier directly opened cells. Both modes and all actual minima inspected. Mandatory showcase markup/data preserved.

Own paragraph and optional icon only; no invented state or ancestor condition. Compact flex basis reserves sentence caption share in mandatory stack; grid retains allocated size. New Korean long business copy replaces source-independent generic six-character common phrasing to keep the conservative copy audit at zero.

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
    "Source03 independent outlined title and neutral body plus source06 accent index circle inform the inferred agenda."
  ],
  "corrections": [
    "Removed generic whole-card outline and centered25% index row. Restored separate title/body, full Korean business notes, active inverse title.",
    "Do Hyeon actual glyph dy=-2.203125 at28px corrected with.16em optical top padding; all20 final cases chip_alignment0."
  ],
  "differences": [
    "Small entries use56px title floor for full Korean heading; absent source agenda is explicitly inferred."
  ],
  "supplemental_geometry": "20 cases raster0;12 final native panels manually reviewed."
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
    "Source06 Do Hyeon400 index plus22px inverse capsule and18/300 explanatory copy supply the bare metric hierarchy. Stats uses own member containers and count-controlled dividers."
  ],
  "corrections": [
    "Fresh CSS preserves index/capsule/explanation hierarchy without a containing gray face. Added actual stats3 fixture; unit minimum type12.",
    "Limited divider painter to last real division after9x4 showed a rounding-induced extra edge line. All final rows rerendered and directly reviewed;34 nonstats PNG hashes identical."
  ],
  "differences": [
    "No bare source metric; source capsule hierarchy is inferred rather than claimed as a source instance."
  ],
  "supplemental_geometry": "44 final9QA0/raster0/copy0;28 native panels directly reviewed."
}


### review-text-transfer

# Transferred inferred elements — final review

card: replica03 topcell 330×45, Do Hyeon 28px, square gray description field, body20/350 and thin dark outline에서 fresh 작성. 06 원형 강조를 mark에 적용. note 길이에 영향받던 title 위치를 고정된 의미별 트랙으로 바로잡고 최소칸을 6x4/8x4/10x4로 정직하게 올림. 6개 mandatory fixture의 원래 마크업·데이터 유지,52칸. 숫자 mark의 실제 글리프 중심은 icon이 없는 자기 자식 조건으로 보정.
quote: 03/06 직각 회색면·검정 author띠·원형 강조 문법에서 추론. avatar가 회색면에 묻히던 문제는 n-3와 가는 outline으로 해결. 사진없는 author의 빈 열 제거. min4x4/5x4,20칸.
tag: 03/06의 검정 label띠·주황 강조를 inline 계약으로 추론. 2x1에서는 부모 prose의 한글이 부자연스러워 min3x1로 정정. 검정 label의 마지막 글자만 줄바꿈되던 문제는 tag 전체 nowrap으로 해결. 40칸.

이 항목들은 replica의 특정 요소를 직접 옮긴 base가 아니라 명시적으로 추론한 계약 요소다. 최종 수정 뒤 모든 fixture·모든 허용 크기·light/dark의 native 칸을 직접 보았고, 9QA·6자 원문 중복·실제 폰트 fallback·raster 초과를 별도 감사했다.

### review-text

# Text element provenance and review decisions

The fixed replicas were read as evidence and were never edited. Sample HTML supplies mandatory data/markup only; no sample element CSS was read or reused.

## Per-leaf provenance

- card: inferred; no independently expressible source instance.
- pill: 06:base, 06:same-as:06.
- callout: inferred; no independently expressible source instance.
- tag: inferred; no independently expressible source instance.
- list: 03:base, 03:same-as:03.
- quote: inferred; no independently expressible source instance.
- headline: 03:base, 03:same-as:03.
- prose: 06:base, 06:same-as:06.
- metric: inferred; no independently expressible source instance.
- agenda: inferred; no independently expressible source instance.
- person: 04:base.

## Recorded corrections and decisions

- List03 is an actual2/3/1-member set, not a generic three-item fixture. Native30px/20px sides,32px marker gutter,35px/26px first-row positions and37px/29px gaps are measured from the source. The original19px one-off final Latin item is represented by the general20px hierarchy rather than an item-position font rule.
- Person04 owns its complete regular dividers as people pseudo elements, not sibling-position arrows/cards. Source38px gap-center positions correspond to32.1023%/67.8977%; small layouts draw only real occupied-column dividers. Number circles scale against width and capsule-height context.
- Source list data must retain internal br lines inside1/2/3 items. The factory newline-to-item split was bypassed with faithful sourceMarkup. All three native source list cases now have outside0.
- Pill06 is399×43 with40px circle left2,16px gap and22px name left58. Its index actually uses27px400-weight Do Hyeon. The earlier centered group and397px estimate were corrected.
- Compact check lists have transparent inherited context and no source bullet-panel side/top inset; source base remains unchanged.

## Inferred elements

card, callout, tag, quote, metric, agenda. Each has its own build/inferred-spec-<leaf>.json citing this deck’s measured source primitive, an inferred description and fresh business fixtures. These files never claim a source base.

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

