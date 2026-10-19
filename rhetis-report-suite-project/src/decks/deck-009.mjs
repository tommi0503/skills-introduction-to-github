import {T,R,C,L,P,I,Path,Chip} from '../primitives.mjs';

const K='#000000', W='#ffffff', GRAY='#f2f4f5', BG='#f0f0f0', BLUE='#2c4ffe', LIME='#d8ff27';
const text=(x,y,w,h,s,size=24,e={})=>{
  // Noto's metric box exceeds its visible glyph bounds. Give it a full line box
  // while preserving the same visible baseline and explicit multiline spacing.
  const font=e.font||'Noto Sans KR', lh=e.lineHeight??1.25;
  const inset=font==='Noto Sans KR'&&!s.includes('\n')?Math.max(0,(1.5-lh)*size/2):0;
  return T(x,y-inset,w,h+inset*2,s,size,{font,color:K,weight:400,letterSpacing:-0.55,lineHeight:inset?1.5:lh,...e,...(inset?{lineHeight:1.5}:{})});
};
const box=(x,y,w,h,fill=GRAY,e={})=>R(x,y,w,h,fill,{stroke:K,strokeWidth:1.15,radius:10,el:'card',...e});
const center=(x,y,w,h,s,size=24,e={})=>text(x,y,w,h,s,size,{align:'center',...e});
const icon=(x,y,w,h,name,color=K,e={})=>I(x,y,w,h,name,color,{strokeWidth:1.6,...e});
const dot=(x,y,r=4)=>C(x-r,y-r,r*2,r*2,W,{stroke:K,strokeWidth:1.1});
const top=(number,name)=>[
  box(29,26,1222,79,W,{radius:11,el:'image-frame'}),
  R(48,43,48,46,K,{radius:6}),center(48,53,48,27,number,18,{color:W,weight:600}),
  text(110,53,625,33,name,24,{weight:700}),
  icon(1047,51,28,27,'HeartHandshake',K,{strokeWidth:2.1}),text(1085,53,126,27,'미리시, 성장의 기록',16,{weight:600}),
  box(29,117,1222,570,W,{radius:10,el:'image-frame'})
];
const heading=(s,size=48)=>center(70,153,1140,72,s,size,{weight:700,letterSpacing:-1.45});
const footer=()=>[
  box(70,602,1140,58,GRAY,{radius:5}),text(93,621,500,22,'• PERFORMANCE REPORT',14,{letterSpacing:1.5}),
  text(794,622,396,22,'•  보고 기관: 미리시청 기획조정실   •  보고 일자: 2056. 12. 30',14,{letterSpacing:-0.3})
];
const ph=(x,y,w,h)=>P(x,y,w,h,'',{el:'image-frame'});

const slides=[];
slides.push({id:'slide_01',title:'2056년도 주요 성과 보고',background:W,elements:[
  box(619,65,296,261,LIME,{radius:10}),box(914,328,296,261,LIME,{radius:10}),
  ph(602,166,244,212),ph(952,138,257,227),ph(859,352,264,237),
  icon(74,237,43,38,'HeartHandshake',K,{strokeWidth:2.5}),text(125,237,390,38,'미리시, 성장의 기록',25,{weight:700}),
  text(70,272,535,115,'2056년도',82,{weight:700,letterSpacing:-2}),
  text(70,366,550,116,'주요 성과 보고',77,{weight:700,letterSpacing:-2.5}),
  text(74,509,510,43,'ANNUAL RESULTS REPORT',27.5,{font:'Pretendard',color:BLUE,weight:600,letterSpacing:0}),
  ...footer()
]});

