# Dockside 재작성 검수 기록

## 고정한 자료와 범위

- 기존 `deliverables/dockside/review/replica`의 HTML/CSS/PNG는 변경하지 않았다. 30페이지의 DOM 배치, 글자 Range, 도형/테두리/가상요소의 실제 Chromium 수치를 `build/source-measurements.json`에 수집했다.
- 새 CSS는 이전 element.css를 복사하거나 덧씌우지 않고 작성했다. 이전 소스의 페이지 클래스 및 페이지별 선택자는 새 컬렉션에 넣지 않았다. 원본의 장면 전체를 범용 카드의 변형으로 바꾸지 않았다.
- 지도는 페이지 전체 면, 머리글, 레일, 표지 장치, 가시적인 요소와 계약으로 표현할 수 없는 부분을 포함한다. 복합 요소 안의 그림/문구/연결선은 부모 요소의 `source_metrics.nodes`에 포함되어 있다.
- CSS의 색은 팔레트 자리만 사용한다. 참조 팔레트 시트가 주황 계열인 것은 호스트 기본 팔레트다. 원본 대조와 재조립의 호스트는 `source-palette.json`으로 파랑/연한 회색 원본의 자리를 매핑한다.

## 원본에서 가져온 요소

| 요소 | 기준 replica | 적용한 실측/의미 |
|---|---|---|
| agenda | 03 | 345×334 패널 3개, 35px 사이 간격, 두 줄 제목, 단일 괘선, 우하단 원형 화살표 |
| card | 06 | 최대365×520, 사진314×310, 2px 밝은 림, 24px 바깥 반경, 강조 제목과 짧은 설명 행간 |
| pill | 30 | 301×67 연락 캡슐, 검정36px 아이콘 원. 02 line/quiet,05·16 on은 명명된 변형 |
| tag | 05 | 102×34 검정 범례 캡슐. inline hl은 같은 강조 문법으로 추가 |
| list | 09 | 110px 아이콘 판과 inset 설명 판 3행. 07 num,04·11 check,26 check quiet 변형 |
| callout | 23 | 388×72 결론 캡슐, 검정 종 아이콘과 두 줄 텍스트 |
| headline | 11 | 604×78 강조 띠, 왼쪽 제목과 오른쪽37px 원형 조작 |
| prose | 08 | 16px/400, -0.5px 자간, 1.55 행간의 보조 설명 |
| chart-donut | 20 | 339px 외경, 30px 밝은 바깥 림, 249px 안쪽 면, 실제 색 호15px. 두 원 사이35px |
| steps | 22 | 263px 원, 두꺼운22px 면과 내부2px 림, 작은 제목 캡슐, 원 바깥 설명과 검정 이중 쉐브론 |
| timeline | 23 | 1094×458 전체판과189×215 상승 카드5개, 66px 상단 아이콘, 14px Step행, 8px 하단 괘선 |
| hub | 24 | 180px 중심,145px 위성5개,358px 점선 고리. 원 밖으로 잘리는17은 같은 변형으로 합치지 않음 |
| person | 19 | 295×401 인물판,212px 원형사진,212×54 이름 캡슐, 작은3개 체크행, 중앙 강조 |
| hierarchy | 27 | 226px 인물 노드와138px 사진, 상위1·하위3 노드. 전체 트리가 연결선을 소유 |
| mindmap | 28 | 1050×455 면,186×96 중심,243×112 인물 가지4개. 좌우 둥근 연결선은 노드 뒤에 그림 |
| versus | 26 | 317×475 패널2개, 가운데43px 이중쉐브론, 작은 제목/그림/조용한 체크리스트 |
| image-frame | 06 | 카드 안쪽314×310 사진 자리만 추출. 캡션/확대선/장면 배치는 포함하지 않음 |

## 대조 후 수정한 사항

