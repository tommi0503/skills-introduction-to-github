import type {BrochureDraft,Element} from '../model'
import {T,B,I,C,IC,VP} from '../primitives'
// Coordinates below follow the attached 1600×1236 sheet. The 52px export margin
// is removed once here; the renderer uses the undistorted 1600×1131 paper.
const y=(v:number)=>v-52
const tx=(x:number,yy:number,w:number,h:number,text:string,size:number,extra:Partial<Element>={})=>T(x,y(yy),w,h,text,size,{font:'Noto Sans KR',lineHeight:1.28,...extra})
const bx=(x:number,yy:number,w:number,h:number,fill:string,extra:Partial<Element>={})=>B(x,y(yy),w,h,fill,extra)
const im=(x:number,yy:number,w:number,h:number,label:string,extra:Partial<Element>={})=>I(x,y(yy),w,h,{label,...extra})
const chip=(x:number,yy:number,w:number,h:number,text:string,size:number,fill:string,extra:Partial<Element>={})=>C(x,y(yy),w,h,text,size,fill,{font:'Noto Sans KR',...extra})
const ic=(x:number,yy:number,w:number,h:number,icon:string,color='#111',extra:Partial<Element>={}):Element=>{
 if(icon==='Sparkle'||icon==='Sparkles'){
  const star=(a:number,b:number,c:number,d:number)=>`M${a+c/2} ${b} Q${a+c*.58} ${b+d*.42} ${a+c} ${b+d/2} Q${a+c*.58} ${b+d*.58} ${a+c/2} ${b+d} Q${a+c*.42} ${b+d*.58} ${a} ${b+d/2} Q${a+c*.42} ${b+d*.42} ${a+c/2} ${b} Z`
  const d=icon==='Sparkle'?star(0,0,w,h):star(0,0,w*.58,h*.8)+' '+star(w*.52,h*.22,w*.48,h*.58)
  return VP(x,y(yy),w,h,d,{fill:color,color:'none',strokeWidth:0})
 }
 if(icon==='Dumbbell')return VP(x,y(yy),w,h,'M5 27 L5 42 M12 18 L12 51 L18 51 L18 18 Z M18 31 L51 31 L51 39 L18 39 M51 18 L51 51 L57 51 L57 18 Z M64 27 L64 42',{color,strokeWidth:2.5})
 if(icon==='Leaf')return VP(x,y(yy),w,h,'M27 3 L30 15 L44 8 L38 22 L50 23 L36 30 L43 41 L28 35 L25 50 L22 34 L9 40 L15 28 L0 22 L16 20 L12 8 L23 15 Z',{fill:color,color:'none',strokeWidth:0})
 if(icon==='Paperclip')return VP(x,y(yy),w,h,`M${w*.12} ${h*.15} Q${w*.52} ${-h*.06} ${w*.58} ${h*.2} L${w*.73} ${h*.73} Q${w*.79} ${h*.93} ${w*.53} ${h*.96} Q${w*.34} ${h*.98} ${w*.29} ${h*.77} L${w*.21} ${h*.42}`,{color,strokeWidth:4,rotate:-3})
 return IC(x,y(yy),w,h,icon,color,extra)
}
const path=(x:number,yy:number,w:number,h:number,d:string,extra:Partial<Element>={})=>VP(x,y(yy),w,h,d,extra)
const base=(color='#fff')=>[B(0,0,1600,1131,color)]
const rule=(x:number,yy:number,w:number,color:string,dotted=true)=>bx(x,yy,w,1,'transparent',{border:`${dotted?'1px dotted':'1px solid'} ${color}`})
const mrule=(x:number,yy:number,w:number,color:string)=>bx(x,yy,w,4,'transparent',{border:`4px dotted ${color}`})
const arule=(x:number,yy:number,w:number,color:string)=>bx(x,yy,w,2.5,'transparent',{border:`2.5px dashed ${color}`})
const brush=(x:number,yy:number,w:number,h:number,text:string,size:number,color='#111',extra:Partial<Element>={})=>tx(x,yy,w,h,text,size,{font:'Nanum Brush Script',weight:400,color,lineHeight:1.15,...extra})
const gb=(x:number,yy:number,w:number,h:number,text:string,size:number,color='#111',extra:Partial<Element>={})=>tx(x,yy,w,h,text,size,{font:'Gaegu',weight:700,color,lineHeight:1.2,letterSpacing:-1.7,...extra})
const wave=(x:number,yy:number,w:number,h:number,color:string,reverse=false)=>path(x,yy,w,h,reverse?`M0 0 C${w*.33} ${h*.42} ${w*.5} ${h*.56} ${w} ${h*.12} L${w} ${h} L0 ${h} Z`:`M0 ${h*.14} C${w*.4} 0 ${w*.46} ${h*.82} ${w} 0 L${w} ${h} L0 ${h} Z`,{fill:color,color:'none',strokeWidth:0})
const roundedDiamond=(w:number,h:number)=>`path('M ${w*.5} 0 C ${w*.62} 0 ${w*.65} ${h*.27} ${w*.92} ${h*.43} Q ${w*1.08} ${h*.5} ${w*.92} ${h*.59} C ${w*.65} ${h*.76} ${w*.64} ${h} ${w*.5} ${h} C ${w*.36} ${h} ${w*.35} ${h*.77} ${w*.08} ${h*.59} Q ${-w*.08} ${h*.5} ${w*.08} ${h*.42} C ${w*.35} ${h*.25} ${w*.38} 0 ${w*.5} 0 Z')`
const floralLogo=(x:number,yy:number,color:string,size:number):Element[]=>{
 const d=`M${size*.5} 0 C${size*.29} ${size*.18} ${size*.3} ${size*.27} ${size*.5} ${size*.37} C${size*.7} ${size*.27} ${size*.71} ${size*.18} ${size*.5} 0 Z M${size*.27} ${size*.14} C${size*.07} ${size*.42} ${size*.19} ${size*.52} ${size*.49} ${size*.7} C${size*.25} ${size*.43} ${size*.22} ${size*.38} ${size*.27} ${size*.14} Z M${size*.73} ${size*.14} C${size*.93} ${size*.42} ${size*.81} ${size*.52} ${size*.51} ${size*.7} C${size*.75} ${size*.43} ${size*.78} ${size*.38} ${size*.73} ${size*.14} Z M${size*.09} ${size*.37} C${-size*.04} ${size*.67} ${size*.16} ${size*.76} ${size*.49} ${size*.91} C${size*.21} ${size*.63} ${size*.15} ${size*.61} ${size*.09} ${size*.37} Z M${size*.91} ${size*.37} C${size*1.04} ${size*.67} ${size*.84} ${size*.76} ${size*.51} ${size*.91} C${size*.79} ${size*.63} ${size*.85} ${size*.61} ${size*.91} ${size*.37} Z M${size*.48} ${size*.66} L${size*.52} ${size*.66} L${size*.5} ${size} Z`
 const fs=size*.83,xx=x+size+8
 return[VP(x,y(yy),size,size,d,{fill:color,color:'none',strokeWidth:0}),tx(xx,yy-4,fs*3+8,size,'엔젤릭',fs,{color,weight:700,letterSpacing:-2.4}),tx(xx+fs*3-5,yy-4,fs*2+8,size,'뷰티',fs,{color:color==='#fff'?'#c7e7f0':color,weight:700,letterSpacing:-2.4})]
}

