# Inflexion 컬렉션 재작성 기록

2026-10-24 요청 전문과 레퍼런스 README 전체를 다시 읽었다. 기존 replica 20장과 참조 CSS는 변경하지 않았다. 새 작업 위치는 rebuild-20261024/inflexion이며, 이전 element.css를 읽거나 가져오는 대신 measure_replica.py로 실제 브라우저 DOM 수치를 추출하고 new_library.py에서 새 규칙을 작성했다.

## 대응표와 계약 판단

map.json은 페이지 전체 면과 공통 머리글을 포함한147개 항목이다. 각 페이지의 보이는 DOM/SVG 조각을 누락 없이 분류했으며 원래 selector, outerHTML, DOM와 글자 bbox, 폰트·굵기·행간·자간·색·모서리를 source_metrics에 보존한다. source-dom.json은 빌드 근거이며 제출 컬렉션에는 넣지 않는다.

직접 도출한 요소는18개다. 카드 기본은14페이지의 낮은 중성 gradient panel이며,05페이지의 이미지 위 카드가quiet,08페이지의 외곽 capsule이line이다. flowchart 기본은10페이지의 실제5개 chevron이다.03페이지의 회사 연혁은col,12페이지의 교차 일정은alt다. 연결선은 전체 항목을 가진 하나의 요소 안에 그렸다.

단일 share인 chart-donut을 세 지분 pie로 바꾸지 않았다. 겹친 세 시장 산,구멍 없는 세 지분 pie,복합 phase9열 표,임의L분기·색역할을 가진controllergraph 등은현 계약으로충실히 옮길수없으므로GAPS.md에만 이유와 미래 마크업을 적었다. 복합 panel을 텍스트 card로 위장하거나,다른 카드가 뒤에 오는지 검사해 선을 그리는 규칙은 쓰지 않는다.

## 반응형과 실제 검사

요소 root는명시적인 class[data-el]과container-type:size다. source에서 확인한 길이를요소상자/멤버크기의비율로바꾸고cqw/cqh와clamp를사용했다. 사용자 메시지에서clamp를명시 허용했으므로README의기본금지규정보다이를우선한다. 최소칸은안전하게읽히는실제크기를기준으로선언한다.

최초18개요소1564크기probe에서clip/font/hidden/zero는0이었으나면적차트의선·면이보이지않는실오류를직접확인했다. 원인은positioned0×0 point가pseudo의containing block이되며anchor insets가0으로fallback한것이다. series를positioned부모로,point를static·0폭으로두고margin으로높이를주는수학으로수정했다. 면과기울기는CSSanchor에서같은좌표를사용한다.

큰칸에서원본비율보다글자가지나치게작아지는문제도직접확인해,원본폰트/상자비율에맞춰상한을확장했다. 작은칸의최대값라벨은별도plotheadroom을확보하고label-line을사용한다. 인물과포지셔닝원안의이름은작은container규칙이과도하게일찍적용되지않도록수정했다.

5개이상point에는일반적인5분할Y축밀도규칙을적용하여13페이지왼쪽area도같은요소로표현했다. 값이나fixture이름을검사하지않고멤버수만사용한다.3분할인13페이지오른쪽은여전히unexpressible이다. 기존palette/style공급과별개로모든본문tracking이normal임을실DOM에서확인하여parentkit의공유tracking도0으로교정했다.

## 전역 6자 문구 검사
여섯 덱 전체 원문의 정규화 6자 연속 일치를 검사한다. 직접 요청을 우선하여 필수 card-2-quiet 문장만 “기록과 지표가 한곳에 모여 바로 결정을 내립니다.”로 바꾸고 모범 마크업과 숫자는 보존했다. 원래 모범 문장의 공통 어미 “할 수 있습니다”가 다른 덱의 원문과 충돌한 데 따른 명시적 예외다. 비모범 영문 표제와 업무 문장도 독립 문구로 교체했다.

