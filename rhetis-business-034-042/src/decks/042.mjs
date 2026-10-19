import {T,R,C,L,S,I,P,slide} from '../primitives.mjs';
const ic=(x,y,size,name,color,opts={})=>I(x,y,size,name,color,{sw:0.9,...opts});
const B='#123fbd', D='#1234aa', INK='#3d4656', BLUE='#3567da', MID='#5c8ee9', PALE='#9db9ef', GRAY='#eaecee', WHITE='#ffffff';
const tx=(x,y,w,h,text,size=20,color=INK,weight=400,opts={})=>T(x,y,w,h,text,size,color,weight,{lineHeight:1.34,...opts});
const svg=(x,y,w,h,body)=>S(x,y,w,h,`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" fill="none">${body}</svg>`);
const check=(x,y,label)=>[R(x,y+8,13,13,B,1),svg(x+2,y+10,9,9,'<path d="m1 4 2.5 2.5L8 1.5" stroke="white" stroke-width="1.5"/>'),tx(x+24,y,390,34,label,23,INK,600)];
const logo=()=>[svg(38,676,21,10,'<path d="m0 7 3-4h3L3 7zm5 0L10 0h4L9 7zm6 0 5-7h4l-5 7z" fill="#164bad"/>'),tx(62,675,90,15,'MIRI COMPANY',10,INK,500)];
const corner=(x=1205,y=0)=>svg(x,y,75,91,'<path d="M45 0H75L30 45H0z" fill="#3567da"/><path d="M30 45H60L15 91H-15z" fill="#9db9ef"/>');
function shell(page,section,title,active,main){
 const two=page>=5, subs=two?['사업 환경 변화','사업 KPI 체계','주요 추진 현황']:['사업 개요','연간 목표 & 추진 방향'];
 return [R(0,0,174,720,'#f9f9fb'),R(0,0,12,720,'#dce0e6'),R(170,0,5,720,'#eeeeef'),R(0,125,12,two?154:123,BLUE),tx(36,43,130,35,'MIRI COMPANY\n2099 사업성과 보고서',11,INK),L(36,90,174,90,'#94add9',1.5),tx(38,120,120,40,two?'02.':'01.',28,BLUE,700),tx(37,160,136,27,section,16,BLUE,600),L(36,190,174,190,BLUE,1),subs.map((a,i)=>[tx(active===i?38:52,199+i*29,133,25,(active===i?'▸  ':'')+a,11,active===i?BLUE:'#92979e',active===i?600:400),L(36,220+i*29,174,220+i*29,'#c8c8cb',1)]),logo(),tx(239,51,850,32,title,20,INK,600),L(239,90,1205,90,'#97afd4',1.2),tx(1164,65,28,22,String(page).padStart(2,'0'),13,'#174992',500,{align:'center'}),corner(),tx(239,120,974,100,main,32,'#164b9f',600,{lineHeight:1.44})];
}
function doubleCard(x,w,title,icon,color,first,second){return [R(x,310,w,357,GRAY),R(x,310,w,159,color),ic(x+w/2-29,348,58,icon,WHITE),tx(x+10,422,w-20,35,title,21,WHITE,600,{align:'center'}),R(x+11,489,w-22,73,WHITE,0,'#d7dfeb',0.7),R(x+11,579,w-22,73,WHITE,0,'#d7dfeb',0.7),P(x+w/2-10,480,20,20,'1','#86afea',WHITE,16),P(x+w/2-10,569,20,20,'2','#86afea',WHITE,16),tx(x+15,507,w-30,50,first,17,INK,400,{align:'center'}),tx(x+15,579,w-30,73,second,17,INK,400,{align:'center',valign:'center'})];}
const slides=[];
slides.push(slide('slide_01','2099 사업 성과 보고서',[
 svg(0,0,1280,720,'<path d="M0 0h130L0 130z" fill="#e1e5e9"/><path d="M1280 146v190l-185 185H905z" fill="#123fbd"/><path d="M1174 442h106v81l-195 197H895z" fill="#9bb7ef"/><path d="M715 521h190L705 720H515z" fill="#e1e5e9"/>'),
 P(84,169,146,28,'2099. 12. 22',WHITE,INK,17,{stroke:'#62676c',sw:1,weight:600}),tx(83,224,1000,100,'MIRI COMPANY',80,B,800,{tracking:1,lineHeight:1.2}),tx(88,319,900,85,'2099 사업 성과 보고서',57,INK,500,{tracking:-2}),
 tx(89,549,70,29,'mail.',18,B,700),tx(143,549,400,29,'contact@miridih.com',18,INK),tx(89,587,50,29,'tel.',18,B,700),tx(125,587,400,29,'030-000-0000',18,INK),tx(89,625,100,29,'address.',18,B,700),tx(171,628,350,29,'미리시 미리로 미리구 7',14,INK)
]));
slides.push(slide('slide_02','CONTENTS',[
 tx(113,91,450,55,'이곳에 프레젠테이션의\n핵심 주제나 슬로건을 입력해 보세요.',17,INK),tx(112,150,600,78,'CONTENTS',50,B,800,{tracking:0.5}),
 ...[{n:'01.',t:'사업 개요 및 목표',s:['사업 개요','연간 목표 & 추진 방향']},{n:'02.',t:'사업 환경 분석',s:['사업 환경 변화','사업 KPI 체계','주요 추진 현황']},{n:'03.',t:'주요 성과',s:['핵심 성과 요약','프로젝트별 성과']},{n:'04.',t:'프로젝트 상세',s:['세부 프로젝트','세부 프로젝트 상세내용','프로젝트 성공요인','고객 관련 성과','운영 관련 성과','핵심 이슈 및 개선']},{n:'05.',t:'향후 계획',s:['차년도 핵심 전략','차년도 추진 계획','요약 및 추후 방향']}].map((d,i)=>{let x=113+220.5*i;return [tx(x,338,180,62,d.n,46,INK,400),L(x,410,x+155,410,'#7c98d3',2),tx(x,425,200,36,d.t,22,INK,600),d.s.map((s,j)=>tx(x,486+j*26,186,24,s,12,'#737980'))];}),
 svg(0,430,1280,290,'<path d="M1280 0v89l-87 87h-88z" fill="#123fbd"/><path d="M1230 140h50v42l-91 88h-88z" fill="#9bb7ef"/><path d="M0 270h1100l-20 20H0z" fill="#123fbd"/>')
]));
slides.push(slide('slide_03','사업 개요',[
 shell(3,'사업 개요 및 목표','사업 개요',0,'본 사업은 취향 기반 콘텐츠·커뮤니티 플랫폼을 통해 사용자 확보 및\n광고·제휴 수익을 창출'),check(239,272,'사업 구성 요소'),check(846,272,'사업 운영 구조'),
 doubleCard(238,191,'유료 콘텐츠','banknote', '#2454cd','전문 큐레이션\n콘텐츠 판매','구독형 멤버십 운영'),doubleCard(435,191,'브랜드 제휴 캠페인','handshake',MID,'기업 브랜드와\n공동 콘텐츠 제작','커뮤니티 참여형\n이벤트 운영'),doubleCard(631,192,'커뮤니티 기반 광고','network','#2454cd','게시글/피드 기반\n광고 노출','카테고리 타깃형\n광고 상품 운영'),
 R(847,312,340,357,GRAY),svg(880,356,272,268,'<circle cx="136" cy="134" r="99" stroke="white" stroke-width="22"/><path d="M15 149C-1 88 42 18 99 13M208 28c54 27 69 97 43 141M188 246c-55 34-114 7-142-20" stroke="#8c9dce" stroke-width="2"/><path d="m14 143 1 9 5-8m182-119 9 2-5 5m-24 238 8-6-10 1" stroke="#8c9dce" stroke-width="2"/>'),
 C(970,330,95,D),C(876,508,95,BLUE),C(1063,508,95,'#85aded'),tx(986,353,64,60,'콘텐츠\n공급',19,WHITE,600,{align:'center'}),tx(888,533,72,58,'사용자\n활동',19,WHITE,600,{align:'center'}),tx(1075,533,72,58,'키워드\n입력란',19,WHITE,600,{align:'center'}),tx(941,484,152,30,'MIRI COMPANY',18,B,700,{align:'center'}),tx(869,635,298,25,'이곳에 사업의 작동 원리나 순환구조를 설명해 보세요.',12,'#646a74',{align:'center'})
]));
const strategies=[{x:239,c:BLUE,icon:'lightbulb',title:'핵심 카테고리 콘텐츠 공급 확대',lines:['일간 인기 콘텐츠 큐레이션 강화','신규 게시글 생성 프로그램 운영']},{x:558,c:MID,icon:'hand-heart',title:'사용자 참여 촉진 구조 고도화',lines:['참여형 캠페인 운영','목표 달성을 위한 두 번째 전략적\n   방향을 입력해 보세요.']},{x:878,c:BLUE,icon:'megaphone',title:'광고·제휴 상품 경쟁력 강화',lines:['브랜드 협업형 콘텐츠 패키지 개발','목표 달성을 위한 세 번째 전략적\n   방향을 입력해 보세요.']}];
slides.push(slide('slide_04','연간 목표 & 추진 방향',[
 shell(4,'사업 개요 및 목표','연간 목표 & 추진 방향',1,'사용자 참여 확대 및 광고·제휴 수익 강화를 위해 연초 설정한 핵심 전략 방향'),
 svg(239,331,947,90,'<defs><linearGradient id="shade" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#cfd3d7"/><stop offset="1" stop-color="#fff"/></linearGradient></defs><path d="M180 0H765L947 90H0z" fill="url(#shade)"/>'),R(239,253,945,82,D,13),tx(285,276,390,42,'커뮤니티 활동량 확대 및 체류 시간 증가',24,WHITE,600,{align:'center'}),P(690,280,28,28,'+',WHITE,BLUE,24,{weight:700}),tx(734,276,412,42,'광고·제휴 전략 확대로 수익 구조 기반 강화',24,WHITE,600,{align:'center'}),
 strategies.map(a=>[R(a.x,418,309,249,'#eef0f3'),R(a.x,418,309,105,a.c),C(a.x+109,368,91,WHITE,a.c,2.5),ic(a.x+132,389,45,a.icon,'#275abd'),tx(a.x+10,474,289,39,a.title,22,WHITE,600,{align:'center'}),a.lines.map((l,i)=>tx(a.x+26,546+i*37,280,64,'•  '+l,19,INK))])
]));
function pest(){return [
 R(239,278,951,392,GRAY),R(257,299,579,350,WHITE,3),
 svg(422,349,250,250,'<path d="M125 0A125 125 0 0 0 0 125h52A73 73 0 0 1 125 52z" fill="#1234aa"/><path d="M125 0A125 125 0 0 1 250 125h-52A73 73 0 0 0 125 52z" fill="#3567da"/><path d="M250 125A125 125 0 0 1 125 250v-52a73 73 0 0 0 73-73z" fill="#a9c9f4"/><path d="M125 250A125 125 0 0 1 0 125h52a73 73 0 0 0 73 73z" fill="#86aced"/>'),
 L(547,311,547,346,'#8b8b8b',1,{dash:'2 2'}),L(547,607,547,638,'#8b8b8b',1),L(277,474,410,474,'#8b8b8b',1),L(682,474,815,474,'#8b8b8b',1),
 [[428,355,'P','#2447ba'],[606,355,'E',BLUE],[428,532,'S','#86aced'],[606,532,'T','#a9c9f4']].map(([x,y,t,c])=>[C(x,y,60,c),C(x+11,y+11,38,WHITE),tx(x+15,y+16,30,30,t,21,'#264aa8',700,{align:'center'})]),tx(498,438,100,78,'PEST\n분석',28,'#284ab0',700,{align:'center',lineHeight:1.2}),
 P(280,318,120,31,'정책 규제',D,WHITE,18),tx(284,363,148,94,'•  커뮤니티 내 유해\n   콘텐츠 관리 의무 강화\n•  광고·표기 규정의\n   세분화',15,INK,400,{lineHeight:1.5}),
 P(696,318,119,31,'경쟁사',BLUE,WHITE,18),tx(682,363,133,94,'•  이곳에 해당 분야에\n   나타난 주요 변화\n   1~2개를\n   입력해 보세요.',15,INK,400,{align:'right',lineHeight:1.5}),
 P(280,505,120,31,'고객 니즈','#86aced',WHITE,18),tx(284,549,157,90,'•  이곳에 해당 분야에\n   나타난 주요 변화\n   1~2개를 입력해 보세요.',15,INK,400,{lineHeight:1.5}),
 P(696,505,119,31,'기술 변화','#a9c9f4',WHITE,18),tx(673,550,146,85,'• 개인화 추천기술고도화\n• 숏폼, 실시간 콘텐츠\n   소비 증가',14,INK,400,{align:'right',lineHeight:1.5}),
 svg(835,311,49,331,'<defs><linearGradient id="pestArrow"><stop stop-color="#eaecee"/><stop offset="1" stop-color="#a9bfed"/></linearGradient></defs><path d="m0 0 49 165L0 331z" fill="url(#pestArrow)"/>'),
 [0,1,2].map(i=>R(887,299+i*75,280,71,WHITE)),tx(900,309,254,55,'고객 니즈가\n신뢰 기반 커뮤니티 선호로 이동',18,INK,400,{align:'center'}),tx(900,384,254,55,'기술·규제 변화로\n콘텐츠 품질 강화 요구 증가',18,INK,400,{align:'center'}),tx(900,459,254,55,'외부환경의\n핵심 변화를 요약해 보세요.',18,INK,400,{align:'center'}),R(887,528,280,122,BLUE,4),tx(898,545,258,94,'외부 환경 변화가\n실제 사업 방향·전략·성과에 미친\n영향을 정리해 입력해 보세요.',19,WHITE,600,{align:'center',lineHeight:1.45})
];}
slides.push(slide('slide_05','사업 환경 변화',[shell(5,'사업 환경 분석','사업 환경 변화',0,'20XX년 외부 환경 변화로 콘텐츠 신뢰성과 커뮤니티 품질이\n핵심 경쟁 요소로 부상'),pest()]));
const metricRow=(y,label,cells)=>[check(268,y,label),cells.map((t,i)=>[R(266+i*146,y+38,139,77,WHITE),R(266+i*146,y+38,139,3,'#a1bdea'),tx(272+i*146,y+38,127,77,t,18,INK,400,{align:'center',valign:'center',lineHeight:1.4})])];
slides.push(slide('slide_06','사업 KPI 체계',[
 shell(6,'사업 환경 분석','사업 KPI 체계',1,'매출·고객·전환율 중심의 사업 성과 측정 체계 및 핵심 지표 구조'),R(239,226,944,441,GRAY),metricRow(249,'매출 (Revenue)',['광고 매출','제휴 매출','유료 콘텐츠\n매출']),metricRow(387,'고객수 (Customers)',['신규 고객\n확보 수','이탈률','고객 생애 가치\n(LTV)']),metricRow(525,'전환율 (Conversion)',['구매 완료율','특정 기능 이용률','콘텐츠 클릭률\n(CTR)']),
 svg(718,251,1,390,'<path d="M.5 0V390" stroke="#777" stroke-width="1" stroke-dasharray="1.5 2"/>'),P(841,262,210,46,'성과','#2446b1',WHITE,26),L(945,309,945,337,'#969c9e',1.3),svg(830,337,230,30,'<path d="M0 25V7q0-7 7-7h216q7 0 7 7v18" stroke="#969c9e" stroke-width="1.3"/>'),
 [[778,'chart-line',735,'콘텐츠 노출량 증가','카테고리 별 노출수','추천 피드 도달률'],[1001,'coins',958,'광고 상품 이용률 증가','관련 세부지표 입력란','관련 세부지표 입력란']].map(([x,icon,bx,title,a,b])=>[C(x,364,118,'#bcdbf9'),ic(x+32,394,55,icon,'#3b68ca'),R(bx,465,204,50,MID,8),tx(bx+7,475,190,35,title,21,WHITE,600,{align:'center'}),L(bx+96,515,bx+96,589,'#a1a6a9',1),R(bx+2,529,200,51,WHITE),R(bx+2,589,200,51,WHITE),tx(bx+9,541,186,35,a,18,INK,400,{align:'center'}),tx(bx+9,601,186,35,b,18,INK,400,{align:'center'})])
]));
const execution=[{x:239,c:BLUE,title:'콘텐츠 공급 강화',icon:'newspaper',lines:['신규 테마 콘텐츠 시리즈 제작','인기 콘텐츠 큐레이션 재편'],v:78},{x:558,c:MID,title:'사용자 참여 기능 개선',icon:'message-square-heart',lines:['댓글·공감 인터랙션 개선','두 번째 실행 내용을 입력하세요.'],v:64},{x:877,c:BLUE,title:'광고·제휴 상품 고도화',icon:'laptop',lines:['광고 상품 리뉴얼','세 번째 실행 내용을 입력하세요.'],v:90}];
slides.push(slide('slide_07','주요 추진 현황',[
 shell(7,'사업 환경 분석','주요 추진 현황',2,'분기별 핵심 과제 순차 추진으로 연간 목표 달성 기반 마련'),
 ['#a9caf3','#86adee',BLUE,D].map((color,i)=>{let x=239+i*237;return [svg(x,228,247,34,`<path d="M0 0H237l10 17-10 17H0${i?'l10-17':''}z" fill="${color}"/>`),tx(x+15,231,100,31,`${i+1}Q`,21,WHITE,700),tx(x+14,276,219,64,['콘텐츠 공급 기반 확장','사용자 참여 강화 활동 실행','광고·제휴 상품 재정비','운영·정책 정비 및 시스템\n고도화'][i],19,INK),L(x,342,x+226,342,color,2.5),i<3?svg(x+232,267,1,76,'<path d="M.5 0V76" stroke="#aaa" stroke-dasharray="1 2"/>'):null];}),
 check(240,383,'주요 실행 항목'),execution.map(a=>[R(a.x,423,310,243,GRAY),R(a.x,423,310,80,a.c),tx(a.x+20,446,224,38,a.title,24,WHITE,600),ic(a.x+239,439,46,a.icon,'#c6dcf9'),a.lines.map((t,i)=>tx(a.x+17,523+i*35,284,35,'•  '+t,20,INK)),tx(a.x+23,606,110,22,'진행률',13,BLUE),tx(a.x+185,596,56,32,`${a.v}%`,22,B,700,{align:'right'}),R(a.x+23,628,271,15,WHITE),R(a.x+23,628,271*a.v/100,15,'#2855cb')])
]));
export default {id:'042',title:'MIRI COMPANY — 2099 사업 성과 보고서',slides};
