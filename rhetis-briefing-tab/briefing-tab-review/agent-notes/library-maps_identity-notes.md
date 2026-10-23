# 담당 D — maps / identity

## 범위 및 결과

person, logo-group, image-frame, slope, roadmap, swimlane, concentric, journey, mindmap, decision-tree, balance, matrix-nine, positioning, network의 14개 요소를 새 CSS로 작성했다. 각 폴더 element.css/element.json/description.md/fixtures 완성. fixture 총29개(각2개, slope는 dumbbell 포함3개). 샘플 CSS 복사 없음. 원본 replica와 디자인 언어 문서를 먼저 검토한 뒤 확장했다.

## 해석과 기하

- person: 동일 행의 이름 시작 위치를 맞추고 가운데 무게중심 유지. 로고·이미지는 숫자 seat이며 거의 정사각이다. image-frame은 기본 정사각/portrait 변형을 제공한다.
- slope: 공급된 전/후 값에서 끝점의 높이와 선의 길이·각도를 CSS hypot/atan2로 구한다. dumbbell은 같은 값의 가로 거리로 바꾼다.
- roadmap: --from/--to의 기간 길이와 --at 마일스톤 위치를 실제 칸 수로 계산한다.
- swimlane: 부서별 행, 가로·세로 방향 화살표, 둥근 시작·끝을 구현했다. 소유자 이름은 별도 왼쪽 공간으로 빼서 노드와 겹치지 않는다.
- concentric: 원들이 아래쪽 접점에서 실제 포함되며 상단에 노출된 이름·숫자를 둔다. venn과 달리 겹침으로 해석하지 않는다.
- journey: --mood와 --next로 점 높이 및 연결선 각도를 계산한다. 초기 padding으로 생긴 선 연결 간극을 수정했다.
- mindmap: 중앙 이름에서 좌우 가지로 뻗는 직선·둥근 elbow를 구현했다. leaf는 숨기지 않고 단계형 글자 크기로 유지한다.
- decision-tree: 질문에서 조건·결과 및 중첩 질문으로 분기하는 선을 구현했다. 첫 검수에서 질문 직후의 세로 출발선을 추가했다.
- balance: --tilt로 기울어진 beam과 pan 중심의 정확한 높이를 tan()으로 계산해 연결한다. 원본에 없는 천칭이지만 중립 면·얇은 선·한 곳의 강조만 사용했다.
- matrix-nine: 9칸과 양축 3라벨, 좁은 높이에서는 note만 숨긴다.
- positioning / network: 좌표로 표지를 배치한다. 바깥의 이름 잘림을 피하도록 12~14% 내부 여백을 예약했다. network 링크 끝점과 실제 선 길이·각도가 노드 위치와 일치한다.

## 브라우저 검수

로컬 Chromium에서 14개 요소를 fixture별 full/min으로 렌더하고, 라이트와 다크의 각 요소 시트 이미지를 각각 직접 열어 확인했다. 14개 모두 실제 Pretendard Variable/Noto Sans KR 글꼴을 로드한다. 시트에서 label 정렬·형태·다크 면 분리를 확인했고 수정 후 다시 렌더했다. 담당 임시 시트는 work/maps-preview.html, work/maps-preview-dark.html이다(최종 제출 시트는 주 에이전트가 통합 생성).

실제 foundation과 tokens를 사용해 최소 칸부터12x6까지 가능한 가로·세로 조합을 라이트/다크에서 전수 검사했다. 754 cases, 페이지 슬롯 밖 텍스트0건. 결과 work/maps-audit-results.json. 텍스트의 실제 계산색과 가장 가까운 불투명 부모 바탕에 대해 대비 검사했으며 실패0건(work/maps-contrast-results.json). 복잡한 gradient의 개별 픽셀 대비까지 측정한 것은 아니다.

남은 차이: 원본에 없는14요소는 해석 설계이므로 원본과의 픽셀 일치 대상으로 보지 않았다. 코어를 중심으로 한 map의 구조용 곡선/천칭 지지대 외에 장식은 추가하지 않았다. 원본의 파란색은 디자인 CSS에 넣지 않았고 모두 팔레트 자리로 옮겼다.

## 통합 검수 후 slope 수정

주 에이전트의 텍스트 Range 교차검사에서 slope-3의 8x4~12x4 구간 오른쪽86/91이 가까워지는 문제를 발견했다. 최소 칸을 늘리지 않고, 플롯 끝점은6px 점으로 유지하며 수치 라벨을 오른쪽 예약 여백으로 분리했다. 강조 라벨은 점 아래, 중립 라벨은 점 위에 둬 촘촘한 끝값을 구별한다. 실제 slope 값과 선의 기하는 그대로 유지했다. 동일한 통합 AUDIT 함수로 slope3fixture의 최소~12x6, 양모드70case를 다시 검사하여 겹침/잘림/대비/폰트실패0건. 마지막8x4 브라우저 PNG를 직접 열어86/91 분리 및 수정 반영 확인. 결과 work/slope-final-check.json.

## 추가 담당 — 원본27/28 복합 도넛·파이 복원

초기 조립본의 단일비율 도넛은 원본의 의미와 형태를 충분히 보존하지 못했다. chart-donut CSS에 동일한 그리드 자리를 공유하는 누적 conic layer의 범용 조합을 추가했다. 원본27은20/40/35/10/50(합155) 다섯 구간을 그대로 표시하며 누적 전체비중100→67.74→61.29→38.71→12.90으로 쌓는다. 원본28은20/30/50%의 세 구간 파이이며 중앙 구멍을 만들지 않는다. 각 fig/name의 --v는 실제 해당 구간의 비중을 보관하며, root의 누적 --v와 함께 중간각도·숫자 위치·라벨 위치를 계산한다. 새 클래스나 페이지 전용CSS 없이 기존 donut/donuts/fig/name/tone-N과 수치데이터만 사용했다.

원본27 도넛 중심934,435 / 지름338px, 원본28 파이 중심944,429 / 지름330px로 실제 렌더가 일치한다. 중앙 구멍40%와 모든 구간의 숫자, 바깥 알약 라벨과 연결선을 복원했다. 라벨 위치는 범용 충돌회피식이므로 원본에 비해 일부5~15px 차이가 있다. 오른쪽 라벨은 슬롯 경계를 보존하기 위해 원본보다11px 안쪽이다. 원문이 아닌 ‘비중 요약’ 추가문구를 제거했다. 기존 모범구성 donuts3/4는 독립 row이므로 전혀 변경하지 않았다. 새 composite-ring-5/composite-pie-3 fixture를 기존 donuts root로 추가했다.

라이트·다크에서 기존5개+새2개 fixture를 최소~12x6까지334case 검사: 범위초과·문자교차·잘림·대비·폰트실패0건. source27/28 페이지도1280×720, 같은 AUDIT issues0. conic pseudo의 바탕은 DOM 검사에서 보이지 않으므로 fig의 실제 바탕색을 같은 slice색으로 명시했다(화면에는 변화 없음). 기준palette의 a3와white는4.5미달이므로 세번째 구간을a3-7/page쌍으로 설계했고, source-theme의a3-7은 원본 보라색으로 매핑하도록 주 에이전트에게 전달했다. 원본 비교2회 및 최종 fixture 라이트·다크 렌더를 직접 확인했다. 결과 work/donut-final-check.json.
