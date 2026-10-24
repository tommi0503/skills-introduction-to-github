# Unexpressible instances

## 01 · 01-foundation-7

bbox: `[891, 549.61, 329.77, 129.0]`

오른쪽 아래 고정된 브랜드 표제와 설명

cover의 허용 anchor에는 at-bottom-right가 없다. 반대 의미의 at-bottom-left 또는 일반 요소로 바꾸어 숨기지 않는다.

Proposed markup (not a supported extension):

```html
<div class="lockup at-bottom-right" data-contract-proposal="foundation.page@2"><h1 class="title">MIRIMedi AI</h1><p class="lead">The New Vision of Radiology</p></div>
```

## 02 · 02-gap-1

bbox: `[631, 59, 271, 169]`

흰leaf-caption과15px 역상산문·위14px순번의ExecutiveSummary. 세로선은페이지전체열의경계이며card03의안쪽note rule가아님.

card03/12의leaf-title+inset rule/body와달리전체페이지경계rule에붙은whitecap/inversecopy설계다. .on으로개별body채움을만들면원래없는면이생기고.page외부를보는조건도금지된다.

Proposed markup (not a supported extension):

```html
<section class="summary-column inverse"><p class="kick">...</p><h3>...</h3><p>...</p></section>
```

## 02 · 02-gap-2

bbox: `[921, 251, 271, 168]`

흰leaf-caption과15px 역상산문·위14px순번의ExecutiveSummary. 세로선은페이지전체열의경계이며card03의안쪽note rule가아님.

card03/12의leaf-title+inset rule/body와달리전체페이지경계rule에붙은whitecap/inversecopy설계다. .on으로개별body채움을만들면원래없는면이생기고.page외부를보는조건도금지된다.

Proposed markup (not a supported extension):

```html
<section class="summary-column inverse"><p class="kick">...</p><h3>...</h3><p>...</p></section>
```

## 02 · 02-gap-3

bbox: `[631, 358, 271, 166]`

흰leaf-caption과15px 역상산문·위14px순번의ExecutiveSummary. 세로선은페이지전체열의경계이며card03의안쪽note rule가아님.

card03/12의leaf-title+inset rule/body와달리전체페이지경계rule에붙은whitecap/inversecopy설계다. .on으로개별body채움을만들면원래없는면이생기고.page외부를보는조건도금지된다.

Proposed markup (not a supported extension):

```html
<section class="summary-column inverse"><p class="kick">...</p><h3>...</h3><p>...</p></section>
```

## 03 · 03-foundation-24

bbox: `[47, 186.33, 529.61, 93.31]`

주 표제의 행별 폭 맞춤: 실제 글자 크기 60px 초과와 큰 음수 자간이 결합된 행

고정 replica에는 행마다 서로 다른 font-size·line-height·큰 음수 tracking으로 폭을 맞춘 결과가 있다. foundation의 단일 title 타이포 계약으로는 이 독립 행 효과를 표현할 수 없다. 조립본의 표제는 보통 크기 44px 의미 구조를 유지하므로 해당 행은 replica와 다르다.

Proposed markup (not a supported extension):

```html
<h1 class="title"><span class="run" data-contract-proposal="foundation.title-runs@1" data-font-ratio="source-size / title-box" data-track-ratio="source-tracking / source-size">overwhelms manual review</span></h1>
```

## 04 · 04-gap-1

bbox: `[650, 211, 580, 80]`

portrait옆이름/나이·환경·상태·기술의key/value인물detail표

person22base의위portrait/leaf이름/biography와다르고side-detail명명변형이없다. table16의grid비교표와도별도디자인이라새profile-details구조가필요하다.

Proposed markup (not a supported extension):

```html
<div class="person details"><dl><dt>...</dt><dd>...</dd></dl></div>
```

## 05 · 05-quote-caption-effect-gap

bbox: `[672, 368, 100.02, 11]`

Hospital Admin caption fixed-fit11px/500,+1.72792px tracking instead of base18px attribution.

Independent caption typography has no named quote variant; keep the semantic quote but document the unsupported exact caption effect.

Proposed markup (not a supported extension):

```html
<div class="by"><span class="name compact-tracked">Hospital Admin</span></div>
```

## 06 · 06-foundation-62

bbox: `[48, 102.41, 637.33, 73.19]`

주 표제의 행별 폭 맞춤: 실제 글자 크기 60px 초과와 큰 음수 자간이 결합된 행

고정 replica에는 행마다 서로 다른 font-size·line-height·큰 음수 tracking으로 폭을 맞춘 결과가 있다. foundation의 단일 title 타이포 계약으로는 이 독립 행 효과를 표현할 수 없다. 조립본의 표제는 보통 크기 44px 의미 구조를 유지하므로 해당 행은 replica와 다르다.

