# scanline-rise 검수 기록 — round5

## 실제 컬렉션 구성

- 관찰 디자인 및 실제 중첩 의존성: 36개.
- 삭제한 미관찰 일반 요소: 38개 — balance, bullet, callout, chart-donut, chart-line, chart-scatter, chart-stack, chart-waterfall, code, concentric, decision-tree, delta, flowchart, funnel, heatmap, journey, legend, logo-group, matrix, matrix-nine, metric, mindmap, network, person, pill, positioning, pricing, pyramid, quote, radar, roadmap, sankey, slope, sparkline, swimlane, treemap, venn, waffle.
- 독립 디자인/패널로 교체한 기존 계열 폴더: 5개 — chart-area, chart-bar, list, prose, tag.
- 새 디자인 폴더: callout--band, callout--large, callout--tipped, card--caption, card--checklist, card--diagnosis, card--project-brief, card--project-detail, card--row-blue, card--row-neutral, card--summary, card--tiered, chart-area--mini, chart-bar--combo, chart-bar--comparison, chart-bar--grouped, chart-donut--annotated, headline--tracked, hub--clover, image-frame--accent-device, image-frame--wide, table--issues, timeline--period-strip.
- 원본은 위에서 아래로 의미 요소를 먼저 분류했습니다. 글자 조각을 DOM 잔여물로 잘라 gap으로 남기지 않았습니다.
- 표제 틀은 foundation.panel이 소유하고, 표·차트·카드는 독립 data-el 요소로 중첩했습니다.
- 페이지 body는12×6이며 패널 내부의 배치는120×60 비율 그리드입니다. 이 내부 그리드는 데이터가 아니라 하위 요소의 원본 상대 위치를 보존하는 foundation 레이아웃입니다.
- 사진·3D·복잡한 이미지 자리는 연한 중성 면이며, 페이지 전체 장식은 foundation 배경 vector로 기록합니다.
- replica 파일203개와 제공된 폰트는 원본 SHA-256으로 보존합니다.
- fixture는 새 한국어 업무 문구이며, 원문은 조립 검증 페이지에만 사용합니다.
- 원본 숫자 굵기·선·형태 수치는 유지하되 색과 글자 크기는 round5의 팔레트 역할·8–256 타입 토큰을 따릅니다.
- git 명령을 사용하지 않았습니다. 이전 결과를 덮어쓰지 않고 별도 round5 폴더에서 작업했습니다.

## 패널과 차트 확장

- replica 10: Thin accent outline encloses the consumption ratio callout and annotated donut. / bbox [667, 323, 494, 321]
- replica 08: Shared thin accent chart enclosure behind the combined plot and bottom callout. / bbox [119, 335, 484, 302]

차트 확장: chart-area--mini, chart-bar--combo, chart-bar--grouped, chart-donut--annotated, table.

## 요소 담당 검수 기록

# Scanline Rise — Round5 완료 보고

2026-10-25. 동결된 18장 replica의 실제 DOM·계산 스타일·PNG를 기준으로 다시 분류했다. 최종 요소 폴더는 **36개**, 신규 독립 디자인은 **23개**다. 기존 56개를 채우기 위해 남아 있던 미관찰·중복·대체 폴더 **43개**를 제거했다. 남은 GAP는 **0개**다. replica와 다른 컬렉션, foundation, 공통 도구는 수정하지 않았다.

## 페이지 위에서 아래로 읽은 요소

| 페이지 | 소유 요소 |
|---|---|
| 01 | 표지의 브랜드·제목·배경: foundation 페이지 장치 |
| 02 | `agenda` |
| 03 | `headline` → `cycle` → `card--row-blue` |
| 04 | `card` → `callout--large` |
| 05 | `hub` → `card--checklist` |
| 06 | `hierarchy` → `architecture` |
| 07 | `card` → `headline` → `gauge` → `timeline` |
| 08 | `headline--tracked` → `card` → `callout--tipped` → `chart-bar--combo` |
| 09 | `table` → `chart-area--mini` |
| 10 | `headline` → `card--row-neutral` → `chart-donut--annotated` → `callout--band` |
| 11 | `image-frame` → `card--project-brief` → `card--project-detail` → `image-frame--accent-device` → `chart-bar--comparison` |
| 12 | `card--tiered` |
| 13 | `headline` → `card--caption` → `chart-bar--grouped` |
| 14 | `versus` → `card--diagnosis` |
| 15 | `table--issues` |
| 16 | `hub--clover` |
| 17 | `steps` → `timeline--period-strip` |
| 18 | `card--summary` → `image-frame--wide` |

