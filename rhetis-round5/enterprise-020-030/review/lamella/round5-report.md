# Round5 — lamella

## 새 디자인 폴더 ← replica 페이지

- `architecture--columns` ← 09
- `card--allocation` ← 20
- `card--compact` ← 06
- `card--driver` ← 21
- `card--licensing` ← 12
- `card--summary` ← 02
- `card--white-step` ← 08
- `chart-area--adoption-growth` ← 17
- `chart-bar--financial-combo` ← 21
- `chart-bar--market-growth` ← 11
- `chart-donut--allocation-pie` ← 20
- `chart-donut--allocation-ring` ← 14
- `chart-donut--channel-share` ← 14
- `headline--white-tab` ← 07
- `person--details` ← 04
- `positioning--competitive-field` ← 15
- `prose--calculation` ← 10
- `quote--double-glyph` ← 18
- `quote--tracked-author` ← 05
- `table--financial-summary` ← 21

## 패널을 쓴 곳

- 14 / 14-r5-furniture-92: Leaf-titled channel column with97px ring, rich prose and vertical rule at19px inset.; bbox [49, 232, 291, 488]
- 14 / 14-r5-furniture-93: Leaf-titled channel column with97px ring, rich prose and vertical rule at19px inset.; bbox [340, 232, 291, 488]
- 14 / 14-r5-furniture-94: Leaf-titled channel column with97px ring, rich prose and vertical rule at19px inset.; bbox [631, 232, 291, 488]
- 20 / 20-r5-furniture-96: Funding title strip plus3allocation cards at52/180/308px local y, each356x108 with20px gaps; independent page rule is preserved.; bbox [776, 211, 375, 415]
- 22 / 22-r5-furniture-95: Leaf advisory caption +three independently ruled text columns, no invented portraits.; bbox [49, 575, 883, 145]

## 차트 확장

- `chart-area--adoption-growth` ← 17; 묶음/조각/공유축/주석은 요소가 소유한다.
- `chart-bar--financial-combo` ← 21; 묶음/조각/공유축/주석은 요소가 소유한다.
- `chart-bar--market-growth` ← 11; 묶음/조각/공유축/주석은 요소가 소유한다.
- `chart-donut--allocation-pie` ← 20; 묶음/조각/공유축/주석은 요소가 소유한다.
- `chart-donut--allocation-ring` ← 14; 묶음/조각/공유축/주석은 요소가 소유한다.
- `chart-donut--channel-share` ← 14; 묶음/조각/공유축/주석은 요소가 소유한다.
- `positioning--competitive-field` ← 15; 묶음/조각/공유축/주석은 요소가 소유한다.

## 지운 일반 요소

`agenda`, `architecture`, `balance`, `bullet`, `callout`, `chart-area`, `chart-bar`, `chart-donut`, `chart-line`, `chart-scatter`, `chart-stack`, `chart-waterfall`, `code`, `cycle`, `decision-tree`, `delta`, `flowchart`, `funnel`, `gauge`, `heatmap`, `hierarchy`, `hub`, `journey`, `legend`, `list`, `logo-group`, `matrix`, `matrix-nine`, `metric`, `mindmap`, `network`, `pill`, `positioning`, `pricing`, `pyramid`, `radar`, `sankey`, `slope`, `sparkline`, `steps`, `swimlane`, `timeline`, `treemap`, `venn`, `versus`, `waffle`

공통 상태 fixture는 선택이므로 기존 필수 예시를 6개 제외하고, source 기반의 새 한국어 fixture와 데이터 변형을 남겼다.

## 남은 gap과 이유

- 없음. 글자 스타일·캡션·측정 잔여물·큰 제목·사진 비율은 gap으로 분류하지 않았다.

## 실제 최종 시트·비교

요소별 `sheets/<design>-light.png`, `-dark.png`, `-replica.png`; foundation도 동일한 크기별 시트다. 실제 열람 증거는 주 담당자의 `root-final-review.json`의 최종 PNG 해시와 아래 담당자 기록에 연결한다. 조립 비교는 `compare-reassembled/slide_NN.png`이다.

### review-round5-charts

# Round5 차트·표·포지셔닝 검수

