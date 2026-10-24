> 아래 과거 동결 기록은 후속 원문·의미 감사로 무효화되었다. 최종 상태는 마지막 원문 복구/계약 교정 절을 따른다.

# Crossrail v2 검수 기록

## 작업 경계

073 덱 30장, 컬렉션 `crossrail`, 요소 56개를 맡았다. 원본과 복사된 replica는 v2 작업에서 바꾸지 않았다. README 전체를 재독했고 예시는 계약 마크업/fixture 데이터만 참고했다. 이전 요소 CSS는 재사용하지 않았다. map의 sourceMeasurements는 보이는 직접 노드 983개를 모두 소유자에 연결한다.

## 문구와 데이터

새 기본 fixture와 `replica-NN.html`은 물류·장비 회수·정비 업무의 새 한국어 문구를 쓴다. 원본 6자 연속 일치를 금지한 최신 요구를 우선했다. Golden의 구조와 수치는 유지했고 card-2-quiet의 겹치는 끝맺음 한 문장만 “접수 대장은 방문 순번과 묶어 창구마다 열람합니다.”로 바꿨다. card-4의 제공된 ✹은 golden 구조 보존 때문에 그대로 두었다. 새 아이콘은 빈 data-icon이다.

기기 길이 `1500mm` / `1200mm`는 문자 포함 6자 중복 제한 때문에 `1540mm` / `1260mm`로 바꿨다. 그 밖의 원본 차트 수치는 디자인 기하이므로 유지했다. 특히 source22의 일곱 점은 5000,4500,4000,5000,4800,5000,5200이다. 기본 waterfall의 끝 합계는 앞선 증감의 산술과 맞게 1241로, 기본 bullet의 범위를 벗어난 104는 96으로 고쳤다. 원문을 추정하여 대체한 작업이 아니라, 새 문구를 요구한 v2 fixture 정책에 따른 재작성이다.

## 비교·수정 범위

1. 30장 원본 | 불변 replica | 첫 조립본을 한 장씩 열고 도형, 구성, 정보 소유권을 비교했다. 원본과 다른 레이아웃은 GAPS에 남겼다. 표의 강조 면을 표현할 수 없다는 이유로 행 데이터까지 빠진 20/29는 일반 행으로 복구했다. 29의 네 번째 점이 화살표 gap에 묶인 소유권도 고쳐 여섯 점을 실제 측정 좌표로 복구했다.
2. 56개 요소의 light/dark 크기 시트를 모두 열었다. 자동 경계 검사 외에 native crop으로 원·연결선·숫자·장문을 확인했다. 시트는 모든 최소 이상 대표 크기를 포함한다. 큰 전체 시트에서 읽기 어려운 세부는 native 셀과 실제 DOM 범위를 함께 검토했다.
3. 실제 결함을 묶음으로 고친 뒤 마지막 소스로 전체 시트와 조립본을 다시 렌더한다. 최종 수치와 fingerprint 일치 여부는 `source-contract-audit.json`, `sheets/*-checks.json`, `nested-root-checks.json`, `reassembly-checks.json`이 근거다. 아래 시각 수정 목록은 자동 0만으로 승인하지 않은 항목이다.

## 실제 고친 문제

