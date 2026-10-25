# Corner Signal Round 5 최종 요소 검수

21페이지의 관찰된 형태를 30개 독립 디자인, 19개 기존 계약 계열, 40개 원본 요소 인스턴스로 다시 구성했다. 01 표지는 공통 페이지 장치와 사진 영역이 담당한다. 이전 범용 CSS를 재사용하지 않고 원본의 좌표·도형·문자 위계에서 CSS를 새로 작성했다. 요소 마크업에는 직접 그린 SVG를 넣지 않았다. 아이콘은 빈 Lucide 슬롯이며 연결선과 도형은 소유 요소 CSS가 그린다.

## 페이지와 디자인 대응

| 페이지 | 요소 폴더 |
|---|---|
| 02 | agenda--notched (2판) |
| 03 | prose--letter, image-frame--leader |
| 04 | headline--statement |
| 05 | card--feature (3개) |
| 06 | steps--process |
| 07 | card--opportunity, concentric--market |
| 08 | card--market-forecast, concentric--ascending |
| 09 | hub--product |
| 10 | card--pentagons |
| 11 | pricing--models |
| 12 | chart-donut--metrics, chart-area--growth |
| 13 | card--metric (4개), chart-bar--annual |
| 14 | chart-line--multi, chart-area--overlap, chart-bar--grouped |
| 15 | positioning--market, card--differentiators |
| 16 | versus--mirror |
| 17 | timeline--phases |
| 18 | architecture--layers |
| 19 | person--team (5개) |
| 20 | chart-donut--allocation, list--allocation, chart-bar--forecast |
| 21 | steps--funding |

기존 14개 관찰 계열은 독립 디자인으로 교체했다. 이전의 관찰 없는 42개 범용 폴더는 제거했으며, 그중 agenda·chart-line·list·pricing·versus는 실제 관찰된 형태로 새로 작성했다. 사용되지 않는 37개 계약 계열은 억지로 채우지 않았다. 영문 description.md 30개를 작성했고 계약 ID는 기존 leaves.json과 일치한다.

## 패널과 소유권

패널 9개를 지도에 기록했다. 12·20페이지는 각각 [77,219,725,429], [818,219,387,429]의 tip-l 패널이다. 13페이지는 [77,317,1128,327]의 무장식 패널이다. 14페이지는 [77,215,366,433], [458,215,366,433], [840,215,365,433]의 tip-r 패널이며, 15페이지는 [71,229,713,413]의 무장식 패널이다. 패널 구현은 공통 foundation 소유다. 차트 내부 제목·설명·범례·축은 해당 차트 소유다. 페이지 사진과 큰 배경 윤곽은 공통 페이지 장치로 분리했다. 측정 덤프나 작은 캡션을 미지원 영역으로 남기지 않았다. 최종 GAPS는 0개다.

## 실제 수정과 검수

- 02의 노치 두 판, 08의 상승하는 겹침 오각형, 10의 교차 방향 사업모델 4개, 11의 두 요금 항목을 가진 모델 3판, 16의 두 회사 거울 막대, 19의 CEO와 팀 프로필, 21의 자금 단계 4개를 각각 원본 부품과 배치로 구성했다.
- 14페이지의 3시리즈 선, 2시리즈 영역, 2그룹×2막대 및 20페이지의 4분할 파이를 실제 데이터와 연결했다. Y축 눈금은 --max에서 계산한다. 원본의 고정 글자나 고정 경로를 데이터 대신 사용하지 않는다.
- 파이 대체값 35/25/25/15에서 라벨이 다른 조각에 가려지던 결함을 수정했다. 조각과 라벨의 쌓임을 분리했으며 해당 대체값을 그대로 유지해 검수했다.
- positioning의 일반 마크 규칙이 버블의 중앙 정렬을 덮던 문제를 제거했다. 원본의 84/98/100/130 지름과 중앙 이름 정렬을 보존했다.
- metrics 링은 바깥 173, 안쪽 147, 선 두께 13의 실제 비율을 복원했다. radial mask의 기준을 closest-side로 고쳐 두꺼워 보이던 오류를 없앴다.
- 아이콘은 경로 경계가 아닌 실제 SVG 뷰포트로 측정했다. 05의 Handshake/ListTodo/Settings, 18의 Factory/PackageOpen 등 실제 아이콘 종류와 크기를 교정했다.
- 단계 설명 fixture의 의미 없는 짧은 조각을 완결된 냉장물류 문장으로 교체했다. 원본의 수동 줄바꿈 수는 유지했다.
- 16·17의 중성 진하기 구분과 13의 quiet 숫자 위계를 복원했다. 03의 작은 캡션은 한 줄을 유지했다.

최종 정식 시트는 70 fixture × 허용 크기 × 라이트·다크의 508 상태다. 잘림, 글자 겹침, 이름·수치 숨김, 실제 배경 대비, 폰트 오류, 그리기 영역 초과, chip 정렬 오류는 모두 0건이며 staleDuringRender도 0건이다. 공식 시트의 큰 칸과 최소 칸을 확대해서 형태와 정렬을 직접 확인했다. 발견된 결함은 수정 후 해당 전체 상태를 다시 렌더했다.

원본 좌표의 native 비교 40개를 양 모드로 렌더한 80상태도 영역 초과·글자 겹침·폰트 오류 0건이다. native root 크기가 원본 bbox와 일치함을 자동 검사했다. 핵심 원본 비교를 개별로 열어 도형·문자·선·아이콘을 확인했다. 최종 21페이지 전체 조립의 페이지 장치와 통합 비교는 주 에이전트가 수행한다.

별도 수치 검사는 7개 대체 데이터 사례에서 오류 0건이다. max=120/180/60의 축 눈금, 점의 Y 좌표, 다음 점 연결 길이·회전, 막대 높이, 파이 합계 100과 시작 각도를 확인했다. fixture 원문 6-gram 검사는 80개 대상에서 0건이다. 요소 fixture 70개와 공통 패널 fixture 10개를 포함한다.

수치 근거와 결과는 corner-signal-review/audits 및 sheets에 있다. 추가 native·수치·문구 검사 기록은 /workspace/work/element-rebuild/corner-round5-native/audit.json, corner-round5-numeric-probe.json, corner-round5-text.json에 남겼다.

## 차이와 판단

사진·기기 화면은 요청대로 중성 회색 seat다. 원본 고정 색상은 팔레트 역할로 옮겼으며, 밝은 면 위 작은 흰 글자의 대비가 부족한 경우 잉크 역할로 읽히게 했다. 이는 색 역할 해석이며 원본의 도형과 마크업은 유지했다.

원본의 7.5px 캡션은 허용 토큰 최솟값 8px을 사용한다. 겹침 영역 차트의 원본 값 라벨이 다른 계열 선과 만나는 곳에는 작은 페이지색 배경을 두어 읽히게 했다. 원본 연간 막대의 시각적 높이와 인쇄 수치가 서로 다른 경우 canonical 지도는 원본을 보존하고 새 fixture는 데이터와 문구를 일치시켰다. 원본 거울 비교의 00%도 canonical에서는 유지하고 새 fixture에서는 의미 있는 실제 수치로 바꿨다. 곡선의 CSS 다각형 근사와 브라우저 래스터 경계에는 미세한 차이가 있을 수 있다. 완전한 픽셀 동일성을 주장하지 않는다.

요소 CSS·fixture·지도는 최종 동결했다. 공통 foundation의 마지막 지문 동기화와 전체 조립 산출물 갱신은 주 에이전트가 담당한다. git 작업은 수행하지 않았다.
