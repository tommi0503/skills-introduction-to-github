import {text,rect,ellipse,line,path,icon,placeholder,group,slide} from '../ui/scene.js';
const B='#3b4ca8',BG='#f2f2f2',K='#333333',G='#747e8e',P='#6e7dca',GRID='#cecece',PALE='#cdd2ee';
const T=(x,y,w,h,v,s=18,c=K,wt=400,e={})=>text(x,y,w,h,v,s,c,wt,{lineHeight:1.4,...e});
const C=(x,y,w,h,v,s=20,c=K,wt=400,e={})=>T(x,y,w,h,v,s,c,wt,{align:'center',verticalAlign:'middle',...e});
const R=(x,y,w,h,fill='#fff',border=K)=>rect(x,y,w,h,fill,border?{border}:{});
const para=(x,y,w,h,fill=B,slant=18)=>path(x,y,w,h,`M${slant} 0H${w}L${w-slant} ${h}H0Z`,fill,'none');
const tag=(x,y,w,label,size=24)=>[para(x,y,w,42,B,9),C(x+10,y,w-20,42,label,size,'#fff',700)];
const arrow=(x1,y1,x2,y2,c=K,w=1.7)=>{let a=Math.atan2(y2-y1,x2-x1),r=6;return [line(x1,y1,x2-x1,y2-y1,c,w),path(x2-7,y2-7,14,14,`M7 7L${7-r*Math.cos(a-.5)} ${7-r*Math.sin(a-.5)}M7 7L${7-r*Math.cos(a+.5)} ${7-r*Math.sin(a+.5)}`,'none',c,{strokeWidth:w})]};
const bullet=(x,y,w,value,s=18)=>[ellipse(x,y+9,7,7,K),T(x+18,y,w-18,120,value,s)];
const head=(n,title,sec)=>[rect(52,50,6,34,B),T(66,37,800,59,title,38,K,800,{letterSpacing:-1,font:'Noto Sans CJK KR'}),T(850,47,365,22,'MIRI COMPANY BUSINESS PROJECT',16,'#85858b',300,{align:'right'}),T(850,68,365,23,sec,16,B,500,{align:'right'}),line(52,101,1176,0,'#b8b8b8'),T(1185,662,38,26,String(n).padStart(2,'0'),18,'#c2c2c2',400,{align:'center'})];
const make=(n,title,sec,nodes)=>slide(`053-${String(n).padStart(2,'0')}`,[...head(n,title,sec),...nodes],{bg:BG});
const S1='01_기본개요',S2='02_해당 연도 사업 성과',S3='03_기업 전체 현황',S4='04_시장 비교 분석';
const details='이곳에 해당 항목의 상세 내용을 입력해 주세요.';
function bars(x,y,w,h,values,labels,{max=1000,color=P,colors=null,ticks=0,size=14,labelSize=14,barRatio=.63,axis=true,format=v=>v.toLocaleString()}={}){
 let a=[]; if(ticks)for(let i=0;i<=ticks;i++){let yy=y+h-h*i/ticks;a.push(line(x,yy,w,0,GRID,1),T(x-60,yy-10,52,22,format(max*i/ticks),size,K,400,{align:'right'}));}
 else for(let i=0;i<=4;i++)a.push(line(x,y+h-h*i/4,w,0,GRID,1));
 let step=w/values.length,bw=step*barRatio;values.forEach((v,i)=>{let xx=x+step*i+(step-bw)/2,hh=h*v/max;a.push(rect(xx,y+h-hh,bw,hh,colors?colors[i]:color),C(xx-15,y+h-hh-27,bw+30,25,format(v),size,colors?colors[i]:color),C(x+step*i,y+h+8,step,25,labels[i],labelSize,K));});return a;
}
function lineChart(x,y,w,h,series,labels,{max=3000,ticks=3,legendX=x+w/2-70,legendY=y+h+62,size=14}={}){
 let a=[];for(let i=0;i<=ticks;i++){let yy=y+h-h*i/ticks;a.push(line(x,yy,w,0,GRID,1),T(x-67,yy-10,58,22,(max*i/ticks).toLocaleString(),size,K,400,{align:'right'}));}
 const step=w/labels.length;labels.forEach((v,i)=>a.push(C(x+step*i,y+h+5,step,26,v,size)));
 series.forEach((s,k)=>{const points=s.values.map((v,i)=>[x+step*(i+.5),y+h-h*v/max]);points.forEach(([xx,yy],i)=>{if(i)a.push(line(points[i-1][0],points[i-1][1],xx-points[i-1][0],yy-points[i-1][1],s.color,.8));a.push(ellipse(xx-3.5,yy-3.5,7,7,s.color),C(xx-40,yy-30,80,24,s.values[i].toLocaleString(),size,s.color));});a.push(ellipse(legendX+k*79,legendY+4,14,14,s.color),T(legendX+17+k*79,legendY,70,25,s.name,size,K));});return a;
}
const slides=[];
// 01 Cover: ruled background and a native parallelogram.
{
 let a=[rect(0,0,1280,720,BG)];for(let y=5;y<720;y+=10)a.push(line(0,y,1280,0,'#e3e4e8',1));a.push(path(0,0,350,720,'M0 0H350L204 720H0Z',B,'none'),T(64,48,200,30,'2099.00.00.',16,'#fff'),T(900,47,315,26,'MIRI COMPANY',16,B,400,{align:'right'}),T(900,68,315,26,'20XX  BUSINESS PROJECT',16,K,400,{align:'right'}),line(1201,98,0,447,B,1.5),R(64,315,677,337,'#fff',B),line(65,403,674,0,'#ccc'),line(65,490,674,0,'#ccc'),T(110,326,600,78,'필요한 정보만',50,B,500,{letterSpacing:-1,font:'Noto Sans CJK KR'}),T(111,409,620,78,'심플하게 전달하는',50,B,500,{letterSpacing:-1,font:'Noto Sans CJK KR'}),T(107,495,628,156,'표 형식 보고서',100,K,800,{letterSpacing:-3,font:'Noto Sans CJK KR',lineHeight:1.3}),T(1000,561,215,32,'소속 / 소속입력',20,K,500,{align:'right'}),T(1000,594,215,32,'직급 / 이름입력',20,K,500,{align:'right'}),T(940,626,275,30,'기타 정보를 입력하세요.',19,K,400,{align:'right'}));slides.push(slide('053-01',a,{bg:BG}));
}
{
 let a=[path(0,0,406,720,'M0 0H406L262 720H0Z',B,'none'),T(111,116,200,75,'목차',56,'#fff',700),T(111,191,220,45,'CONTENTS',28,'#fff',500),T(900,47,315,26,'MIRI COMPANY',16,B,400,{align:'right'}),T(900,68,315,26,'2099  BUSINESS PROJECT',16,K,400,{align:'right'}),T(1185,662,38,26,'02',18,'#c2c2c2')];
 const rows=[['기본 개요','분석 배경 / 분석 목적 / 분석 방법 / 전체 개요 요약'],['해당 연도 사업 성과','분기별 진행 사업 / 매출 성과 / 목표대비 성과 / 사업별 성과 요약 / 역량 성과 / 성과 요인 분석'],['기업 전체 현황','시기별 추이 변화 / 전년 대비 매출 변화 / 월별 주요 변화 / 기업 성장 추이 / 주요 변곡점 분석'],['시장 비교 분석','환경 분석 / 경쟁사 비교 / 시장 포지션 분석 / 서비스 비교 / 마케팅 전략 / 분석 인사이트'],['결론','종합 평가 / 전략적 시사점 / 한계점 / 결론 요약'],['추후 방향','개선과제 및 방향성 / 다음 분기 목표']];rows.forEach(([title,note],i)=>{let y=114+i*94.5;a.push(R(444,y,75,60,'#fff',B),C(444,y-3,75,65,String(i+1).padStart(2,'0'),40,B,750),T(535,y-3,680,36,title,25,B,700),line(535,y+34,680,0,'#bbb'),T(535,y+39,700,30,note,17,'#82848a',400,{letterSpacing:-.3}));});slides.push(slide('053-02',a,{bg:BG}));
}
{
 let a=[R(137,210,472,172,'#fff',B),...tag(277,189,193,'핵심 배경'),T(169,250,410,126,'이곳에 이번 보고서의 목표와 관련된 배경의 핵심 요인 및 사례의 공통점 등의 내용을 요약해 적어보세요. 다음 목차에 이어질 내용에 기반하여 가장 중점적으로 봐야 할 핵심적인 내용을 적어보세요.',19,K,400,{lineHeight:1.37}),...bullet(145,413,465,'보고서의 분석 배경이 되는 사례 내용을 이곳에 간단하게 요약해 적어보세요. 관련 기사나 정확한 데이터에 기반한 인용구를 이용해 이곳에 적어보세요.',18),...bullet(145,513,465,'이곳에 우측에 설명 예시로 첨부한 이미지에 기반하여 배경과 연관된 사례를 간단하게 요약하여 작성해보세요. 이번 목표의 배경이 되는 여러 설득력 있는 사례를 요약하여 작성해주세요.',18),placeholder(654,179,488,414,{border:'#777'})];slides.push(make(3,'분석 배경',S1,a));
}
{
 let a=[para(115,191,413,402,B,80),C(200,307,230,47,'최종 목표',24,'#fff',700),C(197,365,246,95,'이곳에 보고서에서 다룰\n주요 목표를 한 두줄 이내로\n간단히 요약해 적어보세요.',21,'#fff'),...arrow(587,395,506,395),R(587,219,564,349)];for(let i=0;i<3;i++){let y=219+i*116;if(i)a.push(line(587,y,564,0,K));a.push(line(720,y+19,0,78,K,1.5),C(603,y+31,102,55,`키워드${i+1}`,23,B,700),T(744,y+33,382,70,'이곳에 선정한 키워드를 중점으로 최종 목적을 도출하기 위한 근거가 되는 내용의 상세를 입력해 주세요.',18));}slides.push(make(4,'분석 목적',S1,a));
}
{
 let a=[];[126,484,842].forEach((x,i)=>{a.push(R(x,209,312,382,'#fff',B),para(x+110,180,93,69,B,14),i===1?path(x+137,194,43,43,'M28 3H8Q4 3 4 7V35Q4 39 8 39H34Q39 39 39 34V18M13 28L15 19L32 2L40 10L22 28Z M27 7L35 15','none','#fff',{strokeWidth:3}):i===0?path(x+137,194,43,43,'M25 1A14 14 0 1 1 24.99 1M15 25L2 39','none','#fff',{strokeWidth:4}):icon(x+137,194,43,43,'lightbulb','#fff',{strokeWidth:2}),C(x+20,265,272,43,`단계별 방법${i+1}`,25,K,700),line(x+28,317,256,0,B,1.5),...bullet(x+29,351,257,'이곳에 앞으로 진행할 분석 단계에 대한 내용을 정리해주세요.',18),...bullet(x+29,426,257,'분석을 진행할 해당 방법 단계에 대한 설명을 적어주세요.',18),...bullet(x+29,500,257,'이곳에 해당 항목의 상세 내용을 입력해주세요.',18));if(i<2)a.push(...arrow(x+312,416,x+348,416));});slides.push(make(5,'분석 방법',S1,a));
}
{
 let a=[R(425,140,430,108,'#fff',B),C(440,157,400,42,'분석 대상',23,B,700),C(440,196,400,40,'이곳에 상세 내용을 입력해 주세요.',20),line(640,248,0,21,K,1.5)];[66,448,830].forEach((x,i)=>{a.push(R(x,269,383,141,BG,K),placeholder(x+1,270,113,139),T(x+127,281,240,42,['분석 배경','분석 목적','분석 방법'][i],23,K,650),line(x+128,323,239,0,K),T(x+127,342,245,63,'이곳에 상세 내용을 입력해 주세요.\n이곳에 상세 내용을 입력해 주세요.',18));});a.push(...arrow(640,410,640,460),para(276,472,716,186,B,37),C(327,491,611,49,'주요 내용 요약',25,'#fff',700),C(345,542,580,90,'이곳에 보고서에서 다룰 주요 내용을 간략히 요약해 주세요.\n가장 눈여겨보아야 할 수치를 제시해 주장을 강조해 주세요.\n분석 내용 요약과 함께 추후 개선 방향을 입력해 보세요.',21,'#fff'));slides.push(make(6,'전체 개요 요약',S1,a));
}
{
 let a=[];for(let i=0;i<4;i++){let x=66+i*287.25;a.push(R(x,154,287.25,49,'#fff','#7b84c1'),C(x,154,287.25,49,`${i+1}분기`,22,B,700));}for(let i=0;i<=12;i++){let x=66+i*95.75;a.push(line(x,203,0,437,i%3===0?'#8390c7':'#c4c4c4'));if(i<12)a.push(C(x,614,95.75,34,String(i+1),16,'#c3c3c3'));}[[74,233,464,85,1],[842,233,366,85,2],[266,363,464,85,3],[552,493,656,85,4]].forEach(([x,y,w,h,i])=>a.push(para(x,y,w,h,B,17),T(x+30,y+12,w-65,33,`진행 사업${i}`,22,'#fff',700),T(x+30,y+45,w-65,29,'이곳에 사업 내용을 간단히 입력해 주세요.',18,'#fff')));slides.push(make(7,'분기별 진행 사업',S2,a));
}
{
 let a=[];const vals=[[400,600,800,700],[200,300,700,900],[150,400,800,1000],[400,700,500,400]];[77,365,652,939].forEach((x,i)=>{a.push(R(x,170,263,444,'#fff',K),R(x,170,263,280,BG,B),...tag(x+51,149,161,`사업명${i+1}`),...bars(x+36,247,185,127,vals[i],['1분기','2분기','3분기','4분기'],{max:[800,1000,1100,800][i],size:14,labelSize:13,barRatio:.66}),C(x+20,405,223,35,'<분기별 매출>',16),...bullet(x+19,476,228,'해당 매출에 대한 주요 내용을 간단히 이곳에 적어보세요.',18),...bullet(x+19,543,228,'이곳에 해당 매출에 대한 내용을 요약해 입력해보세요.',18));});slides.push(make(8,'매출 성과',S2,a));
}
{
 let a=[...lineChart(164,253,566,280,[{name:'매출총액',color:B,values:[1200,1100,1700,2100]},{name:'목표매출',color:G,values:[1000,1300,1500,1800]}],['1분기','2분기','3분기','4분기'],{legendX:355,legendY:582}),R(792,237,378,304,'#fff',B),...tag(885,216,193,'성과 요약'),T(833,287,294,205,'이곳에 좌측 표에 관한 설명을 입력해 주세요. 이번 년도의 목표매출과 매출총액이 어떤 성과를 이루었고 어떤 점을 주의깊게 봐야 하는지 간단하게 요약하여 이곳에 적어주세요.\n\n추가로 설명해야 하는 내용이나 수치가 있다면 이곳에 적어주세요.',20,K,400,{lineHeight:1.3})];slides.push(make(9,'목표대비 성과',S2,a));
}
{
 let a=[T(64,169,520,42,'20XX년 사업별 성과',24,B,700),T(634,169,520,42,'성과 분석 요약',24,B,700),R(64,222,513,395,'#fff',B),R(64,222,513,41,B,null),C(64,222,124,41,'사업 항목',21,'#fff',700),C(188,222,389,41,'상세 내용',21,'#fff',700),line(188,222,0,395,'#8e98ca')];for(let i=0;i<4;i++){let y=263+i*88.5;a.push(C(64,y,124,88.5,`사업명${i+1}`,22,B,500),T(246,y+20,315,66,'이곳에 사업 성과 및 내용을 입력하세요.\n이곳에 사업 성과 및 내용을 입력하세요.',18));if(i)a.push(line(64,y,513,0,'#ccc'));}a.push(placeholder(634,222,291,165),placeholder(634,452,291,164),line(634,420,581,0,'#72768d'),...bullet(948,231,270,'성과 원인을 분석하고 성과별 공통 핵심 포인트를 찾아보세요.',18),...bullet(948,282,270,'표에 포함된 데이터를 기반으로 설명하세요.',18),...bullet(948,332,270,'숫자나 비율을 활용하여 신뢰성을 높여보세요.',18),...bullet(948,461,270,'성과가 미친 긍정적인 영향을 설명하세요.',18),...bullet(948,512,270,'표에 포함된 데이터를 기반으로 설명하세요.',18),...bullet(948,562,270,'해당 성과가 목표에 어떻게 기여했는지 설명해보세요.',18));slides.push(make(10,'사업별 성과 요약',S2,a));
}
{
 let a=[R(134,189,377,407,BG,K),R(134,189,377,175,'#fff',B),...tag(226,173,193,'핵심 성과'),T(168,233,309,110,'이곳에 우측 표 데이터에 기반한 핵심적인 포인트를 간단히 요약해 적어보세요. 가장 성과가 좋았던 역량에 대해 설명해 보세요.',20),...bullet(168,392,312,'이곳에 우측 표에 기반하여 주목해야 할 포인트에 대해 상세히 적어보세요.',18),...bullet(168,468,316,'이곳에 우측 표에 기반하여 주목해야 할 포인트에 대해 상세히 적어보세요. 가장 좋은 성과와 저조한 성과에 대해 분석한 내용을 요약해보세요.',18)];let cx=883,cy=410,r=225;let points=[];for(let i=0;i<5;i++){let ang=(-90+i*72)*Math.PI/180;points.push([cx+Math.cos(ang)*r,cy+Math.sin(ang)*r]);}for(let step=1;step<=4;step++){let p=points.map(([x,y])=>[cx+(x-cx)*step/4,cy+(y-cy)*step/4]);a.push(path(0,0,1280,720,'M'+p.map(v=>v.join(' ')).join('L')+'Z','none','#c1c1c1'));}points.forEach(([x,y])=>a.push(line(cx,cy,x-cx,y-cy,'#c1c1c1')));let rates=[.48,.48,.74,.48,.74];let p=points.map(([x,y],i)=>[cx+(x-cx)*rates[i],cy+(y-cy)*rates[i]]);a.push(path(0,0,1280,720,'M'+p.map(v=>v.join(' ')).join('L')+'Z','none',B,{strokeWidth:2.5}));p.forEach(([x,y])=>a.push(ellipse(x-4.5,y-4.5,9,9,B)));a.push(C(804,150,158,37,'역량 및 기술2',17,K,600),T(1108,328,155,33,'역량 및 기술3',17,K,600),C(956,591,150,33,'역량 및 기술4',17,K,600),C(680,591,150,33,'역량 및 기술5',17,K,600),T(573,328,150,33,'역량 및 기술1',17,K,600));slides.push(make(11,'역량 성과',S2,a));
}
{
 let a=[para(332,156,616,136,B,27),C(373,168,535,42,'핵심 요인',24,'#fff',700),C(390,214,500,62,'이곳에 이번 년도 사업 성과의 핵심 요인을 총 정리하여 간단히\n보기 쉽게 한 두줄로 요약하여 작성해보세요.',20,'#fff'),line(301,336,678,0,K,1.7),...arrow(640,363,640,301)];[146,485,823].forEach((x,i)=>{a.push(line(x+155,336,0,27,K,1.7),R(x,363,310,251,BG,K),R(x,363,310,51,'#fff',K),C(x,363,310,51,['마케팅','기술','전략'][i],25,B,700),...bullet(x+28,438,260,'이곳에 해당 항목의 상세 내용을 입력해 주세요.',19),...bullet(x+28,514,260,`이곳에 성과 요인에 기여한 ${['마케팅적인','기술적인','전략적인'][i]} 부분을 요약하여 간단하게 입력해보세요.`,19));});slides.push(make(12,'성과 요인 분석',S2,a));
}
{
 let a=[R(180,179,920,128,'#fff',B),...tag(543,158,194,'표 내용 요약'),C(216,217,850,63,'이곳에 아래 표에 관한 간단한 설명을 입력하세요.\n추가로 설명해야 하는 내용이나 수치가 있다면 요약 문장 아래 적어주세요.',20),T(920,315,180,26,'(단위: 만 원)',16,'#81848a',400,{align:'right'})];let x=242,y=356,w=848,h=206;for(let i=0;i<=4;i++){let yy=y+h-h*i/4;a.push(line(x,yy,w,0,GRID),T(x-64,yy-10,57,25,(i*5000).toLocaleString(),14,K,400,{align:'right'}));}const values=[[2304,3234,1432,2312],[5232,6343,2453,3323],[11343,1232,7342,5342],[15343,2123,10232,8321]],colors=[K,P,G,B];values.forEach((vs,i)=>{vs.forEach((v,j)=>{let xx=x+12+i*212+j*49.5,hh=v/20000*h;a.push(rect(xx,y+h-hh,40,hh,colors[j]),C(xx-10,y+h-hh-25,60,24,v.toLocaleString(),14,colors[j]));});a.push(C(x+i*212,y+h+4,212,28,`${2089+i}년`,14));});['매출액','매입액','매출이익','손익'].forEach((v,i)=>a.push(rect(522+i*65,611,14,14,colors[i],{radius:3}),T(539+i*65,607,75,26,v,14)));slides.push(make(13,'시기별 추이 변화',S3,a));
}
{
 let a=[R(193,154,894,364,BG,K),...lineChart(322,243,686,182,[{name:'2098년',color:B,values:[1200,1100,1700,2100]},{name:'2099년',color:G,values:[2200,1700,2000,2700]}],['1분기','2분기','3분기','4분기'],{legendX:564,legendY:196,size:16})];[192,703].forEach((x,i)=>a.push(R(x,549,384,106,'#fff',B),para(x+101,535,182,34,B,7),C(x+108,535,168,34,`${2098+i} 총 매출액`,22,'#fff',700),C(x+20,575,344,64,'0,000,000원',40,K,600)));a.push(T(595,569,140,31,'(00% 상승)',20,B,600),...arrow(576,599,695,599,B));slides.push(make(14,'전년 대비 매출 변화',S3,a));
}
{
 let a=[...bars(122,265,1078,294,[300,430,860,670,500,600,570,670,800,700,600,630],Array.from({length:12},(_,i)=>`${i+1}월`),{max:1000,color:B,ticks:5,barRatio:.66,size:14,labelSize:14}),...arrow(442,204,340,204),...arrow(340,204,340,262),R(442,140,461,128,'#fff',B),T(470,158,405,35,'주요 핵심 추이',23,B,600),line(465,194,415,0,B),T(471,204,405,49,'이곳에 전체 12개월 데이터 중 가장 성과가 좋거나, 주요하게 봐야 할 데이터에 대한 내용을 간단히 입력해보세요.',17),C(280,604,720,44,'20XX년 월별 고객 유치 추이',24,B,700)];slides.push(make(15,'월별 주요 변화',S3,a));
}
{
 let a=[];for(let i=0;i<=4;i++)a.push(line(109,207+i*61,1054,0,GRID));const points=[[240,390],[503,329],[767,237],[1030,268]];a.push(path(0,0,1280,720,'M240 451L240 390L503 329L767 237L1030 268L1030 451Z',B,'none',{opacity:.3}),path(0,0,1280,720,'M240 390L503 329L767 237L1030 268','none',B,{strokeWidth:.7}));points.forEach(([x,y],i)=>a.push(line(x,y,0,462-y,B,1.5,{dash:'2 4'}),ellipse(x-4,y-4,8,8,B),C(x-45,y-30,90,26,[2000,4000,7000,6000][i].toLocaleString(),18,B)));
 [100,370,640,910].forEach((x,i)=>a.push(R(x,463,269,167,BG,K),C(x+10,471,249,43,`${2096+i} 주요 성과`,23,B,600),line(x+20,515,229,0,K),T(x+20,534,229,80,'이곳에 해당 년도의 성장에 관한 주요 성과를 간단히 요약해 입력해보세요.',18)));slides.push(make(16,'기업 성장 추이',S3,a));
}
{
 let a=[];for(let i=0;i<=4;i++)a.push(line(136,210+i*85.5,522,0,GRID));a.push(path(0,0,1280,720,'M267 552V253L527 423V552Z',B,'none',{opacity:.3}),line(267,253,260,170,B,.7),line(267,253,0,299,B,1.5,{dash:'2 4'}),line(535,423,0,129,B,1.5,{dash:'2 4'}),ellipse(262,248,10,10,B),ellipse(522,418,10,10,B),C(217,216,100,31,'7,000',20,B),C(485,385,100,31,'6,000',20,B),C(211,558,112,36,'2098',18),C(479,558,112,36,'2099',18),...arrow(751,250,291,250),...arrow(751,426,554,426));[204,393].forEach((y,i)=>a.push(R(751,y,413,168,i?'#f2f2f2':'#fff',K),T(775,y+19,364,36,['주요 고점 분석','주요 저점 분석'][i],23,B,600),line(776,y+60,362,0,K,1.5),T(776,y+74,364,83,'이곳에 해당 항목의 상세 내용을 입력해 주세요. 이곳에 해당 수치에서 중요하게 봐야할 부분에 대해 상세히 정리하여 적어보세요.',18)));slides.push(make(17,'주요 변곡점 분석',S3,a));
}
{
 let a=[];const xs=[114,377,640,903],heads=['정치 (Political)','경제 (Economic)','사회 (Social)','기술 (Technological)'];xs.forEach((x,i)=>{a.push(R(x,196,263,399,BG,K),R(x,196,263,71,'#fff',B),para(x+101,175,61,42,B,9),C(x+105,175,51,42,'PEST'[i],25,'#fff',700),C(x+9,216,245,45,heads[i],23,B,700),...bullet(x+18,295,231,'이곳에 PEST 분석에 알맞는 분석 내용과 그로 인해 도출한 경영 전략을 상세하게 정리해 적어보세요.',18),...bullet(x+18,408,231,'이곳에 해당 항목에 알맞는 분석을 상세하게 정리해 기록해 주세요.',18),...bullet(x+18,497,231,'이곳에 해당 항목에 들어갈 수 있는 상세 내용을 분석해 입력해 주세요.',18));});slides.push(make(18,'환경 분석',S4,a));
}
{
 let a=[R(66,167,1149,450,'#fff',B),rect(66,167,156,450,B),rect(222,167,993,55,PALE),rect(66,167,156,55,P),line(66,167,156,55,'#fff')];const heights=[55,52,46,69,49,90,89],labels=['','설립연도','사업분야','서비스/제품','주고객층','강점','한계점'];let y=167;for(let r=0;r<heights.length;r++){let h=heights[r];if(r)a.push(line(66,y,1149,0,'#ccc'));a.push(C(67,y,154,h,labels[r],22,'#fff',500));for(let c=0;c<4;c++){let x=222+c*248.25;a.push(line(x,167,0,450,'#8590c5'));let val=r===0?`경쟁사${c+1}`:['','20XX년','분야 입력','서비스/제품 입력','XX~XX대','이곳에 해당 경쟁사의\n강점을 입력해보세요.','이곳에 해당 경쟁사의\n한계점을 입력해보세요.'][r];a.push(C(x+8,y+1,232,h-2,val,r===0?23:19,r===0?B:K,r===0?700:400));}y+=h;}slides.push(make(19,'경쟁사 비교',S4,a));
}
{
 let a=[R(104,150,613,503,BG,K),line(410,188,0,423,'#b5b5b5'),line(126,401,569,0,'#b5b5b5'),C(367,159,87,31,'특성A',17,G),C(367,614,87,31,'특성B',17,G),T(133,374,90,27,'유형A',17,G),T(630,374,64,27,'유형B',17,G),...arrow(749,299,550,299),...arrow(749,500,359,500),rect(749,197,427,201,B),para(852,220,221,37,'#fff',8),C(860,219,205,39,'현재 포지션 분석',22,B,650),T(782,278,362,81,'이곳에 우측 표 데이터에 기반한 핵심적인 포인트를 간단히 요약해 적어보세요. 가장 성과가 좋았던 역량에 대해 설명해보세요.',20,'#fff'),R(749,437,427,160,'#fff',B),C(779,454,365,44,'주요 경쟁사 포지션 분석',23,B,650),line(784,500,357,0,B,1.3),T(782,521,362,62,'회사와 비교군이 되는 주요 경쟁사의 포지션을 분석한 내용을 간단히 정리하여 이곳에 작성해보세요.',18)];[[527,299,'회사명',B],[269,333,'경쟁사1',G],[339,500,'경쟁사2',G],[228,553,'경쟁사3',G],[594,587,'경쟁사4',G]].forEach(([x,y,v,c])=>a.push(ellipse(x-10,y-10,20,20,c),C(x-70,y-45,140,30,v,21,v==='회사명'?B:K,600)));slides.push(make(20,'시장 포지션 분석',S4,a));
}
{
 let a=[...tag(508,147,265,'서비스 비교 분석'),R(184,215,912,398,'#fff',B)];const xs=[184,543,730],ws=[359,187,366],heights=[55,86,86,86,85];let y=215;const content=[['A서비스','기준','B서비스'],['기능1, 기능2, 기능3','주요 기능','기능1, 기능2, 기능3'],['월 평균 100만명','사용자 수','월 평균 80만명'],['웹, 모바일, 데스크탑','지원 형식','웹, 모바일'],['리뷰를 입력하세요.\n리뷰를 입력하세요.','리뷰','리뷰를 입력하세요.\n리뷰를 입력하세요.']];heights.forEach((h,r)=>{for(let c=0;c<3;c++){a.push(rect(xs[c],y,ws[c],h,c===1?B:r===0?PALE:'#fff'));if(c)a.push(line(xs[c],y,0,h,'#aaaecb'));a.push(C(xs[c]+12,y+1,ws[c]-24,h-2,content[r][c],r===0?23:21,c===1?'#fff':r===0?B:K,r===0||c===1?650:400));}if(r)a.push(line(184,y,912,0,'#ccc'));y+=h;});a.push(R(184,215,912,398,'transparent',B));slides.push(make(21,'서비스 비교 분석',S4,a));
}
export { slides };
