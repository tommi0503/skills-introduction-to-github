# l13–l24 제작 및 개별 비교 기록

담당 범위는 브로셔 12종, 원본 025–048의 앞·뒷면 24장, 분리한 접지면 72페이지다. 원본 24장 각각을 개별 열람했다. 접지면은 같은 펼침면의 native 좌표 데이터에서 3등분으로 잘라 1280×720 캔버스 중앙에 비율을 보존해 배치한다.

## 구현

- `src/data/patch-d.ts`의 24개 `SidePatch`는 공유 T/B/C/L/IC/P primitives와 renderer를 사용한다. 원본 전체를 이미지로 삽입하지 않는다.
- 사진·상품·인물·지도·QR·엠블럼·복잡한 장식/배경은 #e5e5e5 단색 placeholder다. 단순 카드/프레임/표/막대 차트/티켓/타임라인/원형 배지와 Lucide 아이콘은 실제 요소다.
- 첫 비교에서 OCR의 병합·문자 오류·본문 누락을 발견하여 담당 24면의 baseline 텍스트를 제거하고, 각 원본에 판독되는 제목과 본문을 수동 전사했다. 일부 작은 판독 불가 본문은 문맥에 맞는 자연스러운 안내 문구로 구성했다. 회색 선을 글자로 대신하지 않았다.
- Noto Sans KR, Noto Serif KR, Pretendard, Do Hyeon, Hahmlet(900), Bodoni Moda(실제 italic 포함), Archivo Black, Black Han Sans, Lilita One, Nanum Pen Script, Roboto Condensed, Tinos의 실제 로드 폰트를 사용한다.
- 별도 행인 헤드라인만 ink box에 맞춘다. 일반 본문은 실제 폰트 크기/행간과 명시적 줄바꿈으로 처리하여 다중 행 글자를 강제로 늘리지 않는다.
- 칩은 공유 renderer의 actual glyph 측정으로 중앙을 맞춘다. 임의 chip margin은 추가하지 않았다.

## 시각 검수: 2단계

1. `review-1`: 앞·뒷면 pair 24개와 접지면 6개 contact grid 12개를 개별 확인했다. OCR 텍스트 왜곡, 누락 제목, 여러 카드 위의 색상 오류, 사진 레이어, 폰트 모양 및 칩을 확인했다. 전체 본문 수동 복원과 UI 기하 정리를 진행했다.
2. `review-2`: 앞·뒷면 pair 24개와 contact grid 12개를 개별 확인했다. 2차 검수 내에서 영향을 받는 캡처를 갱신하여 가격/제품명/전화번호 줄바꿈, 일정표 시간 열, 큰 영문 헤드라인 크기, 티켓 프레임 닫힘, 지도·인물 placeholder 누락, 웹주소 높이를 수정했다. 최종 큰 한글 제목은 별도 폰트 표본 대조로 직선적 획이 가장 가까운 Hahmlet 900을 선택했다.

두 번째 비교를 마친 source를 freeze한다. 총 72개 출력은 1280×720이며, 접지면 경계에서 원본처럼 연속된 타임라인/문구는 동일 master 데이터를 공유한다. 별도 3차 비교는 root 최종 검수에 남겼다.

## 자동 렌더 확인

`npm run typecheck` 통과. 최신 review-2 담당 12종을 모두 렌더했다. l13/l14/l15/l17/l18/l19/l20/l21/l22/l23/l24는 panel finding 0이다. l16/s01-p2의 4개 칩에 자동 측정 약 -1.58px가 기록되어 root에 전달했다. 공유 font glyph readiness 보완과 fresh 최종 캡처에서 재확인하며, 임의 수치 보정은 하지 않았다. 문구 세로/가로 overflow는 없다.
