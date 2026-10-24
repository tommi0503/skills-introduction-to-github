# 074 지원 검수 — Vectorbox 14요소

검수 범위는 위임받은 14요소 폴더뿐이다. kit, foundation, 원본, replica, map, 조립 페이지와 다른 42요소는 수정하지 않았다. 전체 writer를 재실행하지 않았으며, 기존 v2 새 CSS를 요소 안에서 교정했다.

최종 46 fixtures × 양 모드, 566개의 native grid 칸을 렌더했다. 각 fixture의 최소 칸부터 제공된 모든 크기까지 밝은/어두운 화면을 직접 확인했다. 전체 요소별 대형 시트만 보지 않고 fixture별 native 칸 묶음으로 검수했다. rendererVersion은 `v2-grid-paint-font-parts-1`이다.

## 교정과 판단

- chart-stack: 세그먼트와 관계없던 숫자 행을 실제 각 세그먼트의 중심에 결합했다. 세로는 오른쪽 숫자 공간, 가로는 아래 숫자 공간을 확보했다. 좁은 12개 막대의 끝 숫자가 넘치지 않도록 수평 가용 폭도 글자 크기에 반영했다. 실제 합100인 세로/가로 pct fixtures를 추가했다.
- bullet: 복수 `.bullets`에만 있던 기본 CSS를 단독 `.bullet`에도 같은 literal root로 적용했다. fixture의 104는 계약0–100에 맞게94 및94%로 고쳤다. 좁은 행에서는 보조 note를 숨기고 이름·수치·목표선은 유지했다.
- heatmap: calendar의 가로·세로 가용 크기로 동일한 정사각 변을 산출했다. 표준 모드 머리글과 이름 gutter도 정렬했다. 반복 톱니 예시값은 완만한 주간/요일 업무량으로 교체했다. 숫자는0–100이다.
- treemap: 8% 작은 tile에서 제목/숫자가 겹치던 고정 세로 배치를 이름·수치 grid로 바꿨다. 세로로 긴 tile은 자체 orientation query로 세로 배치한다. branch 머리글을 실제 흐름에 포함했다. 실제 최소는 단일branch6x4, 4branch8x4이다. branch와 tile이 포함 관계를 갖는 신규 업무명으로 교체했다.
- sparkline: 선점에서 상속된 align-self:start 때문에 미니 막대가 위에 매달리던 오류를 bottom baseline으로 고쳤다. 5점 `.up` fixture는 실제 작은3x1칸도 검수했다. 기존24점 선과8개 `.down.bars`도 전 크기 검수했다.
- scatter: 정확히 축 중간값일 때 sign(0) 때문에 글자가 점 중심에 겹치던 것을 위쪽 배치로 결정했다. bubble은 양 치수의 작은 쪽을 사용해 원을 유지했다.
- chart-line: `.on` 점의 halo를 명확히 했다. 수평44→44 구간까지 선이 이어짐을 직접 확인했다.
- chart-area/radar: 순위별 실제 면과 대응하는 색 키를 범례 이름에 추가했다. stacked area의 누적합 입력은 그대로 보존했다. explicit tone은 ordinal보다 우선한다. radar 업무명은 비교 가능한 역량 축으로 고쳤고 수치는 유지했다.
- concentric: 서로 무관한 업무 대신 실제 포함 관계인 전체→국내→목표 시장, 검토 대상→연간 계약 고객사로 신규 예시 의미를 바로잡았다. 값은 유지했다.
- waffle: square unit과20명 person pictogram을 모두 직접 확인했다. `.figures` fixture를 추가해 on10/secondary5/quiet5개의 실제 개수를 유지했다.
- chart-bar, waterfall, slope: 각각 실제 크기·모드에서 값/라벨/연결선을 확인했다. waterfall의 시작·종료 total과 중간 증감은 숫자와 일치했다. dumbbell의6→9 근접한 두 원은 겹쳐도 숫자는 각각 판독되며 자동 텍스트 겹침은0이다.
- 14 descriptions를 요소별 실제 형태·정보 위계·변형을 설명하는 영어 문단으로 교체했다.

## 최종 검사

요소별 잘림, 문자 영역 초과, 텍스트 겹침, nested component 초과, icon/seat/mark 초과, 실제 페인트 대비 후보는 모두0이다. 글꼴은 선언되고 로드되었다. 각 checks의 sourceFingerprint는 현재 소스와 일치한다. 읽기 전용 source audit도 현재56요소 전체 errors0/warnings0/원본6문구0이었다. 계약 통합 감사는 errors0/pending0이다. 보조 슬롯 누락 후보와 원본 golden의 알려진 예외는 확정 오류로 바꾸지 않았다. 내 지원 범위 golden14개(bar6,line4,area4)의 구조·숫자 데이터는 보존했다.

| 요소 | fixture 수 | 양모드 native 칸 | 최종 sourceFingerprint |
|---|---:|---:|---|
| chart-bar | 8 | 84 | `965bdba1d60a5e6a1b80ee4e81c2adb2a8869928b82f66f07a7356ac88bd9f50` |
| chart-line | 6 | 82 | `9a29541826d64ba14fec468961721f7ffe782a32de1241f981d17c5791a4cbfb` |
| chart-area | 6 | 86 | `7cbb1916b609a075090bf83e26cf44de78068d7c30883f579fbe88fee06d84c9` |
| chart-stack | 4 | 44 | `debc963037b92a9a08e947f843d9da3a1e5ec139f15dca76f803ecb89c59eb12` |
| chart-waterfall | 2 | 24 | `fdf8d3bc33982d5c1e7bfae6a2987d20e28cd74e05ee80174746e72275fc61f2` |
| chart-scatter | 2 | 24 | `afd96752fc23088d47488b11f4decc8dceed5907b1e296586669b4a1c3c574f2` |
| sparkline | 3 | 44 | `10a21d122a2d4028e7d7f42d6b0f91dd695771aa53b69f21254f279b596fb9b7` |
| heatmap | 2 | 24 | `49c46aac37a92adeaf0483b4f07533d8c2ba35a53becccb51db20bb4a8e5a656` |
| waffle | 3 | 40 | `9f9e862bd0899dafd17861b64c14737f827aee2fc4abbad7540b1ea9a8f85a1f` |
| treemap | 2 | 18 | `eca4b2c27c4d3eab41221313e587d9278431d938123918d4fa541d1dea55f1d8` |
| bullet | 2 | 24 | `d9cb13f95be8b6a8496ae7c28a15a7245b84ab7645f6dbb1bc8fb53e7f950b0d` |
| slope | 2 | 24 | `9d9597376d3ce8a3c588a2a56c09e9c912e276510d5481215886e9f09510d5e3` |
| radar | 2 | 24 | `f6557d3998d36fc2250764ac86775f7c2b100bee8ad352ca4710f9a1451ebebb` |
| concentric | 2 | 24 | `dc6b437f15205b125538a739c1cb825247d1e6f175ec4f5fdb55bcdf4ad493db` |