03·10의 인접 라벨·본문 조각은 각 행 카드 하나로, 12의 돌출 원형 아이콘·제목·연한 설명·하단 도구 목록은 tiered 카드 하나로 묶었다. 18의 번호·헤더·요약은 summary 카드가, 아래 사진은 wide frame이 소유한다. 03의 작동 원리 캡션은 cycle.note에 흡수했고 중복 furniture를 제거했다. 측정 문자열과 제목·라벨 조각을 GAP로 취급하지 않았다.

## 새 폴더와 원본

| 독립 폴더 | 원본 페이지 |
|---|---|
| `card--row-blue` | 03 |
| `callout--large` | 04 |
| `card--checklist` | 05 |
| `card--row-neutral` | 10 |
| `card--project-brief` | 11 |
| `card--project-detail` | 11 |
| `card--tiered` | 12 |
| `card--caption` | 13 |
| `card--diagnosis` | 14 |
| `card--summary` | 18 |
| `chart-bar--grouped` | 13 |
| `timeline--period-strip` | 17 |
| `image-frame--accent-device` | 11 |
| `image-frame--wide` | 18 |
| `hub--clover` | 16 |
| `chart-donut--annotated` | 10 |
| `callout--band` | 10 |
| `chart-bar--comparison` | 11 |
| `table--issues` | 15 |
| `chart-bar--combo` | 08 |
| `callout--tipped` | 08 |
| `chart-area--mini` | 09 |
| `headline--tracked` | 08 |

기존 `hub`, `timeline`, `hierarchy`, `architecture`, `cycle`, `versus`도 실제 원본 측정으로 CSS 전체를 새로 썼다. 특히 06에서 원본에 없던 세로 점선과 회색·파랑 연결선을 없애고, 중앙 점선 원을 실제 180px로 복원했다. 05·16의 연결 곡선은 CSS `shape()`의 quadratic curve로 직접 소유한다. 원본 SVG는 source 측정 필드에만 보존했고 fixture와 map.markup에는 SVG가 없다. 아이콘은 빈 Lucide 자리이며 시트의 점선 슬롯은 공식 preview 표현이다.

## 패널과 중첩 소유

- 08 `[119,335,484,302]`: 얇은 외곽 panel 안에 combo chart와 tipped callout. 네 분기·회색 막대·반투명 면·추세선·점·범례는 combo 하나가 소유한다.
- 10 `[667,323,494,321]`: 얇은 외곽 panel 안에 callout과 주석 도넛.
- 13의 회색 `[134,326,512,332]` 면은 단일 grouped chart의 자체 plotting surface다.
- 09의 세 miniature area는 table 내부에 포함된다. 11의 두 막대는 project-detail 내부에 포함되며 `[308,497,205,125]` 독립 source entry에 `contained_by`를 명시했다. 소스 대조 행은 만들고, 페이지 grid에는 중복 출력하지 않는다.
- 이전 versus의 list는 원본에 없는 중간 정규화 wrapper여서 `.members`로 흡수했다. 다른 관찰·중첩 참조가 없음을 확인한 뒤 list 폴더를 제거했다.

## 차트 데이터와 해석

08·09·11·13 원본에는 숫자 y축 눈금이 없고 수평 가이드만 있다. 고정 100/80 문자열을 만들지 않았다. 막대·점·면은 `--v`와 `--max`를 사용한다. 13은 `.bars.grouped > .group > label + .bar` 구조이며 08은 `.bars > .line > .pt` 결합 구조다.

10은 네 slice의 비율 40/25/25/10과 35/30/20/15 두 fixture를 사용한다. 각각 합100이며 중앙값·외부 백분율·라벨·누적 각도가 같은 데이터에 대응한다. 주석 가로선과 원형 바깥 점선은 도넛 CSS 소유다.

11 원본은 표기 10,000/35,000에 높이56/89를 사용하여 단순한 0기준 높이 비례와 맞지 않는다. 원본 높이를 임의로 바꾸지 않고, 같은 시각적 하한 높이와 값 비례 증분을 갖는 표현으로 보존했다. 숫자 y축이 존재하는 것으로 주장하지 않는다. fixture는 새로운12,500/34,000 및14,000/32,000을 사용한다.

## 실제 검수와 교정

정식 시트 **36개 폴더 × 라이트·다크 =72개 PNG**를 직접 열었다. 각 행의 허용 크기와 honest min을 보고, 원본 대조 PNG도 별도로 열었다. 모든 source entry의 원문 마크업을 원래 bbox에서 렌더한 native 검사와, 조립에서 문제가 난 실제 좁은 칸을 별도로 검사했다.

