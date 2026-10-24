# Unexpressible instances

## 02 · 02-agenda-1

bbox: `[0, 155, 1192, 565]`

1192×565px;2열×5행번호목차. 각행48px/700순번+22px/650이름,순번과이름28px간격. 행/열1px구분선.

한 목차 요소 안의 2열×5행, 총10항목은 agenda.entries@1의 최대8개를 넘는다. 원본을 두 목차로 나누거나 항목을 줄여 같은 원본인 것처럼 기록하지 않는다.

Proposed markup (not a supported extension):

```html
<div class="agenda" data-contract-proposal="agenda.entries@2"><div class="entry"><span class="mark">01</span><p class="name">투자자의 가슴을 뛰게 할 비전</p></div><div class="entry"><span class="mark">02</span><p class="name">우리가 해결하려는 명확한 문제</p></div><div class="entry"><span class="mark">03</span><p class="name">우리의 혁신적인 해결책</p></div><div class="entry"><span class="mark">04</span><p class="name">우리가 공략할 거대한 시장</p></div><div class="entry"><span class="mark">05</span><p class="name">제품 상세 및 핵심 기술</p></div><div class="entry"><span class="mark">06</span><p class="name">우리의 수익 모델</p></div><div class="entry"><span class="mark">07</span><p class="name">우리가 증명한 성과</p></div><div class="entry"><span class="mark">08</span><p class="name">경쟁 환경 및 우리의 독보적 위치</p></div><div class="entry"><span class="mark">09</span><p class="name">우리의 성장 로드맵</p></div><div class="entry"><span class="mark">10</span><p class="name">팀 소개</p></div></div>
```

## 03 · 03-gap-1

bbox: `[0, 155, 1280, 352]`

긴수평사진띠

가로로만긴seat띠를허용하지않는계약과충돌하므로모양을바꾸지않고배너slot부재로기록.

Proposed markup (not a supported extension):

```html
<figure class="frame banner"><div class="seat" data-ph="1"></div></figure>
```

## 04 · 04-gap-1

bbox: `[0, 155, 596, 188.33]`

긴수평사진띠

가로로만긴seat띠를허용하지않는계약과충돌하므로모양을바꾸지않고배너slot부재로기록.

Proposed markup (not a supported extension):

```html
<figure class="frame banner"><div class="seat" data-ph="1"></div></figure>
```

## 04 · 04-gap-2

bbox: `[596, 343.33, 596, 188.33]`

긴수평사진띠

가로로만긴seat띠를허용하지않는계약과충돌하므로모양을바꾸지않고배너slot부재로기록.

Proposed markup (not a supported extension):

```html
<figure class="frame banner"><div class="seat" data-ph="1"></div></figure>
```

## 04 · 04-gap-3

bbox: `[0, 531.66, 596, 188.33]`

긴수평사진띠

가로로만긴seat띠를허용하지않는계약과충돌하므로모양을바꾸지않고배너slot부재로기록.

Proposed markup (not a supported extension):

```html
<figure class="frame banner"><div class="seat" data-ph="1"></div></figure>
```

## 06 · 06-foundation-57

bbox: `[766, 223, 380, 436]`

TAM/SAM/SOM 라벨을 가진380×256·313×214·216×153px 타원3개를위로겹쳐쌓음. 각타원은다음타원을완전히포함하지않으며수치가없다.

orbit는다음집합을안에포함하는구조이고venn은교집합관계이며funnel은정량폭+fig를가진단계이다. 이그림은시장포함의미를서로포개진타원으로나타내므로어느계약으로도구조와의미를동시에유지할수없다.

Proposed markup (not a supported extension):

```html
<div class="market-stack" data-el="portico-market-stack"><div class="market"><span class="name">TAM</span></div><div class="market"><span class="name">SAM</span></div><div class="market"><span class="name">SOM</span></div></div>
```

## 09 · 09-foundation-106

bbox: `[590, 195, 563, 457]`

2개 시리즈×5그룹 쌍막대, 수평20단위 가는 괘선, 왼쪽0~100축, 아래연도공통라벨, 막대를 가로지르는 곡선상승화살표와 원형100억배지.

chart.bar@1에 시리즈 쌍을 묶는 그룹 및 공통 category label 구조가 없다. 상승화살표/정량배지 데이터 슬롯도 없다. 두 시리즈를 막대10개로 평탄화하거나 배지를 삭제하지 않는다.

Proposed markup (not a supported extension):

```html
<div class="grouped-bars" data-el="<collection>-chart-grouped-bar" style="--max:100"><div class="axis"><div class="annotation"><span class="fig">100억</span><span class="note">전년 대비120% 성장</span></div></div><div class="groups"><div class="group"><span class="name">분류명</span><div class="bar tone-1" style="--v:20"><b>20</b></div><div class="bar tone-2" style="--v:30"><b>30</b></div></div></div><div class="series-keys"><span class="key tone-1">시리즈 A</span><span class="key tone-2">시리즈 B</span></div></div>
```

## 09 · 09-gap-1

bbox: `[1025, 235, 128, 128]`

128px채움원+10px옅은테두리안의3행매출badge

metric은면없는수치이며현재card기본은flat정보패널이다. 원형badge를표현하는계약/변형이없다.

Proposed markup (not a supported extension):

```html
<div class="badge circle"><p class="kick">...</p><p class="name">...</p><p class="fig">...</p></div>
```

## 13 · 13-gap-1

bbox: `[0, 155, 595, 197]`

50억62px수치가왼쪽,투자제목20px와16px본문은오른쪽인BareAsk

metric의source09기본은수치오른쪽이다. .reverse/.h같은metric변형이없으며,문구를뒤집거나같은기본이라고주장하지않는다.

Proposed markup (not a supported extension):

```html
<div class="stat reverse"><div class="parts"><p class="fig">50억</p><p class="name">...</p><p class="note">...</p></div></div>
```

## 13 · 13-foundation-141

bbox: `[65, 384, 466, 290]`

5그룹 쌍막대와 0~100 축, 20단위 수평선, Keyword1~5 공동 라벨, 아래에서 우상향하는 채움 곡선화살표.

portico09와 동일하게 chart.bar@1에는 2시리즈 그룹과 공통그룹라벨·장식상승화살표 슬롯이 없다. 작은칸에서 다른형태로 대체하지 않는다.

Proposed markup (not a supported extension):

```html
<div class="grouped-bars" data-el="<collection>-chart-grouped-bar" style="--max:100"><div class="axis"></div><div class="groups"><div class="group"><span class="name">분류명</span><div class="bar tone-1" style="--v:20"><b>20</b></div><div class="bar tone-2" style="--v:30"><b>30</b></div></div></div><div class="series-keys"><span class="key tone-1">시리즈 A</span><span class="key tone-2">시리즈 B</span></div></div>
```
