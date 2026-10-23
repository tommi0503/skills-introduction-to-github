from pathlib import Path
import json,re
C=Path('/workspace/output/cyanloop');R=Path('/workspace/output/cyanloop-review')
desc={
'card':'A compact rounded panel pairs a circular icon or numeral with a stable title and note stack. Emphasis fills one panel while line and quiet variants preserve the same internal alignment.',
'pill':'A single capsule centres its mark, Korean label and short supporting note on their visual centre. Smaller allocations remove secondary text before disturbing the primary name.',
'callout':'A long deep capsule places a concluding sentence and its bold phrase on one centred reading line, with an optional proportionate icon.',
'tag':'Small capsule labels sit in running copy; inline highlights use a soft accent surface without changing the paragraph rhythm.',
'list':'A vertical list places tiny round markers, drawn check strokes or numbered circular endpoints beside a disciplined Korean text column. Divided lists add quiet hairline rules.',
'quote':'An inset quotation uses a broad display sentence, a slim accent edge and a compact attribution group with a circular avatar.',
'headline':'A strong display heading floats inside the content grid with a short kicker and optional subtitle. Its statement, centred and accent-ground variants retain the deck’s forceful hierarchy.',
'prose':'Readable Korean paragraphs keep a calm line length and generous paragraph rhythm, with lead, secondary and two-column treatments.',
'metric':'A large condensed figure stands free of a card surface above a precise Korean metric name. Multiple metrics use hairline dividers and matching vertical positions.',
'delta':'Two display figures sit on a shared baseline; a small drawn directional chevron bridges the quiet previous value and the darker emphasized result.',
'chart-bar':'Rounded capsule tops grow from a shared baseline, with one darker bar and value labels kept above the marks. Horizontal bars reuse the capsule track and reserve a separate name gutter.',
'chart-line':'Discrete circular endpoints sit on one continuous thin polygon stroke calculated from the fixture values. Labels remain above the points and horizontal step names occupy a separate baseline.',
'chart-donut':'An unbroken circular track carries the measured share, while a neutral centre holds the display percentage and a concise Korean name. Repeated rings keep equal size.',
'gauge':'A slim capsule track follows the label and figure row, emphasizing completion without turning the whole cell into a heavy panel.',
'table':'A deep header band anchors a clear business table, with quiet fine rules and soft selected columns. Numeric cells align to the right while Korean names retain a stable column rhythm.',
'legend':'Small ranked-colour discs precede concise series names in one centred row, wrapping only as a complete label group.',
'steps':'Numbered circular endpoints lead a row of compact stage panels, joined by fine connectors. The column variant uses the same endpoint and a dedicated text gutter.',
'timeline':'A fine chronological track connects circular date points and concise event blocks, with one softly emphasized stop. The column variant trades width for a compact vertical rhythm.',
'cycle':'Circular members orbit a deep central disc on an open visual track, with directional arrowheads distinguishing recurrence from a simple hub.',
'hub':'Capsule spokes surround a central idea, using short fine links and a consistent title-note hierarchy rather than decorative imagery.',
'funnel':'Progressively shorter capsules represent diminishing stages, keeping the name and figure readable at opposite ends of each level.',
'pyramid':'Successively wider capsule levels form an educational hierarchy, placing the shortest executive level above broad foundational capability levels.',
'matrix':'A quiet two-by-two field reserves separate axis gutters and one accent quadrant. The SWOT variant replaces axes with strong letter kickers and properly nested business lists.',
'venn':'Thin outlined circular sets overlap with soft palette surfaces, with a deep shared label where the intersection carries the conclusion.',
'hierarchy':'A centred deep root capsule connects to equal branch capsules and pale leaf strips. The complete tree is vertically balanced within its allocation.',
'flowchart':'Rounded process nodes and deep terminal capsules occupy explicit grid cells, with hairline directional connections and a circular decision node.',
'architecture':'A stack of long capsule layers separates a strong layer name from small outlined capability chips, using one deep primary layer.',
'versus':'Two rounded comparison panels face a small central disc marked VS; one soft accent side receives the recommendation while nested lists stay readable.',
'pricing':'Equal plan panels align the name, price and benefits, with one accent-topped recommendation and a concise capsule tag.',
'person':'Circular or portrait seats lead a centred profile name and role; optional career lists occupy a measured lower block without stretching the photograph.',
'logo-group':'Equal circular logo seats form a balanced single row or a uniform two-row grid, avoiding an oversized final member.',
'image-frame':'A thin accent ring contains a square neutral image seat; the circle remains a circle even when the allocated grid cell is wide.',
'agenda':'Strong display numerals introduce equal-width agenda entries with compact Korean names and notes, finished by a quiet lower rule.',
'chart-stack':'Ranked filled segments share one bar and retain their own readable value labels; horizontal and percentage arrangements preserve the same restrained rules.',
'chart-waterfall':'Small floating rounded bars distinguish increases, decreases and totals, with a fine connector showing the running balance between steps.',
'chart-area':'Value-driven continuous filled polygons occupy a ruled plot, with each series named in a separate upper legend row and x labels below the plot.',
'chart-scatter':'Small circular marks sit on quiet two-value axes, while bubble marks use thin outlines and soft fills so their labels remain distinct.',
'sparkline':'A small capsule-ended microtrend sits beside a larger figure, using semantic upward or downward colour only when the variant carries that meaning.',
'heatmap':'Rounded density cells form aligned business rows; visible values receive tiny page-colour capsules to preserve contrast in both themes. Calendar cells keep square geometry.',
'waffle':'A counted unit grid precedes a display share and Korean explanation; the figures variant uses drawn human silhouettes and a compact adjacent caption.',
'treemap':'Nested rounded rectangles translate group and tile shares into proportional widths, using a single accent tile and short internal figures.',
'sankey':'A deep source capsule feeds measured rounded bands and quieter destination capsules, including a second split when the fixture contains nested branches.',
'radar':'Three to eight labelled spokes surround a circular ruled field; each series is a real value-driven polygon, with its name in an unclipped upper legend position.',
'bullet':'A short capsule bar compares the actual value against a thin target mark, with a separate label and figure row and a readable goal note.',
'slope':'Named before-and-after pairs use restrained linking strokes and one stronger series. The dumbbell variant places both observations on a shared horizontal track.',
'roadmap':'A deep period header sits above quiet lane tracks and capsule duration bars, with milestone points kept separate from task labels.',
'swimlane':'Light owner lanes support explicit process nodes, maintaining separate owner labels, rounded terminals and fine directional links.',
'concentric':'Nested inclusion fields descend toward a common lower centre, using alternating soft ranked surfaces and a deep innermost outcome.',
'journey':'Equal stage panels carry a circular emotion trace above concise touchpoint text; pain labels remain secondary and one stage receives a soft emphasis.',
'mindmap':'A central disc balances free branches on both sides; small capsule leaves and fine branch rules preserve an exploratory rather than strictly hierarchical reading.',
'decision-tree':'Deep question capsules split into labelled alternatives and quiet outcome panels, with the recommended end receiving the accent fill.',
'balance':'Two measured panels hang against a tilted fine beam, with one softly emphasized pan and a separate centred verdict below.',
'matrix-nine':'Nine compact rounded boxes align behind independent three-step axis labels, using one primary accent rather than a competing rainbow of fills.',
'positioning':'Circular named marks sit on two crossing fine axes, with our position emphasized by one filled accent disc.',
'network':'Circular relationship nodes connect through thin geometry calculated from both coordinate axes, with a stronger accent link only for the principal relationships.',
'code':'A restrained inset source panel uses the actual Nanum Gothic Coding monospace face, optional line numbering and readable ranked syntax colours.'}
for n,t in desc.items():(C/'elements'/n/'description.md').write_text(t+' The component inherits the collection’s capsule, circle and hairline vocabulary, and uses explicit container steps for readable smaller allocations.\n')
notes='''# cyanloop 검수 기록

## 범위와 빌드

- 덱 003의 실제 PNG 18장, 모두 1280×720. 원본 18장을 개별 확대 확인하고 페이지별 원본|replica 및 원본|조립본 비교를 수행했습니다.
- 컬렉션: kit, foundation, 56개 요소, 요소 fixture 170개와 foundation fixture 2개. 모범 구성 28개 fixture의 마크업·데이터를 보존했습니다(data-el의 컬렉션 이름만 변경).
- replica는 독립 HTML/CSS/SVG이며 원본 비트맵을 배경으로 사용하지 않습니다. 사진과 인물은 의도적으로 회색 번호 seat입니다.
- 조립본은 컬렉션의 foundation/요소 CSS와 계약 마크업, 12×6 grid 배치만 사용합니다. `runtime-original.css`는 이 CSS를 그대로 합친 뒤 원본 팔레트 역할 값을 공급한 파일입니다. 별도의 페이지별 레이아웃 CSS는 없습니다.
- 요소 시트는 계약 preview.py로 라이트·다크를 생성한 뒤 실제 Chromium으로 렌더했습니다. 각 요소 폴더의 light.png / dark.png는 해당 요소의 모든 fixture를 포함합니다. 전체 PDF는 각 fixture를 1280×720 화면으로 따로 담습니다.

## 비교·수정

1. 원본 18장을 각각 읽고 1차 replica 생성. 배치, 숫자, 표, 도형과 사진 자리를 분리했습니다.
2. 나란히 비교하여 제목 크기, 본문 행간, 06 페이지의 흰 영문 라벨과 왼쪽 반원, 09 허브 글자 대비, 사진 frame과 13 중심 문장의 색을 수정했습니다.
3. 표지·목차·간지·마지막 페이지의 열린 루프를 원본 좌표에 가까운 별도 SVG 궤적으로 다시 그렸습니다. 최종 원본 비교와 PNG 재렌더를 완료했습니다.

라이브러리 검수에서는 작은 높이에서의 목록·목표·표·프로필 overflow를 줄였고, 카드 제목/노트에 일정한 행 자리를 확보했습니다. 선/면 차트의 소수 값 dispatch, 3~8축 radar, cycle 궤도와 방향, network의 가로세로 비율에 따른 연결 길이를 고쳤습니다. 영역 차트 위에 잘못 남던 막대형 면도 제거했습니다. `--a1`의 작은 글자색은 깊은 단계로 옮겼고, heatmap 숫자는 작은 page색 캡슐에 놓아 두 모드에서 대비를 확보했습니다. 중첩 list/tag의 data-el과 item/name 계약도 정규화했습니다.

## 폰트와 해석 결정

- 원본에 폰트 메타데이터가 없어 동일한 폰트라고 확정할 수 없습니다. replica는 시각적으로 가장 가까운 **Anton**을 실제 로드했고, 한국어는 제공된 **Pretendard Variable**을 사용했습니다.
- 라이브러리는 허용된 family만 사용해야 하므로 display를 **Do Hyeon**, 본문을 **Pretendard Variable**로 옮겼습니다. 따라서 특히 영문 제목의 폭·인상은 replica와 다릅니다. code는 kit extension으로 제공한 **Nanum Gothic Coding**을 실제 로드합니다.
- 원본의 단순 선 아이콘은 replica에서 직접 SVG로 그렸습니다. 조립본은 실제 Lucide를 로컬 파일로 로드하여 빈 data-icon 칸을 채웁니다. 기본 계약 시트의 아이콘은 preview.py 규칙대로 점선 seat로 보입니다.
- canonical fixture에 들어 있는 `✹` 글자와 callout의 원래 grid 위치는 '같은 마크업·데이터' 의무를 우선하여 그대로 보존했습니다. 비모범 fixture의 최상위 배치는 12×6으로 정규화했고, 중첩 요소는 각자의 data-el을 갖습니다.
- 샘플 컬렉션의 CSS는 가져오지 않았습니다. fixture는 계약 구조와 다양성을 보여주는 마크업 형식으로 사용했으며, 모든 외형 CSS는 새로 작성했습니다. expanded versus/tag/legend/pricing은 실제로 다른 문구·멤버 수를 갖습니다.
- 사진을 놓는 seat는 circle/portrait의 실제 종횡비를 유지합니다. 원본의 큰 사진 위 텍스트와 겹치는 부분은 임의 사진 복원이 아닌 회색 자리로 표현했습니다.

## 원본과 남는 차이

| 페이지 | replica 및 조립본 차이 |
|---|---|
| 01 | replica의 표지 궤적은 직접 그린 SVG여서 그라데이션 분포가 조금 다릅니다. 조립본은 공통 cover lockup과 열린 원 장식으로 단순화됩니다. |
| 02 | replica는 상단 절반 띠와 4개 목록을 재현합니다. 조립본은 일반 foundation 제목과 agenda 4개로 재배치합니다. |
| 03 | replica는 간지의 세 궤적과 하단 목차를 재현합니다. 조립본은 headline + agenda로 표현하여 원본의 자유 배치와 차이가 납니다. |
| 04 | 사진은 회색 seat. 복합 막대/선 차트는 replica에서 중첩 플롯으로 재현했으며, 조립본은 각각의 계약 요소로 두 시리즈를 나누어 표시합니다. |
| 05 | 사진 카드의 사진은 회색 자리. 조립본의 강조 카드와 아이콘 크기는 라이브러리 공통 규칙을 따릅니다. |
| 06 | 건물 사진은 회색 circle. replica는 왼쪽 반원 선과 세 가지 원형 키워드를 유지했고, 조립본은 공통 pill/card/frame으로 해석합니다. |
| 07 | 단순 아이콘은 같은 의미의 선 아이콘으로 대체. 조립본은 동일한 네 가지 내용과 하단 결론을 보존하지만 카드 내부 비율은 공통 규칙을 따릅니다. |
| 08 | replica는 원본 계층별 캡슐의 폭과 위치를 재현합니다. 조립본은 pyramid 계약의 단계별 폭을 사용하며 색의 강조 순위를 단순화합니다. |
| 09 | replica는 좌우 캡슐과 중심 원을 재현. 조립본은 공통 hub 배치로 멤버 순서와 중심 비율이 달라집니다. |
| 10 | 사진은 회색 circle. 조립본은 네 개의 picture frame과 timeline으로 분리하여 원본의 겹친 원형 타임라인과 차이가 납니다. |
| 11 | replica는 유기적인 다섯 단계 모양을 직접 SVG로 구현했습니다. 조립본은 공통 cycle을 사용해 균등한 궤도형 단계로 정리합니다. |
| 12 | 온보딩 사진은 회색 circle. 조립본은 공통 image frame과 네 개의 pill로 표현합니다. |
| 13 | replica는 원형 역량 위성과 잘린 하단 중심 원을 재현. 조립본은 잘리지 않는 공통 hub 구성으로 정리합니다. |
| 14 | 표의 내용과 행 수는 유지. 조립본은 계약 table의 동일 폭 열과 공통 header 규칙을 사용합니다. |
| 15 | 인물 사진 3개는 회색 portrait. 조립본은 사진과 프로필/이력 목록을 동일 폭으로 분리합니다. |
| 16 | 원본의 수치와 키워드 placeholder를 유지. 조립본은 metric + 6 card로 구성하며 고정한 제목 자리로 정렬을 맞춥니다. |
| 17 | 원본 주차와 기간은 보존. 조립본의 기간 막대는 직각 사각형 대신 collection의 capsule 문법을 사용합니다. |
| 18 | replica는 연락처와 큰 감사 문구, SVG 궤적을 재현. 조립본은 공통 cover 잠금구성과 간결한 연락처 줄로 변환합니다. |

## 판독 불가 및 문구 처리

주요 제목, 숫자, 표, 단계 이름은 개별 원본에서 읽어 입력했습니다. 작은 부연 문구는 띄어쓰기와 문장부호가 원본과 다를 수 있습니다. 원본 자체의 `Tranning`, `00%`, '키워드를 입력해주세요' 같은 문구는 자료의 placeholder로 판단하여 replica에 보존했습니다. 조립본에서는 일부 긴 설명을 해당 요소의 note에 맞게 축약했습니다. 이 축약과 공통 서체/그리드 전환 때문에 조립본은 픽셀 동일 재현본이 아니며 원본 그대로의 시각 검토에는 replica를 사용해야 합니다.

## 자동 검사 결과

최종 정적 계약 검사와 브라우저 검사의 자세한 수치는 `verification.json`, `library/browser-checks.json`, `library/grid-audit.json`을 확인하십시오. 글자 범위 검사는 DOM text range와 할당한 grid 영역을 비교하며, 글꼴·페이지 크기·PNG 크기·ZIP CRC도 확인합니다. 이 검사는 실제 Rhetis intake 실행을 대체하지 않습니다.
'''
(R/'review-notes.md').write_text(notes)
(R/'fonts/sources.md').write_text('Fonts in artifacts/ were supplied in the user-provided Rhetis reference archive. Anton.ttf was retrieved from Google Fonts (Anton v27, fonts.gstatic.com), under the SIL Open Font License, for the independent replica only. The collection package itself contains no font binaries.\n')
(R/'index.html').write_text('''<!doctype html><html lang="ko"><meta charset="utf-8"><title>cyanloop 검수 미리보기</title><style>body{font:18px sans-serif;max-width:960px;margin:50px auto;line-height:1.7}a{color:#0053d6}img{width:100%;border:1px solid #ddd}</style><h1>cyanloop · 교육 자료 18장</h1><p><a href="library/light.html">라이트 요소 시트</a> · <a href="library/dark.html">다크 요소 시트</a> · <a href="replica/replica.pdf">replica PDF</a> · <a href="reassembled/reassembled.pdf">조립본 PDF</a> · <a href="review-notes.md">검수 기록</a> · <a href="design-language.md">디자인 언어</a></p><h2>원본 | replica</h2><img src="compare-replica/slide_01.png"><h2>원본 | 조립본</h2><img src="compare-reassembled/slide_01.png"></html>''')
print('review docs written')
