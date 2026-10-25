# corner-signal 검수 기록 — round5

## 실제 컬렉션 구성

- 관찰 디자인 및 실제 중첩 의존성: 30개.
- 삭제한 미관찰 일반 요소: 42개 — agenda, balance, bullet, callout, chart-line, chart-scatter, chart-stack, chart-waterfall, code, cycle, decision-tree, delta, flowchart, funnel, gauge, heatmap, hierarchy, journey, legend, list, logo-group, matrix, matrix-nine, metric, mindmap, network, pill, pricing, pyramid, quote, radar, roadmap, sankey, slope, sparkline, swimlane, table, tag, treemap, venn, versus, waffle.
- 독립 디자인/패널로 교체한 기존 계열 폴더: 14개 — architecture, card, chart-area, chart-bar, chart-donut, concentric, headline, hub, image-frame, person, positioning, prose, steps, timeline.
- 새 디자인 폴더: agenda--notched, architecture--layers, card--differentiators, card--feature, card--market-forecast, card--metric, card--opportunity, card--pentagons, chart-area--growth, chart-area--overlap, chart-bar--annual, chart-bar--forecast, chart-bar--grouped, chart-donut--allocation, chart-donut--metrics, chart-line--multi, concentric--ascending, concentric--market, headline--statement, hub--product, image-frame--leader, list--allocation, person--team, positioning--market, pricing--models, prose--letter, steps--funding, steps--process, timeline--phases, versus--mirror.
- 원본은 위에서 아래로 의미 요소를 먼저 분류했습니다. 글자 조각을 DOM 잔여물로 잘라 gap으로 남기지 않았습니다.
- 표제 틀은 foundation.panel이 소유하고, 표·차트·카드는 독립 data-el 요소로 중첩했습니다.
- 페이지 body는12×6이며 패널 내부의 배치는120×60 비율 그리드입니다. 이 내부 그리드는 데이터가 아니라 하위 요소의 원본 상대 위치를 보존하는 foundation 레이아웃입니다.
- 사진·3D·복잡한 이미지 자리는 연한 중성 면이며, 페이지 전체 장식은 foundation 배경 vector로 기록합니다.
- replica 파일203개와 제공된 폰트는 원본 SHA-256으로 보존합니다.
- fixture는 새 한국어 업무 문구이며, 원문은 조립 검증 페이지에만 사용합니다.
- 원본 숫자 굵기·선·형태 수치는 유지하되 색과 글자 크기는 round5의 팔레트 역할·8–256 타입 토큰을 따릅니다.
- git 명령을 사용하지 않았습니다. 이전 결과를 덮어쓰지 않고 별도 round5 폴더에서 작업했습니다.

## 패널과 차트 확장

- replica 12: White containing sheet with primary top rule and upper-left triangular notch; its children own editable chart names and all data. / bbox [77, 219, 725, 429]
- replica 12: White containing sheet with primary top rule and upper-left triangular notch; its children own editable chart names and all data. / bbox [818, 219, 387, 429]
- replica 13: Plain white containing sheet; no coloured top rule, notch, outline or rounding. / bbox [77, 317, 1128, 327]
- replica 14: White chart plate with an 11px primary top rule and upper-right 68×69 triangular tab. / bbox [77, 215, 366, 433]
- replica 14: White chart plate with an 11px primary top rule and upper-right 68×69 triangular tab. / bbox [458, 215, 366, 433]
- replica 14: White chart plate with an 11px primary top rule and upper-right 68×69 triangular tab. / bbox [840, 215, 365, 433]
- replica 15: Plain white containing sheet; no coloured top rule, notch, outline or rounding. / bbox [71, 229, 713, 413]
- replica 20: White containing sheet with primary top rule and upper-left triangular notch; its children own editable chart names and all data. / bbox [77, 219, 725, 429]
- replica 20: White containing sheet with primary top rule and upper-left triangular notch; its children own editable chart names and all data. / bbox [818, 219, 387, 429]

차트 확장: chart-area--growth, chart-area--overlap, chart-bar--grouped, chart-donut--allocation, chart-line--multi.

## 요소 담당 검수 기록

# Corner Signal Round 5 최종 요소 검수

21페이지의 관찰된 형태를 30개 독립 디자인, 19개 기존 계약 계열, 40개 원본 요소 인스턴스로 다시 구성했다. 01 표지는 공통 페이지 장치와 사진 영역이 담당한다. 이전 범용 CSS를 재사용하지 않고 원본의 좌표·도형·문자 위계에서 CSS를 새로 작성했다. 요소 마크업에는 직접 그린 SVG를 넣지 않았다. 아이콘은 빈 Lucide 슬롯이며 연결선과 도형은 소유 요소 CSS가 그린다.

