# Review notes

기존 replica의 HTML/CSS/PNG/PDF는 수정하지 않았다. replica-freeze.json의191개 SHA-256과최종파일을대조한다. 기존 element.css는 읽어고쳐쓰지않았으며, 새 생성기는 replica의수치와계약fixture마크업만자료로읽는다. old/new CSS의byte비교는재작성여부검증용이다.

픽셀의색은검수호스트 source-palette.json에만있고 컬렉션CSS는팔레트자리만사용한다. 라이브러리light/dark는수정하지않은reference palette로검수한다. 원본팔레트의낮은텍스트대비를라이브러리로옮기지않았다.

모범구성마크업·숫자데이터는원본과같다. 단, card-2-quiet의“기록과 지표가 한곳에 모여 바로 결정할 수 있습니다.”는원본덱문구와6자겹침이있어 “기록과 지표가 한곳에 모여 바로 결정을 내립니다.”로한문장만바꿨다. 새사용자요청의문구복제금지가README의문구유지보다우선한다. validator는이정확한한문장외차이를허용하지않는다.

fixture는모양·멤버수·문장길이를따라새한국어업무내용을썼다. 6자검사는여섯replica전체에대한NFKC/소문자/공백·문장부호제거후텍스트노드내연속6자대조다. 단순히회사명만바꾸지않았다. 코드fixture는실행가능한SQL/Python문장과새한국어주석으로썼다.

검수이미지는1280×720브라우저에서그린다. 시트는요청된9종크기중min의두축이상인크기와min을모두포함한다. root가스스로줄어들어도배정grid칸전체+6px를잘라기록한다. 원본대조는map.bbox의frozen replica조각과source-palette12×6/min을나란히보인다. 최종조립비교는원본|frozen replica|새조립순서의3840×720이다.

자동검사는텍스트범위의밖으로나감·겹침·clip조상·font error·숨긴name/fig·0크기root·chip기하중심을보존한다. 실제글자위치와글자를숨긴두번째스크린샷으로대비를계산한다. 단순조상배경/gradient최악stop방식의rawContrast도삭제하지않고오탐근거를구분한다. 작은숫자면의대비가공급palette에서부족할때는page/ink숫자판으로보장한다. chip은추가로렌더된ink의상하·좌우중심도기록한다.

연결도는요소가선을그린다. 행사의무관한장식을이웃card유무로만들지않는다. flowchart/swimlane의방향flag는인접grid칸으로연결한다. 마지막node의to-u도그위칸으로돌아가며DOM다음node를추측하지않는다. decision모양은.name면만마름모로잘라연결화살표를자르지않는다. 조직도선은마지막자식의중심에서끝난다. 누적면적의--v는계약대로누적값이고역순z-order로올바른층을보인다.

새조립에는계약class/data-el과foundation만있다. 새페이지CSS나페이지번호selector는없다. root배치는정수12×6grid이므로그리드사이에있는source좌표와몇십px차이가날수있다. 이차이를요소CSS의페이지별보정으로감추지않았다. GAPS는unexpressible만담으며, 그표현을위한제안마크업은현재컬렉션에반입하지않았다.

Source base는agenda02,card03,hub04이다. sourcecover01/centerhead02/sidehead03는foundation이다. 346×152패널·53px순번(23px중첩)·32px이름·17pxcorner·3열2행,242×433field카드·220×68header·26px/750header·20px/700field·52px/800값·점선을측정했다. hub는367px중심원+17pxrim,60px/800단어,76px아이콘,40px/800주변제목,14pxnote다.

표지의128px/900/-8px제목,47px부제,오른쪽701px lockup과sidebar의60px두줄표제도foundation에서다시옮겼다. 47·26·13·9px처럼표에없는글자크기는허용type두끝사이clamp또는가장가까운type를쓴다. source색은cyan/blue라는물성이아닌a1/a2순위로만나눈다.

source03상단의blue label/value띠는card03의세로field모양과다르며해당semanticvariant가없어GAP이다. 가로띠를card의페이지특정variant로만들지않았다. 새조립에서는그자리를비워놓고주석과GAPS를연결한다.

실제로찾아고친것:순번원까지포함하도록agenda bbox를y272부터다시자름,field/agenda의700·750·800굵기를각역할토큰으로구분,core순번의a1/a2교대,cover아래8px두색stripe복구,chart/hierarchy/flow등새관계요소의자료의미와연결선,작은donut100%의단위가ring에걸림,작은겹침영역숫자의대비.

최종자동검수결과와파일/ZIP무결성은첨부audit JSON 및최상위delivery-validation.json에기록한다.