- bullet 행 묶음의 align-items 상속 때문에 자식 폭이 0이 되던 문제를 stretch와 명시적 행 배치로 수정.
- 기본 callout-stack의 bare seat가 넓은 띠로 늘어나던 문제를 foundation의 정사각 배치로 수정.
- 여섯 node cycle의 note가 core 위에 겹치던 문제를 순서가 유지되는 하단 설명 열로 분리.
- concentric 바깥 레이블이 안쪽 원에 가려지던 문제를 실제 annulus 중심 수식으로 수정.
- mindmap 양방향 연결선과 decision-tree 질문→분기 trunk, hierarchy의 끊긴 수평 bus를 실제 도형 연결로 수정.
- flowchart의 to-d+to-r가 한 pseudo를 덮어쓰던 문제를 수평/수직 pseudo로 나눠 동시 표시. grid track은 실제 배치된 좌표에서 생기도록 변경.
- swimlane 면과 이름이 음수 z-index로 페이지 뒤에 숨던 문제, 노드 margin 때문에 수직 화살표가 짧던 문제를 수정.
- bubble의 width/height 최대 제한이 달라 원이 타원이 되던 문제를 하나의 지름 수식으로 수정.
- donut 행의 긴 이름은 고리 아래에 두어 수치와 이름이 겹치지 않게 수정. 하나짜리 donut은 내부 레이블 유지.
- logo-group의 여섯/여덟 seat가 영역 밖으로 넘던 문제를 실제 멤버 수에서 계산한 정사각 지름으로 수정.
- matrix의 y축 writing-mode가 flex 축을 바꾸던 문제를 축 container가 아닌 개별 span에 적용.
- waffle 31–60개 멤버 분기가 누락된 것을 10–100 전 범위의 자기 자식 개수 계산으로 수정.
- source19는 비교 본문을 금지된 side.note로 끼워 넣지 않고 독립 prose로 분리하고, 두 상단 표제는 headline.on으로 조립. V S 표식은 계약의 중앙 비교 표식이며 원본의 헤더 화살표와 다르다.
- 새 fixture의 중첩 list/tag에는 각 요소 data-el과 계약 item/name 구조를 명시했다.
- 비교 원본의 문구보다 훨씬 긴 제목·식별자 때문에 밀도가 깨지던 표/카드 문구를 실제 업무 값과 비슷한 길이로 다시 작성했다.

## 해석·결정과 남은 차이

모든 표현 불가 항목은 `GAPS.md`와 map의 unexpressible에 명시한다. 다중 분할 pie를 여러 one-share donut으로 겹치거나, reverse steps를 정상 steps의 글자 순서만 바꾸어 흉내 내지 않았다. 12×6 정수 칸 때문에 원본의 42px badge나 65px 본문 상자를 완전히 같은 좌표로 배치할 수 없는 경우도 있다. 이를 요소 CSS의 페이지별 수치 변수로 숨기지 않았다.

source03의 사진과 source04의 세로 사진은 gray back seat다. source09/13/17/21은 foundation의 강조 페이지다. source15 사진 중앙 rule은 foundation furniture다. source25는 at-left cover의 넓은 하단 hatch다. source05의 제목 옆에서 시작하는 높은 세 패널과 source30의 폭이 다른 좌측 연락 lockup은 공급된 foundation 기하로 정확히 표현할 수 없어 별도 foundation gap이다.

작은 원문의 글꼴은 Noto Sans KR가 가장 가까운 허용 family로 판단했다. 복잡한 원본 아이콘은 Lucide로 대체했다. 외부 source palette의 secondary copy는 원본보다 조금 진하게 공급해 읽힘을 확보했다. 라이브러리의 모든 숫자/문자 대비는 공식 두 모드로 별도 검사한다.

최종 검수 완료 표시는 실제 마지막 렌더와 보고서가 일치한 뒤 추가한다. 이 파일의 존재만으로 완성·무결성·출고 승인을 뜻하지 않는다.

## 21장 정수 그리드 충돌

원본 두 metric 카드 폭은 각각 402px이다. body pitch=(1090+12)/12=91.833px에서 (402+12)/pitch=4.508이므로 span5, 시작 x367→col4 / x782→col8로 반올림되며 8열이 겹친다. 한쪽 span을 임의로 4로 바꾸는 보정은 철회했다. 카드 fixture와 측정은 그대로 보존하며, 동시에 놓는 페이지 배치는 foundation unexpressible로 기록하고 네 카드를 조립본에서 생략했다. 이는 카드 CSS 결함을 숨긴 것이 아니라 정해진 정수 그리드에서 독립 레이아웃을 표현할 수 없는 계약 gap이다.

## 마지막 native 확인에서 추가한 검증

person의 선택적 list가 flex 중앙 정렬에서 intrinsic 폭/높이 0이 되는 실제 오류를 native 셀에서 찾았다. list 전용 폭/높이를 예약하고 부모의 name/note 선택자를 직접 자식으로 좁혔다. 두 항목과 긴 소개를 가진 fixture는 작은 크기에서도 숨김 없이 읽히는 min 6×3에서 읽힘을 검증했다. 투명 `.card.line`은 페이지의 전경을 상속하도록 고쳐 어두운 면에서 제목이 사라지는 오류를 제거했다. steps.col은 이름과 note의 독립 열을 확보했다.