chart-donut--channel-share ← replica14. 세 독립 채널의15.3px name/97px ring/30%hole을 panel 안에서 독립 사용하도록 분리했다. 기존3-member그룹id를제거하고3instance를기록. 첫시트에서line1로인한글자range위쪽초과78건과큰칸의과도한이격을직접보고,1.2line및source의131/97비율묶음을가운데로정돈하여fresh재작성. 최종78칸두모드9QA0/원문0. light/dark의네fixture전행과native최소칸을모두열어확인했다. 출처파일: delivery/lamella/review/replica/slide_14.html. 최종실제검수: review/sheets/chart-donut--channel-share-light.png·dark.png 및build/chart-donut--channel-share-review/*-all-minima.png. source조각대조는향후root합성페이지에서도확인한다.

chart-donut--allocation-pie ← replica20. 400px holeless sector3개를실제CSS conic/polar 데이터로복구. --from누적각과선택label좌표를 root승인하에사용하며선택좌표없는4sector긴fixture도검증. 원문의첫sector40%면적/Ops30%표시와마지막30%면적/R&D40%표시불일치는round5_markup에만그대로보존했고새한국어fixture는모두비중과숫자를일치시켰다. 최종26칸두모드9QA0/원문0. 모든행·native최소칸을직접확인. 실제본파일 review/sheets/chart-donut--allocation-pie-light.png·dark.png,build/chart-donut--allocation-pie-review/*-all-minima.png.

chart-donut--allocation-ring ← replica14. 실제310px/40·30·30 sector 및30%hole을복구. 첫sector에는큰비중+3줄name,둘째는비중만,셋째는원본에서보이지않는값/이름을임의로추가하지않음. 긴4sector변형은모든이름을보이게확인. 최종26칸양모드9QA0/원문0, 실제본파일review/sheets/chart-donut--allocation-ring-light.png·dark.png와전행/native최소칸.
정직한정정: pie/ring의초기fixture()가첫descendant style에grid를넣던마크업오류를root검수에서발견했다. 최상위파싱으로helper를고치고두design의모든fixture를정상rootgrid로재작성한뒤전칸을다시렌더하고직접열었다. harness자체가각칸마다rootgrid를변경하므로초기QA0은이정적계약오류를잡지못했다. 현재루트grid자동검사도별도로통과.

table--financial-summary ← replica21. source1038×127·4column·21pxrow·수평선만있는compact표를새작성. 가장큰칸에서도127/1038비율의낮은표를세로중앙에유지하며source처럼첫머리칸만채움,이익행전체soft강조. 원문OCR결함2)/coos/$18/05/40을round5_markup에그대로보존, 잘린header조각은일반tail정렬part로오른쪽끝만유지. 새fixture는정상한국어5·6행재무데이터. 최종24칸양모드9QA0/원문0, 전행·native최소칸직접검수. 실제본파일review/sheets/table--financial-summary-light.png·dark.png 및build/table--financial-summary-review/*-all-minima.png.

positioning--competitive-field ← replica15. source706×560交叉축과98/176px경쟁사원,194px강조droplet,큰mark의3행note를새작성. 단일축명/--r사이즈·note확장사용. 기본fixture는inherit로ink를받고원문inst는foundation_context:on으로흰면문맥을받음(root승인). 원본soft면위흰색의낮은대비는source자체한계로기록. 첫시트9QA0이었으나실제PNG의위·우측화살촉2~3px면초과를추가픽셀검사에서찾아내아래/왼쪽으로회전bbox만큼정확히안착시킴. 최종18칸9QA0/원문0, 두모드전행/native최소칸과화살촉경계픽셀을직접확인. 실제본파일review/sheets/positioning--competitive-field-light.png·dark.png 및build/positioning--competitive-field-review/*-all-minima.png.

chart-bar--market-growth ← replica11. source106pxbar·55pxgap·392pxplot·$100축최대값을한root로묶고164pxCAGRdroplet와투명곡선outline을복구. outline은sourceBezier경로를표본화한후양측0.5pxoffset한evenodd CSSpolygon으로그려밑bar를가리지않는다. 주석foreground는선언된--lamella-market-drop-ink기본ink,원문만page역할override(root승인);새긴fixture는deepa1-7/page문맥도검증. 원문soft면/흰색대비한계는source자체이며축전체를흰색으로바꾸지않음. 최종20칸9QA0/원문0, 두모드전행/native최소칸직접검수. 실제본파일review/sheets/chart-bar--market-growth-light.png·dark.png 및build/chart-bar--market-growth-review/*-all-minima.png.

chart-area--adoption-growth ← replica17. source723×502 plot, 두 6점 series, .7px stroke, 6px dot, source 전역투명도에서 파생한 gradient를 새 작성.164px 성장 droplet 및123px retention주석과성장배지아래두줄 milestone도 chart직계.at로포함. 처음20칸의 fig/name Range 겹침은 실제 single-line glyph ink는분리되어있음을native로확인했고 root가공유검사를실제glyph기준으로보완했다. source좌표는그대로유지. segment별fill의AA세로seam은실제로보여거절했고 series의prefixed파생값으로단일polygon을그리도록전면새작성해제거했다. child --v와파생값40개를자동대조하여전부일치. 최종20칸양모드9QA0/원문0, 전행/native최소칸과면내부seam제거직접확인. 실제본파일review/sheets/chart-area--adoption-growth-light.png·dark.png 및build/chart-area--adoption-growth-review/*-all-minima.png.

chart-bar--financial-combo ← replica21. source643×310, 133px막대3개·71pxgap·네 y축값, .line>.pt3개(10px hollow dot/2px stroke)와BEP capsule을같은chart root에새작성. plot별다른수치를유지하면서같은좌표공간에원문의막대·상승선을복구. source0축의OCR SoM은원문조립에만보존,새한국어fixture는정상0/새재무데이터.4멤버긴변형포함최종20칸양모드9QA0/원문0, 전행/native최소칸직접검수. 실제본파일review/sheets/chart-bar--financial-combo-light.png·dark.png 및build/chart-bar--financial-combo-review/*-all-minima.png.

최종 source 대조 직접 열람: 위 여덟 디자인의 review/sheets/<design>-replica.png 전부. allocation-pie의원문면적/표시불일치, positioning의원문blue면/white전경과기본fixture의page면/ink전경문맥차이는의도적으로구분했다. market-growth의독립projection본문카드는기존source card소유로유지하며차트에중복추가하지않는다. 전체신규8디자인232 native칸은마지막CSS수정뒤양모드전행을다시열어확인했다.

주 에이전트 요청으로 retained 전체 최종검사까지 수행했다: 30디자인/1144 native칸, 공유의존성 stale14개 최종렌더 후 stale0/9QA0. 실제 CDP 폰트160 fixture-mode검사에서load/fallback0, raster1144칸 전부bleed0, PNG무결성과정확한crop치수1144개모두통과. refresh변경은card76칸이며나머지13개는native동일. card최소8칸및light12x6/dark.on12x6 실제PNG를직접추가검수했다. 이감사에서CSS/fixture수정은없다. 증거: build/round5-lamella-final-audit.json.

### review-round5-diagrams

# Round5 diagrams 검수 — lamella

신규 1개 디자인, 원본 1개 인스턴스, 최종 8개 light/dark 크기별 셀을 직접 열어 확인했다. 9개 자동 지표·raster·복제 문구 검사·정적 계약 오류는 모두 0이다. 원본 replica는 수정하지 않았다.

## 출처와 크기

- `architecture--columns` ← replica 09. 8칸. operations-platform: min 9x4, partner-platform: min 9x4.

## 판단·잔차

- 09의 Experience/Intelligence/Foundation은 세로 계층이 아니라 가로 architecture--columns다. cap·세로 guide·3×3 module의 한 의미 구조를 그대로 소유한다.
- 291px 열 pitch, 217×30 leaf cap, 271×85 module, module 안의 238px 실제 본문 폭을 source 수치로 옮겼다. cap별 11/18/17px 및 자간·inset 차이를 own child 디자인 부품으로 보존했다.
- 가운데 첫 module은 큰 문장 하나와 작은 설명 두 줄인 원본 rich content다. .detail 자식으로 실제 정보 위계를 보존했으며 fixtures는 같은 형상과 새 한국어 업무 문장으로 작성했다. 마지막 수정 뒤 8칸 모두 다시 렌더·직접 확인하고 copy 검사도 다시 수행했다.

## 실제 렌더 확인 기록

마지막 소스 변경 뒤의 native 패널과 각 셀 PNG SHA-256, 원본 크기 대조 PNG의 SHA-256은 같은 이름의 JSON에 기록했다. native 패널은 원본 셀 이미지를 축소하지 않고 배치한 확인 자료다. 요소 안의 글자/면 경계, 두 모드 대비, 정렬, 작은 칸의 유지, 연결 방향을 확인했다. 새 unexpressible은 없다.

전체 페이지 조립, 공유 foundation, 최종 공개 패키지는 주 에이전트가 별도로 통합 검수한다. 이 기록은 담당 요소의 최종 소스·크기별 시트·source bbox 대조에 대한 기록이다.

### review-round5-systems

# Round5 foundation 최종 담당 검수 기록

담당 소스는 동결했습니다. replica는 수정하지 않았습니다. root의 통합 페이지 검수와 최종 수락은 별도입니다.

01–23의 fitted 행과 큰 제목은 실제 크기·자간·행간에서 비율화했습니다. 14 세 leaf-column은 각 headline/channel-share/prose 전체 DOM 폭291px를 담습니다. 22 advisory-strip은 headline+세 자문 본문과 괘선을 소유합니다. 20 allocation-panel은 제목띠+3 card--allocation을 source y262/390/518 간격으로 묶어 grid 행 양자화 차이를 줄였습니다. CardB/ar/ge 및 font= 측정 잔여물은 재등장시키지 않았습니다.

타이포 수치는 실제 source DOM/Range/loaded font를 읽어 요소 상자 비율로 옮겼습니다. SVG text는 선택 가능한 HTML로, source 인장은 실제 글자 좌표/회전으로 그렸습니다. 폰트 크기는 공유 type8–256과 cqw/cqh의 clamp를 사용하며 디자인 색상은 팔레트 자리만 사용합니다. 장면 selector나 fixture별 CSS 보정은 없습니다.

source 장치 96개, 기존 중복 제거 ID 70개입니다. source 페이지/정확 bbox/완전 원문 markup 및 nested source_children은 build/map-round5-systems.json에 있습니다. 불필요한 원문 fragment/측정 dump는 새 장치로 만들지 않았습니다. 담당 신규 unexpressible은 없습니다.

최종 size matrix는 foundation/fixtures 14개, 양모드 합 112칸입니다. review/validation/foundation.json의 9종 QA는 모두 0입니다. proof source_hashes는 실제 현재 파일과 일치합니다. 새 한국어 fixture와 전체 frozen replica의 정규화 6자 중복 검사도 0건입니다. 원문은 검증 조립 markup에만 둡니다.

실제로 연 최종 자료: review/sheets/foundation-light.png와 foundation-dark.png를 그대로 보존한 root-sheet-pairs/lamella-foundation-part01.png부터 part04.png까지 모든 행의 양모드 pair를 직접 열었습니다. 작은 칸에서도 도형/선/표/문자가 겹치거나 잘리지 않는지 확인했습니다. 별도로 직접 연 native 칸: r5-panel-allocation-light-9x4.png, r5-panel-channel-1-dark-3x6.png, r5-panel-advisory-strip-light-9x4.png. 앞선 source/native 검토와 이번 마지막 렌더 파일 검토는 구분하며, 최종 전체 페이지 원본|replica|조립본 비교는 주 에이전트 담당입니다.

거대 native PNG는 바꾸지 않았습니다. 축소 pair manifest에는 각 원본 SHA256·크기·source hash current 여부·chunk 행/좌표가 기록되어 있습니다. 이 자료의 상태는 awaiting_root_visual_review이며 자동 수락하지 않았습니다.

### 주 담당자 통합 검수

# 주 담당자 최종 통합 검수

## 검수 범위와 판정의 뜻

7개 컬렉션은 동결 replica의 실제 source 수치로 만든 디자인과 필요한 의존 요소만 남겼다. 남긴 요소107개, 신규 독립 디자인44개, 제외·보존한 일반 요소329개다. 요소의 크기별 light/dark 시트와 foundation 시트를 직접 열었고, 원본 | 동결 replica | 조립본 비교를87페이지 각각 열어 확인했다. 담당자는 각 native 칸을 확인했고 주 담당자는 통합 시트와 페이지 대조를 확인했다. 최종 파일 해시별 열람 기록은 root-final-review.json에 있다.

READY는 계약·반응형 fixture·현재 소스와 증거의 일치·파일 무결성 판정이다. 원본과 픽셀 단위로100% 같다는 뜻이 아니다. 아래 잔차를 숨기지 않는다. gap0은 round5의 확장 계약으로 표현하지 못한 디자인이 없다는 뜻이며, 시각적 차이가0이라는 뜻이 아니다.

## 직접 고쳐 확인한 문제

- Lamella20: 작은 도넛3개로 바뀌었던 구성을 지우고, 원본의 큰3조각 파이1개와 오른쪽 배분 패널/카드3개를 복구했다. 파이와 카드의 연결된 데이터/형태를 독립 요소가 소유한다.
- Cutfield02: 빠졌던 과녁 도형을 source의65×65 벡터로 복구했다.03 하단 절단면의 마지막 조각을 원본 팔레트 역할로 정정했다.06 목록 화살표와11 타임라인,08·12·13의 source 반전 글자 역할도 정정했다.
- Portico12: 사진의 흰 테두리, 회색 사진 자리, 교대 면, 금색 직함을 source 수치로 복구했다.
- Toggle04:212×212 원형 사진 테두리를 복구했다.12 중앙 영문은 허용된 가변 폭 폰트로1행을 유지한다. source Oswald 폭252.296875px에 대해 대체 Noto Sans 폭251.78125px이며, 글리프 모양 차이는 남는다. 글자를 기울이거나 transform으로 늘리지 않았다.
- Filament01: 반전 표지에서 사라졌던 ellipse seal의 currentColor 상속을 복구했다.04·07에서는 부모 표제에 들어 있는 span을 별도 인스턴스로도 포착했던 중복2건을 지웠다. 원본 부모 마크업은 보존했다. 전체7덱 DOM 부모/자식 자동 검사에서 이 두 건 외의 중복 포착은 없었다.
- Rulemark06: data.sourceText를 읽지 않아3개 카드의 parts가 비었던 조립기 문제를 바로잡았다. 원문 숫자·제목·설명을 kick/name/note로 읽는다. 페이지별 CSS 보정은 쓰지 않았다.

## 남겨 둔 차이와 스스로 내린 결정

- 모든 사진·복잡한 브랜드 로고·일러스트는 회색 placeholder다. Filament04의 입체 점 구체와 개별 로고, Toggle01의 기울어진 덱 몽타주도 이 범주로 판단했다. 단순 도형/괘선/표/차트는 구현했다. placeholder 숫자는 이미지 내용이 아니며, 독립 자리와 패널 안에서 번호/표시 여부가 원본과 다를 수 있다(Portico05, Toggle06 등).
- Lamella의 동결 replica01·03·06·08·09·11·13·14·16·18·19·21에는 일부 영문 표제가 과도한 음수 자간으로 뭉쳐 보이는 문제가 이미 있다. 동결 replica를 변경하지 말라는 요청에 따라 그 수치를 유지했다. 이는 원본 이미지와의 알려진 차이다. 신규 한국어 fixture에서는 이 겹침이 없도록 검수했다.
- 12×6 정수 슬롯의 양자화 때문에 본문/카드 간격이 source와 다를 수 있다. 구체적으로 Tide08 callout source bbox[210,553.34,860,23.89]는 슬롯[210,565.285,860,79.715]에 놓여 문장 시각 중심이 약40px 아래로 내려간다. 이를 숨기는 페이지 CSS나 전체 장면 패널은 만들지 않았다. Rulemark02의 목차 열, Filament05의 사진/본문 배치, Lamella19의 일정표 구획에도 그리드 비율 차이가 있다.
- Rulemark09의 밝은 단계 면은 읽기 쉬운 palette foreground를 사용하여 원본의 흰 글자와 다르다. source를 재현하기 위한 일부 밝은 반전 면은 해당 데이터의 팔레트 바인딩으로 흰 글자를 유지했다. 밝은 사진 placeholder 위 source의 흰 문구(Cutfield06)는 replica의 대비 문제도 물려받는다. 이 조립본 문맥과 신규 fixture 대비 검사는 구별한다.
- Portico02의 목차10개는 독립5행 두 열로 해석해 foundation panel로 묶었다. 전체를 계약 최대 멤버 초과 gap으로 버리지 않았다. Toggle12의 위 화살표는 hub와 표를 묶는 panel의 연결 장치다.
- Lamella20의 source 파이 실제 조각40/30/30과 source 라벨30/30/40의 불일치는 검증 조립본에서 그대로 보존했다. 새 fixture의 값과 라벨은 일치한다.
- Filament01 Branding의 왼쪽−14px 출혈은 frozen replica의 의도된 페이지 가장자리 잘림이다. 실제 텍스트 Range 검사에서 이 source 출혈만 별도로 기록하고 새로운 페이지 밖 글자 오류와 구분했다.
- 실제 로드할 수 있는 README 허용 폰트 중 가까운 글꼴을 썼다. Lucide로 대체한 아이콘은 원본 그림과 획/자형이 다르다.8px보다 작은 source 글자는 확장된 타입 토큰의 하한8px를 따른다. 원본의 부드러운 색조는 팔레트 자리와 preview palette로 옮겼으므로 색 보간/렌더링 차이가 있다.

## 보존과 배포

동결 replica192개 파일은 SHA256로 보존 여부를 검사한다. 소스 ZIP은 컬렉션 최상위 폴더1개와 허용된.css/.json/.md/.html만 포함한다. 검수 ZIP에는 지도·최종 크기별 시트·요소 대조·조립 소스/PNG·원본/replica/조립 비교·검수 증거를 담는다. git 명령은 사용하지 않는다. GitHub REST API로 기존 main의 트리를 보존한 새 commit을 만들고 force:false로 반영하며, 올라간14개 ZIP을 고정 commit에서 다시 내려받아 SHA256/CRC/멤버/PNG 크기를 검사한다.

