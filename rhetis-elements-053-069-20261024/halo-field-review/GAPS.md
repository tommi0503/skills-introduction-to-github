# halo-field — unexpressible

## 1. replica 04 / prose

- bbox: `[498.66, 626.0, 689.34, 20.0]`
- 디자인: font="Pretendard Variable"; size=12px; weight=400; line=16.8px; track=normal; color=rgb(85, 88, 90); background=rgba(0, 0, 0, 0); border=0px none rgb(85, 88, 90); borderRadius=0px; padding=0px; gap=normal; display=block
- 이유: 본문 base와 다른 실제 타이포: size=12px (base 22px), line=16.8px (base 29.7px), color=rgb(85, 88, 90) (base rgb(7, 11, 9)), padding=0px (base 24px 0px 0px). 단순 같은 prose/의미 없는 변형으로 투영하지 않음. 상위 compound가 소유한 경우 그 내부 parts로 흡수.

- 필요한 구조: {'contract': 'source-specific caption or heading inside its semantic compound', 'requiredTypography': {'size': '12px', 'weight': '400', 'line': '16.8px', 'track': 'normal', 'color': 'rgb(85, 88, 90)', 'padding': '0px'}, 'reason': '현재 prose의 base/lead/quiet/cols 의미만으로 이 별도 형태를 정확히 표현할 수 없음'}

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="prose quiet" data-proposed-contract="prose.alternate-source-design@future"><p>* 최근 3개년 마케팅 데이터 및 2026년 예상 성과 지표 기준</p></div>
```

## 2. replica 07 / card

- bbox: `[54.0, 269.0, 572.0, 186.5]`
- 디자인: font="Pretendard Variable"; size=20px; weight=400; line=28px; track=normal; color=rgb(7, 11, 9); background=rgb(255, 255, 255); border=1px solid rgba(0, 0, 0, 0); borderRadius=18px; padding=28px; gap=normal; display=block
- 이유: 07은 가로로 넓은2×2 운영 역량 타일이며 번호·제목·설명과 우측 큰 아이콘으로 구성된다. 05의 세로 목표 카드와 같은.semantic.on/quiet/line로 표현할 의미 차이가 아니라 별도 구조 차이다.

- 필요한 구조: 가로 역량 타일 계약: 왼쪽 번호/제목/한줄 설명 + 독립 우측 아이콘 슬롯; 네 타일을2×2로 묶는 소유 root

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="card" data-proposed-contract="card.alternate-source-design@future"><div class="parts"><p class="kick">01</p><p class="name">맞춤형 전략 수립</p><p class="note">정밀한 데이터 분석 기반의 미디어 믹스 설계</p><span class="mark"><span class="icon" data-icon="sprout"></span></span></div></div>
```

## 3. replica 07 / card

- bbox: `[654.0, 269.0, 572.0, 186.5]`
- 디자인: font="Pretendard Variable"; size=20px; weight=400; line=28px; track=normal; color=rgb(7, 11, 9); background=rgb(255, 255, 255); border=1px solid rgba(0, 0, 0, 0); borderRadius=18px; padding=28px; gap=normal; display=block
- 이유: 07은 가로로 넓은2×2 운영 역량 타일이며 번호·제목·설명과 우측 큰 아이콘으로 구성된다. 05의 세로 목표 카드와 같은.semantic.on/quiet/line로 표현할 의미 차이가 아니라 별도 구조 차이다.

- 필요한 구조: 가로 역량 타일 계약: 왼쪽 번호/제목/한줄 설명 + 독립 우측 아이콘 슬롯; 네 타일을2×2로 묶는 소유 root

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="card" data-proposed-contract="card.alternate-source-design@future"><div class="parts"><p class="kick">02</p><p class="name">실무 중심 실행</p><p class="note">검증된 채널과 매체를 활용한 신속한 실행</p><span class="mark"><span class="icon" data-icon="sprout"></span></span></div></div>
```

## 4. replica 07 / card

- bbox: `[54.0, 489.5, 572.0, 186.5]`
- 디자인: font="Pretendard Variable"; size=20px; weight=400; line=28px; track=normal; color=rgb(7, 11, 9); background=rgb(255, 255, 255); border=1px solid rgba(0, 0, 0, 0); borderRadius=18px; padding=28px; gap=normal; display=block
- 이유: 07은 가로로 넓은2×2 운영 역량 타일이며 번호·제목·설명과 우측 큰 아이콘으로 구성된다. 05의 세로 목표 카드와 같은.semantic.on/quiet/line로 표현할 의미 차이가 아니라 별도 구조 차이다.

- 필요한 구조: 가로 역량 타일 계약: 왼쪽 번호/제목/한줄 설명 + 독립 우측 아이콘 슬롯; 네 타일을2×2로 묶는 소유 root

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="card" data-proposed-contract="card.alternate-source-design@future"><div class="parts"><p class="kick">03</p><p class="name">크리에이티브 마케팅</p><p class="note">시선을 사로잡는 독창적 콘텐츠 제작</p><span class="mark"><span class="icon" data-icon="sprout"></span></span></div></div>
```

## 5. replica 07 / card

