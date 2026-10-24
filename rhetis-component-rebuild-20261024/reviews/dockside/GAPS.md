## 02-009 — replica 02

작은 원형 알림 숫자

- bbox: `[336, 357, 22, 22]`
- 표현 불가 이유: 알림 수 badge는 tag base(검은 범례 캡슐)와 다른 외형이며 tag에 명명된 badge 변형이 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<span class="badge" aria-label="알림 수">2</span>
```

## 04-022 — replica 04

Context Brief 머리글과 + 조작을 포함한 큰 유리 패널

- bbox: `[445, 111, 756, 552]`
- 표현 불가 이유: 목록을 담는 제목 패널 계약이 없다. 목록의 CSS가 임의의 Context Brief 문자열을 만들지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<section class="captioned-panel"><header><b class="label">Context Brief</b><button class="action" aria-label="더 보기"></button></header><div class="content"><div class="list check" data-el="dockside-list">…</div></div></section>
```

## 05-029 — replica 05

captioned-stat-panel: 부유 제목 캡슐·특수 성장 그림 또는 비교 버블·범례·설명이 한 표면에 결합한다. card의 photo base에 line/quiet를 붙여 그래프 종류를 바꾸지 않는다.

- bbox: `[445, 169, 362, 441]`
- 표현 불가 이유: captioned-stat-panel: 부유 제목 캡슐·특수 성장 그림 또는 비교 버블·범례·설명이 한 표면에 결합한다. card의 photo base에 line/quiet를 붙여 그래프 종류를 바꾸지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<figure class="stat-panel"><header class="caption">…</header><div class="graphic"><div class="bubble"><b class="fig">40<small>%</small></b></div><span class="legend">…</span></div><figcaption class="note">…</figcaption></figure>
```

## 05-030 — replica 05

captioned-stat-panel: 부유 제목 캡슐·특수 성장 그림 또는 비교 버블·범례·설명이 한 표면에 결합한다. card의 photo base에 line/quiet를 붙여 그래프 종류를 바꾸지 않는다.

- bbox: `[845, 169, 362, 441]`
- 표현 불가 이유: captioned-stat-panel: 부유 제목 캡슐·특수 성장 그림 또는 비교 버블·범례·설명이 한 표면에 결합한다. card의 photo base에 line/quiet를 붙여 그래프 종류를 바꾸지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<figure class="stat-panel"><header class="caption">…</header><div class="graphic"><div class="bubble"><b class="fig">40<small>%</small></b></div><span class="legend">…</span></div><figcaption class="note">…</figcaption></figure>
```

## 06-039 — replica 06

오른쪽에서 잘린 세 번째 사진 카드 조각

- bbox: `[1252, 145, 28, 520]`
- 표현 불가 이유: 완성 카드가 아닌 페이지 밖으로 의도적으로 잘린 조각이다. 슬롯 바깥 넘침으로 재현하지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<div class="carousel"><div class="viewport"><div class="track"><article class="media-card">…</article><article class="media-card">…</article><article class="media-card">…</article></div></div></div>
```

## 07-045 — replica 07

keyword-orbit: 이중 장식 링과 중앙 키워드는 포함관계 집합 차트가 아니다. concentric으로 의미를 바꾸지 않는다.

- bbox: `[164, 256, 366, 366]`
- 표현 불가 이유: keyword-orbit: 이중 장식 링과 중앙 키워드는 포함관계 집합 차트가 아니다. concentric으로 의미를 바꾸지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<figure class="keyword-orbit"><div class="orbit"></div><div class="core"><b class="name">…</b></div></figure>
```

## 07-047 — replica 07

자동 번호와 한 캡슐로 묶인 Problem 접두어

- bbox: `[888, 206, 1, 416]`
- 표현 불가 이유: list.num 계약은 번호를 counter로만 그린다. 번호 앞의 가변 접두어를 담을 마크업이 없으며 CSS에 원문 또는 특정 업무 문구를 고정하지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<div class="list num"><div class="item"><span class="prefix">Problem</span><b class="name">…</b><p class="note">…</p></div></div><!-- counter remains generated; prefix needs a new contract field -->
```

## 08-052 — replica 08

insight-media-card: 상단 강조 띠 + 작은 그림 + 제목/설명이 결합한 별도 카드 외형이다. 06 photo card의 이름 없는 두 번째 디자인으로 넣지 않는다.

- bbox: `[190, 292, 315, 330]`
- 표현 불가 이유: insight-media-card: 상단 강조 띠 + 작은 그림 + 제목/설명이 결합한 별도 카드 외형이다. 06 photo card의 이름 없는 두 번째 디자인으로 넣지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<article class="insight-card"><header class="caption">…</header><div class="seat" data-ph="1"></div><b class="name">…</b><p class="note">…</p></article>
```