## 페이지와 디자인 대응

| 페이지 | 요소 폴더 |
|---|---|
| 02 | agenda--notched (2판) |
| 03 | prose--letter, image-frame--leader |
| 04 | headline--statement |
| 05 | card--feature (3개) |
| 06 | steps--process |
| 07 | card--opportunity, concentric--market |
| 08 | card--market-forecast, concentric--ascending |
| 09 | hub--product |
| 10 | card--pentagons |
| 11 | pricing--models |
| 12 | chart-donut--metrics, chart-area--growth |
| 13 | card--metric (4개), chart-bar--annual |
| 14 | chart-line--multi, chart-area--overlap, chart-bar--grouped |
| 15 | positioning--market, card--differentiators |
| 16 | versus--mirror |
| 17 | timeline--phases |
| 18 | architecture--layers |
| 19 | person--team (5개) |
| 20 | chart-donut--allocation, list--allocation, chart-bar--forecast |
| 21 | steps--funding |

기존 14개 관찰 계열은 독립 디자인으로 교체했다. 이전의 관찰 없는 42개 범용 폴더는 제거했으며, 그중 agenda·chart-line·list·pricing·versus는 실제 관찰된 형태로 새로 작성했다. 사용되지 않는 37개 계약 계열은 억지로 채우지 않았다. 영문 description.md 30개를 작성했고 계약 ID는 기존 leaves.json과 일치한다.

## 패널과 소유권

패널 9개를 지도에 기록했다. 12·20페이지는 각각 [77,219,725,429], [818,219,387,429]의 tip-l 패널이다. 13페이지는 [77,317,1128,327]의 무장식 패널이다. 14페이지는 [77,215,366,433], [458,215,366,433], [840,215,365,433]의 tip-r 패널이며, 15페이지는 [71,229,713,413]의 무장식 패널이다. 패널 구현은 공통 foundation 소유다. 차트 내부 제목·설명·범례·축은 해당 차트 소유다. 페이지 사진과 큰 배경 윤곽은 공통 페이지 장치로 분리했다. 측정 덤프나 작은 캡션을 미지원 영역으로 남기지 않았다. 최종 GAPS는 0개다.

## 실제 수정과 검수

- 02의 노치 두 판, 08의 상승하는 겹침 오각형, 10의 교차 방향 사업모델 4개, 11의 두 요금 항목을 가진 모델 3판, 16의 두 회사 거울 막대, 19의 CEO와 팀 프로필, 21의 자금 단계 4개를 각각 원본 부품과 배치로 구성했다.
- 14페이지의 3시리즈 선, 2시리즈 영역, 2그룹×2막대 및 20페이지의 4분할 파이를 실제 데이터와 연결했다. Y축 눈금은 --max에서 계산한다. 원본의 고정 글자나 고정 경로를 데이터 대신 사용하지 않는다.
- 파이 대체값 35/25/25/15에서 라벨이 다른 조각에 가려지던 결함을 수정했다. 조각과 라벨의 쌓임을 분리했으며 해당 대체값을 그대로 유지해 검수했다.
- positioning의 일반 마크 규칙이 버블의 중앙 정렬을 덮던 문제를 제거했다. 원본의 84/98/100/130 지름과 중앙 이름 정렬을 보존했다.
- metrics 링은 바깥 173, 안쪽 147, 선 두께 13의 실제 비율을 복원했다. radial mask의 기준을 closest-side로 고쳐 두꺼워 보이던 오류를 없앴다.
- 아이콘은 경로 경계가 아닌 실제 SVG 뷰포트로 측정했다. 05의 Handshake/ListTodo/Settings, 18의 Factory/PackageOpen 등 실제 아이콘 종류와 크기를 교정했다.
- 단계 설명 fixture의 의미 없는 짧은 조각을 완결된 냉장물류 문장으로 교체했다. 원본의 수동 줄바꿈 수는 유지했다.
- 16·17의 중성 진하기 구분과 13의 quiet 숫자 위계를 복원했다. 03의 작은 캡션은 한 줄을 유지했다.

최종 정식 시트는 70 fixture × 허용 크기 × 라이트·다크의 508 상태다. 잘림, 글자 겹침, 이름·수치 숨김, 실제 배경 대비, 폰트 오류, 그리기 영역 초과, chip 정렬 오류는 모두 0건이며 staleDuringRender도 0건이다. 공식 시트의 큰 칸과 최소 칸을 확대해서 형태와 정렬을 직접 확인했다. 발견된 결함은 수정 후 해당 전체 상태를 다시 렌더했다.