- bbox: `[654.0, 489.5, 572.0, 186.5]`
- 디자인: font="Pretendard Variable"; size=20px; weight=400; line=28px; track=normal; color=rgb(7, 11, 9); background=rgb(255, 255, 255); border=1px solid rgba(0, 0, 0, 0); borderRadius=18px; padding=28px; gap=normal; display=block
- 이유: 07은 가로로 넓은2×2 운영 역량 타일이며 번호·제목·설명과 우측 큰 아이콘으로 구성된다. 05의 세로 목표 카드와 같은.semantic.on/quiet/line로 표현할 의미 차이가 아니라 별도 구조 차이다.

- 필요한 구조: 가로 역량 타일 계약: 왼쪽 번호/제목/한줄 설명 + 독립 우측 아이콘 슬롯; 네 타일을2×2로 묶는 소유 root

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="card" data-proposed-contract="card.alternate-source-design@future"><div class="parts"><p class="kick">04</p><p class="name">성과 및 ROI 관리</p><p class="note">실시간 리포팅을 통한 월별 성과 측정 및 최적화</p><span class="mark"><span class="icon" data-icon="sprout"></span></span></div></div>
```

## 6. replica 12 / card

- bbox: `[54.0, 360.0, 279.5, 310.0]`
- 디자인: font="Pretendard Variable"; size=20px; weight=400; line=28px; track=normal; color=rgb(7, 11, 9); background=rgb(255, 255, 255); border=1px solid rgba(0, 0, 0, 0); borderRadius=22px; padding=24px; gap=normal; display=block
- 이유: base와 시각적 레이아웃 계열이 다르다. 비율 차이만으로 계약 .on/.quiet/.line/.tone을 의미 없는 레이아웃 스위치로 쓰지 않음. 최종 통합 검수에서 의미 없는 변형을 추가하지 않고 unexpressible로 유지하기로 결정했습니다.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="card" data-proposed-contract="card.alternate-source-design@future"><div class="parts"><p class="kick">01</p><p class="name">검색 광고</p><p class="note"></p><span class="mark"><div class="seat icon" data-ph="" data-icon="circle"></div></span></div></div>
```

## 7. replica 12 / card

- bbox: `[351.5, 360.0, 279.5, 310.0]`
- 디자인: font="Pretendard Variable"; size=20px; weight=400; line=28px; track=normal; color=rgb(7, 11, 9); background=rgb(255, 255, 255); border=1px solid rgba(0, 0, 0, 0); borderRadius=22px; padding=24px; gap=normal; display=block
- 이유: base와 시각적 레이아웃 계열이 다르다. 비율 차이만으로 계약 .on/.quiet/.line/.tone을 의미 없는 레이아웃 스위치로 쓰지 않음. 최종 통합 검수에서 의미 없는 변형을 추가하지 않고 unexpressible로 유지하기로 결정했습니다.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="card" data-proposed-contract="card.alternate-source-design@future"><div class="parts"><p class="kick">02</p><p class="name">디스플레이</p><p class="note"></p><span class="mark"><div class="seat icon" data-ph="" data-icon="circle"></div></span></div></div>
```

## 8. replica 12 / card

- bbox: `[649.0, 360.0, 279.5, 310.0]`
- 디자인: font="Pretendard Variable"; size=20px; weight=400; line=28px; track=normal; color=rgb(7, 11, 9); background=rgb(255, 255, 255); border=1px solid rgba(0, 0, 0, 0); borderRadius=22px; padding=24px; gap=normal; display=block
- 이유: base와 시각적 레이아웃 계열이 다르다. 비율 차이만으로 계약 .on/.quiet/.line/.tone을 의미 없는 레이아웃 스위치로 쓰지 않음. 최종 통합 검수에서 의미 없는 변형을 추가하지 않고 unexpressible로 유지하기로 결정했습니다.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="card" data-proposed-contract="card.alternate-source-design@future"><div class="parts"><p class="kick">03</p><p class="name">숏폼 콘텐츠</p><p class="note"></p><span class="mark"><div class="seat icon" data-ph="" data-icon="circle"></div></span></div></div>
```

## 9. replica 12 / card

