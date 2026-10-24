# cinder-pulse — unexpressible

## 1. replica 04 / metric

- bbox: `[437.0, 369.0, 772.0, 279.0]`
- 디자인: Venn core below-label dotted connector at x823 from y369 to551, and gray three-part qualitative value panel at [437,550,772,98].
- 이유: The dotted connector joins the Venn core to a three-part qualitative value panel. Neither venn.overlap nor metric can own the linked caption panel and its relationship. The panel and connector are retained together as an unexpressible relationship; no dangling decorative line is added to the Venn.

- 필요한 구조: 표면을 소유하는 KPI/qualitative panel 계약 + 그 안의 bare metric 또는 이름/note 묶음

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="stats" data-proposed-contract="metric.alternate-source-design@future"><div class="stat"><div class="parts"><p class="fig"></p><p class="name">기술 우위</p><p class="note">Technological Excellence</p></div></div><div class="stat"><div class="parts"><p class="fig"></p><p class="name">고객 중심</p><p class="note">Customer First</p></div></div><div class="stat"><div class="parts"><p class="fig"></p><p class="name">지속 가능한 혁신</p><p class="note">Sustainable Innovation</p></div></div></div>
```

## 2. replica 05 / prose

- bbox: `[468.0, 575.0, 260.0, 34.8]`
- 디자인: font="Pretendard Variable"; size=16px; weight=400; line=23.2px; track=normal; color=rgb(0, 0, 0); background=rgba(0, 0, 0, 0); border=0px none rgb(0, 0, 0); borderRadius=0px; padding=0px; gap=normal; display=block
- 이유: 본문 base와 다른 실제 타이포: size=16px (base 18px), line=23.2px (base 24.84px), color=rgb(0, 0, 0) (base rgb(85, 85, 85)). 단순 같은 prose/의미 없는 변형으로 투영하지 않음. 상위 compound가 소유한 경우 그 내부 parts로 흡수.

- 필요한 구조: {'contract': 'source-specific caption or heading inside its semantic compound', 'requiredTypography': {'size': '16px', 'weight': '400', 'line': '23.2px', 'track': 'normal', 'color': 'rgb(0, 0, 0)', 'padding': '0px'}, 'reason': '현재 prose의 base/lead/quiet/cols 의미만으로 이 별도 형태를 정확히 표현할 수 없음'}

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="prose" data-proposed-contract="prose.alternate-source-design@future"><p>미리컴퍼니 대표이사　김미리</p></div>
```

## 3. replica 05 / headline

- bbox: `[680.0, 552.0, 200.0, 101.5]`
- 디자인: font="Pretendard Variable"; size=60px; weight=400; line=87px; track=normal; color=rgb(0, 0, 0); background=rgba(0, 0, 0, 0); border=0px none rgb(0, 0, 0); borderRadius=0px; padding=0px; gap=normal; display=block
- 이유: 34px/500 gray statement base와 별도 타이포/역할이다. 대표자60px 서명은 브랜드 furniture/서명 계약으로 분리해야 함.

- 필요한 구조: {'contract': 'signature furniture', 'sourceDesign': {'font': '"Pretendard Variable"', 'size': '60px', 'weight': '400', 'line': '87px', 'track': 'normal', 'color': 'rgb(0, 0, 0)', 'background': 'rgba(0, 0, 0, 0)', 'border': '0px none rgb(0, 0, 0)', 'borderRadius': '0px', 'padding': '0px', 'gap': 'normal', 'display': 'block'}, 'reason': '해당 목적의 compact/quiet headline 변형이 현재 계약에 없음'}

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="headline" data-proposed-contract="headline.alternate-source-design@future"><h2>김미리</h2></div>
```

## 4. replica 07 / callout

- bbox: `[70.0, 567.0, 1139.0, 82.0]`
- 디자인: surface=Measured visible grouping in replica; parts=[{'bbox': [91, 586, 1099, 33.34], 'numbers': {'font': '"Pretendard Variable"', 'size': '23px', 'weight': '400', 'line': '33.35px', 'track': 'normal', 'color': 'rgb(0, 0, 0)', 'background': 'rgba(0, 0, 0, 0)', 'border': '0px none rgb(0, 0, 0)', 'borderRadius': '0px', 'padding': '0px', 'gap': 'normal', 'display': 'block'}, 'text': '지금까지 쌓아온 경험과 혁신을 바탕으로, 앞으로도 여러분과 함께 더 큰 미래를 만들어 나가겠습니다.'}]
- 이유: Original source has a centered23px/400 concluding sentence (two explicit lines on09), whereas observed base11 is a left-aligned21px sentence with a real bold lead-in. callout.sentence@1 allows inline emphasis and an optional icon but no centered alignment variant. Absence of b is not an alignment flag; changing alignment through b absence, page selectors, or an invented variant would not be a legitimate same-as projection.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<section data-proposed-contract="source-design@future">
<div class="box soft" style="left:70px;top:567px;width:1139px;height:82px"><div class="text" style="left:20px;top:18px;width:1099px;font-size:23px;font-weight:400;line-height:1.45;"><div style="text-align:center">지금까지 쌓아온 경험과 혁신을 바탕으로, 앞으로도 여러분과 함께 더 큰 미래를 만들어 나가겠습니다.</div></div></div>
</section>
```

