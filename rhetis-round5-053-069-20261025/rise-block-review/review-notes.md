# rise-block 검수 기록 — round5

## 실제 컬렉션 구성

- 관찰 디자인 및 실제 중첩 의존성: 1개.
- 삭제한 미관찰 일반 요소: 55개 — agenda, architecture, balance, bullet, callout, card, chart-area, chart-bar, chart-donut, chart-line, chart-scatter, chart-stack, chart-waterfall, code, concentric, cycle, decision-tree, delta, flowchart, funnel, gauge, headline, heatmap, hierarchy, hub, image-frame, journey, legend, list, logo-group, matrix, matrix-nine, metric, mindmap, network, person, pill, positioning, pricing, prose, pyramid, quote, radar, roadmap, sankey, slope, sparkline, steps, swimlane, table, tag, treemap, venn, versus, waffle.
- 독립 디자인/패널로 교체한 기존 계열 폴더: 0개 — 없음.
- 새 디자인 폴더: 없음.
- 원본은 위에서 아래로 의미 요소를 먼저 분류했습니다. 글자 조각을 DOM 잔여물로 잘라 gap으로 남기지 않았습니다.
- 표제 틀은 foundation.panel이 소유하고, 표·차트·카드는 독립 data-el 요소로 중첩했습니다.
- 페이지 body는12×6이며 패널 내부의 배치는120×60 비율 그리드입니다. 이 내부 그리드는 데이터가 아니라 하위 요소의 원본 상대 위치를 보존하는 foundation 레이아웃입니다.
- 사진·3D·복잡한 이미지 자리는 연한 중성 면이며, 페이지 전체 장식은 foundation 배경 vector로 기록합니다.
- replica 파일203개와 제공된 폰트는 원본 SHA-256으로 보존합니다.
- fixture는 새 한국어 업무 문구이며, 원문은 조립 검증 페이지에만 사용합니다.
- 원본 숫자 굵기·선·형태 수치는 유지하되 색과 글자 크기는 round5의 팔레트 역할·8–256 타입 토큰을 따릅니다.
- git 명령을 사용하지 않았습니다. 이전 결과를 덮어쓰지 않고 별도 round5 폴더에서 작업했습니다.

## 패널과 차트 확장

패널 없음.

차트 확장: 없음.

## 요소 담당 검수 기록

# rise-block — round5

기존 관찰 요소만 유지했습니다. 55개 일반 요소 폴더를 제거했습니다. 남은 gap은 없습니다.

유지: timeline

삭제: chart-line, versus, code, metric, positioning, concentric, chart-donut, steps, bullet, cycle, decision-tree, headline, card, image-frame, chart-stack, pill, slope, delta, flowchart, funnel, person, list, quote, pricing, network, roadmap, pyramid, callout, chart-bar, sankey, architecture, waffle, agenda, sparkline, matrix-nine, gauge, swimlane, chart-scatter, journey, hierarchy, prose, treemap, matrix, tag, chart-area, venn, radar, chart-waterfall, heatmap, logo-group, hub, table, legend, balance, mindmap


### 주 에이전트 최종 통합 검수

19–20페이지의 타임라인은 소유 요소에서 연결선을 그립니다. 이 덱에 없는 일반 요소는 추가하지 않았습니다.

공통 판단: 원본 색을 팔레트 역할로 바꿨으므로 검증 페이지 색은 원본과 다릅니다. 사진·3D는 중성 placeholder입니다. 자유 좌표를 body의12×6 정수 격자로 옮긴 조립본은 원본/replica와 픽셀 단위로 같지 않습니다. 작은 칸에서의 가독성 검수는 각 fixture의 명시 min 이상 범위이며 min 미만을 보장하지 않습니다. 보존한 replica의 기존 문구·판독 판단은 바꾸지 않았고 새로 지어낸 fixture 문구만6자 중복 검사했습니다. 최종 주 에이전트 열람은435개 시트PNG와95개 삼단 비교PNG의 SHA-256에 연결되어 있습니다. GitHub 게시에는 git 명령 대신 연결 도구와 HTTP API만 사용합니다.

검수 ZIP에는 이 컬렉션 CSS에서 실제 참조하는 폰트 계열만 포함합니다. 제공된 전체32개 폰트 파일은 소스에서 그대로 보존하며, ZIP에 포함하는 폰트의 바이트도 바꾸지 않습니다. 원본32개 전체를 각 ZIP에 중복 포함했을 때 GitHub 파일 API 요청 크기를 넘었던 문제를 사용하지 않는 폰트 제외로 해결했습니다.


## 최종 통합 검수

실제 마지막 렌더와 검수한 시트/페이지 해시는 루트 primary-visual-review.json 및 각 audits에 기록합니다. 최종 성공 여부는 verification.json을 기준으로 확인합니다.
