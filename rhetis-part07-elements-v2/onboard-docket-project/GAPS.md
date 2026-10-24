# Unexpressible

## 04-076 · page 04

본문 그리드 위로125px 뻗는400×608 인물 사진

foundation.body는y237..657이며 이 사진은y112..720이다. 계약의frame을본문정수그리드에배치해서는원래경계와크기를보존할수없다.

Proposed markup (not admitted by the current contract):
```html
<div class="page"><div class="portrait-bleed"><div class="seat portrait" data-ph="1"></div></div><header class="head">…</header><div class="body">…</div></div>
```

## 06-083 · page 06

3색 ring과 중앙3갈래 분기 및 외부 leader

donut은 한 share이며 cycle은3–6개 node와 core를 가진다. 세 조각 ring+외부 leader는 어느 구조와도 일치하지 않는다.

Proposed markup (not admitted by the current contract):
```html
<div class="split-ring"><div class="ring"><div class="segment" style="--v:33.333"><span class="name">업무 기준</span></div><div class="segment" style="--v:33.333"><span class="name">업무 기준</span></div><div class="segment" style="--v:33.333"><span class="name">업무 기준</span></div></div><div class="core"><span class="icon" data-icon="git-fork"></span></div><div class="annotations"><span class="label">접수 분류</span><span class="label">승인 이력</span><span class="label">후속 점검</span></div></div>
```

## 08-089 · page 08

아이콘과 이름을 담은 삼각 배치의3원·흰색 분리 틈

venn.set 구조는 name만 허용하며 원마다 icon을 담는 mark 부품이 없다. 아이콘을 빼거나 가짜 class를 추가하지 않는다.

Proposed markup (not admitted by the current contract):
```html
<div class="icon-sets"><section class="set"><span class="icon" data-icon="globe"></span><p class="name">운영 기준</p></section><section class="set"><span class="icon" data-icon="file-check"></span><p class="name">운영 기준</p></section><section class="set"><span class="icon" data-icon="lightbulb"></span><p class="name">운영 기준</p></section></div>
```

## 09-093 · page 09

CEO·COO/CFO와5개 부서/3팀의 조직 트리

hierarchy의 branch 수는2–4이며 이 원본은 두 경영층과5개 부서로 이루어진다. 다른 중간 root를 억지로 더하지 않는다.

Proposed markup (not admitted by the current contract):
```html
<div class="executive-org"><div class="root">총괄 책임자</div><div class="executives"><div>고객 운영</div><div>기술 운영</div></div><div class="departments"><section class="department"><h3>담당 조직</h3><ul><li>접수 분류</li><li>승인 검토</li><li>품질 점검</li></ul></section><section class="department"><h3>담당 조직</h3><ul><li>접수 분류</li><li>승인 검토</li><li>품질 점검</li></ul></section><section class="department"><h3>담당 조직</h3><ul><li>접수 분류</li><li>승인 검토</li><li>품질 점검</li></ul></section><section class="department"><h3>담당 조직</h3><ul><li>접수 분류</li><li>승인 검토</li><li>품질 점검</li></ul></section><section class="department"><h3>담당 조직</h3><ul><li>접수 분류</li><li>승인 검토</li><li>품질 점검</li></ul></section></div></div>
```

## 11-096 · page 11

1119×54px 세 카드 묶음을 제목 짓는 강조 띠