## 5. replica 09 / callout

- bbox: `[70.0, 552.0, 1140.0, 95.0]`
- 디자인: surface=Measured visible grouping in replica; parts=[{'bbox': [91, 571, 1100, 66.69], 'numbers': {'font': '"Pretendard Variable"', 'size': '23px', 'weight': '400', 'line': '33.35px', 'track': 'normal', 'color': 'rgb(0, 0, 0)', 'background': 'rgba(0, 0, 0, 0)', 'border': '0px none rgb(0, 0, 0)', 'borderRadius': '0px', 'padding': '0px', 'gap': 'normal', 'display': 'block'}, 'text': '현재 우리는 STAGE 3 · 확장기에 있습니다.\n기술과 고객 기반을 바탕으로 글로벌 시장 확장을 본격화하는 단계'}]
- 이유: Original source has a centered23px/400 concluding sentence (two explicit lines on09), whereas observed base11 is a left-aligned21px sentence with a real bold lead-in. callout.sentence@1 allows inline emphasis and an optional icon but no centered alignment variant. Absence of b is not an alignment flag; changing alignment through b absence, page selectors, or an invented variant would not be a legitimate same-as projection.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<section data-proposed-contract="source-design@future">
<div class="box soft" style="left:70px;top:552px;width:1140px;height:95px"><div class="text" style="left:20px;top:18px;width:1100px;font-size:23px;font-weight:400;line-height:1.45;"><div style="text-align:center">현재 우리는 STAGE 3 · 확장기에 있습니다.<br>기술과 고객 기반을 바탕으로 글로벌 시장 확장을 본격화하는 단계</div></div></div>
</section>
```

## 6. replica 10 / headline

- bbox: `[437.0, 76.0, 772.0, 30.0]`
- 디자인: surface=Measured visible grouping in replica; parts=[{'bbox': [437, 76, 700, 31.89], 'numbers': {'font': '"Pretendard Variable"', 'size': '22px', 'weight': '400', 'line': '31.9px', 'track': 'normal', 'color': 'rgb(0, 0, 0)', 'background': 'rgba(0, 0, 0, 0)', 'border': '0px none rgb(0, 0, 0)', 'borderRadius': '0px', 'padding': '0px', 'gap': 'normal', 'display': 'block'}, 'text': '연도별 성장 추이 콤보차트'}]
- 이유: 34px/500 gray statement base와 별도 타이포/역할이다. 22px chart caption 또는23px partner heading은 크기·굵기·역할이 다른데 headline의 big/center/on 의미와 맞지 않으므로 같은 base로 간주하지 않음.

- 필요한 구조: {'contract': 'compact chart caption / partner subsection heading', 'sourceDesign': {'surface': 'Measured visible grouping in replica', 'parts': [{'bbox': [437, 76, 700, 31.89], 'numbers': {'font': '"Pretendard Variable"', 'size': '22px', 'weight': '400', 'line': '31.9px', 'track': 'normal', 'color': 'rgb(0, 0, 0)', 'background': 'rgba(0, 0, 0, 0)', 'border': '0px none rgb(0, 0, 0)', 'borderRadius': '0px', 'padding': '0px', 'gap': 'normal', 'display': 'block'}, 'text': '연도별 성장 추이 콤보차트'}]}, 'reason': '해당 목적의 compact/quiet headline 변형이 현재 계약에 없음'}

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="headline" data-proposed-contract="headline.alternate-source-design@future"><h2>연도별 성장 추이 콤보차트</h2></div>
```