Proposed markup (not a supported extension):

```html
<h1 class="title"><span class="run" data-contract-proposal="foundation.title-runs@1" data-font-ratio="source-size / title-box" data-track-ratio="source-tracking / source-size">diagnostic speed and accuracy.</span></h1>
```

## 06 · 06-card-1

bbox: `[49, 296, 310, 424]`

170×30 compact leaf cap at y296;15px subheadings at365/472/578,11px body lines below; no numerical mark or kick exists.

The03 base has a217px leaf on a271px root. Source06 has a170px cap and a wider body without any optional prefix; no named card variant expresses this distinct cap/body ratio. Earlier invented01/02/03 data was removed.

Proposed markup (not a supported extension):

```html
<div class="card compact-cap"><div class="parts"><h3 class="name">...</h3><div class="note"><p><b>...</b>...</p></div></div></div>
```

## 06 · 06-card-2

bbox: `[359, 296, 291, 424]`

170×30 compact leaf cap at y296;15px subheadings at365/472/578,11px body lines below; no numerical mark or kick exists.

The03 base has a217px leaf on a271px root. Source06 has a170px cap and a wider body without any optional prefix; no named card variant expresses this distinct cap/body ratio. Earlier invented01/02/03 data was removed.

Proposed markup (not a supported extension):

```html
<div class="card compact-cap"><div class="parts"><h3 class="name">...</h3><div class="note"><p><b>...</b>...</p></div></div></div>
```

## 06 · 06-card-3

bbox: `[650, 296, 320, 424]`

170×30 compact leaf cap at y296;15px subheadings at365/472/578,11px body lines below; no numerical mark or kick exists.

The03 base has a217px leaf on a271px root. Source06 has a170px cap and a wider body without any optional prefix; no named card variant expresses this distinct cap/body ratio. Earlier invented01/02/03 data was removed.

Proposed markup (not a supported extension):

```html
<div class="card compact-cap"><div class="parts"><h3 class="name">...</h3><div class="note"><p><b>...</b>...</p></div></div></div>
```

## 07 · 07-residual-white-cap-gap-1

bbox: `[340, 381, 198, 30]`

흰 198×30px section cap, 우상단만34px 곡선, 파란 제목. 첫 캡은 source fitted9.69231px/500 및 2.33194px 자간, 둘째 캡은18px/500 및 -.3px 자간.

headline.block@1의 허용 변형은 .big/.center/.on뿐이다. Lamella base(22쪽)는 양대각 모서리 곡선과 연보라 면이며 .on은 강조색 면이다. 이 캡의 흰 역상 면과 단일 우상단 곡선을 유지할 계약 변형이 없다. 색이나 모서리를 임의로 바꾸어 같은 요소라 부르지 않는다.

Proposed markup (not a supported extension):

```html
<div class="headline inverse-tab" data-contract-proposal="headline.block@2"><h2>The Problem</h2></div>
```

## 07 · 07-residual-white-cap-gap-2

bbox: `[776, 381, 198, 30]`

흰 198×30px section cap, 우상단만34px 곡선, 파란 제목. 첫 캡은 source fitted9.69231px/500 및 2.33194px 자간, 둘째 캡은18px/500 및 -.3px 자간.

headline.block@1의 허용 변형은 .big/.center/.on뿐이다. Lamella base(22쪽)는 양대각 모서리 곡선과 연보라 면이며 .on은 강조색 면이다. 이 캡의 흰 역상 면과 단일 우상단 곡선을 유지할 계약 변형이 없다. 색이나 모서리를 임의로 바꾸어 같은 요소라 부르지 않는다.

Proposed markup (not a supported extension):

```html
<div class="headline inverse-tab" data-contract-proposal="headline.block@2"><h2>The Solution</h2></div>
```

## 08 · 08-foundation-87

bbox: `[47, 103.2, 821.02, 72.58]`

주 표제의 행별 폭 맞춤: 실제 글자 크기 60px 초과와 큰 음수 자간이 결합된 행

고정 replica에는 행마다 서로 다른 font-size·line-height·큰 음수 tracking으로 폭을 맞춘 결과가 있다. foundation의 단일 title 타이포 계약으로는 이 독립 행 효과를 표현할 수 없다. 조립본의 표제는 보통 크기 44px 의미 구조를 유지하므로 해당 행은 replica와 다르다.

Proposed markup (not a supported extension):