source07/18의 55.5px 높이 슬롯은 큰 글자로 세 줄이 넘치는 실제 문제가 있었다. 페이지 좌표를 늘리지 않고 자신의 작은 높이에 반응하는 prose/list 14px 본문 단계와 body 행간으로 교정했다. 이 크기에서 실제 읽힘을 확인한 새 source fixture의 min은 3×1이다. source27의 네 문장은 원문 길이보다 과도하게 길었던 것을 비슷한 업무 문장 길이로 다시 썼다. 사진 뒤 흰 panel의 kicker가 강조 페이지 색을 잘못 상속하던 것은 foundation 자신의 photo-panel 조건에서 n7 역할로 복원했다.

source11의 중앙 세로 구분선은 위/아래 카드에 중복 소유되던 측정 자료를 분리해 foundation gap으로 기록했다. 직접 측정한 source 노드 983개가 각기 한 소유자를 갖는다. 후속 taxonomy 교정을 포함한 현재 map은381 instances, 명시적인 unexpressible29개다.

## 최종 기술 동결 (2026-10-24T12:52:49.408010+00:00)

56개 CSS와 244개 fixture(기본 112 + golden 28 + 새 source형 104)를 현재 소스로 렌더했다. renderer `v2-grid-paint-font-parts-1`의 3,234 native 셀에서 영역 초과/잘림/텍스트 겹침/component·parts 초과/실제 대비/폰트 실패가 모두 0이다. 정적 계약 감사는 errors 0, warnings 0, 원본 6자 일치 0이며, 모든 sheet fingerprint가 현재 소스와 같다. 오래된 min 렌더의 쓰이지 않는 crop 188개도 지워 최종 native PNG와 보고서가 일치한다.

조립 30장은 모두 1280×720이고 원본 | 불변 replica | 조립 비교 30장은 3840×720이다. `reassembly-painted-checks.json`은 원래 DOM 후보를 별도 원본 보고서에 보존하고 현재 source/HTML SHA를 확인한 뒤 실제 PNG 바탕색으로 대비를 판정한다. 최종 잘림/영역/겹침/부분영역/실제 대비/폰트/요청 실패는 모두 0이다. 이는 29개 명시적 계약 gap까지 복원했다는 뜻이 아니다. 특히 21장의 네 카드 배치와 23/24/27의 unsupported 도해는 생략된 상태다.

모든 112개 light/dark 크기 시트를 직접 열었다. 큰 전체 시트의 미세한 글자는 native crop과 DOM 검사로 보완했으며, 3,234개 native crop 각각을 사람이 한 장씩 모두 읽었다고 주장하지 않는다. 부모 스타일만으로 놓치는 자식 b/span의 실제 타입 차이 22개를 `fragment-measurements.json`에 따로 측정했고, source21 rank의 자식 숫자 40px 위계를 반영했다.

## 후속 taxonomy 계약 교정

추가 감사에서 source18 단일 항목5개의 list 최소2항목 규칙 위반을 확인했다. 행을 지어내지 않고 같은 문장·지도 슬롯을 prose로 옮겼다. 원래 한 글자 bullet은 DOM Range로 측정해 marked-prose gap으로 기록했다. matrix-nine의 첫 기본 fixture에 누락된 axis-x/axis-y와 각3개 라벨도 넣었다. 관련 시트와 조립본을 다시 렌더한다.

추가 readonly 감사에서 matrix.cell에 계약에 없는 tone-2/tone-3 선택자 두 개도 발견했다. 어느 fixture에도 쓰이지 않는 규칙이라 제거했으며, 실제 페인트를 바꾸지 않고 공개 CSS 계약을 좁혔다.

후속 교정 최종 재동결: 현재 taxonomy definite errors0, 기존 정적 errors0/warnings0/6자중복0이다. 관련 시트를 다시 렌더한3234 native 셀과 현재 source/HTML SHA를 검증한30장 조립본의 기술 실패는 모두0이다. source fixture104개와 전체244개 수는 그대로이며, 옛 list 이름의 사용하지 않는 native crop100개도 지웠다. 현재 map381/gap29와 단일 direct-node 소유983개가 최종 값이다.


## 원문 복구와 의미 감사 정정