- 12×6에서 요소가 슬롯 전체로 늘어나던 card, headline, callout, image-frame, timeline, donut 그룹에 원래 최대 크기/비율을 반영했다.
- 도넛의45px 두꺼운 색 호를 원본의 밝은30px 림+15px 색 호로 수정했다. 중앙 Lucide 아이콘과 두 번째 지표의 tone-2를 복원했다.
- card 제목을 원본의 강조 글자 자리로 수정했고, 본문은 긴 행간 대신 원본의 짧은1.2 행간을 사용했다.
- steps의 원 내부 림과 가로 간격, 큰 칸의18px 설명, 작은 칸의16/12px 설명을 구분했다. 12×3에서 마지막 설명 줄이 슬롯을 넘던 부분은 작은 높이 단계에서 설명의 시작 위치와 크기를 줄여 해결했다.
- timeline Step행과 아이콘 사이 간격,18px 제목,14px 설명, 하단8px 괘선과20px 아래 여백을 실측에 맞췄다.
- 긴 인물 이름/보조 note가 겹치던 상세 fixture는 note가 있는 노드의 이름 크기와 내부 여백을 조정했다. 원본의 빈 note 인물판은 그대로다.
- mindmap 곡선이 사진 위에 그려지거나 면 뒤에 숨는 문제를 노드/가상요소의 적층 순서로 해결했다.
- list base/divided의 최소 크기는 설명이 읽히는6×4로 두었다. 작은 높이에서 제목만 남는 표현을 source base의 최소 크기로 승인하지 않았다.

## 판단과 한계

- source15는 축/분류 의미가 없는 중앙 이미지와 바깥 기능 설명이다. matrix 또는 SWOT으로 의미를 바꾸지 않고 GAP으로 분류했다.
- pill.on은05의300×60과16의1090×60에서 채움/높이/끝모양이 같고 문장 폭만 다르다. 할당 폭100%의 반응형 캡슐로 유지했다. 원형 마커/사진이 긴 띠로 변하는 경우와 구분하며 별도 페이지 변형을 만들지 않았다.02의 quiet 요약은755px의 원래 최대 폭을 유지한다.
- source07의 `Problem` 접두어는 list.num 계약에 필드가 없다. 번호는 counter로 그리며 접두어를 CSS에 고정하지 않는다. 정확한 prefix+번호 캡슐은 별도 GAP이다.
- source19의 마지막 인물판에 겹친 추가 버튼은 person 계약의 조작 필드가 없어 GAP이다. 마지막 자식의 위치 조건으로 버튼을 만들어 넣지 않았다.
- source17의 페이지 밖으로 잘린 허브는 source24의 온전한 자원 허브와 의미/경계가 다르다. 임의의 tone/quiet 페이지 전환으로 합치지 않았다.
- 나머지 미표현 항목은 `GAPS.md`에만 명시하며, 현재 계약에 포함하지 않은 제안 마크업을 각각 적었다. 재조립의 비어 있는 부분을 일반 카드나 회색 이미지로 속여 채우지 않았다.
- 12×6 정수 그리드로는 원본의 모든 절대좌표를 동시에 표현할 수 없다. 예를 들어 source06 첫 카드의 y145는 가까운 row2의 y164/496px 높이가 되고, 둘째는 row1 중앙 y100으로 배치된다. source19와28의 큰 장면은 가까운 슬롯 때문에 약35~38px 상향 차이가 남는다. source30 연락 캡슐은 전체면 grid column2/span10,row4/span2로 배치해 원본보다 약18.5px 아래에 온다. 페이지 CSS로 이 차이를 보정하지 않았다.
- 모범 card-2-quiet fixture의 문장1개는 여섯 글자 중복 금지라는 최신 사용자 요청이 이전 동일 문구 지시보다 우선하므로 `기록과 지표가 한곳에 모여 바로 결정을 내립니다.`로 변경했다. 마크업, 숫자 데이터, 강조 구조는 유지했다.
- 새 fixture 문구는 냉장 운송/배차 운영의 실제 같은 한국어로 새로 썼다. 판독 불가 원문을 이번 재작성 단계에서 새로 지어낸 곳은 없다. 기존 replica의 해석/placeholder는 그대로 둔다.

## 자동 검사 및 최종 산출물 확인