## 7. replica 10 / headline

- bbox: `[437.0, 389.0, 772.0, 31.0]`
- 디자인: surface=Measured visible grouping in replica; parts=[{'bbox': [437, 389, 700, 31.89], 'numbers': {'font': '"Pretendard Variable"', 'size': '22px', 'weight': '400', 'line': '31.9px', 'track': 'normal', 'color': 'rgb(0, 0, 0)', 'background': 'rgba(0, 0, 0, 0)', 'border': '0px none rgb(0, 0, 0)', 'borderRadius': '0px', 'padding': '0px', 'gap': 'normal', 'display': 'block'}, 'text': '사업 영역별 매출 비중 표'}]
- 이유: 34px/500 gray statement base와 별도 타이포/역할이다. 22px chart caption 또는23px partner heading은 크기·굵기·역할이 다른데 headline의 big/center/on 의미와 맞지 않으므로 같은 base로 간주하지 않음.

- 필요한 구조: {'contract': 'compact chart caption / partner subsection heading', 'sourceDesign': {'surface': 'Measured visible grouping in replica', 'parts': [{'bbox': [437, 389, 700, 31.89], 'numbers': {'font': '"Pretendard Variable"', 'size': '22px', 'weight': '400', 'line': '31.9px', 'track': 'normal', 'color': 'rgb(0, 0, 0)', 'background': 'rgba(0, 0, 0, 0)', 'border': '0px none rgb(0, 0, 0)', 'borderRadius': '0px', 'padding': '0px', 'gap': 'normal', 'display': 'block'}, 'text': '사업 영역별 매출 비중 표'}]}, 'reason': '해당 목적의 compact/quiet headline 변형이 현재 계약에 없음'}

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="headline" data-proposed-contract="headline.alternate-source-design@future"><h2>사업 영역별 매출 비중 표</h2></div>
```

## 8. replica 10 / prose

- bbox: `[445.0, 259.0, 30.0, 17.39]`
- 디자인: font="Pretendard Variable"; size=12px; weight=400; line=17.4px; track=normal; color=rgb(85, 85, 85); background=rgba(0, 0, 0, 0); border=0px none rgb(85, 85, 85); borderRadius=0px; padding=0px; gap=normal; display=block
- 이유: 본문 base와 다른 실제 타이포: size=12px (base 18px), line=17.4px (base 24.84px). 단순 같은 prose/의미 없는 변형으로 투영하지 않음. 상위 compound가 소유한 경우 그 내부 parts로 흡수.

- 필요한 구조: {'contract': 'source-specific caption or heading inside its semantic compound', 'requiredTypography': {'size': '12px', 'weight': '400', 'line': '17.4px', 'track': 'normal', 'color': 'rgb(85, 85, 85)', 'padding': '0px'}, 'reason': '현재 prose의 base/lead/quiet/cols 의미만으로 이 별도 형태를 정확히 표현할 수 없음'}

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="prose" data-proposed-contract="prose.alternate-source-design@future"><p>100</p></div>
```

## 9. replica 10 / prose

- bbox: `[445.0, 224.0, 30.0, 17.39]`
- 디자인: font="Pretendard Variable"; size=12px; weight=400; line=17.4px; track=normal; color=rgb(85, 85, 85); background=rgba(0, 0, 0, 0); border=0px none rgb(85, 85, 85); borderRadius=0px; padding=0px; gap=normal; display=block
- 이유: 본문 base와 다른 실제 타이포: size=12px (base 18px), line=17.4px (base 24.84px). 단순 같은 prose/의미 없는 변형으로 투영하지 않음. 상위 compound가 소유한 경우 그 내부 parts로 흡수.