- 최종 공식 검사: **1170 states / 0 flags / 0 stale**. 실제 stage는1280×720이며, 폰트 로딩·문구 영역·겹침·paint overflow·대비·chip 잉크 중심을 검사했다.
- 현재 요소 fixture는100개 HTML이다. 원문6자 중복 검사기는 부모 foundation fixture3개까지 포함하여103개를 검사했고 문제0이었다.
- 최종 원문 native: **68회 / 글자 영역 밖0**. 원래 크기65개 source entry와 실제 조립칸3개를 포함한다.
- 추가 조립칸: 08 제목 `[99,252,173.33,61]`, `[655,252,80.66,61]`은 자연 줄바꿈으로 원문 전체를 표시한다. 14 비교판 `[191.66,471,914.67,134]`은 모든 세로 치수를 같은 단일 배율로 줄여 이름이 아래로 넘치지 않는다.
- 07 note의 브라우저 적용 padding은10px65px였다. CSS 파일의48px override는 실제 부모 구조에 맞지 않아 적용되지 않았다. 계산 스타일을 재측정해65px로 바로잡았고, 원본의 세 줄 잉크가 회색 face 아래4px까지 보이는 것을 포함해 bbox를986×122로 확정했다. 이것은 문구 축약이나 clipping이 아니다.
- 새 행 카드의 본문 폭을 짧은 원문의 intrinsic width로 잡았던 오류를 실제 할당 field로 고쳤다. 제목·아이콘은 flex 그룹으로 정렬해 원문 줄바꿈과 중앙을 맞췄다.
- 04의 중앙127px 점선 원·77px plus disc를 누락 없이 복원했다. 16은132px 바깥 원 안에76px 흰 자리와26px 실제 아이콘을 분리했다.
- 큰 칸에서 낮은 강조 띠가 판 전체 높이로 늘어나던 현상을 교정해, band/tip/period strip 모두 원본 비율과 연결 상태를 유지한다.
- 마지막 열람에서 남아 있던 agenda·steps의 반복 filler를 서로 다른 실제 운송 업무 내용으로 바꾸고 다시 렌더했다. CSS나 원문 map 문구를 fixture에 맞춰 바꾸지 않았다.

색은 `--page/--ink/--a1-7/--a1-N-soft/--n-N` 역할로만 배정한다. 사진·기기 화면은 허용된 단색 placeholder이며 실제 사진을 재현했다고 주장하지 않는다. 복원 중 새 원문 추측 문구를 추가하지 않았다. fixture 문구는 새 한국어 업무 예시이고, 원문은 map·재조립 검증에만 사용한다.

## 최종 폴더별 검사

모든 행의 대응 파일은 `scanline-rise-review/sheets/<folder>-light.png`, `-dark.png`, `-replica.png`다. 36개 폴더 모두 source entry가 있으며 중첩 인스턴스도 대조 행을 보유한다.

| 폴더 | fixture | honest min | states | flags |
|---|---:|---|---:|---:|
| `agenda` | 2 | 8x5, 9x4 | 10 | 0 |
| `architecture` | 2 | 6x2 | 28 | 0 |
| `callout--band` | 2 | 6x2 | 28 | 0 |
| `callout--large` | 2 | 6x2 | 28 | 0 |
| `callout--tipped` | 2 | 6x2 | 28 | 0 |
| `card` | 17 | 12x4, 3x2, 4x3, 8x4, 9x4 | 220 | 0 |
| `card--caption` | 2 | 6x4 | 20 | 0 |
| `card--checklist` | 2 | 6x6 | 12 | 0 |
| `card--diagnosis` | 2 | 6x2 | 28 | 0 |
| `card--project-brief` | 2 | 6x2 | 28 | 0 |
| `card--project-detail` | 2 | 6x4 | 20 | 0 |
| `card--row-blue` | 3 | 6x2 | 42 | 0 |
| `card--row-neutral` | 3 | 6x2 | 42 | 0 |
| `card--summary` | 2 | 6x4 | 20 | 0 |
| `card--tiered` | 3 | 4x6 | 24 | 0 |
| `chart-area--mini` | 3 | 3x2 | 60 | 0 |
| `chart-bar--combo` | 2 | 6x3 | 24 | 0 |
| `chart-bar--comparison` | 2 | 3x3 | 36 | 0 |
| `chart-bar--grouped` | 2 | 6x4 | 20 | 0 |
| `chart-donut--annotated` | 2 | 6x4 | 20 | 0 |
| `cycle` | 2 | 4x6 | 16 | 0 |
| `gauge` | 5 | 4x1, 8x4 | 80 | 0 |
| `headline` | 8 | 4x2, 6x2 | 136 | 0 |
| `headline--tracked` | 2 | 3x1 | 40 | 0 |
| `hierarchy` | 2 | 10x5 | 8 | 0 |
| `hub` | 2 | 10x5 | 8 | 0 |
| `hub--clover` | 2 | 12x6 | 4 | 0 |
| `image-frame` | 2 | 3x3 | 36 | 0 |
| `image-frame--accent-device` | 2 | 3x6 | 16 | 0 |
| `image-frame--wide` | 2 | 6x2 | 28 | 0 |
| `steps` | 2 | 10x5 | 8 | 0 |
| `table` | 2 | 12x6 | 4 | 0 |
| `table--issues` | 2 | 12x6 | 4 | 0 |
| `timeline` | 2 | 10x5 | 8 | 0 |
| `timeline--period-strip` | 2 | 6x1 | 28 | 0 |
| `versus` | 2 | 10x5 | 8 | 0 |

