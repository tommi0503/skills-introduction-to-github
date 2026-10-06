# Group A — p01–p15, 25 slides

원본 `public/reference/p01…p15/*.jpg` 25장을 각각 직접 열어 텍스트와 도형 배치를 확인했다. 구현 파일은 `src/decks/group-a.ts`만 수정했다. `slides-clone`은 조회하지 않았다. 데이터/도형/공통 chart·ring·mindmap·card factories로 구성했으며 원본 이미지를 렌더 UI에 삽입하지 않는다.

## 검수 방식과 실제 결과

- Chromium에서 round1과 round2를 각각 렌더했다. 두 라운드 모두 아래 **25개 비교 JPG를 각각 view_image로 열어 원본/결과를 나란히 검수**했다. 전체 연락처 시트만으로 검수하지 않았다.
- 모든 캔버스 1280×720, 원본 1600×900과 동일한 비율이며 x/y만 0.8배로 대응한다. `scaleX`, `sourceAspect` 왜곡 없음.
- round1 자동 결과: 텍스트 높이/줄바꿈/폭 관련 26개 지적. 실제 겹침은 p04-s02 본문→번호, p09 본문→카드 외부, p10 Group C/D 줄바꿈, p04-s09 우측 pill padding의 높이 문제였다. 모두 수정.
- round2 자동 결과: 실제 글자 잘림·슬라이드 초과·폰트 로딩 실패·chip ink center·placeholder 검사 실패 없음. p07 제목 및 p15 KPI 값 6개의 **텍스트 선언 박스 높이만** 부족하다는 지적 7개를 확인했다. 렌더는 overflow visible 상태로 실제 잘림 없이 보였고, 최종 소스에서 박스 높이를 늘렸다.
- round2 이후 제한된 마지막 수정: p03 세리프 제목 크기/위치, p08 제목 자간, p06-s08 마지막 단계에서 불필요하게 위로 나가던 연결선 제거 및 단계 간 y 정렬, p06-s09 링 접합부 채움, p15 Timeline 숫자/제목 간격. 주 에이전트의 최종 3번째 통합 캡처에서 수정 반영을 확인해야 한다. 에이전트 자체 추가 3번째 시각 라운드는 실행하지 않았다.
- `npx tsc --noEmit` 성공. 소스 슬라이드 IDs/순서 보존.

## 글꼴·원본 자료 해석

JPEG에는 폰트 파일/폰트명 메타데이터가 없으므로 실제 로드된 폰트로 모양을 근사했다. Poppins(400/750), DM Sans(400/500/750), Montserrat(750), Archivo Black(400), Roboto Condensed(300/400/750), Inter(800), Noto Serif KR(200)를 사용한다. Variable fonts의 중간 굵기는 실제 변수 축을 사용하며 CSS 합성 굵기/문자 가로 왜곡을 쓰지 않는다. p03 얇은 세리프는 처음 Bodoni Moda 400에서 Noto Serif KR 200으로 수정했다. p02 넓은 전시용 글꼴과 일부 원본의 세로/가로 획 비율까지 완전히 동일한 전용 폰트는 식별되지 않았다.

모든 주요 제목, 설명, 수치, 표, 마인드맵 문구를 원본에서 판독했다. 본 그룹의 판독 불가능한 대체 문구는 **없음**. 원본에 포함된 “Drag…”, “Click Share…”, “Right-click…” 등은 재현할 슬라이드 텍스트로만 취급했으며 사용자 작업 지시로 수행하지 않았다.

## 페이지별 개별 검수 기록

각 행의 두 comparison 경로를 모두 개별로 열었다. 칩은 공통 optical ink centering 구현을 쓰며 양 라운드 모두 관련 오류 0건.