slides.push({id:'slide_02',title:'Chapter — 목차',background:W,elements:[
  text(74,96,260,80,'Chapter',62,{color:BLUE,weight:700,letterSpacing:-1.6}),
  text(333,126,310,41,'2056년도 주요 성과 보고',24.5,{weight:700}),
  L(639,141,1209,141,K,1.2),dot(639,141),dot(1209,141),
  ...[
    ['01.','핵심 주요 성과','대시보드',336],['02.','분야별 추진 실적','경제·복지·환경·문화',356],
    ['03.','예산 결산 및 만족도','지표·추이',386],['04.','대외 평가 및 시민 목소리','수상·인터뷰',431],
    ['05.','향후 과제 및 비전','목표',364]
  ].flatMap((a,i)=>[
    text(124,241+i*56,49,34,a[0],27,{font:'Pretendard',color:BLUE,weight:600}),
    text(175,239+i*56,310,39,a[1],24.5,{weight:700}),
    text(a[3],245+i*56,290,30,a[2],20,{font:'Pretendard',color:'#a0a0a0',weight:600})
  ]),
  Path(824,317,150,286,'M2 280 L40 5 Q41 0 46 1 L50 2 Q53 3 52 8 L14 282 Q13 286 9 285 L5 285 Q1 285 2 280 Z M98 280 L136 5 Q137 0 142 1 L146 2 Q149 3 148 8 L110 282 Q109 286 105 285 L101 285 Q97 285 98 280 Z M48 15 H135 V23 H47 Z M41 56 H129 V64 H40 Z M35 98 H123 V106 H34 Z M29 139 H117 V147 H28 Z M23 180 H111 V188 H22 Z M17 222 H105 V230 H16 Z',{viewBox:'0 0 150 286',fill:LIME,stroke:K,strokeWidth:1.6}),
  ph(960,336,146,266),...footer()
]});

slides.push({id:'slide_03',title:'시정개요 — 핵심 비전',background:BG,elements:[
  ...top('01','시정개요'),heading('2056 미리시정 3대 핵심 비전'),
  box(110,246,295,261,GRAY),box(494,246,296,261,LIME),box(879,246,296,261,BLUE),
  center(110,273,295,30,'01',23,{weight:700}),center(110,303,295,37,'활력 경제',25,{weight:700}),
  center(494,273,296,30,'02',23,{weight:700}),center(494,303,296,37,'포용 복지',25,{weight:700}),
  center(879,273,296,30,'03',23,{color:W,weight:700}),center(879,303,296,37,'친환경 도시',25,{color:W,weight:700}),
  R(221,362,73,42,'none',{stroke:K,strokeWidth:2.8,radius:3}),
  Path(221,362,73,42,'M0 14 Q14 14 14 0 M73 27 Q59 27 59 42',{viewBox:'0 0 73 42',fill:'none',stroke:K,strokeWidth:2.8}),
  center(233,367,47,35,'₩',28,{weight:700}),
  icon(607,351,70,65,'Scale',K,{strokeWidth:1.55}),icon(993,353,62,62,'Globe',W,{strokeWidth:1.5}),
  L(405,377,494,377,K,1),dot(405,377),dot(494,377),
  L(790,377,879,377,K,1),dot(790,377),dot(879,377),
  center(110,443,295,37,'지역상권 회복 및 일자리 창출',19),
  center(494,443,296,37,'단 한 명도 소외 없는 맞춤 복지',19),
  center(879,443,296,37,'탄소중립 실천 및 녹색공간 확충',19,{color:W}),
  box(110,547,1065,73,GRAY,{radius:7,strokeWidth:0.7,el:'callout'}),
  center(125,568,1035,41,'"시민이 행복한 스마트 미래도시 미리"',28,{weight:700})
]});

slides.push({id:'slide_04',title:'성과 하이라이트 — 핵심 성과 대시보드',background:BG,elements:[
  ...top('02','성과 하이라이트'),heading('2056 미리시 4대 핵심 성과 대시보드'),
  box(110,246,396,375,GRAY),text(143,285,330,35,'•  투자 유치',22,{weight:700}),
  text(142,315,146,125,'2.4',88,{weight:700,letterSpacing:-3,el:'metric'}),text(276,373,100,45,'조 원',28,{weight:700}),
  ph(291,414,194,206),text(144,547,217,35,'(전년 대비 135% 달성)',18),
  box(533,246,642,107,'#efefef'),box(533,380,642,107,LIME),box(533,513,642,107,BLUE),
  text(570,285,220,38,'•  일자리 창출',22,{weight:700}),
  text(799,263,187,80,'18,500',56,{weight:700,letterSpacing:-1.4,el:'metric'}),
  text(986,293,33,34,'개',24,{weight:700}),text(1017,296,155,30,'(목표치 초과 달성)',17),
  text(570,420,220,38,'•  시민 만족도',22,{weight:700}),
  text(865,396,121,80,'92.4',56,{weight:700,letterSpacing:-1,el:'metric'}),
  text(986,427,33,34,'점',24,{weight:700}),text(1017,430,155,30,'(역대 최고치 기록)',17),
  text(570,554,240,38,'•  공공예산 절감',22,{weight:700,color:W}),
  text(878,530,109,80,'450',56,{weight:700,color:W,letterSpacing:-1,el:'metric'}),
  text(987,559,56,34,'억 원',24,{weight:700,color:W}),text(1040,563,131,30,'(사업 구조조정)',17,{color:W})
]});

