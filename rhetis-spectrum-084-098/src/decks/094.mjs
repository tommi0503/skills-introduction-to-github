import {T,R,C,L,PH,S,I,P,slide} from '../primitives.mjs';
const green='#73df61',mint='#40cbb3',blue='#46a7e4',cyan='#95e4f6',bg='#f7f7f7',grey='#bcbebe',black='#000000';
const txt=(x,y,w,h,s,size=18,col=black,weight=400,opts={})=>T(x,y,w,h,s,size,col,weight,{font:'Pretendard',lineHeight:1.45,...opts});
const en=(x,y,w,h,s,size=46,col=black,weight=650,opts={})=>T(x,y,w,h,s,size,col,weight,{font:'Montserrat',tracking:-1,lineHeight:1.35,...opts});
const pill=(x,y,w,h,s,col=mint,size=20)=>P(x,y,w,h,s,col,'#fff',size,{weight:700});
const box=(x,y,w,h,fill='#fff',radius=7)=>R(x,y,w,h,fill,radius,'none',1,{shadow:'0 2px 16px rgba(0,0,0,.025)'});
const list=(x,y,w,ss,size=18,gap=30,col=black)=>ss.map((t,i)=>[C(x,y+i*gap+size*.6,Math.max(5,size*.3),col),txt(x+20,y+i*gap,w-20,gap,t,size,col)]);
const logo=()=>[S(1070,40,22,17,`<svg viewBox="0 0 22 17" xmlns="http://www.w3.org/2000/svg"><path d="M3 13L8 3M10 13L15 3M17 13L19 9" stroke="${green}" stroke-width="5" stroke-linecap="round"/></svg>`),en(1102,35,160,28,'Miri Company',19,black,650,{tracking:0,lineHeight:1.3})];
const header=(title,sub='',sx=0)=>[...logo(),C(79,76,16,green),en(107,74,1090,70,title),sub&&txt(sx||107+title.length*27,103,440,28,'|  '+sub,16,'#858585')];
let uid=0;
function glow(x,y,w,h,variant=0){const id='halo'+(++uid);return S(x,y,w,h,`<svg xmlns="http://www.w3.org/2000/svg" overflow="visible" viewBox="0 0 800 500"><defs><radialGradient id="${id}g"><stop stop-color="${green}" stop-opacity=".85"/><stop offset=".45" stop-color="${green}" stop-opacity=".5"/><stop offset="1" stop-color="${green}" stop-opacity="0"/></radialGradient><radialGradient id="${id}m"><stop stop-color="${mint}" stop-opacity=".75"/><stop offset="1" stop-color="${mint}" stop-opacity="0"/></radialGradient><radialGradient id="${id}b"><stop stop-color="${blue}" stop-opacity=".75"/><stop offset=".4" stop-color="${blue}" stop-opacity=".5"/><stop offset="1" stop-color="${blue}" stop-opacity="0"/></radialGradient></defs><ellipse cx="${variant?520:260}" cy="290" rx="315" ry="280" fill="url(#${id}g)"/><ellipse cx="410" cy="360" rx="310" ry="280" fill="url(#${id}m)"/><ellipse cx="${variant?200:610}" cy="330" rx="310" ry="280" fill="url(#${id}b)"/></svg>`);}
const advances={'0':.66015625,'1':.46875,'2':.61035156,'3':.63867188,'4':.65722656,'5':.62695313,'6':.64257813,'7':.57519531,'8':.64355469,'9':.64257813,'.':.28222656,',':.28710938,'%':.95996094,'억':.86425781,'명':.86425781,'매':.86425781,'출':.86425781,'+':.65332031,' ':.23046875};
const measure=(v,size)=>[...v].reduce((a,c)=>a+size*(advances[c]||.8643),0);
function number(x,y,w,value,size=42,col=black){const m=value.match(/^(매출\s*|\+\s*)?([\d,.]+)(.*)$/);if(!m)return [txt(x,y,w,60,value,size,col,700,{align:'center'})];const pre=m[1]||'',num=m[2],unit=m[3]||'',us=Math.round(size*.5);const nw=measure(num,size),pw=pre?measure(pre,us)+3:0,uw=unit?measure(unit,us):0;const left=x+(w-nw-pw-uw)/2;return[pre&&txt(left,y+size*.47,pw+3,36,pre,us,col,400,{lineHeight:1.2}),txt(left+pw,y,nw+3,60,num,size,col,700,{lineHeight:1.2}),unit&&txt(left+pw+nw+1,y+size*.47,uw+5,36,unit,us,col,400,{lineHeight:1.2})];}
function artIcon(x,y,size,name,col){const paths={
Target:'<circle cx="21" cy="24" r="18"/><circle cx="21" cy="24" r="12"/><circle cx="21" cy="24" r="6"/><path d="M21 24H43M37 20H44L41 24L44 28H37"/>',
ChartColumn:'<path d="M5 44H43"/><rect x="9" y="25" width="10" height="19"/><rect x="19" y="8" width="10" height="36"/><rect x="29" y="20" width="10" height="24"/>',
Presentation:'<path d="M5 5H38V29H5Z M9 23L18 15L23 19L33 10"/><circle cx="35" cy="29" r="6"/><path d="M24 45V39Q24 34 35 34Q46 34 46 39V45Z M35 35V45"/>',
Puzzle:'<rect x="5" y="5" width="38" height="38" rx="2"/><path d="M24 5V14C33 9 33 25 24 20V29C15 24 15 40 24 35V43M5 24H14C9 15 25 15 20 24H29C24 33 40 33 35 24H43"/>',
CalendarCheck:'<rect x="4" y="7" width="33" height="34" rx="3"/><path d="M4 16H37M12 3V11M29 3V11M10 23H15M22 23H28M10 29H15M10 35H15"/><circle cx="36" cy="36" r="10"/><circle cx="36" cy="33" r="3"/><path d="M29 43Q29 36 36 36Q43 36 43 43"/>',
Laptop:'<rect x="5" y="6" width="38" height="31" rx="1"/><path d="M2 37H46V41H2Z"/><circle cx="24" cy="19" r="6"/><path d="M13 35Q13 25 24 25Q35 25 35 35"/>',
TrendingUp:'<path d="M5 40H15V33H24V26H33V19H43V25L48 17H36V21H29V28H20V35H5Z M5 24L26 10H23V5H35L31 16L29 12L7 28Z"/>'
};return paths[name]?S(x,y,size,size,`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50" fill="none" stroke="${col}" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round">${paths[name]}</svg>`):I(x,y,size,name,col,{sw:1.25});}
function edgeGlow(y){const id='edge'+(++uid);return S(0,0,1280,720,`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720"><defs><radialGradient id="${id}g"><stop stop-color="#77f675" stop-opacity=".8"/><stop offset="1" stop-color="#77f675" stop-opacity="0"/></radialGradient><radialGradient id="${id}b"><stop stop-color="#43b8ed" stop-opacity=".85"/><stop offset="1" stop-color="#43b8ed" stop-opacity="0"/></radialGradient></defs><ellipse cx="70" cy="${y-10}" rx="165" ry="265" fill="url(#${id}g)"/><ellipse cx="-18" cy="${y+10}" rx="150" ry="185" fill="url(#${id}b)"/></svg>`);}
const iconCircle=(x,y,d,col,name)=>[C(x,y,d,col),artIcon(x+d*.25,y+d*.25,d*.50,name,'#fff')];
const grad='linear-gradient(100deg,#73df61,#40cbb3)';
const metric=(x,y,w,num,unit='',size=42,col=black)=>number(x,y,w,num+unit,size,col);
const s=[];
// 01 — vector halo and inset cover typography.
s.push(slide('slide_01','2080 H2 Operational Plan',[
S(0,0,1280,720,`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720"><defs><filter id="blur"><feGaussianBlur stdDeviation="25"/></filter><linearGradient id="halo"><stop stop-color="#a9fc7f"/><stop offset=".46" stop-color="#84fac0"/><stop offset="1" stop-color="#8bd6ff"/></linearGradient></defs><circle cx="640" cy="675" r="605" fill="none" stroke="url(#halo)" stroke-width="75" filter="url(#blur)"/><circle cx="640" cy="675" r="600" fill="white"/><circle cx="-106" cy="953" r="529" fill="none" stroke="#8dd47d" stroke-width=".8"/><circle cx="1294" cy="-160" r="380" fill="none" stroke="#66bad9" stroke-width=".6"/></svg>`),...logo().map(n=>({...n,y:n.y+16})),en(260,231,760,110,'2080 H2',88,mint,700,{align:'center',tracking:0,style:{background:grad,backgroundClip:'text',color:'transparent'}}),en(170,338,940,120,'Operational Plan',88,black,700,{align:'center',tracking:-2.2}),R(349,534,582,72,'#fff',8,'none',1,{shadow:'0 0 10px rgba(64,203,179,.35)'}),R(372,552,5,36,mint,3),txt(394,552,460,40,'미리컴퍼니 하반기 운영 계획 보고서',26,black,650),L(883,565,895,577,black,2),L(895,577,907,565,black,2)
],'#fff'));
// 02
s.push(slide('slide_02','Contents',[
R(0,0,1280,310,bg),glow(900,130,550,400),R(0,310,1280,410,'#fff'),...logo(),C(79,109,16,green),en(105,106,500,64,'Contents',34,black,700,{tracking:-.5}),txt(79,172,740,115,'성과를 점검하고 전략을 세우고,\n실행으로 연결합니다.',38,black,400,{lineHeight:1.48}),
...[['상반기 운영 점검','핵심 성과 분석','이슈 및 개선 과제'],['하반기 목표 및 전략','운영 목표 재정의','성장 전략','중점 과제'],['실행 계획 및 관리 체계','실행 로드맵','예산 및 리스크 관리','Contact Us']].map((a,j)=>{let x=74+j*390;return[box(x,362,352,308),R(x,362,352,308,'transparent',0,'#e7faf3',1),pill(x+118,390,116,36,'Part '+(j+1),grad,18),R(x+14,452,324,203,bg,7),...a.map((v,i)=>[txt(x+35,480+i*40,275,32,v,18,black,500),txt(x+303,480+i*40,18,30,String(j===0?i+1:j===1?i+4:i+8),17,black,300,{align:'right'})])]})
],bg));
// 03
s.push(slide('slide_03','Executive Summary',[
glow(660,350,820,530),...header('Executive Summary'),
...[[75,206,'상반기 매출','목표 대비 108% 달성','64.8억',mint],[457,206,'영업이익률','전년 동기 대비 +2.1%p','18.4%',blue],[75,435,'신규 고객 수','목표 대비 96% 달성','18,420명',mint],[457,435,'하반기 목표','영업이익률 20% 달성','매출 78억',blue]].map(([x,y,k,n,v,c])=>[box(x,y,367,214),pill(x+115,y+25,139,39,k,c),txt(x+20,y+79,327,38,n,21,'#5f5f5f',400,{align:'center'}),R(x+22,y+120,324,81,bg,6),...metric(x+25,y+134,318,v,'',40)]),
...['성장 채널 집중','비용 효율화','실행 관리 강화'].map((v,i)=>[box(838,206+i*153,367,135),pill(866,254+i*153,90,39,'전략 '+(i+1),black),R(985,233+i*153,198,82,bg,7),txt(993,254+i*153,182,50,v,23,black,400,{align:'center',valign:'center'})])
],bg));
// 04
s.push(slide('slide_04','Operating Results',[
edgeGlow(405),...header('Operating Results','상반기 주요 운영 실적',550),...Array.from({length:4},(_,i)=>[L(294,445-i*77,1017,445-i*77,i===0?'#777':'#c5c5c5',i===0?1.2:1,{dash:i===0?'':'2 2'}),txt(247,432-i*77,41,25,(i*5)+'억',15,'#444',400,{align:'right'})]),
R(862,190,8,8,'#818181'),txt(875,184,68,24,'매출목표',13,'#888'),R(940,190,8,8,mint),txt(953,184,68,24,'매출실적',13,mint),
...[8.6,9.5,10.2,11,12.1,13.4].map((v,i)=>{let x=312+i*120.3,h=v/15*232;let t=[8,8.8,9.4,10.3,11.2,12.3][i],py=445-t/15*232;return[R(x,445-h,84,h,mint,4),txt(x-10,419-h,104,24,v+'억',16,mint,400,{align:'center'}),i<5&&L(x+42,py,x+162.3,445-[8.8,9.4,10.3,11.2,12.3][i]/15*232,'#dcfffa',.7),C(x+38.5,py-3.5,7,'#fff'),txt(x,py+5,84,24,t+'억',15,'#fff',400,{align:'center'}),txt(x,449,84,28,(i+1)+'월',15,'#444',400,{align:'center'})]}),
box(74,495,1132,174),pill(142,530,217,38,'상반기 누적 매출 추이',grad,20),txt(93,581,315,65,'상반기 전 기간 목표를 상회하며,\n6월 최고 매출을 달성했습니다.',21,black,400,{align:'center',lineHeight:1.4}),...[[432,'누적 매출','64.8억'],[687,'목표 달성률','108%'],[942,'목표 초과','+ 4.8억']].map(([x,k,v])=>[R(x,516,236,134,bg,6),txt(x,536,236,34,k,21,black,700,{align:'center'}),...number(x,580,236,v,40,blue)])
],bg));
// 05
s.push(slide('slide_05','Key Issues',[
...header('Key Issues','상반기 이슈 및 개선 과제',376),...[[65,mint,'성과영역',['핵심 상품 매출','재구매율','운영 처리 시간'],['42.5억 달성','34% → 39% 상승','평균 2.8 → 2.1일 단축'],green,['Calculator','CreditCard','Clock']],[652,blue,'보완과제',['신규 고객 확보','마케팅 비용 관리','실행 일정 관리'],['목표 대비 4% 미달','예산 대비 12% 초과 집행','일부 부서 일정 지연 발생'],cyan,['Users','ChartNoAxesCombined','CalendarCheck']]].map(([x,c,k,n,v,ic,icons])=>[R(x+35,200,490,5,mint,5,'none',1,{style:{filter:'blur(8px)'}}),box(x,203,563,445),pill(x+201,233,161,43,k,c,23),...n.map((name,i)=>[R(x+33,299+i*111,496,98,bg,7),...iconCircle(x+49,312+i*111,73,ic,icons[i]),txt(x+137,334+i*111,190,43,name,20),txt(x+275,332+i*111,228,46,v[i],22,c,700,{align:'right',style:{whiteSpace:'nowrap'}})])])
],bg));
// 06
s.push(slide('slide_06','S.W.O.T',[
...header('S.W.O.T','하반기 운영 SWOT 분석',303),
...[[74,191,mint,'내부 성과를 뒷받침하는 핵심 경쟁력',['핵심 상품 매출 42.5억 달성','재구매율 34% → 39% 상승','운영 처리 시간 2.8일 → 2.1일 단축'],false],[740,191,blue,'하반기 보완이 필요한 운영 과제',['마케팅 비용 12% 초과 집행','신규 고객 목표 대비 4% 미달','일부 부서 실행 일정 지연'],true],[74,437,green,'성장 확대를 위한 외부 기회 요인',['신규 제휴 채널 발굴 여지','고효율 성장 채널 확대 가능성','재구매 고객 기반 확장 가능'],false],[740,437,'#888','성과에 영향을 줄 수 있는 위험 요인',['경쟁사 프로모션 강화 가능성','광고 단가 및 고객 획득 비용 상승','시장 수요 변동성 확대'],true]].map(([x,y,c,k,a,right])=>[box(x,y,466,229),R(x+22,y+81,422,122,bg,8),R(right?x+158:x+33,y+35,4,23,c,2),txt(right?x+174:x+49,y+31,right?280:390,35,k,20,black,650,{align:right?'right':'left'}),...a.map((v,i)=>txt(x+49,y+99+i*29,363,30,'•  '+v,18,black,400,{align:right?'right':'left'}))]),
...[[447,212,mint,'S'],[646,212,blue,'W'],[447,459,green,'O'],[646,459,black,'T']].map(([x,y,c,t])=>[C(x,y,186,c),en(x,y+53,186,85,t,62,'#fff',700,{align:'center',tracking:0})])
],bg));
// 07
s.push(slide('slide_07','H2 Goals & Strategic Direction',[
S(0,0,750,720,`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 750 720"><defs><filter id="part2blur"><feGaussianBlur stdDeviation="23"/></filter><linearGradient id="part2gradient" x2=".3" y2="1"><stop stop-color="#78ddc5"/><stop offset=".45" stop-color="#81ec83"/><stop offset="1" stop-color="#7ce0f3"/></linearGradient></defs><path d="M454 -25L625 114Q720 207 617 311L193 744" fill="none" stroke="url(#part2gradient)" stroke-width="55" filter="url(#part2blur)"/><path d="M0 0H455L612 121Q695 204 610 291L199 720H0Z" fill="${bg}"/></svg>`),
...['Goal','Strategy','Priority'].map((v,i)=>[pill(88,104+i*53,123,35,v,black,18),txt(228,106+i*53,220,34,['운영 목표 재정의','성장 전략 수립','중점 과제 선정'][i],22,black,700),L(379,121+i*53,445,121+i*53,'#aaa',1,{dash:'2 2'}),txt(464,108+i*53,18,30,String(i+8),17,black,300,{align:'center'})]),pill(1054,372,144,45,'Part 2',grad,26),en(552,433,646,160,'H2 Goals &\nStrategic Direction',60,black,700,{align:'right',lineHeight:1.35,tracking:-1.6}),txt(938,615,260,40,'|  하반기 목표 및 전략 방향',21,'#7d7d7d',500,{align:'right'})
],bg));
// 08
s.push(slide('slide_08','Objectives',[
glow(50,124,1230,800),...header('Objectives','하반기 운영 목표',377),
...[[69,285,green,'ChartColumn','매출목표','상반기 대비 +20.4%','핵심 사업 성장 및 신규 채널 확대','78억'],[457,167,mint,'Target','영업이익률 목표','상반기 대비 +1.6%p','비용 효율화 및 수익 구조 개선','20.0%'],[845,285,blue,'Presentation','신규 고객 목표','상반기 대비 +30.3%','전환 캠페인 및 유입 채널 강화','24,000명']].map(([x,y,c,ic,k,up,body,value])=>[C(x,y,389,'#fff'),artIcon(x+172,y+63,48,ic,c),pill(x+Math.round((389-(k.length>5?175:135))/2),y+138,k.length>5?175:135,43,k,c,23),txt(x+17,y+206,355,33,up,23,'#555',700,{align:'center'}),txt(x+15,y+238,359,36,body,22,'#666',400,{align:'center'}),...number(x+20,y+283,349,value,46,black)])
],bg));
// 09
s.push(slide('slide_09','Key Strategies',[
...header('Key Strategies','하반기 3대 핵심 전략',466),
...[[green,'TrendingUp','성장 채널 집중','핵심 채널 중심으로 매출 성장 확대','목표 매출','46억'],[mint,'Puzzle','비용 효율화','저효율 비용을 줄이고 수익성 개선','비용 절감 목표','3.2억'],[blue,'CalendarCheck','실행 관리 강화','KPI 기반으로 실행 속도와 품질 관리','과제 완료율 목표','92%']].map(([c,ic,k,n,label,v],i)=>{let y=192+i*160;return[box(112,y,1056,145),...iconCircle(153,y+24,96,c,ic),txt(290,y+55,245,48,k,26,black,700),txt(460,y+59,345,35,n,19),L(744,y+72,809,y+72,'#bbb',1,{dash:'2 2'}),R(841,y+19,299,107,c,7),txt(883,y+59,150,35,label,18,'#fff',500),...number(1005,y+48,115,v,42,'#fff')]})
],bg));
// 10
s.push(slide('slide_10','Execution Framework',[
...header('Execution Framework','전략별 실행 과제 및 관리 지표',645),box(81,185,1118,482),R(114,219,4,55,green,2),txt(142,219,980,60,'각 과제의 추진 현황과 성과를 체계적으로 관리하고,\n목표 달성 여부를 지속적으로 점검할 수 있도록 구성했습니다.',19,black,400,{lineHeight:1.48}),
...(()=>{let xs=[110,358,643,799,1049],ws=[248,285,156,250,121];let rows=[['전략','실행 과제','담당 부서','관리 지표','점검 주기'],['성장 채널 집중','핵심 채널 4개 집중 운영','마케팅운영팀','채널별 매출전환율','주간'],['비용 효율화','저효율 캠페인 20% 축소','사업기획팀','CAC비용 집행률','월간'],['실행 관리 강화','월간 성과 리뷰 체계화','데이터분석팀','과제 완료율지연 건수','월간']];return rows.map((row,r)=>row.map((v,c)=>[R(xs[c],304+r*83,ws[c],83,r===0?(c===0?green:mint):c===0?blue:c===4?bg:'#fff',0,r===0?'#ffffff66':'#ededed',.5),txt(xs[c]+8,329+r*83,ws[c]-16,45,v,r===0||c===0?22:19,r===0||c===0?'#fff':black,r===0||c===0?650:400,{align:'center',valign:'center'})]))})()
],bg));
// 11
s.push(slide('slide_11','Portfolio Strategy',[
glow(580,-380,680,500,1),...header('Portfolio Strategy','사업 포트폴리오 운영 방향',539),
...[[green,'핵심 사업','집중 확대','42.5억','67%','52억',67],[mint,'성장 사업','테스트 강화','14.8억','26%','20억',26],[blue,'관리 사업','비용절감','7.5억','7%','6억',7]].map(([c,k,n,a,p,target,v],i)=>{let x=74+i*384;return[box(x,213,363,433),pill(x+101,250,161,43,k,c,23),R(x+19,316,325,247,bg,7),...list(x+76,333,260,['운영 방향 : '+n,'상반기 매출 : '+a,'매출 비중 : '+p],21,33),S(x+146,461,72,26,`<svg viewBox="0 0 72 26" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="triangle${i}" x2="0" y2="1"><stop stop-color="${c}" stop-opacity="0"/><stop offset="1" stop-color="${c}" stop-opacity=".8"/></linearGradient></defs><path d="M0 0H72L42 23Q36 28 30 23Z" fill="url(#triangle${i})"/></svg>`),txt(x+15,510,333,44,'하반기 목표 '+target,23,black,700,{align:'center'}),txt(x+20,581,58,35,p,25,c,700),R(x+74,584,269,28,bg,14),R(x+74,584,Math.max(28,269*v/100),28,c,14)]})
],bg));
// 12
s.push(slide('slide_12','Organization',[
...header('Organization','하반기 운영 조직 체계',441),S(69,221,416,386,`<svg viewBox="0 0 416 386" xmlns="http://www.w3.org/2000/svg"><defs><filter id="orb"><feGaussianBlur stdDeviation="15"/></filter></defs><g filter="url(#orb)"><ellipse cx="201" cy="190" rx="168" ry="160" fill="#72ff29"/><ellipse cx="233" cy="178" rx="137" ry="140" fill="#1daffb"/><ellipse cx="134" cy="153" rx="95" ry="124" fill="#34f684"/></g></svg>`),C(113,270,325,'transparent'),artIcon(243,329,69,'Target','#fff'),txt(147,404,260,42,'전략운영본부',24,'#fff',700,{align:'center'}),txt(137,449,280,39,'전체 목표 관리 및 경영진 보고',19,'#fff',400,{align:'center'}),L(444,407,512,407,'#999',1,{dash:'2 2'}),L(512,215,512,615,'#999',1,{dash:'2 2'}),
...[[mint,'Presentation','사업기획팀','6명',['전체 목표 관리','경영진 보고']],[blue,'CalendarCheck','마케팅운영팀','8명',['채널 운영','고객 유입 관리']],[mint,'Settings','프로세스개선팀','5명',['운영 효율화','리스크 점검']],[blue,'Laptop','데이터분석팀','4명',['KPI 대시보드','월간 리포트']]].map(([c,ic,k,n,items],i)=>{let y=158+i*133.5;return[L(512,y+57,583,y+57,'#999',1,{dash:'2 2'}),box(628,y,254,114),...iconCircle(583,y+12,91,c,ic),txt(692,y+30,155,32,k,20,black,700,{align:'center'}),txt(692,y+60,155,34,'('+n+')',20,black,400,{align:'center'}),...items.map((a,j)=>[L(883,y+26+j*62,940,y+26+j*62,'#999',1,{dash:'2 2'}),R(941,y+j*62,195,52,'#fff',26),txt(964,y+13+j*62,170,32,'•  '+a,18)])]})
],bg));
// 13
const arc=(x,y,w,h,v,col,full=false)=>S(x,y,w,h,`<svg viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg"><path d="${full?'M '+w/2+' 14 A '+(w/2-14)+' '+(w/2-14)+' 0 1 1 '+(w/2-.01)+' 14':'M 14 '+(h-14)+' A '+(w/2-14)+' '+(w/2-14)+' 0 0 1 '+(w-14)+' '+(h-14)}" fill="none" stroke="${bg}" stroke-width="22" stroke-linecap="round"/><path d="${full?'M '+w/2+' 14 A '+(w/2-14)+' '+(w/2-14)+' 0 1 1 '+(w/2-.01)+' 14':'M 14 '+(h-14)+' A '+(w/2-14)+' '+(w/2-14)+' 0 0 1 '+(w-14)+' '+(h-14)}" fill="none" stroke="${col}" stroke-width="22" stroke-linecap="round" pathLength="100" stroke-dasharray="${v} 100"/></svg>`);
s.push(slide('slide_13','KPI Management',[
...header('KPI Management','핵심 KPI 관리 체계',534),box(79,210,397,446),pill(200,235,156,42,'매출 달성률',grad,22),arc(191,303,172,172,83,green,true),txt(200,362,154,55,'83%',36,black,700,{align:'center'}),txt(170,498,70,30,'기준',18,black,400,{align:'center'}),txt(314,498,70,30,'목표',18,black,400,{align:'center'}),txt(144,528,122,45,'64.8억',25,black,700,{align:'center'}),txt(288,528,122,45,'78억',25,black,700,{align:'center'}),L(277,501,277,552,'#aaa',1,{dash:'2 2'}),R(99,584,357,50,bg),txt(111,594,333,34,'매출 성장 관련 키워드를 입력해주세요.',20,black,400,{align:'center'}),
...[[mint,'영업이익률','20.0%','18.4%',92],[blue,'신규 고객 수','18,420','24,000',77],[grey,'과제 완료율','81%','92%',88]].map(([c,k,b,t,v],i)=>{let y=210+i*156;return[box(498,y,704,134),pill(522,y+46,156,41,k,i===2?black:c,22),txt(721,y+40,75,30,'기준',18,black,400,{align:'center'}),txt(865,y+40,75,30,'목표',18,black,400,{align:'center'}),txt(700,y+70,116,46,b,25,black,700,{align:'center'}),txt(845,y+70,116,46,t,25,black,700,{align:'center'}),L(830,y+43,830,y+94,'#aaa',1,{dash:'2 2'}),arc(992,y+18,176,103,v,c),txt(1016,y+68,130,47,v+'%',30,black,700,{align:'center'})]})
],bg));
// 14
s.push(slide('slide_14','Key Initiatives',[
glow(745,371,650,400),...header('Key Initiatives','중점 추진 과제 우선순위',462),R(90,201,31,425,black,16),R(143,627,1027,32,black,16),txt(86,168,60,30,'High',18,black,500),txt(90,632,60,28,'Low',18),txt(1183,630,55,30,'High',18),txt(96,354,21,110,'실\n행\n난\n이\n도',18,'#fff',500,{lineHeight:1.05}),txt(600,629,112,30,'기대효과',20,'#fff',600,{align:'center'}),
...[[158,201,'우선실행',grad,['핵심 채널 예산 확대','재구매 캠페인 강화','저효율 광고 캠페인 축소']],[668,201,'선별 투자',mint,['신규 제휴 채널 테스트','신규 상품군 파일럿','키워드를 입력해주세요.']],[158,418,'운영 개선',green,['월간 리포트 자동화','운영 프로세스 표준화','키워드를 입력해주세요.']],[668,418,'중장기 검토',blue,['운영 시스템 고도화','외부 협업 체계 구축','키워드를 입력해주세요.']]].map(([x,y,k,c,a])=>[box(x,y,487,193),pill(x+35,y+75,143,43,k,c,23),R(x+205,y+23,254,147,bg,6),...list(x+228,y+45,240,a,20,35)])
],bg));
// 15
s.push(slide('slide_15','Execution & Governance',[
S(500,0,780,720,`<svg viewBox="0 0 780 720" xmlns="http://www.w3.org/2000/svg"><defs><filter id="part3blur"><feGaussianBlur stdDeviation="22"/></filter><linearGradient id="part3gradient" x2="0" y2="1"><stop stop-color="#b3fc74"/><stop offset=".5" stop-color="#83f58d"/><stop offset="1" stop-color="#83def9"/></linearGradient></defs><ellipse cx="640" cy="370" rx="520" ry="458" fill="url(#part3gradient)" filter="url(#part3blur)"/><ellipse cx="650" cy="370" rx="522" ry="461" fill="${bg}"/></svg>`),pill(83,218,145,45,'Part 3',grad,26),en(83,279,550,168,'Execution &\nGovernance',60,black,700,{tracking:-1.5,lineHeight:1.35}),txt(88,451,450,38,'|  실행 계획 및 관리 체계',23,'#7d7d7d'),...['Roadmap','Milestone','Budget','Risk'].map((v,i)=>[pill(750,403+i*53,123,35,v,black,18),txt(889,405+i*53,240,34,['일정별 실행 흐름 관리','핵심 점검 시점 관리','예산 및 리소스 운영','주요 리스크 대응 관리'][i],22,black,700),L(1109,420+i*53,1174,420+i*53,'#aaa',1,{dash:'2 2'}),txt(1191,407+i*53,22,30,String(i+16),17,black,300,{align:'center'})])
],bg));
// 16
s.push(slide('slide_16','Roadmap',[
...header('Roadmap','하반기 실행 로드맵',371),L(59,425,1221,425,'#dedede',6),...['July','August','September','October','November','December'].map((v,i)=>pill(104+i*180.5,403,171,44,v,[grey,cyan,blue,green,grad,mint][i],18)),
...[[59,191,grey,'부서별 KPI 확정',['목표 확정 및 과제배포','예산 재배분'],192],[239,471,cyan,'신규 고객 3,800명',['핵심 채널 캠페인 시작','신규 고객 확보','내용을 입력해 주세요'],219],[420,191,blue,'누적 매출 25억',['1차 성과 리뷰','저효율 항목 조정'],192],[600,471,green,'제휴 후보 3건 검토',['성장 사업 테스트 확대'],192],[780,104,mint,'예산 집행률 85% 이내',['비용 효율 점검','예산 운영 조정','내용을 입력해 주세요','내용을 입력해 주세요','내용을 입력해 주세요'],279],[960,471,mint,'차년도 실행 과제 도출',['최종 성과 리뷰','차년도 계획 수립'],192]].map(([x,y,c,k,a,h])=>[box(x,y,261,h),R(x+32,y+30,4,24,c,2),txt(x+49,y+29,205,37,k,20,black,650),R(x+19,y+82,223,h-107,bg,6),...list(x+43,y+96,207,a,18,29),S(x+121,y<400?y+h-1:y-7,18,9,`<svg viewBox="0 0 18 9" xmlns="http://www.w3.org/2000/svg"><path d="${y<400?'M0 0H18L9 9Z':'M0 9H18L9 0Z'}" fill="white"/></svg>`)])
],bg));
// 17
s.push(slide('slide_17','Milestones',[
{...glow(-240,-290,700,600,1),opacity:.65},{...glow(810,541,600,350,1),opacity:.65},...header('Milestones','주요 마일스톤',385),
...[[60,349,green,'목표 확정','7월 1주',3,['KPI 및 부서별 역할 확정','내용을 입력해 주세요','내용을 입력해 주세요']],[360,279,grad,'실행 착수','7월 3주',4,['핵심 과제별 운영 시작','내용을 입력해 주세요','내용을 입력해 주세요','내용을 입력해 주세요']],[655,207,mint,'중간 점검','9월 4주',6,['매출 25억','과제 완료율 45% 점검','내용을 입력해 주세요','내용을 입력해 주세요','내용을 입력해 주세요','내용을 입력해 주세요']],[951,136,blue,'최종 보고','12월 3주',8,['하반기 성과 및','차년도 제안 정리','내용을 입력해 주세요','내용을 입력해 주세요','내용을 입력해 주세요','내용을 입력해 주세요','내용을 입력해 주세요','내용을 입력해 주세요']]].map(([x,y,c,k,date,n,a],i)=>[box(x,y,269,665-y),R(x+32,y+37,4,25,i===1?mint:c,2),txt(x+48,y+36,201,38,k,22,black,650),txt(x+46,y+78,199,35,'( '+date+' )',17,'#858585'),S(x-6,y+131,299,53,`<svg viewBox="0 0 299 53" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="step-gradient"><stop stop-color="${green}"/><stop offset="1" stop-color="${mint}"/></linearGradient></defs><path d="M0 0H279L299 26.5L279 53H0Z" fill="${i===1?'url(#step-gradient)':c}"/></svg>`),txt(x+32,y+144,220,35,'Step '+(i+1),21,'#fff',600),...list(x+32,y+204,231,a,19,30)])
],bg));
// 18
function donut(x,y,d,vals,colors,width=114){let total=0;let r=d/2,ri=r-width;const pt=(r,a)=>[r*Math.sin(a)+d/2,-r*Math.cos(a)+d/2].join(' ');return S(x,y,d,d,`<svg viewBox="0 0 ${d} ${d}" xmlns="http://www.w3.org/2000/svg">${vals.map((v,i)=>{let a=total*Math.PI/50,b=(total+v)*Math.PI/50;total+=v;return `<path d="M${pt(r,a)} A${r} ${r} 0 ${v>50?1:0} 1 ${pt(r,b)} L${pt(ri,b)} A${ri} ${ri} 0 ${v>50?1:0} 0 ${pt(ri,a)} Z" fill="${colors[i]}"/>`}).join('')}</svg>`)}
s.push(slide('slide_18','Budget & Operations',[
...header('Budget & Operations','하반기 예산 배분 계획',624),donut(95,182,392,[40,20,17,13,10],[green,mint,blue,cyan,'#fff']),txt(215,339,152,34,'하반기 예산',18,black,400,{align:'center'}),txt(215,367,152,60,'18억',44,black,700,{align:'center'}),...number(386,342,87,'40%',40,'#fff'),txt(255,496,72,35,'20%',25,'#fff',650,{align:'center'}),txt(128,413,70,35,'17%',25,'#fff',650,{align:'center'}),txt(136,294,65,35,'13%',25,'#fff',650,{align:'center'}),txt(210,224,65,35,'10%',25,'#888',650,{align:'center'}),R(86,597,4,26,green,2),txt(99,596,140,35,'예산 운영 원칙',18,black,700),txt(225,594,315,66,'핵심 매출 기여 과제 우선 배정\n월별 집행률 점검 · 저효율 항목 수시 조정',18,black,400,{lineHeight:1.5}),
...[[green,'마케팅 운영  |  7.2억','핵심 채널 캠페인 및 고객 유입 확대'],[mint,'신규 사업 테스트  |  3.6억','신규 상품·제휴 채널 검증'],[blue,'인력·외주 리소스  |  3.1억','핵심 과제 운영 인력 및 전문 역량 확보'],[cyan,'시스템·툴 고도화  |  2.3억','데이터 관리 및 운영 자동화'],[bg,'예비비  |  1.8억','시장 변화 및 긴급 과제 대응']].map(([c,k,n],i)=>[box(546,190+i*93,653,79),pill(562,202+i*93,275,55,k,c,22),txt(850,216+i*93,340,43,n,20,black,400),i===4&&txt(562,588,275,45,k,23,black,700,{align:'center'})])
],bg));
// 19
s.push(slide('slide_19','Expected Outcomes',[
edgeGlow(710),...header('Expected Outcomes','기대 효과',601),txt(93,224,140,35,'Before',18,black,650),txt(926,224,100,35,'After',18,green,650),
...[[64.8,'64.8억','78억','매출',166,208],[18.4,'18.4%','20.0%','영업이익률',58,83],[18420,'18,420명','24,000명','신규 고객',83,160],[81,'81%','92%','과제 완료율',129,174]].map(([v,b,t,k,bw,tw],i)=>{let y=259+i*97;return[box(89,y,885,81),R(440-bw,y+23,bw+40,36,grey,18),R(600,y+23,tw+22,36,green,18),txt(111,y+25,190,40,b,24,'#888',500),txt(810,y+21,140,45,t,28,black,700,{align:'right'})]}),R(440,206,182,440,black,7),txt(459,224,144,35,'Category',18,'#fff',650,{align:'center'}),...['매출','영업이익률','신규 고객','과제 완료율'].map((k,i)=>[txt(454,284+i*97,154,39,k,22,'#fff',700,{align:'center'}),i<3&&L(459,348+i*97,603,348+i*97,'#929292',1,{dash:'2 2'})]),...[[275,'핵 개선폭','+13.2억 ▴'],[467,'핵심개선폭','+5,580명 ▴']].map(([y,k,v])=>[R(991,y,199,51,grad,5),S(984,y+18,8,15,`<svg viewBox="0 0 8 15" xmlns="http://www.w3.org/2000/svg"><path d="M8 0V15L0 7.5Z" fill="${green}"/></svg>`),txt(1008,y+15,75,29,k,14,'#fff'),txt(1072,y+10,118,39,v,22,'#fff',600,{align:'center',style:{whiteSpace:'nowrap'}})])
],bg));
// 20
s.push(slide('slide_20','Decision Requests',[
edgeGlow(405),C(79,76,16,green),en(107,74,360,140,'Decision\nRequests',46,black,650,{tracking:-1,lineHeight:1.22}),txt(112,207,340,35,'|  의사결정 요청사항',18,'#888'),
...[[477,92,green,'ClipboardCheck','운영 목표 승인',['핵심 채널 예산 확대','재구매 캠페인 강화','저효율 광고 캠페인 축소']],[855,92,mint,'FileCheck','핵심 전략 확정',['성장 채널 집중','실행 관리 강화']],[477,392,blue,'Puzzle','예산 및 리소스 배정',['총 예산 18억','4개 운영 조직 기준','비용 효율화']],[855,392,cyan,'Presentation','관리 체계 운영',['월간 KPI 리뷰','고위험 리스크 별도 보고']]].map(([x,y,c,ic,k,a])=>[box(x,y,359,275),...iconCircle(x+245,y+30,84,c,ic),txt(x+29,y+74,275,40,'•  '+k,24,black,700),R(x+23,y+123,313,130,bg,7),...a.map((v,i)=>txt(x+40,y+142+i*34,290,38,'□ '+v,20))]),box(87,552,339,49),box(87,612,339,49),R(99,565,4,24,green,2),R(99,625,4,24,green,2),txt(116,565,305,34,'전략운영본부 : 김미리 팀장',18),txt(116,625,305,34,'연락처 :  miri@company.co.kr',18)
],bg));
export default {id:'094',title:'2080 H2 Operational Plan',slides:s};