const travelFront:Element[]=[...base('#f8f5ca'),
 gb(46,218,450,190,'감성의 남해,\n활력의 부산,\n청량한 동해로 떠나요',46,'#111',{lineHeight:1.33,letterSpacing:-1.4}),
 tx(46,468,445,120,'바다를 따라, 당신만의 속도로\n남해 · 부산 · 동해\n1박 2일 추천 코스 & 여행 팁',25,{font:'Gowun Dodum',lineHeight:1.55}),
 chip(587,220,207,53,'교통',22,'#00a5b9',{weight:500,color:'#fff',radius:30}),
 tx(587,307,423,104,'남해: 부산/진주에서 차량 2시간\n부산: K00·S00 가능 / 시내 교통 편리\n동해: 강릉역 or 동해선 이용',21,{font:'Gowun Dodum',lineHeight:1.63}),
 chip(587,457,207,53,'문의 및 예약',22,'#00a5b9',{weight:500,color:'#fff',radius:30}),
 tx(587,545,420,70,'전화: 123–456–7890\n홈페이지: www.reallygreatsite.com',22,{font:'Gowun Dodum',lineHeight:1.5}),
 gb(1120,245,430,300,'낭만\n도시\n그리고 힐링',65,'#000',{align:'center',lineHeight:1.55,letterSpacing:-4}),
 path(0,636,1600,547,'M0 0 C390 290 995 489 1600 331 L1600 547 L0 547 Z',{fill:'#00a5b9',color:'none',strokeWidth:0}),
 tx(46,888,430,30,'여행 팁',23,{font:'Gowun Dodum',color:'#fff'}),rule(46,941,438,'#fff'),
 tx(59,977,470,103,'•  감성 산책은 남해/야경은 부산/일출은 동해\n•  여름 인기 지역은 숙소 사전 예약 필수\n•  해안도로 드라이브 코스도 확인하기',21,{font:'Gowun Dodum',color:'#fff',lineHeight:1.62}),
 im(707,809,893,294,'복잡한 바다·교량 일러스트',{clipPath:'polygon(0 53%, 10% 42%, 11% 31%, 19% 28%, 20% 0, 100% 0, 100% 100%, 55% 100%, 46% 90%, 22% 90%, 14% 78%, 0 77%)'}),
 bx(1319,683,135,135,'linear-gradient(#b396d5, #00a5b9)',{radius:'50%',border:'3px solid #262522'}),
 ...[[1013,769],[1116,769],[1188,693],[1253,753],[1490,753],[1556,693]].map(([x,yy])=>ic(x,yy,25,25,'Star','#292722',{fill:'#f5c95d',strokeWidth:2})),
]
const travelBack:Element[]=[...base('#f8f5ca'),bx(533,52,533,1131,'#00a5b9'),
 ...[{x:46,color:'#111',title:'남해',sub:'감성으로 걷는 바다길',quote:'한적한 길 따라\n마음도 쉬어갑니다',body:'000마을: 계단식 논과 푸른 바다의 절경\n00마을: 이국적인 분위기와 감성 카페\n000모래비치: 가족과 연인 모두에게 인기',tags:'추천 키워드: 조용한, 감성, 힐링',ix:80,iw:370,clip:'45% 53% 46% 49% / 60% 57% 42% 39%'},{x:579,color:'#fff',title:'부산',sub:'도시의 리듬, 바다와 함께',quote:'도시와 바다가 만나는\n가장 부산다운 시간',body:'해운대: 부산 대표 해변, 낮과 밤 모두 매력\n00문화마을: 골목을 수놓은 예술\n광안대교: 밤바다의 하이라이트\n000시장: 먹거리 천국',tags:'추천 키워드: 활기, 다양성, 즐거움',ix:654,iw:282,clip:'55% 48% 49% 50% / 57% 46% 57% 46%'},{x:1106,color:'#111',title:'동해',sub:'청명한 하늘과 첫 빛의 바다',quote:'새벽 바다,\n당신을 깨우는 첫 여행',body:'동진: 바다 옆 기차역, 일출 명소\n경포대: 해변과 호수가 만나는 곳\n00 촛대바위: 파도와 바위의 조화',tags:'추천 키워드: 청량, 자연, 일출',ix:1142,iw:367,clip:'57% 44% 43% 51% / 59% 48% 54% 43%'}].flatMap(p=>[
  gb(p.x,148,438,57,p.title,48,p.color),tx(p.x,219,448,43,p.sub,26,{font:'Gowun Dodum',color:p.color}),
  im(p.ix,295,p.iw,p.x===579?336:347,`${p.title} 여행 사진`,{radius:p.clip}),
  gb(p.x,677,448,108,p.quote,43,p.color),tx(p.x,829,448,153,p.body,23,{font:'Gowun Dodum',color:p.color,lineHeight:1.49}),
  rule(p.x,1013,438,p.color),tx(p.x,1043,455,37,p.tags,24,{font:'Gowun Dodum',color:p.color}),
 ])]