페이지 결론 문장이 아니라 여러 카드를 담는 패널 머리글이다. callout을 panel header인 척 사용하지 않는다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="list divided" data-el="onboard-docket-list"><div class="item"><p class="name">담당자 협의</p><p class="note">승인 근거를 기록합니다.</p></div><div class="item"><p class="name">담당 조직 확인</p><p class="note">이관 근거를 대조합니다.</p></div></div></div></section>
```

## 13-107 · page 13

하단으로 잘리는 반원 ring 위4개 아이콘 원과 외부 제목·번호·설명

hub는 core에서 뻗는 spokes이며 이 구조는 반원 track의4개 point와 바깥 주석이다. 어느 contract도 이러한 track/annotation 구조를 제공하지 않는다.

Proposed markup (not admitted by the current contract):
```html
<div class="semicircle-track"><div class="track"></div><div class="core"><p class="name">운영 원칙</p></div><section class="point" style="--at:0"><span class="icon" data-icon="shield-check"></span><div class="annotation"><p class="name">검토 항목</p><p class="note">담당 부서와 승인 근거를 확인합니다.</p></div></section><section class="point" style="--at:33"><span class="icon" data-icon="shield-check"></span><div class="annotation"><p class="name">검토 항목</p><p class="note">담당 부서와 승인 근거를 확인합니다.</p></div></section><section class="point" style="--at:66"><span class="icon" data-icon="shield-check"></span><div class="annotation"><p class="name">검토 항목</p><p class="note">담당 부서와 승인 근거를 확인합니다.</p></div></section><section class="point" style="--at:100"><span class="icon" data-icon="shield-check"></span><div class="annotation"><p class="name">검토 항목</p><p class="note">담당 부서와 승인 근거를 확인합니다.</p></div></section></div>
```

## 14-108 · page 14

211px 원4개의 중첩, 둘레 캡슐, 각 원 아래 점선 leader/이름

venn은2–3집합의 포함/교집합이며 이 그림은4개 키워드 원의 나열이다. steps에는 원 안 kick/name과 원 밖 label을 함께 담는 부품이 없다.

Proposed markup (not admitted by the current contract):
```html
<div class="topic-chain"><div class="outline"></div><section class="topic"><p class="kick">SERVICE VALUE</p><p class="name">안정적인 응답</p><div class="leader"></div><p class="label">검토 범주</p></section><section class="topic"><p class="kick">SERVICE VALUE</p><p class="name">안정적인 응답</p><div class="leader"></div><p class="label">검토 범주</p></section><section class="topic"><p class="kick">SERVICE VALUE</p><p class="name">안정적인 응답</p><div class="leader"></div><p class="label">검토 범주</p></section><section class="topic"><p class="kick">SERVICE VALUE</p><p class="name">안정적인 응답</p><div class="leader"></div><p class="label">검토 범주</p></section></div>
```

## 16-114 · page 16

266×53px 상단만 둥근 탭

다른 요소를 담는 panel의 header/tab은 list나card 부품이 아니다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="list divided" data-el="onboard-docket-list"><div class="item"><p class="name">담당자 협의</p><p class="note">승인 근거를 기록합니다.</p></div><div class="item"><p class="name">담당 조직 확인</p><p class="note">이관 근거를 대조합니다.</p></div></div></div></section>
```

## 16-115 · page 16

306×324px 둥근 목록 패널의 면·흰 테두리·그림자

list는 목록이며 panel surface를 별도 감싸는 계약이 없다. generic card로 list를 담아 panel인 척하지 않는다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="list divided" data-el="onboard-docket-list"><div class="item"><p class="name">담당자 협의</p><p class="note">승인 근거를 기록합니다.</p></div><div class="item"><p class="name">담당 조직 확인</p><p class="note">이관 근거를 대조합니다.</p></div></div></div></section>
```

## 16-117 · page 16

266×53px 상단만 둥근 탭

다른 요소를 담는 panel의 header/tab은 list나card 부품이 아니다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="list divided" data-el="onboard-docket-list"><div class="item"><p class="name">담당자 협의</p><p class="note">승인 근거를 기록합니다.</p></div><div class="item"><p class="name">담당 조직 확인</p><p class="note">이관 근거를 대조합니다.</p></div></div></div></section>
```

## 16-118 · page 16

306×324px 둥근 목록 패널의 면·흰 테두리·그림자

