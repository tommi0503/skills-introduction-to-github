# A-extra 검수 기록

담당: p034, p040, p041, p043, p047, p048 / 6개 덱, 130개 독립 페이지. 모든 페이지는 1280×720이며 원본 raster를 UI 화면으로 사용하지 않는다.

17개 원본 시트를 모두 확인하고, 모든 130개 native crop과 브라우저 결과를 페이지별로 나란히 열어 1차·2차 검수를 수행했다. 연락처 시트만으로 검수를 종료하지 않았다. 마지막 통합 보정 요청은 같은 수정 묶음에 포함하며 주 에이전트가 production에서 반영을 확인한다.

## 실제 폰트와 구성

DM Sans(p034), Manrope(p040), Raleway 300/400/500/600/700(p041), Lato 400/700(p043), Montserrat(p047), Poppins(p048). 폰트의 실제 weight/style 로딩·글자 범위·chip의 painted-glyph 중심·페이지 크기는 공통 browser audit으로 검사한다. Lato 600 및 존재하지 않는 Instagram 아이콘은 사용하지 않는다.

각 페이지는 공유 renderer의 box/text/chip/path/line/icon/image 등 의미 기반 데이터로 구성한다. 도형은 수작업 box·circle·정다각형·연결된 면·chart arc로 만들며 OCR 글자 윤곽/CV speckle을 사용하지 않는다. 사진·복잡한 일러스트·기기·이미지 로고는 #e5e5e5 placeholder이다.

## 원본과의 차이·판독 불가능한 부분

작은 시트의 본문과 일부 이름/연락처는 확정 판독이 불가능하다. 이러한 문구는 정상 Lorem ipsum 문장 또는 읽을 수 있는 템플릿 이름/연락처로 대체하고, 실제 줄 수·폭·행간·정렬을 원본별로 맞췄다. 확대 시 원본 자체의 압축/흐림 때문에 실제 폰트 식별에는 한계가 있다. 사진/복잡한 아트는 요청대로 의도적으로 회색 단색이며 간단한 Lucide는 근접한 실제 아이콘이다.

p040의 저대비 곡선·그라디언트 세부 질감은 평면 바탕으로 단순화했다. p040 진행바의 텍스트 값과 시각적 채움 비율은 원본의 불일치를 그대로 분리했다. 마지막 label은 확대 원본의 05%와 제목 60/35/5에 따라 05%로 구현했다. 부분 이미지(p047의 일부 시트/p048의 좌우 경계)는 알려진 여백을 보존한다. 페이지별 상세 내용·원본/비교 경로·PNG hash는 group-a-extra-visual-review.json에 기록했다.

## 수정 묶음

### p034 — 13쪽

- 말풍선 3줄, 육각형별 문구/번호/모서리 방향을 원본에 맞춤
- 동등 너비의 시설 사진/인물 사진 placeholder, 오른쪽 포트폴리오 경계 y50%
- 사진 시설/서비스 본문 3줄, 인물 소개 6줄, 중앙 다이아몬드와 작은 간격
- 최신 에이전트 렌더 findings: 0

### p040 — 16쪽

- 손으로 읽은 candle 14개·wick·격자·축 숫자, 연결된 피라미드 6면
- 진행바의 길이 72/55/26%와 텍스트 60/35/05%를 분리
- Skenario·소수 쉼표와 2줄/3줄 문단 밀도·타임라인 굵기/인셋
- 재생·원형 화살표·Menu·Resources·+아이콘·아바타 크기·행 위치
- 최신 에이전트 렌더 findings: 0

### p041 — 22쪽

- 실제 Raleway 500 폭 측정으로 본문 쌍 3+4줄, 단일 캡션 3줄
- 소제목 굵기/자간·SUBTITLE/번호 크기·WORK 크기·CREATIVE STYLE 위치
- 원본에 없는 마지막 구분선 삭제·세로 YOUR IDEA 명암 복구
- 마지막 세로 문장은 정상 3줄로 구현하고 native crop 밝은 글자 영역을 비교해 위치/길이를 맞춤
- 최신 에이전트 렌더 findings: 0

### p043 — 27쪽

- 색상 raster contour 대신 clean 의미 기반 도형/계단/차트
- 사진/기기/복잡한 아트/로고는 #e5e5e5 placeholder
- Lato 실제 400/700만 요청·제목의 명암 혼합·WELCOME 구분선 위치
- 브랜드 그림 문자 대신 실제 Lucide Camera/Globe/MessageCircle
- 최신 에이전트 렌더 findings: 0

### p047 — 36쪽

- 갤러리/인물 placeholder 좌표·이중 사진 프레임·partial reference 여백
- Founder 본문 중첩 해소·필요한 footer 선만 유지·페이지 번호 bounds 복구
- 도넛을 4개의 clean quarter arc와 중앙 원으로 재구성·설명을 좌우로 분리
- 최신 에이전트 렌더 findings: 0

