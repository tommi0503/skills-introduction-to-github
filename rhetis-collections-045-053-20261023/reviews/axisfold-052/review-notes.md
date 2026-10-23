# Axisfold 052 검수 기록

## 범위와 제작 순서

052 덱20장 전체를 각각 열었다. `inventory.md`에 페이지 유형과 계약 요소 대응을 기록했다. README 전체를 읽은 뒤 standalone replica20장→개별 원본 비교→디자인 언어→56요소/170fixture→요소 시트→foundation/계약 요소만의 재조립20장 순서로 제작했다. 샘플은 fixture 마크업·데이터와 폴더 구조만 참조했으며 샘플 CSS 디자인은 사용하지 않았다.

## 원본 복원과 발견한 결함

초기 재조립에 있던 목차의 잘못된 세로 구성, 장표지 누락, 관계도를 카드로 바꾸는 문제, 긴 원문 축약, 표 행 잘림은 거절 대상으로 처리하고 수정했다. 차이를 추상화라고 승인하지 않는다.

- 08의 core와 5패널을 원본 bbox로 복원했다. core208×208, left440×118(3개), right440×118(2개), 직각 커넥터·5끝점·실제 SVG 아이콘·원문2행 note를 적용했다.
- 03/16의 사진은 연회색이며 원본의 연결 모듈 마스크 외곽을 editable CSS vector path로 복원했다. 모서리 장식도 사진과 분리된 SVG 기하이다.
- 04의 교집합을 실제 렌즈로,12의 세 원을 삼각 교집합으로,15를6분할 annulus로,17을4노드 궤도로 복원했다.
- 06 조직8행·합계 진한 띠·재무현황·2026열 강조·원 단위,10의 막대/선/면 공통 플롯과 서비스명,11의2×2사업 카드와 매출비중을 복원했다.
- 05의 마지막 혁신/글로벌 문장,07의 긴 연혁 bullet,13의70%실적/서비스·성과 pill,14의6개 서비스 원문,18의8개 고객사명/파트너 고유명사,19의원문·연도·수치를 복원했다.
- 원본 범위에 없는 요소도 같은 형태·선·위계로 구성했다. balance의 실제빔·지지대·행거와 tilt부호, bullet의 targettick, waterfall의 연결선 및 누락된+43신규사업, slope/dumbbell의 데이터 기하, sparkline의 연속선, flowchart/swimlane의4방향 화살표를 별도 점검했다.

## 실제 글리프 측정

눈대조만으로SUITE를 골랐던 결정을 철회했다. 제공된 실제 폰트 파일을 브라우저 Canvas로 렌더하여 원본 텍스트 crop의 글리프 bbox/F1을 측정했다. 전체 픽셀을 늘이거나 기울이지 않았다.

|원문 영역|채택/비교 근거|
|---|---|
|08 제목|Pretendard Variable48px/600/자간+0.5px. 원본bbox358×44, 렌더358×43, F1.9079.700은.9061, NotoSansKR700/-1.5는.9021.|
|08 첫 note|Noto Sans KR16px/400/자간0. 원본/렌더bbox137×14, F1.8230. 같은bbox의Pretendard는.6187.|
|08 작은 한글 라벨|Pretendard Variable16px/500/자간0, 원본80×14/렌더80×15, F1.7708.|
|08 파란 영문 이름|Freesentation22px/600/자간0, 원본99×19/렌더99×21, F1.8291. 색 있는 글자 threshold를 사용한 비교라 경계 AA 차이가 남음.|
|08 흰 core|Pretendard Variable26px/600/자간−1px, 원본141×17/렌더141×18, F1.8270. 반전한 흰 글자 threshold 비교.|

공식 라이브러리 시트는 `contract/type-steps.json`의 정상 타입 단계를 그대로 쓴다. 08의 note는 컬렉션 CSS에서 `--type-16`을 사용한다. 다른 역할까지 축소하던 전역 `--type-18:16px` 호스트 매핑은 제거했다. 표지 연락처에만 호스트 `--type-20:19px`를 공급한다. 컬렉션 CSS의 `font-size`는 정상 `var(--type-N)`만 사용하며 불법 타입 이름이나 페이지별font-size CSS는 만들지 않았다. 가는 본문은 Noto Sans KR, 제목과 축라벨은 Pretendard Variable, 문화 영문 이름은 등록된 private font token으로Freesentation을 로드한다.

