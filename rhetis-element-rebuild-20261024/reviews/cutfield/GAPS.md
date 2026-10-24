# Unexpressible instances

## 01 · 01-foundation-7

bbox: `[59.64, 189.82, 705.88, 440.0]`

원본 대형 표제 217.81px

공유 타입의 최댓값은128이며 원본의 대형 표제를 같은 크기로 담을 수 없다. 타입 확장이나 SVG 텍스트로 계약을 우회하지 않는다.

Proposed markup (not a supported extension):

```html
<div class="lockup display-xl" data-contract-proposal="foundation.page@2"><h1 class="title">VISION<br>DECK</h1></div>
```

## 02 · 02-gap-1

bbox: `[45, 393, 1189, 282]`

1189×282 긴 사진 배너

정사각에 가까운 seat 규칙과 충돌하는 긴 배너를 square fixture로 위장하지 않는다.

Proposed markup (not a supported extension):

```html
<figure class="frame banner"><div class="seat" data-ph="1"></div></figure>
```

## 03 · 03-gap-4

bbox: `[42, 85, 548, 100]`

The first/third figure row has irregular source offsets: figure22/4px and metadata23/5px relative to the common middle band.

No content, member-count or named variant explains these source-only offsets. The common fig card preserves the measured middle-band geometry; page/ordinal selectors are forbidden.

Proposed markup (not a supported extension):

```html
<div class="card"><div class="parts" data-content-offset-y="23">...</div></div>
```

## 03 · 03-gap-1

bbox: `[612, 212, 28, 28]`

28px chamfer triangle reveals the next source band or deep page underlay.

The independently clipped card reveals its parent background. Source03 uses overlapping next-band/deep-page underlays, and card has no underlay-content slot or semantic next-sibling color rule.

Proposed markup (not a supported extension):

```html
<div class="group underlay tone-N"><div class="card">...</div></div>
```

## 03 · 03-gap-2

bbox: `[612, 452, 28, 28]`

28px chamfer triangle reveals the next source band or deep page underlay.

The independently clipped card reveals its parent background. Source03 uses overlapping next-band/deep-page underlays, and card has no underlay-content slot or semantic next-sibling color rule.

Proposed markup (not a supported extension):

```html
<div class="group underlay tone-N"><div class="card">...</div></div>
```

## 03 · 03-gap-5

bbox: `[42, 547, 548, 100]`

The first/third figure row has irregular source offsets: figure22/4px and metadata23/5px relative to the common middle band.

No content, member-count or named variant explains these source-only offsets. The common fig card preserves the measured middle-band geometry; page/ordinal selectors are forbidden.

Proposed markup (not a supported extension):

```html
<div class="card"><div class="parts" data-content-offset-y="5">...</div></div>
```

## 03 · 03-gap-3

bbox: `[612, 692, 28, 28]`

28px chamfer triangle reveals the next source band or deep page underlay.

The independently clipped card reveals its parent background. Source03 uses overlapping next-band/deep-page underlays, and card has no underlay-content slot or semantic next-sibling color rule.

Proposed markup (not a supported extension):

```html
<div class="group underlay tone-N"><div class="card">...</div></div>
```

## 04 · 04-foundation-38

bbox: `[545, 159, 689, 499]`

4개 시리즈를 가진 3개 묶음 막대: 43px 직각 막대, 막대 사이9px, 그룹마다 Human/Systemic/Opportunity Cost 공통 라벨, 각 막대 안쪽 위 흰값, 왼쪽0/5/10/15m 축, 위 네 키의 범례.

chart.bar@1은 bar마다 값과 label 하나만 정의한다. 여러 막대가 공유하는 그룹 라벨·시리즈 그룹·공통 범례를 정확히 담는 구조가 없다. 단순12막대 나열로 바꾸지 않는다.

Proposed markup (not a supported extension):

```html
<div class="grouped-bars" data-el="<collection>-chart-grouped-bar" style="--max:100"><div class="axis"></div><div class="groups"><div class="group"><span class="name">분류명</span><div class="bar tone-1" style="--v:20"><b>20</b></div><div class="bar tone-2" style="--v:30"><b>30</b></div></div></div><div class="series-keys"><span class="key tone-1">시리즈 A</span><span class="key tone-2">시리즈 B</span></div></div>
```

## 06 · 06-gap-1

bbox: `[795, 205, 389, 411]`

