# Review notes

기존 replica의 HTML/CSS/PNG/PDF는 수정하지 않았다. replica-freeze.json의191개 SHA-256과최종파일을대조한다. 기존 element.css는 읽어고쳐쓰지않았으며, 새 생성기는 replica의수치와계약fixture마크업만자료로읽는다. old/new CSS의byte비교는재작성여부검증용이다.

픽셀의색은검수호스트 source-palette.json에만있고 컬렉션CSS는팔레트자리만사용한다. 라이브러리light/dark는수정하지않은reference palette로검수한다. 원본팔레트의낮은텍스트대비를라이브러리로옮기지않았다.

모범구성마크업·숫자데이터는원본과같다. 단, card-2-quiet의“기록과 지표가 한곳에 모여 바로 결정할 수 있습니다.”는원본덱문구와6자겹침이있어 “기록과 지표가 한곳에 모여 바로 결정을 내립니다.”로한문장만바꿨다. 새사용자요청의문구복제금지가README의문구유지보다우선한다. validator는이정확한한문장외차이를허용하지않는다.

fixture는모양·멤버수·문장길이를따라새한국어업무내용을썼다. 6자검사는여섯replica전체에대한NFKC/소문자/공백·문장부호제거후텍스트노드내연속6자대조다. 단순히회사명만바꾸지않았다. 코드fixture는실행가능한SQL/Python문장과새한국어주석으로썼다.

검수이미지는1280×720브라우저에서그린다. 시트는요청된9종크기중min의두축이상인크기와min을모두포함한다. root가스스로줄어들어도배정grid칸전체+6px를잘라기록한다. 원본대조는map.bbox의frozen replica조각과source-palette12×6/min을나란히보인다. 최종조립비교는원본|frozen replica|새조립순서의3840×720이다.

자동검사는텍스트범위의밖으로나감·겹침·clip조상·font error·숨긴name/fig·0크기root·chip기하중심을보존한다. 실제글자위치와글자를숨긴두번째스크린샷으로대비를계산한다. 단순조상배경/gradient최악stop방식의rawContrast도삭제하지않고오탐근거를구분한다. 작은숫자면의대비가공급palette에서부족할때는page/ink숫자판으로보장한다. chip은추가로렌더된ink의상하·좌우중심도기록한다.

연결도는요소가선을그린다. 행사의무관한장식을이웃card유무로만들지않는다. flowchart/swimlane의방향flag는인접grid칸으로연결한다. 마지막node의to-u도그위칸으로돌아가며DOM다음node를추측하지않는다. decision모양은.name면만마름모로잘라연결화살표를자르지않는다. 조직도선은마지막자식의중심에서끝난다. 누적면적의--v는계약대로누적값이고역순z-order로올바른층을보인다.

새조립에는계약class/data-el과foundation만있다. 새페이지CSS나페이지번호selector는없다. root배치는정수12×6grid이므로그리드사이에있는source좌표와몇십px차이가날수있다. 이차이를요소CSS의페이지별보정으로감추지않았다. GAPS는unexpressible만담으며, 그표현을위한제안마크업은현재컬렉션에반입하지않았다.

Source base는agenda02,headline04,list04,card05,area06,tag07,image-frame04,prose08,steps08이다. quiet/lead/center/check같이의미가맞는계약변형만썼다. source07의작은quiet문자는실제폭에비례해14px근처로,source01의넓은quiet문자는16px근처로달라진다.

읽은수치:frame(27,27)/1226×666/16px,top17px·32px,headline21/32px,line1.35,card280×376/14pxgap/260×212그림,step140px/13pxgap/82px아이콘/33px연결원. 원본16px본문은Freesentation,표제·기타는Pretendard Variable로분리한다.

source09의16px가운데본문을28px의prose.lead로잘못대응시킨초안을철회했다. prose에는center변형이없으므로map에unexpressible로기록하고조립에서빼두었다. footer문의는foundation metadata다. source03의176px와source06의140px는type128상한을고정glyph배율로우회하지않았다.

실제로찾아고친것:line플롯에서padding을두번뺀음수높이,0×0dot의사각shadow,영역면의다른series가림,32pxmark에40px숫자가들어가optical center가7px내려가던문제,stack의flex로늘어난tag,본문headline의size containment높이0,역상흰패널안nestedlist/code의대비,배경glow위axis글자의대비,calendar셀이직사각으로늘어남,forward anchor로사라진flow화살표,마름모모양에잘린화살표,끝아래까지남은org선.

