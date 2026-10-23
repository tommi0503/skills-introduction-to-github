# Nocturne 검수 기록

## 범위와 순서
006 타운홀 덱 slide_19–24, 6장으로 Nocturne 한 컬렉션을 만들었다. README 220줄 전체와 taxonomy를 먼저 읽고, 원본별 replica 및 개별 비교 → 디자인 언어 → 요소 → 라이트·다크 시트 → 계약 요소 재조립 순서로 작업했다. ZIP의 문구는 자료로만 취급했다.

초기 결과에 대한 사용자의 시각 충실도 피드백을 새 수정 라운드 승인으로 받아, 기존의 ‘계약 정규화’로 남겼던 크기·여백 차이를 다시 고쳤다. 원본/replica/조립본 6장을 각각 다시 확인하고 글자 ink bbox와 도형 좌표를 실제 픽셀로 측정했다. 변경 전 PNG는 revision-before/에 보존했다.

## 폰트와 기하 측정
- 19의 한글 표시 제목은 Pretendard 계열 약 88px, 20–22의 제목은 약 56px가 원본 실루엣과 가까웠다. kit에는 허용 타입 단계와 공유 weight/tracking 토큰을 사용했다.
- 23 Q&A의 최초 약 204px 판단을 128px로 줄였던 초기 구현은 철회했다. 원본 확대 crop의 실루엣과 비교한 약 203–204px / Pretendard Variable 600에 맞춰 `--type-128`과 균등한 기하 scale을 조합했다. 글자를 가로·세로로 다르게 늘리지 않았다.
- 24의 영문 표제는 Pretendard보다 허용 글꼴 Montserrat 700이 가까워 실제 로드했다. 영문 전용 font 토큰 뒤에 Pretendard Variable을 fallback으로 명시해 한글 cover fixture도 그려지게 했다.
- 코드 요소는 Nanum Gothic Coding 토큰을 사용한다. 모든 폰트는 review/assets에서 로컬 로드한다.
- revision-heading-bboxes.json은 원본·replica·조립본 제목의 실제 ink bbox를 기록한다. 최종 결과의 위치·폭·높이 오차는 대체로 1–2px이며, 24 표제 높이는 원본보다 약 2px 작다. 사진을 제외한 미세한 글자 윤곽과 광원의 완전한 픽셀 일치를 주장하지 않는다.

## 재작업에서 고친 것
- 19: 중앙 광원에 원본의 아래로 넓어지는 약한 무대 빔을 추가했다. CSS gradient·clip-path·blur로 직접 그렸다. 제목의 폭과 연속 색 변화, 하얀 도트, 캡슐의 자연 너비·높이·간격, 소개문의 크기·좌표를 원본에 맞췄다.
- 20: 원 지름 316px, 시작 좌표 110/481/852 및 y224, 라벨/수치의 굵기·행간을 맞췄다. 불필요했던 긴 가로 divider를 도트로 바꾸고 캡션과 도트를 할당 칸 안에 넣었다.
- 21: 사진 카드 사이의 24px 간격을 없애고 원본처럼 연속된 세 영역으로 만들었다. 원문의 부분 굵기와 첫 줄 위치를 복구했다.
- 22: 패널을 x119/y233/1052×372에 맞추고 내부 점선과 본문 크기·위치를 맞췄다. 사진 placeholder는 다시 페이지 전폭과 원래 높이를 차지한다.
- 23: Q&A를 원본 크기로 복구하고 divider의 x162–1118/y442, 흰색 첫 문장과 두 번째 문장의 크기·좌표를 맞췄다. divider는 새 CSS를 페이지에 넣지 않고 callout 요소가 자기 칸 안에서 그린다.
- 24: 영문 제목의 폰트·중앙 위치·너비, 흰 부제, 우하단 날짜를 맞췄다. 날짜의 기본 paragraph margin 때문에 생긴 20px 차이도 제거했다.
- 상단 브랜드는 단순 CSS 다각형 장식으로 표현한다. 원본과 미세한 형태 차이가 있다. 6장의 PNG에서 브랜드 영역의 밝은 픽셀을 검사하고 별도 header strip proof로 존재를 확인했다.