const blue='#83b4d2',medium='#468ebe',darkBlue='#306489',lightBlue='#cae7f7'
const prices=[['턱 보톡스 (1회)','5만원'],['코 필러 (1cc)','15만원'],['입술 필러 (1cc)','10만원'],['윤곽주사 (부위당)','6만원'],['실 리프팅','60만원'],['쌍꺼풀 매몰','70만원'],['쌍꺼풀 절개','100만원'],['코성형','140만원'],['리프팅 레이저','10만원'],['레이저 제모 (겨드랑이)','2만원']]
const medicalFront:Element[]=[...base(),bx(0,52,533,1131,blue),bx(1066,52,534,1131,blue),
 // Balloon photographs keep their circular silhouettes, separated from text.
 im(0,52,93,128,'풍선 장식 사진',{radius:'0 0 80% 0'}),im(0,130,64,153,'풍선 장식 사진',{radius:'50%'}),im(450,52,83,189,'풍선 장식 사진',{radius:'50%'}),
 tx(103,141,187,80,'엔젤릭',67,{weight:700,color:'#fff',letterSpacing:-4.7}),tx(291,141,166,80,'뷰티',67,{weight:700,color:'#c7e7f0',letterSpacing:-4.7}),tx(103,233,386,78,'특가 이벤트',66,{weight:800,color:darkBlue,letterSpacing:-4.8}),
 ...prices.flatMap(([label,price],i)=>{const yy=332+i*72.7;return[bx(52,yy,427,61,'#fff',{radius:27}),tx(77,yy+10,310,44,label,29,{color:medium,weight:600,letterSpacing:-1.4}),tx(342,yy+10,107,44,price,29,{color:medium,weight:600,align:'right',letterSpacing:-.8})]}),
 tx(86,1069,373,40,'Plastic Surgery & Dermatology',24,{font:'Arial',color:'#fff',align:'center',letterSpacing:-.7}),
 chip(628,148,344,73,'오시는 길',39,'#fff',{color:medium,weight:700,border:`11px solid ${medium}`,radius:20}),
 im(625,246,350,223,'입체 도로 안내 지도',{radius:17}),
 tx(624,499,352,78,'서울특별시 다정구 상상로 77\n희망빌딩 1층 00031',28,{color:medium,weight:700,align:'center',letterSpacing:-1.7,lineHeight:1.5}),
 mrule(606,608,383,medium),tx(635,639,330,83,'월 - 금 AM9:00-PM7:00\n토요일 AM9:00-PM1:30',29,{color:medium,weight:700,lineHeight:1.57,letterSpacing:.1}),mrule(606,754,383,medium),
 tx(641,785,346,139,'02-1234-5678\nwww.umchungjoeun.kr\n@dreamcanvakorea',28,{color:medium,weight:700,lineHeight:1.65,letterSpacing:.7}),
 ...floralLogo(657,972,medium,54),chip(659,1037,279,47,'성형외과 / 피부과',31,medium,{color:'#fff',weight:700,radius:28}),
 im(1066,52,132,130,'풍선 장식 사진',{radius:'0 0 100% 0'}),im(1066,139,94,139,'풍선 장식 사진',{radius:'50%'}),im(1495,131,105,163,'풍선 장식 사진',{radius:'50%'}),im(1509,249,91,217,'풍선 장식 사진',{radius:'50%'}),im(1538,52,62,97,'풍선 장식 사진',{radius:'0 0 0 80%'}),im(1066,987,83,168,'풍선 장식 사진',{radius:'50%'}),im(1066,1126,180,57,'풍선 장식 사진',{radius:'60% 50% 0 0'}),
 tx(1218,150,332,100,'Plastic Surgery\n& Dermatology',35,{font:'Arial',color:'#fff',lineHeight:1.45,letterSpacing:-.3}),
 bx(1124,287,425,512,'#fff',{clipPath:roundedDiamond(425,512)}),im(1138,301,397,484,'피부과 모델 인물 사진',{clipPath:roundedDiamond(397,484)}),
 ic(1162,332,42,43,'Sparkle','#c9e5ed',{strokeWidth:1.3}),ic(1445,393,59,56,'Sparkles','#c9e5ed',{strokeWidth:1.3}),ic(1160,691,72,68,'Sparkles','#c9e5ed',{strokeWidth:1.3}),ic(1481,669,47,47,'Sparkle','#c9e5ed',{strokeWidth:1.3}),
 ...floralLogo(1129,865,'#fff',77),chip(1133,960,407,67,'성형외과 / 피부과',43,'#fff',{weight:700,color:blue,radius:40}),tx(1163,1065,364,43,'www.umchungjoeun.kr',28,{font:'Arial',color:'#fff',letterSpacing:.1})]
