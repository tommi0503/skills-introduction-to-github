# Unexpressible instances

## 01 · 01-foundation-3

bbox: `[0, 206, 1280, 514]`

기울어진 여러 페이지 미리보기 몽타주

복수 페이지를 담고 원근/회전을 적용한 장면 장치다. 요소 계약이나 foundation의 단일 seat로 동일한 편집 구조를 담지 못한다.

Proposed markup (not a supported extension):

```html
<div class="page-montage" data-contract-proposal="foundation.page@2"><div class="page-preview"></div><div class="page-preview"></div></div>
```

## 03 · 03-foundation-15

bbox: `[132, 34, 1148, 86.890625]`

79px/700 Oswald 장치 제목의 정확한 글꼴 윤곽

원본 실제CDP는 Oswald-Bold를 사용하지만 README 허용글꼴표에는 Oswald가 없다. 컬렉션은 허용 Noto Sans의 native wdth75%/700을 사용하며 정확한 Oswald 글리프 높이·윤곽까지 동일하다고 주장하지 않는다. font alias나 transform으로 우회하지 않는다.

Proposed markup (not a supported extension):

```html
<h1 class="title" data-contract-proposal="foundation.allowed-fonts@2" data-font-family="Oswald" data-font-weight="700">BRAND STRATEGY</h1>
```

## 03 · 03-list-3

bbox: `[884, 286, 330, 301]`

330×301px회색면의bullet목록.20px/350·29px행간,왼쪽30px+marker32px,상단22–31px,멤버사이29–37px. 원본의한항목과5행본문은분리하지않는다.

회색 면 안의 단일 bullet 항목은 list.items@1의 최소2개를 충족하지 않는다. 줄바꿈5개를 여러 항목으로 분리하거나 항목을 추가해 원본을 변조하지 않는다.

Proposed markup (not a supported extension):

```html
<div class="list" data-contract-proposal="list.items@2"><div class="item"><p class="name">브랜드의 존재 이유와<br>브랜드가 현재와 미래<br>타겟하는 고객과 갖는<br>주요 접점과 직접적으로<br>관련되는 구체적인 방법론</p></div></div>
```

## 04 · 04-foundation-27

bbox: `[132, 34, 1148, 86.890625]`

79px/700 Oswald 장치 제목의 정확한 글꼴 윤곽

원본 실제CDP는 Oswald-Bold를 사용하지만 README 허용글꼴표에는 Oswald가 없다. 컬렉션은 허용 Noto Sans의 native wdth75%/700을 사용하며 정확한 Oswald 글리프 높이·윤곽까지 동일하다고 주장하지 않는다. font alias나 transform으로 우회하지 않는다.

Proposed markup (not a supported extension):

```html
<h1 class="title" data-contract-proposal="foundation.allowed-fonts@2" data-font-family="Oswald" data-font-weight="700">WHO</h1>
```

## 05 · 05-foundation-35

bbox: `[132, 34, 1148, 86.890625]`

79px/700 Oswald 장치 제목의 정확한 글꼴 윤곽

원본 실제CDP는 Oswald-Bold를 사용하지만 README 허용글꼴표에는 Oswald가 없다. 컬렉션은 허용 Noto Sans의 native wdth75%/700을 사용하며 정확한 Oswald 글리프 높이·윤곽까지 동일하다고 주장하지 않는다. font alias나 transform으로 우회하지 않는다.

Proposed markup (not a supported extension):

```html
<h1 class="title" data-contract-proposal="foundation.allowed-fonts@2" data-font-family="Oswald" data-font-weight="700">WHY</h1>
```

## 05 · 05-gap-1

bbox: `[174, 260, 981, 301]`

회색233px판과주황301px판의질문/전구말풍선아이콘+굵기다른2행주장,사이114×71px분절화살표

delta.from/to에는아이콘말풍선이나각side의세부구조가없고,versus에는단일주장쌍을담는계약이없다. card두개에형제순서화살표를붙이는방식은금지되어새change-panel구조가필요하다.

Proposed markup (not a supported extension):

```html
<div class="change-panels"><div class="from"><span class="icon"></span><p>...</p></div><div class="to"><span class="icon"></span><p>...</p></div></div>
```

## 06 · 06-gap-1

bbox: `[494, 62, 700, 571]`