최종자동검수결과와파일/ZIP무결성은첨부audit JSON 및최상위delivery-validation.json에기록한다.


최종 통합 보완: 원본에 없는 fixture도 자료 의미를 검토했다. 사람 소개에는 실제 인명을, 의사결정에는 질문·조건·결론을, 표에는 수치와 단위가 일치하는 열 이름을 넣었다. headline의 무의미한 숫자 연결과 timeline의 역행 연도를 수정했고, bullet의 --v와 fig를 일치시켰다. 마크업과 멤버 수는 유지하되 matrix-nine의 생략된 축과 dumbbell의 두 시점 제목은 계약에 맞게 보완했다. fixture-editorial-pass.json에 해당 파일을 기록했다.

시각 검수에서 추가로 고친 것: 다섯·여섯 spoke가 있는 hub는 중앙 원을26%로 줄이고 위아래 spoke를18%의 띠에 두었다. core의 직접 icon은 원의55% 크기를 명시해 점으로 축소되지 않게 했다. 여덟 logo의12×3 칸에서 두 번째 행이 잘리던 문제는 멤버 수로 정한 행·열과 cqw/cqh 양축 상한으로 해결했다. quote의 avatar는 두 축을 같은 길이로 고정하고 인명 줄바꿈을 막았다. 이 변경은 source base의 자식 구조를 식별하는 규칙과 충돌하지 않는다.

표지는 README의 head/body 없는 .slide.cover 구조를 따른다. afterglow01처럼 상단 표제와 하단 본문이 함께 있는 intro는 일반 페이지 head와body로 표현했다. GAPS와 별개인 정수 grid의 근사 차이는 원본 bbox에 의한 배치에서 발생하며, 페이지번호 선택자나 CSS 회피 이동으로 보정하지 않았다.


## Native bbox 최종 교정 및 재검수

source-native 진단에서 발견한 headline21→14/32→24px, list18→14/16→12px 축소를 요소 CSS의 root 폭 비율로 바로잡았다. mark가 있는 list의 원본38px 텍스트 gutter는 item이 소유하며 불필요한 root inset을 제거했다. agenda의 내용 길이에 따라 줄던 괘선은 native100px 폭을 명시했고 원160×160, 이름25px/설명16px를 유지한다. steps는 원본667×140 패널 세 개/13px 간격과82px 아이콘을 복구했다. 원본bbox446px에서 padding 때문에 compact 분기가 켜지던 문제를 없애 설명16px가 보이게 했다. 아이콘에는 enclosing 배지 원이 없으므로 mark 안의 Lucide placement 자체가82px를 채운다. 작은 칸의 compact 분기는350px 이하에서 유지한다.

수정 후 원본 bbox에서 Afterglow9개 base를 다시 측정해 글자 크기5% 초과 차이0을 확인했다. headline20.9999/31.9992, list18/16, agenda25/16px·괘선100px·원160px, steps18/16px·아이콘82×82·패널667×140이다. 기존 prose 시각16.92→16.2324px(4.06%) 및 미세 반올림은 이번 지정 범위에서 변경하지 않았다. fixture·페이지 본문·replica는 바꾸지 않았다.

변경4요소 라이트·다크 크기 시트136개 사례를 모두 다시 렌더하고 표시된 모든 칸을 직접 확인했다. 전체56요소1,270개 사례를 `--contrast --resume`으로 현재 SHA `adc6a69d34f2e6677a5907fbdc69d50994b2208ed77182e723ebe6b6701cd86c`에 맞춰 집계했으며 영역 초과·겹침·클립·폰트·숨김·0크기·실제 픽셀 대비 실패는 모두0이다. 활성 CSS와 fixture가 동일한 캐시는 공용 동등성 증거로 재사용했고, 중첩 list에 영향을 받는 pricing/versus 등도 재검사했다.

조립 HTML 본문은 보존하고 library.css만 갱신하여9페이지를 최종 렌더했다. 전체9요소 source 대조와9개의 원본|replica|조립본 삼중 비교를 직접 확인했다. 조립 PNG1280×720/비교3840×720, 페이지 클립·사용 폰트 실패0이다. 기존 의미적 GAPS 및 정수 그리드 차이는 그대로 남고 새 GAPS는 추가하지 않았다. `native-source-audit-final.json`에 수치, `native-fix-verification.json`에 최종 SHA·해시·PNG 검증을 기록했다.