const textRows=(x:number,yy:number,w:number,rows:string[][],color:string,size=29,step=45):Element[]=>rows.flatMap(([label,value],i)=>[tx(x,yy+i*step,w*.62,40,label,size,{color,weight:600,letterSpacing:-1.4}),tx(x+w*.64,yy+i*step,w*.45,45,value,size-1,{color,weight:600,letterSpacing:-1.4})])
const medicalBack:Element[]=[...base(),bx(533,52,533,1131,blue),bx(1066,52,534,1131,lightBlue),
 ...floralLogo(90,146,medium,64),chip(94,227,346,58,'성형외과 / 피부과',36,medium,{color:'#fff',weight:700,radius:32}),
 im(52,311,434,170,'수술실 사진',{radius:19}),im(52,500,434,170,'병원 로비 사진',{radius:19}),
 ...[{yy:729,name:'이현우',role:'대표원장'},{yy:930,name:'이수정',role:'부원장'}].flatMap(p=>[
 im(52,p.yy,138,161,`${p.role} 프로필 사진`,{radius:'50%'}),chip(197,p.yy,135,48,p.role,31,'#4d5150',{weight:700,color:'#fff0a3',radius:27}),brush(341,p.yy-8,159,77,p.name,62,'#414443'),
 tx(197,p.yy+70,308,104,'•  의과대학 의학과 졸업\n•  성형외과 전문의\n•  대학병원 성형외과 전공의 수료',22,{color:medium,weight:700,lineHeight:1.56,letterSpacing:-1.1})
 ]),
 ic(558,65,72,70,'Sparkles',lightBlue,{strokeWidth:1.6}),chip(629,148,344,74,'보톡스 / 필러',40,blue,{weight:700,color:'#fff',border:'11px solid #fff',radius:20}),
 ...textRows(606,260,368,[['사각턱 보톡스','1회 5만원'],['주름 보톡스','1회 3만원'],['승모근 보톡스','1회 15만원'],['종아리 보톡스','1회 15만원']], '#fff'),
 ...textRows(606,452,372,[['코 필러','1cc 15만원'],['입술 필러','1cc 10만원'],['팔자주름 필러','1cc 10만원'],['애교살 필러','1cc 15만원']], '#fff'),mrule(606,679,383,'#fff'),
 chip(629,757,344,74,'눈 / 코 성형',40,blue,{weight:700,color:'#fff',border:'11px solid #fff',radius:20}),
 ...textRows(606,870,364,[['자연유착','1회 80만원'],['매몰법','1회 80만원'],['절개법','1회 100만원'],['코끝성형','1회 90만원'],['콧대성형','1회 120만원']], '#fff',29,48),
 ic(1002,653,44,51,'Sparkle',lightBlue,{strokeWidth:1.3}),ic(1048,590,45,64,'Sparkles',lightBlue,{strokeWidth:1.3}),
 ic(1528,87,72,107,'Sparkles',blue,{strokeWidth:1.7}),chip(1160,148,344,74,'보톡스 / 필러',40,lightBlue,{weight:700,color:darkBlue,border:`11px solid ${darkBlue}`,radius:20}),
 ...textRows(1138,260,372,[['실리프팅','1줄 10만원'],['미니거상','1회 290만원'],['안면거상','1회 500만원'],['이중턱 지방흡입','1회 150만원']],darkBlue),mrule(1138,467,383,darkBlue),
 brush(1151,499,401,70,'다양한 피부 레이저 보유',53,darkBlue),chip(1160,577,344,74,'피부레이저 / 관리',39,lightBlue,{weight:700,color:darkBlue,border:`11px solid ${darkBlue}`,radius:20,letterSpacing:-1.5}),
 ...textRows(1149,693,359,[['레이저 제모','1회 5만원'],['홍조 레이저','1회 10만원'],['기미 / 잡티 레이저','1회 5만원'],['모공 레이저','1회 15만원'],['탄력 레이저','1회 30만원']],darkBlue,28,47),
 ...textRows(1149,934,359,[['코 모공청소','1회 5만원'],['스킨 스케일링','1회 15만원'],['비타민 관리','1회 8만원'],['피부 진정','1회 5만원']],darkBlue,28,47)]