- 필요한 구조: {'contract': 'source-specific caption or heading inside its semantic compound', 'requiredTypography': {'size': '12px', 'weight': '400', 'line': '17.4px', 'track': 'normal', 'color': 'rgb(85, 85, 85)', 'padding': '0px'}, 'reason': '현재 prose의 base/lead/quiet/cols 의미만으로 이 별도 형태를 정확히 표현할 수 없음'}

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="prose" data-proposed-contract="prose.alternate-source-design@future"><p>200</p></div>
```

## 10. replica 12 / list

- bbox: `[615.0, 204.0, 594.0, 349.0]`
- 디자인: 회색 외곽 판+무표식 3개 상단 행+4개 bullet 흰 행은 단일 list 계약의 동일 item 문법이 아니다. 판/상단 행을 억지 레이아웃 변형으로 만들지 않는다.
- 이유: 회색 외곽 판+무표식 3개 상단 행+4개 bullet 흰 행은 단일 list 계약의 동일 item 문법이 아니다. 판/상단 행을 억지 레이아웃 변형으로 만들지 않는다.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="list" data-proposed-contract="list.alternate-source-design@future"><div class="item"><p class="name">Miri Intelligence</p><p class="note"></p></div><div class="item"><p class="name">|　독자 개발한 고성능 AI 예측 알고리즘 기술</p><p class="note"></p></div><div class="item"><p class="name">Miri Cloud</p><p class="note"></p></div><div class="item"><p class="name">|　대용량 데이터를 유연하게 처리하는 클라우드 인프라</p><p class="note"></p></div><div class="item"><p class="name">DX Consulting</p><p class="note"></p></div><div class="item"><p class="name">|　각 산업 분야별 도메인 전문성과기획 역량</p><p class="note"></p></div><div class="item"><p class="name">교집합 A　　　클라우드 환경에서 즉시 동작하는 AI SaaS 모델 구축</p><p class="note"></p></div><div class="item"><p class="name">교집합 B　　　기업 맞춤형 클라우드 데이터 파이프라인 구현</p><p class="note"></p></div><div class="item"><p class="name">교집합 C　　　해당 교집합에 해당하는 내용을 적어주세요</p><p class="note"></p></div><div class="item"><p class="name">교집합 D　　　고객 맞춤형 데이터 생태계 구축 및 자동화 완성</p><p class="note"></p></div></div>
```

## 11. replica 12 / callout

- bbox: `[615.0, 566.0, 594.0, 83.0]`
- 디자인: surface=Measured visible grouping in replica; parts=[{'bbox': [636, 585, 554, 33.34], 'numbers': {'font': '"Pretendard Variable"', 'size': '23px', 'weight': '400', 'line': '33.35px', 'track': 'normal', 'color': 'rgb(0, 0, 0)', 'background': 'rgba(0, 0, 0, 0)', 'border': '0px none rgb(0, 0, 0)', 'borderRadius': '0px', 'padding': '0px', 'gap': 'normal', 'display': 'block'}, 'text': '사업은 나뉘어 있지만 역량은 하나로 모입니다.'}]
- 이유: Original source has a centered23px/400 concluding sentence (two explicit lines on09), whereas observed base11 is a left-aligned21px sentence with a real bold lead-in. callout.sentence@1 allows inline emphasis and an optional icon but no centered alignment variant. Absence of b is not an alignment flag; changing alignment through b absence, page selectors, or an invented variant would not be a legitimate same-as projection.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<section data-proposed-contract="source-design@future">
<div class="box soft" style="left:615px;top:566px;width:594px;height:83px"><div class="text" style="left:20px;top:18px;width:554px;font-size:23px;font-weight:400;line-height:1.45;"><div style="text-align:center">사업은 나뉘어 있지만 역량은 하나로 모입니다.</div></div></div>
</section>
```

## 12. replica 13 / card

- bbox: `[437.0, 72.0, 772.0, 281.0]`
- 디자인: 사업 카드의 성과 띠/프로세스 카드의 별도 접속 구조는 제품카드 base와 다른 시각 계열이다. 무의미한 계약변형이나 페이지조건으로 숨기지 않고 판단 요청.
- 이유: 사업 카드의 성과 띠/프로세스 카드의 별도 접속 구조는 제품카드 base와 다른 시각 계열이다. 무의미한 계약변형이나 페이지조건으로 숨기지 않고 현 계약으로는 표현하지 않습니다.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="card" data-proposed-contract="card.alternate-source-design@future"><div class="parts"><p class="name">주력 사업 1.　Miri Intelligence</p><p class="note">기업 내 유기적으로 흩어져 있는 비정형 데이터를 실시간으로 수집하고 분석하는 AI 솔루션입니다. 고도화된 예측 알고리즘을 통해 의사결정 시간을 70% 이상 단축시킵니다.<br>주요 서비스　　　AI 데이터 분석, 실시간 이상 탐지, 미래 매출 예측 모델<br>주요 성과<br>프로젝트<br>180건<br>고객<br>120개 사</p></div></div>
```

