# Inflexion 검수 기록

## 범위와 제작 순서

011_1ku2l_파랑의_트렌드한_IR_덱의 원본 20장(모두 1280×720)을 담당했다. reference README 전체 220줄과 taxonomy, kit-token, palette, type-step 계약을 읽은 뒤 원본 목록을 정리했다. replica 20장을 먼저 DOM·CSS·직접 그린 SVG로 재현하고 원본과 개별 비교한 다음 디자인 언어를 도출했다. 그 뒤 foundation 및 계약 요소 56개를 만들었다. 요소 fixture는 172개다. 지정 모범 fixture 28개는 prefix만 바꾸고 마크업·데이터를 보존했다.

초기 재조립에서 원본의 큰 형태를 일반적인 카드·단일 비율 도넛·선형 단계로 바꾼 것은 잘못이었다. 사용자의 재검토 지시 후 이를 수용 가능한 차이로 처리하지 않고 20장 모두를 다시 작업했다. 수평 rule, 큰 둥근 면, 산의 겹침, 계단형 막대, 낮은 capsule, 반원 궤도, 반환 화살표, 세 조각 차트, 교차 일정, flowchart, 전폭 띠를 계약 요소의 재사용 가능한 semantic variant로 복원했다. 이 추가 수정은 사용자의 새 지시에 따른 수정 회차다.

재조립은 컬렉션 foundation과 계약 마크업·data-el을 사용한다. body 직속 요소의 배치는 12×6 grid-column/grid-row다. 각 페이지에 좌표 변수를 심어 우회하지 않았다. review/assets/collection에 복사한 CSS 58개는 컬렉션 원본과 같은 바이트이며, review ZIP만 풀어도 링크가 열린다. source-style.css는 호스트가 공급하는 원본 팔레트·타입 크기 선언뿐이다.

## 원본과의 차이·판독·결정