const mint='#55ad9f',coral='#f27765',cream='#ffe1a0',mintText='#62a89d',coralText='#da8574'
const head=(x:number,yy:number,title:string,color:string):Element[]=>[tx(x,yy,446,63,title,43,{weight:700,color:color===mint?mintText:coralText,letterSpacing:-1.8}),bx(x,yy+70,42,3,color===mint?mintText:coralText)]
const libraryFront:Element[]=[...base(),
 ...head(46,163,'수강안내',coral),...head(581,163,'다양한 프로그램',mint),
 ...[{yy:283,title:'접수 기간',body:'매월 10일 10:00 ~ 선착순 마감',icon:'CalendarDays'},{yy:424,title:'접수 방법',body:'홈페이지 또는 방문 접수\n(회원 로그인 후 신청 가능)',icon:'Smartphone'},{yy:575,title:'수강료 결제',body:'프로그램별 상이 / 안내 후\n입금 또는 카드 결제',icon:'CreditCard'}].flatMap(p=>[
 bx(47,p.yy,92,92,cream,{radius:'50%'}),ic(69,p.yy+23,48,50,p.icon,'#191919',{strokeWidth:1.2}),tx(161,p.yy+9,336,38,p.title,25,{weight:700,color:coralText}),tx(161,p.yy+54,354,63,p.body,20,{letterSpacing:-.6,lineHeight:1.24})
 ]),
 im(158,722,342,308,'아이들과 독서 지도 선생님 일러스트',{radius:'45% 47% 24% 25%'}),
 ic(77,852,46,62,'Sparkles','#f3d985',{strokeWidth:1.4}),ic(432,747,42,48,'Sparkles','#f3d985',{strokeWidth:1.4}),ic(158,770,23,23,'Heart','#bb977d',{strokeWidth:1.1}),ic(138,790,28,28,'Heart','#bb977d',{strokeWidth:1.1}),ic(184,805,21,21,'Heart','#bb977d',{strokeWidth:1.1}),ic(169,823,25,25,'Heart','#bb977d',{strokeWidth:1.1}),ic(161,741,14,14,'Heart','#bb977d',{strokeWidth:1.1}),
 wave(0,933,533,250,coral),ic(35,1097,22,22,'Phone','#fff',{strokeWidth:2}),tx(67,1097,140,29,'02-1234-5678',17,{font:'Arial',color:'#fff'}),bx(200,1097,1,23,'#fff'),ic(238,1097,22,22,'Globe','#fff',{strokeWidth:2}),tx(271,1097,246,28,'http://www.umchungjoeun.kr',17,{font:'Arial',color:'#fff',letterSpacing:-.4}),
 ...[{x:582,yy:279,color:'#e4eee7',title:'문화/예술',body:'미술, 음악, 공예등\n문화 체험 활동 운영',icon:'Palette'},{x:747,yy:279,color:'#fae5cf',title:'인문/교양',body:'어학, 인문학 강좌\n및 독서 모임 운영',icon:'BookOpen'},{x:909,yy:279,color:'#e7ebd4',title:'건강/운동',body:'요가,필라테스,댄스등\n건강 강좌 운영',icon:'Dumbbell'},{x:582,yy:566,color:'#fff0cc',title:'어린이/청소년',body:'어린이 독서 프로그램\n창의력 체험 활동',icon:'Baby'},{x:747,yy:566,color:'#f6e4e8',title:'생활/특강',body:'요리, 재테크, 정리수납등\n실생활 도움 강의',icon:'Coffee'},{x:909,yy:566,color:'#ede0e8',title:'특별 프로그램',body:'계절 행사, 가족 프로그\n램등 다양한 이벤트',icon:'Star'}].flatMap((p,i)=>[
 bx(p.x,p.yy,109,109,p.color,{radius:'50%'}),ic(p.x+20,p.yy+23,70,65,p.icon,'#111',{strokeWidth:1}),tx(p.x-18,p.yy+140,146,38,p.title,25,{weight:700,color:i<3?mintText:coralText,align:'center',letterSpacing:-1.2}),tx(p.x-24,p.yy+185,158,60,p.body,15,{align:'center',letterSpacing:-.8,lineHeight:1.2})
 ]),
 ...[719,882].flatMap(x=>[bx(x,280,1,217,'transparent',{border:'1px dashed #d4d4d4'}),bx(x,566,1,217,'transparent',{border:'1px dashed #d4d4d4'})]),
 brush(618,875,411,117,'당신의 일상을 풍성하게, ♡\n새로운 즐거움을 만나세요!',42,'#111',{align:'center',lineHeight:1.4}),
 bx(584,1040,433,93,'#fff',{border:'1px solid #d5d5d5',radius:14}),tx(608,1078,329,33,'자세한 내용은 홈페이지를 참고해 주세요',20,{letterSpacing:-1.2}),im(932,1058,62,63,'홈페이지 QR 이미지'),
 // Plain colour ornaments are editable geometry; only the photograph is grey.
 path(1325,52,275,189,'M0 0 H275 V111 C232 112 211 137 188 163 C145 211 104 196 82 133 C73 107 76 75 48 57 C21 42 7 22 0 0 Z',{fill:'#fbd5b3',color:'none',strokeWidth:0}),
 ...[[1325,283,17,12,-18],[1354,281,17,13,13],[1340,300,18,13,-4],[1365,307,13,11,20]].map(([x,yy,w,h,rotate])=>bx(x,yy,w,h,'#a9cdcc',{radius:'50%',rotate})),
 ...[[1499,251,8,13,-20],[1531,256,9,13,7],[1557,257,12,9,-8],[1515,277,9,13,24],[1541,278,9,13,-17],[1494,299,8,8,0],[1511,311,8,10,-11],[1548,302,7,11,15],[1568,284,8,11,9]].map(([x,yy,w,h,rotate])=>bx(x,yy,w,h,'#f4c76e',{radius:'50%',rotate})),
 tx(1128,160,385,83,'일상에',66,{weight:700,color:'#000',letterSpacing:-2}),tx(1128,252,398,83,'배움과',66,{weight:700,color:mint,letterSpacing:-2}),
 tx(1128,343,253,83,'즐거움',66,{weight:700,color:coral,letterSpacing:-2}),tx(1320,343,141,83,'을',66,{weight:700,color:'#000',letterSpacing:-2}),tx(1128,435,398,83,'더하다',66,{weight:700,color:'#000',letterSpacing:-2}),
 tx(1129,529,260,90,'함께 배우고\n함께 즐기는\n우리 도서관',24,{lineHeight:1.3,letterSpacing:-.7}),ic(1246,530,47,46,'Sparkles','#f8d881',{strokeWidth:1.5}),
 im(1217,434,383,597,'도서관 서가 사진',{radius:'100% 0 0 70% / 67% 0 0 33%'}),
 bx(1066,886,270,257,'#d7e6dc',{radius:'75% 75% 0 0'}),path(1091,803,73,176,'M40 174 Q24 131 38 93 Q55 52 56 0 M38 94 Q9 88 20 55 Q42 66 38 94 M31 122 Q2 117 9 88 Q31 99 31 122 M38 103 Q65 98 70 79 Q46 73 38 103 M39 71 Q15 66 22 34 Q46 51 39 71 M43 63 Q68 54 70 37 Q48 38 43 63 M47 35 Q33 14 56 0 Q58 26 47 35 M33 147 Q4 140 6 117 Q30 127 33 147 M33 136 Q63 121 65 110 Q42 113 33 136',{color:mint,strokeWidth:1.8}),wave(1066,937,534,246,mint,true),
 ic(1127,1048,34,34,'House','#fff',{strokeWidth:2}),tx(1165,1055,320,42,'라라나도서관',27,{color:'#fff',letterSpacing:-.7}),tx(1129,1089,432,34,'모두를 위한 지식, 모두의 기쁨',20,{color:'#fff',letterSpacing:-.5})]