- bbox: `[946.5, 360.0, 279.5, 310.0]`
- 디자인: font="Pretendard Variable"; size=20px; weight=400; line=28px; track=normal; color=rgb(7, 11, 9); background=rgb(255, 255, 255); border=1px solid rgba(0, 0, 0, 0); borderRadius=22px; padding=24px; gap=normal; display=block
- 이유: base와 시각적 레이아웃 계열이 다르다. 비율 차이만으로 계약 .on/.quiet/.line/.tone을 의미 없는 레이아웃 스위치로 쓰지 않음. 최종 통합 검수에서 의미 없는 변형을 추가하지 않고 unexpressible로 유지하기로 결정했습니다.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="card" data-proposed-contract="card.alternate-source-design@future"><div class="parts"><p class="kick">04</p><p class="name">체험단 운영</p><p class="note"></p><span class="mark"><div class="seat icon" data-ph="" data-icon="circle"></div></span></div></div>
```

## 10. replica 15 / prose

- bbox: `[54.0, 528.33, 359.33, 141.67]`
- 디자인: font="Pretendard Variable"; size=22px; weight=600; line=31.9px; track=normal; color=rgb(7, 11, 9); background=rgba(0, 0, 0, 0); border=0px none rgb(7, 11, 9); borderRadius=0px; padding=0px; gap=normal; display=flex
- 이유: 본문 base와 다른 실제 타이포: weight=600 (base 400), line=31.9px (base 29.7px), padding=0px (base 24px 0px 0px). 단순 같은 prose/의미 없는 변형으로 투영하지 않음. 상위 compound가 소유한 경우 그 내부 parts로 흡수.

- 필요한 구조: {'contract': 'source-specific caption or heading inside its semantic compound', 'requiredTypography': {'size': '22px', 'weight': '600', 'line': '31.9px', 'track': 'normal', 'color': 'rgb(7, 11, 9)', 'padding': '0px'}, 'reason': '현재 prose의 base/lead/quiet/cols 의미만으로 이 별도 형태를 정확히 표현할 수 없음'}

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="prose" data-proposed-contract="prose.alternate-source-design@future"><p>브랜드 인지도 및<br>선호도 상승</p></div>
```

## 11. replica 15 / prose

- bbox: `[460.33, 528.33, 359.34, 141.67]`
- 디자인: font="Pretendard Variable"; size=22px; weight=600; line=31.9px; track=normal; color=rgb(7, 11, 9); background=rgba(0, 0, 0, 0); border=0px none rgb(7, 11, 9); borderRadius=0px; padding=0px; gap=normal; display=flex
- 이유: 본문 base와 다른 실제 타이포: weight=600 (base 400), line=31.9px (base 29.7px), padding=0px (base 24px 0px 0px). 단순 같은 prose/의미 없는 변형으로 투영하지 않음. 상위 compound가 소유한 경우 그 내부 parts로 흡수.

- 필요한 구조: {'contract': 'source-specific caption or heading inside its semantic compound', 'requiredTypography': {'size': '22px', 'weight': '600', 'line': '31.9px', 'track': 'normal', 'color': 'rgb(7, 11, 9)', 'padding': '0px'}, 'reason': '현재 prose의 base/lead/quiet/cols 의미만으로 이 별도 형태를 정확히 표현할 수 없음'}

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="prose" data-proposed-contract="prose.alternate-source-design@future"><p>신규 고객 유입량 및<br>구매 전환율 대폭 개선</p></div>
```

## 12. replica 15 / prose

- bbox: `[866.67, 528.33, 359.33, 141.67]`
- 디자인: font="Pretendard Variable"; size=22px; weight=600; line=31.9px; track=normal; color=rgb(7, 11, 9); background=rgba(0, 0, 0, 0); border=0px none rgb(7, 11, 9); borderRadius=0px; padding=0px; gap=normal; display=flex
- 이유: 본문 base와 다른 실제 타이포: weight=600 (base 400), line=31.9px (base 29.7px), padding=0px (base 24px 0px 0px). 단순 같은 prose/의미 없는 변형으로 투영하지 않음. 상위 compound가 소유한 경우 그 내부 parts로 흡수.

- 필요한 구조: {'contract': 'source-specific caption or heading inside its semantic compound', 'requiredTypography': {'size': '22px', 'weight': '600', 'line': '31.9px', 'track': 'normal', 'color': 'rgb(7, 11, 9)', 'padding': '0px'}, 'reason': '현재 prose의 base/lead/quiet/cols 의미만으로 이 별도 형태를 정확히 표현할 수 없음'}

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="prose" data-proposed-contract="prose.alternate-source-design@future"><p>자사몰 데이터 확보를 통한<br>장기적 자산화</p></div>
```

## 13. replica 11 / steps

- bbox: `[54.0, 245.0, 1172.0, 425.0]`
- 디자인: Five large circular ring process stages in one horizontal row, with small curved directional connectors and lower explanatory notes.
- 이유: Second horizontal steps design, not .col. Switching between ring stages and chevrons by5vs6 count would smuggle in another design.

현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.

```html
<div class="steps" data-proposed-contract="steps.alternate-source-design@future" style="grid-column:1 / span 12; grid-row:1 / span 6"><div class="step"><span class="mark">1.</span><p class="name">니즈 분석</p><p class="note">사전 진단 인터뷰 진행 및<br>브랜드 과제 파악</p></div><div class="step"><span class="mark">2.</span><p class="name">전략 기획</p><p class="note">맞춤형 믹스<br>(Media Mix) 및<br>예산 배분안 수립</p></div><div class="step"><span class="mark">3.</span><p class="name">캠페인 집행</p><p class="note">광고 소재<br>제작 및 주요 매체<br>라이브 집행</p></div><div class="step"><span class="mark">4.</span><p class="name">성과 평가</p><p class="note">주간/월간 핵심 지표<br>(KPI) 달성도 측정</p></div><div class="step"><span class="mark">5.</span><p class="name">사후 관리</p><p class="note">픽셀 데이터 기반의<br>2차 리타겟팅 세팅</p></div></div>
```