- source17의 최신 크기별 라이트/다크 시트는 합계790case다. 잘림, 영역 밖 글자, 텍스트 겹침, 폰트 실패, 숨김 필수부, zero root와 raw 대비 오류가0이었다.
- `source-elements-audit.json`에는 요소별 CSS SHA256과 light/dark probe에 최신 CSS 전체가 그대로 들어 있는지 기록한다. 전체 컬렉션 SHA는 다른 담당의 별도 요소 작성 중 바뀔 수 있어 각 source CSS의 정확한 포함 여부를 함께 확인했다.
- 새 source fixture72개는 공백/문장부호 정규화와 NFKC/lowercase 후 원본6개 덱 전체의6자 window와 비교해 충돌0이었다.
- 재조립 페이지는 모두 실제 Chromium에서1280×720으로 렌더한다. 최종 PNG, 원본|고정replica|재조립3840×720 비교와 audit을 함께 제출한다.
- 원본에 없는 요소의 검수 기록과 전체56개 최종 시트/zip 무결성 결과는 통합 검수에서 이어 기록한다.

- 모범 donuts-4는4×3에서 긴 지점명이 원 밖으로 나가는 문제를 확인해 최소를6×3으로 올렸다. 단일 도넛의 제목 폭도 전체슬롯이 아닌 실제 원 지름의82.3%로 제한해 원 안에서 줄바꿈한다.

## Cover metadata decision
The latest request and README cover contract take precedence: slide30 contact pills are cover metadata in `.meta`, outside a body, matching the cover no-head/no-body structure. This replaces an earlier conservative body-grid interpretation. No page CSS was added.

## 새 조립본 개별 검수와 최종 수정

30개의 원본 | 불변 replica | 새 조립본 비교 PNG를 한 장씩 확인했다. 04 목록의 selector가 여러 item을 가리키는데 첫 item의 자식을 찾던 생성 오류를 수정했다. 10 Idea 칩의 icon을 계약의 `.mark`로 이동했다. 11에 남아 있던 이전 `.divided` 클래스를 제거했고, 16은 map의 `.on`을 실제 root에 적용했다. 16 이미지 mark는 사진/3D 허용 placeholder이며 44px 밝은 원 안에 32px seat로 유지했다. 07 `.num`은 원본의 작은 사각 면과 강조색 번호 캡슐로 수정했다. 원문의 Problem 접두사는 계약 counter에 없는 필드이므로 CSS에 고정하지 않았고 GAP 제안을 유지했다.

04 외곽 Context Brief panel, 05 bubble/growth panel 등 37개 GAP 영역은 계약을 임의 확장하지 않아 조립본에 빈 영역이 남는다. 07 접두사, 11과 04 checklist 면의 모서리 차이, 17 잘린 hub, 18 가로 media row 등 차이를 없애기 위해 새 페이지 CSS나 tone 번호 분기를 추가하지 않았다. 원본100% 동일 완성으로 주장하지 않는다. 정수12×6 배치가 만드는 위치 차이와 GAP의 의미를 비교 이미지와 map에서 직접 확인할 수 있다.

## 원본에 없는 요소 39개

신규19개와 별도 담당20개를 독립 작성했다. 본 담당19개는 architecture, balance, concentric, cycle, decision-tree, delta, flowchart, funnel, journey, logo-group, matrix, matrix-nine, metric, network, positioning, pricing, pyramid, quote, swimlane이다. element.css는 이전 컬렉션 CSS를 읽거나 overlay하지 않고 새 비율로 작성했다. source17 측정의 흰 rim·20px corner·짧은 capsule·부드러운 면과 수치 위계를 확장했다.

크기 시트에서 matrix/matrix-nine 축 라벨이 가운데 모이던 문제를 각 행 소유 grid로 수정했다. journey 선분은 padding을 뺀 content box 단위 때문에 끊기던 부분을 보정해 실제 다음 점까지 연결했다. decision-tree는 불필요하게 커지던 결과 면을 높이 제한한 inset으로 고치고, 2/3 갈래 및 질문3단계 fixture를 넣었다. flowchart/swimlane는 노드 높이를104px로 제한하고 같은48px 연결 간격을 유지한다. concentric4는 짧은 높이에서12/18px type-step을 사용해 annulus별 문구 겹침을 해소했다. 더 작은 크기에서도 모든 문구가 읽히는 구조는 min을 낮추어 다시 렌더했다.

