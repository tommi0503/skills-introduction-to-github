# Unexpressible instances

## 07 · 07-foundation-21

bbox: `[94, 273, 1092, 373]`

둥근 흰 일정판 안 5주 머리띠, 5개 옅은 track, 실제 기간 bar 5개. 1–3행은 오른쪽 촉,4–5행은 왼쪽 촉. STEP명과 담당자가 bar 밖에 놓임.

roadmap.bar에는 .on/.tone-N 외에 방향 변형이 없고 외부 담당자 note 슬롯도 없다. 행 번호·색·--from 값에 따라 촉 방향을 바꾸는 규칙은 fixture 보정이 된다. 전체 기간표를 지원불가로 기록하며, 오른쪽 3개만 떼어 다른 디자인으로 재정의하지 않는다.

Proposed markup (not a supported extension):

```html
<div class="roadmap" style="--cols:5"><div class="heads"><span>1주차</span><span>2주차</span><span>3주차</span><span>4주차</span><span>5주차</span></div><div class="lane"><span class="name">STEP01</span><div class="bar" style="--from:0;--to:1.03"><span>프로젝트 기획 &amp; 자료조사</span><span class="note">담당자: 김미리 차장</span></div></div><div class="lane"><span class="name">STEP04</span><div class="bar to-l" style="--from:2.53;--to:3.97"><span>프로젝트 세부 일정 타이틀 영역</span><span class="note">담당자: 박미리 대리 / 한미리 주임</span></div></div></div>
```

## 08 · 08-gap-1

bbox: `[300, 146, 680, 171.14]`

680px 폭의 3행 중앙 선언. 53.3333px/1.07, -0.04em; 한 구절900, 두 구절700/순위 강조. 상단9.3333px/0.43em 라틴 kicker는 페이지 장치로 분리.

하나의 h2 안에900/ink·700/a1·700/a2의세강조범위가있고계약b에독립tone/weight변형이없다. 위치별조건으로색을정하지않는다.

Proposed markup (not a supported extension):

```html
<div class="headline center"><h2><b>...</b>...<b class="tone-1">...</b>...<b class="tone-2">...</b></h2></div>
```