새 업무 문장 제약을 reassembled에도 적용한 것은 범위 해석 오류였다. 이 제약은 fixture에만 적용하며 조립본은 불변 replica의 원문과 공개 수치를 옮기는 것이 맞다. 30장 조립본의 원문을 다시 복구했고 `original-assembly-identities.json`으로 문구와 독립적인 source identity를 고정했다. 원래 배치된 모든 root의 grid style은 그대로다. 18장에는 별도 제목 ‘강력한 파트너십’의 실제 측정 bbox가 furniture로 잘못 분류된 것을 바로잡아 처음 정수화한 headline을 추가했다. 오른쪽 마지막 제목의 중복 identity도 바로잡았다. 지원 body 원문 노드368개와 header 원문을 공백/계약상 CSS bullet만 정규화해 대조하며, 원문에서 실제 빠진 영역은 GAPS.md에 따로 남긴다.

26장 roadmap의 칠해진 막대 두 개를 underlay gap으로 잘못 분류했던 것을 수정했다. 4개 lane의 총5개 bar는 원본 start/end를 quarter축227px 기준으로 계산한 공개 from/to 데이터이며 수치와 이름을 모두 보존한다. 남은 두 pale time-rail만 gap이다. 22장 line의 weekday/숫자 데이터와 24장 범례의 지역별 비율도 원본대로 복구했다.

source07 반원 peer track은 중앙에서 방사로 연결하는 hub 계약과 다르다. 해당 source fixture/조립 root는 제거하고 arc-track 필요 마크업을 gap에 명시했다. 필수 inferred hub 자체는 얇은 선과 원형 core를 가진 실제 radial hub로 새로 설계했다. metric의 수치는 bare 계약이므로 숫자 주위 capsule border를 제거했으며 원본22의 별도 outline은 gap이다.

versus의 사이 mark는 문자 VS가 필수가 아니므로 빈 b.vs와 CSS 도형 화살표로 표현했다. 조립 root 밖 원본 header-arrow 자리에 임의로 내보내지 않았다. 원본 header-band 위치의 비교 화살표는 comparison-panel foundation 구성 gap으로 정직하게 남기며, root 안의 관계 mark만 표시한다.

pricing은 추천 배지 유무와 관계없이 같은 이름/금액 행을 모든 plan에 예약한다. venn은 실제 원 지름에 비례하는 중심 간격을 사용해12×3에서도 항상 교집합을 유지한다. slope의 a/b는 실제 데이터 endpoint 위치에 두고, 가까운 값은 ordinal 두 label열과 얇은 leader로 연결해 원데이터를 옮기지 않았다. dumbbell 배치는 그대로다. radar는 각 K축마다 원중심에서 동일 각도로 방사선을 그린다. 이7개 요소의 라이트/다크 크기 시트를 직접 다시 열고 각 칸의 자동 검사를 확인했다.

현재 map의 모든381 instance에는 원본 bbox, 실제 형태·타입·연결 관계를 설명하는 design 문장을 넣었고 deck 전체 팔레트 자리 roles도 기록했다. 원본/불변 replica는 수정하지 않았다. 이전 기술 검사0만으로 위 의미 오류를 통과시킨 판단은 철회한다.


### 원문 길이를 가진 실제 재검증

원문 복구 뒤03 prose와05 quiet card3개에서 실제 슬롯 밖 글자4건을 발견했다. 페이지 grid/원문/BR은 유지했다. prose의 작은 높이에서 본문 행간을 공유 body-line으로 적용하고, quiet card는251–450px 높이에서 spacer/padding/gap을 줄여 본문 영역을 확보했다. 03 fixture는 원본과 비슷한9/8행,05 fixture는2행 제목+7행 note/108–111자의 새로운 업무 문장으로 다시 썼으며6자 원문 일치 금지는 유지했다.05 fixture min은 실제263×393px 조립 슬롯과 거의 같은3×4(263×390px)도 직접 검사하도록 정정했다.

후속 paint 검수에서는19 오른쪽 prose가 DOM에만 있고 positioned versus.side.on의 면 뒤에 가려지는 실제 오류를 찾았다. prose root 자체의 position:relative로 일반 DOM 페인트 순서를 보장했다. 페이지별 형제 조건, z-index 숫자 보정, grid 이동은 쓰지 않았다. 실제 원문 pixels를 확인한 뒤에만 완료 판정을 한다.

외부 source-palette의 a3-7은 두 번째 톤과 잘못 같았던#65719a에서 실제 세 번째 중간톤#959db6으로 바로잡았다. 공식 라이트/다크 라이브러리 팔레트에는 영향이 없다. 임시 사진 placeholder의 숫자3/4도 원본에 없으므로 조립본 foundation data-ph를 빈값으로 비웠다.