## 원본 색 실측과 자리

큰 면의 최빈 RGB를 측정하여 replica/검수 호스트에만 공급했다. 컬렉션 CSS는 팔레트 자리만 쓴다.

|역할|원본 modal RGB/호스트 값|자리|
|---|---|---|
|rail|69,159,249 / #459ff9|`--a4`|
|원형 blue1|80,126,193 / #507ec1|`--a2`|
|원형 blue2|77,142,232 / #4d8ee8|`--a3`|
|중립 core|72,72,72 / #484848|`--n-9`|
|회색 페이지|244,246,248 / #f4f6f8|`--n-1`|
|파란 장표지|69,109,166 / #456da6|`--a1`|
|짙은 페이지|45,67,100 / #2d4364|검수 호스트의다크`--page`|
|밝은 장식|215,236,247 / #d7ecf7|`--a4-2-soft`|
|짙은 배경 장식|119,158,211 / #779ed3|`--a1-3-soft`|

## 검수 기록과 제한

페이지별 실제 관찰은 `visual-review.md`, 자동 경계·폰트·chip·대비 결과는 `fixture-audit.json`, 마지막 브라우저가 읽은 소스 해시는 `render-source-audit.json`에 남긴다. 시트 자동0은 관계/데이터 의미의 증명이 아니므로 native 시트도 읽는다. 발견된 결함을 결과에서 지우거나 성공으로 바꾸지 않는다.

사진·복잡한 기술 이미지·고객사 이미지 로고·세계지도 그래픽만 연회색 placeholder다. 읽을 수 있는 원문을 축약하지 않는다. 대표 서명은 원본의 이미지 자산이므로 연회색 단색 placeholder로 바꾸었다. 임의 손글씨로 대체하지 않는다. Lucide로 표현 가능한 아이콘은 얇은 SVG로 구현하며 원본 자산과 세부 획은 다를 수 있다. 이 기록이 남은 시각 차이를 면제하지 않으며 최종 승인 전까지 완료로 판정하지 않는다.

## 통합 원해상도 검수와 실제 반영

초기 자동 검사 0 이후에도 native 시트를 읽어 발견한 관계 의미 결함을 별도로 수정했다. 4-member hub 상단 커넥터의 단절, mindmap 링크의 보이지 않는 곡률, hierarchy/decision-tree의 부모 연결선, timeline dot와 축의 분리, sparkline이 중첩될 때의 0 높이, pricing 제목/가격의 서로 다른 기준선, person portrait의 소실, sankey 분기 높이가 실제 share를 반영하지 못하던 문제, 3/8축 radar가 5각형으로 고정되던 문제, journey 선이 stage 면 뒤에 숨던 문제를 실제 화면에서 확인하고 교정했다.

chart-stack은 각 segment에 tone을 명시하고 own data-el legend를 넣었다. 서비스 계열의 light/dark 대비 부족도 실제 측정값에 맞춰 더 짙은/밝은 팔레트 자리로 옮겼으며 legend key와 segment 색을 같이 바꾸었다. waterfall-6의 누락된 +43 신규 사업을 더해 1,284 합계가 산술적으로 이어진다. line의 같은 값 44→44 및 flat fixture, 누적 면의 아래 계열, balance의 음수 tilt 방향을 원해상도에서 읽었다.

cycle의 기본 fixture에는 순환 화살표를 그린다. 원본의 무화살 고리 검수 호스트만 등록된 숫자 `--axisfold-052-cycle-arrows:0`을 공급한다. 17의 상단 원이 본문 그리드 위로 걸쳐 있는 원본 배치는 등록된 private 숫자 입력 `--axisfold-052-cycle-top-shift:-23px`로 공급하고, 공식 fixture 기본값 0은 원을 슬롯 안에 유지한다.

01 사진 내부의 건물 윤곽을 추적했던 잘못된 흰 구멍을 제거했다. 사진은 회색 단색이고 원본의 바깥 모듈 윤곽만 곡선으로 남긴다. 02/03/17/20의 단순 모서리 장식과 03/16 사진 mask도 추적 노이즈/chamfer를 제거하고 명시적인 직선+quadratic 둥근 모서리로 다시 그렸다.

