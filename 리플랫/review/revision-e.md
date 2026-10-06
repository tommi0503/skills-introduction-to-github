# l37–l48 재검수 및 개선

담당 변경: `src/data/patch-e.ts`. 공유 CSS/UI/model/package는 직접 변경하지 않았다. 원본 이미지를 페이지 전체로 삽입하지 않았으며, 사진·복잡한 일러스트·기기 이미지의 회색 placeholder를 유지했다. 기본 지도·표·도형은 HTML/SVG 요소로 보완했다.

## 대조와 검증

- 기존 `comparisons/final`의 24개 앞/뒤 전체 비교 이미지를 실제 `view_image`로 확인했다.
- `node scripts/render.mjs --round=revision-e l37 l38 l39 l40 l41 l42 l43 l44 l45 l46 l47 l48`로 72패널과 24개 펼친 면을 출력했다.
- 1차의 전체 비교 24개 및 contact 12개를 실제 확인하고, 글꼴·줄바꿈·도형 순서·배경 누락을 수정했다.
- 2차의 전체 비교 24개 및 contact 12개도 실제 확인했다. 후속 수정 l38/l39/l40/l41/l43/l46, 실제 Allura400 적용 l42/l48은 같은 revision-e 회차에서 재출력·재확인했다.
- 최종 비교 산출물: `comparisons/revision-e/lNN-s01.jpg`, `lNN-s02.jpg`, `lNN-contact.jpg`. 펼친 PNG는 원본의 native 비율을 보존하며, 페이지 배율/1280×720 프레젠테이션 UI 규칙은 변경하지 않았다.
- l38–l48의 자동 layout findings는 0. l37의 −12도 회전한 표지 제목 3개는 회전 후 axis-aligned Range 측정이 텍스트 박스보다 4–6.5px 넓게 나오는 기록이 남는다. 실제 전체 비교에서 제목 잘림이나 패널 경계 침범은 확인되지 않았다.
- 단일 굵기 display face는 실제 400을 명시했고 Tinos는 실제 400/700만 사용했다. l42/l48 script는 실제 로드된 Allura400 normal로 적용했다. patch 좌표에 NaN/Infinity는 없다.

## 종류별 변경과 남는 차이