```html
<h1 class="title"><span class="run" data-contract-proposal="foundation.title-runs@1" data-font-ratio="source-size / title-box" data-track-ratio="source-tracking / source-size">data ingestion to final report generation.</span></h1>
```

## 08 · 08-card-3

bbox: `[422, 229, 281, 199]`

독립leaf-caption+1px세로hairline+richnote정보column. 실제Step/Weeks정보는kick,14px namecap과11px/16px본문은03기본과동일. 멤버간연결선은없음.

White single-top-right-corner cap over a transparent body cannot use source03 blue leaf cap or source12 quiet/on filled body; no named card variant preserves this independent design.

Proposed markup (not a supported extension):

```html
<div class="card" data-el="lamella-card"><div class="parts"><h3 class="name">Multi-Layer Inference (The Brain)</h3><div class="note"><p><span>Focus: The core Al processing power.<br>- Action: Simultaneous parallel inference for<br>multiple conditions.<br>- Tech Detail: Hybrid CNN-Transformer<br>architecture for local and global analysis.<br>- Speed: Complete inference takes 3 seconds per<br>study.</span></p></div></div></div>
```

## 08 · 08-card-2

bbox: `[132, 464, 281, 199]`

독립leaf-caption+1px세로hairline+richnote정보column. 실제Step/Weeks정보는kick,14px namecap과11px/16px본문은03기본과동일. 멤버간연결선은없음.

White single-top-right-corner cap over a transparent body cannot use source03 blue leaf cap or source12 quiet/on filled body; no named card variant preserves this independent design.

Proposed markup (not a supported extension):

```html
<div class="card" data-el="lamella-card"><div class="parts"><p class="kick">Step 2</p><h3 class="name">Pre-Processing (The Cleanup)</h3><div class="note"><p><span>Focus: Ensuring data quality before analysis.<br>- Action: Filters out non-diagnostic slices (e.g.,<br>scout views, air) and normalizes image contrast.<br>- Tech Detail: Applies 3D Volumetric<br>Reconstruction to stack 2D slices into a unified<br>3D block, preparing the data for spatial analysis.<br>- Edge: Eliminates &quot;noise&quot; that typically causes<br>false positives in legacy systems.</span></p></div></div></div>
```

## 08 · 08-card-6

bbox: `[840, 464, 281, 199]`

독립leaf-caption+1px세로hairline+richnote정보column. 실제Step/Weeks정보는kick,14px namecap과11px/16px본문은03기본과동일. 멤버간연결선은없음.

White single-top-right-corner cap over a transparent body cannot use source03 blue leaf cap or source12 quiet/on filled body; no named card variant preserves this independent design.

Proposed markup (not a supported extension):

```html
<div class="card" data-el="lamella-card"><div class="parts"><p class="kick">Step 6</p><h3 class="name">Auto-Reporting (The Closure)</h3><div class="note"><p><span>Focus: Reducing administrative burden.<br>- Action: One-click insertion of Structured<br>Reports into the EMR.<br>- Content: Auto-fills findings (e.g., nodule<br>size/location) and clinical guidelines.<br>- Verification: The radiologist simply reviews the<br>pre-filled text, makes final edits, and hits &quot;Sign.&quot;</span></p></div></div></div>
```

## 09 · 09-foundation-100

bbox: `[49, 145.38, 768.67, 74.23]`

주 표제의 행별 폭 맞춤: 실제 글자 크기 60px 초과와 큰 음수 자간이 결합된 행

고정 replica에는 행마다 서로 다른 font-size·line-height·큰 음수 tracking으로 폭을 맞춘 결과가 있다. foundation의 단일 title 타이포 계약으로는 이 독립 행 효과를 표현할 수 없다. 조립본의 표제는 보통 크기 44px 의미 구조를 유지하므로 해당 행은 replica와 다르다.

Proposed markup (not a supported extension):

```html
<h1 class="title"><span class="run" data-contract-proposal="foundation.title-runs@1" data-font-ratio="source-size / title-box" data-track-ratio="source-tracking / source-size">the largest annotated clinical dataset.</span></h1>
```

## 09 · 09-foundation-101

bbox: `[49, 274, 872, 406]`

Experience/Intelligence/Foundation의 3개 층을 세로가 아닌 가로3열로 나열. 각 열에는 layer번호/leaf탭/소개와3개 모듈 박스가 있다.

architecture 계약은 stacked layers이며 가로 .h 변형이 없다. layer 소개와 제목+설명의 모듈 슬롯도 현 .name+.chip 텍스트보다 풍부하다. 다른 table/card로 재해석하지 않는다.

Proposed markup (not a supported extension):