모든 신규 fixture 문구는 냉장 운송·창고·배차 업무의 새 한국어로 작성했고, 최종161 fixture 검사에서 원본6개 덱과 정규화6자 연속 중복0을 확인했다. 모범 card-2-quiet 문장의 단1건 예외는 상단 기록처럼 최신6자 금지 우선의 명시 결정이다.

## 동결 결과

source17 790조건 및 본 담당 신규19 298조건, 합계1,088조건에서 outsideText/textOverlaps/clipped/fontFailures/hiddenEssential/zeroRoots/rawContrast 전부0이다. 각 light/dark probe HTML에 최종 해당 element.css의 동일바이트가 포함되어 있음도 확인했다. 별도 담당20의 검수는 audit-absent-011.json을 참조한다. 전체56/161 fixture 계약 errors0·warnings0,6자중복0,Chromium selector1,379개 invalid0 및58CSS 중괄호 균형0이다. 최종 원본 대응17개 비교 시트도 base/명명 변형별로 다시 직접 확인했다. 최신 foundation의03 plain topbar와16 photo-mark 수정까지 반영한30 PNG(1280×720),30개의 삼중비교PNG(3840×720),reassembled.pdf를 생성했다. 최종 전체56 glyph 대비검사는 부모 통합 snapshot의 별도 결과를 따른다.

주 에이전트 실제glyph통합검수에서donuts-3의두줄긴caption이작은원안쪽너비를넘어ring위로걸치며dark대비2.71인것을확인했다. 240px이하member에서는아이콘없는caption너비를지름의62%로줄여안쪽현에들어가도록수정했다. source20의339px원·아이콘caption좌표는보존하며이leaf전칸/원본대조/30조립의최종렌더를갱신한다.

## 마지막 카드·도넛 보정 후 통합 재검수

부모가 수정한 모범 card의 ✹ 중앙 정렬과 작은 도넛 caption 폭0.62×지름을 보존했다. CSS source generator는 실행하지 않았다. 최종 컬렉션을 새 조립본 library.css에 반영하고30페이지1280×720·삼중비교3840×720를 모두 새 브라우저 렌더로 갱신했다. 카드와도넛 원본 대응 시트도 재생성했다. card light/dark48조건,chart-donut80조건을 전칸 직접 확인하고,card-4최소12×4의✹와donuts-4최소6×3의긴caption을native PNG로 다시 확인했다. 조립본06/20의원본·replica·조립본 비교도 확인했다.

전체56개를 `size_review.py dockside --contrast --resume`로 최종 검증했다.1620조건의 outside/overlap/clip/font/hidden/zero/pixelFailure가 모두0이며, 모든 case에 실제glyph 대비 결과가 있다. 최신 CSS 브라우저 동등성 검증 또는 동일 source hash의 직접 렌더를 사용했다. size-summary-all.json·reassembled-audit.json·이번 card/donut replica-comparison-audit.json은 같은최종 sourceSHA256 `8a96bfe69aa1ec0d5178f2f1029249d166837e189965c1ae575b1180816d333d`에 묶인다. 최종161fixture 계약 오류·경고0,6자문구충돌0을 다시 확인했다. 최신30PNG에서reassembled.pdf도갱신했다. 이전min이 바뀐 뒤 남은옛probe32개는 obsolete-probe-cleanup.json에목록을기록하고제거해 현재12×6·선언min진단PNG만 남겼다.

## Fixture 의미·단위 최종 정리

사람 profile의 name을 실제 한국어 인명으로 바로잡았다. four-contacts는 정하린·윤서진·한도윤·이서율이고, 각 기존 접수/집계/운임/회신 역할은 note에 유지했다. replica-19도 정하린·윤서진·한도윤을 name으로 쓰고 입고창구/운임조정/냉장회차 담당 역할을 note로 옮겼다. 긴 이름 검수용 profile-detail은 `정하린 · 관할 창고 입고 배차 담당`으로 인명과 역할을 함께 보존했다. 최종 native PNG에서 배차라는 단어가 줄 중간에서 갈라지지 않는 것도 확인했다.