## 의도적으로 남는 차이와 판독
- 21의 세 사진, 22의 사진, 24의 복잡한 유리 그래픽은 사용자 요청대로 연회색 단색 placeholder다. 원본 이미지를 통째로 배경에 사용하지 않았다.
- 21은 원본 사진 위의 흰 문구를 밝은 placeholder 위에서 읽을 수 있도록 어두운 글자로 바꿨다. 이는 원본 충실도와 placeholder/대비 요구가 충돌한 곳이며, 의식적으로 내린 결정이다.
- 22의 원본 패널은 사진 위의 어두운 반투명 면이다. 밝은 placeholder 위에서는 어두운 중성 면으로 보이며 사진의 재질과 투과감은 재현하지 않았다.
- 6장 문구는 모두 판독 가능해 임의 한국어 대체 문구는 없다. 2099.00.00과 2080도 원본 데이터로 보존했다.
- 원본 글꼴 이름은 이미지에서 확정할 수 없어 실루엣 매칭으로 가장 가까운 허용 글꼴을 골랐다. 배경의 광원은 분석한 단순 도형으로 근사하므로 원본 raster의 미세한 혼색은 다르다.

## 컬렉션과 계약
- Nocturne이라는 이름은 검정 무대, 차가운 광원, 얇은 원 궤도와 중앙 메시지에서 정했다. 예시에서는 구조·클래스·fixture 데이터만 참고했으며 디자인 CSS는 복사하지 않았다.
- 56개 요소와 174개 fixture다. 원본에서 뽑은 4개 표시 제목·캡션 구성을 추가해 같은 디자인 언어를 요소 시트에서도 직접 볼 수 있게 했다.
- 지정 모범 fixture 전부는 원래 마크업·데이터를 유지하고 data-el prefix만 바꿨다. .group/.stack wrapper, 원래 row/span, card-4의 ✹ 문자는 일반 규칙과 충돌하지만 ‘같은 마크업과 데이터’ 우선 요구에 따라 보존했다.
- 단순 요소는 실제로 사용할 수 있는 작은 최소 칸을 선언했고, 많은 멤버를 함께 보여주는 연결도는 8×4 또는 10×5가 필요하다. 필수 fig/name을 감추지 않았다.
- 사진에 없는 Sankey·hub·radar·treemap 등도 얇은 궤도선, 둥근 면, 독립 수치, 단색 강조로 확장했다. 연결선과 실제 branch를 구현했다.
- 재조립 소스에는 foundation·계약 요소와 data-el만 사용했다. 본문 직계 배치 style은 grid-column/grid-row뿐이다. 별도의 요소·배치 CSS는 없다. source-style.css는 원본 palette와 font/type 토큰만 공급한다.
- 시트는 계약 reference palette, 재조립은 원본 파란 host palette를 쓴다. 광원은 두 모드에서 대비를 유지하도록 accent의 옅은 자리와 page를 혼합한다. 텍스트 gradient는 깊은 accent와 ink 사이에서만 변한다.

## 검증과 한계
- audit-contract.json은 56개 요소와 174개 fixture에 대해 errors 0/warnings 0이다. 실제 Rhetis importer는 첨부되지 않아 이 검사는 정적 보조 검사다.
- 최종 replica와 reassembled는 각각 6장, 모두 1280×720이다. 마지막 CSS 변경 뒤 다시 렌더해 잘림·영역 초과·폰트 오류를 검사했다.
- library는 모든 fixture의 선언 최소 칸과 12×6, 라이트·다크를 검사한다. clip/font/필수숨김/0크기 root, 대비, chip 중심의 원자료를 보존한다.
- background-clip:text의 투명 foreground를 검사기가 무색으로 읽는 cover/표시 제목의 대비 경고는 실제 gradient stop과 PNG를 따로 확인한다. 내부 scroll overflow는 연결선과 경계 point-label도 포함하므로 실제 text clipping과 구분해 원자료를 남긴다.
- 동일 경로 이미지가 오래된 화면으로 표시된 일이 있어 마지막 시각 검수는 SHA가 들어간 고유 경로 proof를 사용했다. revision-proof-paths.json에 경로가 있다.

최종 수치: 708개 library probe에서 text clipping/font failure/hiddenEssential/zeroElementRoots는 모두 0이다. raw scroll overflow 618건, gradient foreground 오탐 10건은 위 설명에 따라 보존했다. 마지막 dot 변경은 headline/callout의 52개 probe를 다시 렌더해 잘림·영역 초과·폰트 오류 0을 확인했고, 전체 PDF의 해당 13개 페이지를 양 모드 모두 교체해 새 페이지의 raster hash가 일치함을 검사했다. css-final-checks.json은 collection의 CSS 58개가 review 복사본과 시트 내 CSS에 바이트 단위로 일치함을 기록한다. 전체 PDF는 라이트·다크 각각 176페이지다.