```html
<div class="arch h" data-contract-proposal="architecture.layers@2"><div class="layer"><p class="kick">Layer 1: Application</p><h3 class="name">The Experience Layer</h3><p class="note">The visible interface that doctors interact with.</p><div class="chip"><b>Clinician Dashboard</b><p>An intuitive, web-based command center.</p></div></div><div class="layer"><p class="kick">Layer 2: AI Core</p><h3 class="name">The Intelligence Layer</h3></div><div class="layer"><p class="kick">Layer 3: Infrastructure</p><h3 class="name">The Foundation Layer</h3></div></div>
```

## 10 · 10-gap-1

bbox: `[1031, 147, 199.08, 43.47]`

11px 세 행의 오른쪽 정렬 계산근거, 제목과 분리된 텍스트 블록.

기본 prose07은 왼쪽 정렬이다. 현재 lead/cols/quiet에는 오른쪽 정렬 의미가 없으므로 계산식만 위한 조건을 만들지 않는다.

Proposed markup (not a supported extension):

```html
<div class="prose right"><p>...</p></div>
```

## 10 · 10-foundation-112

bbox: `[47, 267.41, 338.88, 75.17]`

주 표제의 행별 폭 맞춤: 실제 글자 크기 60px 초과와 큰 음수 자간이 결합된 행

고정 replica에는 행마다 서로 다른 font-size·line-height·큰 음수 tracking으로 폭을 맞춘 결과가 있다. foundation의 단일 title 타이포 계약으로는 이 독립 행 효과를 표현할 수 없다. 조립본의 표제는 보통 크기 44px 의미 구조를 유지하므로 해당 행은 replica와 다르다.

Proposed markup (not a supported extension):

```html
<h1 class="title"><span class="run" data-contract-proposal="foundation.title-runs@1" data-font-ratio="source-size / title-box" data-track-ratio="source-tracking / source-size">strategy.</span></h1>
```

## 11 · 11-foundation-119

bbox: `[47, 102.38, 862.16, 74.23]`

주 표제의 행별 폭 맞춤: 실제 글자 크기 60px 초과와 큰 음수 자간이 결합된 행

고정 replica에는 행마다 서로 다른 font-size·line-height·큰 음수 tracking으로 폭을 맞춘 결과가 있다. foundation의 단일 title 타이포 계약으로는 이 독립 행 효과를 표현할 수 없다. 조립본의 표제는 보통 크기 44px 의미 구조를 유지하므로 해당 행은 replica와 다르다.

Proposed markup (not a supported extension):

```html
<h1 class="title"><span class="run" data-contract-proposal="foundation.title-runs@1" data-font-ratio="source-size / title-box" data-track-ratio="source-tracking / source-size">aging population and government support.</span></h1>
```

## 11 · 11-foundation-120

bbox: `[391, 237, 23, 10]`

차트최대값의통화기호와숫자 $100.

chart.bar@1의 --max는숫자만받고통화단위/축단위슬롯이없다. 달러기호를디자인CSS의고정content로박으면다른퍼센트/억원fixture의데이터를오염시킨다.

Proposed markup (not a supported extension):

```html
<div class="bars" style="--max:100"><div class="axis-y"><span class="unit">$</span><span class="max">100</span></div><div class="bar" style="--v:5"></div></div>
```

## 11 · 11-gap-1

bbox: `[714, 283, 164, 164]`

한모서리직각의채움droplet badge 안 큰수치+작은이름

metric은면없는수치이고card기본은leaf-title+rule panel이다. 이별도droplet badge에맞는계약변형이없다.

Proposed markup (not a supported extension):

```html
<div class="badge droplet"><p class="fig">+25%</p><p class="name">CAGR</p></div>
```

## 12 · 12-residual-source-fragment-gap-1

bbox: `[631, 276, 32.015625, 11.546875]`

독립 source-fitting 잔여 텍스트 조각. 현재 보이는 글자와 실제 DOM 경계만 기록한다.

원본 fitting 과정에 남은 텍스트 조각으로 계약 요소의 명칭/설명이라고 의미를 확정할 수 없다. 어떤 원래 문장인지 임의 복원하거나 새 비즈니스 문장으로 바꾸지 않는다.

Proposed markup (not a supported extension):

```html
<span class="source-fragment" data-contract-proposal="source-fragment.text@1">CardB</span>
```

## 12 · 12-residual-source-fragment-gap-2

bbox: `[929.5, 278, 10.515625, 11.875]`

독립 source-fitting 잔여 텍스트 조각. 현재 보이는 글자와 실제 DOM 경계만 기록한다.

