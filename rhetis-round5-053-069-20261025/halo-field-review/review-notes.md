# halo-field 검수 기록 — round5

## 실제 컬렉션 구성

- 관찰 디자인 및 실제 중첩 의존성: 17개.
- 삭제한 미관찰 일반 요소: 40개 — architecture, balance, bullet, chart-area, chart-scatter, chart-stack, chart-waterfall, code, concentric, decision-tree, delta, flowchart, funnel, gauge, heatmap, hierarchy, hub, journey, list, logo-group, matrix, matrix-nine, metric, mindmap, network, pill, positioning, pricing, quote, radar, roadmap, sankey, slope, sparkline, swimlane, tag, treemap, venn, versus, waffle.
- 독립 디자인/패널로 교체한 기존 계열 폴더: 3개 — chart-bar, chart-line, headline.
- 새 디자인 폴더: card--program, card--service, chart-bar--combo, steps--rings.
- 원본은 위에서 아래로 의미 요소를 먼저 분류했습니다. 글자 조각을 DOM 잔여물로 잘라 gap으로 남기지 않았습니다.
- 표제 틀은 foundation.panel이 소유하고, 표·차트·카드는 독립 data-el 요소로 중첩했습니다.
- 페이지 body는12×6이며 패널 내부의 배치는120×60 비율 그리드입니다. 이 내부 그리드는 데이터가 아니라 하위 요소의 원본 상대 위치를 보존하는 foundation 레이아웃입니다.
- 사진·3D·복잡한 이미지 자리는 연한 중성 면이며, 페이지 전체 장식은 foundation 배경 vector로 기록합니다.
- replica 파일203개와 제공된 폰트는 원본 SHA-256으로 보존합니다.
- fixture는 새 한국어 업무 문구이며, 원문은 조립 검증 페이지에만 사용합니다.
- 원본 숫자 굵기·선·형태 수치는 유지하되 색과 글자 크기는 round5의 팔레트 역할·8–256 타입 토큰을 따릅니다.
- git 명령을 사용하지 않았습니다. 이전 결과를 덮어쓰지 않고 별도 round5 폴더에서 작업했습니다.

## 패널과 차트 확장

- replica 04: Rounded report panel; one ruled title and unit, legend, combo chart, then a footnote. / bbox [460.65625, 269, 765.34375, 401]

차트 확장: chart-bar--combo, chart-donut.

## 요소 담당 검수 기록

# Halo Field — Round 5 요소 검수 보고

## 범위와 출처

동결 replica를 수정하지 않고 실제 관찰된 17개 디자인을 검수했다. 아래 페이지 번호는 halo-field 원본 덱의 페이지다. 컬렉션·foundation·도구·다른 덱은 수정하지 않았다.

| 디자인 폴더 | 원본 페이지 | fixture | 검수 상태 수 |
|---|---|---:|---:|
| `agenda` | 02 | 2 | 10 |
| `callout` | 12 | 2 | 12 |
| `card` | 05 | 3 | 24 |
| `card--program` | 12 | 5 | 50 |
| `card--service` | 07 | 5 | 60 |
| `chart-bar--combo` | 04 | 2 | 24 |
| `chart-donut` | 15 | 2 | 12 |
| `cycle` | 06 | 2 | 8 |
| `image-frame` | 06 | 2 | 36 |
| `legend` | 04 | 2 | 22 |
| `person` | 14 | 5 | 32 |
| `prose` | 04 | 3 | 26 |
| `pyramid` | 08 | 2 | 8 |
| `steps` | 09 | 2 | 8 |
| `steps--rings` | 11 | 2 | 14 |
| `table` | 13 | 2 | 16 |
| `timeline` | 10 | 2 | 8 |

## 재매핑과 소유권

- 관찰되지 않은 범용 폴더 및 분리 이전 폴더 43개를 제거한 구조를 유지했다. 기존 `chart-bar`/`chart-line`은 실제 콤보 차트 `chart-bar--combo`로 통합되었고, 04페이지 차트 표제·단위·하단 설명은 foundation panel로 귀속되었다. 삭제 내역은 `halo-deleted.json`을 따른다.
- 04페이지 둥근 패널 1개는 범례와 콤보 차트를 자식으로 가진다. 표제와 하단 설명을 요소에 중복하지 않았다. 패널 구현 및 최종 조립 검수는 주 에이전트 담당이다.
- 07 서비스 카드와 12 프로그램 카드는 각각 4개의 실제 멤버에 맞춘 고유 source fixture를 갖는다. 제목 길이, 번호, 설명 유무 및 사진 슬롯을 보존하고 새 물류 업무 문구로 작성했다.
- 14페이지 인물 그룹이 3명을 함께 소유한다. 개별 인물 instance는 `contained_by`와 함께 출처 crop 추적용으로 유지하며 그룹의 `absorbed_instances`에도 기록했다.
- 지도에서 남은 `unexpressible`은 0개다. 원문은 출처 지도에만 남기고 fixture에는 새 한국어 비즈니스 데이터를 사용한다.