## 최종 시각 리뷰에서 고친 실오류
막대 기본의 하단 모서리도 원본처럼 둥글게 만들고, 작은 범례 키는 너비에 따라 늘어나는 가로막대 대신 정사각형을 유지했다. 코드 줄 번호10–12의 세로 줄바꿈, Venn의 불투명 면이 앞 원 이름을 가리는 문제, 작은 dumbbell 수치가 맞붙는 문제를 수정했다. cycle에 실제 방향 화살표를 넣고, decision-tree와mindmap의 모든 분기를 코어까지 연결했다. 네 donut은 작은 너비에서2×2로 돌아서며 각 멤버가 부모 높이의 절반을 갖도록 했다. 겹친 area 면이 앞 계열 라벨을 가리지 않도록 데이터 라벨을 별도 앞 레이어로 옮겼다.

작은흰숫자/a3초록면의실제대비가3.08이라reference팔레트는그대로두고각stack값뒤에작은page/ink중성라벨면을두었다. matrix.on아래중첩list는강조면의잉크역할을상속하도록교정했다. pseudo배경을측정하지못하는bar/balance,원밖scatter라벨은rawcontrast오탐과실제화면을구분한다.

원본19하단callout의옅은gradient끝에흰작은글씨를그대로두면대비계약과충돌한다. 컬렉션은a1의94%까지완만하게옮겨대비를우선했으므로원본보다면의밝기변화가작다. 원본15quietnote의맨끝“다.”고아줄과배경밖문구는불변replica에남아있다. 재조립에서는quietnote·timeline note·hub note·plaincard note의원본문장과단어는보존하고수동br만빈칸으로바꿔격자너비에서다시줄바꿈했다.

## 재조립의 격자 제약
기본격자는1116×496,12×6,gap20이다. 원본bbox를가장가까운시작track과span에한번대응했다.04의MISSION/VISION세역할은각각foundation.group.col안의tag/headline/prose로묶어텍스트겹침을없앴다.14의95px카드3개도group.col을쓴다.12의세번째사진은timeline note를가리지않도록한행아래,13의긴caption은선언한4열최소칸,17의짧은caption은자기면안에글자가들어가도록2열,20의budgetcaption은인접list와겹치지않도록한열왼쪽을사용한다. 이변경은grid-column/grid-row만이며새페이지CSS를추가하지않았다.

이재조립은원본과100%동일하다고주장하지않는다.20개unexpressible항목은GAPS.md의이유에따라비워두고HTML주석으로남긴다.03복합제품panel,06TAM산형도,11/15세지분pie,16controller분기,17성장화살표,18아홉마일스톤등큰차이가이에속한다. 그밖의작은좌표·행높이·글자크기차이는12×6nativegrid의양자화와요소의일반반응형규칙에서온다. 그림placeholder는번호가있는연한중성면이다.

01의두pill도cover.body>stack안으로옮겼다. stack은column1/span2,row6/span1만쓴다. 원본74/561위치와148×96쌍을정수격자에그대로넣을수없어위치와사이간격차이가남는다. meta는요소컨테이너로사용하지않는다.

실제글자위치의pixelcontrast검사에서추가로확인한두실오류도수정했다. 짧은높이에서긴bar범주가막대면위로올라가던것은축font를cqh에도연동하고,겹친area의작은값라벨은page배경의작은seat를주어a1-7글자대비를보장했다. area의면색은page와섞인불투명색이아닌transparent와섞은투명면으로바꿔두계열의선과값을모두보존한다.


## Final freeze receipt

최종 56요소/193fixture, 크기 시트 112장·2364조건의 outsideText/textOverlaps/clipped/fontFailures/hiddenEssential/zeroRoots는 모두 0. 실제 글리프 대비 214조건 실패 0. 현재 CSS와 활성 요소·중첩 요소 CSS/kit/foundation 대조 112시트 불일치 0 (`audit-render-current.json`). 원본/replica/조립본 20장 개별 비교 완료. 최종 조립본은 Lucide review runtime을 포함하며 1280×720 PNG20장과 PDF20쪽, triple3840×720 PNG20장, library PDF 라이트56쪽·다크56쪽. 마지막 렌더의 rawOverflow59는 pseudo/anchor/bleed/SVG 경계 진단으로 남기며, 실제 문자 영역의 페이지 초과·문자끼리 겹침은 20장 모두 0이다. 계약 밖 형상20개는 GAPS에 남겨두었고 임의 요소로 바꾸지 않았다.