|페이지|복원과 남은 차이|
|---|---|
|01|세 3D 장면을 각각 회색 placeholder로 치환했다. 긴 상단 rule의 굴곡, presenter, title, subtitle, 두 pill을 복원했다. 회사 심벌은 단순한 세 막대로 근사했으며 원래 로고와 다르다.|
|02|상단 furniture, Contents, 번호·점선·영한 목차 두 열을 복원했다. 읽히는 문구는 전사했다.|
|03|오른쪽의 큰 둥근 강조면, 겹친 두 원과 제품 원, 화살표, 네 날짜, What We Do 원문을 복원했다. 아이콘은 Lucide 선형 아이콘이므로 원래 채움 아이콘과 다르다.|
|04|MISSION/VISION 라벨, 중앙 수평선, 원호·원점, 두 이미지 자리와 원문을 복원했다. CSS 원호의 곡률은 원본과 미세하게 다르다.|
|05|반원 gradient 배경, 가운데 항목의 낮은 배치, 고정 폭 capsule, 하단 headline과 rule을 복원했다. 세 3D 장면은 placeholder다.|
|06|겹친 세 산의 둥근 정상·높이·순서, TAM/SAM/SOM과 설명, 500/50/17 trillion을 복원했다. SAM/SOM 설명은 흰색이다. 원본 수치가 화면 아래에 의도적으로 걸치므로 replica·재조립 모두 같은 crop을 보존했다. 자동 clip 6개는 이 세 숫자와 세 단위다. 초기에 수치를 위로 밀어 넣은 처리는 취소했다. 정상 곡률과 gradient 분포는 미세한 차이가 있다.|
|07|붙어 있는 네 계단 막대와 내부 15/30/50/70%, 연도, Key Drivers capsule·rule·목록을 복원했다. 판독이 애매한 마지막 설명은 “고객이 선호하는 비즈니스 문화의 확산”으로 작성했다.|
|08|세 낮은 capsule, 상단 Problem pill, 점선, 전체 설명, 전폭 하단 gradient 띠와 두 텍스트 역할을 복원했다. 전구는 Lucide 선형 대체다.|
|09|반원 궤도·번호 세 개·아이콘·전체 설명, 하단 양쪽 rule과 두 제목을 복원했다. 중앙 3D는 placeholder다. 선형 Lucide와 원래 채움 아이콘의 모양은 다르다.|
|10|상단 세 개·하단 왼쪽 방향 두 개의 5단계 반환 도형과 오른쪽 세 설명을 모두 복원했다. CSS 닫힌 chevron과 원본 열린 화살표 끝의 세부가 다르다.|
|11|30/55/15 실제 세 섹터 ring, 세 범주, 두 panel·capsule, 축 숫자, 20/40/70 area를 복원했다. 단일 share로 축약했던 처리는 취소했다. ring의 구멍 비율은 지름의 40%다.|
|12|세 이미지 placeholder, 교차된 일정, 반원 gradient, y418 수평선, 날짜·원문을 복원했다. 이미지 장면을 회색 사각형으로 치환하므로 원본의 반원 배경 일부가 가려지는 차이가 있다.|
|13|세 차트의 모든 값·축 숫자·연도·capsule을 복원했다. bar의 1·3·5번째가 강조이고 나머지가 중성이다. area 채움은 gradient다. 축 라벨·점 라벨 위치와 면의 채도는 작은 차이가 있다.|
|14|610×498 포지셔닝, 네 점, 세 낮은 gradient card와 원래 기술/비즈니스 모델/네트워크 문구를 복원했다. 판독 가능한 카드 문구를 일반문구로 바꾼 초기 데이터 오류를 수정했다.|
|15|15/55/30 실제 세 섹터 solid pie, 고객 세 범주, 진입시장 두 역할 caption, 원문 note, 선정 이유 pill·점선을 복원했다. 3D는 placeholder다. caption과 pie의 지름은 원본을 기준으로 보정했다.|
|16|시각·객체 식별·암·그리퍼·포장·패킹·컨베이어의 7개 node와 점선 flowchart, 오른쪽 두 panel 및 인증서 placeholder를 복원했다. 원본 점선의 세부적인 방향 표식은 CSS 경로와 다르다.|
|17|중성 3개와 강조 1개의 gradient 막대, 내부 70%, 위로 휘는 화살표, 하단 rule, 모든 가정을 복원했다. 첫 세 막대에는 원래 수치가 없으므로 높이만 35.8/33.7/54.8(마지막 70 기준)의 상대값으로 추정하며 숫자를 화면에 새로 표시하지 않았다.|
|18|아홉 마일스톤을 전부 9열로 복원하고 phase 세 capsule, 점선, 하단 화살표 rule을 구현했다. 원본 복합 아이콘은 의미가 가까운 Lucide다.|
|19|지름 200의 네 사진 자리·chevron·경력 목록과 전폭 gradient 띠를 복원했다. 사진은 회색 원형 placeholder다. 목록 전체와 세 텍스트 역할을 유지했다.|
|20|중앙 5 billion, gradient figure·pill·점선, 높이 367의 두 시리즈 area, 네 개 자금 사용 항목을 두 열로 복원했다. OO%/O% 같은 템플릿 값은 추정 수치로 바꾸지 않았다.|

원본 폰트 파일명·가변축 정보는 이미지에서 확인할 수 없었다. README 글꼴 범위에서 Pretendard Variable을 실제 로드했고 코드에는 Nanum Gothic Coding을 실제 로드한다. 원본과 폰트 metrics·굵기·자간이 완전히 같다고 주장하지 않는다. 원본의 두께·크기·줄바꿈을 기준으로 보정했지만 글자 폭과 baseline의 미세 차이가 남는다.

## 라이브러리 결정과 검사 해석

