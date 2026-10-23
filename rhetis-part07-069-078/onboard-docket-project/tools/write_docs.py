from pathlib import Path
P=Path(__file__).parent;C=P/'onboard-docket'
shapes={
'card':'A softly rounded document panel centers a balanced content block with fixed title and description tracks. Circular numbered or icon marks sit above the title; selected panels use the principal accent as a complete surface.',
'pill':'A single line sits in a bounded capsule with a circular leading mark. Its height remains controlled even when the assigned grid slot is tall, so it reads as a label rather than a circular card.',
'callout':'A broad neutral capsule contains one centered conclusion. Bold words use a deep accent role and an optional small icon leads the line without changing its optical center.',
'tag':'A small accent capsule labels a local detail while inline highlights use a quiet accent wash. Both forms remain visually subordinate to the heading they accompany.',
'list':'Neutral capsule tracks organize each item. Numbered lists separate a circular automatic counter, an accent title capsule and a right-hand explanation; divided lists become simple ruled document rows.',
'quote':'A narrow accent rule anchors a substantial quotation, followed by a compact author block. A dark reverse highlight can emphasize a short phrase, echoing the welcome slide.',
'headline':'A strong sans heading sits inside a generously padded block. Kicker, main phrase and note follow distinct levels, with a single deep accent emphasis and optional fully accented surface.',
'prose':'Readable paragraphs retain an open document rhythm without ornamental frames. Two-column passages use a compact discrete type step before their text could generate an unwanted third column.',
'metric':'A bare, right-weighted figure anchors a quiet label and note. Rows use thin dividers on one neutral strip, directly recalling the original KPI table.',
'delta':'Two substantial figures share a neutral capsule, joined by an element-drawn directional arrow. The destination carries a deeper accent while the starting value stays quiet.',
'chart-bar':'Rounded-ended bars rise from a hairline baseline with reserved value and category tracks. Horizontal plots allocate an explicit wider label gutter and allow long category names to wrap.',
'chart-line':'Generic zero-size point anchors derive every segment from the current and previous values. Opposite diagonal rectangles draw rising and falling segments while separate category and value tracks remain outside the stroke.',
'chart-donut':'A broad circular ring surrounds a figure and short name. The selected share uses the ranked accent and the rest stays neutral, with circular geometry repeated consistently across individual and grouped rings.',
'gauge':'A quiet document row contains a capsule progress track, a left label and a right-aligned figure. The actual numeric value controls the filled length.',
'table':'A broad accent header and alternating quiet document rows organize tabular data. Numeric cells align right and selected columns use a soft accent ground; compact containers reduce type and cell padding in discrete steps.',
'legend':'Small circular swatches and compact labels form a restrained horizontal key. It wraps at narrow widths while retaining clear series ordering.',
'steps':'Equal circular marks lead a left-to-right sequence with small triangular connectors. Fixed content tracks keep every title aligned; the vertical form becomes dark or accent step tabs beside quiet explanations.',
'timeline':'Small accent dots mark a hairline track with dates held above and descriptions below. The column variant places dates in a dedicated left track, and an alternating variant changes the rhythm without changing type roles.',
'cycle':'Members travel around a thin circular path and a quiet central disc. Number or icon circles repeat the onboarding diagram language rather than adding decorative symbols.',
'hub':'Spokes follow a semicircular arc above a bottom core. Each spoke combines a colored capsule name, quiet explanation and circular icon or number mark, echoing the keyword diagram in the source deck.',
'funnel':'Centered bands narrow according to numeric shares. Quiet neutral and soft accent surfaces support one clearly selected leading stage, with figures separated from the stage names.',
'pyramid':'Progressively wider clipped bands build a tiered structure. The top tier carries the principal accent, while lower tiers recede into softly rounded document tones.',
'matrix':'Four rounded document panels share one consistent internal rhythm. Axis labels sit outside the panels; SWOT cells use a large single-letter kick above the name and nested list.',
'venn':'Two sets overlap in a horizontal composition; three sets form the triangular cluster seen in the company-values slide. Dark neutral circles and a single accent circle retain white page dividers.',
'hierarchy':'A central accent capsule connects to dark branch heads and small quiet leaf capsules. Thin perpendicular links remain separate from the text and preserve the document-like organization chart.',
'flowchart':'Quiet rounded process nodes occupy an explicit grid, with capsule endpoints and outlined questions. Small element-drawn connector arrows communicate direction without decorative icons.',
'architecture':'Full-width rounded layers align a bold left name with internal capsule chips. The leading layer is accented, while subsequent layers use quiet surfaces and a thin name divider.',
'versus':'Two neutral document panels face one another around a small circular comparison mark. The selected side uses a soft accent background and a colored capsule heading.',
'pricing':'Rounded plan panels combine a capsule heading, centered price and nested checklist. The selected plan is distinguished by a restrained accent outline and soft surface.',
'person':'Circular or rounded portrait seats sit above aligned names and concise roles. A row distributes people evenly and reserves generous quiet space around each portrait.',
'logo-group':'Near-square neutral logo seats form a wrapping row with generous spacing. Quiet rounded corners keep the logos in the same document system without inventing brand artwork.',
'image-frame':'A simple padded document frame holds a neutral numbered picture seat. The frame preserves a square-like placement and lets the supplied grid determine the surrounding composition.',
'agenda':'Two columns of quiet capsules carry automatic-looking circular number marks and a strong short name. Optional notes remain subordinate, and compact layouts step down before becoming a single column.',
'chart-stack':'Vertical or horizontal stacks use ordered accent and neutral bands with values centered inside them. A dedicated category track and an external legend protect the plot from long labels.',
'chart-waterfall':'Rounded floating bars show changes from an explicit previous total to the next total. Thin connectors follow the running total while total bars stand from zero.',
'chart-area':'Each interpolated area segment uses the previous point anchor and the current point value to construct a clipped quadrilateral down to the baseline. Cumulative series layer in reverse order for stacked areas, with reserved external series and category labels.',
'chart-scatter':'Small circular data marks sit on a quiet ruled field with labels above them. Bubble marks use restrained transparent fills; one selected point receives the principal accent.',
'sparkline':'A compact run of tiny rounded bars forms an inline trend strip. Meaningful upward or downward states use the semantic palette roles rather than a new brand color.',
'heatmap':'Rounded density cells form a labeled grid on the document surface. Numeric intensity controls a restrained accent wash and calendar mode turns the cells into compact square day seats.',
'waffle':'A counted grid of small rounded units expresses the share, followed by an explicit figure and short name. The figures variant uses a simple person silhouette clipped from the same units.',
'treemap':'Quiet rectangles divide branches by their numeric shares and stack child tiles within each branch. Compact tile containers use thinner shared-token padding and discrete smaller figures so small branches remain readable.',
'sankey':'A central source panel distributes into right-hand rounded branches through proportioned bands. The selected path uses the accent while drop-off paths stay quiet.',
'radar':'Filled generic polygons derive directly from each series numeric variables over three to eight axes. Circular guides, reserved perimeter labels and separate bottom series names retain the restrained diagram vocabulary.',
'bullet':'A quiet horizontal row combines a capsule actual bar, a thin target mark and an explicit figure. Labels have a dedicated leading column and target notes sit below the plot.',
'slope':'Before and after values share a restrained row with an element-drawn relation line. The dumbbell variant uses circular endpoint badges and one selected pair is accented.',
'roadmap':'Rounded duration capsules span a period grid alongside dedicated lane names. Accent milestone rules and quiet period labels provide an orderly schedule without arbitrary decoration.',
'swimlane':'Quiet ownership lanes contain a grid of rounded process nodes. Capsule endpoints, outlined questions and small directional connectors repeat the flowchart vocabulary inside the lane structure.',
'concentric':'Nested neutral discs communicate inclusion while an accent ring identifies the selected scale. Names and figures occupy the exposed top of each disc rather than overlap the next level.',
'journey':'Stage panels place clear titles and touchpoint notes below a numeric mood path. Small accent points and a restrained connecting line trace the experience, with pains separated on a high-contrast local surface.',
'mindmap':'Rounded branch panels radiate to either side of a central accent capsule. Quiet curved-edge relations and compact leaves keep the otherwise free structure orderly.',
'decision-tree':'Capsule questions branch into named conditions and rounded outcomes. The selected outcome alone uses an accent fill, with thin links and shared spacing preserving a clear reading direction.',
'balance':'Two quiet rounded pans sit on a thin beam whose tilt follows the supplied numeric value. A triangular fulcrum carries a concise verdict and the selected pan uses a soft accent surface.',
'matrix-nine':'Nine compact rounded panels occupy a labeled three-by-three field. One selected cell carries the accent while supporting cells use neutral or soft accent tones.',
'positioning':'A restrained cross-axis field holds rounded name or logo markers at explicit coordinates. The selected company is accented and competitors remain quiet.',
'network':'Circular nodes connect through generic trigonometric line geometry derived from endpoint coordinates. Strong links and one selected node use the accent while the rest remain neutral.',
'code':'A rounded document panel contains monospaced source loaded through an explicit Nanum Gothic Coding kit extension. A capsule file label, automatic line counters and high-contrast token colors support source review.'}
assert len(shapes)==56
for n,t in shapes.items():(C/'elements'/n/'description.md').write_text(t+' All typography, spacing and surfaces belong to the shared kit, and text contrast remains tied to palette roles in both display modes.\n')
(P/'design-language.md').write_text('''# Onboard Docket — 078 덱 디자인 언어

## 원본에서 확인한 문법

19장 모두 1280×720이다. 원본을 한 장씩 전체 크기로 확인하고 replica를 먼저 작성했다. 배경 위에 종이 한 장이 떠 있고, 분리된 바인더 띠가 상단을 가로지른다. 큰 장 번호와 세로 구획선, 굵은 제목, 머리글 아래 가는 가로선이 반복된다. 본문은 회색 캡슐 목록, 둥근 문서 패널, 원형 아이콘, 단순한 계층 연결로 정보를 나눈다.

| 항목 | 반복 규칙 | 라이브러리 반영 |
|---|---|---|
| 선 | 구획·연결은 약 1px, 핵심 도형은 2px | `--stroke`, 필요시 2px 도형 선 |
| 모서리 | 종이 약 14px, 내부 패널 약 10px, 목록은 완전한 캡슐 | `--radius`, `--radius-sm`, 999px |
| 여백 | 8 / 16 / 24 / 32 / 48px, 큰 표지는 96px | 공유 gap/pad 토큰의 배수 |
| 페이지 | 바깥 여백 가로 46px, 위·아래 38px, 띠 높이 49px | foundation의 고정 1280×720 캔버스 |
| 머리글 | 장 번호 약 56–58px, 제목 약 48px, 보조 브랜드 14–16px | 정수 type 단계, 제목 650 굵기 |
| 본문 | 일반 16–20px, 소제목 20–24px, 지표 48–52px | 칸 크기에 따라 단계적으로 축소 |
| 강조 | 하나의 채움, 어두운 중립 면, 큰 수치, 반전 문구 | 전체 면과 글자 강조를 구분 |
| 장식 | 바인더 띠, 얇은 구획선, 원형 연결, 작은 삼각 화살표 | 본문 정보와 관계를 설명할 때만 사용 |

## 색은 자리가 갖는다

- 바탕 종이 = `--page`, 글자 = `--ink`, 책상 바탕 = `--n-3`.
- 바인더 띠·선택 캡슐·선택 원 = `--a1`, 그 위 글자 = `--a1-on`.
- 바탕 위 작은 강조 글자와 장 번호 = `--a1-7`. 원본의 밝은 강조색을 임의 사용자 팔레트에 그대로 적용하면 대비가 부족하므로 글자에는 깊은 강조 단계를 쓴다.
- 일반 카드·목록 = `--n-2`, 옅은 보조 면 = `--n-1`, 관계선 = `--n-4`.
- 어두운 단락·단계 캡슐 = `--n-8` 또는 `--n-9`, 글자 = `--page`.
- 옅은 강조 카드 = `--a1-2-soft`. 복수 시리즈는 `--a1`부터 순위대로 배정한다.
- source-palette.css는 원본 색을 비교하기 위한 외부 style 입력이며 레이아웃을 바꾸지 않는다. 컬렉션 CSS에는 원본 색값이 없다.

## 폰트와 표현의 결정

원본에 사용된 정확한 글꼴 파일명은 이미지에서 확인할 수 없다. 제공 폰트 표의 Noto Sans KR을 실제 로드했으며 서명은 Nanum Pen을 근접 대체로 사용했다. 코드 블록은 Nanum Gothic Coding을 키트 확장 토큰으로 실제 지정한다. 사진·로고 이미지·복잡한 인물 표현은 회색 자리로 대체했고, 구현 가능한 아이콘과 차트·원·표·연결은 구조와 데이터로 그렸다.

원본에 없는 56개 계약 요소도 캡슐, 둥근 종이 면, 큰 숫자, 가는 연결선과 원형 표식이라는 같은 문법으로 확장했다. 조립본에는 새 페이지 레이아웃 CSS를 넣지 않고 foundation과 요소의 계약 마크업을 12×6 그리드에 배치했다. runtime.css는 브라우저 기본 body 여백을 제거하는 중립 출력 프레임일 뿐이다.
''')
(P/'review-notes.md').write_text('''# Onboard Docket 검수 기록

## 범위와 순서

078 덱의 slide_01–19, 19장 전부를 읽고 replica HTML을 먼저 작성했다. 이후 디자인 언어를 문서화하고 foundation과 56개 요소를 제작했으며, 마지막에 계약 마크업만으로 19장을 다시 조립했다. 다른 샘플의 디자인 CSS는 읽거나 가져오지 않았다. fixture는 지정 모범 구성의 마크업·데이터와 비지정 계약 구조 예시를 사용했고 data-el만 이 컬렉션으로 바꿨다.

## 실제 비교와 수정

- 원본 19장 각각을 전체 크기로 확인했다. 실제 Chromium 브라우저에서 replica를 렌더하고 19개의 원본 | replica 쌍을 한 장씩 보았다. 연락처 시트만으로 검수를 끝내지 않았다.
- 비교 뒤 표지 라틴 제목의 폭, CHAPTER 제목의 세로 위치, 인재상 도넛 시작 각도, 세로 단계 탭의 직각 모서리, 키워드 반원 도형의 종이 끝 잘림을 수정했다.
- 폰트 요청이 실패한 404 초기 환경 렌더는 검수 결과에서 제외했다. HTTP 200 응답과 실제 font load를 확인하는 경로로 고쳤다.
- 라이트·다크 시트에서 제목 정렬, 작은 칸의 글자와 긴 가로 차트 라벨, 단위 색, 강조 면의 대비를 검토했다. 카드 제목은 내용 길이에 관계없이 같은 트랙에서 시작하도록 고쳤다.
- 선 차트는 앞 점과 현재 점을 잇는 실제 CSS anchor 선으로, 영역 차트는 현재 값과 앞 점 위치로 계산한 보간 다각형으로 수정했다. 특정 fixture 값에 맞춘 하드코딩은 사용하지 않았다. 공유한 것은 이 좌표 계산 방법뿐이며 디자인 CSS는 독립적이다.
- 조립본 19개 비교 쌍을 각 장별로 보았다. 표지 제목 위치, 한 줄 pill 높이, 작은 카드 note 보존, 단계 제목 정렬, 원본의 반원형 hub 문법을 요소 CSS에 반영했다. 브라우저 기본 body 8px 여백도 중립 출력 프레임에서 제거했다.

## 원본과 남는 차이·해석

| 장 | replica에서 남는 차이 | 조립본의 계약에 따른 결정 |
|---|---|---|
| 01 | 원본 로고는 회색 자리, 라틴 제목은 근접 폰트 폭을 보정 | 표지 띠와 lockup을 foundation으로 표현, 우측 아이콘 레일은 단순화 |
| 02 | 로고 자리, 미세한 자간 차이 | agenda의 자동 트랙과 글자 단계로 목차를 배치 |
| 03 | 정확한 원본 폰트는 미확인 | headline의 제목·note 위계로 재구성해 원본의 구획선 간격과 다름 |
| 04 | 인물 사진은 회색 자리, 서명은 근접 서체 | quote의 인용 규칙과 author 슬롯 때문에 대표이사 표기가 본문 위쪽으로 이동 |
| 05 | 건물 사진은 회색 자리 | 7/5 그리드 열 분할로 원본과 문단 줄바꿈이 달라짐 |
| 06 | 세 조각 경계·폰트 세부는 근사 | 단일 share 계약의 donut으로 핵심 비중을 보여주어 원본의 세 이름 중심 도해와 다름. 33은 세 균등 부문의 약 1/3로 해석한 값이며 원본에 인쇄된 수치가 아님 |
| 07 | 이름·설명은 판독된 원문 | list.num의 자동 원형 번호가 원본 캡슐 안 번호와 분리됨 |
| 08 | 아이콘은 직접 구현한 간단 선 아이콘 | 세 set의 삼각 배치를 지원하도록 venn CSS를 수정, 오른쪽 설명은 list 트랙 사용 |
| 09 | 계층 연결선의 미세한 곡률 차이 | hierarchy 계약은 branch 2–4개라서 원본 5부서는 pill/list 5열로 구성. 부서 수는 보존했으나 전역 계층 연결선은 생략 |
| 10 | 근접 폰트에 따른 본문 폭 차이 | steps.col로 원본 3단 흐름을 재현, 긴 note는 그리드 폭에 맞춰 재줄바꿈 |
| 11 | 작은 그림은 Lucide에 가까운 단순 선 도형 | headline과 3열 card를 사용, 원본보다 상위 문장 위계가 큼 |
| 12 | 작은 사진은 회색 자리 | headline/prose/image-frame만 사용해 원본의 두 구획과 문장 흐름을 유지, 일부 긴 안내문은 의미를 보존해 축약 |
| 13 | 심장·전구 아이콘의 선 세부는 근사 | hub를 반원형 원본 문법으로 수정. 계약의 core와 spoke 안에서 이름·note·표식을 정리 |
| 14 | 겹치는 원의 투명도 세부는 근사 | steps와 card로 네 단계를 조립해 원의 겹침과 내부 키워드 위치가 원본과 다름 |
| 15 | 아이콘 세부는 제공 가능한 Lucide형으로 대체 | 같은 steps 계약에 원본의 네 아이콘을 지정, 고정 제목 트랙으로 줄 정렬 |
| 16 | Noto의 행간·점 크기 차이 | pill과 divided list로 세 일차를 조립, 원본의 탭 그림자와 바깥 테두리는 단순화 |
| 17 | KPI 글자 폭·굵기 세부 차이 | card와 stats를 사용해 3×3 핵심 수치를 보존, 단위와 설명 정렬은 요소 규칙 사용 |
| 18 | 사진은 회색 자리 | image-frame과 list로 원본의 사진/설명 비율을 근접 재구성 |
| 19 | 사진 3개는 회색 자리 | 원본의 세 사진과 세 설명을 그리드 요소로 유지, 좌측 세로 라벨은 card로 표현 |

## 판독 불가·추정과 계약 충돌

본문은 대체로 판독 가능했다. 로고의 원본 벡터 형태와 사진 내부의 아주 작은 화면 문구는 전사하지 않고 자리로 처리했다. 서명 김미리는 읽을 수 있지만 정확한 원본 서명 글꼴은 미확인이다. 원본의 긴 안내문 중 계약 칸에 들어가기 어려운 일부는 조립본에서 의미를 유지해 짧게 정리했으며 replica에는 읽은 원문을 유지했다.

지정 모범 fixture card-4에는 원본 샘플부터 `✹` 아이콘 문자가 들어 있다. "같은 마크업과 데이터"라는 사용자 지정 요구를 지키기 위해 이 한 곳은 그대로 보존했다. 새 fixture나 조립본에 새 문자 아이콘을 만들지는 않았다.

## 자동 검수의 해석

렌더 크기·font load·요청 실패·문자 범위·부모 잘림·칩 중심·대비는 루트 통합 검수의 JSON 결과와 최종 렌더 지문을 함께 제출한다. 문자 잉크의 자연스러운 line-box 초과와 실제 조상 overflow 잘림을 구분했다. 마지막 소스 변경 뒤 최종 렌더가 다시 수행되어야 하며, 최종 PNG/PDF 생성과 ZIP 무결성·다운로드 검증은 주 에이전트의 통합 단계에서 확인한다. 이 문서는 통과하지 않은 항목을 자동 통과로 주장하지 않는다.
''')
print('docs',len(shapes))