const teacherCards=[{yy:226,name:'강지민 강사',tag:'미술',body:'•  미술대학교 미술학과 졸업\n•  전 창작 아트 클래스 강의\n•  미술 심리 상담사 1급 보유'},{yy:477,name:'이준우 강사',tag:'운동',body:'•  체육대학교 체육학과 졸업\n•  전 필라테스 전문 강사\n•  생활 스포츠 지도사 2급'},{yy:723,name:'박지연 강사',tag:'베이킹',body:'•  베이커리 제과 과정 수료\n•  전 홈베이킹 클래스 강의\n•  제과 기능사 자격증 보유'}]
const libraryBack:Element[]=[...base(),...head(46,116,'강사진 소개',mint),...head(598,116,'인기 프로그램',coral),...head(1114,116,'오시는길/문의',coral),
 ...teacherCards.flatMap(p=>[bx(47,p.yy,437,227,'#fff',{border:'1px solid #bdd4ce',radius:20}),im(47,p.yy,158,227,`${p.name} 프로필 사진`,{radius:18}),tx(250,p.yy+46,128,37,p.name,23,{weight:700,color:mint,letterSpacing:-1}),chip(369,p.yy+45,63,31,p.tag,20,mint,{color:'#fff',weight:400,radius:18,letterSpacing:-.7}),tx(247,p.yy+99,228,120,p.body,18,{lineHeight:1.83,letterSpacing:-.9})]),
 wave(0,934,533,249,mint),tx(47,1088,408,35,'배움이 일상이 되는곳, 라라나도서관 문화센터',20,{color:'#fff',letterSpacing:-.8}),ic(420,1055,64,58,'Sprout','#fff',{strokeWidth:1.4}),
 ...[{yy:226,title:'창작 그림 클래스',body:'나만의 이야기를 색으로\n표현하는 힐링 아트',a:'초등이상',b:'매주 수\n10:00~12:00',c:'20,000원\n(재료비별도)',label:'회화 미술 도구 사진'},{yy:422,title:'몸 & 필라테스',body:'코어 강화와 유연성 향상\n을 돕는 건강한 습관',a:'성인남녀',b:'매주 월/수\n19:00~20:00',c:'30,000원\n(재료비별도)',label:'필라테스 운동 사진'},{yy:618,title:'창작 그림 클래스',body:'나만의 이야기를 색으로\n표현하는 힐링 아트',a:'초등이상',b:'매주 금\n10:30~12:30',c:'25,000원\n(재료비별도)',label:'베이킹 쿠키 사진'},{yy:815,title:'스토리 놀이교실',body:'놀이와 책이 만나는\n창의력 쑥쑥 시간',a:'유아 6~7세',b:'매주 토\n11:00~12:00',c:'15,000원\n(재료비별도)',label:'어린이 놀이 사진'}].flatMap(p=>[
 bx(585,p.yy,437,184,'#fff',{border:'1px solid #dec6bd',radius:17}),im(585,p.yy,117,184,p.label,{radius:15}),tx(718,p.yy+22,145,33,p.title,20,{weight:700,color:coral,letterSpacing:-1}),tx(718,p.yy+72,145,66,p.body,15,{lineHeight:1.8,letterSpacing:-.5}),
 ...[{dy:24,text:p.a},{dy:70,text:p.b},{dy:125,text:p.c}].flatMap(o=>[chip(861,p.yy+o.dy,43,28,'대상',14,'#f7edce',{weight:400,radius:15}),tx(908,p.yy+o.dy+2,108,45,o.text,14,{lineHeight:1.3,letterSpacing:-.5})])
 ]),tx(584,1088,402,39,'* 상기 프로그램은 사정에 의해 변경될 수 있습니다',20,{letterSpacing:-1}),ic(960,1052,59,61,'Sprout',coral,{strokeWidth:1.7}),
 im(1114,234,441,360,'교통 안내 지도 그래픽',{radius:22}),
 bx(1114,628,441,322,'#fff',{border:'1.5px solid #c98576',radius:24}),bx(1334,628,1.5,322,'#c98576'),bx(1114,790,441,1.5,'#c98576'),
 ...[{x:1138,yy:648,icon:'TramFront',title:'지하철',body:'[초록선] 00역 2번 출구\n도보 10분\n[파랑선] 00역 5번 출구\n도보 2분'},{x:1361,yy:648,icon:'BusFront',title:'버스 이용',body:'초록 정류장\n1-11, 1-51, 2-22\n파랑 정류장\n20-22, 23-22, 25-12'},{x:1138,yy:807,icon:'CarFront',title:'주차 이용',body:'건물 지하 주차장 이용\n(최초 2시간 무료)\n주차공간이 협소하여 대중\n교통 이용을 권장합니다'},{x:1361,yy:807,icon:'Phone',title:'문의/상담',body:'02-1234-5678\n서울특별시 다정구 상\n상로 77 희망빌딩 1층\n00031'}].flatMap(p=>[ic(p.x,p.yy,29,33,p.icon,'#c98576',{strokeWidth:1}),tx(p.x+39,p.yy,153,36,p.title,20,{color:coral,weight:700,letterSpacing:-.7}),tx(p.x+39,p.yy+39,162,111,p.body,14,{lineHeight:1.6,letterSpacing:-.4})]),
 wave(1066,937,534,246,coral,true),tx(1129,1088,406,35,'배움이 일상이 되는곳, 라라나도서관 문화센터',20,{color:'#fff',letterSpacing:-.8}),ic(1492,1056,61,58,'Sprout','#fff',{strokeWidth:1.4})]