## 08-053 — replica 08

insight-media-card: 상단 강조 띠 + 작은 그림 + 제목/설명이 결합한 별도 카드 외형이다. 06 photo card의 이름 없는 두 번째 디자인으로 넣지 않는다.

- bbox: `[537, 292, 315, 330]`
- 표현 불가 이유: insight-media-card: 상단 강조 띠 + 작은 그림 + 제목/설명이 결합한 별도 카드 외형이다. 06 photo card의 이름 없는 두 번째 디자인으로 넣지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<article class="insight-card"><header class="caption">…</header><div class="seat" data-ph="1"></div><b class="name">…</b><p class="note">…</p></article>
```

## 08-054 — replica 08

insight-media-card: 상단 강조 띠 + 작은 그림 + 제목/설명이 결합한 별도 카드 외형이다. 06 photo card의 이름 없는 두 번째 디자인으로 넣지 않는다.

- bbox: `[884, 292, 315, 330]`
- 표현 불가 이유: insight-media-card: 상단 강조 띠 + 작은 그림 + 제목/설명이 결합한 별도 카드 외형이다. 06 photo card의 이름 없는 두 번째 디자인으로 넣지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<article class="insight-card"><header class="caption">…</header><div class="seat" data-ph="1"></div><b class="name">…</b><p class="note">…</p></article>
```

## 10-066 — replica 10

carousel-picture: 화면 아래 페이지 점과 겹친 Idea 캡슐이 있는 캐러셀. frame 계약의 seat 하나로 제어 데이터까지 표현할 수 없다.

- bbox: `[205, 214, 960, 470]`
- 표현 불가 이유: carousel-picture: 화면 아래 페이지 점과 겹친 Idea 캡슐이 있는 캐러셀. frame 계약의 seat 하나로 제어 데이터까지 표현할 수 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<figure class="media-carousel"><div class="viewport"><div class="seat" data-ph="1"></div></div><div class="keywords">…</div><nav class="dots" aria-label="그림 페이지">…</nav></figure>
```

## 10-069 — replica 10

가운데 정렬 설명과 위쪽 원형 화살표를 결합한 caption-action

- bbox: `[572.41, 539, 563.59, 101.8]`
- 표현 불가 이유: prose는문단과강조글만있다. 별도action을가진caption계약이없으며새페이지조건을추가하지않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<figcaption class="caption-action"><button class="action" aria-label="이전 단계"></button><p class="note">…</p></figcaption>
```

## 12-082 — replica 12

flow-screen-panel: 부유 캡슐 + 앱 화면 + 하단 설명. 사진형 card와 다른 외형이며 대응하는 명명 변형이 없다.

- bbox: `[196, 247, 474, 401]`
- 표현 불가 이유: flow-screen-panel: 부유 캡슐 + 앱 화면 + 하단 설명. 사진형 card와 다른 외형이며 대응하는 명명 변형이 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<article class="screen-flow-panel"><header class="caption">…</header><div class="seat portrait" data-ph="1"></div><p class="note">…</p></article>
```

## 12-083 — replica 12

flow-screen-panel: 부유 캡슐 + 앱 화면 + 하단 설명. 사진형 card와 다른 외형이며 대응하는 명명 변형이 없다.

- bbox: `[701, 247, 474, 401]`
- 표현 불가 이유: flow-screen-panel: 부유 캡슐 + 앱 화면 + 하단 설명. 사진형 card와 다른 외형이며 대응하는 명명 변형이 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<article class="screen-flow-panel"><header class="caption">…</header><div class="seat portrait" data-ph="1"></div><p class="note">…</p></article>
```

## 13-090 — replica 13

numbered-feature-bands: 파란 제목 띠/괄호 번호/다음 행 설명 구조로, 기본 icon-list와 다른 외형이다.