추가 글리프 측정: 01 Introduction의 분리된 crop은 Pretendard Variable 100/700/+0.5, bbox 573×77, F1 .8242가 가장 가깝다(원본 572×74). 02 Contents는 Pretendard Variable 106/600/0, bbox443×78, F1 .8910(원본438×76); 공식 type104를 사용한다. 03 Who We Are는 Pretendard Variable88/700/−1, bbox499×64, F1 .8899(원본499×65). 20 부제는 Noto Sans KR30/700/−0.5, bbox405×28, F1 .8837로 측정해 채택했다. 08 Autonomy를 600과700으로 재측정했을 때 F1 .8291 대 .7274여서 600을 유지했다. 허용 글꼴 파일 안의 가장 가까운 결과를 택했으며 bbox/AA 차이를 100% 동일이라고 기록하지 않는다.

페이지별 폰트 역할은 따로 맞춘다. 06 표 body14/header16, 08 note16, 12 원 내부 name20/note18, 13 상세 body14/name20, 14 카드 body16, 16 일정 name20/note16 등 실제 원본 역할에 맞췄다. 전역 폰트 크기 매핑으로 모든 본문을 줄이는 방식은 쓰지 않는다.

수정 후의 최신 브라우저 렌더 및 전수 자동 검사 결과가 이전 PNG/검사 결과를 대체한다. 최종 시각 승인 전에는 페이지 동일 판정을 보류한다.

## 마지막 확정 수선과 검증

replica04의 Mission 한줄이 두줄이 되어 다음 설명과 겹치던 결함을22px/regular/nowrap 역할과220px 폭으로 복구했다. replica03 목차 page번호를 원본 오른축으로 옮겼다. replica10의28 값이 파랑 막대 밑으로 나가 흰 배경에서 소실되던 문제는20px line-height와 padding0으로 고쳤고, 11은 gear와 작은 매출비중 label 및 독립 수치 위치를 복구했다. 19 긴 bullet은 원래 카드 안에서 읽히도록14px/고정 원문 줄바꿈으로 맞췄다.

조립10의 작은2행 범례와 표 top287px를 복구했고 선/면 점의 inset을 제거해 여섯 막대 중심과 맞췄다. area의 축·series 이름은 이 콤보의 같은 연도 bar label 및 명시적 legend와 중복되어 원본처럼 겹쳐 표시하지 않는다. 일반 fixture의 축은 모두 표시된다. 좁은 칸의 축 솎기는 README상 허용이지만 현재 네 차트는12px 역할로 모두 표시하는 구현을 유지한다.

12는 흰 panel490px, 점선4개, 모든 원의 면 아래/이름·note 위 레이어를 분리했다. 16은 원본 darknode modal #4670a1, spine #d9eaed를 hostpalette로 공급한다. 18은 점선/파트너 슬롯/27~28px 행간을,20은 원본 연락처27px 행간을 복구했다.

01 Company는 F1만 최적화한400굵기 선택이 원본보다 ink42% 굵어져 재검수에서 거절되었다. 실제 Canvas 글리프의 면적과 bbox도 함께 비교해 Pretendard Variable102px/250/자간4.25px로 낮추고 y를5px 복구했다. 호스트는 공식type96 자리에102px를 공급하며 collectionCSS는 정상var(--type-96)만 소비한다. 이전400굵기 시안은 최종 결과가 아니다.

최종 실제폰트40페이지0결함, 모든 eligible정수칸9978회0finding,56요소의 light/dark native시트 개별 관찰을 기록했다. 이 자동 결과가 원본 시각 동일 판정을 대신하지 않으며 부모 통합 승인 전에는 완료라고 표시하지 않는다.

마지막 원본08의 우측 core→panel 선을 replica에서 x718~769로 복구했다. 가는 선의 실제 픽셀을 대조해 replica의1px SVG만 opacity.5, 조립 hub의 connector만 등록된 `--axisfold-052-connector-alpha` 기본1/source호스트.24로 공급한다. endpoint dot은 그대로다. 최종(724,358)/(735,358)/(740,358)의 조립값은 RGB213/215/216, replica는213/214/216으로 원본213~216 범위와 일치한다. 11 상·하 수치의 최종 glyph y359~386/594~621은 원본과 같다. Company의 최종 bbox는 두 구현 모두(66,108)~(508,201), ink6322로 원본6236보다약1.4% 많으며 bbox와 굵기 교정을 실측으로 확인했다.