const brown='#bd4900',orange='#cc6c05',yellow='#f8c73c',ink='#432407',autumnCream='#fffaec'
const autumnHeading=(x:number,yy:number,w:number,title:string):Element[]=>[tx(x,yy,w,70,title,53,{font:'Black Han Sans',weight:400,color:brown,align:'center',letterSpacing:-2.3}),ic(x+w-66,yy-28,50,50,'Leaf',brown,{strokeWidth:2}),path(x+35,yy+64,w-70,18,`M0 16 Q10 0 22 10 T44 10 T66 10 T88 10 T110 10 T132 10 T154 10 T176 10 T198 10 T220 10 T242 10 T264 10 T286 10`,{color:'#d3a769',strokeWidth:4})]
const autumnFront:Element[]=[...base(autumnCream),bx(0,52,533,1131,yellow),
 ...autumnHeading(115,137,321,'축제 소개'),tx(63,283,429,89,'온 가족이 함께 즐기는 가을 문화축제!\n다양한 체험과 공연, 먹거리를 만나보세요.',24,{weight:700,color:ink,align:'center',lineHeight:1.7,letterSpacing:-1.1}),
 bx(40,403,449,646,'#fff',{radius:24}),
 ...[{yy:451,title:'주요 행사',body:'개막식, 가족 공연\n체험 부스, 먹거리 장터',icon:'UsersRound'},{yy:649,title:'추천 체험',body:'가을 만들기,자연 체험,\n가족 미션,포토존',icon:'CalendarDays'},{yy:855,title:'문의처',body:'다정구청 문화관광과\nT.02-1234-5678',icon:'PhoneCall'}].flatMap(p=>[bx(92,p.yy,119,119,'#f9c627',{radius:'50%'}),ic(126,p.yy+34,51,53,p.icon,orange,{strokeWidth:1.4}),tx(245,p.yy-2,209,42,p.title,29,{weight:700,color:brown,letterSpacing:-1.1}),tx(245,p.yy+47,226,90,p.body,22,{color:ink,lineHeight:1.6,letterSpacing:-1})]),
 arule(74,609,379,'#d8b997'),arule(74,818,379,'#d8b997'),ic(424,396,43,55,'Paperclip',orange,{strokeWidth:2}),
 ...autumnHeading(646,143,327,'오시는 길'),tx(651,254,303,82,'가을 축제 장소를 확인하고\n편하게 방문해 주세요.',25,{weight:700,color:ink,align:'center',lineHeight:1.55,letterSpacing:-1}),
 // This flat schematic is simple geometry and remains editable.
 bx(569,349,467,218,'#ffefc3',{radius:25}),bx(594,438,414,11,'#e2aa39',{radius:7}),bx(715,444,11,97,'#e2aa39',{radius:7}),bx(825,374,11,168,'#e2aa39',{radius:7}),bx(946,371,11,170,'#e2aa39',{radius:7}),
 tx(870,385,72,28,'라라나역',19,{color:ink,letterSpacing:-.6}),bx(919,411,17,17,'#f8ca4f',{radius:'50%'}),ic(880,454,28,32,'MapPin','#f27607',{strokeWidth:3}),tx(848,498,112,35,'라라나공원',20,{weight:700,color:ink,letterSpacing:-.6}),
 ic(575,594,24,24,'MapPin',ink,{strokeWidth:2}),tx(607,592,439,44,'서울특별시 다정구 상상로 77 희망빌딩 1층 00031',22,{weight:700,color:ink,letterSpacing:-1.4}),
 ...[{yy:658,title:'주차 안내',body:'행사장 인근 공영 주차장을 이용해 주세요',icon:'CarFront'},{yy:766,title:'지하철',body:'라라나역 2번 출구 도보 5분',icon:'TramFront'},{yy:870,title:'버스',body:'라라나공원 정류장 하차 후 도보 3분',icon:'BusFront'}].flatMap(p=>[bx(577,p.yy,71,71,orange,{radius:'50%'}),ic(595,p.yy+19,35,36,p.icon,'#fff',{strokeWidth:1.5}),tx(681,p.yy+1,340,41,p.title,29,{weight:700,color:ink,letterSpacing:-1.3}),tx(681,p.yy+45,355,49,p.body,21,{color:ink,letterSpacing:-1.1})]),rule(577,747,459,'#c7ac83'),rule(577,852,459,'#c7ac83'),
 im(1066,52,150,382,'가을 잎 모서리 일러스트',{radius:'0 0 50% 0'}),im(1434,52,166,361,'가을 잎 모서리 일러스트',{radius:'0 0 0 50%'}),
 tx(1130,306,410,205,'가을\n한마당 축제',88,{font:'Black Han Sans',weight:400,color:brown,align:'center',lineHeight:1.1,letterSpacing:-3}),
 chip(1141,513,402,50,'함께 즐기는 우리 동네 가을 행사',25,orange,{color:'#fff5d9',weight:400,radius:26,letterSpacing:-.5}),
 tx(1134,596,414,59,'10.25.(토) 10:00 ~ 17:00',38,{weight:800,color:ink,align:'center',letterSpacing:-1.6}),tx(1233,708,257,44,'장소  |  라라나 공원',25,{weight:700,color:brown,letterSpacing:-1.2}),
 // Curved ground is a simple editable shape, independent of complex art.
 path(533,1056,1067,127,'M0 127 Q300 -43 620 58 Q869 151 1067 44 L1067 127 Z',{fill:'#f7c725',color:'none',strokeWidth:0}),
 im(1133,810,402,373,'가을 행사 인물 일러스트',{radius:'40% 45% 0 0'}),im(533,982,470,136,'나뭇잎 관목 배경 일러스트',{radius:'50% 50% 0 0'}),im(1512,980,88,160,'가을 관목 배경 일러스트',{radius:'50% 50% 0 0'})]