사진+번호캡슐+산문3개행을담고행사이를가르는media-list wrapper

같은row에독립frame/pill/prose가있는owner가없다. list의mark는사진slot이아니며,별도카드의뒤에rule를붙이는형제조건으로위장하지않는다.

Proposed markup (not a supported extension):

```html
<div class="media-list divided"><div class="item"><div class="seat"></div><div class="body">...</div></div></div>
```

## 06 · 06-foundation-46

bbox: `[127, 180, 251, 90]`

79px/700 Oswald 장치 제목의 정확한 글꼴 윤곽

원본 실제CDP는 Oswald-Bold를 사용하지만 README 허용글꼴표에는 Oswald가 없다. 컬렉션은 허용 Noto Sans의 native wdth75%/700을 사용하며 정확한 Oswald 글리프 높이·윤곽까지 동일하다고 주장하지 않는다. font alias나 transform으로 우회하지 않는다.

Proposed markup (not a supported extension):

```html
<h1 class="title" data-contract-proposal="foundation.allowed-fonts@2" data-font-family="Oswald" data-font-weight="700">HOW</h1>
```

## 07 · 07-foundation-58

bbox: `[132, 34, 1148, 86.890625]`

79px/700 Oswald 장치 제목의 정확한 글꼴 윤곽

원본 실제CDP는 Oswald-Bold를 사용하지만 README 허용글꼴표에는 Oswald가 없다. 컬렉션은 허용 Noto Sans의 native wdth75%/700을 사용하며 정확한 Oswald 글리프 높이·윤곽까지 동일하다고 주장하지 않는다. font alias나 transform으로 우회하지 않는다.

Proposed markup (not a supported extension):

```html
<h1 class="title" data-contract-proposal="foundation.allowed-fonts@2" data-font-family="Oswald" data-font-weight="700">BRAND STRATEGY GRID</h1>
```

## 07 · 07-foundation-59

bbox: `[139, 239, 1060, 346]`

Input3개 독립박스 / Brand Development의2개 하위열(2행/5행) / Outputs2개 독립박스를 서로 다른 행수와 여백으로 함께 놓은 다단 프레임워크. 각 상단은다른 촉/gradient 제목 띠.

단일 table의 공유 행/열 격자도 아니며 일반 matrix9칸/architecture stacked layers로 의미를 바꿀 수도 없다. 서로 다른 표·제목 패널을 묶는 프레임워크 계약이 필요하다.

Proposed markup (not a supported extension):

```html
<div class="framework" data-contract-proposal="framework.columns@1"><section class="column input"><h3>Input</h3><div class="items"><p>미션</p><p>비전</p><p>핵심가치</p></div></section><section class="column"><h3>Brand Development</h3><div class="columns"><section><h4>Fundametal</h4><p>핵심고객</p><p>Key Success Factor</p></section><section><h4>Components</h4><p>기능 및 속성</p><p>기능적 강점</p><p>정서적 강점</p><p>브랜드 약속</p><p>포지셔닝</p></section></div></section><section class="column output"><h3>Outputs</h3><p>브랜드 퍼스널리티</p><p>핵심 메시지</p></section></div>
```

## 08 · 08-foundation-65

bbox: `[132, 34, 1148, 86.890625]`

79px/700 Oswald 장치 제목의 정확한 글꼴 윤곽

원본 실제CDP는 Oswald-Bold를 사용하지만 README 허용글꼴표에는 Oswald가 없다. 컬렉션은 허용 Noto Sans의 native wdth75%/700을 사용하며 정확한 Oswald 글리프 높이·윤곽까지 동일하다고 주장하지 않는다. font alias나 transform으로 우회하지 않는다.

Proposed markup (not a supported extension):

```html
<h1 class="title" data-contract-proposal="foundation.allowed-fonts@2" data-font-family="Oswald" data-font-weight="700">BRAND STRATEGY GRID</h1>
```

## 08 · 08-foundation-66

bbox: `[139, 243, 1060, 46]`

1060×46 가로 제목 띠. 왼쪽은 밝게 사라지고 오른쪽 촉이 있는 Input이며 바로 아래 표를 묶는다.