### Cover metadata contract correction

최신 요청5와 README의 cover 계약(no head/body)을 우선해 표지의 Journey/Innovation pill 두 개는 `.meta`의 두 자식으로 복구했다. 표지에서 이 두 항목은 본문이 아닌 발표 메타데이터다. 이 결정은 앞서 적용한 일반 본문 그리드 근사 기록을 대체한다. 요소 CSS와 fixture는 수정하지 않았다.


## Source-only grid correction — final superseding decision

이 절은 이전 검수 기록의 12·13·17·20페이지별 좌표 보정 설명을 대체한다. `build/reassemble.py`의 해당 네 `grid-column`/`grid-row` 문자열 replace를 완전히 제거했다. 조립본 화면이나 요소 CSS에서 좌표를 역산하지 않는다.

일반 요소는 원본 bbox의 양 끝점과 가능한 12×6 그리드 끝점의 제곱거리 합을 최소화한다. 이미지 프레임에는 원본 두 축을 등방으로 스케일했을 때 생기는 종횡비 잔차를 대칭으로 더한다. 이는 04의 정사각과 12의 가로 프레임 모두에 같은 식을 적용한다.

작은 pill은 원본 paint bbox를 포함하는 최소 폭과 인접 폭 중 원본 중심에 가까운 슬롯을 고른다. 같은 원본 기준선에서 분리되어 있는 작은 요소들은 공통 DP가 좌우 순서를 보존하며 함께 배치하고 같은 세로 슬롯을 쓴다. 13의 세 caption과 20의 caption·목록이 같은 규칙을 받는다. 별도 capsule은 원본에서 위아래로 분리된 내용과의 앞뒤 관계를 source paint 높이와 이웃 grid edge로 보존한다. 페이지 번호·fixture 이름·렌더된 CSS 값은 이 판단에 들어가지 않는다.

20의 목록은 source_metrics에서 13px/450·20.15px 행간·4항목 2열이다. 4-item compact 목록을 공유 type 토큰의 13/12 비율로 최대 13px에 맞추고, 두 열의 간격과 빈 note 때문에 생기던 item 내부 grid 간격을 바로잡았다. 실제 글줄의 기준선 간격은 20.14px(브라우저 양자화)이고 각 항목은 한 줄이다. source20은 본문색 역할 `--ink`를 쓴다.

.on pill의 원본 padding은 좌우16px/상하3px이다. 실제 kit gap-sm이10px임을 다시 확인해 좌우를 pad×2/3으로 교정하고, 상하는 기존 gap-sm×.3으로 유지했다. 중간 검수에서 gap-sm을12px로 가정한 산정은 잘못되었으며 최종 CSS에는 적용하지 않는다. 기본148×41 pill, 부모가 최종 수정한 card-4의 문자 아이콘 CSS와 모범 마크업은 보존했다.

원본의 모든 좌표를 정수 12×6 트랙으로 표현할 수는 없다. 예를 들어 20의 compact 두 요소를 원래 순서와 폭으로 함께 담으면 caption은 (column7,span2), 목록은 (column9,span4), 공통 row5/span2가 최적이다. 이 차이는 source bbox에서 나온 그리드 근사이며 CSS를 피하려고 넣은 페이지 보정이 아니다. 17의 caption은 원본의 본문 앞 관계를 지키는 한 행 슬롯을 쓴다.

비모범 table의 operating-compact/expanded는 수치가 증감률이므로 열 이름을 ‘차이’에서 ‘증감률’로 고쳤다. source comparison과 조립본 원문은 바꾸지 않았다.


최종 재검수: 수정한 list/pill/table와 중첩 matrix/person/pricing/versus의 446조건은 outsideText/textOverlaps/clipped/fontFailures/hiddenEssential/zeroRoots/실제 글리프 대비 실패 모두0. 현재 leaf별 전체2364조건도 동일 항목0이며 실제 글리프 대비 검사2364조건 실패0이다. 112모드 시트의 현재 활성 CSS·fixture 대조 불일치0, static56요소/193fixture 오류0, 전덱6자 중복0. 원본 대조18시트와 20장 삼중 비교를 최종 소스로 다시 렌더했다. 페이지PNG20장1280×720, 삼중PNG20장3840×720, PDF20/56/56쪽 동기화. 소스·페이지별SHA-256은 final-source-grid-receipt.json에 기록했다.