const timetable=[['10:00 ~ 10:30','개막식'],['10:30 ~ 11:30','문화 공연'],['11:30 ~ 13:00','체험 부스 운영'],['13:00 ~ 14:00','점심 시간'],['14:00 ~ 15:00','가을 음악 공연'],['15:00 ~ 16:30','참여 이벤트'],['16:30 ~ 17:00','폐막식 및\n경품 추첨']]
const autumnBack:Element[]=[...base(autumnCream),...autumnHeading(118,138,320,'행사 일정'),...autumnHeading(606,138,438,'주요 프로그램'),...autumnHeading(1180,135,317,'이용 안내'),
 bx(41,280,451,576,yellow),bx(41,280,235,576,orange),bx(41,280,451,60,'#462007'),bx(275,280,1,576,'#816443'),tx(66,295,186,36,'시간',28,{color:'#fff',weight:700,align:'center'}),tx(298,295,177,36,'주요내용',28,{color:'#fff',weight:700,align:'center'}),
 ...timetable.flatMap(([time,event],i)=>{const yy=349+i*66;return[tx(55,yy+9,208,56,time,28,{font:'Arial',color:'#fff5df',align:'center',letterSpacing:-.8}),tx(283,yy+9,199,i===6?78:55,event,28,{color:ink,align:'center',lineHeight:1.5,letterSpacing:-1.2}),...(i<6?[arule(41,yy+57,451,'#f1daa9')]:[])]}),
 tx(64,872,441,51,'※ 일정은 운영 상황에 따라 변경될 수 있습니다.',20,{color:'#111',letterSpacing:-1}),
 ...[{yy:260,title:'만들기 체험',body:'가을 소품 만들기 등\n다양한 체험',fill:yellow,color:brown,label:'가을 만들기 가방 일러스트'},{yy:470,title:'가을 포토존',body:'단풍 배경에서\n기념사진 촬영',fill:'#ff8a3a',color:'#fff1be',label:'포토존 카메라 일러스트'},{yy:677,title:'공연',body:'가족이 함께 즐기는\n문화 공연',fill:yellow,color:brown,label:'공연 드럼 일러스트'},{yy:888,title:'먹거리',body:'맛있는 간식과\n푸드존 운영',fill:'#ff8a3a',color:'#fff1be',label:'먹거리 매대 일러스트'}].flatMap(p=>[
 bx(584,p.yy,443,193,p.fill,{radius:50}),bx(615,p.yy+27,149,141,'#fff',{radius:38}),im(644,p.yy+48,92,99,p.label,{radius:10}),tx(799,p.yy+45,211,41,p.title,29,{font:'Black Han Sans',weight:400,color:p.color,letterSpacing:-1}),tx(799,p.yy+89,211,85,p.body,23,{color:ink,lineHeight:1.6,letterSpacing:-1}),ic(947,p.yy-7,41,49,'Paperclip',orange,{strokeWidth:2})]),
 tx(1132,267,356,46,'참여 방법',33,{font:'Black Han Sans',weight:400,color:ink,letterSpacing:-1}),tx(1132,330,429,90,'현장 자유 참여\n※ 일부 프로그램은 사전 신청이 필요합니다.',24,{color:ink,lineHeight:1.65,letterSpacing:-1}),arule(1132,449,418,'#d1b68f'),
 tx(1132,495,356,47,'참여 대상',33,{font:'Black Han Sans',weight:400,color:ink,letterSpacing:-1}),tx(1132,557,429,85,'누구나 참여 가능\n가족 · 친구 · 이웃과 함께',24,{color:ink,lineHeight:1.65,letterSpacing:-1}),arule(1132,666,418,'#d1b68f'),
 tx(1132,709,356,48,'유의사항',33,{font:'Black Han Sans',weight:400,color:ink,letterSpacing:-1}),tx(1132,769,443,133,'• 쓰레기는 지정된 곳에 버려주세요.\n• 어린이는 보호자와 함께 이용해 주세요.\n• 우천 시 일부 프로그램이 변경될 수 있습니다.',23,{color:ink,lineHeight:1.74,letterSpacing:-.9}),
 im(0,918,593,226,'가을 관목 배경 일러스트',{radius:'35% 60% 0 0'}),im(1145,936,455,211,'가을 관목 배경 일러스트',{radius:'45% 35% 0 0'}),
 path(0,1053,1600,130,'M0 130 Q320 -18 665 75 Q775 95 883 130 Q1165 -38 1600 0 L1600 130 Z',{fill:'#e8aa39',color:'none',strokeWidth:0}),
 path(0,1103,900,80,'M0 80 Q320 -54 900 80 L0 80 Z',{fill:'#f7c725',color:'none',strokeWidth:0}),im(1294,925,246,164,'푸드 트럭 일러스트',{radius:17}),im(774,1103,100,80,'가을 나무 일러스트',{radius:'50% 50% 0 0'})]

const travelAligned=(es:Element[])=>es.map(e=>e.kind==='text'&&e.font==='Gowun Dodum'?{...e,y:e.y-5}:e)
const libraryAligned=(es:Element[])=>es.map(e=>e.kind==='text'&&!e.chip&&e.font!=='Nanum Brush Script'?{...e,y:e.y-7}:e)
const autumnAligned=(es:Element[])=>es.map(e=>e.kind==='text'&&!e.chip?{...e,y:e.y-(e.font==='Black Han Sans'?2:7)}:e)
export const groupF:BrochureDraft[]=[
 {id:'l23',sides:[{id:'s01',elements:travelAligned(travelFront),notes:['손상된 첨부 PNG044의 하단은 Canva 공개 상세 페이지의 동일 1600px 원본으로 복구해 비교했다.','여행 사진과 복잡한 교량 그림은 회색 placeholder. 단순 물결·원·별은 구현했다.','여행 제목은 실제 Gaegu700, 본문은 Gowun Dodum400으로 원본 굵기와 둥근 획을 보정했다. 일부 획 형태는 다르다.']},{id:'s02',elements:travelAligned(travelBack),notes:['3열 배경·비정형 사진 마스크·점선·문구를 원본 위치로 재현. 사진만 회색 placeholder.','원문의 000 지명 및 K00·S00 등 표기는 읽힌 그대로 보존했다.']}]},
 {id:'l24',sides:[{id:'s01',elements:medicalFront,notes:['인물·풍선·입체 지도 사진은 원본 마스크 형태의 회색 placeholder.','가격행은 공통 pill 형식과 동일 좌우 가격열로 구성했다. 원본 식물 로고를 재사용하는 단순 SVG로 구성했다.']},{id:'s02',elements:medicalBack,notes:['가격·시술명·장식별·윤곽선 배지를 재현. 의료진 프로필과 병원 사진은 회색.','의료진 이름 손글씨는 Nanum Brush Script로 대체하여 일부 획 모양이 다르다.']}]},
 {id:'l25',sides:[{id:'s01',elements:libraryAligned(libraryFront),notes:['6개 분야의 원형 배경·Lucide 아이콘·접수안내·바닥 물결·표지 복숭아색 유기형 도형·작은 색상 점을 구현했다.','복잡한 인물 삽화·도서관 사진·QR 이미지는 회색.']},{id:'s02',elements:libraryAligned(libraryBack),notes:['강사3명과 프로그램4개 및 연락처2×2표를 데이터 기반 카드로 구현했다.','사진·지도는 회색. 원본의 반복된 창작 그림 클래스 및 대상 칩 표기는 읽힌 그대로 보존.']}]},
 {id:'l26',sides:[{id:'s01',elements:autumnAligned(autumnFront),notes:['실제 Black Han Sans400 축제 제목, 원본 일정·장소·시각·행사내용과 편집 가능한 단순 교통 지도를 구현했다.','복잡한 인물·식물 일러스트는 회색으로 보존. 바닥 곡선·표·아이콘은 구현했다.']},{id:'s02',elements:autumnAligned(autumnBack),notes:['7행 일정표, 4개 프로그램, 참여 방법·대상·유의사항을 재현했다.','프로그램 삽화·푸드트럭·관목은 회색. 단순 단풍잎과 세로 클립은 SVG 도형으로 구현했다.']}]},
]
