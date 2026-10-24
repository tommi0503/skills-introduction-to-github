# Unexpressible instances

## 03 · 03-gap-1

bbox: `[1213, 253, 67, 399]`

페이지오른쪽67×439px의연속사진crop

별도정사각좌석이아니라페이지밖사진의노출된edge다. 이를다른사진seat나길쭉한fixture로변형하지않는다.

Proposed markup (not a supported extension):

```html
<figure class="frame bleed clip"><div class="seat" data-ph="1"></div></figure>
```

## 10 · 10-foundation-60

bbox: `[142, 257, 997, 383]`

좌우446×383 비교 패널. 50px Before/After 제목띠(After만ink), 흰333px body안26px 가운데 h3와긴단락, 중앙75px 점선 화살표.

versus는 각 side가 name+.list 구조여야 하고 list는 marker를그려야한다. 이 source는 marker없는 title+paragraph 패널이다. single list item으로 바꾼 뒤 marker를숨기는것은허용하지않는다.

Proposed markup (not a supported extension):

```html
<div class="versus" data-contract-proposal="versus.rich@2"><section class="side"><p class="label">Before</p><h3 class="name">변화전의 모습</h3><div class="prose"><p>변화 전의 모습을 간략히 적어보세요.</p></div></section><section class="side on"><p class="label">After</p><h3 class="name">변화후의 모습</h3><div class="prose"><p>변화 후의 모습을 간략히 적어주세요.</p></div></section></div>
```

## 12 · 12-foundation-71

bbox: `[635, 250, 573, 399]`

회색/검정 두시리즈×세그룹,61px 막대, 그룹내19px·그룹사이38px간격, 상단값라벨14px, 0~80좌축/20단위수평선, 아래항목01/02/03그룹라벨, 플롯내작은2키범례.

chart.bar@1에는세항목별두시리즈를묶고한category라벨을공유하는그룹구조가없다. 6개독립막대로라벨을중복하거나배치조건으로특정3쌍에만걸리는규칙을만들지않는다.

Proposed markup (not a supported extension):

```html
<div class="grouped-bars" data-el="<collection>-chart-grouped-bar" style="--max:100"><div class="axis"></div><div class="groups"><div class="group"><span class="name">분류명</span><div class="bar tone-1" style="--v:20"><b>20</b></div><div class="bar tone-2" style="--v:30"><b>30</b></div></div></div><div class="series-keys"><span class="key tone-1">시리즈 A</span><span class="key tone-2">시리즈 B</span></div></div>
```