다른 요소의 제목 패널이며 table thead는 실제 표의 subsection header에 사용된다. pill/tag/headline은 이런 타 요소를 담는 제목 패널 계약이 아니다. 세 방향/gradient 처리도 기존 계약 변형이 없다.

Proposed markup (not a supported extension):

```html
<section class="panel" data-contract-proposal="panel.header@1"><header class="head input">Input</header><div class="body"><div class="tablebox" data-el="toggle-grid-table">…표…</div></div></section>
```

## 09 · 09-foundation-73

bbox: `[132, 34, 1148, 86.890625]`

79px/700 Oswald 장치 제목의 정확한 글꼴 윤곽

원본 실제CDP는 Oswald-Bold를 사용하지만 README 허용글꼴표에는 Oswald가 없다. 컬렉션은 허용 Noto Sans의 native wdth75%/700을 사용하며 정확한 Oswald 글리프 높이·윤곽까지 동일하다고 주장하지 않는다. font alias나 transform으로 우회하지 않는다.

Proposed markup (not a supported extension):

```html
<h1 class="title" data-contract-proposal="foundation.allowed-fonts@2" data-font-family="Oswald" data-font-weight="700">BRAND STRATEGY GRID</h1>
```

## 09 · 09-foundation-74

bbox: `[139, 243, 1060, 46]`

1060×46 가로 제목 띠. 양쪽 촉이 있는 검정 Brand Development이며 바로 아래 표를 묶는다.

다른 요소의 제목 패널이며 table thead는 실제 표의 subsection header에 사용된다. pill/tag/headline은 이런 타 요소를 담는 제목 패널 계약이 아니다. 세 방향/gradient 처리도 기존 계약 변형이 없다.

Proposed markup (not a supported extension):

```html
<section class="panel" data-contract-proposal="panel.header@1"><header class="head both-ends">Brand Development</header><div class="body"><div class="tablebox" data-el="toggle-grid-table">…표…</div></div></section>
```

## 10 · 10-foundation-81

bbox: `[132, 34, 1148, 86.890625]`

79px/700 Oswald 장치 제목의 정확한 글꼴 윤곽

원본 실제CDP는 Oswald-Bold를 사용하지만 README 허용글꼴표에는 Oswald가 없다. 컬렉션은 허용 Noto Sans의 native wdth75%/700을 사용하며 정확한 Oswald 글리프 높이·윤곽까지 동일하다고 주장하지 않는다. font alias나 transform으로 우회하지 않는다.

Proposed markup (not a supported extension):

```html
<h1 class="title" data-contract-proposal="foundation.allowed-fonts@2" data-font-family="Oswald" data-font-weight="700">BRAND STRATEGY GRID</h1>
```

## 10 · 10-foundation-82

bbox: `[139, 243, 1060, 46]`

1060×46 가로 제목 띠. 양쪽 촉이 있는 검정 Brand Development이며 바로 아래 표를 묶는다.

다른 요소의 제목 패널이며 table thead는 실제 표의 subsection header에 사용된다. pill/tag/headline은 이런 타 요소를 담는 제목 패널 계약이 아니다. 세 방향/gradient 처리도 기존 계약 변형이 없다.

Proposed markup (not a supported extension):

```html
<section class="panel" data-contract-proposal="panel.header@1"><header class="head both-ends">Brand Development</header><div class="body"><div class="tablebox" data-el="toggle-grid-table">…표…</div></div></section>
```

## 10 · 10-foundation-83

bbox: `[139, 308, 1060, 277]`

같은 subsection/label/note 계열이지만 source Components 표는 label29.15%, note왼쪽86px, 옅은 별도 body면, 본문5행46px인 조밀한 두 번째 테이블 디자인.

행수에 따른 높이 반응은 가능하지만 label25%→29.15%/note66→86px/새 body면을 특정5행일 때만 바꾸면 fixture 디자인 특례다. table에는 이를 명시하는 compact variant가 없다.

Proposed markup (not a supported extension):