slides.push({id:'slide_05',title:'민생경제 — 지역경제와 일자리',background:BG,elements:[
  ...top('03','민생경제'),heading('지역 경제 활성화 및 일자리 성과',46.5),
  box(110,246,520,375,GRAY),box(655,246,520,375,LIME),
  text(143,285,440,38,'•  주요 경제 지표 추이',23,{weight:700}),
  R(147,342,119,111,BLUE,{radius:9}),R(147,471,119,111,BLUE,{radius:9}),
  Path(181,375,51,48,'M5 3 H45 Q48 3 48 6 V37 H2 V6 Q2 3 5 3 Z M3 30 H47 M19 37 L16 45 H32 L29 37 M10 25 L21 13 L29 19 L39 9',{viewBox:'0 0 51 48',fill:'none',stroke:W,strokeWidth:2.1}),
  Path(181,502,51,49,'M16 47 V5 Q16 2 19 2 H46 Q49 2 49 5 V47 H36 V36 H25 V47 Z M16 22 H4 Q2 22 2 25 V47 H16 M23 12 H42 M23 19 H42 M23 26 H42',{viewBox:'0 0 51 49',fill:'none',stroke:W,strokeWidth:2.1}),
  text(306,347,290,34,'소상공인 지원금 집행률',21),
  text(305,370,135,88,'98.2',64,{weight:700,letterSpacing:-1.5,el:'metric'}),text(437,410,65,31,'%',26,{weight:600}),
  text(306,480,290,34,'청년 창업 지원 기업 수',21),
  text(305,503,111,89,'142',64,{weight:700,letterSpacing:-1.7,el:'metric'}),text(415,541,48,35,'개사',25,{weight:600}),
  text(466,548,145,30,'(전년比 +28%)',18),
  text(686,285,440,38,'•  지역 경제 규모 추이',23,{weight:700}),
  R(707,440,119,108,BLUE,{radius:9,el:'chart-bar'}),R(855,394,119,154,BLUE,{radius:9,el:'chart-bar'}),R(1003,349,119,199,BLUE,{radius:9,el:'chart-bar'}),
  L(690,548,1142,548,K,1),center(704,560,125,31,'2054년',21),center(852,560,125,31,'2055년',21),center(1001,560,125,31,'2056년',21),
  C(758,431,18,18,K),C(906,385,18,18,K),C(1054,340,18,18,K),
  center(706,406,120,28,'1.2조',20),center(854,359,120,28,'1.8조',20),center(1001,314,125,28,'2.4조 원',20),
  Path(709,361,374,187,'M0 183 C173 188 282 145 342 22 L321 26 L356 0 L374 38 L357 34 C289 166 179 197 0 187 Z',{viewBox:'0 0 374 187',fill:K,stroke:'none',el:'chart-line'})
]});

