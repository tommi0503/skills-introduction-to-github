import type {SidePatch,Region} from '../model'
import {T,C,B,L,IC,P} from '../primitives'
const R=(x:number,y:number,w:number,h:number):Region=>({x,y,w,h})
const img=(x:number,y:number,w:number,h:number,dropText=true,radius?:number|string)=>({x,y,w,h,dropText,radius})
const heading=(x:number,y:number,w:number,h:number,text:string,size:number,color='#111',font='Pretendard')=>T(x,y,w,h,text,size,{weight:700,color,font,align:'center',lineHeight:1.1})
const p:Record<string,SidePatch>={
'l49/s01':{background:'#efefef',defaultFont:'Pretendard',images:[img(53,180,68,69),img(53,283,68,69),img(53,384,68,69),img(53,487,68,69),img(53,590,68,69),img(494,191,69,69),img(600,191,69,69),img(707,191,69,69),img(589,585,102,103),img(870,459,392,179),img(870,642,195,180),img(1068,642,193,180),img(624,762,31,26),img(1212,834,31,24)],removeText:[R(895,81,341,221)],elements:[C(897,81,338,108,'스마트팜',64,'#fff',{border:'1px solid #111',radius:70,weight:700}),C(898,187,337,110,'완전정복',63,'#ffe349',{border:'1px solid #111',radius:70,weight:700})],textStyles:[{...R(0,0,850,80),weight:700,font:'Do Hyeon'},{...R(0,106,850,45),weight:700}]},
'l49/s02':{background:'#efefef',defaultFont:'Pretendard',images:[img(48,185,340,177),img(48,524,340,177),img(65,420,83,66),img(62,778,83,53),img(470,185,340,85),img(470,353,340,86),img(470,520,340,86),img(470,688,340,86),img(1115,185,116,118),img(1080,246,67,68),img(1115,374,116,117),img(1080,435,67,67),img(1115,564,116,117),img(1080,625,67,68),img(900,756,41,81)],textStyles:[{...R(0,0,1280,85),font:'Do Hyeon',weight:700},{...R(0,105,1280,47),weight:700}]},
'l50/s01':{background:'#f5ffe5',defaultFont:'Jua',images:[img(64,237,100,160),img(252,265,114,132),img(53,600,131,160),img(268,603,96,157),img(493,343,270,303),img(480,770,84,85),img(878,449,373,378)],textStyles:[{...R(0,0,427,149),size:40,weight:400},{...R(870,76,395,266),size:69,weight:400},{...R(458,782,363,79),font:'Montserrat',size:14}],notes:['Custom vegetable mascots and cover greenhouse scene replaced by bounded flat gray areas.']},
'l50/s02':{background:'#f5ffe5',defaultFont:'Jua',images:[img(70,292,287,138),img(70,589,287,136),img(489,351,126,83),img(500,546,110,80),img(500,744,110,87),img(953,596,252,157)],textStyles:[{...R(0,36,1280,111),size:39,weight:400},{...R(67,472,291,81),font:'Pretendard',size:15},{...R(67,775,291,79),font:'Pretendard',size:15},{...R(618,346,190,491),font:'Pretendard',size:14}],elements:[IC(905,202,33,33,'Headset','#fff'),IC(905,285,33,33,'MessageCircle','#fff'),IC(905,369,33,33,'BadgeCheck','#fff'),IC(905,452,33,33,'Megaphone','#fff'),IC(905,535,33,33,'FileText','#fff')]},
'l51/s01':{background:'#16112a',defaultFont:'Noto Serif KR',images:[img(138,47,174,196),img(874,0,406,245),img(874,651,166,258)],textStyles:[{...R(852,130,426,400),color:'#fff'},{...R(0,0,1280,909),font:'Noto Serif KR'}],notes:['Piano photographic and textured cover background are gray; recital titles remain actual text.']},
'l51/s02':{background:'#e5e5e5',defaultFont:'Noto Serif KR',images:[img(104,264,98,113),img(270,264,104,113),img(104,561,98,111),img(270,561,95,111),img(561,414,162,147)],elements:[B(55,53,1170,803,'#fff'),B(445,53,382,803,'#f0f0f0')],notes:['Content card background manual restoration required before baseline text (renderer layering noted).']},
'l52/s01':{background:'#f8edda',defaultFont:'Noto Serif KR',images:[img(0,0,426,909,false),img(589,198,101,100),img(850,365,430,488),img(1040,26,48,49)],removeShapes:[R(0,0,426,909)],textStyles:[{...R(0,0,427,909),color:'#fff'},{...R(854,0,426,363),color:'#65421e'}],notes:['Patterned paper and decorative illustrated packaging are gray; actual text and geometric frames retained.']},
'l52/s02':{background:'#f9f0df',defaultFont:'Noto Serif KR',images:[img(89,200,250,249),img(484,154,166,156),img(484,398,166,138),img(484,640,170,139),img(854,0,426,200)],textStyles:[{...R(0,0,1280,909),color:'#795634'},{...R(439,82,402,82),size:32,weight:700}]},
'l53/s01':{background:'#f3f4dc',defaultFont:'Pretendard',images:[img(55,162,319,162),img(55,546,319,162),img(883,0,368,535)],textStyles:[{...R(0,0,854,92),weight:400,size:24},{...R(870,637,388,130),color:'#a5c653',size:49,weight:500}],notes:['Cover robot photograph follows large notched region with gray placeholder.']},
'l53/s02':{background:'#f3f4dc',defaultFont:'Pretendard',images:[img(0,0,823,325),img(480,445,118,119),img(480,591,118,119),img(480,738,118,117)],textStyles:[{...R(0,334,854,70),weight:700},{...R(865,0,398,79),weight:700}]},
'l54/s01':{background:'#fff',defaultFont:'Pretendard',images:[img(48,211,332,211),img(48,570,334,210),img(427,624,427,285),img(854,374,426,464),img(478,358,61,61),img(605,358,61,61),img(733,358,61,61)],textStyles:[{...R(0,42,426,85),font:'Montserrat',weight:600},{...R(867,40,401,179),font:'Montserrat',weight:800},{...R(445,30,383,340),weight:600}],notes:['Farm, farmer and architectural drawings gray; mint central panel and English type remain.']},
'l54/s02':{background:'#fff',defaultFont:'Pretendard',images:[img(44,238,92,91),img(44,414,92,91),img(44,582,92,91),img(44,750,92,91),img(465,217,159,198),img(465,435,159,196),img(465,650,159,204),img(1130,698,118,86)],textStyles:[{...R(0,38,1280,100),font:'Montserrat',weight:600}]},
'l55/s01':{background:'#fff342',defaultFont:'Do Hyeon',images:[img(101,174,216,122),img(501,797,72,72),img(941,531,291,298)],textStyles:[{...R(20,336,399,529),font:'Pretendard'},{...R(471,231,339,479),font:'Pretendard'},{...R(870,70,391,340),font:'Do Hyeon',weight:400}],notes:['Cover elderly characters and application illustration are gray; contact map roads remain editable geometry.']},
'l55/s02':{background:'#f3f3f3',defaultFont:'Pretendard',images:[img(505,26,283,151)],textStyles:[{...R(0,0,630,177),font:'Do Hyeon',weight:400},{...R(853,0,426,180),font:'Do Hyeon',weight:400}],notes:['Education schedules and registration tables retained as actual text and source-aligned solid cells.']},
'l56/s01':{background:'#ffd277',defaultFont:'Pretendard',images:[img(49,142,326,181),img(854,0,426,909,false),img(498,670,84,84)],textStyles:[{...R(0,12,1280,122),font:'Lilita One',weight:400},{...R(470,161,354,153),font:'Lilita One'},{...R(854,60,426,290),font:'Lilita One'}],notes:['Festival decorative illustration/background gray, simple schedule, road map and color chips retained.']},
'l56/s02':{background:'#ffd277',defaultFont:'Pretendard',images:[img(37,142,101,101,true,"50%"),img(164,142,101,101,true,"50%"),img(291,142,101,101,true,"50%"),img(37,311,101,101,true,"50%"),img(164,311,101,101,true,"50%"),img(291,311,101,101,true,"50%"),img(475,193,149,100),img(652,193,149,100),img(475,345,149,101),img(652,345,149,101),img(475,578,149,100),img(652,578,149,100),img(475,730,149,100),img(652,730,149,100),img(902,133,80,72),img(902,230,80,72),img(902,328,80,72),img(902,425,80,72),img(887,598,98,245),img(1012,598,98,245),img(1138,598,99,245)],textStyles:[{...R(0,17,1280,113),font:'Lilita One',weight:400},{...R(0,542,420,69),font:'Lilita One'}]},
'l57/s01':{background:'#f0f3f5',defaultFont:'Pretendard',images:[img(276,146,106,106,true,"50%"),img(276,371,106,106,true,"50%"),img(293,577,72,72),img(899,169,340,309)],textStyles:[{...R(0,18,1280,155),font:'Do Hyeon',weight:400},{...R(870,500,390,265),font:'Black Han Sans',weight:400},{...R(0,171,425,650),weight:500}],notes:['Elderly characters and QR codes gray; contact details, road map and speech-pill geometry retained.']},
'l57/s02':{background:'#eef6fc',defaultFont:'Pretendard',images:[img(55,746,237,163),img(483,164,107,107,true,"50%"),img(483,535,107,107,true,"50%")],textStyles:[{...R(10,28,396,213),font:'Black Han Sans',weight:400},{...R(445,50,378,75),font:'Do Hyeon',weight:400},{...R(870,28,390,95),font:'Do Hyeon',weight:400}]},
'l58/s01':{background:'#fff',defaultFont:'Pretendard',images:[img(750,808,64,63),img(895,262,348,501),img(1176,807,66,66)],textStyles:[{...R(33,52,374,125),weight:700},{...R(446,46,378,112),weight:700},{...R(854,30,426,177),font:'Montserrat',weight:400}]},
'l58/s02':{background:'#fff',defaultFont:'Pretendard',images:[img(31,240,365,190),img(31,445,365,248),img(455,449,370,130),img(455,596,370,130),img(455,743,370,129),img(854,0,426,430)],textStyles:[{...R(30,26,390,150),font:'Montserrat',weight:800},{...R(440,25,388,97),font:'Montserrat',weight:800},{...R(870,490,390,99),font:'Montserrat',weight:800}]},
'l59/s01':{background:'#1db5b1',defaultFont:'Pretendard',images:[img(47,132,363,188),img(850,520,430,389)],textStyles:[{...R(0,0,1280,136),font:'Do Hyeon',weight:400},{...R(867,184,400,185),font:'Do Hyeon',weight:400}],notes:['Caregiver cover image gray; contact map and outlined house geometry retained.']},
'l59/s02':{background:'#1db5b1',defaultFont:'Pretendard',images:[img(0,0,426,202,false),img(471,282,352,141),img(471,472,352,140),img(854,687,426,222,false)],textStyles:[{...R(0,20,1280,113),font:'Do Hyeon',weight:400}]},
'l60/s01':{background:'#ffd346',defaultFont:'Pretendard',images:[img(55,176,347,144),img(55,403,347,145),img(55,632,347,143),img(620,308,43,49),img(899,543,325,267),img(54,102,78,73)],textStyles:[{...R(0,13,426,75),font:'Do Hyeon',weight:400},{...R(870,76,389,265),font:'Do Hyeon',weight:400},{...R(440,370,389,145),font:'Do Hyeon',weight:400}]},
'l60/s02':{background:'#fff',defaultFont:'Pretendard',images:[img(0,572,1280,337,false),img(62,292,151,100),img(62,444,151,100),img(62,596,151,100),img(62,747,151,100),img(468,274,153,153,true,"50%"),img(661,274,151,153,true,"50%"),img(468,572,153,153,true,"50%"),img(661,572,151,153,true,"50%"),img(909,329,64,74),img(902,509,80,59),img(903,678,81,78),img(885,797,54,55),img(1001,797,54,55),img(1114,797,54,55)],textStyles:[{...R(0,28,1280,97),font:'Do Hyeon',weight:400}],notes:['Right-panel decorative photographic background gray with actual white support cards preserved.']}
}
export default p
// Explicit copy and centered chips where OCR splits glyphs or omits colored headings.
const add=(key:string,e:ReturnType<typeof T>[],remove:Region[]=[])=>{p[key].elements=[...(p[key].elements??[]),...e];p[key].removeText=[...(p[key].removeText??[]),...remove]}
const text=(x:number,y:number,w:number,h:number,t:string,size=15,color='#111',weight=400)=>T(x,y,w,h,t,size,{color,weight,lineHeight:1.35})
const green='#3da775'
add('l49/s01',[
 C(74,41,35,35,'4',20,green,{color:'#111',border:'1px solid #111',radius:'50%'}),text(121,43,291,37,'어떻게 진행되나요?',29,'#111',700),
 C(534,41,35,35,'5',20,green,{color:'#111',border:'1px solid #111',radius:'50%'}),text(579,43,241,37,'상담 신청 안내',29,'#111',700),
 C(21,106,395,44,'컨설팅 진행 절차',21,'#ffe349',{radius:0,color:'#111'}),C(442,106,395,44,'상담 가능 분야',21,'#ffe349',{radius:0}),C(442,350,395,45,'상담 신청 및 문의 안내',21,green,{radius:0}),C(21,695,395,45,'기대 효과',21,green,{radius:0}),
 ...['상담 신청','사전 확인','맞춤 분석','컨설팅 진행','적용 점검'].flatMap((t,i)=>[text(137,188+i*102,60,27,`${i+1}단계`,18,green,700),text(200,188+i*102,186,27,t,18,'#111',700),text(137,219+i*102,246,47,['기본 정보와 농장 현황 접수','작물, 시설, 운영 방식 점검','농장 조건에 맞는 기술 방향 정리','현장 또는 비대면 방식으로 솔루션 안내','실행 가능한 항목부터 적용 후\n보완 포인트 확인'][i],15)]),
 ...['스마트팜\n도입 상담','친환경 농업\n운영 상담','청년 농업인\n맞춤 컨설팅 상담'].map((t,i)=>T(483+i*106,273,92,41,t,15,{align:'center',lineHeight:1.4})),
 ...['기관명','대표번호','이메일','홈페이지'].flatMap((t,i)=>[C(476,427+i*33,105,28,t,15,'#efefef',{border:'0.5px solid #666',radius:20}),text(591,432+i*33,228,25,['미리스마트농업연구소','00-123-4567','smartfarm@miriagri.co.kr','www.mirismartagri.co.kr'][i],15)]),
 heading(1010,327,119,24,'2059 VER.',23),heading(905,357,322,25,'스마트팜·친환경 농업 기술 컨설팅 프로그램',16),heading(570,697,145,20,'온라인 문의 및 상담',14),
 ...['농장 운영 방향이 더 명확해집니다','기술 도입 우선순위를 정리할 수 있습니다','친환경·스마트농업 운영 이해도를 높일 수 있습니다'].flatMap((t,i)=>[IC(44,767+i*28,19,19,'SquareCheck','#111'),text(70,769+i*28,330,23,t,14)]),
 heading(478,800,327,45,'농장에 맞는 기술 도입 방향이 궁금하다면\n지금 상담으로 먼저 확인해보세요.',17)
],[R(0,0,850,80),R(21,106,816,45),R(137,184,251,505),R(483,270,337,48),R(442,350,395,45),R(476,420,343,141),R(21,695,395,45),R(43,763,358,100),R(479,694,334,36),R(479,792,334,64),R(905,318,322,64)]);
add('l49/s02',[
 ...['어떤 컨설팅을 하나요?','이런 분께 추천합니다','컨설팅 프로그램 안내'].flatMap((t,i)=>[C(31+i*423,41,35,35,String(i+1),20,green,{radius:'50%',border:'1px solid #111'}),text(78+i*423,43,340,39,t,28,'#111',700)]),
 ...['주요 컨설팅 분야','추천 대상','프로그램 구성'].map((t,i)=>C(21+i*423,106,395,45,t,21,'#fff',{radius:0})),
 text(48,380,350,27,'1. 스마트팜 기술 컨설팅',20,green,600),text(169,417,225,78,'• 온습도·환기·관수 환경 제어 안내\n• 센서 기반 재배 관리 방향 제안\n• 작물별 운영 데이터 점검',15),
 text(48,721,350,27,'2. 친환경 농업 컨설팅',20,green,600),text(169,755,226,77,'• 친환경 재배 운영 방향 상담\n• 토양·급수·관리 체계 점검\n• 지속가능 재배 방식 제안',15),
 ...['스마트팜 도입을 처음 검토하는 농업인','친환경 재배로 전환을 고민하는 농가','청년 농부·귀농 준비자','기존 농장 운영을 개선하고 싶은 농장주'].flatMap((t,i)=>[text(470,286+i*168,346,28,`• ${t}`,18,green,600),text(470,315+i*168,346,28,['어떤 설비부터 시작해야 할지 막막한 경우','운영 기준과 적용 방법이 필요한 경우','기술 기반 농업 운영 방향을 배우고 싶은 경우','현재 시설과 재배를 점검하고 싶은 경우'][i],15)]),
 ...['A. 기초 진단 컨설팅','B. 맞춤 설계 컨설팅','C. 현장 적용 컨설팅'].flatMap((t,i)=>[text(902,188+i*190,210,28,t,19,green,600),text(902,223+i*190,202,83,['• 농장 현황 파악\n• 시설·재배 환경 점검\n• 현재 운영 문제점 정리','• 작물 및 운영 형태별 기술 제안\n• 도입 우선순위 설계\n• 재배·운영 방향 정리','• 기술 적용 체크\n• 운영 중 보완 포인트 안내\n• 실무형 피드백 제공'][i],15)]),
 text(957,757,285,28,'MIRI SMART AGRICULTURE',18,'#111',700),text(957,792,275,49,'농장 진단부터 맞춤 설계,\n현장 적용까지 단계별로 함께합니다.',18,'#111',600)
],[R(0,0,1280,152),R(48,374,351,117),R(48,715,350,121),R(470,281,350,59),R(470,448,350,60),R(470,618,350,59),R(470,787,350,61),R(898,183,213,119),R(898,376,213,118),R(898,563,213,125),R(955,753,289,94)]);
// Music-festival inner spread: most colored typography was absent in OCR.
p['l56/s02'].removeText=[R(0,0,1280,909)];p['l56/s02'].elements=[];
const orange='#c45425',olive='#9b982c',cream='#fff9e4';
add('l56/s02',[
 heading(76,34,286,66,'Music Stage',50,orange,'Figtree'),heading(496,34,300,66,'Festival Zone',50,'#ffcf62','Figtree'),heading(1004,34,155,66,'Event',50,orange,'Figtree'),heading(86,472,274,66,'Time Table',50,orange,'Figtree'),heading(915,512,317,66,'Special Guest',48,orange,'Figtree'),
 ...['버스킹 공연','인디밴드 무대','댄스 퍼포먼스','메인 공연','초청가수 무대','DJ 퍼포먼스'].map((t,i)=>heading(30+(i%3)*126,253+Math.floor(i/3)*169,114,24,t,16,orange)),
 ...['오프닝','버스킹 공연','인디밴드 무대','댄스 퍼포먼스','초청가수 스페셜 무대','피날레 공연'].flatMap((t,i)=>[text(69,568+i*55,76,27,`${15+i}:00`,21,orange,700),text(142,568+i*55,237,27,t,21,'#7d7055',600),...(i<5?[L(45,602+i*55,337,1,orange)]:[])]),
 C(553,140,170,38,'체험 프로그램',21,olive,{color:'#fff',radius:22}),C(553,524,170,39,'푸드트럭',21,olive,{color:'#fff',radius:22}),
 ...['가을 포토존','아트 체험존','캘리그라피 체험','향초 만들기','푸드트럭','커피 & 디저트','간식 부스','야외 푸드존'].map((t,i)=>heading(472+(i%2)*178,301+Math.floor(i/2)*151+(i>=4?82:0),152,29,t,18,'#7d7055')),
 ...['럭키드로우','SNS 인증 이벤트','스탬프 투어','현장 경품 추첨'].flatMap((t,i)=>[C(997,135+i*97,81,27,`Event 0${i+1}`,16,orange,{color:'#fff',radius:18,weight:400}),text(1084,138+i*97,163,27,t,18,orange),text(1000,172+i*97,232,48,['행운 가득 럭키드로우에 참여하고\n푸짐한 경품의 주인공이 되어보세요','축제의 즐거운 순간을 사진으로 남기고\n인증하면 특별한 선물을 받아보세요','행사장 곳곳을 둘러보며 스탬프를 모으고\n다양한 기념품과 혜택을 만나보세요','축제의 마지막까지 함께 즐기며\n풍성한 경품 추첨의 행운을 만나보세요'][i],13,'#776b55')]),
 ...['가수 김미리','밴드 비즈노래','DJ 미캔'].map((t,i)=>heading(882+i*126,852,107,23,t,13,orange))
]);
add('l56/s01',[
 heading(79,38,288,61,'Information',50,orange,'Figtree'),heading(549,38,180,61,'Contact',50,'#ffcf62','Figtree'),
 ...['Autumn','Music','Festival'].map((t,i)=>heading(548,160+i*53,206,60,t,53,[orange,'#e9b633',olive][i],'Figtree')),
 ...['주최·주관','문의','이메일','홈페이지','SNS','입장료'].flatMap((t,i)=>[C(486,354+i*48,96,32,t,19,olive,{color:'#fff',radius:18}),text(594,359+i*48,218,30,['미리문화재단','123-456-789','festival@miricity.go.kr','www.festival.co.kr','@autumnfestival','미리 시민 입장 무료'][i],18,'#7d7055',600)]),
 ...['Autumn','Music','Festival'].map((t,i)=>heading(921,196+i*78,324,82,t,70,[orange,'#e9b633',olive][i],'Figtree')),
 heading(977,446,259,33,'2096.10.17 SAT',26,'#da970c','Figtree'),heading(976,482,260,26,'중앙광장 특설무대',19,'#776b55'),
 heading(597,664,190,51,'2090 AUTUMN\nMUSIC FESTIVAL',22,olive),text(597,717,190,47,'실시간 주차 현황 및\n공연 라인업 확인하기',18,'#7d7055'),heading(569,811,167,39,'⚠ Notice',32,'#ffcf62','Figtree'),heading(450,856,377,23,'주차장이 혼잡할 수 있으니 대중교통 이용을 권장합니다',14,'#df9c81')
],[R(43,18,366,85),R(502,17,306,97),R(481,136,329,188),R(482,350,332,290),R(895,108,385,408),R(588,660,218,114),R(447,806,382,79)]);
// Rebuild true structural shapes; OCR color components are not semantic cards.
p['l51/s02'].clearShapes=true;
p['l51/s02'].elements=[B(55,53,1170,803,'#fff'),B(435,53,409,803,'#f1f3f4'),L(870,481,328,1,'#a7a0b8'),L(870,610,328,1,'#a7a0b8'),L(870,648,328,1,'#a7a0b8'),L(870,805,328,1,'#a7a0b8'),L(472,732,336,1,'#a7a0b8'),...(p['l51/s02'].elements??[]).filter(e=>e.kind!=='box')];
p['l52/s01'].images![0].layer='background';
p['l52/s01'].elements=[B(0,754,427,155,'#f3e8cf'),B(850,0,430,365,'#d5c2a5'),B(850,853,430,56,'#876240'),B(454,22,368,860,'#fff',{border:'3px solid #d7bf98',radius:55}),B(76,144,120,120,'#fff3da',{border:'2px solid #cfb790',radius:20}),B(233,144,120,120,'#fff3da',{border:'2px solid #cfb790',radius:20}),B(76,366,120,120,'#fff3da',{border:'2px solid #cfb790',radius:20}),B(233,366,120,120,'#fff3da',{border:'2px solid #cfb790',radius:20}),IC(99,184,74,45,'Truck','#876240'),IC(258,179,67,54,'Building2','#876240'),IC(108,402,55,46,'Gift','#876240'),IC(269,400,60,48,'CalendarClock','#876240'),...(p['l52/s01'].elements??[])];
p['l56/s01'].images!.find(i=>i.x===854&&i.h===909)!.layer='background';
p['l60/s02'].images![0].layer='background';p['l60/s02'].clearShapes=true;
p['l60/s02'].elements=[
 B(0,0,429,161,'#ffd346'),B(429,0,422,161,'#83cbc5'),B(851,0,429,161,'#19bed4'),
 ...[64,459,886].map(x=>B(x,87,334,62,'#fff',{radius:50})),
 ...[452,644].flatMap(x=>[B(x,258,183,286,'#fff',{border:'1px solid #111',radius:9}),B(x,556,183,286,'#fff',{border:'1px solid #111',radius:9})]),
 ...[261,435,610].map(y=>B(875,y,348,160,'#effaff',{border:'1px solid #111',radius:20})),
 ...[278,452,628].map(y=>B(897,y,306,31,'#19bed4',{border:'1px solid #111',radius:20})),
 ...[255,407,559,710].map(y=>B(62,y,334,30,'#ffd346',{border:'1px solid #111',radius:18})),
 ...[292,444,596,747].flatMap(y=>[0,1,2].map(i=>B(222,y+i*35,174,31,'#fff',{border:'1px solid #edc34c',radius:10}))),
 ...(p['l60/s02'].elements??[])
];
p['l56/s02'].clearShapes=true;p['l56/s02'].elements=[B(427,0,426,909,'#c45a39'),
 ...[0,1,2,3,4,5].map(i=>B(29+(i%3)*126,126+Math.floor(i/3)*170,117,160,cream,{radius:16})),
 B(31,550,365,325,cream,{radius:17}),B(456,126,364,365,cream,{radius:24}),B(456,510,364,365,cream,{radius:24}),
 ...[126,223,320,417].map(y=>B(886,y,364,84,cream,{radius:16})),
 ...[877,1003,1129].map(x=>B(x,590,117,285,cream,{radius:16})),...(p['l56/s02'].elements??[])];