원본 fitting 과정에 남은 텍스트 조각으로 계약 요소의 명칭/설명이라고 의미를 확정할 수 없다. 어떤 원래 문장인지 임의 복원하거나 새 비즈니스 문장으로 바꾸지 않는다.

Proposed markup (not a supported extension):

```html
<span class="source-fragment" data-contract-proposal="source-fragment.text@1">ar</span>
```

## 12 · 12-card-3

bbox: `[921, 296, 271, 384]`

271px폭의전체leaf제목띠와311pxbody면. quiet는흰내용면, on은강조내용면+반전leaf. .note는명시된항목명과짧은설명을번갈아배치.

Its 12px/500, -0.329427px caption in the same271×384 panel is an independent typography design from quiet source12-card-1 (10px/500, +1.49614px). No additional named quiet typography variant exists; text/position rules are forbidden.

Proposed markup (not a supported extension):

```html
<div class="card quiet" data-el="lamella-card"><div class="parts"><h3 class="name">OEM &amp; API Licensing (The Scale)</h3><div class="note"><p><b>Type</b><span>B2B2B Partnership Revenue.</span></p><p><b>Structure</b><span>Royalty per pre-installed device<br>or third-party API call.</span></p><p><b>Partners</b><span>MRI/CT Hardware Vendors<br>(GE, Siemens) &amp; Telehealth Platforms.</span></p><p><b>Pricing</b><span>10-15% Revenue Share or flat license fee<br>per unit.</span></p><p><b>Why it works</b><span><b>Zero CAC: leveraging global</b><br>networks to reach inaccessible markets.</span></p></div></div></div>
```

## 13 · 13-foundation-142

bbox: `[44, 144.63, 848.73, 90.72]`

주 표제의 행별 폭 맞춤: 실제 글자 크기 60px 초과와 큰 음수 자간이 결합된 행

고정 replica에는 행마다 서로 다른 font-size·line-height·큰 음수 tracking으로 폭을 맞춘 결과가 있다. foundation의 단일 title 타이포 계약으로는 이 독립 행 효과를 표현할 수 없다. 조립본의 표제는 보통 크기 44px 의미 구조를 유지하므로 해당 행은 replica와 다르다.

Proposed markup (not a supported extension):

```html
<h1 class="title"><span class="run" data-contract-proposal="foundation.title-runs@1" data-font-ratio="source-size / title-box" data-track-ratio="source-tracking / source-size">motion to minimize friction and build trust.</span></h1>
```

## 14 · 14-foundation-152

bbox: `[45, 102.38, 841.52, 74.23]`

주 표제의 행별 폭 맞춤: 실제 글자 크기 60px 초과와 큰 음수 자간이 결합된 행

고정 replica에는 행마다 서로 다른 font-size·line-height·큰 음수 tracking으로 폭을 맞춘 결과가 있다. foundation의 단일 title 타이포 계약으로는 이 독립 행 효과를 표현할 수 없다. 조립본의 표제는 보통 크기 44px 의미 구조를 유지하므로 해당 행은 replica와 다르다.

Proposed markup (not a supported extension):

```html
<h1 class="title"><span class="run" data-contract-proposal="foundation.title-runs@1" data-font-ratio="source-size / title-box" data-track-ratio="source-tracking / source-size">makers through high-trust channels.</span></h1>
```

## 14 · 14-gap-1

bbox: `[49, 232, 271, 488]`

leafheadline·donut·richprose를함께감싸는271pxcolumn과세로rule

각하위요소는표현가능하지만이들을담는titled-panel의body slot이없다. card.note에차트와문단을임의로감추지않는다.

Proposed markup (not a supported extension):

```html
<section class="panel"><header>...</header><div class="body">...</div></section>
```

## 14 · 14-gap-2

bbox: `[340, 232, 271, 488]`

leafheadline·donut·richprose를함께감싸는271pxcolumn과세로rule

각하위요소는표현가능하지만이들을담는titled-panel의body slot이없다. card.note에차트와문단을임의로감추지않는다.

Proposed markup (not a supported extension):

```html
<section class="panel"><header>...</header><div class="body">...</div></section>
```

## 14 · 14-gap-3

bbox: `[631, 232, 271, 488]`

leafheadline·donut·richprose를함께감싸는271pxcolumn과세로rule

각하위요소는표현가능하지만이들을담는titled-panel의body slot이없다. card.note에차트와문단을임의로감추지않는다.

Proposed markup (not a supported extension):

```html
<section class="panel"><header>...</header><div class="body">...</div></section>
```

## 14 · 14-foundation-159

bbox: `[921, 253, 310, 310]`

310px 다중분할 도넛. 40/30/30 세색 구역과 구역내라벨, 가운데구멍30%지름.