03 긴 원문형 새 fixture의 min은5×2(447×189px)까지 검증해 실제 조립본450×190px과 같은 작은 높이에서 테스트한다.05는3×4(263×390px)에서7행 note가 읽힘을 확인했다. 따라서 과거의 과도하게 여유로운5×3/4×6min 기록은 최종값이 아니다. 마지막 원본색 a3-7의 흰 글자는 원본과 같은2.7:1 대비이며 재현본 한건의 알려진 차이가 아니라 원본 자체의 조합이다. 공식 light/dark 시트는 이 외부 source색을 사용하지 않는다.


## 원문·의미 교정 후 최종 동결

최종 source fingerprint `13a53c83e4a0bbb57b07b188d2ff19c56109f14312ecda982352f50e51296c59`.56개 요소/244개fixture(원본형104개), map381/design381/roles/직접노드983개 단독소유, GAP31개다. renderer `0922c056afae5c426afbc69106eb3d7e3fdea1c41d8d6b65128441a61de07e76`의 독립 context+250ms 최종30장 렌더가 같은 fingerprint를 기록한다. 최신3,254개 native 셀은 영역/잘림/겹침/component·parts/실제대비/폰트 실패0이고, 원문368/368/header누락0이다. 조립30장의 geometry/font/request 실패0이며 source26원본색의2.7:1 대비 한건은 그대로 남겨 기록했다. 이는31개GAP이 복원됐다는 주장이 아니다. 최종 원문 삼중비교30장을 다시 직접 확인했고,03/05/18/19/26은 실제 native 영역을 추가 대조했다. 이전의 사업문구 조립본/기술0만으로 의미까지 통과시킨 기록은 최종 승인이 아니다.


## 주 에이전트 최종 대조 후 선·마감 페이지 교정

11/12의 card.line 외곽box는 원본에 없었다. open line-card의 외곽 border를 제거하고 note는 secondary n7 역할로 복구했다. 원본17 navy 위 투명 line-card의 흰 note는 외부 source-palette의 기존 `.slide.on .card.line` 문맥에서 n7=#fff로 공급한다. 다른 흰 카드에 흰 note가 전염되지 않도록 `.slide.on` 전체의n7를 바꾸지 않았다. 공식 palette/새 alias/페이지번호 조건은 없다.17의 별도 전체 outline4개(첫 면의slate fill포함)는 단일 line 디자인에 숨겨 넣지 않고 각각의 boundary gap으로 소유를 분리했다. name/note 원문은 유지한다.

14 상단3개는10의연속단색 steps와 달리 실제로분리간격과서로다른tone을가진 두번째디자인이다. same-as10분류를 철회하고 기존reverse아래행과 별도로 second-design gap에 명시했다. 원본에없는연속단색수평레일을조립본에남기지 않았다.

30 마감은 초기foundation선택오류였다. 계약에있는 `.head.at-bottom-left` + `.rail.on`이 원본의 navyleft면/상단kicker/큰하단title를 담당할수있어GAP판정을철회했다. 해당variant자식기하만 실제원본수치로교정하고 그foundation실측 body[646,64,539,592]에서 contact원본bbox[686,442,484,180]를최초nearestgrid col2/span11,row5/span2로산정했다. 이전 잘못된fullbody격자내table을CSS회피목적으로움직인것이아니다. 최종kicker y99/title y539.17·76px/navy면581.12px, 새tablebox[691.92,466.67,493.08,189.33]이다. 근거 `source30-foundation-correction.json`. 기존29장의root grid문자열은변경하지 않았다(14unsupported root제거예외). 새 closing foundation fixture는 업무용새문장으로 같은6자금지 검사를 받는다.


## 마지막 mapped 원형 대조

08funnel의 STEP/숫자 두 필드는 맞닿은 반쪽 border를 사용해 하나의 outline capsule 안에 놓으며 마지막 단계는 solid capsule이다. 긴 이름이 두줄로 꺾여 pill이늘어지지않게 두필드를한줄로유지한다.19 headline.on은 강조면만담당하며, 원본HTML의 malformed `text-align:centerletter-spacing`가실제start로해석된것을확인해 .center추출오류를제거했다. 기존정수grid는그대로다.

