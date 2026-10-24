# Unexpressible

## 21 — 사진 전면과 세 텍스트 역할의 중첩 패널 (세 인스턴스)

- 대상: `21-media-panel-1`, `21-media-panel-2`, `21-media-panel-3`.
- 사진 또는 placeholder가 패널 전체를 채우고 그 위에 작은 keyword, 부분 굵기를 가진 두 줄 제목, 작은 설명이 중첩된다.
- `card`의 base는 20의 채워진 원형 KPI다. `.quiet`나 `.line`을 전혀 다른 사진 전면 패널로 바꾸지 않는다. 다른 계약도 사진면과 이 세 역할을 함께 소유하지 않는다.

필요한 새 계약 제안:

```html
<section class="media-panel">
  <div class="seat back" data-ph="1"></div>
  <p class="kick">분기 실행 원칙</p>
  <h2 class="name"><b>빠른 확인</b><br>낮은 비용으로 배웁니다.</h2>
  <p class="note">고객 신호를 확인한 뒤 투자 범위를 결정합니다.</p>
</section>
```

이 마크업은 기존 컬렉션에 넣지 않은 확장 제안이다. 새 계약은 배경 이미지 자리와 전경 텍스트의 대비 역할을 명시해야 한다.

## 23 — 204px Q&A 표시 표제

- 대상: `23-qa-heading`.
- source의 글자 크기는 204px이며 허용 타입 단계 상한은128이다.
- 128 토큰을 font-size 곱이나 고정 glyph scale로 확대해 상한을 우회하지 않는다.

필요한 확장 제안:

```html
<div class="headline big">
  <p class="kick">구성원의 질문을 기다립니다.</p>
  <h2>Q&amp;A</h2>
</div>
```

기존 headline.big 마크업을 유지하면서 표시용 타입 단계204 또는 상자에 맞추는 fit-text 역할을 계약과 렌더러가 명시적으로 지원해야 한다. 위 제안은 현재 컬렉션에서 구현하지 않았다.

## 19 — 중앙 spotlight·beam·하단 띠 장면 장식

- 대상: `19-spotlight-scene`.
- 중앙상단 타원 광원과 아래로 벌어지는 흐린 사다리꼴 beam, 하단 수평 광원 띠가 동시에 있다. 이는 일반 page 면과 분리해 지도에 기록했다.
- 현재 foundation의 공통 좌상/우하 광원과 다른 장면이며 이를 선택할 계약 명명 변형이 없다. body의 headline 같은 요소를 식별하여 페이지 배경을 고치는 규칙을 만들지 않는다.

필요한 foundation 확장 제안:

```html
<section class="slide">
  <div class="page">
    <div class="deco spotlight" aria-hidden="true"></div>
    <div class="body">…</div>
  </div>
</section>
```

`.deco.spotlight`는 새 변형 승인이 필요한 제안이다. 현재 컬렉션 CSS와 실제 조립본에는 넣지 않았다. CSS gradient·mask·clip-path로 구현할 수 있는 도형이지만, 여러 배경 장면을 고르는 계약 문법이 먼저 필요하다.
