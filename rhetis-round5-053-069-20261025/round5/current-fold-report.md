# current-fold Round5 검수 기록

## 의미 단위 분류와 폴더

18페이지를 위에서 아래로 읽고, 실제 관찰된 디자인만 남겼다.01·03·18은 표지 장치로 foundation에 귀속한다. 원본 replica는 수정하지 않았다. 아래의 페이지 번호는 독립 root 매핑이며,08의 중첩 tag/legend는 chart-bar--combo 의존성으로 들어간다.

| 폴더 | 원본 페이지 | fixture | 렌더 상태 | 계보 | flags |
|---|---|---:|---:|---|---:|
| agenda | 02 | 2 | 10 | current | 0 |
| card--capsules | 10 | 3 | 24 | current | 0 |
| card--case-study | 14 | 2 | 24 | current | 0 |
| card--certificate | 15 | 4 | 32 | current | 0 |
| card--kpi | 11 | 4 | 48 | current | 0 |
| card--metric | 16 | 6 | 72 | current | 0 |
| card--trend | 10 | 2 | 24 | current | 0 |
| chart-area | 11 | 2 | 8 | current | 0 |
| chart-bar--combo | 08 | 2 | 12 | current | 0 |
| hierarchy | 08 | 2 | 8 | current | 0 |
| hub | 06 | 2 | 8 | current | 0 |
| hub--competence | 13 | 2 | 4 | current | 0 |
| hub--spokes | 09 | 2 | 8 | current | 0 |
| image-frame | 04 | 2 | 36 | current | 0 |
| legend | 11 | 3 | 30 | current | 0 |
| list | 06 | 2 | 12 | current | 0 |
| logo-group--captioned | 14 | 2 | 20 | current | 0 |
| pricing--service-tier | 12 | 2 | 4 | current | 0 |
| prose | 04 | 2 | 18 | current | 0 |
| prose--signature | 04 | 2 | 28 | current | 0 |
| steps | 17 | 2 | 8 | current | 0 |
| table | 05 | 2 | 20 | current | 0 |
| tag | 11 | 2 | 36 | current | 0 |
| timeline | 07 | 2 | 8 | current | 0 |

## 실제 추가·분리

- card--capsules ←10: 세 원형 medallion 카드와 하단3캡슐. 캡슐은 독립 root 중복배치 대신 각 카드가 소유한다.
- card--trend ←10, card--kpi ←11, card--case-study ←14, card--certificate ←15, card--metric ←16: 서로 다른 실제 배치를 독립 디자인으로 분리했다. 사례 카드는205px 정사각 gradient 브랜드 면·캡슐 제목·3개 결과 행을 복원한다.
- hub--spokes ←09: 좌측174px core와 우측122px 원형 서비스 mark3개 및 별도 설명 열.
- hub--competence ←13:206px core, 좌우116px medallion6개, 실제 각도·길이의 점선 연결. 원래1093px DOM root 밖으로 나가는 우측 제목까지1099.016px 소유 union으로 기록했다.
- pricing--service-tier ←12: 네 단계의 제목 탭,96px 상징 아이콘, check4개와 추천 label을 패키지 전체가 소유한다. 가격 숫자로 바꾸지 않았다. 별도 list/tag로 잘라 두었던8개 인스턴스를 흡수했다.
- prose--signature ←04: 직함16px와 Nanum Pen48px 서명을 분리된 prose closing으로 복원했다. 원래 root51.17px와 전체72px 서명 행을 source 자료에 구별해 기록했다.
- logo-group--captioned ←14:547×422의3×3 dotted wall, y24의70px 정사각 placeholder, y43 index, y99의18px/700 캡션을 복원했다. caption은 이미지로 평탄화하지 않았다.

## 패널·사진·차트 확장

추가 foundation.panel 제안은 없다. 이번 복합 디자인의 제목 면과 자식은 모두 해당 의미 요소 하나의 부품이므로, 별도 패널 제목을 중복하지 않는다.05의 장식 없는 사진은 부모가 승인한 foundation.seat furniture로 추가했다: `current-fold-05-photo-seat`, bbox[129,230,535,422], seatClass wide.

08은 chart-bar--combo로 통합했다. 하나의535×422 viewport가 bar6개, 내부 `.line > .pt`6개, 한 벌 연도축, 중첩 legend 및 tag 제목을 소유한다. 기존 독립 line·범례·제목 인스턴스는 absorbed_instances에 기록했다.11의 두 시리즈 area는 기존 전체-series 소유 구조를 유지했다.

## 삭제와 gap

기존 관찰 디자인이 대체·흡수되어 제거된 기본 폴더: card, pill, chart-bar, chart-line, logo-group.

원본에 직접 관찰되지 않은 generic 폴더 제거: architecture, balance, bullet, callout, chart-donut, chart-scatter, chart-stack, chart-waterfall, code, concentric, cycle, decision-tree, delta, flowchart, funnel, gauge, headline, heatmap, journey, matrix, matrix-nine, metric, mindmap, network, person, positioning, pricing, pyramid, quote, radar, roadmap, sankey, slope, sparkline, swimlane, treemap, venn, versus, waffle.

기존11개 unexpressible은 signature, 서비스 패키지의 label, 사례 카드, 고객사 caption, 두 hub 디자인의 실제 소유 구조로 복원했다. 현재 map의 unexpressible은0개이다. font dump·캡션 조각을 별도 gap으로 남기지 않았다. 원본 측정 정보는 source 자료에 남기고 design은 읽을 수 있는 구성 설명으로 바꿨다.

## 검수와 수정

실제 Chromium으로24개 디자인의 지원 크기·최소 칸을 라이트/다크 양쪽 모두 렌더했다. 요소별 시트48장을 각각 열어 멤버/선/면/타이포와 최소·최대 크기 배치를 직접 보았다. source 대응 비교 PNG도 신규 card계열, hub, combo, pricing, signature, logo를 확인했다. 이번 단계는 요소 검수이며 새18페이지 조립본의 최종 통합 비교는 주 에이전트 담당이다.

직접 본 시트에서 발견해 수정한 항목: 캡슐의 잘못된 타원 반경, intrinsic text 폭 때문에 생긴 긴 캡슐 줄바꿈, metric의28px unit 누락, 큰 칸에서 고정 type 상한 때문에 벌어진 계층, certificate 제목 띠 역할, source figure−1px tracking, KPI 회색 글자 대비, 투명 gradient-text를 가시 강조 역할로 정리한 figure, 로고 fixture의 caption 누락. 원/정사각형은 공유 min unit으로 비율을 보존한다. 시트 아이콘은 사용자 요청대로 점선 슬롯이고, 실제 Lucide SVG는 조립 렌더에서 주입된다.

fixture는 새 물류업무 문구로 작성·정리했다. 모범 generic fixture를 유지하기 위해 원본 없는 방향·모양을 추가하지 않았다. 각 디자인은2개 이상의 source-shaped/긴 문구/멤버 수 변형 fixture를 갖는다. 원문6gram 검사는59개 파일에서0건이었다. 실제 source 문구는 조립 검증 마크업에만 보존한다.

## 마지막 계보 확인

- 디자인 24개, fixture 58개, 양모드 크기 상태 502개.
- notCurrent 0, stale 0, flags 0.
- 모든 element.json의 contract ID를 contract/leaves.json과 대조했다. card는 card.parts@1을 사용한다.
- 공통 foundation·type·renderer 고정 이후 마지막 CSS/fixture 수정이 최종 PNG에 반영되도록 다시 렌더했다. 이후 요소 CSS/map은 동결한다.