chart.donut@1은 한 전체 중 단일비중 하나만 정의한다. 다중분할·구역별라벨·세색데이터가 없어 단일도넛이나여러원으로바꾸지않는다.

Proposed markup (not a supported extension):

```html
<div class="segmented-donut" data-el="lamella-chart-share"><div class="segment tone-1" style="--v:40"><span class="fig">40%</span><span class="name">범주 A</span></div><div class="segment tone-2" style="--v:30"><span class="fig">30%</span></div><div class="segment tone-3" style="--v:30"><span class="fig">30%</span></div></div>
```

## 14 · 14-residual-source-fragment-gap-3

bbox: `[1186.5, 613, 9, 7.96875]`

독립 source-fitting 잔여 텍스트 조각. 현재 보이는 글자와 실제 DOM 경계만 기록한다.

원본 fitting 과정에 남은 텍스트 조각으로 계약 요소의 명칭/설명이라고 의미를 확정할 수 없다. 어떤 원래 문장인지 임의 복원하거나 새 비즈니스 문장으로 바꾸지 않는다.

Proposed markup (not a supported extension):

```html
<span class="source-fragment" data-contract-proposal="source-fragment.text@1">ge</span>
```

## 15 · 15-foundation-174

bbox: `[504, 64, 706, 560]`

교차축 위 서로 다른 크기의 경쟁사 원4개와 강조 teardrop1개. 강조 mark와 큰 경쟁사 mark 안에는 이름 외에2–3행 세부설명이 들어간다. 축은 endpoint쌍이 아닌 단일 Workflow Compatibility 이름이다.

positioning mark는 .seat.logo 또는 .name만 갖고 .note/개별 --r 필드가 없다. source는98/176/194px의 다른 크기와 mark내 세부설명, 축명 슬롯을 함께 필요로 하므로 유령label이나 class외삽으로 덮지 않는다.

Proposed markup (not a supported extension):

```html
<div class="posmap bubble" data-contract-proposal="positioning.rich@2"><div class="axis-x"><span class="label">Workflow Compatibility</span></div><div class="axis-y"><span class="label">Diagnostic Accuracy</span></div><div class="mark on" style="--x:76;--y:75;--r:28"><span class="name">MIRIMedi AI</span><p class="note">High Accuracy<br>High Compatibility</p></div><div class="mark" style="--x:33;--y:22;--r:25"><span class="name">Competitors</span><p class="note">Others are either accurate but slow, or fast but inaccurate.</p></div></div>
```

## 16 · 16-foundation-181

bbox: `[48, 101.63, 763.13, 90.72]`

주 표제의 행별 폭 맞춤: 실제 글자 크기 60px 초과와 큰 음수 자간이 결합된 행

고정 replica에는 행마다 서로 다른 font-size·line-height·큰 음수 tracking으로 폭을 맞춘 결과가 있다. foundation의 단일 title 타이포 계약으로는 이 독립 행 효과를 표현할 수 없다. 조립본의 표제는 보통 크기 44px 의미 구조를 유지하므로 해당 행은 replica와 다르다.

Proposed markup (not a supported extension):

```html
<h1 class="title"><span class="run" data-contract-proposal="foundation.title-runs@1" data-font-ratio="source-size / title-box" data-track-ratio="source-tracking / source-size">that matter most to clinical workflows.</span></h1>
```

## 17 · 17-gap-1

bbox: `[651, 189, 164, 164]`

한모서리직각의채움droplet badge 안 큰수치+작은이름

metric은면없는수치이고card기본은leaf-title+rule panel이다. 이별도droplet badge에맞는계약변형이없다.

Proposed markup (not a supported extension):

```html
<div class="badge droplet"><p class="fig">X00%</p><p class="name">QoQ Growth</p></div>
```

## 17 · 17-gap-2

bbox: `[991, 443, 123, 123]`

한모서리직각의채움droplet badge 안 큰수치+작은이름

metric은면없는수치이고card기본은leaf-title+rule panel이다. 이별도droplet badge에맞는계약변형이없다.

Proposed markup (not a supported extension):

```html
<div class="badge droplet"><p class="fig">X% > XX%</p><p class="name">Retention Rate</p></div>
```

## 18 · 18-quote-glyph-effect-gap-2

bbox: `[1035.5, 188, 28.53, 24.88]`

Source text extraction is literal99, rendered as a different double-curved opening glyph.

quote.voice@1 draws one common opening glyph; an alternate source glyph has no named variant and cannot depend on item position.

Proposed markup (not a supported extension):

```html
<span class="quote-glyph alt">99</span>
```