## 13. replica 13 / card

- bbox: `[437.0, 367.0, 772.0, 281.0]`
- 디자인: 사업 카드의 성과 띠/프로세스 카드의 별도 접속 구조는 제품카드 base와 다른 시각 계열이다. 무의미한 계약변형이나 페이지조건으로 숨기지 않고 판단 요청.
- 이유: 사업 카드의 성과 띠/프로세스 카드의 별도 접속 구조는 제품카드 base와 다른 시각 계열이다. 무의미한 계약변형이나 페이지조건으로 숨기지 않고 현 계약으로는 표현하지 않습니다.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="card" data-proposed-contract="card.alternate-source-design@future"><div class="parts"><p class="name">주력 사업 2.　Miri Cloud</p><p class="note">초기 구축 비용 부담 없이 월 구독 형태로 이용할 수 있는 보안 특화 클라우드 플랫폼입니다. 엔터프라이즈급 보안 환경을 바탕으로 데이터 시각화 리포트를 제공합니다.<br>주요 서비스　　　SaaS 데이터 스토리지, Auto-DashBoard, 데이터 암호화<br>주요 성과<br>프로젝트<br>95건<br>고객<br>85개 사</p></div></div>
```

## 14. replica 18 / metric

- bbox: `[70.0, 204.0, 291.0, 287.0]`
- 디자인: 04는 숫자가 없는 회색3분할 가치판,18 전체는 제목/회색 판을 포함한 KPI 카드다. bare figure 계약이 판을 소유할 수 없어 판틀과 내부 수치를 분리한다.
- 이유: 04는 숫자가 없는 회색3분할 가치판,18 전체는 제목/회색 판을 포함한 KPI 카드다. bare figure 계약이 판을 소유할 수 없어 판틀과 내부 수치를 분리한다.

- 필요한 구조: 표면을 소유하는 KPI/qualitative panel 계약 + 그 안의 bare metric 또는 이름/note 묶음

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="stats" data-proposed-contract="metric.alternate-source-design@future"><div class="stat"><div class="parts"><p class="fig">320건</p><p class="name">프로젝트</p><p class="note"></p></div></div><div class="stat"><div class="parts"><p class="fig">210개 사</p><p class="name">고객사</p><p class="note"></p></div></div><div class="stat"><div class="parts"><p class="fig">94%</p><p class="name">재계약률</p><p class="note"></p></div></div></div>
```

## 15. replica 18 / list

- bbox: `[70.0, 505.0, 1140.0, 143.0]`
- 디자인: 3개 제목+두줄 설명은 marker가 없는3열 파트너 판이며 list가 아니다. 회색 공유 판은 별도소유계약필요, 내부3개 headline은 분리지원.
- 이유: 3개 제목+두줄 설명은 marker가 없는3열 파트너 판이며 list가 아니다. 회색 공유 판은 별도소유계약필요, 내부3개 headline은 분리지원.