15tag는이미허용된자식span을42×42px최소filledcircle로설계해한글자는원,긴이름은자연폭 capsule이된다. root는투명한수용칸이며size container를유지한다.24legend의key marker는원래의사각형으로,08list.divided는bullet없이굵은name/얇은행선으로,06pyramid는공유gap단계의9px분리간격으로복구했다. 일반list의원형bullet은유지한다.

원문검사범위를모든foundation문구까지넓혀확인한22의‘일별 생산량 추세’는 별도직각charttitlepanel이었다. source16을막연한furniture로분류했던오류를바로잡아chart-panel계약GAP으로정정했다. 사용자예시처럼기존line-chart는titlepanel을갖지않으며source15원형tag를두번째직각디자인으로몰래재사용하지않았다.

지원본문원문수가368→359인것은잘못그린14상단3단계의9text를명시second-designGAP으로옮겼기때문이다.359개지원원문과모든지원header는그대로보존되며공개차트수치는바꾸지않았다. source30감사문구는foundation복원으로다시표시된다. 현재map385/GAP36/elementfixture243(원본형103)/foundationfixture3이다. 이전381/31/244와여러기술동결수치는이최종분류이전의이력이다.

closing 공식팔레트 kicker는inverse page역할로AA대비를회복했다. 외부source provider는같은kicker문맥의page역할에원본gray를공급한다. 원본과같은30kicker4.46:1과26bar2.7:1은source조건으로남기며,공식library/foundation의AA실패와구별한다.


## 최종 증거 갱신 완료

최종 FP `31f53dd4961898cff6f1866afca8faebea8ee7306e7a09517116f8da7db027ab`.56요소/243개fixture(원본형103),foundationfixture3개/light·dark6render,map385/design385/GAP36/원본직접노드983개중복소유0이다. 최종전체시트 3244개 native 셀은영역·잘림·겹침/component·parts/실제대비/폰트실패0,56FP모두현재다. 마지막pricing nested baretag의on색상속회귀도color:inherit한속성으로해결해16셀양모드0을확인했다.

30조립본과foundation6render의FP도현재와일치한다. 모든조립geometry/font/request실패0,공식foundation대비0,지원원문본문359/359와지원foundation문구89개누락0이다. source26/30의원본색대비2.7/4.46두건은보존한원본조건이다. source14의9문구와22charttitlecaption은명시GAP이며다른사업문구로대체하지않았다. 최신30삼중PNG전부를직접다시검수했고최종변경6leaf의양모드시트/42pxtag/작은funnelcapsule/3×4longnote/5×2prose/마감title를native크기에서추가확인했다. `final-original-semantic-review.json`이이전동결스냅샷수치보다우선한다.


## 계산 가능한 숫자축 GAP 철회와 마지막 동결

20막대의max30→0/10/20/30,22선의max6000→0/2000/4000/6000은공개max에서계산가능하므로‘axismarkup없음’을GAP사유로삼은판단을철회했다. 해당8source측정은원래chart소유로합치고두GAP을제거했다. root의before/after counter rail만사용하며,한rail은정수3등분일때표시하고다른rail은소수3등분을round/mod와builtin decimal-leading-zero로표시한다. golden max2.6은2.60/1.73/0.87/0.00으로실제nativepaint검증했고상한을3으로잘못반올림하지않는다. 허용밖@counter-style은쓰지않았다. 천단위comma는생성틱에삽입하지않는표기차이가있다. h막대는수직tickrail을표시하지않는다.

line-height의100cqh/3은4숫자를plot의3간격에놓는기하stride로본문leading과다르다. 공유font-size/weight/tracking은그대로이며raw정적경고2를별도해석과함께보존했다. 해당해석을숨기거나억지상쇄token식으로경고만없애지않았다. source20/22와소수golden의실제counterSet/opacity/좌표증거는numeric-axis-proof.json에있다.

이최종 FP `f6da2672991d7df1de56e1d8c263544bfbb215079fc11ec673f934d538d3f373`에서56요소/243fixture(원본형103),map383/design383/GAP34,직접source노드983단독소유다.3244native기하·대비·폰트0,56시트와30조립/foundation6이모두현재FP이며지원원문367/367·지원foundation문구누락0이다. 공식foundationAA0. source26/30원본대비2.7/4.46은기록된원본조건이다. 이전385/GAP36/본문359는숫자축복원전이력이다.