## 발견하여 수정한 결함

- 단독 인물 카드가 가로로 긴 칸에서 초상화까지 가로로 늘어나는 결함을 수정했다. source 377.333×401 비율의 내부 캔버스를 맞춰 넣어 모든 구성 요소가 같은 비율로 움직이도록 CSS를 새로 정리했다.
- native 인물 초상화는 158.469×244.984px, 12×6 넓은 칸에서는 167.953×259.656px로 측정되었다. 두 상태 모두 원비율 약 0.64685를 유지한다. native 이름·설명·직함은 각각 약26/18/14px이며 원본 좌표를 유지한다.
- 서비스·프로그램의 반복 fixture 참조를 고유 멤버별 참조로 교체했다. cycle·steps·timeline의 기계 설비 문구는 실제 배송·배차·회수 업무 문구로 정리했다.
- 콤보 차트 fixture의 비정량 연도는 2032~2035로 바꾸고 실제 수치와 간격은 유지했다. 지도 원문 데이터는 변경하지 않았다.

## 실제 확인과 한계

- 17개 디자인의 라이트·다크 시트 34장을 실제 이미지로 열어 확인했다. 서비스/프로그램 카드, 링 단계, 콤보, 도넛, 인물, 피라미드, 타임라인, 단계, 순환의 source 비교 crop도 확인했다. 원·링·초상화 비율, 점선·접힌 면, 연결선, 설명 줄바꿈과 칩 중앙을 검토했다.
- 최종 요소 fixture 45개, 양모드·규정 크기 상태 370개 모두 현재 소스 해시와 일치한다. quick=false, stale=false이며 overflow·textOverlap·hiddenNameFig·contrastFailures·paintOverflow·chipAlignmentFailures·fontErrors가 모두 0이다. 17개 contract ID도 `contract/leaves.json`과 일치한다.
- 최종 source6gram 검사: foundation fixture를 포함한 47개 파일, issues 0. 마지막 문구 수정 뒤 관련 시트와 감사 결과를 다시 생성했고 전체 해시를 재확인했다.
- 이 보고서는 요소 시트 및 source 크기 검증의 결과다. 최종 15페이지 조립본, foundation 패널, 격자 투영 결과, 배포 ZIP·push 성공은 이 보고서의 완료 주장에 포함하지 않는다. 사진은 사용자 규칙에 따라 회색 placeholder이며 시트 아이콘은 점선 슬롯이다.

검수 완료 후 halo-field 요소 및 지도는 동결한다.


### 주 에이전트 최종 통합 검수

07 카드 note의 폭을 replica 장식 원과 겹치지 않게 source 좌표에 맞추어 좁히고, 긴 fixture 문장을 자연스러운 한국어 1–2줄로 다시 썼습니다. 조립본의 네 아이콘은 전략/실행/발상/성과의 의미에 맞게 서로 다르게 복구했습니다. 12 사진 seat에 잘못 붙은 circle 아이콘 데이터 속성을 제거했습니다. 14 초상은 158.469×244.984 비율을 보존합니다. 04의 차트 전체 판과 표제는 foundation 패널입니다.

공통 판단: 원본 색을 팔레트 역할로 바꿨으므로 검증 페이지 색은 원본과 다릅니다. 사진·3D는 중성 placeholder입니다. 자유 좌표를 body의12×6 정수 격자로 옮긴 조립본은 원본/replica와 픽셀 단위로 같지 않습니다. 작은 칸에서의 가독성 검수는 각 fixture의 명시 min 이상 범위이며 min 미만을 보장하지 않습니다. 보존한 replica의 기존 문구·판독 판단은 바꾸지 않았고 새로 지어낸 fixture 문구만6자 중복 검사했습니다. 최종 주 에이전트 열람은435개 시트PNG와95개 삼단 비교PNG의 SHA-256에 연결되어 있습니다. GitHub 게시에는 git 명령 대신 연결 도구와 HTTP API만 사용합니다.

검수 ZIP에는 이 컬렉션 CSS에서 실제 참조하는 폰트 계열만 포함합니다. 제공된 전체32개 폰트 파일은 소스에서 그대로 보존하며, ZIP에 포함하는 폰트의 바이트도 바꾸지 않습니다. 원본32개 전체를 각 ZIP에 중복 포함했을 때 GitHub 파일 API 요청 크기를 넘었던 문제를 사용하지 않는 폰트 제외로 해결했습니다.


## 최종 통합 검수

실제 마지막 렌더와 검수한 시트/페이지 해시는 루트 primary-visual-review.json 및 각 audits에 기록합니다. 최종 성공 여부는 verification.json을 기준으로 확인합니다.