p['l56/s01'].clearShapes=true;p['l56/s01'].removeText=[R(0,0,1280,909)];
p['l56/s01'].elements=[B(427,0,427,909,'#c45a39'),B(30,125,364,345,cream,{radius:29}),B(30,486,364,389,cream,{radius:29}),B(455,125,365,674,cream,{radius:30}),B(482,652,312,121,'#fbefc5',{radius:16}),
 ...['일시','장소','참여대상'].flatMap((t,i)=>[C(52,337+i*41,96,33,t,20,orange,{color:'#fff',radius:22}),text(161,345+i*41,210,29,['2096.10.17(토)','미리시 중앙광장','전 연령 참여 가능'][i],18,'#7d7055',600)]),
 C(52,506,96,33,'오시는길',20,orange,{color:'#fff',radius:22}),text(70,552,278,28,'비즈시 비즈구 비즈로 123',16,'#7d7055'),
 ...[[57,629,316,12],[124,590,12,161],[214,590,12,164],[307,590,12,165],[59,679,270,12]].map(([x,y,w,h])=>B(x,y,w,h,'#f5edcf')),
 ...[[143,619,'비즈북중학교'],[264,599,'비즈여자\n중학교'],[66,653,'비즈2차\nAPT'],[203,654,'비즈소방서'],[139,697,'비즈시립\n도서관'],[332,661,'미리시\n중앙광장']].map(([x,y,t])=>text(x as number,y as number,81,32,t as string,12,'#7d7055')),
 ...['대중교통 이용 시 버스 101·202·303번','지하철 이용 시 지하철 비즈역 1번 출구 도보 5분','자가용 이용 시 비즈공원 주차장 최초 1시간 무료'].map((t,i)=>text(53,772+i*31,326,25,t,15,orange,600)),
 ...(p['l56/s01'].elements??[]),heading(952,124,248,54,'음악으로 물드는 가을밤',24,olive)
];
p['l58/s02'].removeText=[R(0,0,1280,909)];p['l58/s02'].clearShapes=true;p['l58/s02'].elements=[
 text(30,45,365,30,'INFO',23,'#999',700),text(30,83,373,98,'ABOUT\nEXHIBITION',43,'#000',700),text(30,197,372,29,'익숙한 풍경 사이에 머무는 작은 순간들',21),
 text(33,723,372,82,'〈김미리 개인전〉은 우리가 무심코 지나치는\n일상의 장면과 그 안에 남겨진 감정을\n천천히 바라보는 전시입니다.',18),text(33,821,372,79,'작가는 빛과 색, 반복되는 형태를 통해\n익숙한 공간을 새로운 시선으로 기록합니다',18),
 text(456,45,367,30,'NOTE',23,'#999',700),text(456,83,365,98,'ARTIST\nNOTE',43,'#000',700),text(460,196,365,29,'< KIM MIRI > , 전시를 기획하며',21),
 text(459,245,368,58,'“익숙한 풍경을 오래 바라보면\n그 안에서 낯선 순간을 발견하게 됩니다.”',19,'#4fb8c5'),text(459,323,368,105,'매일 마주하지만 쉽게 지나쳐버리는 장면들을\n화면 안에 천천히 쌓아 올렸습니다.\n이번 전시가 각자의 기억 속 풍경을\n다시 바라보는 작은 계기가 되기를 바랍니다.',18),
 text(888,469,365,29,'ABOUT',23,'#999',700),text(888,511,365,52,'WORKS',43,'#000',700),text(888,563,365,29,'SELECTED WORKS · 2099',21),
 ...['오후의 창','머무는 빛','조용한 정원'].flatMap((t,i)=>[text(890,621+i*101,25,28,`0${i+1}`,15),text(921,615+i*101,126,32,t,21,'#000',700),text(1015,625+i*101,180,23,['Afternoon Window','Light That Stays','Quiet Garden'][i],13,'#4fb8c5'),text(921,645+i*101,199,33,['72.7 × 60.6 cm','90.9 × 72.7 cm','65.1 × 53.0 cm'][i]+'\nOil on canvas, 2099',13,'#777'),...(i<2?[L(888,694+i*99,365,1,'#999')]:[])]),
 text(1075,470,427,150,'MIRI.KIM\nGALLERY',70,'#eeeeee'),
];
// Explicit chips retain optical centering; plain rounded rectangles have no text padding heuristics.
add('l53/s01',[C(32,31,362,55,'어떤 기술을 컨설팅하나요?',24,'#a8c858',{radius:12,weight:400}),C(459,31,362,55,'상담 신청 및 문의 안내',24,'#a8c858',{radius:12,weight:400}),C(55,118,318,42,'1. 스마트팜 기술 컨설팅',19,'#a8c858',{radius:0}),C(55,505,318,42,'2. 친환경 농업 컨설팅',19,'#a8c858',{radius:0}),C(481,118,318,42,'상담 신청 안내',19,'#a8c858',{radius:12}),C(481,505,318,42,'상담 가능 분야',19,'#a8c858',{radius:12})],[R(25,23,798,66),R(51,112,755,50),R(51,499,755,50)]);
add('l53/s02',[C(32,357,362,55,'이런 분께 추천합니다',24,'#a8c858',{radius:12,weight:400}),C(459,357,362,55,'컨설팅 프로그램 안내',24,'#a8c858',{radius:12,weight:400}),C(886,31,362,55,'어떻게 진행되나요?',24,'#a8c858',{radius:12,weight:400}),C(907,634,318,42,'컨설팅 기대 효과',19,'#a8c858',{radius:0})],[R(28,350,800,66),R(877,23,379,70),R(900,624,338,61)]);
add('l55/s01',[
 heading(58,49,306,97,'무료 교육\n신청 방법 안내',45,'#303030','Jua'),
 C(485,39,136,42,'교육 장소',25,'#fff342',{border:'2px solid #303030',radius:30,font:'Jua'}),heading(503,99,275,104,'오시는 길\n및 종합 안내',45,'#303030','Jua'),
 C(940,101,255,59,'시니어를 위한',38,'#f8edaf',{border:'3px solid #303030',radius:7,font:'Jua'}),C(891,166,351,110,'AI·디지털',72,'#43c6f1',{border:'3px solid #303030',radius:13,font:'Jua'}),C(908,268,325,113,'무료교육',75,'#fff',{border:'3px solid #303030',radius:13,font:'Jua'}),
 ...['오시는 길','운영 시간','문의처'].map((t,i)=>C(489,442+i*106,110,34,t,24,'#43c6f1',{radius:20,font:'Jua'}))
],[R(44,39,361,112),R(483,36,312,172),R(879,79,375,317),R(479,436,134,47),R(479,542,134,47),R(479,648,134,47)]);
add('l55/s02',[
 heading(48,50,370,103,'시니어를 위한\n맞춤형 디지털 교육',45,'#fff','Jua'),heading(48,208,360,53,'이런 분께 추천드려요!',35,'#303030','Jua'),heading(465,208,337,53,'교육 과정 안내',35,'#303030','Jua'),heading(900,50,339,99,'2080년 하반기\n교육 일정 안내',45,'#303030','Jua'),
 C(484,279,191,40,'스마트폰 기초반',26,'#fff342',{border:'2px solid #333',radius:30,font:'Jua'}),C(484,586,191,41,'AI 생활 체험반',26,'#43c6f1',{border:'2px solid #333',radius:30,font:'Jua'}),C(897,603,112,34,'공통 안내',24,'#43c6f1',{radius:20,font:'Jua'})
],[R(37,35,384,122),R(45,205,787,59),R(890,38,358,120),R(480,270,208,57),R(480,577,208,57),R(890,595,129,50)]);
add('l57/s01',[C(36,51,362,65,'신청방법',27,'#00b8e9',{color:'#fff',radius:45,font:'Jua'}),C(461,52,362,64,'오시는 길',27,'#08528c',{color:'#fff',radius:45,font:'Jua'}),C(461,594,362,65,'문의처',27,'#08528c',{color:'#fff',radius:45,font:'Jua'}),C(888,52,362,64,'스마트폰, 이제 어렵지 않아요!',27,'#00b8e9',{color:'#fff',radius:45,font:'Jua'})],[R(28,39,380,89),R(451,40,380,89),R(451,585,380,87),R(879,40,382,89)]);
add('l57/s02',[heading(496,71,294,55,'교육 과정 소개',42,'#fff','Black Han Sans'),heading(960,71,244,55,'교육 일정표',42,'#08528c','Black Han Sans'),C(879,145,377,51,'2080 하반기 교육 일정',29,'#08528c',{color:'#fff',radius:30,font:'Jua'}),C(878,620,378,50,'공통 안내',27,'#08528c',{color:'#fff',radius:30,font:'Jua'})],[R(487,62,322,64),R(945,64,309,72),R(873,138,386,64),R(872,614,388,66)]);
add('l59/s01',[heading(138,79,204,38,'미리요양원 소개',32,'#fff','Jua'),heading(466,94,189,43,'오시는 길',34,'#fff','Jua'),text(885,226,360,87,'미리요양원',68,'#fffba3',700)],[R(131,71,216,52),R(458,85,229,56),R(882,223,376,94)]);
add('l59/s02',[C(58,69,337,58,'입소 안내',32,'#fff',{color:'#1db5b1',radius:45,font:'Jua'}),C(455,68,368,58,'시설 소개',32,'#fff',{color:'#1db5b1',radius:45,font:'Jua'}),C(881,69,365,58,'프로그램 & 서비스',32,'#1db5b1',{color:'#fff',radius:45,font:'Jua'})],[R(54,61,349,82),R(450,58,377,86),R(875,58,375,86)]);
const scheduleRows=[['스마트폰\n기초반','8. 4\n~ 8. 25','화\n10:00\n~12:00','7. 31'],['생활 앱\n활용반','8. 6\n~ 8. 27','목\n14:00\n~16:00','7. 31'],['AI 체험반','9. 2\n~ 9. 23','화\n10:00\n~12:00','8. 29'],['키오스크\n적응반','9. 4\n~ 9. 25','목\n14:00\n~16:00','8. 29']];
add('l55/s02',[
 ...['과정명','운영 기간','요일·시간','접수 마감'].flatMap((t,j)=>[B(892+j*87.3,177,87.3,42,'#43c6f1',{border:'0.7px solid #aca78e'}),C(892+j*87.3,177,87.3,42,t,17,'transparent',{color:'#fff',radius:0,weight:400})]),
 ...scheduleRows.flatMap((row,i)=>row.flatMap((t,j)=>[B(892+j*87.3,219+i*88.5,87.3,88.5,'#fff',{border:'0.7px solid #aca78e'}),T(896+j*87.3,235+i*88.5,79,71,t,17,{align:'center',lineHeight:1.23,color:'#444'})]))
],[R(887,173,361,407)]);
const scheduleBlue=[['스마트폰\n기초반','8.4 -\n8.25','화 10:00 -\n12:00','7.31'],['생활앱\n활용반','8.6 -\n8.27','목 14:00 -\n16:00','7.31'],['AI\n체험반','9.2 -\n9.23','화 10:00 -\n12:00','8.29'],['키오스크\n적응반','9.4 -\n9.25','목 14:00 -\n16:00','8.29']];
add('l57/s02',[
 ...['과정명','운영기간','요일·시간','접수마감'].map((t,j)=>C(879+j*94,196,94,54,t,22,'#00b8e9',{color:'#fff',radius:0,font:'Jua'})),
 ...scheduleBlue.flatMap((row,i)=>row.flatMap((t,j)=>[B(879+j*94,250+i*86,94,86,i%2?'#f8f8f8':'#fff'),T(884+j*94,268+i*86,84,63,t,21,{align:'center',lineHeight:1.5,color:j===3?'#00b8e9':'#08528c',weight:j===0||j===3?700:400})]))
],[R(875,194,386,408)]);
add('l55/s01',...(()=>{const icons=['PhoneCall','Building2','MonitorUp','ClipboardCheck'];return [[...icons.flatMap((n,i)=>[B(66,320+i*140,92,90,'#43c6f1',{radius:12}),IC(84,339+i*140,56,52,n,'#fff')])],[...icons.map((_,i)=>R(63,318+i*140,99,96))]] as [ReturnType<typeof T>[],Region[]]})());
add('l55/s02',...(()=>{const icons=['Smartphone','MousePointerClick','Monitor','Video'];return [[...icons.map((n,i)=>IC(90,303+i*119,47,52,n,'#303030'))],[...icons.map((_,i)=>R(77,293+i*119,68,70))]] as [ReturnType<typeof T>[],Region[]]})());
p['l49/s01'].clearShapes=true;p['l49/s01'].elements=[B(21,106,395,765,'#fff',{border:'1px solid #111'}),B(442,106,396,765,'#fff',{border:'1px solid #111'}),B(869,457,394,414,'#fff',{border:'1px solid #111'}),...(p['l49/s01'].elements??[])];
p['l49/s02'].clearShapes=true;p['l49/s02'].elements=[...[21,442,866].map(x=>B(x,106,395,765,'#fff',{border:'1px solid #111'})),B(866,724,395,147,green,{border:'1px solid #111'}),...[21,442,866].map(x=>L(x,150,395,1,'#777')),...(p['l49/s02'].elements??[])];
// Fine dotted separators are simple editable rules.
const dots=(x:number,y:number,w:number)=>Array.from({length:Math.floor(w/5)},(_,i)=>B(x+i*5,y,2,1,'#aaa'));
p['l49/s01'].elements!.unshift(...[265,367,470,572].flatMap(y=>dots(54,y,330)));
p['l49/s02'].elements!.unshift(...[339,528].flatMap(y=>dots(897,y,335)));
p['l49/s01'].removeText!.push(R(881,831,381,30));add('l49/s01',[text(889,837,285,27,'MIRI SMART AGRICULTURE',18,'#111',600)]);
p['l52/s01'].textStyles!.push({...R(0,754,427,155),color:'#795634'},{...R(94,58,240,61),color:'#876240'});
const lime='#83b71e',forest='#4a8f39',pale='#f5ffe5';
p['l50/s01'].removeText=[R(0,0,1280,909)];p['l50/s01'].clearShapes=true;p['l50/s01'].elements=[B(427,0,427,909,forest),B(854,746,426,163,lime),
 heading(115,54,203,95,'이런 분께\n추천합니다',40,lime,'Jua'),
 ...['새싹농부','성장농부','예비농부','꼼꼼농부'].flatMap((t,i)=>[C(71+(i%2)*186,177+Math.floor(i/2)*358,102,24,t,17,lime,{color:'#fff',radius:20,font:'Jua'}),heading(38+(i%2)*200,208+Math.floor(i/2)*358,180,29,['스마트팜 도입 준비','친환경 재배 전환','청년 농부 준비','기존 농장 개선'][i],20,lime,'Jua'),C(43+(i%2)*186,410+Math.floor(i/2)*365,159,97,['어떤 설비부터\n시작해야 할지\n막막해요','친환경 농업\n운영 기준 방법을\n모르겠어요','기술 기반\n농업 운영 방향을\n배우고 싶어요','현재 시설과\n재배 흐름을\n점검하고 싶어요'][i],18,i===1||i===2?lime:'#fff',{border:'1px solid #8fac42',color:i===1||i===2?'#fff':lime,radius:11,font:'Jua',lineHeight:1.2})]),
 C(549,67,230,78,'청년인데 농업을\n시작하고싶어요!',20,'#fff',{color:forest,radius:60,font:'Jua',lineHeight:1.2}),C(461,162,230,78,'친환경 농업은\n어떻게 운영해야하죠?',20,lime,{color:'#fff',radius:60,font:'Jua',lineHeight:1.2}),C(591,256,230,78,'농장에 맞는\n기술 도입이 궁금해요~',20,'#fff',{color:forest,radius:60,font:'Jua',lineHeight:1.2}),
 B(458,646,364,97,lime,{radius:18}),heading(482,660,318,29,'미리스마트농업연구소',21,'#fff','Jua'),IC(480,694,34,34,'Phone','#fff'),heading(516,686,286,45,'000-000-0000',39,'#fff','Jua'),B(458,750,364,123,'#fff',{radius:18}),text(581,772,225,26,'홈페이지',17,forest,700),text(581,795,225,20,'www.mirismartagri.co.kr',14,forest),text(581,820,225,24,'이메일',17,forest,700),text(581,841,225,20,'smartfarm@miriagri.co.kr',14,forest),
 heading(937,82,280,87,'스마트팜',73,forest,'Jua'),C(949,166,242,94,'더 쉽게',73,forest,{color:'#fff',font:'Jua',radius:15}),heading(934,276,287,78,'시작하기',73,lime,'Jua'),heading(925,375,304,53,'스마트팜·친환경 농업 기술\n컨설팅 프로그램',24,lime,'Jua'),heading(926,843,309,34,'미리스마트농업연구소',24,'#fff','Jua')
];
p['l50/s02'].removeText=[R(0,0,1280,909)];p['l50/s02'].clearShapes=true;p['l50/s02'].elements=[B(854,0,426,909,forest),
 heading(87,54,262,98,'어떤 기술을\n컨설팅하나요?',40,lime,'Jua'),heading(515,54,262,98,'컨설팅\n프로그램 안내',40,forest,'Jua'),heading(960,54,262,98,'어떻게\n진행되나요?',40,'#fff','Jua'),
 B(32,252,363,621,'#fff',{border:'1px solid #a6bc66',radius:20}),B(459,252,362,621,'#fff',{border:'1px solid #669b4e',radius:20}),C(32,188,363,51,'주요 컨설팅 분야',28,lime,{color:'#fff',radius:35,font:'Jua'}),C(459,188,362,51,'프로그램 구성',28,forest,{color:'#fff',radius:35,font:'Jua'}),
 C(69,429,288,37,'스마트팜 기술 컨설팅',23,'#fff',{border:'1px solid #aac060',radius:22,font:'Jua',color:lime}),C(69,725,288,37,'친환경 농업 컨설팅',23,'#fff',{border:'1px solid #aac060',radius:22,font:'Jua',color:lime}),
 T(70,477,288,78,'• 온습도·환기·관수 환경 제어 안내\n• 센서 기반 재배 관리 방향 제안\n• 작물별 운영 데이터 점검',16,{align:'center',color:'#92ab42',lineHeight:1.55}),T(70,775,288,78,'• 친환경 재배 운영 방향 상담\n• 토양·급수·관리 체계 점검\n• 지속가능 재배 방식 제안',16,{align:'center',color:'#92ab42',lineHeight:1.55}),
 ...['기초 진단 컨설팅','맞춤 설계 컨설팅','현장 적용 컨설팅'].flatMap((t,i)=>[B(477,339+i*196,326,106,'#f4f4f4',{radius:11}),C(538,292+i*196,204,37,`${i===2?2:i+1}  ${t}`,22,'#fff',{border:'1px solid #669b4e',radius:22,font:'Jua',color:forest}),text(624,359+i*196,176,91,['• 농장 현황 파악\n• 시설·재배 환경 점검\n• 현재 운영 문제점 정리','• 작물 및 운영 형태별\n  기술 제안\n• 도입 우선순위 설계\n• 재배·운영 방향 정리','• 기술 적용 체크\n• 운영 중 보완 포인트 안내\n• 실무형 피드백 제공'][i],16,'#699c5d')]),
 ...['상담 신청','사전 확인','맞춤 분석','컨설팅 진행','적용 점검'].flatMap((t,i)=>[B(886,188+i*84,362,67,'#fff',{radius:40}),B(886,188+i*84,66,66,i%2?lime:forest,{border:'1px solid #fff',radius:'50%'}),IC(903,201+i*84,33,39,['Headset','MessageCircle','BadgeCheck','Megaphone','FileText'][i],'#fff'),text(968,202+i*84,269,29,`${i+1}. ${t}`,24,i%2?lime:forest,700),text(968,230+i*84,269,28,['기본 정보와 농장 현황 접수','작물, 시설, 운영 방식 점검','농장 조건에 맞는 기술 방향 정리','현장 또는 비대면 방식으로 솔루션 안내','실행 가능한 항목 적용 후 포인트 확인'][i],15,'#7da36d')]),
 B(886,753,362,120,'#fff',{radius:18}),heading(939,767,257,30,'이런 걸 기대할 수 있어요!',23,forest,'Jua'),T(911,796,312,67,'1. 농장 운영 방향이 더 명확해져요\n2. 기술 도입 우선순위가 정리돼요\n3. 친환경·스마트농업의 이해도가 높아져요',16,{color:'#789d68',align:'center',lineHeight:1.5})
];
const purple='#433c75',paleType='#c3c2d7';
p['l51/s01'].removeText=[R(0,0,1280,909)];p['l51/s01'].clearShapes=true;p['l51/s01'].elements=[B(437,0,437,909,'#0b041b'),
 heading(171,266,112,32,'GREETING',22,paleType,'Tinos'),L(79,277,72,1,'#c3c2d7'),L(293,277,71,1,'#c3c2d7'),T(56,318,333,67,'오늘 이 자리에 함께 해 주신 모든 분께\n진심으로 감사드립니다.',22,{font:'Noto Serif KR',weight:700,color:'#fff',align:'center',lineHeight:1.55}),heading(56,396,333,26,'음악이 여러분의 일상에 작은 위로와 기쁨이 되기를 바랍니다.',13,paleType),heading(185,456,82,30,'공연 안내',20,paleType,'Noto Serif KR'),
 ...[['공연명','비즈홀 피아노 독주회'],['공연 기간&일정','2090.07.12 (토), 오후 5:00'],['공연 장소','비즈시 비즈구 비즈로 123 비즈홀']].flatMap(([a,b],i)=>[B(56,493+i*47,332,41,'#322d46'),L(56,492+i*47,332,1,'#b5b3c5'),text(70,503+i*47,127,31,a+' |',16,paleType,700),T(169,503+i*47,210,31,b,15,{font:'Noto Serif KR',color:'#fff',align:'right'})]),
 text(56,644,331,24,'* 관람등급: 8세 이상',13,paleType),text(56,665,331,28,'* 공연 러닝타임은 인터미션 포함 1시간 30분입니다.',13,paleType),heading(197,716,65,29,'티켓',20,paleType,'Noto Serif KR'),B(56,748,332,41,'#322d46'),L(56,747,332,1,'#b5b3c5'),C(56,748,332,41,'R석 50,000원 / S석 30,000원 / A석 20,000원',15,'transparent',{font:'Noto Serif KR',color:'#fff',radius:0,weight:400}),text(56,798,332,23,'* 예매 문의는 01) 1234-5555로 유선 연락 부탁드립니다.',13,paleType),text(56,819,332,23,'* 현장 발권은 공연 1시간 전부터 가능합니다.',13,paleType),
 heading(608,70,109,28,'LOCATION',17,'#716b86','Tinos'),heading(577,101,164,39,'찾아오시는 길',29,paleType,'Noto Serif KR'),L(626,153,66,1,'#928aa7'),IC(573,172,34,42,'MapPin','#8d68ab'),heading(609,183,149,33,'비즈콘서트홀',23,'#fff','Noto Serif KR'),heading(550,231,222,50,'서울특별시 비즈구 비즈로 123\n비즈아트센터 2F',17,'#fff','Noto Serif KR'),
 B(488,317,337,208,'#0b041b',{border:'2px solid #21172f',radius:10}),L(538,342,7,160,'#544967'),L(653,342,7,161,'#544967'),L(504,422,305,7,'#544967'),B(556,453,70,40,'#4b335f'),IC(575,432,36,45,'MapPin','#fff'),
 ...[[581,344,'비즈역\n(3번 출구)'],[746,354,'비즈공원'],[694,397,'비즈초등학교'],[746,446,'비즈중학교'],[692,482,'비즈시청'],[561,476,'비즈콘서트홀']].map(([x,y,t])=>text(x as number,y as number,95,30,t as string,12,'#fff')),
 ...[[555,347],[725,351],[673,390],[725,441],[673,478]].map(([x,y])=>B(x,y,16,16,'#0b041b',{border:'4px solid #7d758f',radius:'50%'})),
 ...['지하철','버스','주차 안내'].flatMap((t,i)=>[IC(521+i*119,567,40,49,['TrainFront','BusFront','Car'][i],'#777084'),heading(491+i*119,630,101,28,t,20,'#fff','Noto Serif KR'),T(489+i*119,655,104,48,['비즈역 3번 출구에서\n도보 약 5분','비즈아트센터 정류장\n123·456·7890번','비즈아트센터 지하\n관람객 3시간 무료'][i],13,{color:'#fff',align:'center',lineHeight:1.4})]),
 B(488,725,331,71,'#282135'),L(488,725,331,1,'#c3c2d7'),T(510,741,287,54,'공연 당일 주변 교통이 혼잡할 수 있으니\n가급적 대중교통을 이용해 주시기 바랍니다.',16,{font:'Noto Serif KR',align:'center',color:'#fff',lineHeight:1.6}),text(487,832,335,23,'문의처  01) 1234-5678   연주  비즈 챔버앙상블',15,'#fff'),
 heading(1015,255,123,35,'2090',31,'#fff','Tinos'),heading(921,301,313,55,'BIZ HALL',51,'#cdd6ee','Tinos'),heading(909,363,337,64,'피아노 독주회',52,'#cdd6ee','Noto Serif KR'),heading(939,448,273,35,'2090. 7. 12. SAT. PM 5:00',25,'#fff','Tinos'),heading(993,487,165,29,'비즈홀 콘서트홀',21,paleType,'Noto Serif KR'),C(984,552,183,33,'MUSICAL PERFORMANCE',16,'#8d94aa',{color:'#fff',radius:0,font:'Tinos',weight:400}),heading(996,598,160,28,'비즈 챔버 앙상블',18,paleType,'Noto Serif KR'),heading(1073,847,164,26,'BIZ CONCERT CHAMBER',15,'#fff','Tinos')
];
p['l51/s02'].removeText=[R(0,0,1280,909)];p['l51/s02'].elements=[B(55,53,1170,803,'#fff'),B(435,53,409,803,'#f1f3f4'),
 ...[92,922].map(x=>text(x,105,292,28,'2090 PIANO RECITAL',19,'#bbb')),
 text(91,146,330,50,'CHARACTER',39,purple,700),text(231,197,188,50,'PROFILE',39,purple,700),text(326,132,73,87,'&',81,'#ededf0'),
 ...[['정원의 주인 (소프라노)','비즈 소프라노','비밀을 품은 정원지기 여인','· 비즈대학교 음악대학 성악과 졸업\n· 비즈 국제 성악 콩쿠르 1위\n· 비즈 오페라단 주역 다수 역임\n· 현 비즈 예술대학원 출강'],['나그네 (테너)','비즈 테너','정원을 찾아온 이방인','· 비즈대학교 음악대학원 졸업\n· 비즈 오페라 신인상 수상\n· 비즈 시립오페라단 단원'],['정원지기 (바리톤)','비즈 바리톤','오래 정원을 돌봐온 노인','· 비즈 음악원 아카데미아 졸업\n· 비즈 오페라 페스티벌 주역 출연\n· 비즈 국립오페라단 전속 단원'],['소녀 (메조소프라노)','비즈 메조','신과 소통하는 신비한 존재','· 비즈예술고등학교 졸업\n· 비즈음악콩쿠르 2위\n· 비즈 챔버오페라 단원']].flatMap(([a,b,c,d],i)=>{const x=102+(i%2)*168,y=388+Math.floor(i/2)*296;return [text(x,y,151,24,a,16,purple,700),text(x,y+23,151,24,b,15,'#746ab0',700),text(x,y+45,151,29,c,12,'#777'),text(x+6,y+73,151,91,d,11,'#666')]}),
 heading(550,144,186,90,'PROGRAM\nNOTE',39,purple,'Tinos'),T(494,250,297,145,'음악은 때로 말보다 깊은 진실을 전합니다.\n이번 무대는 정원의 비밀을 둘러싼 네 인물의 내면과\n그들이 마주하는 사랑과 갈등, 용서, 구원의 이야기를\n음악으로 풀어냅니다. 네 명의 성악가와\n피아노가 만들어내는 섬세한 울림 속에서\n각자의 기억 속 ‘정원’을 떠올려 보시길 바랍니다.',14,{align:'center',color:purple,lineHeight:1.75}),
 heading(588,587,107,29,'제작참여',21,purple,'Noto Serif KR'),L(472,601,115,1,'#a7a0b8'),L(691,601,115,1,'#a7a0b8'),
 ...[['음악감독 | 비즈 교수진','무대감독 | 박비즈'],['반주기획 | 비즈 챔버 오케스트라','조명감독 | 이비즈'],['연출감독 | 김비즈','무대디자인 | 비즈 디자인팀']].flatMap((row,i)=>row.map((t,j)=>text(472+j*175,638+i*25,173,25,t,12,purple,600))),L(472,732,336,1,'#a7a0b8'),text(473,762,332,26,'ⓘ 본 공연은 인터미션 포함 1시간 30분 예정입니다.',14,purple,600),text(473,789,337,26,'ⓘ 본 공연은 비즈아트센터와 비즈콘서트챔버가 함께 합니다.',14,purple,600),
 heading(940,147,189,47,'SYNOPSIS',39,purple,'Tinos'),T(890,227,293,178,'고요한 도시의 끝자락, 오래된 담장 안에 숨겨진 정원.\n수십 년간 아무도 발걸음하지 않던 그곳에\n어느 날 낯선 나그네가 찾아든다.\n정원의 주인은 그를 경계하면서도,\n오랜날 묻어두었던 비밀을 조금씩 꺼내 보이기 시작한다.\n음악과 함께 펼쳐지는 기억의 조각들,\n그리고 마침내 드러나는 정원의 진실.',14,{color:purple,align:'center',lineHeight:1.8}),heading(963,442,153,27,'PROGRAM',23,purple,'Tinos'),
 C(870,481,328,27,'[ 1부 ]',16,'#f3f4fb',{color:purple,radius:0,font:'Noto Serif KR'}),C(870,648,328,27,'[ 2부 ]',16,'#f3f4fb',{color:purple,radius:0,font:'Noto Serif KR'}),
 ...[481,610,648,805].map(y=>L(870,y,328,1,'#a7a0b8')),
 T(877,529,315,71,"G. VERDI — LA TRAVIATA 中 LIBIAMO NE' LIETI CALICI\nG. PUCCINI — LA BOHÈME 中 CHE GELIDA MANINA\nC. GOUNOD — FAUST 中 AVANT DE QUITTER CES LIEUX",13,{font:'Tinos',align:'center',lineHeight:1.8}),heading(963,622,150,27,'* INTERMISSION *',17,purple,'Tinos'),
 T(883,697,304,105,"G. DONIZETTI — L’ELISIR D’AMORE 中 UNA FURTIVA\nLAGRIMA\nF. LEHÁR — THE MERRY WIDOW 中 VILJA-LIED\n비즈 작곡 — 초연곡 『정원의 노래』",13,{font:'Tinos',align:'center',lineHeight:1.8})
];
p['l51/s02'].elements!.filter(e=>['CHARACTER','PROFILE'].includes(e.text??'')).forEach(e=>e.font='Tinos');
const brown='#876240',darkBrown='#6d4a20',paper='#fff9ed';
p['l52/s01'].removeText=[R(0,0,1280,909)];p['l52/s01'].clearShapes=true;p['l52/s01'].elements=[B(0,754,427,155,'#f3e8cf'),B(850,0,430,365,'#d5c2a5'),B(850,853,430,56,brown),B(454,22,368,860,'#fff',{border:'3px solid #d7bf98',radius:55}),
 C(94,60,239,51,'주문 및 배송 안내',24,paper,{font:'Noto Serif KR',color:brown,radius:35,border:'2px solid #cbb28b'}),
 ...['추석 선물세트\n전국 택배 배송','단체 및 기업\n주문 가능','답례품·행사\n선물 맞춤 제작','예약 주문 시\n원하는 날짜 발송'].flatMap((t,i)=>[B(76+(i%2)*157,144+Math.floor(i/2)*222,120,120,'#fff3da',{border:'2px solid #cfb790',radius:20}),T(62+(i%2)*158,288+Math.floor(i/2)*230,149,64,t,19,{font:'Noto Serif KR',color:'#fff1d7',align:'center',lineHeight:1.45}),IC(109+(i%2)*157,184+Math.floor(i/2)*222,56,48,['Truck','Building2','Gift','CalendarClock'][i],brown)]),
 L(84,590,267,1,'#d9c3a0'),C(152,620,128,38,'문의',22,paper,{font:'Noto Serif KR',color:brown,radius:25,border:'2px solid #cbb28b'}),heading(151,673,141,31,'1588-1234',22,'#fff1d7','Noto Serif KR'),heading(69,709,295,31,'www.bizhangwa.com',22,'#fff1d7','Tinos'),T(76,787,283,80,'전통의 맛을 담아\n정성을 전합니다.',32,{font:'Noto Serif KR',color:darkBrown,align:'center',lineHeight:1.5}),
 heading(577,68,133,57,'BIZ\nHANGWA',24,brown,'Tinos'),heading(540,138,213,51,'비즈한과',39,brown,'Noto Serif KR'),T(500,317,282,74,'좋은 재료와 정직한 손맛으로\n오랜 시간 이어온\n전통 한과를 만듭니다.',18,{font:'Noto Serif KR',color:brown,align:'center',lineHeight:1.45}),L(505,408,268,1,'#d7bf98'),T(500,430,282,53,'전통의 가치를 담아\n소중한 분께 감사의 마음을 전하세요.',18,{font:'Noto Serif KR',color:brown,align:'center',lineHeight:1.45}),
 ...['주소','대표번호','홈페이지','Instagram'].flatMap((t,i)=>[C(576,507+i*88,127,38,t,22,paper,{font:i===3?'Tinos':'Noto Serif KR',color:brown,radius:22,border:'2px solid #cbb28b'}),heading(491,559+i*88,296,29,['비즈특별시 한과로 123','1588-1234','www.bizhangwa.com','@biz_hangwa'][i],18,brown,i>0?'Tinos':'Noto Serif KR')]),
 heading(973,116,187,35,'BIZ HANGWA',24,darkBrown,'Tinos'),heading(968,161,196,40,'추석 선물세트',28,darkBrown,'Noto Serif KR'),T(913,204,309,134,'전통의 맛,\n정성을 담다',53,{font:'Noto Serif KR',color:darkBrown,align:'center',weight:600,lineHeight:1.25}),heading(879,870,375,26,'Premium Korean Traditional Sweets',22,'#f8e6c6','Tinos')
];
p['l52/s02'].removeText=[R(0,0,1280,909)];p['l52/s02'].clearShapes=true;p['l52/s02'].background='#e5e5e5';p['l52/s02'].elements=[B(31,28,368,854,paper,{border:'2px solid #d8c29f',radius:35}),B(430,0,420,909,'#d1c0a3'),
 heading(136,80,155,80,'비즈한과\n이야기',32,darkBrown,'Noto Serif KR'),T(86,493,258,309,'정성을 다해 만든 한과는\n좋은 재료에서 시작됩니다.\n\n엄선한 국내산 원료와\n전통 제조 방식을 바탕으로\n바삭한 식감과 은은한 단맛을\n그대로 담았습니다.\n\n가족과 함께하는 명절,\n소중한 분께 감사의 마음을\n비즈한과와 함께 전해보세요.',20,{font:'Noto Serif KR',color:brown,align:'center',lineHeight:1.55}),heading(504,51,279,55,'추석 선물세트',39,darkBrown,'Noto Serif KR'),
 ...['1호\n선물세트','2호\n선물세트','프리미엄\n선물세트'].flatMap((t,i)=>[B(460,120+i*238,359,226,paper,{border:'3px solid #d8c29f'}),T(663,146+i*238,139,63,t,25,{font:'Noto Serif KR',color:darkBrown,weight:700,lineHeight:1.1}),T(664,213+i*238,137,53,['전통 유과, 약과,\n강정으로 구성된\n실속형 선물세트','다양한 전통 한과를\n풍성하게\n담은 인기 선물세트','엄선한 한과를\n품격 있게 담은\n고급 선물세트'][i],15,{font:'Noto Serif KR',color:darkBrown,lineHeight:1.2}),text(663,301+i*238,145,29,['39,000원 | 500g','59,000원 | 800g','89,000원 | 1.2kg'][i],19,darkBrown,600)]),text(493,843,320,28,'※ 기업·단체 주문 및 예약 배송 가능합니다.',16,darkBrown,700),heading(908,232,321,52,'비즈한과의 특별함',34,darkBrown,'Noto Serif KR'),
 ...['국내산 원료 사용','전통 제조 방식','HACCP 인증 시설 생산','고급 선물 포장','전국 택배 배송','기업·단체 주문 가능'].flatMap((t,i)=>[B(886,292+i*96,364,87,paper),B(886,292+i*96,112,87,'#faf0d8'),IC(915,314+i*96,56,45,['CookingPot','Soup','ShieldCheck','Gift','Truck','Building2'][i],brown),text(1048,325+i*96,196,32,t,19,darkBrown,600)])
];
p['l52/s02'].elements!.filter(e=>e.kind==='text').forEach(e=>e.font='Noto Serif KR');
const agriTitles=['상담 신청','사전 확인','맞춤 분석','컨설팅 진행','적용 점검'];
const agriSteps=['기본 정보와 농장 현황 접수','작물, 시설, 운영 방식 점검','농장 조건에 맞는 기술 방향 정리','현장 또는 비대면 방식으로 솔루션 안내','적용 후 보완 포인트 확인, 보완'];
const agriPrograms=['기초 진단 컨설팅','맞춤 설계 컨설팅','현장 적용 컨설팅'];
const agriBullets=['· 농장 현황 파악\n· 시설·재배 환경 점검\n· 현재 운영 문제점 정리','· 작물 및 운영 형태별 기술 제안\n· 도입 우선순위 설계\n· 재배·운영 방향 정리','· 기술 적용 체크\n· 운영 중 보완 포인트 안내\n· 실무형 피드백 제공'];
const agriRecs=['스마트팜 도입을 처음 검토하는 농업인','친환경 재배로 전환을 고민하는 농가','청년 농부·귀농 준비자','농장 운영을 개선하고 싶은 농장주','추천 대상을 작성하세요'];
const agriRecBody=['어떤 설비부터 시작해야 할지 막막한 경우','운영 기준과 적용 방법이 필요한 경우','기술 기반 농업 운영 방향을 배우고 싶은 경우','현재 시설과 재배 흐름을 점검하고 싶은 경우','이곳에 내용을 작성하세요'];
const mintLime='#a8c858';
p['l53/s01'].removeText=[R(0,0,1280,909)];p['l53/s01'].clearShapes=true;p['l53/s01'].elements=[B(427,0,426,909,'#d4e0a7'),B(32,97,363,780,'#fff',{radius:17}),B(459,97,362,358,'#e6ecc8',{radius:17}),B(459,483,362,317,'#e6ecc8',{radius:17}),
 C(32,31,362,55,'어떤 기술을 컨설팅하나요?',24,mintLime,{radius:12,weight:400}),C(459,31,362,55,'상담 신청 및 문의 안내',24,mintLime,{radius:12,weight:400}),C(55,118,318,42,'1. 스마트팜 기술 컨설팅',19,mintLime,{radius:0}),C(55,505,318,42,'2. 친환경 농업 컨설팅',19,mintLime,{radius:0}),C(481,118,318,42,'상담 신청 안내',19,mintLime,{radius:12}),C(481,505,318,42,'상담 가능 분야',19,mintLime,{radius:12}),
 text(55,342,320,48,'스마트팜의 기술 개발에 대한 컨설팅을 진행합니다.\n이곳에 해당 컨설팅 내용에 대해 짧게 설명해주세요.',15),text(55,397,320,77,'· 온습도·환기·관수 환경 제어 안내\n· 센서 기반 재배 관리 방향 제안\n· 작물별 운영 데이터 점검',15),text(55,728,320,48,'친환경 농업 방식에 대한 컨설팅을 진행합니다.\n이곳에 해당 컨설팅 내용에 대해 짧게 설명해주세요.',15),text(55,784,320,77,'· 친환경 재배 운영 방향 상담\n· 토양·급수·관리 체계 점검\n· 지속가능 재배 방식 제안',15),
 ...['기관명','대표번호','담당자','이메일','홈페이지','팩스'].flatMap((t,i)=>[B(480,186+i*42,319,30,'#fff',{radius:22}),C(480,186+i*42,90,30,t,16,mintLime,{radius:22,weight:400}),text(581,192+i*42,210,24,['미리스마트농업연구소','00-000-0000','010-000-0000','smartfarm@miriagri.co.kr','www.mirismartagri.co.kr','00-000-0000'][i],15)]),
 ...['스마트팜 도입 상담','친환경 농업 운영 상담','청년 농업인 맞춤 컨설팅 상담','상담 가능 분야를 작성하세요'].flatMap((t,i)=>[B(480,572+i*53,319,45,'#fff',{radius:30}),B(480,574+i*53,40,40,mintLime,{radius:'50%'}),IC(488,581+i*53,24,25,['Wifi','Headset','FlaskConical','Sprout'][i],'#fff'),text(532,586+i*53,253,27,t,15)]),
 heading(490,828,302,45,'농장에 맞는 기술 도입 방향이 궁금하다면\n지금 상담으로 먼저 확인해보세요.',16),heading(929,592,288,56,'스마트팜·친환경 농업 기술\n컨설팅 프로그램',22),heading(968,675,210,57,'스마트팜',45,'#89ae35'),heading(909,731,328,59,'더 쉽게 시작하기',45,'#3f7050'),C(884,839,366,70,'미리스마트농업연구소',19,mintLime,{radius:20})
];
p['l53/s02'].removeText=[R(0,0,1280,909)];p['l53/s02'].clearShapes=true;p['l53/s02'].elements=[B(32,424,363,453,'#fff',{radius:17}),B(459,424,362,453,'#fff',{radius:17}),B(886,97,362,503,'#fff',{radius:17}),B(886,613,362,264,'#d4e0a7',{radius:17}),C(32,357,362,55,'이런 분께 추천합니다',24,mintLime,{radius:12,weight:400}),C(459,357,362,55,'컨설팅 프로그램 안내',24,mintLime,{radius:12,weight:400}),C(886,31,362,55,'어떻게 진행되나요?',24,mintLime,{radius:12,weight:400}),C(907,634,318,42,'컨설팅 기대 효과',19,mintLime,{radius:0}),
 ...agriRecs.flatMap((t,i)=>[B(54,451+i*88,20,20,'#fff',{border:'2px solid #a8c858'}),text(88,451+i*88,295,29,t,19),text(88,481+i*88,295,30,'| '+agriRecBody[i],15),...(i<4?dots(54,517+i*88,318):[])]),
 ...agriPrograms.flatMap((t,i)=>[text(614,450+i*146,198,30,`${i+1}. ${t}`,20),text(615,491+i*146,197,78,agriBullets[i],15),...(i<2?dots(479,578+i*146,318):[])]),
 ...agriTitles.flatMap((t,i)=>[B(913,131+i*92,64,64,mintLime,{radius:'50%'}),IC(927,144+i*92,36,36,['Headset','CircleCheck','SearchCheck','Lightbulb','BadgeCheck'][i],'#fff'),L(994,142+i*92,2,40,mintLime),text(1003,143+i*92,230,26,`${i+1}단계 : ${t}`,20),text(1003,170+i*92,229,28,agriSteps[i],15),...(i<4?[IC(933,201+i*92,24,15,'ChevronDown',mintLime)]:[])]),
 ...['농장 운영 방향이 더 명확해집니다.','기술 도입 우선순위를 정리할 수 있습니다.','친환경·스마트팜 운영 이해도를 높입니다.'].flatMap((t,i)=>[B(907,698+i*55,318,42,'#eff3d9',{radius:24}),C(909,700+i*55,38,38,`0${i+1}`,15,mintLime,{color:'#fff',radius:'50%'}),text(960,712+i*55,262,25,t,14)])
];
const seaGreen='#5dae86',mint='#e9f6ef';
const en=(x:number,y:number,w:number,h:number,t:string,size=36)=>T(x,y,w,h,t,size,{font:'Montserrat Alternates',color:'#000',weight:400,lineHeight:1.3});
const linePlus=(x:number)=>[...dots(x,146,332),L(x+319,135,3,22,seaGreen),L(x+309,145,23,3,seaGreen)];
p['l54/s01'].removeText=[R(0,0,1280,909)];p['l54/s01'].clearShapes=true;p['l54/s01'].elements=[B(427,0,427,909,mint),B(854,812,426,97,'#c5e4d5'),en(46,41,351,85,'TECHNOLOGIES\nWE COVER'),...linePlus(46),
 text(48,178,340,27,'| 스마트팜 기술 컨설팅',18,seaGreen,700),text(48,440,340,83,'· 온습도·환기·관수 환경 제어 안내\n· 센서 기반 재배 관리 방향 제안\n· 작물별 운영 데이터 점검',15,'#888'),text(48,536,340,27,'| 친환경 농업 컨설팅',18,seaGreen,700),text(48,798,340,83,'· 친환경 재배 운영 방향 상담\n· 토양·급수·관리 체계 점검\n· 지속가능 재배 방식 제안',15,'#888'),
 IC(463,62,22,22,'CircleCheck',seaGreen),text(495,62,311,33,'기관정보 및 문의처',20,'#000',700),
 ...['기관명','대표번호','모바일상담','이메일','홈페이지'].flatMap((t,i)=>[text(495,110+i*33,96,30,'•  '+t,16,seaGreen,600),text(589,110+i*33,236,30,['미리스마트농업연구소','00-000-0000','00-000-0000','smartfarm@miriagri.co.kr','www.mirismartagri.co.kr'][i],16,'#111',700)]),
 IC(463,308,22,22,'CircleCheck',seaGreen),text(495,308,311,33,'상담 가능 분야',20,'#000',700),
 ...['스마트팜\n도입 상담','친환경\n농업 운영 상담','청년 농업인\n맞춤 컨설팅 상담'].map((t,i)=>T(464+i*128,435,115,51,t,16,{align:'center',weight:600,lineHeight:1.5})),L(566,361,1,113,'#b8d7c8'),L(698,361,1,113,'#b8d7c8'),
 T(455,512,370,62,'농장에 맞는 기술 도입 방향이 궁금하다면\n지금 상담으로 먼저 확인해보세요.',20,{align:'center',weight:700,lineHeight:1.5}),
 heading(941,53,257,44,'· WELCOME TO ·',27,seaGreen,'Montserrat Alternates'),en(935,111,302,173,'SMART\nFARM',78),heading(903,297,340,32,': 스마트팜 친환경 기술 컨설팅',24,'#000'),heading(955,863,272,28,'미리스마트농업연구소',18)
];
p['l54/s02'].removeText=[R(0,0,1280,909)];p['l54/s02'].clearShapes=true;p['l54/s02'].elements=[B(427,0,427,909,mint),en(45,40,365,87,'RECOMMENDED\nFOR'),en(473,40,355,87,'CONSULTING\nPROGRAMS'),en(903,40,348,87,'HOW IT\nWORKS'),...linePlus(45),...linePlus(473),...linePlus(903),text(46,178,333,27,'| 추천 대상',18,seaGreen,700),text(474,178,333,27,'| 프로그램 구성',18,seaGreen,700),text(904,178,333,27,'| 컨설팅 진행 절차',18,seaGreen,700),
 ...[0,1,2,3].flatMap(i=>[text(169,236+i*174,229,64,['스마트팜 도입을\n처음 검토하는 농업인','친환경 재배로 전환을\n고민하는 농가','청년 농부·귀농 준비자','기존 농장 운영을\n개선하고 싶은 농장주'][i],22,'#000',700),text(169,302+i*174,229,53,agriRecBody[i],16,'#888'),...(i<3?[L(42,374+i*166,353,1,'#c5dfd1')]:[])]),
 ...agriPrograms.flatMap((t,i)=>[B(465,217+i*216,356,198,'#fff'),C(649,242+i*216,125,32,`PROGRAM 0${i+1}`,12,'#cce6d8',{radius:20,color:seaGreen,border:'1px solid #69ab88',weight:400}),text(650,287+i*216,162,30,t,19,'#111',600),text(650,332+i*216,162,86,agriBullets[i],15,'#888')]),
 L(941,249,1,408,'#c5dfd1'),...agriTitles.flatMap((t,i)=>[B(905,227+i*99,74,74,'#cce6d8',{radius:'50%'}),IC(924,248+i*99,37,33,['PhoneCall','ClipboardCheck','Monitor','Users','HandHeart'][i],seaGreen),C(962,228+i*99,32,32,String(i+1),14,seaGreen,{color:'#fff',radius:'50%',weight:400}),text(1025,236+i*97,60,31,`${i+1}단계`,22,seaGreen,700),text(1089,236+i*97,160,31,t,22,'#111',700),text(1025,270+i*97,222,51,i===4?'실행 가능한 항목부터 적용 후\n보완 포인트를 확인':agriSteps[i],15,'#888')]),
 B(882,727,371,150,'#fff',{border:'1px dotted #888'}),IC(905,744,22,22,'CircleCheck',seaGreen),text(934,745,177,29,'기대효과',20,'#111',600),L(904,776,331,1,'#c5dfd1'),text(904,796,336,72,'· 농장 운영 방향이 더 명확해집니다\n· 기술 도입 우선순위를 정리할 수 있습니다\n· 친환경·스마트농업 운영 이해도를 높일 수 있습니다',15,'#888')
];
const yellow='#fff342',cyan='#43c6f1',charcoal='#303030';
const keep55=p['l55/s02'].elements!.filter(e=>e.x>=892&&e.y>=177&&e.y<580);
p['l55/s01'].removeText=[R(0,0,1280,909)];p['l55/s01'].clearShapes=true;p['l55/s01'].elements=[B(427,0,426,909,cyan),B(40,298,348,562,'#fff',{border:'3px solid #333',radius:20}),B(466,62,348,704,'#fff',{border:'3px solid #333',radius:20}),B(853,829,427,80,'#fff'),heading(58,49,306,97,'무료 교육\n신청 방법 안내',45,charcoal,'Jua'),C(485,39,136,42,'교육 장소',25,yellow,{border:'2px solid #303030',radius:30,font:'Jua'}),heading(503,99,275,104,'오시는 길\n및 종합 안내',45,charcoal,'Jua'),
 ...['전화로 신청','방문 신청','온라인 신청','신청 완료'].flatMap((t,i)=>[B(66,320+i*140,92,90,cyan,{radius:12}),IC(84,339+i*140,56,52,['PhoneCall','Building2','MonitorUp','ClipboardCheck'][i],'#fff'),C(178,324+i*140,23,23,String(i+1),15,charcoal,{color:'#fff',radius:'50%'}),text(208,322+i*140,162,30,t,24,charcoal,700),text(177,355+i*140,195,68,['• 미리구청 평생교육과\n• 02-000-0000\n• (월~금, 오전 9시~오후 6시)','• 미리구청 2층 평생교육과\n• &미리 종합복지관 1층 접수대\n• 내용을 입력해 주세요.','• 온라인 신청\n• 미리구 평생학습 포털 접속\n• www.miri-life.go.kr','• 접수 완료 문자 확인\n• 교육 일정과 장소 확인\n• 교육 당일 스마트폰 지참'][i],15,charcoal),...(i<3?[IC(100,426+i*140,24,20,'Triangle','#ccc')]:[])]),
 B(489,214,298,208,'#f3f3f3',{radius:14}),L(505,265,264,20,'#bfc0c1'),B(573,224,21,187,'#bfc0c1',{radius:15}),B(594,316,175,21,'#bfc0c1',{radius:15}),L(697,336,9,75,'#bfc0c1'),IC(627,312,31,42,'MapPin','#f56e76'),text(527,240,84,21,'미리카페',12,charcoal,700),text(715,240,66,21,'미리은행',12,charcoal,700),text(527,353,84,21,'미리식당',12,charcoal,700),T(597,360,81,45,'미리구청\n평생교육과',15,{color:'#ee6a72',weight:700,align:'center',lineHeight:1.4}),
 ...['오시는 길','운영 시간','문의처'].flatMap((t,i)=>[C(489,442+i*106,110,34,t,24,cyan,{radius:20,font:'Jua'}),text(489,488+i*106,307,71,['• 미리시 미리구 미리로 123\n  (미리역 3번 출구 도보 5분)','• 월~금 09:00~18:00\n  점심시간(13:00~14:00)','• 02-000-0000\n• edu@miri.go.kr'][i],20,charcoal)]),
 text(593,800,216,73,'QR코드를 스캔하고\n디지털·AI 무료 교육을\n바로 신청하세요 →',20,charcoal),
 C(940,101,255,59,'시니어를 위한',38,'#f8edaf',{border:'3px solid #303030',radius:7,font:'Jua'}),C(891,166,351,110,'AI·디지털',72,cyan,{border:'3px solid #303030',radius:13,font:'Jua'}),C(908,268,325,113,'무료교육',75,'#fff',{border:'3px solid #303030',radius:13,font:'Jua'}),T(945,419,276,70,'스마트폰 사용\n이제 어렵지 않아요!',28,{align:'center',lineHeight:1.4}),IC(906,529,39,37,'Wifi','#fff'),B(893,518,65,52,cyan,{radius:10}),heading(982,854,239,32,'미리구 평생교육센터',26,charcoal,'Jua'),IC(941,856,35,28,'HandHeart',charcoal)
];
p['l55/s02'].removeText=[R(0,0,1280,909)];p['l55/s02'].clearShapes=true;p['l55/s02'].elements=[B(0,0,853,177,cyan),B(853,0,427,909,yellow),
 heading(48,50,370,103,'시니어를 위한\n맞춤형 디지털 교육',45,'#fff','Jua'),heading(48,208,360,53,'이런 분께 추천드려요!',35,charcoal,'Jua'),heading(465,208,337,53,'교육 과정 안내',35,charcoal,'Jua'),heading(900,50,339,99,'2080년 하반기\n교육 일정 안내',45,charcoal,'Jua'),
 ...['스마트폰 사용이\n익숙하지 않은 분','무인 키오스크\n이용이 어려운 분','AI 활용이나 인터넷\n검색이 어려운 분','자녀와 영상통화를\n하고 싶은 분'].flatMap((t,i)=>[B(53,277+i*119,340,98,'#fff',{radius:5}),B(75,291+i*119,74,74,'#e3f7fd',{radius:'50%'}),C(43,267+i*119,30,30,String(i+1),17,cyan,{color:'#fff',radius:'50%',weight:400}),IC(92,304+i*119,41,48,['Smartphone','MousePointerClick','Monitor','Video'][i],charcoal),text(181,303+i*119,199,66,t,24,charcoal,600)]),
 B(53,765,340,95,cyan,{border:'2px solid #333',radius:3}),T(69,784,308,70,'미리구 주민이라면\n수강료 100% 전액 무료',29,{align:'center',font:'Jua',color:'#fff',lineHeight:1.15}),
 ...['스마트폰 기초반','AI 생활 체험반'].flatMap((t,i)=>[B(466,303+i*307,348,249,'#fff',{border:'3px solid #333',radius:13}),C(484,279+i*307,191,40,t,26,i?cyan:yellow,{border:'2px solid #333',radius:30,font:'Jua'}),...['대상','내용','일정','장소'].flatMap((a,j)=>[C(484,341+i*307+[0,46,104,150][j],66,34,a,20,i?cyan:yellow,{radius:20,color:i?'#fff':charcoal}),text(560,346+i*307+[0,46,104,150][j],233,j===1?65:42,[['스마트폰을 처음 사용하시는 분','전화·문자 보내기,\n카카오톡 설치·사용법','매주 화요일 오전 10시','미리 종합복지관 2층 교육실'],['스마트폰 사용자라면 누구나','AI 음성 비서 사용,\n챗봇 대화, 자동 번역','매주 목요일 오후 2시','미리 평생학습관 1층 미디어실']][i][j],19,charcoal)])]),
 ...keep55,C(897,603,112,34,'공통 안내',24,cyan,{radius:20,font:'Jua'}),text(897,651,343,110,'• 수강료 전액 무료\n• 교육 이수자 수료증 발급\n• 교육 교재 및 실습용 기기 제공\n• 보조강사의 개별 실습 지원',21,charcoal),B(897,778,345,82,'#f6e82f'),T(927,797,286,56,'정원 마감 시 조기 마감될 수 있습니다.\n서둘러 신청해 주세요!',18,{align:'center',lineHeight:1.4,color:charcoal})
];
for(const key of ['l56/s01','l56/s02'])for(const e of p[key].elements??[])if(e.font==='Figtree')e.weight=400;
for(const e of p['l56/s02'].elements??[]){if(e.text==='Music Stage'){e.x=37;e.w=362}if(e.text==='Festival Zone'){e.x=455;e.w=365}if(e.text==='Special Guest'){e.x=885;e.w=363;e.size=48}if(e.text==='Time Table'){e.x=45;e.w=352}}
const blue='#08528c',bright='#00b8e9',ice='#f4fbff';
p['l57/s01'].background='#fff';p['l57/s01'].removeText=[R(0,0,1280,909)];p['l57/s01'].clearShapes=true;p['l57/s01'].elements=[B(429,0,427,909,bright),B(856,0,424,909,'#f8f8f8'),B(469,80,346,502,'#fff',{radius:20}),B(469,609,346,232,'#fff',{radius:12}),B(856,841,424,68,blue),
 C(36,51,362,65,'신청방법',27,bright,{color:'#fff',radius:45,font:'Jua'}),C(461,52,362,64,'오시는 길',27,blue,{color:'#fff',radius:45,font:'Jua'}),C(461,594,362,65,'문의처',27,blue,{color:'#fff',radius:45,font:'Jua'}),C(888,52,362,64,'스마트폰, 이제 어렵지 않아요!',27,bright,{color:'#fff',radius:45,font:'Jua'}),
 ...['첫번째','두번째','세번째','준비물'].flatMap((t,i)=>[text(46,[150,377,572,774][i],241,26,t,20,bright,700),text(46,[181,408,603,808][i],340,42,['전화로 신청','방문 신청','온라인 신청','신분증만 챙겨 오세요!'][i],32,blue,700)]),
 text(46,240,341,89,'미리구청 평생교육과\n02-000-0000\n(월~금, 오전 9시~오후 6시)',23,blue),text(46,465,341,62,'미리구청 2층 평생교육과\n또는 미리 종합복지관 1층 접수대',23,blue),text(46,664,341,61,'우측 상단 QR코드 촬영 후 사이트 접속\nwww.miri-life.go.kr',22,blue),...dots(39,347,354),...dots(39,542,354),...dots(39,744,354),
 B(479,138,329,169,'#fff'),L(479,182,329,40,'#e5e5e5'),L(595,114,34,193,'#e5e5e5'),L(694,209,17,98,'#e5e5e5'),L(613,200,195,20,'#e5e5e5'),IC(551,172,39,53,'MapPin',blue),IC(671,208,39,53,'MapPin',bright),
 IC(494,317,27,40,'MapPin',blue),text(530,320,279,44,'미리 종합복지관',34,blue,700),heading(534,368,276,31,'미리시 미리구 미리로 123',25,blue),heading(532,400,278,31,'(미리역 3번 출구 도보 5분)',20,'#111'),...dots(482,438,323),IC(494,463,27,40,'MapPin',bright),text(530,464,279,44,'미리 평생학습관',34,bright,700),heading(534,507,276,32,'미리시 미리구 배움길 45',25,blue),heading(532,540,278,31,'(미리버스 15번·27번 정류장 하차)',19,'#111'),
 IC(482,674,31,25,'Phone',bright),text(596,673,215,44,'02-000-0000',35,bright,700),IC(482,731,31,25,'Mail',bright),text(648,733,164,31,'edu@miri.go.kr',24,blue,700),text(482,789,93,31,'운영시간',24,bright,700),text(613,789,201,31,'월~금 09:00~18:00',24,blue,700),...dots(482,715,323),...dots(482,768,323),heading(481,855,332,35,'www.miri-life.go.kr',29,'#fff'),
 heading(975,503,184,76,'어르신',67,blue,'Black Han Sans'),heading(893,579,349,89,'디지털·AI',82,bright,'Black Han Sans'),heading(893,675,350,74,'무료교육 안내',66,blue,'Black Han Sans'),...dots(893,757,352),IC(900,781,23,23,'SquareCheck',bright),text(930,782,123,31,'신청 및 문의',23,'#111',700),text(1055,782,192,31,'미리구청 평생교육과',23),heading(904,855,337,38,'전화문의 02-000-0000',26,'#fff')
];
p['l57/s02'].removeText=[R(0,0,1280,909)];p['l57/s02'].clearShapes=true;p['l57/s02'].elements=[B(427,0,426,909,bright),
 text(33,74,364,136,'안녕하세요.\n미리구청 평생교육과\n입니다.',43,blue,700),text(33,245,369,31,'스마트폰 때문에 불편하셨던 적 있으시죠?',23,'#000',700),text(33,291,365,51,'카카오톡, 유튜브, 지피티, 키오스크...\n이제 함께 배워요!',19),B(34,395,360,529,'#fafcfe',{border:'5px solid #303030',radius:35}),C(29,365,251,54,'이런분께 추천드려요',28,bright,{color:'#fff',radius:30,font:'Jua'}),
 ...['스마트폰 사용이 서툰 어르신','무인 키오스크가 어려우신 분','AI·인터넷 검색이 낯선 분','자녀와 영상통화 하고 싶은 분'].flatMap((t,i)=>[IC(69,461+i*47,22,25,'SquareCheck',bright),text(101,465+i*47,269,33,t,21,blue,700)]),...dots(65,645,296),text(71,670,301,34,'수강료는 전액 무료입니다',27,bright,700),text(72,715,303,29,'*미리구 주민 누구나 신청가능',21),
 heading(496,71,294,55,'교육 과정 소개',42,'#fff','Black Han Sans'),heading(960,71,244,55,'교육 일정표',42,blue,'Black Han Sans'),
 ...['스마트폰 기초반','AI 생활 체험반'].flatMap((t,i)=>[B(466,146+i*372,350,351,ice,{radius:32}),text(601,203+i*372,200,41,t,30,blue,700),...['대상','내용','일정','장소'].flatMap((a,j)=>[text(497,295+i*372+[0,39,107,147][j],42,31,a,21,blue,700),text(539,295+i*372+[0,39,107,147][j],257,j===1?65:41,[['스마트폰을 처음 사용하시는 분','전화·문자 보내기, 카카오톡 설치\n및 사용법','매주 화요일 오전 10시','미리 종합복지관 2층 교육실'],['스마트폰 기본 사용 가능한 분','AI 음성 비서 사용, 챗봇 대화,\n자동 번역','매주 목요일 오후 2시','미리 평생학습관 1층 미디어실']][i][j],20,blue)])]),
 C(879,145,377,51,'2080 하반기 교육 일정',29,blue,{color:'#fff',radius:30,font:'Jua'}),C(878,620,378,50,'공통 안내',27,blue,{color:'#fff',radius:30,font:'Jua'}),B(879,670,377,149,'#fff'),
 ...['수강료   전액 무료','교재 및 실습 기기 제공','보조 강사 1:1 도움 제공'].flatMap((t,i)=>[text(899,692+i*43,333,34,t,22,blue,700),...(i<2?dots(898,722+i*43,336):[])]),text(916,845,340,34,'⚠ 정원 마감 시 조기 마감될 수 있습니다.',20,bright,700)
];
const widths=[101,77,126,73],starts=[879,980,1057,1183];
add('l57/s02',[
 ...['과정명','운영기간','요일·시간','접수마감'].map((t,j)=>C(starts[j],196,widths[j],54,t,22,bright,{color:'#fff',radius:0,font:'Jua'})),
 ...scheduleBlue.flatMap((row,i)=>row.flatMap((t,j)=>[B(starts[j],250+i*86,widths[j],86,i%2?'#f8f8f8':'#fff'),T(starts[j]+2,268+i*86,widths[j]-4,63,t,21,{align:'center',lineHeight:1.5,color:j===3?bright:blue,weight:j===0||j===3?700:400})]))
]);
p['l58/s01'].removeText=[R(0,0,1280,909)];p['l58/s01'].clearShapes=true;p['l58/s01'].elements=[
 text(455,606,372,153,'MIRI.KIM\nGALLERY',78,'#e7e7e7'),
 text(30,44,365,33,'ARTIST',24,'#999',700),text(30,97,171,66,'김 미리',46,'#000',700),text(174,128,226,30,'MIRI KIM',17),text(30,168,373,52,'일상의 익숙한 풍경과 그 안에 남겨진 감정을\n회화와 오브제를 통해 기록합니다.',18),...dots(29,242,366),
 ...['오후의 창','머무는 빛','조용한 정원'].flatMap((t,i)=>[text(30,286+i*101,26,26,`0${i+1}`,15),text(59,279+i*101,128,37,t,23,'#000',600),text(i===2?166:153,289+i*101,225,24,['Afternoon Window','Light That Stays','Quiet Garden'][i],13,'#4fb8c5'),text(59,312+i*101,200,40,['72.7 × 60.6 cm','90.9 × 72.7 cm','65.1 × 53.0 cm'][i]+'\nOil on canvas, 2099',13,'#777')]),
 ...dots(30,781,364),text(30,819,358,66,'2099   김미리 개인전\n2098   비즈아트페어 참여\n2097   비즈대학교 조형예술학과 졸업',13,'#888'),
 text(457,44,365,33,'INFO',24,'#999',700),text(457,98,350,66,'관람 안내',46,'#000',700),text(457,168,370,52,'일상의 익숙한 풍경과 그 안에 남겨진 감정을\n회화와 오브제를 통해 기록합니다.',18),...dots(457,242,364),
 text(457,287,50,29,'일시',16),text(514,279,217,36,'2099. 10. 18 – 11. 16',25,'#000',700),text(728,290,99,24,'10:00 – 18:00',13,'#4fb8c5'),text(457,326,50,29,'장소',16),text(514,318,110,36,'미리갤러리',25,'#000',700),text(622,328,141,24,'매주 월요일 휴관',13,'#4fb8c5'),text(457,368,50,29,'관람료',16),text(514,357,186,37,'무료 관람',25,'#000',700),...dots(457,781,365),
 text(457,819,281,69,'장소    서울시 미포구 비즈로 123\n문의    02-1234-5678\nSNS    @miri_gallery',13,'#888'),
 T(881,33,374,158,'MIRI.KIM\nGALLERY',78,{font:'Inter',weight:400,lineHeight:1.03}),text(883,203,369,37,'2099 KIM MIRI EXHIBITION',25),...dots(882,242,368),...dots(882,781,368),IC(889,806,21,21,'Clock','#4fb8c5'),text(921,800,249,41,'10.18 - 11.16',35),IC(889,848,23,26,'MapPin','#4fb8c5'),text(921,845,248,39,'MIRI GALLERY',32)
];
for(const e of p['l58/s02'].elements??[])if(e.text?.startsWith('“익숙한'))e.fontStyle='italic';
const wm=p['l58/s02'].elements!.find(e=>e.text==='MIRI.KIM\nGALLERY');if(wm){p['l58/s02'].elements=p['l58/s02'].elements!.filter(e=>e!==wm);p['l58/s02'].elements!.unshift(wm)}
const teal='#18b5b1',tealPale='#60c9c6',sun='#fffba3';
p['l59/s01'].removeText=[R(0,0,1280,909)];p['l59/s01'].clearShapes=true;p['l59/s01'].elements=[B(850,0,430,909,tealPale),B(47,132,363,777,'#fff'),IC(49,65,81,66,'House',tealPale),heading(138,79,204,38,'미리요양원 소개',32,'#fff','Jua'),
 T(63,320,332,88,'어르신을 가족처럼 모시는 미리요양원입니다.\n신체 기능과 건강 상태는 물론 정서적 안정과 일상의\n즐거움까지 세심하게 살피며, 보호자께서도 안심하실\n수 있는 돌봄 환경을 만들어갑니다.',15,{align:'center',lineHeight:1.4,color:'#555'}),
 ...['01. 개인별 맞춤 돌봄','02. 전문적인 건강 관리','03. 균형 잡힌 식생활','04. 신체 기능 유지 지원'].flatMap((t,i)=>[C(i%2?70:207,423+i*95,183,39,t,20,teal,{color:'#fff',radius:12,font:'Jua'}),C(70,468+i*95,320,39,['어르신의 건강 상태와 생활 습관을 고려한 맞춤 케어','간호 인력의 건강 상태 확인 및 투약·복약 관리','어르신의 건강 상태를 고려한 식단과 간식 제공','개인별 상태에 맞춘 운동 및 기능 유지 프로그램'][i],14,'#eee',{radius:15,weight:400,color:'#555'})]),
 T(83,815,300,49,'편안한 하루가 모여\n행복한 노후가 될 수 있도록 함께하겠습니다.',15,{align:'center',lineHeight:1.5,color:'#666'}),heading(466,94,189,43,'오시는 길',34,'#fff','Jua'),
 ...[['주소','미리시 미리구 미리로 16-8 미리빌딩 2~4층',169],['지하철','미리역 2번 출구 도보 약 7분',273],['버스','미리요양원 정류장 하차 후 도보 약 3분',306],['간선버스','101, 105, 120',339],['지선버스','2011, 2213',372],['자가용\n이용 시','미리사거리에서 비즈공원 방향 약 300m\n건물 지하주차장 이용 가능',430]].flatMap(([a,b,y])=>[text(466,y as number,77,47,a as string,16,sun,700),text(538,y as number,279,51,b as string,16,'#fff'),L(466,(y as number)+(a==='자가용\n이용 시'?49:26),347,1,'#9ad5bb')]),text(466,231,256,30,'대중교통',21,sun,700),
 B(466,507,347,136,'#fff',{radius:13}),L(501,563,273,13,'#eaeaea'),...[567,630,696].map(x=>B(x,517,13,116,'#eaeaea',{radius:9})),B(598,597,28,21,'#e5e5e5'),B(690,558,24,24,'transparent',{border:'2px solid #18b5b1',radius:'50%'}),text(466,670,321,31,'입소 및 상담 안내',21,sun,700),
 ...['평일','토요일','입소상담','홈페이지'].flatMap((t,i)=>[text(466,710+i*33,79,28,t,16,sun,700),text(538,710+i*33,277,28,['09:00~18:00','09:00~13:00','02-345-6789','www.miricare.example'][i],16,'#fff',600),L(466,733+i*33,347,1,'#9ad5bb')]),
 text(1140,67,126,28,'미리요양원',20,'#fff',700),text(885,156,330,31,'MIRI SENIOR CARE',22,sun,600),text(885,185,330,42,'마음까지 돌보는',28,'#fff',700),text(885,226,374,90,'미리요양원',68,sun,700),IC(885,350,23,23,'Heart',sun),text(916,351,345,31,'장기요양기관 · 24시간 돌봄 서비스',22,'#fff',700),IC(886,382,23,23,'Phone',sun),text(916,383,345,31,'입소 상담 02-345-6789',22,'#fff',700),text(887,441,344,59,'사랑과 정성으로 함께하는\n어르신의 편안한 일상',18,'#fff',600)
];
p['l59/s02'].removeText=[R(0,0,1280,909)];p['l59/s02'].clearShapes=true;p['l59/s02'].elements=[B(850,0,430,909,'#fff'),B(62,223,339,156,'#fff',{radius:20}),
 C(58,69,337,58,'입소 안내',32,'#fff',{color:teal,radius:45,font:'Jua'}),C(455,68,368,58,'시설 소개',32,'#fff',{color:teal,radius:45,font:'Jua'}),C(881,69,365,58,'프로그램 & 서비스',32,teal,{color:'#fff',radius:45,font:'Jua'}),
 IC(60,149,20,22,'UserRound','#fff'),text(85,150,245,33,'입소 대상',27,'#fff',700),text(61,201,335,25,'다음과 같은 어르신의 입소 상담이 가능합니다.',15,'#fff',600),
 ...['치매·뇌혈관성 질환 등으로 일상생활에 도움이 필요','거동이 불편하여 지속적인 돌봄이 필요','보호자의 부재 또는 돌봄 여건으로 장기간 보호가 필요','식사·위생·복약 등 일상생활 전반에 도움이 필요','사회적 고립이나 정서적 돌봄이 필요'].flatMap((t,i)=>[IC(85+i%2*30,239+i*28,17,19,['Hand','Accessibility','House','Utensils','Heart'][i],tealPale),text(110+i%2*30,241+i*28,273,24,t,14,'#333')]),
 text(130,394,276,23,'※ 정확한 입소 가능 여부는 상담을 통해 확인해 주세요.',12,'#fff',600),text(81,447,284,33,'입소 절차',25,'#fff',700),L(66,500,1,149,sun),
 ...['전화 및 방문 상담','장기요양등급 및 입소 가능 여부 확인','시설 방문 및 생활환경 안내','입소일 결정 및 구비서류 준비','계약서 작성 및 입소'].flatMap((t,i)=>[B(59,493+i*37,15,15,sun,{radius:'50%'}),text(85,492+i*37,73,29,`STEP 0${i+1}`,16,'#fff',700),text(168,494+i*37,237,29,t,15,'#fff',600)]),
 text(80,700,285,32,'입소 시 준비서류',25,'#fff',700),...['장기요양인정서','처방전 및 복용 중인 약 목록','개인별 장기요양 이용계획서','어르신 및 보호자 신분증','의사소견서 또는 건강진단서','가족관계증명서'].map((t,i)=>C(59+(i%2)*180,750+Math.floor(i/2)*34,174,28,t,14,sun,{color:teal,weight:600,radius:20})),
 text(480,149,340,32,'쾌적하고 안전한 생활환경',24,'#fff',700),text(455,199,371,52,'어르신의 이동과 생활 편의를 고려한 공간을 마련하여 보다 안전\n하고 편안하게 생활하실 수 있도록 합니다.',15,'#fff',600),L(455,253,4,170,sun),L(455,441,4,171,sun),text(472,257,64,31,'생활실',23,'#fff',700),text(539,259,280,30,'밝고 쾌적한 생활공간',15,'#fff',600),text(472,447,91,31,'프로그램실',23,'#fff',700),text(572,449,247,30,'인지·여가 프로그램을 위한 공동생활공간',15,'#fff',600),text(617,618,211,25,'*페이지 내 인물 사진은 샘플 이미지입니다.',11,'#fff'),text(480,642,340,34,'장기요양 인정 신청',25,'#fff',700),
 ...['국민건강보험\n공단 신청','방문조사 및\n등급판정','장기요양\n인정서 발급','양원 입소 상담\n및 계약'].flatMap((t,i)=>[B(456+i*97,682,78,78,'#48d4bc',{radius:'50%'}),IC(479+i*97,703,33,38,['Stethoscope','Search','FileText','Handshake'][i],'#fff'),T(453+i*97,779,87,49,t,14,{color:'#fff',align:'center',lineHeight:1.4})]),T(455,823,371,44,'※ 장기요양등급 및 급여 종류에 따라 이용 가능한 서비스와\n본인부담금이 달라질 수 있습니다.',12,{color:'#fff',align:'right',lineHeight:1.5}),
 ...['간호·건강관리 서비스','신체기능 지원','인지·정서 프로그램','일상생활 지원'].flatMap((t,i)=>{const colors=['#00c79a','#55d7aa','#a0d7a5','#76c6b2'],ys=[146,354,527,700];return [C(885,ys[i],29,29,`0${i+1}`,16,colors[i],{color:'#fff',radius:'50%'}),text(922,ys[i]+4,300,34,t,23,colors[i],700),...dots(921,ys[i]+29,296),text(922,ys[i]+43,302,61,['어르신의 건강 상태를 지속적으로 확인하여 안전하고\n편안한 생활을 지원합니다.','개인의 신체 상태와 잔존 기능을 고려하여 일상생활\n능력을 유지할 수 있도록 돕습니다.','즐거운 활동을 통해 인지 기능을 자극하고 정서적으로\n안정된 생활을 지원합니다.','편안하고 청결한 일상을 위해 어르신의 일상생활\n전반을 세심하게 지원합니다.'][i],16,'#555'),...[0,1,2,3].map(j=>C(923+(j%2)*148,ys[i]+105+Math.floor(j/2)*34,141,28,[['혈압·체온·혈당 등 기본 건강 상태 확인','복약 및 투약 관리','건강 상태 변화 관찰','정기적인 건강 상담'],['관절 운동 및 스트레칭','보행 및 균형 유지 훈련','일상생활 동작 훈련','개인별 신체활동 지원'],['미술·색칠 활동','퍼즐 및 기억력 활동','음악 감상 및 노래교실','생신잔치 및 계절 행사'],['식사 및 간식 지원','세면·목욕·위생관리','의복 및 침구 관리','이동 및 생활 보조']][i][j],14,colors[i],{color:'#fff',radius:20}))]})
];
// First service has a full-width introductory pill, then two-column detail rows.
const service=p['l59/s02'].elements!;service.filter(e=>e.chip&&e.y===251).forEach(e=>{if(e.x===923){e.w=296;e.text='혈압·체온·혈당 등 기본 건강 상태 확인'}else e.text='복약 및 투약 관리'});
p['l59/s02'].elements=p['l59/s02'].elements!.filter(e=>!(e.chip&&[251,285].includes(e.y)));
for(const e of p['l59/s02'].elements??[]){if(e.chip&&e.x>=923&&e.y>=459)e.y-=17;if(e.kind==='text'&&e.y>=241&&e.y<=353&&e.x<427){e.size=12;e.w=294}}
add('l59/s02',[C(923,238,296,28,'혈압·체온·혈당 등 기본 건강 상태 확인',14,'#00c79a',{color:'#fff',radius:20}),...['복약 및 투약 관리','건강 상태 변화 관찰','정기적인 건강 상담','협력 의료기관 진료 연계'].map((t,i)=>C(923+(i%2)*148,271+Math.floor(i/2)*34,141,28,t,14,'#00c79a',{color:'#fff',radius:20}))]);
const youthYellow='#ffd346',youthCyan='#19bed4',hand='Single Day';
p['l60/s01'].removeText=[R(0,0,1280,909)];p['l60/s01'].clearShapes=true;p['l60/s01'].elements=[B(427,0,423,909,'#fff'),B(850,810,430,99,'#fff'),
 heading(137,83,259,33,'비즈청소년재단이 추구하는',20,'#fff'),heading(136,117,236,54,'✦ 핵심가치 ✦',43,'#111',hand),
 ...['자립','성장','동행'].flatMap((t,i)=>[C(55,330+i*228,79,57,t,20,youthCyan,{color:'#fff',border:'1px solid #111',radius:18,font:hand}),IC(82,336+i*228,27,21,['Sprout','ChartNoAxesCombined','Users'][i],'#fff'),C(143,330+i*228,259,57,['청소년이 스스로 삶을 선택하고 책임지는\n주체로 성장하도록 돕습니다.','다양한 경험과 도전의 기회를 통해\n자신의 가능성을 발견하도록 지원합니다.','지역사회와 함께 청소년의 곁을 지키는\n든든한 동행이 되어줍니다.'][i],14,'#fff',{color:'#555',border:'1px solid #111',radius:18,lineHeight:1.35,weight:400})]),text(55,853,350,23,'*페이지 내 인물 사진은 샘플 이미지입니다.',12,'#fff'),
 T(534,375,214,82,'꿈꾸고 도전하며\n스스로 일어서다.',32,{font:hand,align:'center',lineHeight:1.3}),text(482,660,314,35,'비즈청소년재단',27,'#000',600),IC(455,658,24,29,'Bird',youthCyan),L(455,700,371,1,'#f7ce63'),
 ...['주소','후원계좌','이메일','홈페이지','SNS'].flatMap((t,i)=>[text(455,718+i*29,81,26,t,17,'#e6bf53',700),text(525,718+i*29,303,26,['강원특별자치도 비즈시 비즈로 36','비즈은행 123-456-789012 (비즈청소년재단)','bizyouth@example.com','bizyouth.or.kr','@biz_youth'][i],16,'#555')]),
 text(1067,64,200,30,'BIZ Youth Foundation',18),...['★','★','★'].map((t,i)=>text(891+i*47,132,26,29,t,22)),T(879,160,367,132,'꿈꾸고 도전하며\n스스로 일어서다.',56,{font:hand,color:'#000',lineHeight:1.27}),text(879,321,366,58,'청소년의 건강한 자립을 위해\n당신의 후원을 기다립니다.',22,'#000',600),heading(1000,832,239,36,'비즈청소년재단',27,'#000',hand),IC(974,830,23,30,'Bird',youthCyan)
];
p['l60/s02'].removeText=[R(0,0,1280,909)];p['l60/s02'].clearShapes=true;p['l60/s02'].elements=[B(0,0,429,161,youthYellow),B(429,0,422,161,'#83cbc5'),B(851,0,429,161,youthCyan),
 ...[64,459,886].map(x=>B(x,87,334,62,'#fff',{radius:50})),...[[129,youthYellow],[489,'#83cbc5'],[922,youthCyan],[335,youthYellow],[795,'#83cbc5'],[1170,youthCyan]].flatMap(([x,c])=>[L(x as number,0,2,101,'#777'),B((x as number)-5,93,12,12,c as string,{radius:'50%'})]),
 ...['지원 서비스','후원이 만드는 변화','함께해주세요'].map((t,i)=>C([66,460,886][i],88,333,57,t,i===1?43:47,'transparent',{font:hand,radius:50,weight:400})),
 text(73,181,324,62,'자립준비청년(또는 청년·취약계층)이 사회에 안착하고 스스로\n삶을 일구어 갈 수 있도록 주거·생계·진로 등 생활 전반을 통합\n적으로 보살피는 맞춤형 종합 지원 체계입니다.',13),text(456,181,374,62,'단순한 시혜적 지원을 넘어, 한 아이의 삶이 긍정적으로 변화하고\n홀로서기에 성공하기까지 지속적인 연대가 필요한 사람들에게\n메시지를 담고 있습니다.',13),text(868,181,367,63,'여러분의 작은 관심과 나눔이 누군가에게는 큰 힘이 됩니다.\n정기후원, 일시후원, 물품후원 등 다양한 방법으로 따뜻한 마음을 나눠\n주세요. 여러분과 함께 더 나은 내일을 만들어가겠습니다.',13),
 ...['주거지원','자립지원','진로지원','맞춤형 사례관리'].flatMap((t,i)=>[C(62,255+i*152,334,30,`   ${t}`,19,youthYellow,{border:'1px solid #111',radius:18,align:'left',font:hand,weight:400}),text(366,261+i*152,29,21,`0${i+1}`,14,'#fff'),IC(77,262+i*152,20,17,['House','BookOpen','BriefcaseBusiness','MessagesSquare'][i],'#80562d'),...['월세 지원','주거 관련 정보 제공','이사 지원'].map((_,j)=>C(222,292+i*152+j*35,174,31,[['월세 지원','주거 관련 정보 제공','이사 지원'],['생필품·의료비 지원','심리상담','학비·교재비 지원'],['취업정보 제공','면접 복장 대여','직업체험 프로그램'],['월 1회 대면 상담','자립계획 수립','실행 모니터링']][i][j],17,'#fff',{border:'1px solid #edc34c',radius:10,color:'#333'}))]),
 text(62,858,350,23,'*페이지 내 인물 사진은 샘플 이미지입니다.',11,'#555'),
 ...['위기 청소년 발굴','상담 및 지원계획 수립','맞춤형 지원','홀로서기, 그리고 동행'].flatMap((t,i)=>{const x=452+(i%2)*192,y=258+Math.floor(i/2)*298;return [B(x,y,183,286,'#fff',{border:'1px solid #111',radius:9}),heading(x+10,y+181,163,23,`0${i+1}`,16,'#59b3be'),heading(x+5,y+200,173,31,t,21,'#59b3be',hand),T(x+13,y+227,156,58,['도움이 절실하지만\n복지 사각지대에 놓여 있는 청소년을\n선제적으로 찾아냅니다.','아이마다 처한 상황이 다르므로,\n1:1 대면 상담을 통해 효과적인 자립\n목표와 로드맵을 함께 세웁니다.','주거 안정, 생필품·심리 지원, 진로\n탐색 등 삶의 전반에 걸쳐 필요한\n솔루션을 다각도로 제공합니다.','밀착케어를 통해 청소년이\n자립 기반을 갖추고 사회의 건강한\n구성원으로 당당히 서게 됩니다.'][i],12,{align:'center',lineHeight:1.4})]}),
 ...['정기후원','일시후원','물품후원'].flatMap((t,i)=>[B(875,261+i*174,348,160,'#effaff',{border:'1px solid #111',radius:20}),C(897,278+i*174,306,31,t,23,youthCyan,{border:'1px solid #111',radius:20,font:hand,weight:400}),text(995,329+i*174,211,100,['작은 나눔이 매일 이어지면 더 큰\n변화를 만들어낼 수 있습니다.\n정기적인 후원으로 따뜻한 마음을\n꾸준히 전해주세요.','한 번의 따뜻한 마음도 소중한\n나눔이 됩니다.\n도움이 필요한 순간, 원하는 때에\n따뜻한 마음을 전해주세요.','생활에 꼭 필요한 생필품과 학용품 등\n필요한 물품을 직접 나누어 주세요.\n작은 물품 하나하나가 도움이 필요한 이웃\n의 일상에 따뜻한 힘이 될 수 있습니다.'][i],13)]),
 ...['블로그','SNS','후원신청'].map((t,i)=>text(947+i*114,834,67,28,t,14,['#89b85e','#ee999d',youthCyan][i],600))
];
// Typography refinements preserve individual colored lines and original hierarchy.
p['l57/s02'].elements=p['l57/s02'].elements!.filter(e=>e.text!=='안녕하세요.\n미리구청 평생교육과\n입니다.');
add('l57/s02',[T(33,74,364,139,'안녕하세요.\n\n입니다.',43,{font:'Black Han Sans',weight:400,color:blue,lineHeight:1.2}),T(33,124,372,56,'미리구청 평생교육과',42,{font:'Black Han Sans',weight:400,color:bright,letterSpacing:-1})]);
for(const e of p['l57/s02'].elements??[])if(['스마트폰 기초반','AI 생활 체험반'].includes(e.text??''))e.size=28;
for(const e of p['l52/s02'].elements??[])if(e.kind==='box'&&e.x===430&&e.h===909)e.fill='#e5e5e5';
for(const e of p['l60/s01'].elements??[])if(['자립','성장','동행'].includes(e.text??'')){e.h=30;e.y+=25}
add('l49/s01',[B(442,741,396,130,'#ffe349'),...[265,367,470,572].flatMap(y=>dots(54,y,330))]);add('l49/s02',[...[339,528].flatMap(y=>dots(897,y,335))]);
for(const e of p['l49/s01'].elements??[])if(e.text==='청년 농업인\n맞춤 컨설팅 상담'){e.x=688;e.w=112;e.size=14}
for(const e of p['l49/s02'].elements??[])if(e.chip&&e.y===106)e.border='1px solid #777';
for(const e of p['l51/s01'].elements??[]){
 if(e.text==='GREETING'){e.size=20;e.x=163;e.w=131}
 if(e.text?.startsWith('오늘 이 자리에')){e.size=19;e.letterSpacing=-.3;e.lineHeight=1.7}
 if(e.text==='공연 안내'){e.x=160;e.w=133;e.size=18}
 if(e.text==='찾아오시는 길'){e.x=549;e.w=220;e.size=24}
 if(e.text==='서울특별시 비즈구 비즈로 123\n비즈아트센터 2F'){e.x=535;e.w=250;e.size=14;e.lineHeight=1.8}
 if(e.text==='비즈시 비즈구 비즈로 123 비즈홀'){e.size=13;e.w=209}
 if(e.text==='비즈역 3번 출구에서\n도보 약 5분'){e.size=12;e.w=112;e.x=486}
 if(e.text==='비즈아트센터 정류장\n123·456·7890번'){e.size=12;e.w=116;e.x=602}
 if(e.text?.startsWith('공연 당일 주변 교통이')){e.size=14;e.x=501;e.w=309;e.lineHeight=1.75}
 if(e.text==='2090. 7. 12. SAT. PM 5:00'){e.size=23;e.w=310;e.x=920;e.weight=400}
 if(e.text==='MUSICAL PERFORMANCE'){e.size=14}
 if(e.text==='BIZ CONCERT CHAMBER'){e.size=13;e.x=1064;e.w=180;e.weight=400}
 if(['2090','BIZ HALL'].includes(e.text??''))e.weight=400;
}
for(const e of p['l51/s02'].elements??[]){
 if(e.text==='PROGRAM\nNOTE'){e.x=527;e.w=226;e.size=35;e.lineHeight=1.2}
 if(e.text==='CHARACTER'){e.size=37;e.y=142;e.letterSpacing=-.3}
 if(e.text==='PROFILE'){e.size=37;e.y=190}
 if(e.text?.startsWith('고요한 도시의 끝자락')){e.x=879;e.w=316;e.size=12.4;e.lineHeight=2.03}
 if(e.text?.startsWith('G. VERDI —')){e.x=872;e.w=324;e.size=11.6;e.lineHeight=2.05}
 if(e.text==='* INTERMISSION *'){e.size=15;e.y=621}
 if(e.text?.startsWith('G. DONIZETTI —')){e.x=880;e.w=317;e.size=11.6;e.lineHeight=2.02}
}
p['l52/s01'].elements!.unshift(B(427,0,423,909,'#fff'));
for(const e of p['l52/s01'].elements??[]){
 if(e.text==='전통의 맛을 담아\n정성을 전합니다.')e.h=103;
 if(e.text==='전통의 가치를 담아\n소중한 분께 감사의 마음을 전하세요.'){e.size=16;e.lineHeight=1.65;e.h=58}
 if(e.text?.startsWith('좋은 재료와 정직한')){e.size=17;e.lineHeight=1.5}
 if(e.font==='Tinos'||['비즈특별시 한과로 123','1588-1234'].includes(e.text??''))e.weight=400;
}
for(const e of p['l52/s02'].elements??[]){
 if(e.text?.startsWith('정성을 다해 만든')){e.y=485;e.size=19;e.lineHeight=1.58;e.h=345}
 if(e.text?.match(/^(39|59|89),000원/)){e.font='Tinos';e.size=19;e.weight=400;e.w=149}
 if(e.text==='HACCP 인증 시설 생산'){e.size=17;e.w=200}
}
// Source octagonal photo mask and octagonal service-icon frames.
p['l52/s02'].underTextElements=[P([[89,200],[124,200],[89,235]],paper,0,paper),P([[304,200],[339,200],[339,235]],paper,0,paper),P([[89,414],[89,449],[124,449]],paper,0,paper),P([[304,449],[339,414],[339,449]],paper,0,paper)];
p['l52/s01'].elements=p['l52/s01'].elements!.filter(e=>!(e.kind==='box'&&e.w===120&&[76,233].includes(e.x)));
add('l52/s01',[...[0,1,2,3].map(i=>{const x=76+i%2*157,y=144+Math.floor(i/2)*222;return P([[x+35,y],[x+85,y],[x+120,y+35],[x+120,y+85],[x+85,y+120],[x+35,y+120],[x,y+85],[x,y+35]],'#cfb790',2,'#fff3da')})]);
add('l50/s01',[P([[654,144],[675,144],[664,154]],'#fff',0,'#fff'),P([[558,239],[579,239],[569,251]],lime,0,lime),P([[695,334],[715,334],[706,345]],'#fff',0,'#fff')]);
add('l50/s02',[...[76,341,503,768].map(x=>B(x,230,8,32,'#fff',{border:'1px solid #a6bc66',radius:3}))]);
for(const e of p['l53/s01'].elements??[])if(['스마트팜','더 쉽게 시작하기','스마트팜·친환경 농업 기술\n컨설팅 프로그램'].includes(e.text??''))e.weight=400;
p['l53/s01'].underTextElements=[B(1204,0,47,97,'#f3f4dc'),P([[1204,97],[1251,97],[1251,133]],'#f3f4dc',0,'#f3f4dc'),P([[883,488],[977,488],[1013,535],[883,535]],'#f3f4dc',0,'#f3f4dc')];
p['l53/s02'].underTextElements=[P([[711,325],[735,284],[823,284],[823,325]],'#f3f4dc',0,'#f3f4dc')];
p['l54/s01'].elements=p['l54/s01'].elements!.filter(e=>e.text!=='TECHNOLOGIES\nWE COVER'&&e.text!=='SMART\nFARM');
p['l54/s02'].elements=p['l54/s02'].elements!.filter(e=>!['RECOMMENDED\nFOR','CONSULTING\nPROGRAMS','HOW IT\nWORKS'].includes(e.text??''));
const exactEnglish=(x:number,y:number,w:number,h:number,t:string)=>T(x,y,w,h,t,36,{font:'Montserrat',weight:500,inkFit:true,color:'#000'});
add('l54/s01',[exactEnglish(46,49,264,27,'TECHNOLOGIES'),exactEnglish(46,95,179,27,'WE COVER'),exactEnglish(936,128,266,59,'SMART'),exactEnglish(962,211,227,59,'FARM'),B(455,497,370,77,'transparent',{border:'1px dotted #aaa'})]);
add('l54/s02',[exactEnglish(46,49,285,27,'RECOMMENDED'),exactEnglish(46,95,69,27,'FOR'),exactEnglish(474,49,238,27,'CONSULTING'),exactEnglish(474,95,206,27,'PROGRAMS'),exactEnglish(904,49,115,27,'HOW IT'),exactEnglish(904,95,126,27,'WORKS')]);
for(const e of p['l54/s02'].elements??[]){
 if(e.text===agriBullets[1])e.text='- 작물·운영 기술 제안\n- 도입 우선순위 설계\n- 재배·운영 방향 정리';
 const index=agriRecBody.indexOf(e.text??'');if(index>=0&&e.x<427)e.text=['어떤 설비부터 시작해야 할지\n막막한 경우','운영 기준과 적용 방법이\n필요한 경우','기술 기반 농업 운영 방향을\n배우고 싶은 경우','현재 시설과 재배 흐름을\n점검하고 싶은 경우'][index];
 if(e.text==='현장 또는 비대면 방식으로 솔루션 안내'&&e.x>1000)e.text='현장 또는 비대면 방식으로\n솔루션 안내';
}
p['l55/s01'].elements=p['l55/s01'].elements!.filter(e=>!(e.kind==='icon'&&e.icon==='Triangle'));
add('l55/s01',[...[428,568,708].map(y=>P([[102,y],[122,y],[112,y+15]],'#ccc',0,'#ccc'))]);
p['l55/s01'].underTextElements=[B(893,518,65,52,cyan,{radius:10})];
p['l55/s02'].elements=p['l55/s02'].elements!.filter(e=>e.text!=='미리구 주민이라면\n수강료 100% 전액 무료');
add('l55/s02',[heading(69,784,308,34,'미리구 주민이라면',29,charcoal,'Jua'),heading(69,815,308,34,'수강료 100% 전액 무료',29,'#fff','Jua')]);
for(const key of ['l56/s01','l56/s02'])for(const e of p[key].elements??[]){if(e.text==='Festival')e.weight=600;if(['Contact','Event'].includes(e.text??''))e.weight=600;if(e.text==='Autumn')e.weight=500;if(e.text==='Special Guest')e.weight=500}
add('l56/s01',[IC(53,549,18,23,'MapPin',orange),IC(53,772,17,20,'BusFront',orange),IC(53,803,17,20,'TrainFront',orange),IC(53,834,17,20,'CarFront',orange),P([[216,590],[264,674]],'#f5edcf',12),P([[52,723],[191,679]],'#f5edcf',10)]);
for(const e of p['l56/s01'].elements??[])if(e.text?.startsWith('대중교통 이용')||e.text?.startsWith('지하철 이용')||e.text?.startsWith('자가용 이용')){e.x=75;e.w=305;e.size=14}
add('l56/s02',[...[331,715].flatMap(y=>dots(478,y,320)),...Array.from({length:112},(_,i)=>B(635,186+i*6,1,2,olive))]);
p['l56/s02'].elements=p['l56/s02'].elements!.filter(e=>!['Music Stage','Time Table','Special Guest'].includes(e.text??''));
add('l56/s02',[T(64,45,141,55,'Music',50,{font:'Figtree',weight:400,color:orange}),T(205,45,151,55,'Stage',50,{font:'Figtree',weight:600,color:orange}),T(90,484,120,55,'Time',50,{font:'Figtree',weight:600,color:orange}),T(210,484,138,55,'Table',50,{font:'Figtree',weight:400,color:orange}),T(913,524,166,56,'Special',48,{font:'Figtree',weight:600,color:orange}),T(1076,524,158,56,'Guest',48,{font:'Figtree',weight:400,color:orange})]);
// Second comparison corrections: preserve single-line native ink bounds.
for(const e of p['l57/s01'].elements??[]){
 if(e.text==='02-000-0000'){e.x=596;e.w=215;e.h=36;e.inkFit=true}
 if(e.text==='edu@miri.go.kr'){e.x=654;e.w=158;e.size=22;e.h=31;e.letterSpacing=-.4}
 if(e.text==='월~금 09:00~18:00'){e.x=610;e.w=204;e.h=29;e.size=22;e.inkFit=true}
 if(e.text==='무료교육 안내'){e.y=676;e.w=350;e.h=57;e.inkFit=true}
}
for(const e of p['l57/s02'].elements??[])if(e.text==='스마트폰 때문에 불편하셨던 적 있으시죠?'){e.size=21;e.letterSpacing=-.35;e.w=373}
for(const key of ['l58/s01','l58/s02'])for(const e of p[key].elements??[]){
 if(e.text==='MIRI.KIM\nGALLERY'&&e.color?.startsWith('#e')){e.font='Inter';e.lineHeight=1.03;e.h=170}
 if(e.text==='2099.10.18–11.16'||e.text==='2099. 10. 18 – 11. 16'){e.size=22;e.w=217;e.h=31;e.inkFit=true}
 if(['ABOUT\nEXHIBITION','ARTIST\nNOTE'].includes(e.text??'')){e.lineHeight=1.2;e.h=108}
}
for(const e of p['l59/s02'].elements??[]){
 if(e.text==='프로그램실'){e.size=22;e.w=100}
 if(e.kind==='text'&&e.x===922&&e.color==='#555'){e.size=14.5;e.lineHeight=1.35;e.h=58;e.w=305}
}
// Long support bars contain left labels and separate right ordinals, rather than centered chips.
p['l60/s02'].elements=p['l60/s02'].elements!.flatMap(e=>{
 if(e.chip&&e.align==='left'&&e.x===62)return [B(e.x,e.y,e.w,e.h,youthYellow,{border:'1px solid #111',radius:18}),T(100,e.y+3,255,24,e.text!.trim(),19,{font:hand,weight:400})];
 if(e.kind==='text'&&e.w===156&&e.h===58){e.size=11;e.w=163;e.h=64;e.lineHeight=1.4}
 return [e];
});
add('l60/s01',[...[330,558,786].map(y=>B(55,y,79,57,youthCyan,{border:'1px solid #111',radius:13}))]);
for(const e of p['l60/s01'].elements??[])if(['자립','성장','동행'].includes(e.text??''))e.fill='transparent';
for(const e of p['l59/s02'].elements??[])if(e.kind==='text'&&e.x===922&&e.color==='#555'){e.size=13.5;e.letterSpacing=-.1}
for(const e of p['l60/s02'].elements??[])if(e.kind==='text'&&e.w===163&&e.h===64){e.size=10;e.w=169;e.x-=3;e.letterSpacing=-.25;e.lineHeight=1.45}
// Parent reserved final-pass findings: enlarge layout bounds without changing glyph styling.
for(const e of p['l56/s01'].elements??[])if(e.text==='Contact'){e.x-=7;e.w+=14}
for(const e of p['l56/s02'].elements??[]){
 if(e.text==='Stage')e.h=69;
 if(e.text==='Time')e.w=125;
 if(e.text==='Table')e.x=220;
 if(e.text==='Special'){e.w=174;e.h=67}
 if(e.text==='Guest')e.x=1091;
}