| 종류 | 구체 변경 | 남는 차이 |
|---|---|---|
| l37 뮤지컬 | MIRI/MUSICAL/미리뮤지컬을 개별 가시영역 폭·높이와 −12도 기울기로 교정. 캐릭터·CAST·무대 스틸 태그 기울기 복원. 연두색 별·구분선, QR 안내/공연 정보 크기 및 line-height 조정. | 원본의 독특한 손글씨 display 형태와 Jua/LilitaOne 차이가 남음. 사진 컷아웃은 회색 유지. |
| l38 가을빛 축제 | 지도 회색판을 실제 길·역명·공원 표식으로 재구성. Autumn/Colors/Festival 및 섹션 제목을 실제 굵은 face와 개별 inkFit으로 교정. 번호 달린 잎형 헤더, 행사 시간 위치, 카드 본문 밀도·문의 크기·점선 복원. | 원본의 둥근 custom display 자형과 휘어진 표지 상단 제목은 완전히 동일하지 않음. 복잡한 단풍 일러스트는 회색 유지. |
| l39 한우 선물 | 단순 녹색/크림 배경을 회색에서 원래 색 구획으로 복원. 표지 오목 코너 액자와 보증 메달/리본/이중 테두리 복원. 상품·가격·Point 라벨 크기, 온라인 주문 pill과 문의 문구·안전 배송 줄바꿈 조정. | 배경 질감·복잡한 문양과 작은 장식 로고는 생략/단순화. 상품 사진은 회색 유지. |
| l40 단풍 축제 | 표지 비즈/단풍/축제의 독립 크기·색·위치를 맞춤. 지도 실제 길/교차로/라벨 복원. 일정/행사 카드의 불규칙 곡선 외곽과 점선, 일정 본문·시설 문자 크기 교정. SVG를 내부 지도·카드보다 먼저 배치하여 가려짐 해결. | 원본 상단 바의 물결 경계와 일부 자연형 장식은 남음. 복잡한 잎 일러스트는 회색 유지. |
| l41 카페 | Tinos400의 가는 serif 제목 유지하며 CAFE/MIRIDANG의 가시 폭·높이, ROASTERY CAFE 두 줄 높이, 작은 subtitle 한 줄 폭 교정. 한글 본문을 Pretendard 실제 face로 조정하고 가격·메뉴 bullet·인용부호·영업시간 정렬 개선. | 원본의 매우 작은 본문 자형과 일부 작은 로고 형태는 차이. 사진은 회색 유지. |
| l42 연극 | recommendation/information/location/Introducing/Cast/Staff/Synopsis를 실제 Allura400 필기체로 교체. 섹션 헤더와 표지 제목 줄높이/크기, 공연 정보와 위치표 균형 및 흰 위치 점 복원. | 원본 필기체의 긴 일부 ascender/descender와 완전히 동일하지 않음. 배경 인물·출연진 복잡 일러스트는 회색 유지. |
| l43 인테리어 | Miri Design/Portfolio를 독립 Tinos700 가시영역으로 확대하여 원본의 제목 폭·줄간격 회복. System/Contact Us 등 가는 제목 Tinos400 교정. 흰 원 안의 집/대화 아이콘 filled 형상 복원. 연락처 본문, 本質 문구, 지도 교차로/QR 위치와 통계 숫자/작은 단위 계층 분리. | 연락처 전화 아이콘은 원본 handset 대신 filled 전화기 형태. 제목 serif 세부 자형과 일부 캡션 굵기 차이. |
| l44 비즈니스 센터 | 표지 MIRI/BUSINESS CENTER의 크기·행간·tracking·색 조정. One-stop/Contact/step 설명 크기와 표의 굵기 감소. 위치 지도 건물/지붕 도형 복원. | 작은 로고는 Lucide 대체 형태, 지도 라벨 미세 위치 차이. 사진/기기는 회색 유지. |
| l45 비상주 오피스 | Office Use/Main/Contact Us를 Tinos400의 가는 serif로 맞춤. 연락처/step/서비스 본문 크기·행간 조정. 5개 step 원형 filled 배경 보존. 회색 지도판을 실제 도로·교차로 번호/라벨로 복원하고 표/서비스 폭과 본문 밀도 교정. | 원본 아이콘 획과 미세 serif 형태 차이. 사진은 회색 유지. |
| l46 금융 파트너 | 전체 회색이던 단순 배경을 flat 주황 구획으로 복원하며 gradient를 추가하지 않음. Private Signature/Wealth 및 내지 heading의 크기·행간, 자격증/연락처/말풍선 문구 줄바꿈 교정. 표지 라벨/로고/No.1 바가 가려지지 않도록 배경 순서 수정. | 원본 gradient·복잡한 구름/마스코트/동전은 원요청 규칙상 재현하지 않음. 해당 이미지 회색 구획은 원본 컷아웃 실루엣과 차이. |
| l47 금융 서비스 | VVIP와 banker/contact 글자 크기, investment/tax/cycle 제목과 본문 줄바꿈 교정. 원형 아이콘의 teal filled 배경 유지. 원본의 teal 점 배열과 카드 구분선·표 글자 밀도 복원. | 작은 은행 swirl 로고는 Aperture 대체. 인물 컷아웃 사진은 회색 둥근 구획 유지. |
| l48 오케스트라 | gray 장식 원을 실제 민트/금색 수평 줄무늬 구로 복원. Greeting/Conductor/Orchestra/Program/Program Note와 ORCHESTRA/CONCERT를 가시 폭·높이로 맞춤. 단장 서명을 실제 Allura400으로 교체. 지도 도로·점, 경력·연주자 본문 크기와 문구 밀도 교정. | 원본 장식 곡선 그래픽과 글자 내 gradient는 생략/flat 색 사용. 줄무늬 구의 빛 번짐은 단순 기하로 처리. 사진은 회색 유지. |
