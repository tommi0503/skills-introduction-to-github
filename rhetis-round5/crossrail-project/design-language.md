# Crossrail 디자인 언어 — Round5

가느다란 페이지 테두리와 상단 깊은 강조 띠가 큰 여백을 정리한다. 백색 면 위에는 명확한 이름/수치와 작은 보조 설명을 둔다. 직각 판, 열린 규칙선 카드, 문자 탭, 원형 순위, 길게 둥근 capsule은 서로 다른 실제 원형이므로 독립 디자인으로 고른다.

- 선: 기본1px, 주요 강조선2px, 원형 peer의 연한 rim6px. 연결과 노치는 멤버 전체를 가진 요소가 소유한다.
- 모서리: 판은 radius0, 날짜/수치 capsule은999px, peer/photo는 동일 지름50%. 원은 cqw/cqh 중 작은 지름을 양 축에 같이 사용한다.
- 간격: kit gap12/24/40 및pad32. 요소 내부는 실제 원형의 위치·폭·높이를100%의 비율로 변환한다. 작은 칸은 타입·간격 단계를 내리고 이름/수치는 유지한다.
- 타이포: Noto Sans KR, 굵은26px 이름,18px 본문,40px 수치,64px page title이 기준이다. 다른 실제 원형은14–76단계와 bounded clamp를 사용한다. 작은 Latin kicker는 별도 label tracking을 쓴다.
- 면과 선: 제목 띠/판/연속 column divider는 foundation panel이며, 내부 headline/prose/list/chart는 독립 계약이다. 페이지 강조면은 vector background다.
- 강조색 자리: page와ink가 바탕/기본 글자. 깊은 strip/chevron은a1-7, 순위별 두 번째/세 번째 면은a2-7/a3-7, 연한 판n1, 경계n3/n4, 보조 문자n7/n8. 채운 면의 글자는page 또는해당강조의on 자리. 공식 팔레트의 두 모드에서 대비를 검수한다.
- 차트: 수치를 길이·위치·sector에 연결한다. 별도 숫자 capsule과 설명은 해당 bar/slice의 소유 부품이다. 실제로 출처가 없는 참고 기둥을 공개 값으로 만들어 내지 않는다.

원본의 남색/슬레이트/회색은 외부 source-palette provider가 위 자리에 공급한다. 컬렉션 CSS는 어떤 색상인지 고정하지 않는다.