두 표의 기존 회차 열은 `운영일`로 바꾸고12일/9일/15일/7일처럼 일 단위를 붙였다. 이 값은 해당 검수 묶음이 실제 운영된 날짜 수이고, 확정 편수와 반려 편수는 그 운영일 동안 접수한 운송 요청의 결과 수이다. 예를 들어 동문 오전은12운영일 동안193건의 편성 요청 중186편을 확정하고7편을 반려한 예시이다. 따라서12일과186편은 같은 단위가 아니며 모순되지 않는다. 서문 야간은9일 동안145건(142확정+3반려), 외곽 순환은15일 동안219건(208+11), 항만 직행은7일 동안100건(98+2)이다. 숫자는 바꾸지 않았으며 fixture 예시 데이터의 분모와 단위만 명확히 했다.

세 갈래 의사결정 질문은 `온도 기록의 검토 상태는?`로 바꾸어 정상/재확인/누락이라는 조건과 직접 대응시켰다. 이 변경은 person3개·table2개·decision-tree1개, 합계6개 fixture의 문구와 필드 의미에만 한정된다.

변경된 세 요소는 라이트·다크 전 허용 크기50조건을 glyph 대비까지 재렌더해 모두0실패를 확인했다. person 원본 대응 비교 시트도 갱신했다. CSS58개와 kit JSON·source palette 및 조립본HTML/CSS/PNG/PDF는 전후 SHA가 모두 같음을 `reassembled-fixture-update-proof.json`에 fixture별 hash와 분리해 기록했다. 조립본은 원본 문구를 유지하므로 이번 fixture 문구 변경이 조립본 화면을 바꾸지 않는다.

의미 수정 후 최종 전체56개·1620조건 `--contrast --resume`가 다시 통과했다. sourceUnchanged=true이며outside/overlap/clip/font/hidden/zero/pixelFailure모두0이다. 최신 sourceSHA256은 `4d779b36aa30680ecc197521249bab44ef1c037ddd0502ec730edc679cfefaa5`이다. paragraph/inline강조검사와block의미단위검사 두 가지 문구중복은모두0,계약오류·경고0이다. 최종요약은 semantic-final-support-016.json이다. 조립본의마지막실제렌더 source hash와최신fixture포함collection hash가달라진이유는같은파일의proof에서명확히구분했다.


## Native typography correction 016 · frozen final pass

Two source-native text errors were corrected solely in element CSS. At the mapped421.77×43.8 prose box, source16px had become12px because short-height and narrow-width container overrides replaced the base size. Those generic base overrides were removed; quiet/lead semantic sizing remains explicit. At the604×78 headline box,3.65cqw used the padded content box (about539.2px), producing19.6815px rather than22px. The valid bounded clamp now uses4.1cqw and caps at the22px contract token. A fresh in-memory native measurement confirms exact16px and22px. No source replica, fixture or assembly HTML was edited.

The other native differences remain visible and recorded: agenda32→31.6158/note18→17.7839 (about1.2%); card26→25.27 (about2.8%, note18 unchanged); steps20→19.7924/note18→17.4393 (about1.0%/3.1%); donut52/24/20 exact. They are small proportional/box-rounding differences and were not silently reported as exact.

Both changed leaves were freshly rendered in light/dark across126 eligible size cases: outside, overlap, clipping, font, hidden, zero-root and actual pixel-contrast failures are0. The complete56-leaf/1620-case final resume also reports all0, sourceUnchanged=true, at SHA `e0cea9b4fe482baebee14a5418b88148747063e3730543dc39c0b9ff7ab2ad7c`. All30 assembly pages and3840×720 triples plus the30-page PDF were rerendered from the updated generated collection CSS snapshot; all HTML bytes/placement/wording are unchanged. The full17-leaf source comparison was refreshed at that same SHA. See audit-native-fix-016.json.
