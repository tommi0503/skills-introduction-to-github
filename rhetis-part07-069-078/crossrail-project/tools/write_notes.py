from pathlib import Path
P=Path(__file__).parent
D={
'card':'A rectangular panel starts with a restrained deep accent rule. Equal title and note tracks keep the names of adjacent cards aligned; short figure cards place the number and its label on one ruled header row.',
'pill':'A fine outline capsule keeps its mark, label and secondary value on a common optical centre. Emphasis changes the capsule to an accent field rather than adding decorative material.',
'callout':'A single centred sentence sits between structural rules on a quiet field. The decisive words deepen into the ranked accent, with an optional modest icon at the left.',
'headline':'A left aligned statement uses a small quiet kicker, strong sans heading and a subordinate note. A larger statement, centred placement and accent-ground state remain part of the same hierarchy.',
'prose':'Plain paragraphs carry the voice, with generous paragraph gaps and restrained bold emphasis. Two-column reading and quieter secondary copy preserve the deck’s calm editorial rhythm.',
'quote':'A large voice is bracketed by fine horizontal rules. The attribution pairs a restrained circular portrait seat with a name and role on a clean two-line baseline.',
'metric':'An unboxed figure dominates a stable name-and-note stack. A ruled name baseline and optional separators in a row of figures echo the source’s summary pages.',
'delta':'A quiet previous figure and a deep-accent resulting figure face each other across a deliberately drawn directional arrow.',
'list':'Ruled or open entries use a modest marker column and strong name before the supporting sentence. Numbered and check states draw their markers without adding text to the data.',
'chart-bar':'Rectangular columns stand on a finely ruled plot with values clearly above the bars and labels below. The singled-out result deepens into the main accent; horizontal bars keep the same label hierarchy.',
'chart-line':'A precise thin line connects actual child point values through CSS anchors. Small circular vertices, above-point values and separated axis labels keep the trend legible at narrow sizes.',
'chart-area':'CSS anchor polygons connect actual adjacent point values to a continuous quiet fill. The same geometry supports multiple and cumulative stacked series while keeping series names above the plot.',
'chart-donut':'A restrained circular share surrounds a large figure and short centred name. The highlighted arc is deep while the remainder is neutral; a row of donuts preserves equal figure baselines.',
'chart-scatter':'Quiet circular observations occupy explicit value coordinates in a simply ruled two-axis field. A deep result and optionally scaled bubbles establish importance without changing label placement.',
'chart-stack':'Crisp rectangular segments stack without rounded corners, reserving ranked accents for meaningful series. Outside category labels and centred segment figures keep the chart analytical.',
'chart-waterfall':'Floating rectangular steps preserve the running total and connect with fine dashed rules. A final total uses a deep solid column, while reductions remain neutral.',
'gauge':'A fine, straight progress track sits beneath a name and numeric result. The deep filled segment communicates progress without a bulky gauge housing.',
'legend':'Small square swatches and short ranked-series names sit on a calm shared baseline, wrapping only as complete keys.',
'steps':'Horizontal steps join through angular chevron heads before ruled name and note blocks. The vertical form becomes a sequence of fine outline capsules with restrained circular marks.',
'timeline':'Moments attach to a fine rule through small circular nodes. Deep date strips and alternating label blocks translate the source’s quarter-by-quarter roadmap.',
'cycle':'Outline capsules arrange around a calm central disc and a thin circular connector. The source’s equal-weight relationship language remains legible for three to six members.',
'hub':'A central label is surrounded by evenly positioned capsule members and modest icon circles. Fine structural connectors avoid heavy spokes competing with the content.',
'funnel':'Three to six flat trapezoid fields narrow through the actual provided stage shares. The final stage becomes deep, carrying a clear name and numeric figure.',
'pyramid':'Four flat, separated hierarchy levels widen from a triangular deep apex into neutral foundation bands. Short names remain centred within their own level.',
'matrix':'Four restrained ruled panels establish a two-by-two decision field. A single chosen cell receives a quiet accent field; the SWOT form replaces axes with clear initial labels.',
'venn':'Thin circular outlines overlap gently around an optional central decision. Neutral transparent fields preserve the relation without introducing decorative gradients.',
'hierarchy':'A deep rectangular root links through thin stems to clear branch headers and ruled leaves. Symmetry and stable label tracks carry the company-structure language.',
'flowchart':'Rectangular process nodes occupy a strict grid and connect through directional line-and-arrow geometry. Start and end nodes use outline capsules; questions receive quiet emphasis.',
'architecture':'Straight horizontal layers use a deep leading rail, strong layer name and finely outlined capsules for their internal services.',
'versus':'Two calm panels face across a small comparison mark. Deep top rails and ruled headings link the comparison to the source partnership page.',
'pricing':'Equal rectangular plan columns receive a deep top rail, a clear price baseline and an open check list. The selected plan uses a quiet accent field rather than a badge explosion.',
'person':'A circular or portrait image seat sits above a strong ruled name and quiet role. Equal-width profiles preserve the source equipment and team alignment.',
'logo-group':'Square logo seats form a generously spaced row or wrap inside fine horizontal rules. The frame supports identity without inventing logo artwork.',
'image-frame':'A fine rectangular picture seat receives only a small structural accent at its upper edge. The image itself remains a numbered neutral seat.',
'agenda':'Each contents label ends on a shared fine rule, with a deep two-digit index aligned at the opposite side. The selected entry receives only a quiet field.',
'sparkline':'A compact unlabelled trend uses crisp vertical units adjacent to a main figure. Up and down states express meaning through status roles.',
'heatmap':'Aligned density cells and clear row names form a compact analytical matrix. Calendar cells become square and omit the row-name column.',
'waffle':'Ten-column square units count a share beside a large figure and short name. The optional figure state cuts the unit into a restrained person silhouette.',
'treemap':'Nested crisp rectangles follow the supplied branch and tile shares. Short centred names and figures remain subordinate to the area relationships.',
'sankey':'A single deep source distributes into quiet rectangular branches through proportioned bands. The principal path receives a stronger leading rail.',
'radar':'Three through eight explicit axes surround a restrained radial field. Each series is an actual-value polygon using the ranked series accents at quiet fill strength.',
'bullet':'A deep actual-value strip crosses quiet qualitative bands and a precise target tick. Name, result and target note remain aligned above the track.',
'slope':'Before and after values occupy a paired comparison field with distinct endpoint discs. The dumbbell form reuses the same figures on horizontal paired tracks.',
'roadmap':'Quarter labels and a stable owner-name column lead into crisp duration bars on thin horizontal rules. Deep bars mark priority and slim dashed lines mark milestones.',
'swimlane':'Owners form quiet horizontal lanes under a shared process grid. Rectangular and capsule nodes use the same thin directional connectors as the flowchart.',
'concentric':'Nested circular fields place the broadest opportunity outside the contained opportunities. Each ring’s name and figure occupy a reserved upper band.',
'journey':'A row of rectangular touchpoints supports a thin mood curve and small vertices above. Notes and restrained pain statements preserve clear stage ownership.',
'mindmap':'A deep central circle distributes into calm left and right branch blocks. Fine linking rules and subordinate leaf dividers keep the map structured.',
'decision-tree':'A deep question block splits through fine rules into named answer branches and rectangular outcomes. The recommended result receives a quiet accent field.',
'balance':'Two rectangular pans share a fine beam whose tilt follows the supplied value. The verdict sits in a restrained triangular fulcrum below the comparison.',
'matrix-nine':'Nine equal ruled decision boxes surround two restrained three-label axes. A single deep cell establishes the chosen option without breaking the grid.',
'positioning':'Small labelled discs occupy explicit coordinates on a crossed two-axis field. The chosen position becomes deep while competitors stay quiet.',
'network':'Circular labelled nodes attach to fine links determined by explicit endpoint coordinates. The important node and strong relation deepen into the primary accent.',
'code':'A crisp neutral source panel has a deep top rail, ruled filename and preserved line breaks. Numbered lines and quiet syntax roles remain subordinate to reading.',
'table':'A precise table uses quiet header fields, fine full rules and deep emphasis on the selected column. Numeric columns align to a common right edge, with container steps reducing padding before text.',
 'tag':'Small labels use a restrained deep capsule; an inline highlight uses a quiet accent field that follows the running text rather than making a separate sticker.'}
