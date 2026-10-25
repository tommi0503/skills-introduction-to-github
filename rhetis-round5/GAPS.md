# ROUND5 잔여 GAP

완화 계약으로 재분류한 뒤 남은 것은 아래 두 디자인이다. 동일 디자인의 반복은 별도 GAP으로 세지 않는다.

|컬렉션|replica|표현 불가 이유|제안 마크업|
|---|---:|---|---|
|seedmark|20|한 관측값의4구간 누적 막대. chart.stack은 .sbar2–12개를 요구하며 round5는 이 하한을 바꾸지 않았다.|`.stacks.pct.h > .sbar ×1 > .seg[style="--v:40/20/30/10"]`|
|meridian-deck|14|한 연속 면 시리즈의 실제15관측값. chart.area의 점 최대12개를 초과한다.|`.areas > .series > .pt ×15` 및 `.axis > span ×15`|

구체적인 제안 마크업과 원형 bbox는 각 프로젝트의 GAPS.md에 있다. 표제·캡션·라벨·측정 잔여물·페이지 배경은 GAP에 포함하지 않았다.