```html
<div class="tablebox compact" data-contract-proposal="table.grid@2"><table class="table"><thead><tr><th colspan="2">Components</th></tr></thead><tbody><tr><th>기능 및 속성</th><td>브랜드의 기능적인 특징, 강점, 차별점 등</td></tr><tr><th>기능적 이점</th><td>브랜드가 제공하는 기능으로 고객이 수행할 수 있는 것</td></tr><tr><th>정서적 이점</th><td>브랜드가 제공하는 기능으로 고객이 만족할 수 있는 것</td></tr><tr><th>브랜드 약속</th><td>브랜드가 어떤 일이 있어도 고객과 지키고자 하는 것</td></tr><tr><th>포지셔닝</th><td>우리 브랜드를 사람들이 어떻게 인식하길 원하는가?</td></tr></tbody></table></div>
```

## 11 · 11-foundation-89

bbox: `[132, 34, 1148, 86.890625]`

79px/700 Oswald 장치 제목의 정확한 글꼴 윤곽

원본 실제CDP는 Oswald-Bold를 사용하지만 README 허용글꼴표에는 Oswald가 없다. 컬렉션은 허용 Noto Sans의 native wdth75%/700을 사용하며 정확한 Oswald 글리프 높이·윤곽까지 동일하다고 주장하지 않는다. font alias나 transform으로 우회하지 않는다.

Proposed markup (not a supported extension):

```html
<h1 class="title" data-contract-proposal="foundation.allowed-fonts@2" data-font-family="Oswald" data-font-weight="700">BRAND STRATEGY GRID</h1>
```

## 11 · 11-foundation-90

bbox: `[139, 243, 1060, 46]`

1060×46 가로 제목 띠. 왼쪽 촉이 있고 오른쪽은 밝게 사라지는 Outputs이며 바로 아래 표를 묶는다.

다른 요소의 제목 패널이며 table thead는 실제 표의 subsection header에 사용된다. pill/tag/headline은 이런 타 요소를 담는 제목 패널 계약이 아니다. 세 방향/gradient 처리도 기존 계약 변형이 없다.

Proposed markup (not a supported extension):

```html
<section class="panel" data-contract-proposal="panel.header@1"><header class="head output">Outputs</header><div class="body"><div class="tablebox" data-el="toggle-grid-table">…표…</div></div></section>
```

## 12 · 12-foundation-99

bbox: `[127, 180, 251, 180]`

79px/700 Oswald 장치 제목의 정확한 글꼴 윤곽

원본 실제CDP는 Oswald-Bold를 사용하지만 README 허용글꼴표에는 Oswald가 없다. 컬렉션은 허용 Noto Sans의 native wdth75%/700을 사용하며 정확한 Oswald 글리프 높이·윤곽까지 동일하다고 주장하지 않는다. font alias나 transform으로 우회하지 않는다.

Proposed markup (not a supported extension):

```html
<h1 class="title" data-contract-proposal="foundation.allowed-fonts@2" data-font-family="Oswald" data-font-weight="700">BRAND<br/>IDENTITY</h1>
```

## 12 · 12-foundation-100

bbox: `[738, 307, 230, 100]`

독립2행 표에서 위쪽 브랜드자산hub로 향하는230×100px 수직 gradient 화살표

서로 다른 계약 요소(table와hub)를 잇는 관계이다. hub는spoke만 가지며table을품는입력패널이아니고, 현재foundation/요소계약에는두독립요소를잇는관계connector가없다.

Proposed markup (not a supported extension):

```html
<div class="relation" data-el="toggle-grid-relation"><div class="from" data-ref="identity-table"></div><div class="connector to-u"></div><div class="to" data-ref="brand-assets-hub"></div></div>
```

## 12 · 12-foundation-101

bbox: `[498, 400, 709, 228]`

헤더 없는2행 정의 표. 각 행은 검정 label/옅은 note 면이며 행 사이8px이 떨어져 있다. label36.5%, 큰24px label과19px note, note59px inset.

table09의 공유 격자/25% label열과 다른 분리행/비율/큰 label 디자인이다. 분리형 표 변형이 없으며 단순 속성 정의를 architecture 층으로 바꾸지 않는다.

Proposed markup (not a supported extension):

```html
<div class="tablebox separated" data-contract-proposal="table.grid@2"><table class="table"><thead></thead><tbody><tr><th>브랜드 퍼스널리티</th><td>브랜드가 사람이라면 어떻게 보이고, 행동하고, 말할 것인지 를 정리</td></tr><tr><th>핵심 메시지</th><td>핵심가치, 가치제안, 차별화 포인트를 반영한 메시지 방향성</td></tr></tbody></table></div>
```