컬렉션 명은 가는 긴 수평선이 가운데에서 휘어 연결되는 모티프의 Inflexion이다. 원본 색 자체를 CSS에 고정하지 않고 주 강조·깊이·중성 역할로 옮겼다. 라이브러리 라이트·다크는 README palette, 원본 조립본은 원본 palette supplier를 사용한다.

모범 fixture의 ✹와 wrapper 등은 동일 마크업 요구를 우선하여 유지했다. 다른 legacy ul/li는 한국어 내용은 유지하면서 .list[data-el] > .item > .name으로 정규화했다. 가격표 추천 표식도 tag data-el이다. 원본에 없는 요소도 같은 가는 선, capsule, 큰 둥근 면, 단순한 글자 위계로 설계했다.

정적 계약 검사는 요소 56개·fixture 172개에 대해 오류 0, 경고 0이다. 이는 실제 Rhetis 서버 반입 성공을 대신하지 않는다. 브라우저 검사는 페이지 크기, 글자 clip, overflow, font failure, chip 정렬, 대비, script 오류를 기록한다. 연결선이 다음 node로 이어지거나 0폭 data anchor 밖에 라벨을 놓는 구조와 full-bleed 장식은 raw overflow로 잡힌다. 이를 실제 글자 잘림과 같은 오류로 숨기지 않았다. 의도적인 P06 하단 crop만 별도로 분류한다.

pie는 부모가 최소·최대 및 중간 478개 슬롯을 검사했다. clip/overflow/font/hidden/zero 0이며, pseudo 배경을 인식하지 못하는 raw 대비 flag는 실제 8개 색짝을 canvas로 따로 확인했다(최소 비율 4.987). 해당 감사 JSON을 함께 보존한다. 마지막 수정 후 모든 페이지 PNG·비교 PNG·PDF와 라이브러리 시트를 다시 생성한다.

## 마지막 통합 수정과 동결

부모의 20장 개별 검수 후 P04 누락 원호 두 개, P05 rule 끝 hook, P07 driver 번호·본문 좌표/줄바꿈, P09 하단 caption 높이, P11 plot의 bbox, P16 위·아래 별도 분기, P17 점선 끝 dot를 수정했다. P16의 세로선이 사라졌던 원인은 pseudo의 content-box 폭에 border가 더해져 clip-path 바깥으로 나간 것이었으며 border-box로 고쳤다. P19 nested list는 글자가 overflow로 보이면서 root 높이가 0이던 오류가 있어 2행/3행의 실제 높이를 복구했다. 일반 pill-stack의 line root 폭 0과 작은 note의 대비도 고쳤다. 사용되지 않던 잘못된 nested :has selector는 삭제했다. 최종 crop을 주 에이전트와 각각 확인했다.

원본의 낮은 대비도 원본과의 차이 기록에 포함한다. 원본 supplier의 연한 보조 시리즈 수치와 두 번째 pie의 흰 55% 등은 원본 자체의 색 조합을 보존하여 자동 대비 경고가 남는다. 이 원본 재현의 경고를 README 기본 라이트·다크 팔레트의 요소 대비 검사와 구분한다. 라이브러리 기본 팔레트에서는 실제 전경/배경 대비를 별도로 검증하며 source 복원의 색 경고를 숨기지 않는다.

마지막 요소 시트 실검수에서 강조 headline의 최소6×2 안에 제목·note가 면 밖으로 내려가고 headline-stack의 seat가 제목 뒤에 겹치는 오류를 추가 발견했다. fixture 마크업과 최소 칸은 유지하고 compact padding8px·gap4px·28/14px 위계 및 stack 제목56–72px 높이로 수정했다. light/dark 해당 PNG와 전체174p PDF의75–80p를 최신 브라우저 렌더로 교체했다. 재조립20장에는 해당 compact selector가 일치하지 않아 HTML/PNG SHA가 그대로임을 별도 JSON으로 검증했다. 최종 통합 감사는700probe이며 clip/font/hidden/zero/script 오류0이다.