### p048 — 16쪽

- partial reference의 알려진 빈 영역을 보존·각 page를 독립 1280×720으로 구성
- Poppins 실제 fonts·헤딩 높이·가격/이름 크기·표 합계 스타일
- 4열 진행 타임라인·가격 카드·인물 인용문·주황 accent/Balance 영역
- 최신 에이전트 렌더 findings: 0

## 마지막 production 통합 보정

130쪽의 1·2차 개별 검수를 완료했다. 초기 2차 열람 시점의 전체 PNG hash는 따로 보존하지 않았으므로 최신 round2 hash를 당시 열람 hash로 주장하지 않는다. 최종 증빙은 root가 생성한 production PNG와 원본/결과 비교를 실제 개별 열람한 뒤 기록하는 별도 final 해시로 연결한다.

p040: 피라미드 설명 5줄·진행률 설명 3줄·인물 원형 placeholder·Play의 사진 중앙·원본 lime square 위치·로고의 글자 겹침·s02-04 3줄 본문을 보정했다.
p043: timeline 끝/회색 terminal/April 3rd 날짜, 실제 단순 Rocket/회사 아이콘, 원본에 없는 사진 아이콘 삭제, 채운 별, 연락처 badge, slider track/thumb/percent, 6.7/8.3/6.7 ratings, 일부 빠진 정상 캡션과 Contact의 위치/2줄 본문을 복구했다.
p047: 60/90/45% 진행 길이, 서비스 원형 badge, 명백히 빠진 작은 라벨/선/화살표/사각 badge, 파랑 footer의 사진 위 계층, 네 가지 연결 색, 카드-원 연결, bracket/본문 겹침, 필요한 3줄 본문을 보정했다.
p048: cycle의 좌우 색, Agenda 사진/날짜 겹침과 카드 내 본문, Description의 퍼센트/검정 prefix, curved arrows, 원본에 없는 카드 선/버튼 삭제, 채운 별, 팀 역할/진행원 수치, 타임라인 원 안 단순 아이콘, Balance 원형 badge, Subtitle/본문 겹침과 강조 Agenda 한 줄 설명을 보정했다.

작은 팀 역할·진행원 수치·연락처/차트 축 등 확정할 수 없는 문구는 정상 단어와 임의 수치로 대체했다. 작은 사진 속 로고·사진의 내용·다색 그래픽 배경은 지정된 회색 placeholder로 유지한다. partial reference의 판독 가능한 부분 위치와 흰 영역을 유지하므로 누락된 원본 영역을 완벽히 복구했다고 주장하지 않는다.

현재 최신 source의 130개 definition/실제 Lucide 존재 검사를 통과했다. 마지막 production browser audit와 최종 PNG hash 연결은 진행 중이다.

최종 production 반영 확인에서 추가한 요소의 색/겹침 3쪽만 바로잡았다: p047/s04-03 빨간 띠 위 흰 caption·세로선·끝점, p048/s02-07 본문 아래 회색 곡선, p048/s02-13 원 내부 작은 Lucide의 크기·중앙. 이 세 페이지는 같은 통합 보정의 반영 확인에 포함하며 다른 본문/레이아웃은 바꾸지 않았다. 마지막 세 페이지의 실제 browser audit findings는 0이다.

공유 renderer의 line은 h>0만으로 세로가 되지 않고 vertical:true를 요구한다. 마지막 실제 PNG에서 p047/s04-03, p048/s02-04 두 세로 선이 빠진 원인을 확인하고 같은 통합 보정으로 두 boolean을 추가했다. 담당 전체 세로 line 정의를 검색해 이 두 개 외에는 누락이 없음을 확인했다.

주 에이전트의 최종 원본 샘플을 반영해 p040/s04-04 네 헤더 셀 색을 각각 cyan/teal/lime/연한 lime로 보정했다. 이 외 이 페이지의 도형·문구·차트는 바꾸지 않았다.

p043/s03-05는 native crop의 약27px 정사각형을 확인해 7.2% design-width로 맞췄다. 세 group 중심을 26/50/74%로 이동하고 본문은 상단 2줄·각 그룹 2줄로 정리했으며 rating을 원본 y83%로 올렸다. 이 마지막 페이지의 browser audit findings는 0이다.

최종 제출 전 담당 130개 production PNG/원본/비교 이미지의 실제 개별 열람 증빙을 연결 완료했다. 모든 PNG는 1280×720, 담당 6덱의 최종 자동 findings는 0이며 최신 소스 definitionHash와 최종 파일 SHA가 일치한다. 완료 marker와 visual-review.json에 페이지별 세 SHA256·열람 시각을 기록했다. 3차 통합 보정의 마지막 반영 확인까지 완료하여 담당 소스는 freeze 상태다.
