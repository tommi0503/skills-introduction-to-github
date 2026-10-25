# 관계 요소 검토 기록

원본에서 관찰한 구성은 실제 HTML 좌표와 글자 수치를 기준으로 신규 CSS로 작성했다. 기존 element CSS를 읽거나 복제하지 않았다. 비교 시트의 예문은 신규 한국어이며, 조립 지도에는 원문을 보존한다.

| 요소 | 페이지 | 판정 | 근거 |
|---|---|---|---|
| steps | slide-17 | base | Four staircase columns with49px tinted headers,32px numbered circles and gray downward continuation lines; main sequence only. The separate period ribbon below is not silently encoded in CSS. |
| steps | slide-17 | unexpressible | No global/subgroup label parts in steps.sequence. These strings cannot become ::before/::after CSS content or be assigned to arbitrary step notes. Requires a real contract resolution before Phase2 assembly. |
| timeline | slide-07 | base | Four quarter chevron bars49px high above69px quiet notes, with one thin vertical point-to-note line per quarter; the full four-member strip is one timeline. |
| cycle | slide-03 | base | Three85px accent circles on a302px pale disk,124px white center. Fine downward center line ends above caption. Caption is outside the diagram and belongs to prose/headline. |
| cycle | slide-16 | unexpressible | This changes three-disc plain circular backing to a clover system with outside notes. cycle has no root variant for a second visual design, and the external prose cannot become hidden page-specific selectors. |
| hub | slide-05 | base | Four P/E/S/T petal circles surround a central white PEST disc; each member owns its quadrant pale note panel. Not a Cartesian matrix and not SWOT. |
| hierarchy | slide-06 | base | Horizontal mirrored two-branch hierarchy: central performance root, one intermediate pale category each side, two outer gray leaves per category. Own all braces, link segments and endpoints as one instance. |
| architecture | slide-06 | base | One990×125 accent band split into3 layer columns, each with136×35 white floating name capsule and three white chips. Dotted internal separators are part of this architecture. |
| versus | slide-14 | base | Two before/after202px panels with49px title strip, two82px icon boxes per side and bidirectional work connectors; gray before, accent-on after. Root owns all within-side link arrows and center division. |
| image-frame | slide-11 | base | Gray6px rounded device frame,196×390, radius28px and neutral screen placeholder. |
| image-frame | slide-11 | unexpressible | Second phone changes border from neutral to accent but frame.picture has no .on variant. A data-ph number must not act as a style switch. |
| image-frame | slide-18 | unexpressible | Distinct wide photo treatment from the phone frame base, with no frame root variant; also violates near-square placement guidance if treated as a standalone frame. |
| image-frame | slide-18 | unexpressible | Distinct wide photo treatment from the phone frame base, with no frame root variant; also violates near-square placement guidance if treated as a standalone frame. |

미관찰 요소는 덱별 기단/캡슐/궤도/헤더판/접힌 면/잘린 모서리/편집 핸들의 형태 규칙으로 새로 설계했다. 계약에 의미상 대응하지 않거나 이미 채택한 base와 전혀 다른 디자인은 임의 변형 클래스를 만들지 않고 위 표에 표현 불가로 기록했다.

사진·기기 화면은 회색 seat placeholder다. 단순 아이콘은 실제 Lucide data-icon 슬롯을 유지한다.

## 최종 검수 결정

- source 비교 시트는 관찰 31개 leaf를 개별 열어 확인했다. source HTML은 동결했고 원문 조립 markup을 줄이지 않았다.
- root 자신의 간격은 %로, 자식·연결선·타이포는 root의 cqw/cqh로 계산한다. source member 전체가 선과 화살표를 소유한다.
- min은 fixture 첫 줄에 하나만 선언한다. 중첩 list에는 실제 남는 높이를 배정했고 pill/tag 및 독립 chip은 잉크 중심을 검수했다.
- 아이콘 슬롯은 공식 시트에서 점선 원, 조립본에서 Lucide로 렌더한다. 단순 아이콘은 빈 data-icon 계약 markup을 유지한다.

신규 fixture는 원본 시간 간격을 보존해 2032년부터 계획을 시작하며, 원문 br·bullet·강조와 글줄의 시각 길이를 맞춘 별도 한국어 사례다. 원문은 조립 map에서 보존한다.
