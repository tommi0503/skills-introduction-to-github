import {text,rect,ellipse,line,path,icon,placeholder,group,slide} from '../ui/scene.js';
const B='#51a8e8',BP='#72b9ec',INK='#080808',G='#f6f6f6',L='#d1d1d1',M='#999999';
const grad='linear-gradient(90deg,#50a8e9 0%,#b7defb 100%)';
const t=(x,y,w,h,v,s=20,c=INK,wt=400,e={})=>text(x,y,w,h,v,s,c,wt,{lineHeight:1.3,...e});
const c=(x,y,w,h,v,s=20,col=INK,wt=400,e={})=>t(x,y,w,h,v,s,col,wt,{align:'center',...e});
const box=(x,y,w,h,fill=G,r=16,stroke=L)=>rect(x,y,w,h,fill,{radius:r,...(stroke?{border:stroke}:{})});
const pill=(x,y,w,h,v,s=20,fill='#fff',col=INK,stroke=L,wt=400)=>[box(x,y,w,h,fill,h/2,stroke),c(x,y,w,h,v,s,col,wt,{verticalAlign:'middle'})];
const logo=(x=1177,y=26,scale=1)=>[path(x,y,15*scale,15*scale,'M0 5Q0 0 5 0H15L8 7H1ZM0 15L7 8H14Q16 15 9 15Z',B,'none',{viewBox:'0 0 16 16'}),t(x+20*scale,y-3*scale,70*scale,25*scale,'MIRI',20*scale,INK,650)];
const foot=(plain=false)=>plain?[rect(0,667,1280,53,'#eeeeee'),t(59,684,750,25,'www.miricompany.com   |  미리컴퍼니 회사 소개서',15)]:[rect(17,666,1246,80,grad,{radius:36}),t(62,683,750,27,'www.miricompany.com   |  미리컴퍼니 회사 소개서',15),ellipse(1201,676,32,32,'#fff'),path(1208,681,18,22,'M5 4L12 11L5 18','none','#d8effc',{strokeWidth:4})];
const head=(title,sub='')=>[...logo(),c(60,53,1160,64,title,42,B,650),...(sub?[c(60,114,1160,38,sub,21)]:[])];
const page=(n,nodes,title,sub='')=>slide(`051-${String(n).padStart(2,'0')}`,[...(title?head(title,sub):[]),...nodes,...foot()]);
const lines=(x,y,w,arr,s=17,lh=1.6,col=INK)=>t(x,y,w,arr.length*s*lh+4,arr.join('\n'),s,col,400,{lineHeight:lh});
const ph=(x,y,w,h,r=22)=>placeholder(x,y,w,h,{radius:r});
const circleIcon=(x,y,name)=>[ellipse(x,y,106,106,'#fff',{border:'#c7c7c7',borderWidth:2}),...(name==='settings'?[aiChip(x+24,y+24,59,59)]:name==='file'?[rect(x+28,y+36,50,45,INK,{radius:3}),rect(x+35,y+26,40,45,'#fff',{border:INK,borderWidth:2}),line(x+39,y+34,29,0,INK,2),line(x+39,y+41,29,0,INK,2),rect(x+29,y+45,49,36,INK,{radius:3}),line(x+35,y+73,20,0,'#fff',2)]:[icon(x+27,y+25,54,54,name,INK,{strokeWidth:2.2})])];

const aiChip=(x,y,w=58,h=58)=>group(x,y,w,h,[path(0,0,w,h,'M13 13H57V57H13Z M19 4V11M30 4V11M41 4V11M52 4V11M19 59V66M30 59V66M41 59V66M52 59V66M4 19H11M4 30H11M4 41H11M4 52H11M59 19H66M59 30H66M59 41H66M59 52H66',INK,INK,{viewBox:'0 0 70 70',strokeWidth:1.5}),c(0,h*.22,w,h*.6,'AI',w*.4,'#fff',300,{verticalAlign:'middle'})]);
const chain=(x,y,w,h)=>path(x,y,w,h,'M31 41V20C31 7 51 7 51 20V42C51 55 31 55 31 42M37 37V21C37 15 45 15 45 21V39M31 43V60C31 73 51 73 51 60V41M37 46V60C37 66 45 66 45 60V44M23 27H11V59H23M59 27H71V59H59','none',INK,{viewBox:'0 0 82 82',strokeWidth:1.5});
const atom=(x,y)=>{let ns=[];for(let q=0;q<3;q++){let angle=q*Math.PI/3,d='';for(let k=0;k<=80;k++){let a=k*Math.PI*2/80,xx=29*Math.cos(a),yy=12*Math.sin(a);d+=(k?'L':'M')+(35+xx*Math.cos(angle)-yy*Math.sin(angle)).toFixed(2)+' '+(35+xx*Math.sin(angle)+yy*Math.cos(angle)).toFixed(2);}ns.push(path(0,0,70,70,d,'none','#fff',{strokeWidth:1.4}));}ns.push(c(0,24,70,30,'AI',18,'#fff',500));return group(x,y,70,70,ns)};
const headAI=(x,y)=>group(x,y,70,70,[path(0,0,70,70,'M52 66L49 47Q62 32 56 17Q49 0 31 3Q12 5 10 25L5 35Q3 40 13 40V48H25V66','none','#fff',{strokeWidth:1.5}),c(10,15,44,32,'AI',22,'#fff',550)]);
const pie=(x,y)=>path(x,y,34,34,'M12 2V12H22A10 10 0 1 1 12 2ZM15 1V9H23A10 10 0 0 0 15 1ZM15 13L22 20M12 12L19 19','none',INK,{viewBox:'0 0 24 24',strokeWidth:.85});
const chat=(x,y)=>path(x,y,34,34,'M12 3C6 3 2 6 2 10Q2 14 5 16L3 20L8 18Q11 19 14 17Q20 17 20 11C20 6 17 3 12 3ZM18 9Q24 10 24 16Q24 20 21 21L23 25L18 23Q12 24 10 20M7 10H7.1M11 10H11.1M15 10H15.1','none',INK,{viewBox:'0 0 26 26',strokeWidth:1});
const checklist=(x,y)=>path(x,y,34,34,'M7 4H3V23H21V4H17M8 3H10V1H14V3H17V6H8ZM6 10L7 11L9 9M12 10H18M6 15L7 16L9 14M12 15H18M6 20L7 21L9 19M12 20H18','none',INK,{viewBox:'0 0 24 25',strokeWidth:.85});