최종 native 감사 JSON은56요소 각각의 light/dark PNG SHA256과 실제 관찰 근거를 포함한다. 최종 페이지 PNG80장(원본대조40포함)의 크기 및 PDF20/20/172/172페이지를 freeze-audit.json에 기록했다. source manifest 시각은12:20:43 UTC다.

## 최종 확정 연결점7px 수선

원본11 하단 두 spoke의 endpoint가 elbow 선보다7px 위에 떨어진 실제 결함을 고쳤다. `--axisfold-052-hub-lower-dot-shift`를 hub.element.json에 기본0px로 등록하고, 원본11의slide만7px를 공급한다. 바꾼CSS는 하단두 `.spoke::after`의top뿐이다. source08·본문·수치·선 geometry 등 다른 것은 변경하지 않았다.

PIL에서 이동 전 dot 중심 row554와 선 row561이 분리돼 있었고, 최종 dot 중심은row561이다. x524의 이전 dot위치는 RGB122→배경244/246/248, 접합위치는 배경→122로 변했다. 좌우55px 수평구간은 모두 연속dark pixel이다. `dot-native-audit.json`에 근거를 남겼다.

기본0px의 hub3/4/6 ×라이트/다크6패널을 실제1280×720로 다시 찍어 기존native PNG crop과 픽셀 완전동일임을 확인했다. 전체library PNG/PDF116개 SHA도 변경없다. 공식HTML에는 새default를 반영했다. 따라서native 전체export는 반복하지 않았다. 최신40페이지 렌더·실제폰트40페이지·340fixture/9978정수칸0finding을 재고정했다. 최종browser manifest시각은12:29:39UTC다.

## 표지 두 글자 역할 최종 실측

01의 부제와 연락처만 다시 맞췄다. Company·Introduction·사진mask는 변경하지 않았고, 다른38페이지PNG는 SHA까지 그대로다. 컬렉션 변경은 foundation.css/json 두 파일뿐이며56요소는 변경하지 않았다. 기본값을 보존한 등록private입력으로 원본표지에만 크기·자간·굵기·위치·메타글꼴을 공급한다. 기본foundation4패널은 기존시트crop과 픽셀완전동일하고libraryPNG/PDF116개SHA도 그대로다.

부제는NotoSansKR35/600/−1.2px, 두구현의최종ink bbox(123,357)~(536,388)로 원본과 같다. meta는Montserrat16/label600/normal300(전화400),31px행간이다. Manager폭136, Mail폭210, Web폭181의원본경계와 맞췄고 전화끝·일부AA행은1px차이가남는다. 두구현의메타픽셀은 서로 완전동일하다. 확대원문에서 도메인은miridih.com이며 이전의miridh.com 중간i 누락을 해당메타에서 복구했다. 측정은cover-role-measurement-audit.json,기본시트불변은cover-native-audit.json에 남겼다.

페이지진단8건은 최신PNGink와실제DOM text-node Range·clipping ancestor를 함께 검증했다. Company/Introduction/Contents/장표지의01·WhoWeAre/샘플안내는 글꼴의loose범위가 소유상자높이를넘는경고이며 실제ink잘림없다. 17 우측note는410px상자만페이지밖으로가고 실제각줄Range와ink는안쪽이다. 기하를 바꾸지 않았고 page-audit-disposition.json에 각각의수치를 기록했다.


## 주 에이전트 최종 통합 판정

원본별 개별 비교 회차와 마지막 변경 화면 재열람 후, 최신 비교 PNG·소스·실제 폰트 지문을 최종 승인 기록에 묶었다. 자동 bounds 검사와 시각 검수는 별도 근거다. 사진·복잡 이미지의 요청된 회색 대체, Lucide 치환, 가장 가까운 허용 실폰트와 안티앨리어싱의 미세 차이를 픽셀100% 동일로 표현하지 않는다. 렌더 뒤 일반 호스트 CSS·팔레트 의존성과 컬렉션 복사본 SHA를 다시 확인했다.

마지막 패키지 대조에서 canonical에 없는 미사용 루트 foundation.css 사본 1개를 정리했다. 참조0건을 확인했고 canonical346파일 및 PNG194개 SHA는 불변이다. 정리 후40페이지와 실제폰트를 다시 검사해 최신지문을 갱신했다. 증거는 unused-extra-cleanup-audit.json이다.