- 필요한 구조: 회색 중성 판에3개의 독립 heading+support paragraph를 놓는 panel/group 계약

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="list" data-proposed-contract="list.alternate-source-design@future"><div class="item"><p class="name">기술 파트너</p><p class="note"></p></div><div class="item"><p class="name">미리테크 : 공식 클라우드 MSP</p><p class="note"></p></div><div class="item"><p class="name">미리클라우드 : AI 기술 협력</p><p class="note"></p></div><div class="item"><p class="name">유통·판매 파트너</p><p class="note"></p></div><div class="item"><p class="name">미리솔루션</p><p class="note"></p></div><div class="item"><p class="name">미리시스템 : 엔터프라이즈 솔루션 총판 계약</p><p class="note"></p></div><div class="item"><p class="name">연구·기관 협력</p><p class="note"></p></div><div class="item"><p class="name">미리대학교 AI 연구원 산학 협력</p><p class="note"></p></div><div class="item"><p class="name">미리기술연구원 공동 연구</p><p class="note"></p></div></div>
```

## 16. replica 18 / prose

- bbox: `[591.0, 228.0, 220.0, 31.89]`
- 디자인: font="Pretendard Variable"; size=22px; weight=400; line=31.9px; track=normal; color=rgb(0, 0, 0); background=rgba(0, 0, 0, 0); border=0px none rgb(0, 0, 0); borderRadius=0px; padding=0px; gap=normal; display=block
- 이유: 본문 base와 다른 실제 타이포: size=22px (base 18px), line=31.9px (base 24.84px), color=rgb(0, 0, 0) (base rgb(85, 85, 85)). 단순 같은 prose/의미 없는 변형으로 투영하지 않음. 상위 compound가 소유한 경우 그 내부 parts로 흡수.

- 필요한 구조: {'contract': 'source-specific caption or heading inside its semantic compound', 'requiredTypography': {'size': '22px', 'weight': '400', 'line': '31.9px', 'track': 'normal', 'color': 'rgb(0, 0, 0)', 'padding': '0px'}, 'reason': '현재 prose의 base/lead/quiet/cols 의미만으로 이 별도 형태를 정확히 표현할 수 없음'}

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="prose" data-proposed-contract="prose.alternate-source-design@future"><p>주요 고객사</p></div>
```

## 17. replica 18 / prose

- bbox: `[990.0, 228.0, 220.0, 31.89]`
- 디자인: font="Pretendard Variable"; size=22px; weight=400; line=31.9px; track=normal; color=rgb(0, 0, 0); background=rgba(0, 0, 0, 0); border=0px none rgb(0, 0, 0); borderRadius=0px; padding=0px; gap=normal; display=block
- 이유: 본문 base와 다른 실제 타이포: size=22px (base 18px), line=31.9px (base 24.84px), color=rgb(0, 0, 0) (base rgb(85, 85, 85)). 단순 같은 prose/의미 없는 변형으로 투영하지 않음. 상위 compound가 소유한 경우 그 내부 parts로 흡수.

- 필요한 구조: {'contract': 'source-specific caption or heading inside its semantic compound', 'requiredTypography': {'size': '22px', 'weight': '400', 'line': '31.9px', 'track': 'normal', 'color': 'rgb(0, 0, 0)', 'padding': '0px'}, 'reason': '현재 prose의 base/lead/quiet/cols 의미만으로 이 별도 형태를 정확히 표현할 수 없음'}

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="prose" data-proposed-contract="prose.alternate-source-design@future"><p>대표 구축 사례</p></div>
```

## 18. replica 18 / prose

- bbox: `[948.0, 309.0, 232.0, 31.89]`
- 디자인: font="Pretendard Variable"; size=22px; weight=600; line=31.9px; track=normal; color=rgb(85, 85, 85); background=rgba(0, 0, 0, 0); border=0px none rgb(85, 85, 85); borderRadius=0px; padding=0px; gap=normal; display=block
- 이유: 본문 base와 다른 실제 타이포: size=22px (base 18px), weight=600 (base 400), line=31.9px (base 24.84px). 단순 같은 prose/의미 없는 변형으로 투영하지 않음. 상위 compound가 소유한 경우 그 내부 parts로 흡수.

- 필요한 구조: {'contract': 'source-specific caption or heading inside its semantic compound', 'requiredTypography': {'size': '22px', 'weight': '600', 'line': '31.9px', 'track': 'normal', 'color': 'rgb(85, 85, 85)', 'padding': '0px'}, 'reason': '현재 prose의 base/lead/quiet/cols 의미만으로 이 별도 형태를 정확히 표현할 수 없음'}

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="prose" data-proposed-contract="prose.alternate-source-design@future"><p>Miri Tech</p></div>
```

## 19. replica 10 / table