## 18 · 18-foundation-208

bbox: `[47, 270.66, 240.22, 90.69]`

주 표제의 행별 폭 맞춤: 실제 글자 크기 60px 초과와 큰 음수 자간이 결합된 행

고정 replica에는 행마다 서로 다른 font-size·line-height·큰 음수 tracking으로 폭을 맞춘 결과가 있다. foundation의 단일 title 타이포 계약으로는 이 독립 행 효과를 표현할 수 없다. 조립본의 표제는 보통 크기 44px 의미 구조를 유지하므로 해당 행은 replica와 다르다.

Proposed markup (not a supported extension):

```html
<h1 class="title"><span class="run" data-contract-proposal="foundation.title-runs@1" data-font-ratio="source-size / title-box" data-track-ratio="source-tracking / source-size">our solution.</span></h1>
```

## 18 · 18-quote-glyph-effect-gap-4

bbox: `[1035.5, 444, 28.53, 24.88]`

Source text extraction is literal99, rendered as a different double-curved opening glyph.

quote.voice@1 draws one common opening glyph; an alternate source glyph has no named variant and cannot depend on item position.

Proposed markup (not a supported extension):

```html
<span class="quote-glyph alt">99</span>
```

## 19 · 19-foundation-218

bbox: `[47, 100.02, 668.23, 75.95]`

주 표제의 행별 폭 맞춤: 실제 글자 크기 60px 초과와 큰 음수 자간이 결합된 행

고정 replica에는 행마다 서로 다른 font-size·line-height·큰 음수 tracking으로 폭을 맞춘 결과가 있다. foundation의 단일 title 타이포 계약으로는 이 독립 행 효과를 표현할 수 없다. 조립본의 표제는 보통 크기 44px 의미 구조를 유지하므로 해당 행은 replica와 다르다.

Proposed markup (not a supported extension):

```html
<h1 class="title"><span class="run" data-contract-proposal="foundation.title-runs@1" data-font-ratio="source-size / title-box" data-track-ratio="source-tracking / source-size">approval and global market entry.</span></h1>
```

## 20 · 20-foundation-230

bbox: `[358, 237, 400, 400]`

400px 구멍없는 세구역 파이. 시작각0°에서40/30/30 면적, 구역안에R&D40%/Ops30%/Sales30% 각각배치.

56개계약에구멍없는다중구역파이가없다. chart.donut은단일share이며구역별비율과라벨을담지못한다. 도넛3개로대체하지않는다.

Proposed markup (not a supported extension):

```html
<div class="pie" data-el="lamella-chart-pie"><div class="slice tone-1" style="--v:40;--start:0"><span class="fig">30%</span><span class="name">Ops</span></div><div class="slice tone-2" style="--v:30;--start:40"><span class="fig">30%</span><span class="name">Sales</span></div><div class="slice tone-3" style="--v:30;--start:70"><span class="fig">40%</span><span class="name">R&amp;D</span></div></div>
```

## 20 · 20-gap-1

bbox: `[795, 262, 356, 108]`

356×108px직각tonal allocation패널.13px왼쪽여백,top26px의14px이름,그아래11px/16px두행note. tone1옅은/2중간/3진한a1면. 이름은채움속ordinarylabel이며추가leaf면을겹치지않음.

leaf 제목면과 세로rule를 모두 없애는 별도 allocation panel이다. tone-N의 색 의미만으로 구조/장식을 바꿀 수 없다.

Proposed markup (not a supported extension):

```html
<div class="allocation tone-N"><p class="name">...</p><p class="note">...</p></div>
```

## 20 · 20-gap-2

bbox: `[795, 390, 356, 108]`

356×108px직각tonal allocation패널.13px왼쪽여백,top26px의14px이름,그아래11px/16px두행note. tone1옅은/2중간/3진한a1면. 이름은채움속ordinarylabel이며추가leaf면을겹치지않음.

leaf 제목면과 세로rule를 모두 없애는 별도 allocation panel이다. tone-N의 색 의미만으로 구조/장식을 바꿀 수 없다.

Proposed markup (not a supported extension):

```html
<div class="allocation tone-N"><p class="name">...</p><p class="note">...</p></div>
```

## 20 · 20-gap-3

bbox: `[795, 518, 356, 108]`

356×108px직각tonal allocation패널.13px왼쪽여백,top26px의14px이름,그아래11px/16px두행note. tone1옅은/2중간/3진한a1면. 이름은채움속ordinarylabel이며추가leaf면을겹치지않음.

leaf 제목면과 세로rule를 모두 없애는 별도 allocation panel이다. tone-N의 색 의미만으로 구조/장식을 바꿀 수 없다.

