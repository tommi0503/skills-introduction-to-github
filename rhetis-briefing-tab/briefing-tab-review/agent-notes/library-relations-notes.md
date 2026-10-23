# 관계·구성 요소 담당 검수

담당: steps, timeline, cycle, hub, funnel, pyramid, matrix, venn, hierarchy, flowchart, architecture, versus, pricing, agenda (14개). HTML fixture 29개. 모든 CSS는 새로 작성했다. sample CSS를 복사하지 않았으며 fixture는 자체 한국어 교육·협업·기업 운영 데이터이다.

## 검수

- 원본 재현 25번 페이지와 design-language.md를 확인하고 중립 종이 면, 1px 구획선, 작은 둥근 모서리, 장 번호 위계를 확장했다.
- 실제 Chromium에서 29개 fixture × 2모드 × 최소/전체 크기 =116회 렌더. root를 넘는 leaf 텍스트, client/scroll 크기로 확인한 텍스트 잘림 현재 0개 (`work/relations-check/errors.json`).
- 요소별 라이트 시트를14개 개별 열어 확인했다. 가격표·허브·SWOT 다크와 플로우 최소 크기도 직접 열어 확인했다. 모든 최종 수정 후 116개를 다시 렌더했다.
- 검사는 DOM 텍스트 경계 중심이다. 전체 grid span sweep와 palette 대비 검사는 주 에이전트가 통합 실행한다.

## 수정

1. Funnel 6단 최소 크기의 마지막 수치가 좁아지는 문제를 900px 이하 타이포/패딩 단계로 해결했다. 폭은 각 stage의 실제 `--v` 비율 그대로다.
2. Hub 연결선이 노드 내부 글자 밑으로 지나던 부분을 배경 마스크로 가렸다. 모든 ray는 중앙과 외곽 노드 중심을 실제 CSS 삼각함수로 연결한다.
3. Hierarchy는 콘텐츠 묶음을 중앙에 놓아 한쪽으로 큰 빈 영역이 남지 않게 조정했다.
4. Pricing은 추천 태그 유무와 관계없이 동일한 태그 행·제목 행을 예약하여 가격과 제목의 높이를 맞췄다.
5. Flowchart는 `to-*` 방향별 실제 연결선과 작은 화살촉을 그렸다. 세로 구간은 컨테이너 높이에서 행간 거리를 계산하여 다음 노드 경계까지 연결한다. decision의 faceted 면은 자식 name에만 잘라내어 선이 같이 잘리는 문제를 해결했다.
6. Timeline.alt의 교대 노드 위·아래 track 접점을 같은 선으로 맞췄다.

## 설계 판단

- 원본에 없는 관계도는 장 번호/구분선/설명 띠의 문법을 작은 단위로 확장했다. 관계를 나타내는 원주·중앙 연결선·겹치는 원·계층 사다리꼴 외에 장식을 추가하지 않았다.
- 순환은 얇은 타원 track과 접선 방향 표시, 허브는 중심을 향하는 실제 ray로 구별한다. 퍼널은 supplied percentage의 폭, 피라미드는 계층의 점증 폭을 쓴다.
- 범용 flowchart의 ask는 문서형 판단 노드의 가독성을 위해 큰 마름모 대신 좌우가 뾰족한 작은 faceted 면으로 해석했다.
- 구성상 필요한 작은 노드 글자는16px, 부연12–14px까지 단계를 내린다. 이름은 숨기지 않는다. 설명은 실제로 좁은 높이에서만 생략한다.