원본 좌표의 native 비교 40개를 양 모드로 렌더한 80상태도 영역 초과·글자 겹침·폰트 오류 0건이다. native root 크기가 원본 bbox와 일치함을 자동 검사했다. 핵심 원본 비교를 개별로 열어 도형·문자·선·아이콘을 확인했다. 최종 21페이지 전체 조립의 페이지 장치와 통합 비교는 주 에이전트가 수행한다.

별도 수치 검사는 7개 대체 데이터 사례에서 오류 0건이다. max=120/180/60의 축 눈금, 점의 Y 좌표, 다음 점 연결 길이·회전, 막대 높이, 파이 합계 100과 시작 각도를 확인했다. fixture 원문 6-gram 검사는 80개 대상에서 0건이다. 요소 fixture 70개와 공통 패널 fixture 10개를 포함한다.

수치 근거와 결과는 corner-signal-review/audits 및 sheets에 있다. 추가 native·수치·문구 검사 기록은 /workspace/work/element-rebuild/corner-round5-native/audit.json, corner-round5-numeric-probe.json, corner-round5-text.json에 남겼다.

## 차이와 판단

사진·기기 화면은 요청대로 중성 회색 seat다. 원본 고정 색상은 팔레트 역할로 옮겼으며, 밝은 면 위 작은 흰 글자의 대비가 부족한 경우 잉크 역할로 읽히게 했다. 이는 색 역할 해석이며 원본의 도형과 마크업은 유지했다.

원본의 7.5px 캡션은 허용 토큰 최솟값 8px을 사용한다. 겹침 영역 차트의 원본 값 라벨이 다른 계열 선과 만나는 곳에는 작은 페이지색 배경을 두어 읽히게 했다. 원본 연간 막대의 시각적 높이와 인쇄 수치가 서로 다른 경우 canonical 지도는 원본을 보존하고 새 fixture는 데이터와 문구를 일치시켰다. 원본 거울 비교의 00%도 canonical에서는 유지하고 새 fixture에서는 의미 있는 실제 수치로 바꿨다. 곡선의 CSS 다각형 근사와 브라우저 래스터 경계에는 미세한 차이가 있을 수 있다. 완전한 픽셀 동일성을 주장하지 않는다.

요소 CSS·fixture·지도는 최종 동결했다. 공통 foundation의 마지막 지문 동기화와 전체 조립 산출물 갱신은 주 에이전트가 담당한다. git 작업은 수행하지 않았다.


### 주 에이전트 최종 통합 검수

01 표지 로고의 77/69 위치와 단순 점·사선 기호를 foundation에서 복구했습니다. 05 세 아이콘의 의미를 구분했고, 12의 도넛은 원본173/147 지름에서13px 링 두께 비율을 복원했습니다. 15 positioning bubble은 가운데 정렬을 복구했습니다. 16 비교 막대 및17 계단 면은 서로 다른 중성 역할을 유지합니다. 20 조각 라벨은 쐐기 위에 별도 층으로 두어 작은 조각에서도 가려지지 않습니다. 19의 다섯 인물 카드가 본문 정수 격자로 투영되면서 높이가 교대로 달라지는 점은 조립 한계로 남습니다.

공통 판단: 원본 색을 팔레트 역할로 바꿨으므로 검증 페이지 색은 원본과 다릅니다. 사진·3D는 중성 placeholder입니다. 자유 좌표를 body의12×6 정수 격자로 옮긴 조립본은 원본/replica와 픽셀 단위로 같지 않습니다. 작은 칸에서의 가독성 검수는 각 fixture의 명시 min 이상 범위이며 min 미만을 보장하지 않습니다. 보존한 replica의 기존 문구·판독 판단은 바꾸지 않았고 새로 지어낸 fixture 문구만6자 중복 검사했습니다. 최종 주 에이전트 열람은435개 시트PNG와95개 삼단 비교PNG의 SHA-256에 연결되어 있습니다. GitHub 게시에는 git 명령 대신 연결 도구와 HTTP API만 사용합니다.

검수 ZIP에는 이 컬렉션 CSS에서 실제 참조하는 폰트 계열만 포함합니다. 제공된 전체32개 폰트 파일은 소스에서 그대로 보존하며, ZIP에 포함하는 폰트의 바이트도 바꾸지 않습니다. 원본32개 전체를 각 ZIP에 중복 포함했을 때 GitHub 파일 API 요청 크기를 넘었던 문제를 사용하지 않는 폰트 제외로 해결했습니다.


## 최종 통합 검수

실제 마지막 렌더와 검수한 시트/페이지 해시는 루트 primary-visual-review.json 및 각 audits에 기록합니다. 최종 성공 여부는 verification.json을 기준으로 확인합니다.
