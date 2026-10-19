import {T,R,C,L,PH,S,I,P,slide} from '../primitives.mjs';
const B='#1746bd',D='#1739b4',INK='#505761',BLUE='#356bd6',MID='#5d92e9',PALE='#a6c7ef',GRAY='#eaecee',WHITE='#ffffff';
const tx=(x,y,w,h,text,size=20,color=INK,weight=400,opts={})=>T(x,y,w,h,text,size,color,weight,{lineHeight:1.34,...opts});
const svg=(x,y,w,h,body)=>S(x,y,w,h,`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" fill="none">${body}</svg>`);
const ic=(x,y,size,name,color=B,opts={})=>I(x,y,size,name,color,{sw:1.15,...opts});
const check=(x,y,label,size=22,color='#3d4656')=>[R(x,y+7,13,13,B,1),svg(x+2,y+9,9,9,'<path d="m1 4 2.5 2.5L8 1.5" stroke="white" stroke-width="1.5"/>'),tx(x+24,y,wFor(label,size),label.includes('\n')?68:36,label,size,color,600)];
const wFor=(s,size)=>Math.max(160,s.length*size);
const outlineCheck=(x,y)=>[R(x,y+8,12,12,'transparent',0,'#345b9c',1),svg(x+2,y+7,14,13,'<path d="m0 6 4 4L13 0" stroke="#164db5" stroke-width="1.1"/>')];
const logo=()=>[svg(38,676,21,10,'<path d="m0 7 3-4h3L3 7zm5 0L10 0h4L9 7zm6 0 5-7h4l-5 7z" fill="#164bad"/>'),tx(62,675,90,15,'MIRI COMPANY',10,INK,500)];
const corner=()=>svg(1205,0,75,91,'<path d="M45 0H75L30 45H0z" fill="#3567da"/><path d="M30 45H60L15 91H-15z" fill="#9db9ef"/>');
function shell(page,title,main='',opts={}){
 let group=page<10?3:page<16?4:5,section=group===3?'주요 성과':group===4?'프로젝트 상세':'향후 계획',subs=group===3?['핵심 성과 요약','프로젝트별 성과']:group===4?['세부 프로젝트','세부 프로젝트 상세내용','프로젝트 성공요인','고객 관련 성과','운영 관련 성과','핵심 이슈 및 개선']:['차년도 핵심 전략','차년도 추진 계획','요약 및 추후 방향'],active=page-(group===3?8:group===4?10:16);
 return [R(0,0,174,720,'#fafafb'),R(0,0,12,720,'#dce0e6'),svg(166,0,9,720,'<defs><linearGradient id="sidebar"><stop stop-color="#f6f6f6"/><stop offset="1" stop-color="#e5e5e5"/></linearGradient></defs><path d="M0 0H9V720H0z" fill="url(#sidebar)"/>'),R(0,125,12,group===4?239:group===5?154:124,BLUE),tx(36,43,133,35,'MIRI COMPANY\n2099 사업성과 보고서',11,INK),L(36,90,174,90,'#94add9',1.5),tx(38,120,120,40,`0${group}.`,28,BLUE,700),tx(37,160,136,27,section,16,BLUE,600),L(36,190,174,190,BLUE,1),subs.map((a,i)=>[tx(active===i?38:52,199+i*29,136,25,(active===i?'▸  ':'')+a,11,active===i?BLUE:'#969a9f',active===i?600:400),L(36,220+i*29,174,220+i*29,'#c8c8cb',1)]),logo(),tx(239,51,850,32,title,20,'#3d4656',600),L(239,90,1205,90,'#97afd4',1.2),tx(1164,65,28,22,String(page).padStart(2,'0'),13,'#174992',500,{align:'center'}),corner(),main?tx(239,120,974,103,main,34,'#194d9e',600,{lineHeight:1.43,...opts}):null];
}
function lineChart(x,y,w,h,values,color=BLUE){let pad=11,by=y+h-18,pts=values.map((v,i)=>[x+47+i*(w-99)/(values.length-1),by-(h-35)*v]);return [R(x,y,w,h,'#e8f2fc'),L(x+pad,y+7,x+pad,by,'#c8cdd1',1),L(x+pad,by,x+w-15,by,'#c8cdd1',1),...pts.slice(1).map((p,i)=>L(pts[i][0],pts[i][1],p[0],p[1],'#628cd0',0.8)),pts.map((p,i)=>[C(p[0]-4.5,p[1]-4.5,9,color),tx(p[0]-16,by+2,32,15,`${i+1}Q`,10,color,400,{align:'center'})])];}
function rich(x,y,runs){let xx=x;return runs.map(([text,width,bold])=>{let w=width-text.length*.2;const r=tx(xx,y,w+3,34,text,20,bold?'#194a9c':INK,bold?600:400,{tracking:-.2});xx+=w;return r;});}
const slides=[];
slides.push(slide('slide_08','핵심 성과 요약',[
 shell(8,'핵심 성과 요약','주요 지표 전년 대비 고른 상승, 참여율 및 콘텐츠 소비 증가가 핵심 동력'),check(239,243,'주요 지표'),check(625,243,'설치 수 및 MAU 추이'),R(239,285,372,383,'#d2e1f8'),R(625,285,562,383,GRAY),
 [{x:262,y:308,t:'MAU',n:'85',u:'만 명',nx:279,ux:347},{x:430,y:308,t:'참여율',n:'+34',u:'%',nx:441,ux:540},{x:262,y:482,t:'광고 매출',n:'30',u:'억 원',nx:279,ux:346},{x:430,y:482,t:'커뮤니티\n만족도',n:'4.5',u:'점',nx:447,ux:529}].map(o=>[R(o.x,o.y,159,164,WHITE,3),tx(o.x+20,o.y+18,130,65,o.t,22,INK,500,{lineHeight:1.25}),tx(o.nx,o.y+(o.y===482?79:87),120,67,o.n,58,B,700,{tracking:-2.5}),tx(o.ux,o.y+(o.y===482?111:119),75,31,o.u,21,B,600)]),
 R(985,254,43,16,PALE),tx(1035,250,72,27,'설치 수',16),L(1099,262,1136,262,MID,1.2),C(1113,257,10,MID),tx(1141,250,60,27,'MAU',16),L(660,324,660,621,'#c6c9cf',1),L(660,621,1155,621,'#c6c9cf',1),
 [178,219,267,309].map((v,i)=>{let x=687+i*124;return [i<3?R(x,621-v,69,v,PALE):svg(x,312,77,317,'<defs><linearGradient id="bar08" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#143db9"/><stop offset="1" stop-color="#a8c8f1"/></linearGradient></defs><path d="M0 0H77V317H0z" fill="url(#bar08)"/>'),tx(x+10,632,54,24,`${i+1}Q`,16,'#3d6ab5',600,{align:'center'})];}),
 tx(686,327,260,66,'이곳에 추세에 관한 설명을\n입력해 보세요.',20,'#2c5bb7',600,{lineHeight:1.5}),svg(715,383,383,117,'<path d="M6 110L130 58 254 33 377 7" stroke="#6d90c5" stroke-width=".7"/>'),[[721,493],[845,441],[968,416],[1092,390]].map(([x,y])=>C(x-6,y-6,12,MID))
]));
slides.push(slide('slide_09','프로젝트별 성과',[
 shell(9,'프로젝트별 성과','3개 프로젝트 모두 핵심 지표에서 일정 수준 이상의 개선을 보이며\n안정적인 성과 달성'),R(239,269,944,398,GRAY),
 [['성과\n요약',326],['관련\n수치',435],['분기별\n지표',532]].map(([t,y])=>[L(258,y,314,y,'#9ca3aa',1),tx(259,y+8,54,64,t,16)]),
 [{x:322,c:MID,t:'프로젝트 1',summary:'월간 신규 게시글 수와\n주간 재방문율 모두\n목표 대비 높은 수준으로 상승',icon:'flag',a:'신규 게시글',av:'+28',au:'%',b:'활동 전환율',bv:'+7',bu:'%',v:[.47,.52,.83]},
 {x:606,c:BLUE,t:'프로젝트 2',summary:'댓글·공감 수 증가와\n참여 기반\n전환율 향상에 기여',icon:'heart-plus',a:'참여 액션',av:'XX',au:'만 건',b:'참여율',bv:'+14',bu:'%',v:[.48,.71,.83]},
 {x:890,c:'#2453c6',t:'프로젝트 3',summary:'광고 상품 이용률과\n제휴 캠페인 수 모두\n성장세 유지',icon:'megaphone',a:'성과 1',av:'XX',au:'%',b:'성과 2',bv:'XX',bu:'%',v:[.53,.55,.83]}].map(o=>[R(o.x,285,277,34,o.c,5),tx(o.x+8,287,261,30,o.t,22,WHITE,500,{align:'center'}),R(o.x,323,277,329,WHITE,3),tx(o.x+20,338,190,78,o.summary,16,INK,400,{lineHeight:1.55}),C(o.x+201,338,62,o.c===' #2453c6'?MID:o.x===322?'#b2cef3':o.x===606?'#97b6ed':'#81a7e8'),ic(o.x+214,350,37,o.icon,WHITE),[434,483].map((y,j)=>[L(o.x+21,y,o.x+252,y,'#aaa',1),tx(o.x+20,y+8,158,29,j?o.b:o.a,18,'#2552b6',500),tx(o.x+164,y+1,74,40,j?o.bv:o.av,29,'#1338a6',700,{align:'right',tracking:-1}),tx(o.x+238,y+6,38,28,j?o.bu:o.au,15,'#1338a6',600)]),lineChart(o.x+18,530,241,103,o.v)])
]));
slides.push(slide('slide_10','세부 프로젝트',[
 shell(10,'세부 프로젝트','세부 프로젝트 추진을 통한 콘텐츠 노출·유입 구조 개선 및 핵심 지표 향상'),check(240,232,'목표'),check(558,232,'접근 방식'),check(874,232,'핵심 지표'),
 [240,557,873].map((x,i)=>R(x,266,i===2?315:308,124,'#e3ecfa')),
 [[260,'콘텐츠 노출 경로 개선','신규 유입 고객의 소비 경험 강화'],[577,'사용자 행동 기반 추천 구조 개편','첫 화면 콘텐츠 큐레이션 재설계']].map(([x,a,b])=>[outlineCheck(x,285),tx(x+25,285,273,35,a,20),L(x,326,x+271,326,'#a7b3c1',.7,{dash:'1 2'}),outlineCheck(x,341),tx(x+25,341,273,35,b,20)]),
 tx(896,285,190,32,'첫 노출 도달 수',20),tx(1065,277,101,46,'1,234',35,B,600,{align:'right'}),L(886,326,1179,326,'#a7b3c1',.7,{dash:'1 2'}),tx(896,341,190,32,'수치 관련 키워드',20),tx(1080,334,86,46,'50%',35,B,600,{align:'right'}),R(240,396,948,272,GRAY),tx(280,420,500,35,'콘텐츠 소비 구조 비중 (단위 %)',22,B,600),
 svg(450,447,204,204,'<circle cx="102" cy="102" r="79" stroke="#81a8eb" stroke-width="46"/><circle cx="102" cy="102" r="79" stroke="#a4c8f2" stroke-width="46" stroke-dasharray="50 447" transform="rotate(0 102 102)"/><circle cx="102" cy="102" r="79" stroke="#1536ac" stroke-width="46" stroke-dasharray="198.55 297.8" transform="rotate(36 102 102)"/><circle cx="102" cy="102" r="79" stroke="#5d91e8" stroke-width="46" stroke-dasharray="124.1 372.3" transform="rotate(180 102 102)"/>'),
 tx(509,520,88,62,'콘텐츠\n소비',20,B,600,{align:'center'}),
 [[281,479,'추천기반','25%',473,508],[281,564,'검색 기반','40%',473,592],[767,479,'피드 기반','25%',636,509],[767,564,'관련 키워드','10%',636,592]].map(([x,y,t,v,lx,ly],i)=>[tx(i<2?x:x-60,y,i<2?110:139,30,t,18,INK,400,{align:i<2?'left':'right'}),tx(x,y+31,79,38,v,29,B,700,{align:i<2?'left':'right'}),L(i<2?x:lx,ly,i<2?lx:x+79,ly,'#627eac',1)]),R(888,421,270,224,WHITE),tx(913,450,224,178,'이곳에\n그래프가 보여주는\n핵심 변화를\n입력해 보세요.',26,B,600,{align:'center',lineHeight:1.52})
]));
slides.push(slide('slide_11','세부 프로젝트 상세 내용',[
 shell(11,'세부 프로젝트 상세 내용','세부 프로젝트를 통한 콘텐츠 노출 구조 개선 및 초기 소비 경험 강화로\n사용자 유입 최적화'),R(239,260,944,407,GRAY),PH(277,290,154,312,23),PH(464,290,154,312,23),
 svg(393,418,69,64,'<defs><linearGradient id="phonearrow"><stop stop-color="#168cf6" stop-opacity="0"/><stop offset="1" stop-color="#168cf6"/></linearGradient></defs><path d="M0 12H45V0l24 32-24 32V50H0z" fill="url(#phonearrow)"/>'),tx(292,612,128,25,'개선 전 화면',16,INK,600,{align:'center'}),tx(290,636,133,17,'개선 전 이미지를 넣어주세요',9,INK,400,{align:'center'}),tx(479,612,127,25,'개선 화면',16,'#2d5bb1',600,{align:'center'}),tx(479,636,127,17,'개선 된 이미지를 넣어주세요',9,INK,400,{align:'center'}),
 R(649,286,512,145,WHITE),check(668,309,'사업 개요',22,B),tx(677,350,459,70,'• 콘텐츠 노출 구조 개선을 통해 초기 소비 경험을 강화\n• 프로젝트가 해결하고자 한 방향을 입력해 보세요.',20,INK,400,{lineHeight:1.75}),
 R(649,441,512,205,WHITE),check(668,462,'세부 내용',22,B),tx(673,508,319,119,'• 첫 화면 콘텐츠 큐레이션 방식 재정비\n• 사용자 행동 기반 추천 알고리즘 적용\n• 콘텐츠 접근 동선 단축 위한 UI 조정',20,INK,400,{lineHeight:1.85}),
 tx(1029,453,111,25,'초기 콘텐츠 소비',14,'#2c5ca8',400,{align:'center'}),L(966,613,1137,613,'#8f969e',1.2),R(975,576,59,37,'#81a9eb'),R(1057,482,67,131,'#1b4ca9'),tx(982,581,50,18,'10,000건',10,WHITE,400,{align:'center'}),tx(1060,493,61,20,'35,000건',12,WHITE,400,{align:'center'}),tx(985,616,38,19,'1Q',11,INK,400,{align:'center'}),tx(1073,616,38,19,'4Q',11,INK,400,{align:'center'}),svg(980,482,76,94,'<defs><linearGradient id="uparrow" x1="0" y1="1" x2="1" y2="0"><stop stop-color="#d7e3fa" stop-opacity="0"/><stop offset="1" stop-color="#2e63d2"/></linearGradient></defs><path d="M0 94C26 78 42 48 56 18l-11-5L69 0l7 27-12-4C48 65 27 85 0 94" fill="url(#uparrow)"/>')
]));
slides.push(slide('slide_12','프로젝트 성공요인',[
 shell(12,'프로젝트 성공요인','세부 프로젝트의 문제 분석·노출 전략·실행 구조 유기적 결합으로\n핵심 지표 개선 견인'),
 [{x:239,c:'#1d46be',title:'사용자\n행동 분석',icon:'user-round',lines:['주요 이탈 지점 분석을 통한 핵심\n병목 파악','사용자 초기 진입 시나리오 기반\n개선 포인트 도출'],tools:['행동로그 분석 툴','활용 도구를 입력해 보세요.']},{x:565,c:'#3c72d8',title:'일관된\n콘텐츠 노출 전략',icon:'square-pen',lines:['사용자 행동 기반 추천 로직\n일괄 적용','첫 노출 영역의 고정된 큐레이션\n규칙 확립'],tools:['큐레이션 가이드','활용 도구를 입력해 보세요.']},{x:891,c:'#1d46be',title:'신속한\n실행 및 피드백',icon:'messages-square',lines:['배포→측정→보완의 짧은\n주기 운영','지표 기반 개선 방식 정착'],tools:['주간 리뷰 체계','활용 도구를 입력해 보세요.']}].map(o=>[R(o.x,264,296,125,o.c),tx(o.x+28,289,254,84,o.title,27,WHITE,500,{lineHeight:1.5}),ic(o.x+224,319,48,o.icon,'#d3e5fa'),R(o.x,393,296,161,'#e8edfa'),R(o.x,555,296,115,'#f3f4f6'),o.lines.map((t,i)=>[tx(o.x+15,412+i*65,20,27,'✚',18,'#8dafd8',600),tx(o.x+40,414+i*65,246,62,t,19,INK,400,{lineHeight:1.45})]),o.tools.map((t,i)=>tx(o.x+25,578+i*36,264,30,'• '+t,19))]),
 [550,876].map(x=>[L(x,263,x,669,'#8d96a7',1.7,{dash:'2 2'}),P(x-13,376,26,26,'+','#6095e5',WHITE,20,{weight:500}),P(x-13,539,26,26,'+','#a6c7ee',WHITE,20,{weight:500})])
]));
slides.push(slide('slide_13','고객 관련 성과',[
 shell(13,'고객 관련 성과','고객 전환율의 경우 신규·기존 사용자의 커뮤니티 참여율 상승으로\n3Q 및 4Q에서 큰 폭 개선'),R(239,272,538,395,GRAY),R(790,271,397,395,'#e3ecfb'),check(269,295,'고객 전환율 변화 (단위 %)',22,B),
 L(283,348,283,629,'#c7cbd1',1),L(283,629,736,629,'#c7cbd1',1),R(302,362,43,15,PALE),tx(352,357,110,25,'신규 고객',16),R(302,388,43,15,MID),tx(352,383,110,25,'기존 고객',16),
 [[294,558,39,71,PALE],[346,523,39,106,MID],[408,523,39,106,PALE],[459,488,39,141,MID],[521,471,39,158,PALE],[572,453,39,176,MID],[637,401,44,233,PALE],[687,355,47,279,'#2452c4']].map(([x,y,w,h,c],i)=>i===6||i===7?svg(x,y,w,h,`<defs><linearGradient id="bar13${i}" x1="0" y1="0" x2="0" y2="1"><stop stop-color="${i===7?'#2452c4':'#5c91e8'}"/><stop offset="1" stop-color="${i===7?'#5c91e8':'#a6c7ef'}"/></linearGradient></defs><path d="M0 0H${w}V${h}H0z" fill="url(#bar13${i})"/>`):R(x,y,w,h,c)),[337,453,571,687].map((x,i)=>tx(x-18,638,36,23,`${i+1}Q`,13,'#3d4656',500,{align:'center'})),
 check(815,298,'경로 다변화로 신규 사용자 참여 확대',22,B),tx(823,349,345,120,'• 신규 유입의 주요 경로가 커뮤니티 콘텐츠\n  → 추천 흐름으로 이동\n• 콘텐츠 기반 유입 고객의 전환율이\n  기존 대비 +7%p',20,INK,400,{lineHeight:1.47}),check(815,495,'기존 사용자의 반복 참여가\n참여율 향상 견인',22,B),tx(823,574,345,65,'• 기존 고객의 반복 전환 비중이 성장\n• 이용 빈도 증가가 전환율 개선에 직접 기여',20,INK,400,{lineHeight:1.72})
]));
slides.push(slide('slide_14','운영 관련 성과',[
 shell(14,'운영 관련 성과','운영 프로세스의 경우 단절된 업무 체계 연계 개선으로\n효율성 및 일관성 향상'),R(239,272,948,134,GRAY),check(271,296,'운영 상황',22,B),tx(408,295,755,39,'주요 업무에 관한 공유 기회가 적어 정보 전달 지연 및 작업 오류가 자주 발생',22),L(271,339,1162,339,'#818995',1,{dash:'1 2'}),check(271,354,'개선 효과',22,B),tx(408,354,755,39,'역할 간 실시간 상호 검증과 정보 교류가 가능해지며 처리 속도 향상과 오류 감소 효과',22),
 R(239,414,948,254,'#e3ecfb'),R(263,446,377,199,WHITE),R(720,446,442,199,WHITE),L(263,446,639,446,'#6689d2',1),L(263,645,639,645,'#6689d2',1),L(720,446,1162,446,'#6689d2',1),L(720,645,1162,645,'#6689d2',1),P(363,432,176,34,'기존','#356bd6',WHITE,24,{radius:6,weight:500}),P(851,432,180,34,'개선 후','#356bd6',WHITE,24,{radius:6,weight:500}),
 L(451,479,451,629,'#6f737b',1.6,{dash:'2 2'}),[[302,486,'user-round-cog','운영 업무'],[487,486,'user-round-search','검수 업무'],[749,486,'settings','운영'],[1022,486,'file-search','검수']].map(([x,y,icon,title])=>[C(x,y,112,'#cce3f8'),ic(x+26,y+25,63,icon,'#164ca7'),tx(x-5,y+113,122,36,title,22,B,600,{align:'center'})]),
 svg(638,463,77,163,'<defs><linearGradient id="processarrow"><stop stop-color="#a4c7f1" stop-opacity="0"/><stop offset="1" stop-color="#83aaeb"/></linearGradient></defs><path d="M0 0C20 32 31 40 48 41V13l29 64-29 65v-27C28 116 18 130 0 163z" fill="url(#processarrow)"/>'),
 svg(862,511,158,50,'<defs><linearGradient id="backarrow"><stop stop-color="#b6bdc7"/><stop offset="1" stop-color="#f4f5f6"/></linearGradient><linearGradient id="forwardarrow"><stop stop-color="#f4f5f6"/><stop offset="1" stop-color="#b6bdc7"/></linearGradient></defs><path d="m0 14 14-14v7h125v14H14v7z" fill="url(#backarrow)"/><path d="M12 32h132v-7l14 14-14 11v-7H12z" fill="url(#forwardarrow)"/>'),tx(890,496,98,23,'자동 확인',16,'#848b94',400,{align:'center'}),tx(895,557,96,23,'키워드',16,'#848b94',400,{align:'center'})
]));
slides.push(slide('slide_15','핵심 이슈 및 개선',[
 shell(15,'핵심 이슈 및 개선','운영 과정에서 확인된 주요 이슈와 이를 해결하기 위한 개선 방향'),
 svg(362,243,833,39,'<path d="M0 0H383l14 19.5L383 39H0z" fill="#6196f7"/><path d="M383 0H818l15 19.5L818 39H383l14-19.5z" fill="#1539ab"/>'),tx(407,247,313,32,'이슈',24,WHITE,500,{align:'center'}),tx(827,247,313,32,'개선 포인트',24,WHITE,500,{align:'center'}),R(362,294,381,357,'#f7f7f9',5),R(743,293,444,357,GRAY,5),L(743,294,743,648,'#abc6ec',1.1),
 [{y:304,label:'사용자\n경험',a:'초기 진입 시 원하는 콘텐츠를 찾기까지\n단계가 많아 이탈 존재',b:'진입 동선을 단순화하고 핵심 콘텐츠 접근성을\n높이는 구조 개편 검토 필요'},
 {y:421,label:'노출 로직',a:'로직이 사용자 패턴을 충분히 반영하지\n못해 일관성 낮음',b:'사용자 행동 기반 데이터 반영을 강화하고\n추천 기준을 재정비'},
 {y:541,label:'콘텐츠\n품질',a:'사용자 경험에 부정적 영향을 준 문제를\n한 줄로 입력해 보세요.',b:'해결을 위해 향후 추진할 필요가 있는 개선 방향을\n작성해 보세요.'}].map((o,i)=>[R(239,o.y,109,95,['#e8f2fc','#e0edfc','#d7e7f9'][i],10,'#c2d2ea',1),tx(250,o.y+10,87,74,o.label,21,'#2b59bc',600,{align:'center',valign:'center',lineHeight:1.3}),L(348,o.y+47,363,o.y+47,'#b7d1f3',1.5),R(361,o.y+45,5,5,'#d2e3fa'),tx(395,o.y+7,326,88,o.a,21,INK,400,{lineHeight:1.7}),tx(781,o.y+7,400,88,o.b,20,INK,400,{lineHeight:1.8}),C(729,o.y+36,30,WHITE,'#3969c1',1.2),svg(735,o.y+43,19,17,'<path d="M0 8h18m-8-8 8 8-8 8" stroke="#618bcd" stroke-width="1.2"/>'),i<2?[L(373,o.y+101,729,o.y+101,'#9eaec4',1,{dash:'1 2'}),L(755,o.y+101,1178,o.y+101,'#9eaec4',1,{dash:'1 2'})]:null])
]));
slides.push(slide('slide_16','차년도 핵심 전략',[
 shell(16,'차년도 핵심 전략','차년도는 콘텐츠 소비 중심 성장 구조 강화 및 커뮤니티 활성화 기반\n확대에 주력'),
 C(209,296,322,'transparent','#8bafe7',1,{style:{borderStyle:'dashed'}}),C(227,317,284,'#e5eefc'),C(245,334,248,'#c2d6f7'),C(255,345,229,'#1d46bd','none',1,{shadow:'0px 6px 9px #9fb8de'}),tx(277,422,188,81,'콘텐츠 소비 중심\n성장 구조 강화',25,WHITE,600,{align:'center',lineHeight:1.45}),
 [{y:266,c:'#366bd7',icon:'search-check',title:'콘텐츠 노출 고도화',txt:'카테고리별 초입 노출 정교화\n신규 사용자 탐색 동선 최적화',point:[472,332]},{y:369,c:'#6899e9',icon:'messages-square',title:'커뮤니티 활성화 강화',txt:'고품질 게시물 추천 정책 개선\n상호작용 증가를 위한 UI 개편',point:[523,412]},{y:461,c:'#366bd7',icon:'chart-no-axes-combined',title:'생태계 성장 인프라 확장',txt:'이곳에 해당 전략에 관한 설명을 입력해 보세요.\n전략의 세부 추진방안을 넣어보세요.',point:[523,509]},{y:553,c:'#6899e9',icon:'settings',title:'프로세스 효율화',txt:'이곳에 해당 전략에 관한 설명을 입력해 보세요.\n전략의 세부 추진방안을 넣어보세요.',point:[472,585]}].map(o=>[R(551,o.y,631,o.y===266||o.y===553?100:89,GRAY,5),L(o.point[0],o.point[1],579,o.point[1],'#75a3e6',1.4),C(o.point[0]-13,o.point[1]-13,26,'#719de5','none',1,{opacity:.45}),C(o.point[0]-4,o.point[1]-4,8,'#2454c9'),C(568,o.y+16,68,WHITE,'#81a6e6',1),ic(583,o.y+31,38,o.icon,'#6999dc'),P(640,o.y+30,195,41,o.title,o.c,WHITE,18,{weight:500}),tx(844,o.y+23,334,63,o.txt.split('\n').map(t=>'•  '+t).join('\n'),16,INK,400,{lineHeight:1.75})])
]));
slides.push(slide('slide_17','차년도 추진 계획',[
 shell(17,'차년도 추진 계획','준비·개선·고도화·확산의 단계별 추진을 통해 전략 실행력 강화 예정'),
 L(243,263,243,321,'#848c99',1,{dash:'1 2'}),L(733,238,733,310,'#848c99',1,{dash:'1 2'}),L(1191,239,1191,297,'#848c99',1,{dash:'1 2'}),L(248,285,730,285,'#9fa6af',1),L(737,261,1185,261,'#9fa6af',1),svg(246,279,486,13,'<path d="m6 0-6 6 6 6m473-12 7 6-7 6" stroke="#9fa6af" stroke-width="1"/>'),svg(734,255,455,13,'<path d="m6 0-6 6 6 6m442-12 7 6-7 6" stroke="#9fa6af" stroke-width="1"/>'),P(393,267,180,38,'상반기','#3e75d9',WHITE,24,{weight:500}),P(864,240,179,37,'하반기','#214cc1',WHITE,24,{weight:500}),
 R(240,380,479,286,'#ebeff7'),R(734,349,458,317,'#f0f0f3',4),R(719,348,15,318,'#c5cad4'),R(240,339,479,42,'#3168d5'),svg(719,308,488,73,'<path d="M0 31 15 0H472l16 21-16 22H15L0 73z" fill="#2445ab"/>'),
 [{x:269,y:356,t:'2099. 1~3',h:'환경 정비',lines:['핵심 지표 구조 재정의','노출·추천 기준표 재정비','운영 프로세스 점검'],headY:418},{x:494,y:356,t:'2099. 4~6',h:'UX 개선',lines:['초기 진입 동선 개편','주요 화면 UI 조정','실험 기반 UX 개선 적용'],headY:418},{x:759,y:324,t:'2099. 7~9',h:'기능 고도화',lines:['추천 알고리즘 반영 강화','콘텐츠 큐레이션 고도화','실험·검증 루프 정착'],headY:389},{x:981,y:324,t:'2099. 10~12',h:'성과 관리',lines:['지표 모니터링 체계 운영','성과 기반 반복 개선','개선 요소의\n서비스 전면 확산'],headY:389}].map(o=>[C(o.x-5,o.y+1,10,WHITE),C(o.x-2,o.y+4,4,'#3465c9'),tx(o.x+12,o.y-5,200,30,o.t,16,WHITE,500),L(o.x,o.y+11,o.x,o.x<700?631:605,'#9ab9ed',1,{dash:'1 2'}),tx(o.x+13,o.headY,208,36,o.h,23,o.x<700?'#2d5ab9':'#17439e',600),o.lines.map((t,i)=>tx(o.x-8,o.headY+57+i*40,218,62,'•  '+t,18,INK,400,{lineHeight:1.5}))])
]));
slides.push(slide('slide_18','요약 및 추후 방향',[
 shell(18,'요약 및 추후 방향'),R(239,124,950,257,'#eef7fd'),R(239,403,950,257,'#eef7fd'),R(266,125,153,8,'#2c56c2'),R(269,403,153,8,'#2c56c2'),tx(275,162,166,38,'사업 핵심 지표',23,'#2d58bc',600),tx(275,193,166,53,'요약',40,'#2d58bc',700),ic(280,270,61,'presentation','#80a2d6'),tx(278,437,165,38,'사업 성장 전략',23,'#2d58bc',600),tx(278,469,166,53,'향후 방향',40,'#2d58bc',700),ic(281,546,64,'scroll-text','#8aadde'),
 [[464,164],[464,223],[464,283],[464,435],[464,532],[464,592]].map(([x,y])=>outlineCheck(x,y)),
 // Emphasis is separate editable text runs, with measured Pretendard advances.
 rich(491,164,[['핵심 지표 전반에서 ',153.34],['긍정적인 개선 흐름과 가시적인 성과',278.26,true],['를 확인했습니다.',131.09]]),
 rich(491,223,[['콘텐츠 노출 및 유입 구조 개편 후 ',259.84],['신규 고객 콘텐츠 소비량과 유입 지표',283.01,true],['가 상승했습니다.',131.09]]),
 rich(491,283,[['주요 성과는 ',96.46],['MAU 85만 명 및 참여율 34% 증가',281.23,true],['이며, ',44.75],['광고 매출 30억 원과 커뮤니티',234.53,true]]),
 rich(491,314,[['만족도 4.5점',104.01,true],['으로 재무 건전성과 고객 만족도를 확보했습니다.',375.88]]),
 L(463,206,1162,206,'#929eac',1,{dash:'1 2'}),L(463,269,1162,269,'#929eac',1,{dash:'1 2'}),
 rich(491,435,[['안정적인 ',74.16],['콘텐츠 소비를 중심',147.77,true],['으로',34.57]]),
 rich(491,466,[['사용자 리텐션을 확보하고, 플랫폼의 ',284.51],['지속적인 성장 모멘텀을 고도화',238.95,true],['할 계획입니다.',113.81]]),
 L(463,514,1162,514,'#929eac',1,{dash:'1 2'}),
 rich(491,532,[['플랫폼 활성화를 위해 ',170.63],['커뮤니티 참여 구조를 대폭 강화',243.69,true],['할 예정입니다.',113.81]]),
 L(463,575,1162,575,'#929eac',1,{dash:'1 2'}),
 rich(491,592,[['커뮤니티 내 ',96.46],['신규 기능 도입과 UI/UX 보완에 대한 구체적인 검토',398.13,true],['를 진행할 것입니다.',153.4]])
]));
export default {id:'042',title:'MIRI COMPANY — 2099 사업 성과 보고서',slides};
