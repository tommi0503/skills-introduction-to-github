# Unexpressible instances

## Page 03 — 한 모서리150px인 큰 강조면 안에 겹친 두 icon 원·제품 원·방향선·별도 설명

두 겹침 icon과 외부 제품 노드 및 하단 설명을 가진 비대칭 복합 패널은 cycle/venn 어느 계약의 core와도 의미가 맞지 않는다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="solution-composition"><div class="combination"><div class="input"></div><div class="input"></div></div><div class="output"></div><div class="summary"></div></div>
```

## Page 04 — 페이지 밖으로 이어지는 세 원호·원점·독립 수평선

어느 연결 요소에도 속하지 않는 자유 페이지 장식이다. 현재 foundation의 이름 붙은 변형으로 지정할 수 없다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="page-decoration" data-motif="mission-orbits"></div>
```

## Page 06 — 서로 겹친 세 둥근 산, 각각 이름·capsule·설명·큰 수치와 상단 점 세 개

pyramid는 위계3–5층이고 concentric은 포함관계다. 세 산의 겹침과 서로 다른 baseline의 숫자는 어느 계약의 마크업도 아니다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="market-overlap"><div class="market"><p class="name"></p><p class="segment"></p><p class="note"></p><p class="fig"></p></div></div>
```

## Page 07 — 독립 pill 옆에 이어지는339px rule

pill 계약은 한 줄 capsule이며 옆 요소와 연결되는 독립 rule을 소유할 수 없다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="caption-rule"><span class="label"></span><i class="rule"></i></div>
```

## Page 08 — 204px 전폭 gradient 띠에서 icon·왼쪽 큰 결론·오른쪽 작은 설명이 두 열로 나뉨

callout은 하나의 결론 문장이며 이 장면은 별도 제목과 설명을 두 열에 담는 복합 배너다. 임의 line 변형을 만들지 않는다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="split-banner"><div class="icon"></div><h2></h2><p></p></div>
```

## Page 09 — 136px 전폭 띠 안의 독립된 두 caption과 양끝 괘선

하나의 문장인 callout도,한 줄 capsule인 pill도 아니다. 두 caption을 가진 배너 계약이 필요하다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="paired-caption-banner"><p></p><p></p></div>
```

## Page 10 — 582×271 둥근 배경 panel

자식 흐름도를 품는 독립 배경 panel이다. card.parts의 텍스트 카드로 대신하지 않는다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="panel"><div class="content"></div></div>
```

## Page 11 — chart를 품는 둥근 gradient 배경 panel

텍스트 parts가 아닌 chart·legend의 독립 배경 컨테이너다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="panel"><div class="content"></div></div>
```

## Page 11 — chart를 품는 둥근 gradient 배경 panel

텍스트 parts가 아닌 chart·legend의 독립 배경 컨테이너다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="panel"><div class="content"></div></div>
```

## Page 11 — 30/55/15 세 지분과40% 구멍을 가진296px ring chart

chart-donut은 한 share만 가진다. 세 지분을 새 token으로 주입하지 않는다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="pie" data-hole="40"><div class="slice" style="--v:30"></div><div class="slice" style="--v:55"></div><div class="slice" style="--v:15"></div></div>
```

## Page 13 — 4점 area의0–60축은20씩3등분

base area의4등분과 다르며 계약에 tick count/step이 없다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="areas" style="--max:60" data-y-step="20"></div>
```

## Page 15 — pie·legend를 품는532×296 panel

chart와legend를 품는 패널은 현 계약에 없다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="panel"><div class="content"></div></div>
```

## Page 15 — 15/55/30 세 지분227px solid pie

단일 share인 chart-donut의 계약과 다르다. 구멍 없는 세 지분 pie 계약이 필요하다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="pie"><div class="slice" style="--v:15"></div><div class="slice" style="--v:55"></div><div class="slice" style="--v:30"></div></div>
```

## Page 15 — 위아래 점선 사이 두 capsule+근거 문장

list.check는 tick marker이고 이 디자인은 선택 근거를 가진 두 capsule 쌍이다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="reasons"><div class="reason"><span class="label"></span><p></p></div></div>
```

## Page 16 — 7노드·임의의중성/강조·두 L자분기와별도return이 있는 제어 flow

현재 to-r/to-d/to-l/to-u는 방향만 표현하고 edge 끝점·L자 경유점·node색 역할을 명시하지 않는다. 기본5-chevron와 다른 디자인의 semantic 변형도 없다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="controller-graph"><div class="node" id="vision"></div><i class="edge" data-from="vision" data-to="gripper" data-route="right-down"></i></div>
```

## Page 17 — caption 옆 독립 점선 rule

pill은 capsule만 소유하므로 외부 점선은 별도 caption-rule 계약이 필요하다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="caption-rule"><span class="label"></span><i class="rule"></i></div>
```

## Page 17 — 축 없이 gradient 막대4개·마지막 내부70%·큰곡선성장arrow·하단긴rule

base vertical bars와 다른 gradient/내부value/꾸밈성장arrow에 해당하는 의미 있는 계약 변형이 없다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="growth-bars"><div class="bar"></div><i class="growth-arrow"></i></div>
```

## Page 18 — phase3개×event3개=9열 milestone 표

timeline은 최대8 stop이며 phase headers를 소유하지 않는다. roadmap은기간이지이벤트의9열표가아니다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="phase-milestones"><div class="phase"><p class="name"></p><div class="event"><span class="icon"></span><p class="name"></p><p class="note"></p></div></div></div>
```

## Page 20 — 558×271 숫자 요소의둥근배경panel

metric은bare figure이고textcard로컨테이너를위장하지않는다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="panel"><div class="content"></div></div>
```

## Page 20 — 자금 사용 구획의독립위아래점선

다른 요소를 감싸는 구획 rule은 목록 계약에 없다.

Proposed markup (a future contract, not included in this collection):

```html
<div class="ruled-section"><div class="content"></div></div>
```