assert len(D)==56
for e,d in D.items():(P/'crossrail/elements'/e/'description.md').write_text(d+' All typography, spacing and colors are supplied through the shared kit and ranked palette roles.\n')
(P/'design-language.md').write_text('''# Crossrail 디자인 언어 — 덱 073

## 출발점
원본 30장을 모두 확대 확인하고 각 페이지를 독립 HTML로 먼저 재현했다. 이 덱의 특징은 색 자체가 아니라 **구조를 드러내는 레일과 교차선, 넓은 직사각형 면, 큰 왼쪽 제목과 작은 영문 보조선**이다. 샘플 컬렉션 CSS는 사용하지 않았다.

## 형태와 선
- 기본 모서리 반경은 0. 사각 정보 패널은 각을 유지한다. 인물·관계·비중은 원형, 짧은 라벨·프로세스는 999px 캡슐을 쓴다.
- 페이지 상단 레일 35px, 오른쪽 기준선은 가장자리에서 59px. 표지의 수평선과 수직선이 만나는 칸만 일정한 사선 해칭으로 채운다.
- 구분선 1px, 중요한 카드 시작선 2px. 아이콘 둘레 원은 연한 외곽선, 아이콘은 원 지름의 약 55%.
- 순서는 직사각형 몸통과 각진 화살촉으로 표현한다. 관계는 얇은 원호·직선으로 연결하고 중심에 핵심 단어를 둔다.

## 여백과 위계
- 기준 여백은 좌우95px, 위아래64px. 페이지 본문은 12×6이며, 원본의 정보 시작선인 y260 부근과 맞춘다.
- 간격 단계: 12 / 24 / 40px, 패널 안쪽32px. 작은 칸은 공유 토큰의 계산값으로 간격을 줄인다.
- 실재 로드되는 Pretendard Variable. 원본 제목64px/700, 표지76px, 본문18~22px, 작은 영문18px, 주요 수치44~64px. 모든 라이브러리 크기는 `--type-N` 단계.
- 카드의 이름과 note 자리를 일정하게 예약해 설명 길이가 다른 카드의 제목 시작선이 흔들리지 않게 한다. 짧은 수치 패널에서는 수치와 이름을 같은 줄에 놓고 아래에 구분선을 둔다.

## 팔레트의 자리 — 디자인은 특정 색을 갖지 않는다
| 쓰임 | 자리 |
|---|---|
| 페이지 / 일반 글자 | `--page` / `--ink` |
| 큰 제목, 진한 레일, 선택한 단계 | `--a1-7` |
| 주 강조 채움과 글자 | `--a1` / `--a1-on` |
| 진한 레일 위 글자 | `--page` |
| 조용한 카드와 표의 보조 면 | `--n-1`, `--n-2` |
| 구분선·나머지 비중 | `--n-3`, `--n-4` |
| 보조 글자 | `--n-7` 이상 |
| 누적·다중 시리즈 | `--a1`부터 `--a4`까지 순위로 배정, 면은 각 `-3-soft` |
| 양호·위험 | 의미 토큰 `--good`, `--bad` |

원본 색은 컬렉션 CSS에 저장하지 않는다. 재조립본의 `assets/source-palette.css`는 원본을 비교하기 위한 외부 style 공급자이며 색 변수만 가진다. `assets/type-steps.css`는 README 표준 측정값 공급자다. 요소 시트는 제공된 reference palette의 라이트·다크로 그린다.

## 원본에 없는 요소의 확장
추가56종을 동일한 구조 문법으로 설계했다. 가격·코드·히트맵·로드맵은 직사각형 면과 시작 레일, 트리·네트워크·저니는 얇은 연결선과 원형 결정점, 게이지·불릿은 곧은 트랙을 사용한다. 색 변경으로 디자인의 정체성이 사라지지 않도록 형태와 간격에 중심을 둔다.
''')
(P/'review-notes.md').write_text('''# Crossrail 검수 기록

## 범위와 순서
- 073 회사소개서의 `slide_01.png`~`slide_30.png`, 총30장, 전부1280×720.
- README 220줄 전체를 먼저 읽음 → 원본30장 개별 확대 확인 → 독립 replica30장 → 디자인 언어 → kit/foundation/요소56개 → 라이트·다크 시트 → 컬렉션 재조립30장.
- replica는 원본 이미지를 배경으로 사용하지 않음. HTML텍스트·CSS도형·직접작성SVG차트 및 단순아이콘만 사용. 사진은 요청대로 연한 회색 placeholder.
- 공식 fixture28개는 제공된 원본 마크업과 데이터에서 collection의 `data-el`만 변경. 나머지는 구조 예시 markup을 사용하며 CSS는 새로 작성.

## 원본과 replica 비교
모든30장 원본|replica PNG를 실제 브라우저 렌더 후 한 장씩 열어 비교했다. 두 번째 보정에서 원본 네이비 픽셀(30,56,93)을 확인하고 제목 위치·자간, 수평 화살표 연결, 14번 역방향 화살표,22번 배경 막대,24번 도넛 라벨·리더,29번 방향선을 수정했다. 최종 수정 후 다시30장 모두 렌더했다.

## 원본과 다르게 남는 부분
- 사진(03·04·15)은 명시된 회색 단색 placeholder다. 원본의 사진 색·질감·기기 디테일은 재현하지 않는다.
- 단순 아이콘은 직접 작성한 SVG선형 아이콘 또는 계약의 Lucide 자리로 대체했다. 원본의 채워진 아이콘과 선 굵기·실루엣이 조금 다르다.
- 원본 글꼴 이름이 이미지에 없으므로 표 안에서 Pretendard Variable을 선택했다. 일부 한국어 줄바꿈과 숫자 너비가 원본과 다르다.
- 24번 도넛의 숫자 라벨과 리더선은 HTML/SVG로 다시 그렸다. 실제 원본의 텍스트 외곽선·안티앨리어싱은 완전히 같지 않다.

## 재조립의 계약상 해석과 결정
- 모든 재조립 본문은 `.slide > .page > .body`12×6. 페이지 HTML은 kit/foundation/element CSS만 사용하고 새 페이지 CSS나 임의 클래스는 넣지 않았다. 표지01·25는 foundation.cover 계약을 따른다.
- 02·30의 비대칭 구조는 foundation의 재사용 가능한 `.rail.on` 및 `.head.at-bottom-left` 배치로 옮겼다. 30의 연락처 오른쪽 구조는 유지하지만 원본의 교차선은 foundation 공통 규칙으로 단순화했다.
- 03의 사진 위 흰 여백 패널,04의 화면 가장자리까지 닿는 사진,05의 비대칭 기둥은 12×6 내부의 prose/table/image-frame/card로 다시 배치했다. 원본의 절대좌표와 똑같은 배치로 억지로 늘리지 않았다.
- 06의 원본 피라미드 안 중복 키워드는 각 level의 단일 name으로 정리했다. 같은 구조상 의미는 유지한다.
- 07·18의 반원 또는 오각형 관계는 모든3~6멤버가 유지되는 hub의 일정한 원형 배치로 일반화했다.
- 09·21 수치 카드는 같은 줄의 fig/name과 아래 note를 갖는 짧은 패널로 구현했다. 장문 note에 따라 title이 오르내리지 않게 예약 행을 둔다.
- 13의 별도 아이콘레일은 vertical steps의 원형 번호와 outline capsule로 통합했다. 원본의 아이콘 열과 번호 열을 서로 다른 임의 요소로 만들지 않았다.
- 14 하단 원본은 역방향 화살표다. 라이브러리 steps계약에는 역방향변형이 없어 번호06·05·04의 정보를 보존한 왼쪽→오른쪽 행으로 재조립했다.
- 17의 중심 시장 매력도 원과 4분면 조합은 matrix의4개 판단 패널로 일반화했다. 4개 이름·설명은 유지한다.
- 22의 배경 보조막대와23의 원 안 항목 이름은 line/bar의 표준 마크업으로 표현하여 정확한 추세와 값에 우선순위를 두었다.
- 24의 원본은5개조각 원그래프지만 donut계약은 한 비중만 받는다. 왼쪽에5개 비중을 보존하고 오른쪽은 주 강조 비중30%를 나타내는 donut으로 옮겼다. 원본과 다른 가장 큰 계약상 해석이다.
- 27 달력은 table계약으로 옮겨 날짜를 보존했다. 원본처럼 일자15~20의 임의 셀 서식은 별도 CSS로 추가하지 않았다.
- 28은 timeline.alt,29는 positioning+table로 재조립했다. 유사 위치들의 이름이 부딪치지 않도록 원본 위치를 약간 조정했다.

## 불명확한 문구
원본의 주요 제목·숫자·문장은 모두 읽을 수 있었다. 일부 반복 설명은 문장부호와 띄어쓰기를 정리했고 재조립 카드에서 장문을 축약했다. 판독 불가 문구를 장식선으로 대신하지 않았다. 20xx·00000·00% 등 원본의 예시 데이터는 실제 값인 것처럼 해석하지 않고 그대로 보존했다.

## 품질 이슈와 수정
- 공식 preview.py는 type단계·팔레트를 공급하지만 standalone문서는 공급하지 않으므로 별도 표준 provider를 연결했다. 첫 재조립 빌드에서 발견한 크기 누락을 수정한 후 재렌더했다.
- 헤더 없는 library fixture가172px제목행에 갇히는 문제를 `.page`구조 조건으로 수정해 전체 시트 영역을 사용한다.
- 작은 카드·vertical steps·표·roadmap·연락처 목록의 overflow를 실제 요소CSS의 container단계로 수정했다.
- 라이트/다크 대비 검사에서 보조글자 `--n-6`를 더 깊은`--n-7`로, 코드 숫자는`--n-8`로 조정했다. preview의 전역small스타일이 단위에 새어드는 것은 요소범위에서inherit로 교정했다.
- line/area는 fixture값을 특수처리하지 않는다. CSS anchor로 먼저배치된 이전 점과 현재 점을 연결하여 임의 데이터에 따라 그린다. 이는 최신Chromium이 제공하는CSS Anchor Positioning을 사용한다.
- 샘플 card-4의 `✹` 아이콘문자는 “모범fixture동일markup”과 “새아이콘Lucide” 규칙이 충돌한다. 사용자 지시에 따라 제공된 모범fixture를 정확히 보존하고, 새로 만든 아이콘에는 empty data-icon만 사용했다.

자동 검사 상세는 주 에이전트가 통합해 함께 제출한다. 자동 검사는 글자모양의 미묘한 차이를 증명하지 않으므로 원본과의 시각차는 위 기록을 함께 본다.
''')
print('56 specific descriptions + design-language.md + review-notes.md written')