slides.push({id:'slide_06',title:'복지보건 — 촘촘한 복지·보건망',background:BG,elements:[
  ...top('04','복지보건'),heading('단 한 명도 소외 없는 촘촘한 복지·보건망 구축',45.8),
  Path(473,271,171,171,'M171 171 H85.5 A85.5 85.5 0 0 1 0 85.5 A85.5 85.5 0 0 1 85.5 0 A85.5 85.5 0 0 1 171 85.5 Z',{viewBox:'0 0 171 171',fill:GRAY,stroke:K,strokeWidth:1.1}),
  Path(644,271,171,171,'M0 171 V85.5 A85.5 85.5 0 0 1 85.5 0 A85.5 85.5 0 0 1 171 85.5 A85.5 85.5 0 0 1 85.5 171 Z',{viewBox:'0 0 171 171',fill:LIME,stroke:K,strokeWidth:1.1}),
  Path(473,442,171,171,'M171 0 V85.5 A85.5 85.5 0 0 1 85.5 171 A85.5 85.5 0 0 1 0 85.5 A85.5 85.5 0 0 1 85.5 0 Z',{viewBox:'0 0 171 171',fill:BLUE,stroke:K,strokeWidth:1.1}),
  Path(644,442,171,171,'M0 0 H85.5 A85.5 85.5 0 0 1 171 85.5 A85.5 85.5 0 0 1 85.5 171 A85.5 85.5 0 0 1 0 85.5 Z',{viewBox:'0 0 171 171',fill:GRAY,stroke:K,strokeWidth:1.1}),
  center(510,301,97,33,'01',23,{weight:700}),center(681,301,97,33,'02',23,{weight:700}),
  center(510,560,97,33,'03',23,{weight:700,color:W}),center(681,560,97,33,'04',23,{weight:700}),
  icon(529,339,58,61,'ChartNoAxesCombined',K,{strokeWidth:1.6}),icon(702,339,55,60,'UserRound',K,{strokeWidth:1.7}),
  icon(526,486,65,55,'BriefcaseBusiness',W,{strokeWidth:1.5}),icon(698,484,61,57,'HeartPulse',K,{strokeWidth:1.6}),
  L(435,352,473,352,K,1),dot(435,352),L(815,352,845,352,K,1),dot(845,352),
  L(435,529,473,529,K,1),dot(435,529),L(815,529,845,529,K,1),dot(845,529),
  text(129,307,288,34,'복지·보건 핵심 인프라 성과',22,{weight:700,align:'right'}),
  text(129,341,288,54,'공공 의료·복지 서비스 수혜 시민 수\n총 125,000명',20,{align:'right',lineHeight:1.4}),
  L(131,441,415,441,K,1.2),
  text(129,487,288,34,'어르신·교통약자',22,{weight:700,align:'right'}),
  text(129,521,288,54,'노인 일자리 3,500개 창출\n저상버스 도입률 85% 달성',20,{align:'right',lineHeight:1.4}),
  text(863,307,287,34,'아동·청소년',22,{weight:700}),
  text(863,341,302,54,'국공립 어린이집 12개소 신설\n맞벌이 돌봄교실 이용률 40% 증가',20,{lineHeight:1.4}),
  L(861,441,1145,441,K,1.2),
  text(863,487,287,34,'공공 보건',22,{weight:700}),
  text(863,521,302,54,'보건소 원스톱 건강증진센터 개관\n취약계층 의료비 지원 20억 투입',20,{lineHeight:1.4})
]});

slides.push({id:'slide_07',title:'도시환경안전 — 녹색 도시 전환',background:BG,elements:[
  ...top('05','도시환경안전'),heading('탄소중립을 향한 녹색 도시 전환 프로세스',46.5),
  ...[
    {x:110,w:250,n:'01',name:'녹지 조성',fig:'5',unit:'곳',note:'도시숲 5곳 신규 개장',ic:'Sprout',fx:202,ux:241},
    {x:381,w:250,n:'02',name:'친환경차',fig:'1,200',unit:'대',note:'전기·수소차 1,200대 보급',ic:'CarFront',fx:426,ux:565},
    {x:653,w:250,n:'03',name:'자원 순환',fig:'30',unit:'소',note:'스마트 재활용 거점 30소 운영',ic:'Atom',fx:735,ux:808},
    {x:924,w:250,n:'04',name:'에너지 절감',fig:'100',unit:'%',note:'공공건물 태양광 설치 100%',ic:'Sun',fx:989,ux:1088}
  ].flatMap(a=>[
    box(a.x,268,a.w,74,GRAY),box(a.x,361,a.w,260,BLUE),
    C(a.x+104,245,41,41,LIME,{stroke:K,strokeWidth:1.15}),center(a.x+104,254,41,27,a.n,20,{weight:700}),
    center(a.x+10,297,a.w-20,32,a.name,22,{weight:700}),
    text(a.fx,400,a.unit==='대'?145:110,84,a.fig,56,{weight:700,color:W,letterSpacing:-1.8,el:'metric'}),
    text(a.ux,432,40,32,a.unit,22,{weight:600,color:W}),center(a.x+8,472,a.w-16,33,a.note,19,{color:W}),
    icon(a.x+94,523,62,62,a.ic,W,{strokeWidth:1.4})
  ]),
  ...[[360,381],[631,653],[903,924]].flatMap(([x,x2])=>[L(x,306,x2,306,K,1.1),dot(x,306),dot(x2,306)])
]});