- bbox: `[800, 180, 417, 471]`
- 표현 불가 이유: numbered-feature-bands: 파란 제목 띠/괄호 번호/다음 행 설명 구조로, 기본 icon-list와 다른 외형이다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<div class="feature-bands"><div class="feature"><b class="marker">1</b><b class="caption">…</b><p class="description">…</p></div></div>
```

## 14-095 — replica 14

사진/설명 띠를 함께 둘러싼 표면

- bbox: `[428, 184, 760, 460]`
- 표현 불가 이유: zoom-annotation: 큰 사진틀과 겹친 확대 원, 꺾인 연결선, 돋보기 설명 띠를 함께 소유하는 계약이 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<figure class="zoom-annotation"><div class="photo seat" data-ph="1"></div><div class="zoom seat" data-ph="2"></div><div class="connector"></div><figcaption><span class="icon"></span><p class="note">…</p></figcaption></figure>
```

## 14-097 — replica 14

확대 원형 그림과 꺾인 blue connector

- bbox: `[170, 274, 332, 318]`
- 표현 불가 이유: zoom-annotation: 큰 사진틀과 겹친 확대 원, 꺾인 연결선, 돋보기 설명 띠를 함께 소유하는 계약이 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<figure class="zoom-annotation"><div class="photo seat" data-ph="1"></div><div class="zoom seat" data-ph="2"></div><div class="connector"></div><figcaption><span class="icon"></span><p class="note">…</p></figcaption></figure>
```

## 15-102 — replica 15

중앙 그림을 비켜 놓은 강조 캡슐 제목과 기능 설명

- bbox: `[194, 265, 422, 122.59]`
- 표현 불가 이유: matrix는 두 축을 가진 사분면 또는 의미가 정해진 SWOT이다. 이 페이지는 네 개 기능 callout을 중앙 이미지 둘레에 놓은 구성으로 축/분류 의미가 없으며 matrix로 바꾸지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<section class="media-callouts"><div class="seat" data-ph="1"></div><article class="feature"><b class="caption">…</b><p class="note">…</p></article><!-- feature ×4; no invented axes --></section>
```

## 15-103 — replica 15

중앙 그림을 비켜 놓은 강조 캡슐 제목과 기능 설명

- bbox: `[763, 265, 421, 122.59]`
- 표현 불가 이유: matrix는 두 축을 가진 사분면 또는 의미가 정해진 SWOT이다. 이 페이지는 네 개 기능 callout을 중앙 이미지 둘레에 놓은 구성으로 축/분류 의미가 없으며 matrix로 바꾸지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<section class="media-callouts"><div class="seat" data-ph="1"></div><article class="feature"><b class="caption">…</b><p class="note">…</p></article><!-- feature ×4; no invented axes --></section>
```

## 15-104 — replica 15

중앙 그림을 비켜 놓은 강조 캡슐 제목과 기능 설명

- bbox: `[194, 517, 422, 122.59]`
- 표현 불가 이유: matrix는 두 축을 가진 사분면 또는 의미가 정해진 SWOT이다. 이 페이지는 네 개 기능 callout을 중앙 이미지 둘레에 놓은 구성으로 축/분류 의미가 없으며 matrix로 바꾸지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<section class="media-callouts"><div class="seat" data-ph="1"></div><article class="feature"><b class="caption">…</b><p class="note">…</p></article><!-- feature ×4; no invented axes --></section>
```

## 15-105 — replica 15

중앙 그림을 비켜 놓은 강조 캡슐 제목과 기능 설명

- bbox: `[763, 517, 421, 122.59]`
- 표현 불가 이유: matrix는 두 축을 가진 사분면 또는 의미가 정해진 SWOT이다. 이 페이지는 네 개 기능 callout을 중앙 이미지 둘레에 놓은 구성으로 축/분류 의미가 없으며 matrix로 바꾸지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<section class="media-callouts"><div class="seat" data-ph="1"></div><article class="feature"><b class="caption">…</b><p class="note">…</p></article><!-- feature ×4; no invented axes --></section>
```

## 16-112 — replica 16

folder-panel: 탭/노치와 inner caption이 있는 폴더다. photo card의 tone 또는 line 페이지 스위치로 만들 수 없다.

- bbox: `[170, 249, 336, 319]`
- 표현 불가 이유: folder-panel: 탭/노치와 inner caption이 있는 폴더다. photo card의 tone 또는 line 페이지 스위치로 만들 수 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<article class="folder-panel"><header class="tab"><span class="caption">…</span><span class="switch"></span></header><div class="content"><div class="seat" data-ph="1"></div><p class="note">…</p></div></article>
```

## 16-113 — replica 16

folder-panel: 탭/노치와 inner caption이 있는 폴더다. photo card의 tone 또는 line 페이지 스위치로 만들 수 없다.

