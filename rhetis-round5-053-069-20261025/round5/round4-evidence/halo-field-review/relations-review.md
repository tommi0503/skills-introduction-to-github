# 관계 요소 검토 기록

원본에서 관찰한 구성은 실제 HTML 좌표와 글자 수치를 기준으로 신규 CSS로 작성했다. 기존 element CSS를 읽거나 복제하지 않았다. 비교 시트의 예문은 신규 한국어이며, 조립 지도에는 원문을 보존한다.

| 요소 | 페이지 | 판정 | 근거 |
|---|---|---|---|
| steps | slide_09 | base | Six contiguous right chevrons with labels alternating above and below the band; gray progression and final accent member. All leader stems/points and chevron joints belong to the same six-member sequence. |
| steps | slide_11 | unexpressible | Second horizontal steps design, not .col. Switching between ring stages and chevrons by5vs6 count would smuggle in another design. |
| timeline | slide_10 | base | Four quarter capsules on a long horizontal baseline with arrow at right; each quarter owns title and multiple notes beneath. |
| cycle | slide_06 | base | Three160px white value discs on a thin circular motion path, subtle accent arrowheads, paired Korean/English labels; central core is visibly empty. |
| pyramid | slide_08 | base | Four detached, offset gray trapezoid tiers forming a stepped pyramid; dotted horizontal leaders with point markers connect each tier to accent capsules and right explanations. |
| image-frame | slide_06 | base | Single quiet rounded rectangle675.66×375 agency/team photo placeholder, radius matching the source frame. |

미관찰 요소는 덱별 기단/캡슐/궤도/헤더판/접힌 면/잘린 모서리/편집 핸들의 형태 규칙으로 새로 설계했다. 계약에 의미상 대응하지 않거나 이미 채택한 base와 전혀 다른 디자인은 임의 변형 클래스를 만들지 않고 위 표에 표현 불가로 기록했다.

사진·기기 화면은 회색 seat placeholder다. 단순 아이콘은 실제 Lucide data-icon 슬롯을 유지한다.

## 최종 검수 결정

- source 비교 시트는 관찰 31개 leaf를 개별 열어 확인했다. source HTML은 동결했고 원문 조립 markup을 줄이지 않았다.
- root 자신의 간격은 %로, 자식·연결선·타이포는 root의 cqw/cqh로 계산한다. source member 전체가 선과 화살표를 소유한다.
- min은 fixture 첫 줄에 하나만 선언한다. 중첩 list에는 실제 남는 높이를 배정했고 pill/tag 및 독립 chip은 잉크 중심을 검수했다.
- 아이콘 슬롯은 공식 시트에서 점선 원, 조립본에서 Lucide로 렌더한다. 단순 아이콘은 빈 data-icon 계약 markup을 유지한다.
- timeline의 왼쪽 원이 기존 field 밖 8px에 있어 실제 시각 bbox[46,245,1180,425]를 사용한다. pyramid의 34px 접힘 면, 원형 연결점·점선과 cycle의 세 화살표를 복원했다.

신규 fixture는 원본 시간 간격을 보존해 2032년부터 계획을 시작하며, 원문 br·bullet·강조와 글줄의 시각 길이를 맞춘 별도 한국어 사례다. 원문은 조립 map에서 보존한다.

halo10 원문 상태 추가 검수: 항목 padding15px, 행간26.1px, 항목 간18px·마지막0px, source의 nowrap + 수동 br를 복원했다. source와 조립본의 세 항목은 모두 x81/w234.5/h52.1875, y475/545.1875/615.375로 일치하고 note bottom667.5625다. 단일 페이지 원문 검사 outside0/overlap0/paint0 및 정식 시트8상태0flag 확인.
