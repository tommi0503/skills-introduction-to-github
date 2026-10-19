import {T,B,P,L,C,I,V,S,D} from '../primitives.mjs';
const bg='#fffef7',ink='#653000',muted='#71665c',line='#b9a78f',white='#fffef8';
const serif=(x,y,w,h,text,size=32,extra={})=>T(x,y,w,Math.max(h,size*1.56),text,size,{font:'Bodoni Moda',color:ink,lineHeight:1.08,weight:400,...extra});
const title=(x,y,w,h,text,size=68,extra={})=>serif(x,y+(size>40?6:0),w,h,text,size===68?65:size,{weight:900,...extra});
const body=(x,y,w,h,text,size=18,extra={})=>T(x,y,w,h,text,size,{font:'Pretendard',color:muted,weight:300,lineHeight:1.5,...extra});
const label=(text,x=67,y=73,w=350,extra={})=>title(x,y,w,45,text,30,extra);
const frame=(x,y,w,h)=>B(x,y,w,h,'transparent',{border:line,borderWidth:1});
const footer=(text)=>[L(54,654,483,0,'#9e988b',1),L(743,654,483,0,'#9e988b',1),body(543,638,194,35,text,22,{align:'center',color:ink})];
export default D('033','갈색 고급 겨울용품 홍보',[
 S('slide_01','Ordinary days',bg,[P(0,0,1280,720),title(140,69,1000,156,'Ordinary days',100,{align:'center'}),body(300,231,680,43,'평범한 하루에 오래 머무는 온도를 만듭니다.',27,{align:'center',color:ink}),...footer('BRAND PROFILE')]),
 S('slide_02','CONTENTS',bg,[title(66,72,594,94,'CONTENTS',68),P(66,189,594,363),serif(66,581,570,84,'Ordinary days,\nmade a little warmer.',30,{color:'#bfa477',lineHeight:1.22}),L(708,104,0,513,line,1),...[
  [139,'ABOUT',['01   Brand Story','02   Brand Philosophy','03   Brand Mood']],
  [324,'OBJECTS',['04   Product','05   Collection']],
  [459,'VALUE',['06   Our Values','07   For Whom','08   Brand Message']]
 ].flatMap(([y,s,items])=>[B(757,y,153,51,'transparent',{border:ink,borderWidth:0.6,radius:'50%'}),serif(762,y+9,143,36,s,27,{align:'center'}),...items.map((t,i)=>serif(933,y+8+i*51,320,45,t,29,{color:'#65564a'}))])]),
 S('slide_03','BRAND STORY',bg,[label('ABOUT'),P(636,67,281,407),P(932,67,281,407),body(911,493,302,27,'*페이지 내 인물 사진은 샘플이미지 입니다.',16,{align:'right'}),title(66,461,574,88,'BRAND STORY',68),body(67,559,1138,104,'우리가 만드는 건 향보다 오래 남는 순간입니다.\n빠르게 흘러가는 하루 속에서 잠시 머물 수 있는 시간을 만들고 싶었습니다.\n오후의 온도는 평범한 일상 속 작은 순간을 향과 오브제로 담아냅니다.',22,{lineHeight:1.44})]),
 S('slide_04','BRAND PHILOSOPHY',bg,[label('ABOUT'),title(66,119,527,171,'BRAND\nPHILOSOPHY',68,{lineHeight:1.14}),P(611,0,296,720),body(66,578,493,46,'우리의 기준은',28),serif(67,618,490,47,'Slowly, Simply, Naturally.',30,{color:'#65564a'}),L(910,240,367,0,line,1),L(910,479,367,0,line,1),...[
 ['SLOWLY','천천히 바라보고\n오래 사용할 수 있는 것을 만듭니다.',73,120],['SIMPLY','불필요한 것을 덜어내고\n본질에 집중합니다.',313,360],['NATURALLY','자연에서 얻은 영감과\n편안한 향을 담습니다.',553,600]
 ].flatMap(([h,t,y,ty])=>[serif(925,y,337,45,h,30,{align:'center'}),body(941,ty,307,71,t,18,{align:'center',lineHeight:1.35})])]),
 S('slide_05','BRAND MOOD',bg,[label('ABOUT'),title(613,71,600,106,'BRAND MOOD',68,{align:'right'}),...[
 [66,'Warm light','따뜻하게 번지는 오후의 빛'],[361,'Quiet space','소리가 잠시 멈춘 듯한 공간'],[656,'Natural texture','자연스러운 질감'],[950,'Slow moments','서두르지 않아도 괜찮은 시간']
 ].flatMap(([x,h,t])=>[P(x,202,263,315),frame(x,517,263,136),serif(x+13,533,244,49,h,30),body(x+13,616,236,26,t,17,{align:'right'})])]),
 S('slide_06','PRODUCT',bg,[label('OBJECTS'),title(66,119,559,93,'PRODUCT',68),frame(66,224,559,109),I(85,245,35,35,'FlaskRound',ink,{strokeWidth:0.8}),serif(126,244,474,42,'Afternoon',31),body(86,286,517,34,'하루 중 가장 좋아하는 오후 시간을 향으로 담았습니다.',18,{color:ink}),frame(66,349,559,305),L(345,374,0,255,line,1),L(89,501,513,0,line,1),...[
 [86,397,'Scent Notes','Fig · Cedarwood · Musk'],[365,397,'Mood','Warm · Soft · Woody'],[86,550,'Size | Price','180g · ₩38,000'],[365,550,'Burning Time','약 35시간']
 ].flatMap(([x,y,h,t])=>[serif(x,y,238,34,h,25,{align:'center'}),body(x,y+35,238,32,t,16,{align:'center'})]),P(655,67,558,357),P(655,441,271,213),P(943,441,270,213)]),
 S('slide_07','COLLECTION',bg,[label('OBJECTS'),label('ORDINARY DAYS',900,73,313,{align:'right',size:28}),title(290,119,700,94,'COLLECTION',68,{align:'center'}),B(66,227,1147,59,ink),...['제품','향','추천하는 순간'].map((t,i)=>body(66+i*382.33,240,382.33,35,t,22,{align:'center',color:white,weight:400})),...[
 ['Afternoon','Fig · Cedarwood · Musk','느긋한 오후'],['Linen','Cotton · Iris · Musk','깨끗한 아침'],['Forest','Pine · Sandalwood · Vetiver','깊은 밤'],['Rain','Green · Moss · Amber','비가 오는 날']
 ].flatMap((row,r)=>row.map((t,c)=>body(66+c*382.33,301+r*58.5,382.33,33,t,18,{align:'center',color:ink,weight:400}))),frame(66,227,1147,293),...Array.from({length:4},(_,i)=>L(66,286+i*58.5,1147,0,line,1)),L(448.33,227,0,293,line,1),L(830.67,227,0,293,line,1),frame(66,542,1147,111),serif(80,564,1119,43,'Morning · Afternoon · Night · Rainy Daym light',30,{align:'center'}),body(80,608,1119,30,'하루의 장면을 떠올리며, 가장 닮은 향을 골라보세요.',18,{align:'center'})]),
 S('slide_08','OUR VALUES',bg,[P(0,0,493,240),P(0,240,493,240),P(0,480,493,240),label('VALUE',557,73,660,{align:'center'}),title(557,127,660,94,'OUR VALUES',68,{align:'center'}),...[
 ['SLOWLY','쉽게 소비되고 버려지는 제품보다 일상에 오래 남을 수 있는 제품을 만듭니다.',264],['SUBTLE','공간을 가득 채우기보다 곁에 은은하게 머무는 향을 추구합니다.',404],['TIMELESS','유행을 좇기보다 시간이 지나도 자연스러운 디자인을 생각합니다.',543]
 ].flatMap(([h,t,y],i)=>[frame(557,y,660,111),serif(577,y+23,620,42,h,30,{align:'center'}),body(580,y+65,614,31,t,18,{align:'center'}),...(i<2?[L(887,y+111,0,29,line,1)]:[])])]),
 S('slide_09','FOR WHOM',bg,[P(0,0,640,720),label('VALUE',707),title(706,119,507,95,'FOR WHOM',68),L(707,211,0,136,line,1),...[
 ['01  SLOW LIVING','바쁜 일상 속에서도 나만의 속도를 지키고 싶은 사람 작은 여유와 혼자만의 시간을\n중요하게 생각합니다.',364],['02  SENSIBLE TASTE','향, 음악, 공간처럼 일상의 작은 취향을 소중히 여기는 사람 유행보다 자신에게 잘\n맞는 것을 오래 선택합니다.',470],['03  QUIET MOMENTS','평범한 하루 속에서 특별한 순간을 발견하는 사람 조용한 공간과 은은한 향으로 자\n신만의 분위기를 만듭니다.',575]
 ].flatMap(([h,t,y])=>[serif(706,y,507,39,h,24),body(706,y+35,507,63,t,15,{lineHeight:1.52})])]),
 S('slide_10','BRAND MESSAGE',bg,[P(0,0,1280,217),label('VALUE'),label('ORDINARY DAYS',900,73,313,{align:'right',size:28}),title(241,311,798,92,'BRAND MESSAGE',68,{align:'center'}),body(340,403,600,47,'우리가 전하고 싶은 것',28,{align:'center',weight:500,color:ink}),body(385,460,510,183,'오후의 온도는\n특별한 날을 위한 향보다\n평범한 하루를 위한 향을 만듭니다.\n\n아침의 첫 커피부터\n하루를 마무리하는 늦은 밤까지.\n당신의 일상에 작은 온도를 더합니다.',18,{align:'center',lineHeight:1.4}),V(66,284,88,108,'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 88 108"><path d="M4 103V21Q4 5 20 5H80" fill="none" stroke="#653000"/><circle cx="4" cy="103" r="4" fill="#653000"/><path d="M80 0L86 5L80 11L74 5Z" fill="#653000"/></svg>'),V(1127,545,88,108,'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 88 108"><path d="M83 5V87Q83 103 67 103H7" fill="none" stroke="#653000"/><circle cx="83" cy="5" r="4" fill="#653000"/><path d="M7 97L13 103L7 109L1 103Z" fill="#653000"/></svg>')]),
 S('slide_11','AFTERNOON AT YOUR OWN PACE',bg,[P(0,0,1280,720),title(45,60,1190,104,'AFTERNOON AT YOUR OWN PACE.',67,{align:'center',letterSpacing:-1.9}),...footer('THANK YOU')])
]);