We Believe 제목과 화살표 리스트를 함께 감싸는 흰 우하단 사선 절단 패널

card.parts의 name/note 한 묶음이 아니라 독립 headline과 list를 담는 패널이다. 현재 foundation/요소에 범용 titled-panel slot이 없다.

Proposed markup (not a supported extension):

```html
<section class="panel"><header>...</header><div class="body">...</div></section>
```

## 07 · 07-foundation-64

bbox: `[0, 319, 1280, 401]`

크고 가는 From/To가 각 색면 위에 분리되어 놓이고, 두 640×360 전폭 면 안에 각 3개의 항목명/설명 쌍과 분리된 밑줄이 놓인다. 면마다 우상단45px 절단.

versus는 side.name+.list를 요구하지만 원본 비교에는 list marker가 없다. table09의 머리칸 채움과 달리 머리글이 면 밖에 있고 body 두 면 전체가 서로 다른 강조색이어서 table .pick만으로 표현할 수 있는 변형도 아니다.

Proposed markup (not a supported extension):

```html
<div class="versus" data-contract-proposal="versus.rich@2"><section class="side"><h3 class="name">From</h3><div class="body"><div class="item"><span class="label">Old way 1</span><p class="note">Manual, disconnected processes</p></div></div></section><section class="side on"><h3 class="name">To</h3><div class="body"><div class="item"><span class="label">Old way 1</span><p class="note">Automated, unified workflows</p></div></div></section></div>
```

## 09 · 09-foundation-82

bbox: `[658, 133, 551, 496]`

중앙 교차축과 서로 다른 채움의 경쟁사 원 3개/자사 원1개. 축에는 low/high 끝값 쌍이 아닌 Speed of Delivery와 Depth of Insight라는 축명 1개씩만 있다.

positioning의 axis-x/axis-y는 각각 low/high 두 라벨이며 축명 슬롯이 없다. 빈 endpoint를 유령으로 만들고 축명을 끼워넣지 않는다. 자사 logo+name 및 원 크기 차이도 후속 확장에 명시한다.

Proposed markup (not a supported extension):

```html
<div class="posmap" data-contract-proposal="positioning.named-axes@2"><div class="axis-x"><span class="label">Speed of Delivery</span></div><div class="axis-y"><span class="label">Depth of Insight</span></div><div class="mark" style="--x:19;--y:23"><span class="name">Competitor</span></div><div class="mark on" style="--x:78;--y:23"><div class="seat logo" data-ph="1"></div><span class="name">Miri Tech</span></div></div>
```

## 12 · 12-gap-3

bbox: `[839, 329, 398, 298]`

우하단28px cut-corner 독립 단계 카드. 순번 없이 약48px 이름이 위쪽, 아래17px 강조 note/설명. 높이는214/256/298px이나 연결선은 없다.

05 카드의17px 이름과 다른48px 단계명 위계다. .mark가 없는08 caption과도 달라, 계약에 없는 big 변형을 반응형으로 위장하지 않는다.

Proposed markup (not a supported extension):

```html
<div class="card big"><div class="parts"><p class="name">...</p><p class="note">...</p></div></div>
```

## 12 · 12-gap-2

bbox: `[441, 371, 398, 256]`

우하단28px cut-corner 독립 단계 카드. 순번 없이 약48px 이름이 위쪽, 아래17px 강조 note/설명. 높이는214/256/298px이나 연결선은 없다.

05 카드의17px 이름과 다른48px 단계명 위계다. .mark가 없는08 caption과도 달라, 계약에 없는 big 변형을 반응형으로 위장하지 않는다.

Proposed markup (not a supported extension):

```html
<div class="card big"><div class="parts"><p class="name">...</p><p class="note">...</p></div></div>
```

## 12 · 12-gap-1

bbox: `[43, 413, 398, 214]`

우하단28px cut-corner 독립 단계 카드. 순번 없이 약48px 이름이 위쪽, 아래17px 강조 note/설명. 높이는214/256/298px이나 연결선은 없다.

05 카드의17px 이름과 다른48px 단계명 위계다. .mark가 없는08 caption과도 달라, 계약에 없는 big 변형을 반응형으로 위장하지 않는다.

Proposed markup (not a supported extension):

```html
<div class="card big"><div class="parts"><p class="name">...</p><p class="note">...</p></div></div>
```