list는 목록이며 panel surface를 별도 감싸는 계약이 없다. generic card로 list를 담아 panel인 척하지 않는다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="list divided" data-el="onboard-docket-list"><div class="item"><p class="name">담당자 협의</p><p class="note">승인 근거를 기록합니다.</p></div><div class="item"><p class="name">담당 조직 확인</p><p class="note">이관 근거를 대조합니다.</p></div></div></div></section>
```

## 16-120 · page 16

266×53px 상단만 둥근 탭

다른 요소를 담는 panel의 header/tab은 list나card 부품이 아니다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="list divided" data-el="onboard-docket-list"><div class="item"><p class="name">담당자 협의</p><p class="note">승인 근거를 기록합니다.</p></div><div class="item"><p class="name">담당 조직 확인</p><p class="note">이관 근거를 대조합니다.</p></div></div></div></section>
```

## 16-121 · page 16

306×324px 둥근 목록 패널의 면·흰 테두리·그림자

list는 목록이며 panel surface를 별도 감싸는 계약이 없다. generic card로 list를 담아 panel인 척하지 않는다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="list divided" data-el="onboard-docket-list"><div class="item"><p class="name">담당자 협의</p><p class="note">승인 근거를 기록합니다.</p></div><div class="item"><p class="name">담당 조직 확인</p><p class="note">이관 근거를 대조합니다.</p></div></div></div></section>
```

## 17-123 · page 17

290×137px 사업명 강조 헤더 면

옆의 여러 metric을 제목 짓는 패널 면이며 standalone one-line pill이나 sentence callout과 의미가 다르다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="group"><div class="stat" data-el="onboard-docket-metric"><div class="parts"><p class="name">접수 건수</p><p class="fig">287</p></div></div></div></div></section>
```

## 17-124 · page 17

807×137px 여러 지표를 담는 회색 패널

metric은 bare figure 계약이다. 패널 면을 metric CSS에 숨겨 추가하지 않는다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="group"><div class="stat" data-el="onboard-docket-metric"><div class="parts"><p class="name">접수 건수</p><p class="fig">287</p></div></div></div></div></section>
```

## 17-126 · page 17

290×137px 사업명 강조 헤더 면

옆의 여러 metric을 제목 짓는 패널 면이며 standalone one-line pill이나 sentence callout과 의미가 다르다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="group"><div class="stat" data-el="onboard-docket-metric"><div class="parts"><p class="name">접수 건수</p><p class="fig">287</p></div></div></div></div></section>
```

## 17-127 · page 17

807×137px 여러 지표를 담는 회색 패널

metric은 bare figure 계약이다. 패널 면을 metric CSS에 숨겨 추가하지 않는다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="group"><div class="stat" data-el="onboard-docket-metric"><div class="parts"><p class="name">접수 건수</p><p class="fig">287</p></div></div></div></div></section>
```

## 17-129 · page 17

290×137px 사업명 강조 헤더 면

옆의 여러 metric을 제목 짓는 패널 면이며 standalone one-line pill이나 sentence callout과 의미가 다르다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="group"><div class="stat" data-el="onboard-docket-metric"><div class="parts"><p class="name">접수 건수</p><p class="fig">287</p></div></div></div></div></section>
```

## 17-130 · page 17

807×137px 여러 지표를 담는 회색 패널

metric은 bare figure 계약이다. 패널 면을 metric CSS에 숨겨 추가하지 않는다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="group"><div class="stat" data-el="onboard-docket-metric"><div class="parts"><p class="name">접수 건수</p><p class="fig">287</p></div></div></div></div></section>
```

## 19-136 · page 19

108×397px 세로 이미지 묶음 헤더

표나 chart의 axis가 아니며 사진 세 개를 제목 짓는 세로 panel header 계약이 없다.

Proposed markup (not admitted by the current contract):
```html
<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content"><div class="list divided" data-el="onboard-docket-list"><div class="item"><p class="name">담당자 협의</p><p class="note">승인 근거를 기록합니다.</p></div><div class="item"><p class="name">담당 조직 확인</p><p class="note">이관 근거를 대조합니다.</p></div></div></div></section>
```