const databaseGear=(x,y)=>group(x,y,70,70,[icon(22,0,29,29,'settings','#fff',{strokeWidth:1}),path(0,0,70,70,'M17 35V61C17 69 35 69 35 61V35C35 29 17 29 17 35C17 41 35 41 35 35M17 43C17 49 35 49 35 43M17 51C17 57 35 57 35 51M43 38V63C43 68 61 68 61 63V38C61 32 43 32 43 38C43 44 61 44 61 38M43 46C43 52 61 52 61 46M43 54C43 60 61 60 61 54M12 18H7V54H12M59 18H65V54H61','none','#fff',{strokeWidth:1.1})]);
const circuitGear=(x,y)=>{let ns=[icon(18,18,34,34,'settings','#fff',{strokeWidth:1.1})];for(let i=0;i<8;i++){let a=i*Math.PI/4,cx=35+27*Math.cos(a),cy=35+27*Math.sin(a),ix=35+19*Math.cos(a),iy=35+19*Math.sin(a);ns.push(line(ix,iy,cx-ix,cy-iy,'#fff',1.1),ellipse(cx-2.2,cy-2.2,4.4,4.4,B,{border:'#fff',borderWidth:1.2}));}return group(x,y,70,70,ns)};

const slides=[];
// Cover — architecture photograph is deliberately replaced with a neutral seat.
slides.push(slide('051-01',[
 ...logo(59,50,1.15),t(58,176,600,55,'다이어그램을 활용한',38,INK,500),t(52,219,620,135,'COMPANY',100,INK,750,{letterSpacing:-1.4}),t(52,327,590,135,'PROFILE',100,B,750,{letterSpacing:-1.2}),t(59,510,550,44,'2056.10 · 경영기획팀',28),
 ph(721,-20,543,400,29),ph(623,388,394,249,29),ph(953,230,311,321,29),rect(725,-15,212,92,grad,{radius:25}),rect(1026,560,235,130,grad,{radius:30}),path(938,-1,335,640,'M2 0V63Q2 84 -19 84H-195Q-221 84 -221 110V349Q-221 384 -189 384H82Q111 384 111 352V255Q111 226 141 226H330', 'none','#fff',{strokeWidth:9}),path(940,225,330,430,'M329 0H139Q106 0 106 32V130Q106 160 77 160H34Q4 160 4 190V294Q4 331 40 331H49Q82 331 82 363V423','none','#fff',{strokeWidth:9}),...foot(true)
]));
// Contents
{
 const nodes=[c(0,50,1280,81,'Contents',58,B,650),line(0,375,1280,0,'#afd8f5',1.5)];
 const cols=[['PART 1.','우리는 어떤 회사인가',['미션과 비전','대표 인사말','일반 현황','연혁','조직 구성','성장 단계']],['PART 2.','무엇을 하는가',['사업 영역','사업 간 시너지','주력 사업','제품·서비스 라인업']],['PART 3.','어떻게 하는가',['프로젝트 일정','핵심 경쟁력','고객사와 파트너십']],['PART 1.','어디로 가는가',['성장 전략','오시는 길과 문의']]];
 cols.forEach((a,i)=>{let x=85+i*282;nodes.push(ph(x,171,258,150,16),t(x+4,340,255,29,a[0],18,B,650),ellipse(x,371,9,9,B),t(x+4,400,270,35,a[1],24,INK,650),lines(x+4,439,255,a[2].map(v=>'· '+v),18,1.55,M));});slides.push(page(2,nodes));
}
// Part divider
slides.push(page(3,[ph(786,-12,502,184,30),ph(880,178,401,290,28),ph(1101,329,210,268,28),rect(853,217,73,73,grad,{radius:13}),rect(775,296,72,73,grad,{radius:13}),rect(853,294,25,25,grad,{radius:4}),path(1099,0,181,340,'M181 6H35Q1 6 1 39V141Q1 174 35 174H71Q106 174 106 210V293Q106 330 144 330H183','none','#fff',{strokeWidth:9}),...pill(59,210,165,51,'Part.1',28,'#fff',INK,INK,650),t(57,278,750,120,'WHO WE ARE',88,INK,750,{letterSpacing:-1.2}),t(59,400,700,47,'우리는 어떤 회사인가',28,INK,650),box(59,487,1017,115,G,29),t(92,513,920,70,'인공지능 기반 데이터 솔루션으로\n기업의 디지털 혁신을 선도하는 미리컴퍼니입니다.',23,INK,400,{lineHeight:1.45})]));
// Vision / mission
slides.push(page(4,[box(157,182,967,307,G,160),ellipse(382,191,287,287,BP),ellipse(612,191,287,287,BP),path(612,245,58,178,'M29 0A143.5 143.5 0 0 1 29 178A143.5 143.5 0 0 1 29 0Z',B,'none',{opacity:.65}),icon(486,264,24,30,'lightbulb'),icon(771,265,28,28,'target'),c(412,298,230,29,'VISION',19,INK,500),c(397,328,260,90,'복잡한 비즈니스 문제를\nAI 기술로 명쾌하게 해결하는\n근본 가치 제공',19,INK,400,{lineHeight:1.4}),c(659,298,250,29,'MISSION',19,INK,500),c(668,328,232,90,'2030년까지 Global\nUnicorn AI Enterprise로의\n성공적인 진입',19,INK,400,{lineHeight:1.4}),line(641,353,0,154,'#888',1),box(158,509,967,116,G,28),c(160,524,963,37,'CORE VALUE',26,INK,650),...pill(186,563,317,47,'기술 우위 (Technological Excellence)',16,'#fff',INK,INK),...pill(522,563,237,47,'고객 중심 (Customer First)',16,'#fff',INK,INK),...pill(777,563,317,47,'지속 가능한 혁신 (Sustainable Innovation)',16,'#fff',INK,INK)],'Misson · Vision · Value','미션과 비전이 겹치는 지점에 우리가 지키는 원칙이 있습니다.'));
// CEO
slides.push(page(5,[ph(0,289,1280,377,0),ph(900,81,330,208,26),ph(771,289,459,377,0),t(86,185,720,80,'안녕하십니까,\n미리컴퍼니 대표 김미리입니다.',29,INK,650,{lineHeight:1.4}),lines(87,328,670,['미리컴퍼니는 2018년, 데이터를 통해 세상의 모든 기업이','더 똑똑하게 일할 수 있도록 돕겠다는 작은 꿈에서 출발했습니다.','지난 8년간 끝없는 기술 도전과 연구개발을 거쳐, 이제는 국내외 200여 개','주요 기업의 디지털 전환을 책임지는 데이터 솔루션 리더로 성장하였습니다.','','우리는 최첨단 AI 기술력과 철저한 사후 관리를 바탕으로, 고객의 성공이 곧','미리컴퍼니의 성장이라는 약속을 반드시 지켜나가겠습니다.','미래 시장을 선도하는 혁신 기술 기업으로서 글로벌 무대를 향해','더 크게 도약하겠습니다.'],15.5,1.55),t(475,581,400,50,'미리컴퍼니 대표이사 | 김미리',23)],"CEO's Message",'데이터와 AI 기술로 기업의 내일을 혁신하는 미리컴퍼니'));
// financial table
{
 let a=[box(95,175,1089,450,'#fff',10),rect(96,176,1087,55,'#a0a0a0',{radius:8}),rect(367,176,816,55,'#a0a0a0'),rect(912,175,272,450,grad),rect(912,176,272,55,'#000'),rect(909,172,278,456,'transparent',{radius:13,border:B,borderWidth:6})];
 const vals=[['구분','2024','2025','2026 예상'],['매출액','320억 원','390억 원','450억 원'],['영업이익','38억 원','47억 원','62억 원'],['영업이익률','11.9%','12.1%','13.8%'],['당기순이익','27억 원','34억 원','46억 원'],['유동자산','145억 원','183억 원','215억 원'],['부채','82억 원','96억 원','108억 원'],['자기자본','118억 원','151억 원','193억 원']];
 vals.forEach((r,i)=>r.forEach((v,j)=>a.push(c(96+j*272,176+i*56.2,272,55,v,j===3?23:19,i===0&&j===3?'#fff':INK,i===0||j===3?550:400,{verticalAlign:'middle'}))));
 for(let i=1;i<8;i++)a.push(line(95,175+i*56.2,1089,0,'#c7c7c7',1));for(let j=1;j<4;j++)a.push(line(95+j*272,175,0,450,'#c7c7c7',1));slides.push(page(6,a,'Financial Status','단단한 재무적 기반 위에 모두가 신뢰할 수 있는 미래를 설계합니다.'));
}
// history
{
 const items=[['2058 · 설립기',['미리컴퍼니 법인 설립','MiriData v1.0 출시']],['2060 · 성장기',['시리즈 A 50억 원 투자 유치','임직원 50명 돌파','미리 R&D 센터 개소','B2B 데이터 솔루션 사업 확대']],['2062 · 도약기',['MiriAI 출시','주요 보안 인증 취득','주요 기업 고객 50개사 확보']],['2064~현재 · 확장기',['시리즈 B 150억 원 투자 유치','누적 매출 400억 원 돌파','해외 법인 설립','글로벌 사업 본격화','국내 중심 사업 구조에서','해외 시장까지 사업 영역 확대']]];
 const a=[line(108,443,1064,0,B,6)];items.forEach((it,i)=>{let x=108+i*268;a.push(ph(x,173,259,162,18),...pill(x+(i===3?18:52),361,i===3?216:164,57,it[0],24,'#fff',INK,'#999',500),line(x+133,418,0,25,'#999',3),ellipse(x+125,435,16,16,B,{border:'#fff',borderWidth:3}),lines(x+19,474,258,it[1].map(v=>'· '+v),17,1.6));});slides.push(page(7,a,'Company History','지난 도전의 발자취가 모여, 더 큰 미래를 향한 길을 만듭니다.'));
}
// culture people
{
 const a=[];const items=[[93,188,'AUTONOMY 자율과 책임',['스스로 판단하고 실행','맡은 업무의 결과까지 책임']],[751,188,'CURIOSITY 끊임없는 탐구',['WHY에서 시작하는 문제 해결','새로운 기술과 방식에 대한 지속적 학습','더 나은 방법을 끊임없이 탐색']],[93,410,'SYNERGY 집단지성 시너지',['서로 다른 전문성을 연결','정보와 경험을 적극적으로 공유','개인의 역량을 조직의 성과로 확장']],[751,410,'GROWTH 함께 성장',['피드백을 통한 지속적인 개선','개인의 성장이 조직의 성장으로 이어지는 환경','새로운 역할과 도전에 적극적으로 참여']]];
 items.forEach(([x,y,title,ls])=>a.push(box(x,y,431,199,'#efefef',10,null),box(x+29,y+26,372,54,'#fff',30),t(x+49,y+39,350,34,title,23,INK,500),lines(x+44,y+98,370,ls.map(v=>'· '+v),17,1.55)));
 a.push(ellipse(544,305,187,187,B),ellipse(623,333,29,29,'#fff'),path(613,361,50,29,'M0 13Q10 0 15 0Q25 6 35 0Q44 3 50 13Q43 29 25 28Q8 28 0 13Z','#fff','none'),c(555,407,166,73,'MIRI\nPEOPLE',24,'#fff',550));slides.push(page(8,a,'Culture & Ideal Talent','전문성을 기반으로 자율적으로, 협업을 통해 큰 성과를 만드는 조직을 지향합니다.'));
}
// growth stages
{
 const d=[['STAGE 1','창업기\n(2058~2059)',['AI 데이터 엔진 핵심','알고리즘 개발','초기 금융권 고객 확보']],['STAGE 2','성장기\n(2060~2062)',['연 매출 150억 원 달성','R&D 중심 연구소 확충','전문 인력 채용 확대','조직 규모 100명으로 성장']],['STAGE 3','확장기\n2063~현재)',['글로벌 SaaS 시장 진출','해외 사업 기반 확대','파트너십 150개사 확보']],['STAGE 4','성숙기\n(2067~)',['글로벌 Enterprise','AI 시장 지위 확립','안정적 수익 구조 구축']]];
 let a=[];d.forEach((it,i)=>{let x=158+i*257,y=254-i*26;a.push(box(x,y,197,262,'#efefef',10,null),rect(x+10,y+10,177,39,B,{radius:2}),t(x+29,y+20,160,29,it[0],17,INK,500),t(x+20,y+66,170,62,it[1],21,INK,500),t(x+20,y+126,172,122,it[2].map((v,j)=>(i===0&&j===1?'  ':i===3&&j===1?'  ':'· ')+v).join('\n'),16.5,INK,400,{lineHeight:1.4}));if(i<3)a.push(icon(x+211,y+109,30,34,'arrow',B,{strokeWidth:2.6}));});a.push(box(158,532,967,91,G,13),c(177,552,930,35,'현재 우리는 STAGE 3 · 확장기에 있습니다.',23),c(177,586,930,25,'기술과 고객 기반을 바탕으로 글로벌 시장 확장을 본격화하는 단계',15,M));slides.push(page(9,a,'Culture & Ideal Talent','전문성을 기반으로 자율적으로, 협업을 통해 큰 성과를 만드는 조직을 지향합니다.'));
}
// business results combo chart and table
{
 let a=[box(94,175,516,49,G,11),c(95,185,514,33,'연도별 성장 추이 콤보차트',23,INK,650),box(665,175,517,49,G,11),c(665,185,517,33,'사업 영역별 매출 비중 표',23,INK,650)];
 for(let i=0;i<6;i++){let y=554-i*56.6;a.push(line(138,y,430,0,'#ccc',1),t(101,y-9,31,24,String(i*100),14,INK,400,{align:'right'}),t(575,y-9,28,24,String(i*20),14));}a.push(line(138,271,0,283,'#ccc',1),line(568,271,0,283,'#ccc',1));
 const rev=[28,67,142,254,380,450],ren=[62,71,78,85,91,94],xs=[173,245,317,389,461,533];
 rev.forEach((v,i)=>{let h=v/500*283;a.push(rect(xs[i]-24,554-h,48,h,'#000'),c(xs[i]-23,559-h,46,25,String(v),14,'#fff'),c(xs[i]-40,560,80,24,i===5?'2065(현재)':String(2060+i),14));});
 for(let i=0;i<5;i++)a.push(line(xs[i],554-ren[i]/100*283,xs[i+1]-xs[i],-(ren[i+1]-ren[i])/100*283,B,2));
 ren.forEach((v,i)=>a.push(ellipse(xs[i]-7,554-v/100*283-7,14,14,B),c(xs[i]-21,554-v/100*283-29,42,23,String(v),14,B)));
 a.push(rect(269,600,13,14,'#000',{radius:3}),t(286,598,80,24,'매출 (억원)',13),ellipse(350,600,13,13,B),t(367,598,100,24,'재계약률 (%)',13));
 let rows=[['사업 영역','주요 서비스','매출 비중','고객사 수'],['Miri\nIntelligence','AI 플랫폼·\n예측 솔루션','45%','120개사'],['Miri\nCloud','SaaS·\n클라우드 스토리지','30%','85개사'],['DX\nConsulting','데이터 파이프라인·\nDX 자문','15%','32개사'],['M&O','24/7 유지보수·\nAI 튜닝','10%','210개사\n(유지)']];let widths=[132,193,92,100];let xs2=[665,797,990,1082];a.push(box(665,237,517,386,'#fff',14),rect(665,237,517,49,B,{radius:12}),rect(665,265,517,21,B));
 rows.forEach((r,i)=>{let y=i===0?237:286+(i-1)*84;if(i>0&&i%2===0)a.push(rect(666,y,515,84,'#efefef'));r.forEach((v,j)=>a.push(c(xs2[j],y,widths[j],i?84:49,v,18,i?'#000':'#fff',i?400:600,{verticalAlign:'middle'})));if(i)a.push(line(665,y,517,0,L,1));});for(let i=1;i<4;i++)a.push(line(xs2[i],237,0,386,L,1));slides.push(page(10,a,'Business Results','지속가능한 미래를 향해 끊임없이 가치를 창출해 나갑니다.'));
}
// at glance
{
 let a=[t(131,165,310,34,'Miri Intelligence',24,INK,550),lines(131,207,290,['데이터 통합 수집','실시간 AI 예측','대규모 데이터 분석 자동화'],19,1.45),t(131,318,310,35,'DX Consulting',24,INK,550),lines(131,357,280,['고객 데이터 환경 진단','맞춤형 데이터 파이프라인 설계','DX 전략 및 실행 로드맵 자문'],19,1.45),t(888,165,261,34,'Miri Cloud',24,INK,550,{align:'right'}),lines(889,207,260,['SaaS SERVICE','Cloud Data Storage','Analytics Tool'],19,1.45),t(881,318,268,35,'Maintenance & Operation',23,INK,550,{align:'right'}),t(893,357,256,87,'성능 모니터링\n장애 대응\n지속적인 운영 최적화',19,INK,400,{align:'right',lineHeight:1.45}),...circleIcon(407,170,'settings'),...circleIcon(407,321,'file'),...circleIcon(767,170,'cloud'),...circleIcon(767,321,'search'),c(523,165,234,37,'MIRI COMPANY',23,B,650),ellipse(544,204,191,191,B),c(546,273,187,70,'데이터 전 과정을 잇는\nEnd-to-End AI 솔루션',19,'#fff',550,{lineHeight:1.4}),c(380,444,520,43,'매출 포트폴리오 요약',27,INK,650)];
 // Keep right service labels right aligned.
 a[5]={...a[5],align:'right'};
 ['Miri Intelligence','Miri Cloud','DX Consulting','Maintenance & Operation'].forEach((v,i)=>{let x=131+i*259;a.push(box(x,496,241,112,G,20),...pill(x,496,241,39,v,18),c(x,548,241,57,['45%','30%','15%','10%'][i],42,INK,700));});slides.push(page(11,a,'Business at a Glance'));
}
// synergy
slides.push(page(12,[box(94,175,1088,448,'#fff',34),ellipse(248,199,234,234,'#fff',{border:L}),ellipse(152,365,234,234,'#eee',{border:L}),ellipse(344,365,234,234,'#92cef7',{opacity:.5,border:'#bbb'}),c(274,253,181,32,'Miri Intelligence',20,INK,650),c(268,286,193,86,'독자 개발한\n고성능 AI 예측\n알고리즘 기술',19,INK,400,{lineHeight:1.45}),c(172,432,196,32,'Miri Cloud',20,INK,650),c(172,465,196,89,'대용량 데이터를\n유연하게 처리하는\n클라우드 인프라',19,INK,400,{lineHeight:1.45}),c(368,432,184,32,'DX Consulting',20,INK,650),c(363,465,195,89,'각 산업 분야별\n도메인 전문성과\n기획 역량',19,INK,400,{lineHeight:1.45}),box(646,197,487,122,'#fff',20),c(661,232,455,80,'기업 맞춤형 클라우드 데이터\n파이프라인 구현',24),box(646,338,487,122,'#fff',20),c(661,369,455,80,'클라우드 환경에서 즉시 동작하는\nAI SaaS 모델 구축',24),box(646,479,487,122,'#e3f2fd',20),c(661,512,455,80,'고객 맞춤형 데이터\n생태계 구축 및 자동화 완성',24,INK,650)],'Business Synergy Structure','사업은 나뉘어 있지만 역량은 하나로 모입니다.'));
// core business
{
 let a=[];const data=[['Miri Intelligence','기업 내 유기적으로 흩어져 있는 비정형 데이터를 실시간으로 수집하고 분석하는 AI 솔루션입니다.\n고도화된 예측 알고리즘을 통해 의사결정 시간을 70% 이상 단축시킵니다.','AI 데이터 분석, 실시간 이상 탐지, 미래 매출 예측 모델','프로젝트 180건 · 고객 120개사','lightbulb'],['Miri Cloud','초기 구축 비용 부담 없이 월 구독 형태로 이용할 수 있는 보안 특화 클라우드 플랫폼입니다.\n엔터프라이즈급 보안 환경을 바탕으로 손쉬운 데이터 시각화 리포트를 제공합니다.','SaaS 데이터 스토리지, Auto-Dashboard, 데이터 암호화','프로젝트 95건 · 고객 85개사','settings']];
 data.forEach((d,i)=>{let y=175+i*230;a.push(box(94,y,1088,219,i? '#fff':G,33),t(160,y+31,760,42,d[0],29,INK,650),t(160,y+81,780,60,d[1],18,INK,400,{lineHeight:1.35}),t(160,y+142,130,31,'주요 서비스',18,B,650),t(281,y+142,660,31,d[2],18),t(160,y+168,100,31,'성과',18,B,650),t(281,y+168,650,31,d[3],18),box(971,y+35,149,149,G,22),...(i?[chain(1005,y+69,80,80)]:[icon(1005,y+69,80,80,d[4],INK,{strokeWidth:.7})]));});slides.push(page(13,a,'Core Business Details','비즈니스의 중심을 지탱하며 가장 확실한 가치를 만들어내는 영역입니다.'));
}
// lineup
{
 let a=[];const d=[['MiriData Engine','•  초고속 실시간 데이터 수집·정\n•  대용량 데이터 처리에 최적화된\n   엔터프라이즈 솔루션','대기업 데이터 조직'],['MiriAI Insights','•  머신러닝 기반 비즈니스 지표 자동\n   예측\n•  주요 지표 예측\n•  데이터 기반 의사결정 지원','전략기획팀·경영진'],['Miri Cloud Hub','•  멀티 클라우드 환경의 데이터를\n   안전하게 통합·관리하는 데이터\n   저장소','IT 인프라·보안 관리팀'],['Miri BI Dashboard','•  코딩 없이 Drag & Drop으로\n   완성하는 데이터 시각화 툴\n•  데이터 연결\n•  대시보드 제작','마케팅·영업팀'],['Miri Security Shield','•  AI 기반 개인정보·민감 데이터\n   자동 탐지 및 마스킹\n•  보안이 중요한 데이터 환경에 특화','금융·의료 기관'],['Miri Ops Agent','•  데이터 파이프라인 자동화\n•  24/7 운영 모니터링\n•  이상 징후 탐지 및 대응\n•  반복 운영 업무 자동화','DevOps·데이터 엔지니어']];
 d.forEach((it,i)=>{let x=94+(i%3)*367,y=175+Math.floor(i/3)*231;a.push(box(x,y,353,220,i%2?'#fcfcfc':'#fff',28),t(x+50,y+26,295,40,it[0],24,INK,650),t(x+50,y+64,288,110,it[1].replaceAll('•',' '),18,INK,400,{lineHeight:1.38}),t(x+50,y+174,90,32,'주요 고객',18,B,650),t(x+131,y+174,209,37,it[2],18));[[0,1],[0,2,3],[0],[0,2,3],[0,2],[0,1,2,3]][i].forEach(r=>a.push(ellipse(x+51,y+73+r*24.84,7,7,INK)));});slides.push(page(14,a,'Product & Service Lineup','세분화된 고객의 니즈에 맞춰 최적화된 라인업을 제공합니다.'));
}
// process
{
 let a=[box(94,175,1088,448,G,34),ellipse(441,200,398,398,'#fff'),ellipse(519,279,241,241,G),ellipse(563,322,154,154,B),c(564,383,153,42,'고객 성공',27,'#fff',650)];
 const ds=[['문의·상담','고객 요구사항 정의\n도입 목적 및 핵심 과제 파악'],['분석·제안','데이터 인프라 현황 진단\n고객 환경에 맞춘 솔루션 제안'],['계약·설계','최종 사업 범위 확정\n프로젝트 수행 체계 설계'],['제작·구축','AI 모델링 개발 및 데이터 연동\n실사용 환경 기준 성능 최적화'],['검수·납품','시스템 최종 통합 테스트\n보안 점검 및 사용자 교육 후 인도'],['운영·고도화','주기적 AI 모델 재학습 및 성능 개선\n개선 결과를 다음 과제 발굴로 연결']];
 ds.forEach((d,i)=>{let right=i>=3,x=right?879:131,y=203+(i%3)*142;a.push(t(x,y,270,24,`PART ${i+1}.`,13,B,650,{align:right?'right':'left'}),t(x,y+22,270,36,d[0],24,INK,650,{align:right?'right':'left'}),t(right?874:131,y+58,right?275:300,70,d[1],19,INK,400,{lineHeight:1.4,align:right?'right':'left'}));if(i%3<2)a.push(line(x,y+125,268,0,'#ddd',1,{dash:'1 2'}));});
 for(let k=0;k<140;k++){let a1=k*Math.PI*2/140;a.push(ellipse(639+159*Math.cos(a1),398+159*Math.sin(a1),1.1,1.1,'#888'));}
 const coords=[[603,202],[465,283],[465,442],[603,522],[741,442],[741,283]];coords.forEach((p,i)=>a.push(ellipse(p[0],p[1],75,75,'#000'),c(p[0]-1,p[1],77,75,ds[i][0].replace('운영·고도화','운영·\n고도화'),19,'#fff',550,{verticalAlign:'middle'})));slides.push(page(15,a,'Our Process','한 번의 거래가 아니라 지속적으로 개선되고 반복되는 고객 관계를 설계합니다.'));
}
// schedule
{
 let a=[line(122,272,1033,0,B,6)];const d=[['1~2주차','착수','프로젝트 킥오프\n워크숍 진행 및 기본\n데이터 · 요구사항 확정','users'],['3~4주차','설계','시스템 데이터 구조\n설계 및 AI 알고리즘\n모델링 기획안 확정','file'],['5~10주차','제작','데이터 파이프라인\n구축, AI 학습 및\n기능 개발','chart'],['11~12주차','검수','내부 QA 수행, 데이터\n정확도 테스트 및\n고객 피드백 반영','file'],['13~14주차','납품','최종 솔루션 운영 환경\n이관, 사용자 매뉴얼\n전달 및 인수인계','briefcase']];
 d.forEach((v,i)=>{let x=225+i*207;a.push(...pill(x-48,205,96+(i>1?10:0),41,v[0],20,B,'#fff',null,550),line(x,246,0,17,B,2),ellipse(x-11,261,22,22,'#fff',{border:B,borderWidth:4}),...(i===0?[chat(x-17,315)]:i===2?[pie(x-17,315)]:i===3?[checklist(x-17,315)]:[icon(x-17,315,34,34,v[3],INK,{strokeWidth:1})]),c(x-95,359,190,39,v[1],24,INK,550),c(x-104,401,208,92,v[2],19,INK,400,{lineHeight:1.45}));});a.push(box(122,516,1036,107,G,17),c(132,535,1016,40,'표준 소요 기간 14주',27,B,650),c(132,579,1016,35,'프로젝트 규모에 따라 조정됩니다',24));slides.push(page(16,a,'Standard Project Schedule','프로젝트의 전체적인 진행 일정과 단계별 절차를 안내합니다.'));
}
// competencies
{
 let a=[];const d=[[122,178,'기술력','독자 개발 AI 특허 34건 보유\n고도화된 데이터 처리 품질 확보'],[821,178,'전문 인력','석·박사급 데이터 분석가, 전문 엔지니어 85명\n기술을 안정적으로 구현하는 전문 조직'],[122,361,'검증된 실적','누적 프로젝트 300건 이상\n다양한 산업 경험 축적'],[821,361,'사후 지원','실시간 모니터링, 주기적인 AI 모델 업데이트\n개선된 기술력을 다시 서비스에 환원']];
 d.forEach(([x,y,tt,b])=>a.push(box(x,y,337,125,'#efefef',7,null),c(x+9,y+17,319,36,tt,24,INK,550),c(x+5,y+59,327,62,b,18.5,INK,400,{lineHeight:1.45})));
 [[483,175,'globe'],[667,175,'user'],[483,358,'building'],[667,358,'settings']].forEach(([x,y,i])=>a.push(ellipse(x,y,130,130,B),...(i==='globe'?[atom(x+30,y+30)]:i==='user'?[headAI(x+30,y+30)]:i==='building'?[databaseGear(x+30,y+30)]:[circuitGear(x+30,y+30)])));a.push(ellipse(559,253,162,162,'#000'),c(564,301,151,32,'재계약률',18,'#fff',550),c(564,330,151,48,'94%',32,B,650),box(122,516,1036,107,G,17),c(132,541,1016,77,'네 가지 핵심 역량이 서로를 강화하고\n높은 고객 만족과 재계약으로 이어지는 선순환 구조',24));slides.push(page(17,a,'Virtuous cycle of core competencies','지속가능한 성장을 이끄는 핵심역량의 선순환'));
}
// clients
{
 let a=[box(94,175,1088,219,G,34),line(354,195,0,181,'#ddd',1,{dash:'1 2'}),line(845,195,0,181,'#ddd',1,{dash:'1 2'}),t(140,201,200,35,'누적 실적',24,INK,550),t(384,201,350,35,'주요 고객사',24,INK,550),t(878,201,290,35,'대표 구축 사례 · 미리전자',23,INK,550),t(878,239,280,56,'스마트 팩토리\n불량률 예측 AI 구축',18,INK,400,{lineHeight:1.45})];
 ['프로젝트','고객사','재계약률'].forEach((v,i)=>a.push(...pill(140,272+i*36,76,23,v,12),t(233,271+i*36,110,30,['320건','210개사','94%'][i],23,B,650)));
 ['미리전자','미리IT','미리금융','미리통신','미리쇼핑','미리소프트'].forEach((v,i)=>{let x=438+i%3*134,y=244+Math.floor(i/3)*65;a.push(ph(x+12,y,31,31,2),c(x-10,y+36,80,24,v,15));});a.push(...pill(878,309,76,23,'공정 불량률',12),t(970,307,190,31,'35% 감소',23,B,650),...pill(878,345,76,23,'재계약률',12),t(970,343,190,31,'120억 원 절감',23,B,650),box(94,407,1088,220,'#fff',34));
 const partners=[['기술 파트너','미리테크','공식 클라우드 MSP','미리클라우드','AI 기술 협력'],['유통·판매 파트너','미리솔루션','엔터프라이즈 솔루션 총판 계약','미리시스템','엔터프라이즈 솔루션 총판 계약'],['연구·기관 협력','미리대학교','AI 연구원 산학 협력','미리기술연구원','미리대학교 공동 연구']];
 partners.forEach((d,i)=>{let x=140+i*355;if(i)a.push(line(x-34,428,0,181,'#ddd',1,{dash:'1 2'}));a.push(t(x,433,295,36,d[0],24,INK,550));for(let j=0;j<2;j++){let y=481+j*67;a.push(ph(x,y,52,53,7),t(x+79,y+2,260,30,d[1+j*2],19),t(x+79,y+33,264,25,d[2+j*2],15,M));}});slides.push(page(18,a,'Partnerships with key clients','신뢰와 협력으로 함께 만드는 성공 파트너십'));
}
// roadmap
{
 let a=[box(94,175,1088,448,'#fff',34),...pill(128,200,1020,41,'Future Plans',24,B,'#fff',null,550)];
 const ds=[['STEP 1','단기 (2026)','생성형 AI 탑재 MiriAI v3.0 출시\n주요 그룹사 도메인 확장'],['STEP 2','중기 (2027~2028)','글로벌 거점 확보\nB2B SaaS 시장 본격 진출\n해외 고객·파트너십 확대'],['STEP 3','장기 (2029~2030)','글로벌 Top 10 진입\n미리닥 IPO 추진\n글로벌 사업 구조 고도화'],['STEP 4','2030 TARGET','매출 2,000억 원\n임직원 500명\n글로벌 매출 비중 40% 달성']];
 ds.forEach((d,i)=>{let x=130+i*255,y=386-i*41.2,h=i?210:187;if(i)a.push(rect(x,y+h,250,597-y-h,G,{radius:5}));a.push(box(x,y,250,h,'#fff',7,'#bbb'),c(x+5,y+27,240,32,d[0],20,B,550),c(x+5,y+68,240,42,d[1],24,INK,550),c(x+9,y+117,232,81,d[2],16,INK,400,{lineHeight:1.4}));});slides.push(page(19,a,'Growth Strategy & Future Plans','지속가능한 미래를 위한 성장 전략과 로드맵'));
}
// Closing
slides.push(slide('051-20',[...logo(72,77,1.15),ph(668,-20,370,120,31),ph(1048,-20,251,304,28),ph(781,110,500,342,28),ph(1043,445,250,162,27),rect(693,148,32,32,grad,{radius:5}),rect(732,156,73,73,grad,{radius:15}),rect(673,236,72,72,grad,{radius:15}),path(1038,-4,251,307,'M2 0V68Q2 109 39 109H93Q126 109 126 144V255Q126 292 163 292H252','none','#fff',{strokeWidth:10}),path(781,443,281,190,'M0 4H227Q260 4 260 37V136Q260 166 281 166','none','#fff',{strokeWidth:7}),t(72,265,650,50,'함께 만들어갈 다음을 기대합니다',30,INK,550),t(68,313,700,126,'THANK YOU',90,B,700,{letterSpacing:.1}),box(72,469,647,134,G,21),rect(106,501,19,20,INK,{radius:2}),icon(108,503,15,16,'target','#fff',{strokeWidth:2.5}),rect(106,527,19,20,INK,{radius:2}),icon(108,529,15,15,'phone','#fff',{strokeWidth:2.5}),path(106,552,19,20,'M0 8L9.5 0L19 8H16V19H11V13H7V19H3V8Z',INK,'none'),lines(139,499,550,['미리시 미리구 미리로 100, 미리타워 15층','미리컴퍼니 경영지원팀 | 02-555-1234 | contact@miri.com','www.miri.com'],17,1.55),rect(0,667,1280,53,B),t(59,684,850,26,'www.miricompany.com   |  미리컴퍼니 회사 소개서',15,'#fff')]));
export {slides};
