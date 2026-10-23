# Briefing Tab 차트 요소 14종 구현·검수

- chart-bar, chart-line, chart-donut, chart-area, chart-stack, chart-waterfall, chart-scatter, sparkline, heatmap, waffle, treemap, sankey, radar, bullet: 14종/39 fixture.
- Golden 19 fixture는 지정 샘플의 마크업·데이터를 그대로 유지하고 data-el 접두사만 교체했다. 나머지는 각2개씩 멤버수·변형·긴한국어를 달리했다.
- CSS는 새로 작성했다. line/area의 값 사이 연결에 CSS anchor 수학을 연구했으며 샘플의 색·장식·형태를 가져오지 않았다. 실제 CSS값을 따라 점·선·면이 움직인다.
- 브라우저에서 각 fixture의 최소 칸/12×6, 라이트·다크 총156뷰를 렌더했다. 초기 및 수정 뒤 검토, 최종 검토 3회. work/chart-b-test/에 임시 HTML·PNG·검사JSON이 있다. 14요소별 연락처 이미지를 각각 열고, 작은 도넛4개는 개별1280이미지도 열어 확인했다.
- 수정: line의 anchor bottom좌표 부호를 수정해 각점연결. flat equal값의 선도 1px 높이로 유지. area 내 cqh 이중 차감을 제거해 톱니모양 오차를 수정. donut size containment에 의한 높이축소를 수정. waffle 단위의 종횡비를 정사각으로 유지. radar polygon을 pseudo로 분리하여 범례이름을 clipping하지 않음. sankey 출발블록과 밴드를 직접 연결. bullet 설명과 실제·목표선 사이 여백 확보.
- 최종 개선: 좁은도넛의 수치16/unit10 단계로 축소해 링과 텍스트 충돌 방지. 모든 figure/name 유지. chart-line 좁은축 라벨만 솎으며 값은 숨기지 않음.
- 임시검사 마지막 결과 모든156뷰 root외부DOM 넘침0. 최종 전체시트는 주 에이전트가 실제 foundation 치수로 다시 검수해야 한다.
- 계약상 CSS-only radar는 타원형 그리드/정확한 다각형 수치로 확장했다. sankey는 데이터비례 직선 밴드로 설계했으며 곡선은 원본 디자인언어에 없는 장식이라 도입하지 않았다.

## 통합 검수 반영

주 에이전트의 실제 foundation 검수 지적을 반영했다. Radar 플롯과 원형 가이드는 min(cqw,cqh) 정방형으로 고쳐 가로로 늘어나지 않는다. Treemap 작은 칸에서는 이름과 수치를 가로로 배치해 15% 타일도 유지한다. 4개 도넛의 작은 링은 수치가 내부에 들어가는 크기로 확보했다. 마지막으로 본문 높이400px 기준 156뷰를 다시 렌더했고 root 밖 DOM 요소0건을 확인했다. 수정된 radar full, treemap min, donuts4 min 이미지를 각각1280×720으로 열어 검수했다. 이 3개 최종 변경이 마지막 임시PNG에 반영되어 있다. 주 에이전트 최종시트에는 재빌드가 필요하다.

## 사용자 지적 후 원본 충실도 교정 — 슬라이드24/25/26

기존 재조립24가 복합 그래프를 단일 막대로 줄였고 25는 긴 이름용 왼쪽 padding 때문에 실제 플롯이 좁아진 문제가 있었다. 이를 원본의 정보를 모두 유지하는 범용 조합 패턴으로 교정했다.

- 24: `.bars`와 `.lines`를 동일12×6칸에 겹쳐 실제 막대+선 복원. 8개64px원형 `0.0/억원` 라벨, 11개 `00명` 행, 20XX 행, 현재 수직화살표·목표, 0–100억원 축눈금, 막대·선 범례 복원. 막대의 `--v`는 실제 수치, b의 별도 `--v`는 원본 원형주석의 높이 위치다. 제목 주석은 표준 `title` 속성을 CSS generated text로 표시한다. 축 단위는 root aria-label에서 가져오며 눈금은 --max에서 계산한다. 그림이나SVG를 넣지 않았다.
- 25: 가로 막대는 max-content 이름열과 실제 값 기반 길이로 구현해 A–F처럼 짧은 이름일 때 왼쪽 공간이 자동으로 줄어든다. 원본 위치x126–540,414px 플롯을 복원했다. 실제values20/40/35/10/50/30과 전부강조색, 0/10/20/30/40/50 눈금 유지. 설명열을 위해6칸 chartroot의 오른쪽만106px reserve하는 일반 chart+notes 패턴이다.
- 26: callout+두차트를 foundation stack/group.two로 쌓았다. summary는104px(원본101px). 막대 플롯448×228, area496×228, y384–612를 복원했다. 눈금0–50 전부와 마커·원본처럼 아래로 옅어지는 면 그라데이션을 복원. foundation의 stack좌14px 이동에 대응하여 요소 padding을 보정해 원본 x좌표를 유지했다.
- 23 지원: 두개의인접 `.lines` root를 겹치는 paired-pattern을 작성했다. 첫선중립/둘째강조, 축0·2·4·6·8·10 및 원형포인트를 그리며 rootpadding만으로 정확한플롯수학을 적용한다. source23 HTML은 relations 담당자가 유지했다.
- 새 클래스와 새 페이지 CSS를 만들지 않았다. 모든 변경은 chart-bar/chart-line/chart-area의 scoped element.css와 계약HTML에 있다. 검수 fixture `bars-lines-composite` / `lines-paired`를 추가했다.
- 최종 실제 Chromium source24/25/26 원본|조립본 비교PNG를 각각 열어 확인했다. `/workspace/work/faithful-charts-b-checks.json`에 페이지1280×720/폰트/viewport초과/원형라벨 중앙정렬/막대 실제길이를 기록했다. 마지막HTML·CSS 변경이 현재 PNG에 반영되어 있다. 전체PDF·라이브러리시트·최종패키징은 주 에이전트가 다시 생성해야 한다.