- bbox: `[530, 249, 336, 319]`
- 표현 불가 이유: folder-panel: 탭/노치와 inner caption이 있는 폴더다. photo card의 tone 또는 line 페이지 스위치로 만들 수 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<article class="folder-panel"><header class="tab"><span class="caption">…</span><span class="switch"></span></header><div class="content"><div class="seat" data-ph="1"></div><p class="note">…</p></div></article>
```

## 16-114 — replica 16

folder-panel: 탭/노치와 inner caption이 있는 폴더다. photo card의 tone 또는 line 페이지 스위치로 만들 수 없다.

- bbox: `[890, 249, 336, 319]`
- 표현 불가 이유: folder-panel: 탭/노치와 inner caption이 있는 폴더다. photo card의 tone 또는 line 페이지 스위치로 만들 수 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<article class="folder-panel"><header class="tab"><span class="caption">…</span><span class="switch"></span></header><div class="content"><div class="seat" data-ph="1"></div><p class="note">…</p></div></article>
```

## 17-120 — replica 17

cropped-idea-hub: 원과 점선이 페이지 아래로 잘린 외형. 24 resource hub와 다르며, 슬롯 안에 모든 장식이 들어가야 하는 품질 기준과 동시에 같게 만들 수 없다.

- bbox: `[169, 248, 1056, 472]`
- 표현 불가 이유: cropped-idea-hub: 원과 점선이 페이지 아래로 잘린 외형. 24 resource hub와 다르며, 슬롯 안에 모든 장식이 들어가야 하는 품질 기준과 동시에 같게 만들 수 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<div class="clipped-radial"><div class="viewport"><div class="hub"><div class="core">…</div><div class="member">…</div><!-- all connected members owned here --></div></div></div>
```

## 18-125 — replica 18

horizontal-media-rows: 사진/파란 캡슐 제목/긴 설명/버튼이 결합한 가로 세부기능 행. list mark에는 그림을 넣을 수 없고 media-row 계약이 없다.

- bbox: `[168, 238, 1064, 423]`
- 표현 불가 이유: horizontal-media-rows: 사진/파란 캡슐 제목/긴 설명/버튼이 결합한 가로 세부기능 행. list mark에는 그림을 넣을 수 없고 media-row 계약이 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<article class="media-row"><div class="seat" data-ph="1"></div><div class="content"><b class="caption">…</b><p class="note">…</p><button class="action">…</button></div></article>
```

## 18-126 — replica 18

horizontal-media-rows: 사진/파란 캡슐 제목/긴 설명/버튼이 결합한 가로 세부기능 행. list mark에는 그림을 넣을 수 없고 media-row 계약이 없다.

- bbox: `[622, 593, 157, 42]`
- 표현 불가 이유: horizontal-media-rows: 사진/파란 캡슐 제목/긴 설명/버튼이 결합한 가로 세부기능 행. list mark에는 그림을 넣을 수 없고 media-row 계약이 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<article class="media-row"><div class="seat" data-ph="1"></div><div class="content"><b class="caption">…</b><p class="note">…</p><button class="action">…</button></div></article>
```

## 19-133 — replica 19

세 번째 인물판 오른쪽 위에 겹친 검정 추가 조작

- bbox: `[1130, 249, 46, 46]`
- 표현 불가 이유: person 계약에는 추가 조작이 없다. 마지막 자식에 의존하는 가짜 버튼을 인물 CSS에 그리지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<div class="people"><div class="person">…<button class="action" aria-label="인물 추가"></button></div></div>
```

## 20-139 — replica 20

Results 캡슐을 왼쪽에 둔 유리 요약 띠

- bbox: `[441, 536, 753, 96]`
- 표현 불가 이유: 짧은 capsule label과 두 줄 본문을 한 표면 안에 나란히 두는 summary-band 계약이 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<aside class="result-band"><b class="label">Results</b><p class="note">…</p></aside>
```

## 21-145 — replica 21

summary-to-emblem: framed icon summary rows와 이중 화살표, 그림을 담은 결과 링의 관계다. share donut 의미가 아니며 단일 연결선 소유 계약이 없다.

- bbox: `[160, 238, 761, 423]`
- 표현 불가 이유: summary-to-emblem: framed icon summary rows와 이중 화살표, 그림을 담은 결과 링의 관계다. share donut 의미가 아니며 단일 연결선 소유 계약이 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<figure class="summary-flow"><div class="summaries"><article class="summary">…</article></div><div class="connector"></div><div class="emblem"><div class="seat" data-ph="1"></div></div></figure>
```

## 21-146 — replica 21

