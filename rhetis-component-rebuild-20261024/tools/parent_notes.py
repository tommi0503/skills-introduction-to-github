from pathlib import Path
import json
B=Path('/workspace/work/rebuild-20261024')
shared='''기존 replica의 HTML/CSS/PNG/PDF는 수정하지 않았다. replica-freeze.json의191개 SHA-256과최종파일을대조한다. 기존 element.css는 읽어고쳐쓰지않았으며, 새 생성기는 replica의수치와계약fixture마크업만자료로읽는다. old/new CSS의byte비교는재작성여부검증용이다.

픽셀의색은검수호스트 source-palette.json에만있고 컬렉션CSS는팔레트자리만사용한다. 라이브러리light/dark는수정하지않은reference palette로검수한다. 원본팔레트의낮은텍스트대비를라이브러리로옮기지않았다.

모범구성마크업·숫자데이터는원본과같다. 단, card-2-quiet의“기록과 지표가 한곳에 모여 바로 결정할 수 있습니다.”는원본덱문구와6자겹침이있어 “기록과 지표가 한곳에 모여 바로 결정을 내립니다.”로한문장만바꿨다. 새사용자요청의문구복제금지가README의문구유지보다우선한다. validator는이정확한한문장외차이를허용하지않는다.

fixture는모양·멤버수·문장길이를따라새한국어업무내용을썼다. 6자검사는여섯replica전체에대한NFKC/소문자/공백·문장부호제거후텍스트노드내연속6자대조다. 단순히회사명만바꾸지않았다. 코드fixture는실행가능한SQL/Python문장과새한국어주석으로썼다.

검수이미지는1280×720브라우저에서그린다. 시트는요청된9종크기중min의두축이상인크기와min을모두포함한다. root가스스로줄어들어도배정grid칸전체+6px를잘라기록한다. 원본대조는map.bbox의frozen replica조각과source-palette12×6/min을나란히보인다. 최종조립비교는원본|frozen replica|새조립순서의3840×720이다.

자동검사는텍스트범위의밖으로나감·겹침·clip조상·font error·숨긴name/fig·0크기root·chip기하중심을보존한다. 실제글자위치와글자를숨긴두번째스크린샷으로대비를계산한다. 단순조상배경/gradient최악stop방식의rawContrast도삭제하지않고오탐근거를구분한다. 작은숫자면의대비가공급palette에서부족할때는page/ink숫자판으로보장한다. chip은추가로렌더된ink의상하·좌우중심도기록한다.

연결도는요소가선을그린다. 행사의무관한장식을이웃card유무로만들지않는다. flowchart/swimlane의방향flag는인접grid칸으로연결한다. 마지막node의to-u도그위칸으로돌아가며DOM다음node를추측하지않는다. decision모양은.name면만마름모로잘라연결화살표를자르지않는다. 조직도선은마지막자식의중심에서끝난다. 누적면적의--v는계약대로누적값이고역순z-order로올바른층을보인다.

새조립에는계약class/data-el과foundation만있다. 새페이지CSS나페이지번호selector는없다. root배치는정수12×6grid이므로그리드사이에있는source좌표와몇십px차이가날수있다. 이차이를요소CSS의페이지별보정으로감추지않았다. GAPS는unexpressible만담으며, 그표현을위한제안마크업은현재컬렉션에반입하지않았다.
'''
extra={
'afterglow':'''Source base는agenda02,headline04,list04,card05,area06,tag07,image-frame04,prose08,steps08이다. quiet/lead/center/check같이의미가맞는계약변형만썼다. source07의작은quiet문자는실제폭에비례해14px근처로,source01의넓은quiet문자는16px근처로달라진다.

읽은수치:frame(27,27)/1226×666/16px,top17px·32px,headline21/32px,line1.35,card280×376/14pxgap/260×212그림,step140px/13pxgap/82px아이콘/33px연결원. 원본16px본문은Freesentation,표제·기타는Pretendard Variable로분리한다.

source09의16px가운데본문을28px의prose.lead로잘못대응시킨초안을철회했다. prose에는center변형이없으므로map에unexpressible로기록하고조립에서빼두었다. footer문의는foundation metadata다. source03의176px와source06의140px는type128상한을고정glyph배율로우회하지않았다.

실제로찾아고친것:line플롯에서padding을두번뺀음수높이,0×0dot의사각shadow,영역면의다른series가림,32pxmark에40px숫자가들어가optical center가7px내려가던문제,stack의flex로늘어난tag,본문headline의size containment높이0,역상흰패널안nestedlist/code의대비,배경glow위axis글자의대비,calendar셀이직사각으로늘어남,forward anchor로사라진flow화살표,마름모모양에잘린화살표,끝아래까지남은org선.
''',
'confluence':'''Source base는agenda02,card03,hub04이다. sourcecover01/centerhead02/sidehead03는foundation이다. 346×152패널·53px순번(23px중첩)·32px이름·17pxcorner·3열2행,242×433field카드·220×68header·26px/750header·20px/700field·52px/800값·점선을측정했다. hub는367px중심원+17pxrim,60px/800단어,76px아이콘,40px/800주변제목,14pxnote다.

표지의128px/900/-8px제목,47px부제,오른쪽701px lockup과sidebar의60px두줄표제도foundation에서다시옮겼다. 47·26·13·9px처럼표에없는글자크기는허용type두끝사이clamp또는가장가까운type를쓴다. source색은cyan/blue라는물성이아닌a1/a2순위로만나눈다.

source03상단의blue label/value띠는card03의세로field모양과다르며해당semanticvariant가없어GAP이다. 가로띠를card의페이지특정variant로만들지않았다. 새조립에서는그자리를비워놓고주석과GAPS를연결한다.

실제로찾아고친것:순번원까지포함하도록agenda bbox를y272부터다시자름,field/agenda의700·750·800굵기를각역할토큰으로구분,core순번의a1/a2교대,cover아래8px두색stripe복구,chart/hierarchy/flow등새관계요소의자료의미와연결선,작은donut100%의단위가ring에걸림,작은겹침영역숫자의대비.
'''}
for n in extra:
 r=B/n/'review';(r/'review-notes.md').write_text('# Review notes\n\n'+shared+'\n'+extra[n]+'\n최종자동검수결과와파일/ZIP무결성은첨부audit JSON 및최상위delivery-validation.json에기록한다.\n')
 d=json.loads((r/'map.json').read_text());base=[x for x in d['instances']if x['use']=='base'];text='# Design language\n\n'
 text+=('바깥면·둥근프레임·가느다란상단세칸·한순위강조와반대면카드가대조된다. 1px선,16pxcorner/8px내부corner,8/16/32px여백,32px두줄표제,작은영문kick와18pxcard이름의위계를쓴다.\n\n'if n=='afterglow'else'17px흰면패널과안쪽강조header,원형번호medallion,중앙의두꺼운ring과얇은십자축을쓴다. 1px선,8px내부corner,10/20/40px여백,800굵기의중심단어와700/750굵기의field·라벨을구분한다.\n\n')
 text+='색의역할은덱전체에서한번정한다.\n\n'+'\n'.join('- '+k+' = `'+v+'`'for k,v in d['roles'].items())+'\n\nSource base:\n\n'+'\n'.join('- `'+x['leaf']+'` → '+x['page']+': '+x['design']for x in base)+'\n'
 (r/'design-language.md').write_text(text)
print('parent notes and design language written')
