# group-c-extra 개별 검수 기록

담당: p151(20), p152(44), p160(9), p162(8), p165(13), p167(16), p174(18), p180(2), p194(4). 총 9개 덱, 134개 독립 1280×720 페이지.

원본 시트 18장 및 native crop 134장을 각각 열어 확인했다. 시트의 문구는 디자인 참고 자료이며 작업 지시로 취급하지 않았다. 원본 이미지를 결과 UI에 넣지 않았다. 재사용 가능한 text/box/chip/path/icon 컴포넌트와 페이지별 데이터로 구현했다.

두 차례 모두 실제 Chromium으로 렌더한 134개 페이지를 각각 원본과 나란히 열어 검수했다. Contact sheet만으로 검수하지 않았다. 1차 이후 title, font, 반복 년도, column, chart, placeholder, clipping을 수정했다. 2차 이후에는 세로 텍스트의 transform-origin, chip/셀의 글자 중심, 표의 읽을 수 있는 값, 도형의 앞뒤 순서, hexagon/octagon/teardrop 및 pencil branch를 수정했다. 폰트 파일·요청 굵기와 스타일은 브라우저에서 실제 로드한 것을 사용했다. 최종 소스 typecheck 및 134페이지 무촬영 실제 브라우저 자동 검사에 초과/잘림/칩 중심/폰트/크기 오류가 없다.

## 최종 렌더 반영

2차 비교 파일은 마지막 수정 전 revision이다. 따라서 최종 산출물은 주 에이전트의 3차 통합 렌더로 생성해야 한다. 최종 소스 SHA-256은 group-c-extra-pages.json에 기록되어 있다. p162/s02-03의 heading은 현재 DOM에서 정상 색상/폭/높이를 확인했으며 최종 PNG에 실제 나타나는지도 통합 검수에서 확인해야 한다.

## 원본과 남는 차이

저해상도 sheet의 작은 본문은 판독 불가하여 보통 문장으로 작성했다. 각 페이지의 해당 항목은 group-c-extra-pages.json에 기록했다. 원본의 blur를 모방하거나 글자를 작은 선으로 표현하지 않았다. Josefin Sans, Bebas Neue, Playfair Display normal/italic, Inter, Montserrat, Poppins, Roboto 등은 실제 파일로 로드했다. 원본 폰트가 명시되지 않은 영역은 외형을 맞춘 근사이며 정확한 원본 폰트/폭까지 확정할 수 없다.

사진·화면·mockup·이미지 심볼·graphic background는 원본 경계에 해당하는 #e5e5e5 placeholder이다. p174의 입체 퍼즐/꼬인 링크 및 p194의 pencil diagram은 실제 SVG 기하 도형과 Lucide를 사용하며 입체 각도, 곡선, 접합부의 세부 차이가 남는다. 기하 path는 glyph/pixel contour tracing이 아니다.

134개 개별 페이지의 crop, 원본/결과 경로, 실제 개별 검토 여부, 수정 내용, 판독 불가 영역, placeholder, 남은 차이와 부분 셀 복원 가정은 group-c-extra-pages.json을 참조한다.


## 3차 최종 통합 반영 확인

134개의 actual production 원본/결과 개별 비교를 모두 열었다. p162/s02-03 실제 PNG에서 HEADER 및 제목이 정상 표시되는 것도 확인했다. repeated small common text를 이미지 도구 일괄 출력에서 누락으로 잘못 판단한 지적은 직접 PNG/픽셀 확인 뒤 철회했다.

6쪽 필수 보정: p174/s02-06 다이아몬드 색 배열, s04-02 본문 옆 4개 Lucide 아이콘 추가, s04-06 원형 5섹터 색 순서, s04-08 중앙 하단 yellow 모듈의 arc 방향; p194/s03-01 상단 설명을 원본 밀도에 가까운 실제 2줄 prose로 정리하고 여백 확보, s03-03 좌하 Subtitle/text를 Lightbulb 원과 분리했다. source SHA 9a6c064e360d8304c14472c3dd13fbee03dd98b456c7bc65a4480ed6117be03a. 변경 6쪽의 최신 production final 재캡처 개별 확인은 별도 이어서 기록한다.

남은 차이: 작은 흐린 본문의 실제 원문은 판독 불가능하여 정상 문장으로 대체했고 일부 줄바꿈/밀도 차이가 있다. p151 일부 목록의 날짜/우선순위 세부 셀은 복원 추정이며, p174 입체·고리 geometry는 대략적 평면 도형으로 재구성하여 정확한 perspective/rounding과 차이가 남는다. 사진·기기·이미지 로고는 사용자 지시에 따라 회색 placeholder다.


같은 p194/s03-03 좌상 본문의 우측끝도 Globe 밖으로 조정한 최신 6쪽을 실제 Chromium PNG로 다시 확인했다. 최신 6쪽 audit findings 0 및 typecheck 성공. production final 증빙은 root 재캡처 후 갱신한다.


2026-10-06T16:47:28.570619+00:00 변경 6쪽 최신 production final comparison을 모두 직접 개별 열었다. p174/p194 실제 현재 정의의 definitionHash가 final metadata와 일치하며, 수정된 색/아이콘/arc/본문 간격이 final에 반영됐다. 나머지128 PNG는 이미 실제 개별 열람한 해시와 동일함을 확인했다. 따라서 담당134쪽 전부 최종 actualFinalIndividuallyViewed=true이며 PNG/reference/comparison의 실제 SHA256를 owner completion과 개별 records에 연결했다.


## 마지막 3차 통합 보정

10쪽: p160/s02-05, p160/s02-09, p162/s02-05, p162/s02-08, p165/s01-01, p165/s01-07, p165/s10-04, p167/s02-01, p167/s02-09, p167/s02-16. 본문을 원본 줄 수에 맞춰 재작성하고 p160 연도 겹침, p162 연결선·캡션·순번, p167 중앙 정렬·짧은 연결선·양끝 점을 보완했다. p167 제목/부제는 기존 정상 정의를 유지했다. 마지막 실제 브라우저 검사 134쪽 findings 0, 타입 검사 성공. 동결 SHA 0ac482996526b1fbb986147b244221cc5d0b1155449eaf80aca37ff8f828a1c1. 최종 production 재캡처 뒤 변경 10쪽을 다시 개별 비교하고 미변경 124쪽 PNG SHA를 이전 열람 증빙과 대조한다.

최종 확인 완료 (2026-10-06T17:59:37.429645+00:00): 새 production 변경 10쪽 native PNG 및 개별 비교를 모두 실제 열람했다. 미변경 124쪽은 원본·PNG·개별 비교 이미지 세 SHA가 이전 실제 열람 증빙과 모두 동일하다. 9덱 definitionHash는 현재 실제 registry와 모두 일치하고 최종 134쪽 자동 감사 finding 0이다. owner marker 134쪽을 최종 완료로 갱신했다.