summary-to-emblem: framed icon summary rows와 이중 화살표, 그림을 담은 결과 링의 관계다. share donut 의미가 아니며 단일 연결선 소유 계약이 없다.

- bbox: `[928, 310, 279, 279]`
- 표현 불가 이유: summary-to-emblem: framed icon summary rows와 이중 화살표, 그림을 담은 결과 링의 관계다. share donut 의미가 아니며 단일 연결선 소유 계약이 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<figure class="summary-flow"><div class="summaries"><article class="summary">…</article></div><div class="connector"></div><div class="emblem"><div class="seat" data-ph="1"></div></div></figure>
```

## 24-166 — replica 24

captioned-explanation-panel: 부유 체크 캡슐과 3줄 설명을 담는 별도 패널. 06 photo card의 명명 변형으로 볼 수 없다.

- bbox: `[212, 277, 383, 161]`
- 표현 불가 이유: captioned-explanation-panel: 부유 체크 캡슐과 3줄 설명을 담는 별도 패널. 06 photo card의 명명 변형으로 볼 수 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<article class="captioned-panel"><header class="caption"><span class="icon"></span><b class="name">…</b></header><p class="note">…</p></article>
```

## 24-167 — replica 24

captioned-explanation-panel: 부유 체크 캡슐과 3줄 설명을 담는 별도 패널. 06 photo card의 명명 변형으로 볼 수 없다.

- bbox: `[212, 469, 383, 161]`
- 표현 불가 이유: captioned-explanation-panel: 부유 체크 캡슐과 3줄 설명을 담는 별도 패널. 06 photo card의 명명 변형으로 볼 수 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<article class="captioned-panel"><header class="caption"><span class="icon"></span><b class="name">…</b></header><p class="note">…</p></article>
```

## 25-173 — replica 25

issue-resolution-rows: 두 설명 행 사이 이중 쉐브론을 포함한다. steps.col을 원형 base와 무관한 사각 미디어 행으로 바꾸지 않는다.

- bbox: `[275, 282, 849, 192.9]`
- 표현 불가 이유: issue-resolution-rows: 두 설명 행 사이 이중 쉐브론을 포함한다. steps.col을 원형 base와 무관한 사각 미디어 행으로 바꾸지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<figure class="issue-resolution"><article class="issue"><div class="seat" data-ph="1"></div><p class="note">…</p></article><div class="connector"></div><article class="resolution"><div class="seat" data-ph="2"></div><p class="note">…</p></article></figure>
```

## 25-174 — replica 25

issue-resolution-rows: 두 설명 행 사이 이중 쉐브론을 포함한다. steps.col을 원형 base와 무관한 사각 미디어 행으로 바꾸지 않는다.

- bbox: `[275, 489, 849, 143]`
- 표현 불가 이유: issue-resolution-rows: 두 설명 행 사이 이중 쉐브론을 포함한다. steps.col을 원형 base와 무관한 사각 미디어 행으로 바꾸지 않는다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<figure class="issue-resolution"><article class="issue"><div class="seat" data-ph="1"></div><p class="note">…</p></article><div class="connector"></div><article class="resolution"><div class="seat" data-ph="2"></div><p class="note">…</p></article></figure>
```

## 29-198 — replica 29

chat-exchange: 질문 캡슐/답변 상자/발화자 아이콘/읽음 표시를 함께 표현하는 대화 턴 계약이 없다.

- bbox: `[224, 266, 942, 162]`
- 표현 불가 이유: chat-exchange: 질문 캡슐/답변 상자/발화자 아이콘/읽음 표시를 함께 표현하는 대화 턴 계약이 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<div class="conversation"><article class="turn"><div class="speaker"><span class="icon"></span></div><div class="bubble"><b class="name">…</b><p class="note">…</p></div><span class="status">…</span></article></div>
```

## 29-199 — replica 29

chat-exchange: 질문 캡슐/답변 상자/발화자 아이콘/읽음 표시를 함께 표현하는 대화 턴 계약이 없다.

- bbox: `[224, 466, 942, 176]`
- 표현 불가 이유: chat-exchange: 질문 캡슐/답변 상자/발화자 아이콘/읽음 표시를 함께 표현하는 대화 턴 계약이 없다.

제안 마크업(현재 계약과 컬렉션에는 포함하지 않음):

```html
<div class="conversation"><article class="turn"><div class="speaker"><span class="icon"></span></div><div class="bubble"><b class="name">…</b><p class="note">…</p></div><span class="status">…</span></article></div>
```
