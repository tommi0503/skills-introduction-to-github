# Unexpressible

## 03 · 176px SUITE 영문 구분 표제

원본176px는 허용된 최대 type128을 넘는다. 고정 glyph 배율로 타입 계약을 우회하지 않는다.

```html
<section class="extended-type">…</section>
```

## 03 · 오른쪽 아래 원형 다음 이동 버튼

독립 navigation/action 버튼 계약이 없고 callout은 결론 문장용이다.

```html
<section class="action-button">…</section>
```

## 06 · 140px 증가 수치와 38px 단위

원본140px 수치가 허용 type128 상한을 넘고 단위는 분리 절대배치된다.

```html
<section class="extended-type">…</section>
```

## 06 · 면적 플롯 위 검정 상향 화살표 세 개

chart.area 구조에 데이터와 무관한 장식 화살표 멤버가 없고 source의 그래프 위에 겹친다.

```html
<div class="trend-arrows"><i></i><i></i><i></i></div>
```

## 07 · 위쪽 두 항목의 아래 1px 가로 괘선

소속 멤버와 무관한 독립 괘선 계약이 없다. prose나 tag의 형제 위치 조건으로 그리지 않는다.

```html
<section class="extended-type">…</section>
```

## 09 · 16px 두 줄 가운데 정렬 본문

prose base는 좌측 본문이고 lead는 28px 도입문이다. 가운데 정렬을 뜻하는 prose.center 변형이 없어 lead를 억지 재해석하지 않는다.

```html
<div class="prose center"><p>가운데 정렬 본문</p></div>
```