Proposed markup (not a supported extension):

```html
<div class="allocation tone-N"><p class="name">...</p><p class="note">...</p></div>
```

## 21 · 21-foundation-239

bbox: `[48, 101.63, 670.77, 90.72]`

주 표제의 행별 폭 맞춤: 실제 글자 크기 60px 초과와 큰 음수 자간이 결합된 행

고정 replica에는 행마다 서로 다른 font-size·line-height·큰 음수 tracking으로 폭을 맞춘 결과가 있다. foundation의 단일 title 타이포 계약으로는 이 독립 행 효과를 표현할 수 없다. 조립본의 표제는 보통 크기 44px 의미 구조를 유지하므로 해당 행은 replica와 다르다.

Proposed markup (not a supported extension):

```html
<h1 class="title"><span class="run" data-contract-proposal="foundation.title-runs@1" data-font-ratio="source-size / title-box" data-track-ratio="source-tracking / source-size">with a scalable financial structure</span></h1>
```

## 21 · 21-card-1

bbox: `[49, 211, 347, 298]`

347px폭의밝은driver면,약80%폭leafcap. body의4개boldlabel/짧은설명을11px/16px으로배치.

Source cap is8px/500,+1.67622px in80% width of347×298 panel, with13px subheads and11px body; this is a separate typography hierarchy from quiet source12-card-1. No named card variant captures it.

Proposed markup (not a supported extension):

```html
<div class="card quiet" data-el="lamella-card"><div class="parts"><h3 class="name">Key Drivers</h3><div class="note"><p><b>Pricing (ARPU)</b><span>Avg. $50k per Hospital/Year (Based on Tier-2 pricing).</span></p><p><b>Volume</b><span>Target 240 Active Sites by 2028.</span></p><p><b>Retention</b><span>95% Net Dollar Retention (Low Churn).</span></p><p><b>Gross Margin</b><span>Expanding from 65% 85% {Cloud efficiency).</span></p></div></div></div>
```

## 21 · 21-foundation-241

bbox: `[433, 220, 643, 310]`

3개반투명직각막대와3점가는선이동일축을공유하는혼합차트, hollow10px 점과중간BEP캡슐, 왼쪽$0M/$5M/$10M/$15M축, 아래연도.

chart.bar와 chart.line은 별도 root와 축을 갖고, 공유 플롯·혼합 데이터·BEP 주석을 담는 복합 계약이 없다. 막대만 또는 선만 남기거나 별도 root를 억지로 겹쳐 의미를 비틀지 않는다.

Proposed markup (not a supported extension):

```html
<div class="combo-chart" data-el="lamella-chart-combo" style="--max:15"><div class="bar-series"><div class="bar" style="--v:2"><span>2097(E)</span></div><div class="bar" style="--v:5.5"><span>2098(E)</span></div><div class="bar" style="--v:12"><span>2099(E)</span></div></div><div class="line-series"><div class="pt" style="--v:.7"></div><div class="pt" style="--v:5.8"></div><div class="pt" style="--v:14.7"></div></div><p class="annotation">BEP Reached (Q3 2098)</p></div>
```

## 21 · 21-foundation-243

bbox: `[49, 552, 1038, 127]`

낮고 넓은 4열 재무표, 첫머리칸만 강조띠, 세로선 없이 수평선, Gross Profit 행 전체soft강조, 작은9–11px 값.

table16과 다른 compact financial design이며 .pick는 point열에 쓰는 계약이다. source의 행 전체강조·부분머리채움·수평괘선만있는디자인을 특정4열/5행일때만 켜면 fixture 특례다.

Proposed markup (not a supported extension):

```html
<div class="tablebox financial" data-contract-proposal="table.grid@2"><table class="table"><thead><tr><th>Unit: $M</th><th>2097(Year 1)</th><th>2098(Year 2)</th><th>2099(Year 3)</th></tr></thead><tbody><tr><th>Revenue</th><td>$2.0</td><td>$5.5</td><td>$12.0</td></tr><tr class="pick-row"><th>Gross Profit</th><td>$1.3 (65%)</td><td>$4.4 (80%)</td><td>$10.2 (85%)</td></tr></tbody></table></div>
```

## 22 · 22-gap-1

bbox: `[49, 575, 873, 145]`

AdvisoryBoardleaf와세textcolumn/세로rule를담는advisory strip

그림없는adviser3명을personportrait로바꾸지않는다. caption+prose를담는ruledtext-panel wrapper가없다.

Proposed markup (not a supported extension):

```html
<section class="advisors text-only"><header>...</header><div class="people">...</div></section>
```