- bbox: `[437.0, 427.0, 772.0, 225.56]`
- 디자인: Same straight-rule zebra table with accent header, four business rows and four columns.
- 이유: Source10 uses a fully accent-coloured 20px header and alternating body rows; source06 has a neutral 16px header and only the final row shaded. Header presence is a genuine structural condition, but row count does not mean emphasis or zebra styling. table.grid@1 has no named header/zebra variant; .pick denotes a focal column rather than a new full-table scene.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="tablebox" data-proposed-contract="table.alternate-source-design@future"><table class="table"><thead><tr><th>사업 영역</th><th>주요 서비스</th><th>매출 비중</th><th>고객사 수</th></tr></thead><tbody><tr><td>Miri Intelligence</td><td>AI 플랫폼·예측 솔루션</td><td>45%</td><td>120개사</td></tr><tr><td>Miri Cloud</td><td>SaaS·클라우드 스토리지</td><td>30%</td><td>85개사</td></tr><tr><td>DX Consulting</td><td>데이터 파이프라인·DX 자문</td><td>15%</td><td>32개사</td></tr><tr><td>M&amp;O</td><td>24/7 유지보수·AI 튜닝</td><td>10%</td><td>210개사(유지)</td></tr></tbody></table></div>
```

## 20. replica 19 / timeline

- bbox: `[440.0, 72.0, 769.0, 576.0]`
- 디자인: Three rising quiet columns of widths249px, x440/700/960; step tabs y248/160/72, full column bottom648; orange top strips and white content field.
- 이유: Chronological periods2026/2027–2028/2029–2030 make this a stair timeline. It is a second visual timeline from horizontal history07 and cannot be selected by page/content or fake .alt/.col.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<section data-proposed-contract="timeline.source-extension@future">
  <header>제목·범주</header>
  <div class="members">단계·노드·항목과 실제 데이터</div>
  <div class="connections" aria-hidden="true"></div>
</section>
```

## 21. replica 17 / cycle

- bbox: `[182.0, 227.0, 916.0, 402.0]`
- 디자인: Four paired strength members around192px orange core, 92px circle icon nodes and255×120 outside quiet panels; same paired-circle/panel design family as service cycle, with genuine4vs6 member geometry.
- 이유: Static retention drivers around a KPI form a hub relation, not the six-step service-cycle base15. Center-aligned regular titles/notes, darker icon-only discs and a404px dashed orbit are independent source design differences; node count alone does not semantically determine them. The existing hub base11 also has four members, so no honest count-only or named contract variant distinguishes this second hub composition.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="cycle" data-proposed-contract="cycle.alternate-source-design@future" style="grid-column:1 / span 12; grid-row:1 / span 6"><div class="core">재계약률<br><b>94%</b></div><div class="node"><span><span class="icon" data-icon="globe"></span></span><b>기술력</b><p>독자 개발 AI 특허 34건 보유<br>고도화된 데이터 처리 품질 확보</p></div><div class="node"><span><span class="icon" data-icon="globe"></span></span><b>전문 인력</b><p>석·박사급 전문 엔지니어 85명<br>안정적 기술의 전문 조직</p></div><div class="node"><span><span class="icon" data-icon="globe"></span></span><b>사후 지원</b><p>24시간 실시간 모니터링<br>주기적인 AI 모델 업데이트</p></div><div class="node"><span><span class="icon" data-icon="globe"></span></span><b>검증된 실적</b><p>누적 프로젝트 300건 이상<br>다양한 산업 경험 축적</p></div></div>
```

## 22. replica 08 / hub

- bbox: `[450.0, 80.0, 750.0, 570.0]`
- 디자인: Orange pentagonal MIRI PEOPLE core inside a five-sided thin outline; five radial title capsules and three-line notes.
- 이유: A pentagonal five-direction culture hub is a second hub design. hub.spokes has no root variant for this change; do not select it by member count/text or attach a page-specific class.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<section data-proposed-contract="hub.source-extension@future">
  <header>제목·범주</header>
  <div class="members">단계·노드·항목과 실제 데이터</div>
  <div class="connections" aria-hidden="true"></div>
</section>
```

## 23. replica 12 / venn

- bbox: `[100.0, 209.0, 465.0, 438.0]`
- 디자인: Three overlapping gray circles; separate A/B/C pairwise intersection labels and central D orange triple intersection.
- 이유: Venn contract has two/three .set names and at most one .core. It cannot encode all three pairwise intersection labels A/B/C plus triple label D as independent data without inventing classes or embedding text in CSS.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<section data-proposed-contract="venn.source-extension@future">
  <header>제목·범주</header>
  <div class="members">단계·노드·항목과 실제 데이터</div>
  <div class="connections" aria-hidden="true"></div>
</section>
```