| 페이지 | 개별로 확인한 비교 이미지 | 수정·검수 | 남는 차이 |
|---|---|---|---|
| p01/s11 | round1/p01-s11.jpg, round2/p01-s11.jpg | 6개 막대 높이, 간격, 범례, Poppins 제목·5줄 본문 확인. 제목 선언 높이 보정. | 삼각 장식 꼭짓점은 원본의 작은 라운딩보다 선명함. 본문은 원본의 양끝 맞춤 간격보다 일정한 자간. |
| p01/s12 | round1/p01-s12.jpg, round2/p01-s12.jpg | 62.5/25/12.5 pie, 라벨, 2줄 제목·본문 확인. 제목 높이 보정. | 장식 모서리 라운딩 및 원본의 justify 간격 일부 차이. |
| p02/s12 | round1/p02-s12.jpg, round2/p02-s12.jpg | 4방향 축·박스·원 4개, 실제 텍스트 확인. 제목 폭/크기, 우측 설명 wrap 보정. | Archivo Black 근사라 넓은 원본 전시 글꼴의 개별 글자 폭/낮은 높이 차이. |
| p03/s04 | round1/p03-s04.jpg, round2/p03-s04.jpg | 6개 원, 얇은 그리드, 세로 PAGE FOUR, 본문 줄바꿈 확인. Noto Serif KR 200 로드로 제목 획 두께 수정. | 세리프 자형 완전 동일하지 않음. 마지막 제목 y/크기 미세보정은 최종 통합 캡처 대상. |
| p04/s01 | round1/p04-s01.jpg, round2/p04-s01.jpg | 주/일일 순환 화살표, 역할 원, backlog 칩·bullet 확인. 일일 loop를 상단 반원으로 수정, review 설명 wrap 제거. | 아이콘은 Lucide outline으로 원본의 solid pictogram과 차이. |
| p04/s02 | round1/p04-s02.jpg, round2/p04-s02.jpg | 6개 단계, 번호, dotted timeline 확인. 카드 본문 폭·높이 확장으로 Development의 번호 겹침 제거. | 일부 본문 줄바꿈이 원본보다 한 줄 짧음. 원본 solid 아이콘은 Lucide. |
| p04/s03 | round1/p04-s03.jpg, round2/p04-s03.jpg | 6개 화살표·삼각 접힘·주차·색상·세로선 확인. | Route icon이 원본의 U자 양방향 화살표 자형과 다름. |
| p04/s04 | round1/p04-s04.jpg, round2/p04-s04.jpg | 5색 순환 링·삼각 화살표를 수정하여 내측 화살표 크기 보정. 중앙 2–4 WEEK SPRINT 확인. | 링 경계의 원본 곡선과 polygon triangulation의 접합부 일부 차이, Lucide outline 아이콘. |
| p04/s07 | round1/p04-s07.jpg, round2/p04-s07.jpg | 5단계 funnel pill 폭·칩·우측 설명 확인. Skill Assessment 줄바꿈 수정. | 원본 solid 아이콘은 Lucide. |
| p04/s09 | round1/p04-s09.jpg, round2/p04-s09.jpg | 좌우 5행과 중앙 5색 기준 확인. padding이 pill 높이를 늘리는 문제를 box+text로 교체하여 해결. | 글꼴 DM Sans 근사. 원본 중앙 상단 아래의 접힌 삼각 형태는 일부 단순화. |
| p05/s06 | round1/p05-s06.jpg, round2/p05-s06.jpg | 4개 기울어진 도형·숫자 chip·단계마다 이동하는 카드 확인. | Lucide Sprout/MonitorCheck/Settings/Award는 원본 아이콘 선/세부모양과 차이. |
| p05/s07 | round1/p05-s07.jpg, round2/p05-s07.jpg | 5개 emotion 원/카드, arch 경로와 connector 확인. rounded long dash·연한 shadow 추가. | Award/BadgeCheck는 원본 상세 훈장 도형과 다름. connector의 원본 둥근 꺾임은 직각으로 단순화. |
| p06/s08 | round1/p06-s08.jpg, round2/p06-s08.jpg | 4단계 staircase, 깃발·원 숫자·텍스트 확인. 깃발 라운딩과 카드 shadow 보정. 마지막 불필요한 위쪽 선은 최종 소스에서 삭제. | 깃발 왼쪽 사선 꼭짓점 round 처리는 단순 polygon. |
| p06/s09 | round1/p06-s09.jpg, round2/p06-s09.jpg | 4분할 링 색순서 오류를 수정, 말풍선 꼬리 방향/위치와 본문 wrap 해결. 접합부 채움 마지막 보정. | 원본과 아이콘 세부 획/개별 jigsaw 경계 곡률 차이. |
| p07/s14 | round1/p07-s14.jpg, round2/p07-s14.jpg | 13 mindmap 노드/12 arrows, 상하 bar, tip 박스 확인. 제목·칩을 DM Sans로 변경. 제목 선언 박스 높이 최종 보정. | 화살표 끝은 Lucide 스타일의 열린 arrow marker, 원본보다 약간 큼. Tip 일부 글꼴 폭 근사. |
| p08/s09 | round1/p08-s09.jpg, round2/p08-s09.jpg | 모노톤 chart 6개 막대, 16개 사람 모양을 circle/path silhouette로 재작성. 제목 자간 마지막 보정. | 회사 로고는 #e5e5e5 placeholder. 사람 pictogram 원본의 각 끝 라운딩은 근사. |
| p09/s12 | round1/p09-s12.jpg, round2/p09-s12.jpg | 5축 radar 3series, 카드의 80%/두 progress bar 확인. 본문을 실제 Roboto Condensed로 변경하여 카드 초과 해결. | 전체 복잡한 graphic background와 로고는 #e5e5e5 placeholder. radar 투명 채움·dash는 근사. |
| p10/s12 | round1/p10-s12.jpg, round2/p10-s12.jpg | 막대 실제 원본 폭32, 4그룹 값/색상 확인. Group C/D를 nowrap 및 충분한 label 폭으로 수정. | 일반 산세리프 폰트의 획/자간 미세차이. |
| p11/s11 | round1/p11-s11.jpg, round2/p11-s11.jpg | 4개의 3단 stacked chart, 값 총합20/30/36/50, 제목 y 위치 수정. | 원본 asterisk는 8개 spokes, Lucide Asterisk는 6개. body justify 간격 근사. |
| p12/s01 | round1/p12-s01.jpg, round2/p12-s01.jpg | 16/23/22/28/11 percent ring, 5행 legend·퍼센트 위치 확인. 제목 Inter와 본문 DM Sans로 수정. | ring 색상 및 항목 글꼴 자간 미세차이. |
| p13/s15 | round1/p13-s15.jpg, round2/p13-s15.jpg | 5색 budget stack, 0–5000축, 긴 축 값 box 폭 확대. 범례 간격·막대 모서리0 및 폭 수정. | 왼쪽 Roboto Condensed가 원본보다 좁음. 값은 시각 높이로 복원하여 세부금액은 근삿값. |
| p14/s05 | round1/p14-s05.jpg, round2/p14-s05.jpg | 4열 SWOT, 질문·bullet·헤더 확인. 마지막 열379px로 총1420폭 복원, DM Sans chip 헤더로 수정. | 로고 placeholder. 질문 본문의 Roboto Condensed 자형 차이. |
| p14/s13 | round1/p14-s13.jpg, round2/p14-s13.jpg | 13 whiteboard nodes/arrows, 타이머 안내·tip 확인. node font DM Sans, 실제 center 확인. | 로고 placeholder, arrow marker가 원본보다 큼. |
| p15/s02 | round1/p15-s02.jpg, round2/p15-s02.jpg | 4개 quarter card·색 bullet·timeline 확인. 본문/제목 DM Sans, 2026/Timeline 사이 간격 마지막 보정. | 글꼴 획/폭 일부 근사. |
| p15/s05 | round1/p15-s05.jpg, round2/p15-s05.jpg | 6개 KPI card, 값·보조문구·색 세로선 확인. DM Sans로 값 폭 복원, 선언 높이 최종 확장. | 원본보다 일부 값 글자의 폭이 약간 넓음. |

## 통합 검수 담당자 확인 요청

최종 round에서는 변경된 소스 해시·PNG SHA256을 반영해 25장 모두 재캡처하고 자동 finding 0건을 확인한다. p07 제목 및 p15 6개 KPI 값 높이 보정은 시각 위치를 바꾸지 않는 안전한 수정이다. p03/p06/p08/p15 마지막 미세보정은 원본/최종 비교에서 확인한다. 본 문서는 원본 일치도가 100%라고 주장하지 않으며, 기록한 Lucide/폰트 근사와 사용자 지정 placeholder 차이를 포함한다.
