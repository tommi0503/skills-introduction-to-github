# 계약으로 표현하지 못한 원본 구조

- 02 / normal background: 비표지 페이지에는 배경 장식 슬롯이 정의되어 있지 않다. 오른쪽으로 잘린 두 선택 프레임을 body 안에 끼워 넣거나 다른 역할 클래스로 위치 분기하지 않았다. 필요한 마크업은 일반 페이지의 명명된 배경 장식 슬롯이다.
- 04 / grouped bar chart: 연도마다 두 계열을 묶은 막대, 별도의 숫자 축과 값 주석 제어를 flat bar 계약으로 표현할 수 없다. 필요한 마크업은 category group 아래의 series bars, 독립 axis ticks와 annotation 제어다.
- 10 / multi-sector ring: one-share donut과 row of donuts는 여섯 독립 조각을 가진 하나의 원형 차트와 다르다. 필요한 마크업은 donut 아래의 이름과 수치를 가진 segment 목록이다.
- 11 / normal background: 비표지의 위쪽 오른쪽 프레임과 왼쪽 아래 프레임 역시 cover 전용 deco 밖의 구조다. 필요한 마크업은 일반 페이지의 명명된 배경 장식 슬롯이다.

- 06 / perimeter graph with independent core: 주변 네 원을 잇는 사각 트랙 안에 중앙 원이 독립적으로 놓인다. 중심→각 spoke의 방사 연결이 없으므로 hub.spokes로 표현할 수 없다. 필요한 마크업은 독립 core/node 목록과 외곽 node 사이 endpoint를 정하는 edge 목록이다. 원본에 없는 방사 선을 추가해 조립하지 않았다.

아래는 위 미표현 구조에 필요한 **계약 확장 제안**이며 현재 컬렉션이나 조립본에 쓰는 허용 클래스가 아니다.

02·11의 일반 페이지 배경 장식:
```html
<div class="page"><div class="background-deco" aria-hidden="true"></div><header class="head">…</header><div class="body">…</div></div>
```

04의 공유 범주를 가진 두 계열 막대:
```html
<div class="grouped-bars" style="--max:100"><div class="category"><span class="name">분기</span><div class="series" style="--v:38"><b>38</b></div><div class="series" style="--v:62"><b>62</b></div></div></div>
```

06의 독립 중심과 외곽 사각 연결:
```html
<div class="perimeter-graph"><div class="core">중심</div><div class="node" data-node="a">항목</div><div class="node" data-node="b">항목</div><div class="node" data-node="c">항목</div><div class="node" data-node="d">항목</div><div class="edge" data-from="a" data-to="b"></div><div class="edge" data-from="b" data-to="c"></div><div class="edge" data-from="c" data-to="d"></div><div class="edge" data-from="d" data-to="a"></div></div>
```

10의 여섯 세그먼트 원형:
```html
<div class="segmented-ring"><div class="segment" style="--v:20"><span class="name">사업 부문</span></div><!-- segment 6개; 합계100 --></div>
```
