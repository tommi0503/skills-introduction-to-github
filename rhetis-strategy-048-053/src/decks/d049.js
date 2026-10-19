import {text as T,rect as R,ellipse as E,line as L,path as P,group as G,slide as S} from '../ui/scene.js';
const C={slate:'#687888',frame:'#aeb7c3',pale:'#ced7e5',ink:'#000',gray:'#818181',line:'#b5b5b5'};
const grad='linear-gradient(90deg,#cfdfef,#697788)';
const gradV='linear-gradient(180deg,#cbdff0,#697988)';
const tx=(x,y,w,h,v,s=20,c='#000',wt=400,e={})=>T(x,y,w,h,v,s,c,wt,{lineHeight:1.3,...e});
const center=(x,y,w,h,v,s=20,c='#000',wt=700,e={})=>tx(x,y,w,h,v,s,c,wt,{align:'center',verticalAlign:'middle',...e});
const heavy=(x,y,w,h,v,s=56,c='#000',e={})=>tx(x,y,w,h,v,s,c,400,{font:'Black Han Sans',letterSpacing:-1.1,...e});
const frame=(dark=false)=>[R(0,0,1280,720,dark?C.slate:C.frame),R(22,21,1236,678,'#fff')];
const base=(title,sub)=>[...frame(),tx(1130,35,114,21,'MIRI COMPANY',13,C.frame,600,{letterSpacing:0}),heavy(79,56,1120,68,title,title.includes('overview')?53.5:title.includes('as-is')?53:56),tx(79,124,1122,35,sub,23,'#000',600,{letterSpacing:-.65}),L(80,177,1120,0,'#888',1)];
const shadow=(x,y,w,h)=>[R(x+4,y+6,w,h,'#f1f1f1'),R(x+8,y+10,w,h,'#f8f8f8'),R(x,y,w,h,'#fff',{border:'#d7d7d7'})];
const panel=(x,w,title)=>[...shadow(x,213,w,444),R(x,213,w,58,C.slate),center(x,213,w,58,title,24,'#fff',700)];
const arrow=(x,y,w,h,fill=C.slate)=>P(x,y,w,h,`M0 0H${w*.65}V${h*.25}H${w}L${w*.5} ${h}L0 ${h*.25}H${w*.35}V0Z`,fill,'none');
const plus=(x,y)=>[E(x,y,46,46,'#fff',{border:C.slate}),R(x+20,y+11,7,25,C.slate),R(x+11,y+20,25,7,C.slate)];
const num=(x,y,n,size=27)=>[E(x,y,size,size,C.slate),center(x,y,size,size,String(n),size*.67,'#fff',700)];
const pill=(x,y,w,h,v,s=18)=>[R(x,y,w,h,'#fff',{radius:h/2,border:C.slate,borderWidth:3}),center(x,y,w,h,v,s,'#000',400)];
const slides=[];
slides.push(S('049-01',[
R(0,0,1280,720,C.slate),R(34,33,1212,654,'#fff'),L(47,33,0,654,'#c8c8c8'),L(1232,33,0,654,'#c8c8c8'),L(34,47,1212,0,'#c8c8c8'),L(34,674,1212,0,'#c8c8c8'),
center(300,119,680,34,'MIRI COMPANY',25,'#818181',600,{letterSpacing:1}),heavy(240,153,800,119,'전사 운영',103,'#000',{align:'center'}),heavy(195,260,890,122,'효율화 전략',103,C.slate,{align:'center'}),center(300,386,680,37,'이곳에 부제목을 입력해 주세요.',27,'#818181',400),L(206,599,868,0,'#999',1.3),
tx(227,615,62,30,'Mail.',21,'#bbb',800),tx(293,615,242,30,'contact@miridih.com',21,'#818181'),tx(532,614,20,30,'|',23,'#818181'),tx(582,615,50,30,'Tel.',21,'#bbb',800),tx(633,615,176,30,'030-000-0000',21,'#818181'),tx(814,614,20,30,'|',23,'#818181'),tx(858,615,250,30,'미리시 미리로 미리구 7',21,'#818181')
]));
{
const n=[...frame(true),heavy(400,105,480,101,'목차',82,'#000',{align:'center'}),L(89,224,1102,0,'#888',1.3)];
[[130,278,1,'배경 및 현황 진단'],[130,398,2,'문제점 및 개선 기회'],[130,519,3,'개선 전략 및 실행 계획'],[657,278,4,'추진 체계 및 관리 방안'],[657,398,5,'이곳에 목차를 입력하세요.']].forEach(([x,y,i,t])=>n.push(...shadow(x,y,493,86),heavy(x+47,y+17,52,58,`${i}.`,43,C.slate),tx(x+101,y+28,370,38,t,24,'#000',500,{letterSpacing:-.8})));
slides.push(S('049-02',n));}
{
const n=[...base('배경 및 필요성','급변하는 시장 환경 속에서 운영 효율화가 기업 생존의 핵심 과제로 부상'),...panel(80,333,'시장 환경 변화'),...panel(474,333,'경쟁사 동향'),...panel(867,333,'내부 당면 과제')];
n.push(center(108,298,277,54,'글로벌 경기 불확실성\n증대로 인한 비용 압박 심화',19,'#000',400),L(115,367,263,0,'#d5d5d5',1,{dash:'2 2'}),center(109,397,276,52,'이곳에 두 번째 외부 환경\n변화 요인을 입력하세요.',19,'#000',400));
[['시장 환경 변화',475],['내부 역량 강화 필요',529],['운영 효율화 시급',582]].forEach(([v,y],i)=>{n.push(R(113,y,267,33,grad),center(113,y,267,33,v,19,'#fff',700));if(i<2)n.push(P(231,y+33,27,21,'M0 0H27L13.5 21Z',C.slate,'none'));});
n.push(...plus(420,409),...plus(813,409),center(499,298,281,54,'주요 경쟁사들의 공격적인\n효율화 투자 진행 중',19,'#000',400),L(508,367,264,0,'#d5d5d5',1,{dash:'2 2'}),center(498,396,284,53,'이곳에 경쟁사의 성과나\n벤치마크 지표를 입력하세요.',19,'#000',400),center(510,464,260,22,'<경쟁사 혁신 투자 규모>',13,'#6f6f6f',400));
const tableX=506,tableY=490,cw=89; n.push(R(tableX,tableY,267,26,'#bebebe')); for(let r=0;r<6;r++)n.push(L(tableX,tableY+r*26,267,0,'#aaa'));for(let c=0;c<4;c++)n.push(L(tableX+c*cw,tableY,0,130,'#aaa'));
[['순위','기업명','투자액'],['1','기업C','XXX억'],['2','기업A','XXX억'],['3','기업D','XXX억'],['4','기업B','XXX억']].forEach((r,i)=>r.forEach((v,j)=>n.push(center(tableX+j*cw,tableY+i*26,cw,26,v,13,'#707070',400))));
n.push(center(894,298,278,54,'레거시 시스템과\n신규 플랫폼 간 호환성 문제',19,'#000',400),L(901,367,263,0,'#d5d5d5',1,{dash:'2 2'}),center(895,397,278,52,'이곳에 두 번째 내부 과제를\n입력하세요.',19,'#000',400),R(899,461,266,59,grad),center(899,461,266,59,'빠른 성과 창출',18,'#fff',700),P(958,516,146,52,'M73 0L146 26L73 52L0 26Z','#d0d9e5','none'),center(958,517,146,49,'항목간\n균형 필요',15,'#000',500),R(899,562,266,59,grad),center(899,562,266,59,'안정적 운영 유지',18,'#fff',700));slides.push(S('049-03',n));}
{
const n=[...base('문제점 분석','현재 운영 상의 핵심 문제점을 구조적으로 파악하여 개선 방향 도출'),...panel(80,547,'현재 운영 구조의 문제점'),...panel(653,547,'운영 관련 조직 인식')];
n.push(R(212,298,123,71,C.slate),center(212,298,123,71,'의사결정\n단계',20,'#fff',700),R(344,298,121,32,'#fff',{border:C.slate}),R(344,336,121,32,'#fff',{border:C.slate}),center(344,298,121,32,'승인 지연',19,'#000',700),center(344,336,121,32,'정보 단절',19,'#000',700),L(348,368,0,54,'#888'),L(190,395,314,0,'#888'),L(190,395,0,27,'#888'),L(504,395,0,27,'#888'));
[['본부장',145],['팀장',303],['실무자',462]].forEach(([v,x])=>n.push(R(x,422,90,32,grad),center(x,422,90,32,v,17,'#fff',700),center(x-26,463,143,40,'이곳에 현재 문제를\n넣어보세요.',14,'#000',400)));
n.push(L(116,523,464,0,'#d0d0d0',1,{dash:'2 2'}));['X단계 이상의 복잡한 의사결정 구조','중복 검토 및 불필요한 보고 단계 존재','구조적 문제점을 구체적으로 설명해 보세요.'].forEach((v,i)=>n.push(...num(184,540+i*35,i+1,27),tx(224,543+i*35,382,27,v,16,'#000',400)));
n.push(tx(739,292,35,31,'Q.',26,C.slate,800),tx(771,297,410,30,'업무 처리 시 가장 큰 애로사항은 무엇인가요?',20,'#000',400));
const cx=824,cy=369,cw=237,ch=152;for(let i=0;i<6;i++){n.push(L(cx,cy+i*ch/5,cw,0,'#d1d1d1'),tx(cx-41,cy-10+i*ch/5,35,20,`${50-i*10}%`,14,'#000',400,{align:'right'}));}n.push(L(cx,cy,0,ch,'#c8c8c8'));
[['복잡한 절차',35],['시스템 장벽',42],['어려운 협업',23]].forEach(([v,p],i)=>{const x=842+i*79,h=p/50*ch;n.push(R(x,cy+ch-h,43,h,C.slate),center(x-9,cy+ch-h-22,61,21,`${p}%`,14,C.slate,400),center(x-21,cy+ch+3,86,24,v,14,'#000',400));});
n.push(L(690,567,462,0,'#d0d0d0',1,{dash:'2 2'}),center(694,584,473,48,'“다수 임직원이 업무 처리 과정에서 어려움을 겪고 있으며\n복잡한 절차와 불편한 시스템이 생산성 저하의 주요 원인으로 지적됨”',16,'#000',400));slides.push(S('049-04',n));}
{
const n=[...base('벤치마킹 (타사 비교)','주요 경쟁사 대비 우리 회사의 운영 효율성 수준을 객관적으로 비교 분석')];
const x=80,y=219,cw=224; n.push(R(x+cw,y,cw*4,47,C.slate));n.push(R(x,y+47,cw,276,C.pale));n.push(P(x,y,cw,47,'M0 0L224 47','none','#bbb'));
for(let c=0;c<6;c++)n.push(L(x+c*cw,y,0,323,'#bdbdbd'));for(let r=0;r<6;r++)n.push(L(x,y+r*46.2,cw*5,0,'#bdbdbd'));n.push(L(x,y+323,1120,0,'#bdbdbd'));
['A사','B사','C사','미리컴퍼니'].forEach((v,i)=>n.push(center(x+cw*(i+1),y,cw,47,v,20,'#fff',700)));
['업무 처리 속도','운영비 비율','자동화율','1인당 생산성','최근 3년 추이'].forEach((v,i)=>n.push(center(x,y+47+i*46.2,cw,i===4?91:46.2,v,19,'#fff',700)));
[['3.2일','2.8일','3.5일','4.5일'],['22%','18%','25%','XX%'],['65%','78%','58%','52%'],['1억 2천만원','1억 5천만원','1억원','9천5백만']].forEach((row,i)=>row.forEach((v,j)=>n.push(center(x+cw*(j+1),y+47+i*46.2,cw,46.2,v,20,'#818181',400))));
for(let j=0;j<4;j++){const sx=303+j*224, by=514; n.push(L(sx+18,by,185,0,'#999'));for(let k=0;k<3;k++)n.push(L(sx+18+k*92,by-5,0,10,'#999'),center(sx+k*92,by+4,36,20,["’89","’90","’91"][k],13,'#818181',400));const start=[510,509,471,484][j],end=[470,474,493,490][j];n.push(L(sx,start,180,end-start,C.slate,7),P(sx+172,end-10,19,21,'M0 0L19 10.5L0 21Z',C.slate,'none'));}
n.push(tx(160,583,530,38,'우리 회사는 업무 처리 속도(4.5일)와 자동화율(52%)에서',24,'#000',400,{letterSpacing:-.65}),R(691,579,394,39,C.slate),center(695,579,386,39,'경쟁사 평균 대비 XX%p 낮은 수치이며,',24,'#fff',700),center(191,628,810,39,'선도 기업의 혁신 사례를 벤치마킹한 전사적 효율화 개선이 시급함',23.2,'#000',400));slides.push(S('049-05',n));}
{
const n=[...base('개선전략 overview','3대 핵심 전략과 5대 세부 실행과제를 통한 전사 운영 효율화 체계 구축'),R(80,213,547,58,C.slate),center(80,213,547,58,'전략 구조 다이어그램',24,'#fff',700),R(653,213,547,58,C.slate),center(653,213,547,58,'5대 실행 과제',24,'#fff',700),P(204,357,298,217,'M149 0L298 217H0Z','#d4e1ef','none')];
[[294,298,'업무\n프로세스\n혁신'],[144,496,'자원\n최적화'],[444,498,'협업체계\n개선']].forEach(([x,y,v])=>n.push(E(x,y,119,119,gradV,{border:C.slate,borderWidth:1.3}),center(x,y,119,119,v,21,'#fff',700,{lineHeight:1.05})));
n.push(center(280,442,148,91,'3대\n핵심 전략',30,'#000',800),R(560,410,34,44,grad),P(593,399,34,66,'M0 0L34 33L0 66Z','#dce3ec','none'),center(147,623,413,47,'“타사 벤치마킹 기반의 실행 가능 전략으로 2년내\n효율성 XX% 향상 및 연간 XX억원 비용 절감”',16,'#000',400));
['의사결정 구조 간소화로 처리 시간 XX% 단축','인력 재배치 및 예산 효율화를 통한 연간 XX억원 비용 절감','레거시 시스템 현대화 및 AI 기반 자동화 솔루션 도입','실시간 KPI 모니터링 및 데이터 기반 의사결정 체계 확립','이곳에 실행과제명과 구체적인 내용을 입력해 보세요.'].forEach((v,i)=>{let y=285+i*76;n.push(R(655,y+2,547,62,'#f3f3f3'),R(653,y,547,62,'#fff',{border:'#ddd'}),...num(678,y+11,i+1,40),tx(732,y+20,458,30,v,18,'#000',400,{letterSpacing:-.35}));});slides.push(S('049-06',n));}
{
const n=[...base('업무흐름 as-is / to-be','현재 업무 프로세스의 비효율을 제거하고 최적화된 흐름으로 재설계')];
['요청 접수','1차 검토','승인 대기','2차 승인','완료'].forEach((v,i)=>{const x=80+i*218.7,w=245;n.push(P(x,213,w,80,i===0?'M0 0H205L245 40L205 80H0Z':'M0 0H205L245 40L205 80H0L40 40Z','#000','none'),center(x+(i?31:0),213,w-(i?45:30),80,v,24,'#fff',700));});
const labelArrow=(y,v,fill,ink)=>[P(80,y,154,80,'M0 0H114L154 40L114 80H0Z',fill,'none'),heavy(81,y+21,133,40,v,27,ink,{align:'center',letterSpacing:0})];n.push(...labelArrow(348,'as-is',C.pale,'#818181'),...labelArrow(530,'to-be',C.slate,'#000'));
[['접수 및 배정\n(0.5일)',259,160,'#dbe4ed'],['실무 검토\n(1.5일)',426,274,'#c8d2dd'],['중복 승인 단계\n(2일)',706,327,'#97a1ad'],['최종처리\n(0.5일)',1040,160,'#97a1ad']].forEach(([v,x,w,fill])=>n.push(R(x,348,w,80,fill),center(x,348,w,80,v,20,'#fff',700)));
n.push(L(414,440,75,77,'#ddd',3),P(480,508,11,11,'M0 0L11 11L0 8Z','#ddd','none'),P(788,440,75,77,'M75 0L0 77','none','#ddd',{strokeWidth:3}),P(786,508,11,11,'M0 11L11 0L8 11Z','#ddd','none'),...pill(327,464,257,30,'이관 과정에서 평균 X일 절약'),...pill(704,464,257,30,'중복 승인 간소화로 1.5일 절약'));
[['유형별 자동 배정\n(0.2일)',259,160,C.pale],['통합 검토\n(0.8일)',426,187,'#b2bece'],['간소화된 승인\n(0.5일)',619,172,'#97a1ad'],['자동 완료\n(0.2일)',798,160,C.slate]].forEach(([v,x,w,fill])=>n.push(R(x,530,w,80,fill),center(x,530,w,80,v,22,'#fff',700)));
n.push(L(261,630,0,13,C.slate),L(261,643,351,0,C.slate),L(612,630,0,13,C.slate),L(620,630,0,13,C.slate),L(620,643,337,0,C.slate),L(957,630,0,13,C.slate),R(365,625,161,33,C.slate,{radius:20}),center(365,625,161,33,'이관시간 X% 단축',18,'#fff',700),R(712,625,160,33,C.slate,{radius:20}),center(712,625,160,33,'처리시간 X% 단축',18,'#fff',700));slides.push(S('049-07',n));}
{
const n=[...base('추진 로드맵','총 18개월에 걸쳐 단계적으로 전략을 실행하며, 주요 마일스톤별 점검 실시'),R(314,257,52,371,gradV),P(288,626,104,45,'M0 0H104L52 45Z',C.slate,'none')];
const rows=[['진단 및 설계 (3개월)','개선 전략 수립 및 상세 설계\n추진 계획서 작성 및 경영진 보고'],['시범 운영 (3개월)','파일럿 부서 선정 (1개 본부)\n시범 시스템 구축 및 테스트\n파일럿 운영 및 모니터링'],['전사 확대 (6개월)','1차 확대: 3개 본부 동시 적용\n2차 확대: 전 부서 순차 적용\n전사 교육 프로그램 운영'],['안정화 및 고도화 (6개월)','시스템 안정화 및 오류 해결\n프로세스 미세 조정 및 최적화\n성과 측정 및 ROI 분석']];
rows.forEach(([a,b],i)=>{const y=214+i*112;n.push(L(479,y+28,208,0,'#bdbdbd'),R(690,y-20,400,100,'#f1f1f1'),R(687,y-22,400,100,C.slate,{border:'#c4c9ce'}),E(681,y+22,12,12,C.pale,{border:'#fff',borderWidth:2}),R(201,y,278,56,'#fff',{border:C.slate,borderWidth:2}),center(201,y,278,56,a,22,'#000',700,{letterSpacing:-.5}),center(704,y-11,365,78,b,17,'#fff',600,{lineHeight:1.4}));});slides.push(S('049-08',n));}
export {slides};