최종 통합 보완: 원본에 없는 fixture도 자료 의미를 검토했다. 사람 소개에는 실제 인명을, 의사결정에는 질문·조건·결론을, 표에는 수치와 단위가 일치하는 열 이름을 넣었다. headline의 무의미한 숫자 연결과 timeline의 역행 연도를 수정했고, bullet의 --v와 fig를 일치시켰다. 마크업과 멤버 수는 유지하되 matrix-nine의 생략된 축과 dumbbell의 두 시점 제목은 계약에 맞게 보완했다. fixture-editorial-pass.json에 해당 파일을 기록했다.

시각 검수에서 추가로 고친 것: 다섯·여섯 spoke가 있는 hub는 중앙 원을26%로 줄이고 위아래 spoke를18%의 띠에 두었다. core의 직접 icon은 원의55% 크기를 명시해 점으로 축소되지 않게 했다. 여덟 logo의12×3 칸에서 두 번째 행이 잘리던 문제는 멤버 수로 정한 행·열과 cqw/cqh 양축 상한으로 해결했다. quote의 avatar는 두 축을 같은 길이로 고정하고 인명 줄바꿈을 막았다. 이 변경은 source base의 자식 구조를 식별하는 규칙과 충돌하지 않는다.

표지는 README의 head/body 없는 .slide.cover 구조를 따른다. afterglow01처럼 상단 표제와 하단 본문이 함께 있는 intro는 일반 페이지 head와body로 표현했다. GAPS와 별개인 정수 grid의 근사 차이는 원본 bbox에 의한 배치에서 발생하며, 페이지번호 선택자나 CSS 회피 이동으로 보정하지 않았다.

Confluence에서 원본에 없는 요소는 source03의 inset 제목띠와 source04의 흰 medallion rim을 반복한다. 새 관계도·비교·축·그래프에도 같은 면/띠/원/선 비율을 적용해 Afterglow의 얇은 규칙선·밝은 역상 패널과 구분했다. 최종 card의 source03 field 구성은 유지하고, mark+name+note만 있는 필수 model은 아이콘 크기와 이름 시작선을 따로 검증했다.


## Hub native 행간 최종 교정 및 재검수

hub에서 원본과 달랐던 행간을 기존 공유 토큰의 비율로 교정했다: 주변 이름1.1, 주변 note1.35, 중심 이름1, 중심 note1.25. native1080×568에서 computed 행간은 주변 이름43.956≈44px, note18.954≈18.9px, 중심 이름59.94≈60px, 중심 note17.55≈17.5px이다. 글자 크기와 내용·도형은 바꾸지 않았다. 3개 base native 감사에서 글자 크기5% 초과 차이는0이다.

hub 라이트·다크 크기 시트10개 사례를 다시 렌더하고 모든 표시 칸을 직접 확인했다. 전체56요소1,100개 사례를 `--contrast --resume`으로 현재 SHA `507debc64f6b4fe9bc15c42dde136dd0b8f69323ea0646c8f353e2882a030296`에 맞춰 집계했으며 영역 초과·겹침·클립·폰트·숨김·0크기·실제 픽셀 대비 실패는 모두0이다. 활성 CSS와 fixture가 같은 캐시는 공용 동등성 증거로 재사용했다. 조립 본문을 보존하고 library.css만 갱신하여4페이지를 렌더했으며 전체3요소 source 대조와4개의 삼중 비교를 직접 확인했다. PNG1280×720/비교3840×720, 페이지 클립·사용 폰트 실패0이다. 의미적 GAPS는 변경하지 않았다. 수치와 최종 파일 검증은 `native-source-audit-final.json` 및 `native-fix-verification.json`에 남겼다.


## Agenda 설명 행간 최종 반영

추가 감사에서 남았던 agenda 설명 행간을 원본1.2배로 교정했다. 해당 element.css의 note 행간 선언 하나만 바꿨으며 다른 leaf·fixture·페이지 본문·replica는 보존했다. 원본13px/15.6px에 대해 native 요소13.104px/15.7248px로, 기존19.656px의 확대는 해소됐다.0.1248px는 기존 글자 크기 비율의 미세 차이이며 행간 배율은 원본과 같다.

agenda 라이트·다크 크기 시트18개 사례를 최종 재렌더하고 모든 표시 칸과 source 대조를 직접 확인했다. 전체1,100개 사례도 현재 SHA `5d96e21726cb5a414b4d5eeee7e93db8a5f66e8b4cda46f5328c0c20d39e2350`로 다시 집계해 영역 초과·겹침·클립·폰트·숨김·0크기·픽셀 대비 실패 모두0이다. library.css snapshot을 갱신하여4페이지와 전체3요소 source 대조를 재렌더했다.4개 삼중 비교를 직접 확인했고 페이지 클립·폰트 실패0, PNG1280×720/삼중3840×720이다. 현재 source/native/전체summary/reassembled/sourcecomparison SHA 일치와 HTML·fixture 해시 및112개 크기 시트PNG 무결성을 `native-fix-verification.json`으로 재확인했다. 의미적 GAPS는 변하지 않았다.