slides.push({id:'slide_08',title:'교육문화관광 — 시민의 일상',background:BG,elements:[
  ...top('06','교육문화관광'),heading('시민의 일상을 채우는 교육·문화·관광',45.2),
  text(111,249,199,124,'Education\nCulture\nTourism',32,{font:'Pretendard',weight:700,lineHeight:1.18,letterSpacing:-0.8}),ph(274,266,165,167),
  ...[
    {x:474,y:246,w:337,n:'01',name:'문화',note:'연간 문화행사 120회 개최',ic:'CalendarClock',color:LIME},
    {x:838,y:246,w:337,n:'02',name:'교육',note:'미래교육지원센터 개관',ic:'PanelsTopLeft',color:BLUE},
    {x:110,y:448,w:336,n:'03',name:'관광',note:'수변공원 방문객 100만 명',ic:'MapPinned',color:LIME},
    {x:474,y:448,w:337,n:'04',name:'체육',note:'생활체육시설 8개소 신설',ic:'Dribbble',color:BLUE},
    {x:838,y:448,w:337,n:'05',name:'축제',note:'빛축제 지역경제 효과 150억',ic:'Sparkles',color:LIME}
  ].flatMap(a=>[
    box(a.x,a.y,a.w,172,GRAY),C(a.x+28,a.y+21,41,41,a.color,{stroke:K,strokeWidth:1.15}),
    center(a.x+28,a.y+30,41,28,a.n,20,{weight:700,color:a.color===BLUE?W:K}),
    text(a.x+28,a.y+82,a.w-60,39,a.name,25,{weight:700}),text(a.x+28,a.y+119,a.w-55,35,a.note,19),
    icon(a.x+a.w-78,a.y+95,53,53,a.ic,K,{strokeWidth:1.55})
  ])
]});

const library={
  slide_01:{folder:'card',items:[{name:'2056년도 주요 성과 보고',note:'미리시, 성장의 기록 · ANNUAL RESULTS REPORT'},{name:'보고 기관',note:'미리시청 기획조정실'},{name:'보고 일자',fig:'2056. 12. 30',note:'PERFORMANCE REPORT'}]},
  slide_02:{folder:'agenda',items:[{name:'핵심 주요 성과',note:'대시보드'},{name:'분야별 추진 실적',note:'경제·복지·환경·문화'},{name:'예산 결산 및 만족도',note:'지표·추이'},{name:'대외 평가 및 시민 목소리',note:'수상·인터뷰'},{name:'향후 과제 및 비전',note:'목표'}]},
  slide_03:{folder:'card',items:[{name:'활력 경제',note:'지역상권 회복 및 일자리 창출'},{name:'포용 복지',note:'단 한 명도 소외 없는 맞춤 복지'},{name:'친환경 도시',note:'탄소중립 실천 및 녹색공간 확충'}]},
  slide_04:{folder:'metric',items:[{fig:'2.4조 원',name:'투자 유치',note:'전년 대비 135% 달성'},{fig:'18,500개',name:'일자리 창출',note:'목표치 초과 달성'},{fig:'92.4점',name:'시민 만족도',note:'역대 최고치 기록'},{fig:'450억 원',name:'공공예산 절감',note:'사업 구조조정'}]},
  slide_05:{folder:'metric',items:[{fig:'98.2%',name:'소상공인 지원금 집행률',note:'주요 경제 지표 추이'},{fig:'142개사',name:'청년 창업 지원 기업 수',note:'전년比 +28%'},{fig:'1.2조 → 2.4조 원',name:'지역 경제 규모 추이',note:'2054년 1.2조 · 2055년 1.8조 · 2056년 2.4조 원'}]},
  slide_06:{folder:'card',items:[{name:'복지·보건 핵심 인프라 성과',fig:'125,000명',note:'공공 의료·복지 서비스 수혜 시민 수'},{name:'아동·청소년',note:'국공립 어린이집 12개소 신설 · 맞벌이 돌봄교실 이용률 40% 증가'},{name:'어르신·교통약자',note:'노인 일자리 3,500개 창출 · 저상버스 도입률 85% 달성'},{name:'공공 보건',note:'보건소 원스톱 건강증진센터 개관 · 취약계층 의료비 지원 20억 투입'}]},
  slide_07:{folder:'steps',items:[{name:'녹지 조성',note:'도시숲 5곳 신규 개장'},{name:'친환경차',note:'전기·수소차 1,200대 보급'},{name:'자원 순환',note:'스마트 재활용 거점 30소 운영'},{name:'에너지 절감',note:'공공건물 태양광 설치 100%'}]},
  slide_08:{folder:'card',items:[{name:'문화',note:'연간 문화행사 120회 개최'},{name:'교육',note:'미래교육지원센터 개관'},{name:'관광',note:'수변공원 방문객 100만 명'},{name:'체육',note:'생활체육시설 8개소 신설'},{name:'축제',note:'빛축제 지역경제 효과 150억'}]}
};
for(const s of slides)s.library=library[s.id];
export default {id:'009',title:'2056 미리시 연간 주요 성과 보고',slides};