## 제거한 미관찰·중복·대체 폴더

`chart-line`, `code`, `metric`, `positioning`, `concentric`, `chart-donut`, `bullet`, `decision-tree`, `chart-stack`, `pill`, `slope`, `delta`, `flowchart`, `funnel`, `person`, `quote`, `pricing`, `network`, `roadmap`, `pyramid`, `callout`, `sankey`, `waffle`, `sparkline`, `matrix-nine`, `swimlane`, `chart-scatter`, `journey`, `treemap`, `matrix`, `venn`, `radar`, `chart-waterfall`, `heatmap`, `logo-group`, `legend`, `balance`, `mindmap`, `chart-bar`, `prose`, `tag`, `chart-area`, `list`

삭제된 옛 시트·audit의 고아 파일은 부모 통합 작업에서 현재 elements 폴더 목록 기준으로 정리한다. 이 보고의 결과는 현존36개 폴더에 한정한다. 소스와 CSS·fixture·map은 동결했다.


### 주 에이전트 최종 통합 검수

하단74px 리본을 표지까지 foundation vector로 복구했고 표지 연락처에 Lucide 아이콘을 넣었습니다. 11 기기 프레임은 자신의 z-index로 원본의 앞쌓임을 복원했습니다. 원본 카드와 폰은 약38px 겹치며 조립본에서는 12×6 반올림으로 약80.67px 겹칩니다. bbox나 페이지 grid를 요소 CSS에 맞추어 바꾸지 않았습니다. 03·10의 짧은 callout, 12 세 번째 카드, 14 비교 요소는 정수 격자 높이 차이로 조립본에서 더 작게 보입니다. 이 차이는 gap이 아니라 재조립 배치의 한계입니다. clover hub와 table 두 계열의 긴 fixture min을 9×4로 낮춘 뒤 정식 시트를 검수했습니다.

공통 판단: 원본 색을 팔레트 역할로 바꿨으므로 검증 페이지 색은 원본과 다릅니다. 사진·3D는 중성 placeholder입니다. 자유 좌표를 body의12×6 정수 격자로 옮긴 조립본은 원본/replica와 픽셀 단위로 같지 않습니다. 작은 칸에서의 가독성 검수는 각 fixture의 명시 min 이상 범위이며 min 미만을 보장하지 않습니다. 보존한 replica의 기존 문구·판독 판단은 바꾸지 않았고 새로 지어낸 fixture 문구만6자 중복 검사했습니다. 최종 주 에이전트 열람은435개 시트PNG와95개 삼단 비교PNG의 SHA-256에 연결되어 있습니다. GitHub 게시에는 git 명령 대신 연결 도구와 HTTP API만 사용합니다.

검수 ZIP에는 이 컬렉션 CSS에서 실제 참조하는 폰트 계열만 포함합니다. 제공된 전체32개 폰트 파일은 소스에서 그대로 보존하며, ZIP에 포함하는 폰트의 바이트도 바꾸지 않습니다. 원본32개 전체를 각 ZIP에 중복 포함했을 때 GitHub 파일 API 요청 크기를 넘었던 문제를 사용하지 않는 폰트 제외로 해결했습니다.


## 최종 통합 검수

실제 마지막 렌더와 검수한 시트/페이지 해시는 루트 primary-visual-review.json 및 각 audits에 기록합니다. 최종 성공 여부는 verification.json을 기준으로 확인합니다.