컬렉션 소스 SHA-256: `cf79cc66d953f4b6e00c934af2c392c95f43c0fdd9214909f08a474a4454bed7`. 부모 card CSS는 `1c1644b273444ea2c4b8e26bd018895b1e53cd8b08f563aa192f0d8462407534`로 보존했다.


## 원본 요소 bbox의 타이포 비율 분모 재검수

18개 mapped base를 실제 source bbox 폭·높이로 별도 브라우저 렌더하여 자식의 computed font를 비교했다. 원본 요소를 넓은 캔버스에 둔 크기와 요소의 실제 paint bbox를 혼동한 비율, 중첩 entry가 새 size container가 된 점, 작은 원본에도 적용된 반응형 breakpoint를 수정했다. 페이지 번호·fixture 이름 조건이나 조립 grid 보정은 추가하지 않았다. 부모의 card 모범문자 중심 패치는 그대로 유지했다.

|요소|원본 수치(px)|수정 전 native(px)|수정 후 native(px)|
|---|---|---|---|
|agenda|.mark 20; .name 20; .note 20|.mark 16.653; .name 14; .note 14|.mark 20; .name 20; .note 20|
|timeline|.kick 18; .name 16|.kick 12; .name 12|.kick 17.999; .name 15.999|
|prose|>p 18|>p 14.158|>p 17.994|
|image-frame|>.seat 14|>.seat 12|>.seat 14|
|flowchart|.node>.name 18|.node>.name 12|.node>.name 18|
|chart-area|.pt>b 14; >.axis>span 14|.pt>b 12; >.axis>span 13.994|.pt>b 14; >.axis>span 13.994|
|chart-bar|>.bar>b 14; >.bar>span 16|>.bar>b 12; >.bar>span 12|>.bar>b 13.999; >.bar>span 15.997|
|metric|.parts>.fig 120; .parts>.fig>small 52; .parts>.name 18; .parts>.note 17|.parts>.fig 72; .parts>.fig>small 24; .parts>.name 17.92; .parts>.note 12|.parts>.fig 120; .parts>.fig>small 52; .parts>.name 18; .parts>.note 17|

나머지 base는 대체로 0–0.7px 오차 범위다. positioning 강조 mark는 native18.85px 대 원본20px로 약1.15px 차이가 남으며 이번 분모 오류 수정 범위와 구분했다.

원본 bbox와 정수12×6 조립칸의 크기가 달라지는 축소는 별도로 기록한다. agenda는 원본745.97×404에서20px, 조립737.34×410에서19.773px이다. prose는 원본534.25×48.89에서17.994px, 3-member group 내부 조립453.33×37.33 및548×37.33에서는 높이비76.35%에 따라13.743px이다. flowchart는527×178에서18px이나547.98×152 조립에서는15.371px, metric은493×256에서120/52/18/17px이나547.98×238에서는111.56/52/16.73/15.80px이다. 요소 native가 맞는 경우 조립칸을 CSS에 맞춰 다시 바꾸지 않았다.

8개 변경 요소의 light/dark 전체 size 시트를 직접 확인했다. 588사례에서 잘림·텍스트 겹침·영역초과·폰트·숨김·zero·실제 glyph 대비 실패가 모두0이다. 18leaf 원본 대조시트와 20페이지 PNG/삼중비교를 갱신했고, 20페이지 실제 텍스트 overlap/outside가0이었다. 정확한 새 SHA와 전체2364사례는 final-source-grid-receipt.json 및 size-summary-all.json을 참조한다.

추가 native crop 검수에서 metric의 신규 긴 note가 원본보다 한 줄 늘어 양 끝이 약6px 넘는 것을 확인했다. `.parts`의 멤버 간 gap을 `min(var(--gap),3.9cqh)`로 바꾸어 native256px 높이에서 약10px 간격을 사용한다. 글자120/52/18/17px는 보존하고 source-native bbox 안에 전체 멤버를 넣었다. 특정페이지나fixture 조건은 없다. metric32크기·모드 재검사 전 항목0.
