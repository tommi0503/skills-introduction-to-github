# Crossrail 디자인 언어

이 문서는 073 덱의 30장과 불변 replica를 읽고 만든 v2 설계 기록이다. 이전 컬렉션의 CSS는 읽거나 재사용하지 않았다. 원본의 실제 DOM 측정은 `source-measurements.json`, 모든 시각 노드의 소유권과 1280×720 좌표는 `map.json`에 있다.

| 문법 | 원본 관찰 | 새 컬렉션의 역할 |
|---|---|---|
| 구조선 | 페이지 가장자리의 가는 수직선과 수평선이 교차한다. | 기본 선은 1px `--n-3` / `--n-4`, 중요한 시작선은 2px `--a1-7` |
| 모서리 | 큰 설명 면은 직각, 칩과 단계 캡션은 알약, 사진과 주요 아이콘은 원형이다. | 직각 surface를 기본으로 하고 의미가 있는 capsule/circle에만 999px/50% 사용 |
| 형태 | 연결 chevron, 계단처럼 분리된 단계, 넓은 흰 판, 얇은 분할선 | steps 한 root가 연결 화살표 전부 소유. 카드 형제 조건으로 연결선을 만들지 않음 |
| 여백 | 일반 페이지 x≈95, body y≈260. 패널 안에서는 여백·선·본문이 분리됨 | foundation x95, body y263. 요소 내부는 받은 상자 비율로 계산하며 공유 gap 12/24/40과 pad32 사용 |
| 제목 | 큰 제목의 좁은 자간, 단단한 굵기, 작은 영문 kicker | Noto Sans KR, title64 / body heading26 / note18을 기본 축으로 사용 |
| 수치 | 수치와 단위가 명확히 분리되고 일부 값만 capsule로 강조됨 | fig는 독립 위계. 단위는 small. metric의 capsule, 선택 막대의 값 badge에 한정 |
| 채움 | 큰 accent field 위의 밝은 정보판, 중립 설명 면, 마지막 단계의 강한 면 | 페이지 강조 `--a1-7`, 정보판 `--page`, 조용한 면 `--n-1`, 중간 계열 `--a2-7` |
| 강조 | 면 한 곳 또는 한 수치만 강하게, 나머지는 가는 선으로 구분 | on은 accent / on-color 짝. 본문은 `--n-7`, 중요한 이름은 `--ink` |
| 도해 | 아이콘 원, 반원 호, 수평·수직 연결, 단순한 채움 | 새 추론 요소에도 같은 선·원·직각 면을 적용. 사진·이미지 아이콘은 회색 seat |

디자인 CSS에는 색 리터럴이 없다. kit의 page/ink 미리보기 값만 예외다. 라이브러리 시트는 공식 light/dark palette를 사용한다. 조립본의 `assets/source-palette.css`는 원본 색을 역할에 공급하는 외부 style이며, 요소별 좌표·폰트·기하 보정은 들어 있지 않다.

각 요소 root는 size container다. 내부 자식의 cqw/cqh는 그 root를 기준으로 한다. 멤버 수는 자기 자식의 개수로 추론하며, 페이지 번호·fixture 파일명·특정 수치·다른 요소의 존재를 분기 조건으로 쓰지 않았다. 작은 상자에서 글자 단계와 간격을 낮추고, fig/name은 유지한다. 실제 읽힘에 필요한 최소 칸은 fixture 첫 줄에 개별 선언했다.

원본에 없는 요소는 같은 언어를 확장했다. flowchart/decision-tree/mindmap은 실제 연결이 이어지는 얇은 규칙선, balance는 수치 부호에 맞는 기울기, concentric은 원형 띠 안에 독립적으로 읽히는 레이블, sankey는 비중에 비례하는 대역으로 설계했다. 선/면 차트는 공개 point 값에서 CSS anchor와 양수 높이의 clip 수식으로 그리며, 임의의 prev/next 데이터를 추가하지 않았다.


## 의미 계약 후속 정리

원본 반원 트랙은 hub의 방사 연결과 구별한다. 라이브러리 hub는 중앙 core와 각 spoke를 가는 직선으로 연결하고 원본 반원 도해는 계약 gap이다. metric의 숫자는 면과 테두리 없이 드러낸다. 원본의 숫자 capsule 장식은 독립 outline 계약이 없으므로 gap으로 남긴다. comparison의 관계 표시는 원본의 단순한 오른쪽 화살표 문법을 사용하되 각 요소의 실제 root 안에 둔다. Venn의 중심 간격은 원 지름에서 계산하며 K축 레이더의 방사선도 데이터와 같은 각도에서 시작한다.


최종 원형 검수 보강: tag는최소42pxfilledcircle/긴문구capsule, legend의범례칸은square marker, dividedlist는dot없는굵은name과가는가로선, pyramid는9pxwhitegap으로분리한단계다. funnel의두텍스트필드는한capsule안에두며마지막단계는filled pill이다. headline.on은채움만을뜻하고.center는독립된명시적정렬이다. 마감페이지는기존head.at-bottom-left/rail.on의큰아래제목과위kicker를결합한다.
