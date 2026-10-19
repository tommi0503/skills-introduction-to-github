import {T,R,C,L,P,I,Path,Chip} from '../primitives.mjs';

// Native 1280 × 720 layout.  Shared frame, cards, headings and diagrams are
// composed from editable vector/text primitives; photographic seats are empty.
const K={bg:'#f9f9f9',paper:'#ffffff',outer:'#eeeeee',blue:'#add9ee',pale:'#e4f7fe',yellow:'#ffffa9',soft:'#fffcc6',pink:'#fbe1df',mint:'#d4f0e8',hi:'#f2f96b',ink:'#000000',gray:'#f9f9f9'};
const tx=(x,y,w,h,text,size=20,extra={})=>T(x,y,w,h,text,size,{font:'Pretendard',color:K.ink,weight:400,lineHeight:1.45,letterSpacing:-0.65,...extra});
const ct=(x,y,w,h,text,size=20,extra={})=>tx(x,y,w,h,text,size,{align:'center',valign:'middle',...extra});
const box=(x,y,w,h,fill=K.gray,extra={})=>R(x,y,w,h,fill,{stroke:'#000',strokeWidth:1.15,...extra});
const line=(x,y,x2,y2,color='#000',width=1.15,extra={})=>L(x,y,x2,y2,color,width,extra);
const screw=(x)=>[C(x,56,22,22,'#f9f9f9',{stroke:'#000',strokeWidth:1.3}),line(x+1,67,x+21,67,'#000',2.3)];
function frame(header='MONTHLY REVIEW'){return [R(43,40,1200,647,'#000'),box(40,37,1200,647,K.outer),box(40,37,1200,60,K.blue),box(74,71,1132,579,K.paper),box(417,37,446,60,K.blue),...screw(436),...screw(821),ct(468,53,343,31,header,19,{font:'Inter',weight:700,letterSpacing:0.3,el:'tag'})];}
const hi=(x,y,w,h=43)=>Path(x,y,w,h,`M${Math.min(16,w*.08)} 0 H${w} L${w-Math.min(16,w*.08)} ${h} H0 Z`,{fill:K.hi,viewBox:`0 0 ${w} ${h}`,el:'tag'});
function title(text,{x=140,y=151,w=1000,markX,markW,center=false,size=48}={}){return [...(markX!==undefined?[hi(markX,y+11,markW)]:[]),tx(x,y,w,64,text,size,{weight:500,align:center?'center':'left',lineHeight:1.15,letterSpacing:-0.3,el:'tag'})];}
function sideTitle(a,b,note){return [...(a?title(a,{w:270}):[]),...(b?[hi(128,215,b.length*42+32),tx(140,207,270,59,b,48,{weight:500,lineHeight:1.13,letterSpacing:-.3})]:[]),...(note?[tx(140,note.split('\n').length<3?542:521,195,65,note,14,{color:'#999',lineHeight:1.5,letterSpacing:-.3})]:[])];}
function arrow(x,y,dir='r',s=19){const d={r:'M0 27 H52 V0 L100 50 L52 100 V73 H0 Z',l:'M100 27 H48 V0 L0 50 L48 100 V73 H100 Z',d:'M27 0 H73 V52 H100 L50 100 L0 52 H27 Z',u:'M27 100 H73 V48 H100 L50 0 L0 48 H27 Z'}[dir];return Path(x,y,s,s,d,{fill:'#000',el:'steps'});}
const bullets=(x,y,w,items,size=20,lh=31)=>items.flatMap((text,i)=>[C(x,y+i*lh+11,7,7,'#000'),tx(x+20,y+i*lh,w-20,lh,text,size,{lineHeight:1.35})]);
const sketch=(x,y,w,h,d,extra={})=>Path(x,y,w,h,d,{viewBox:'0 0 72 72',fill:'none',stroke:'#000',strokeWidth:2.3,...extra});
function stageIcon(x,y,index){
 if(index===0)return [sketch(x,y,69,69,'M15 2 H54 L68 16 V68 H2 V15 Z M15 2 V15 H2 M54 2 V16 H68 M10 22 H37 M10 29 H31 M10 36 H25 M10 43 H19 M39 58 H58 M32 65 H58 M48 51 H58 M53 43 H58 M52 20 L60 28 L22 64 L11 67 L14 55 Z M17 55 L24 62 M47 25 L54 32 M56 16 L64 24'),];
 if(index===1)return [sketch(x,y,69,69,'M4 9 H68 V60 H4 Z M13 37 V31 M20 37 V24 M27 37 V28 M42 29 H57 V45 M35 28 C35 25 36 25 39 25 H50 C54 25 57 27 57 31 V49 M42 32 V43 M43 20 A4 4 0 1 0 43 12 A4 4 0 1 0 43 20 M15 56 A4 4 0 1 0 15 48 A4 4 0 1 0 15 56 M36 56 A4 4 0 1 0 36 48 A4 4 0 1 0 36 56 M57 56 A4 4 0 1 0 57 48 A4 4 0 1 0 57 56 M5 70 V66 Q5 60 15 60 Q25 60 25 66 V70 Z M26 70 V66 Q26 60 36 60 Q46 60 46 66 V70 Z M47 70 V66 Q47 60 57 60 Q67 60 67 66 V70 Z')];
 const nodes=[[36,3],[7,19],[65,19],[7,53],[65,53],[36,69]];return [sketch(x,y,69,69,'M36 18 V27 M15 23 L27 31 M57 23 L45 31 M15 49 L27 41 M57 49 L45 41 M36 46 V57 M23 29 L36 22 L49 29 V43 L36 50 L23 43 Z'),...nodes.flatMap(([cx,cy])=>[C(x+(cx-8.5)*69/72,y+(cy-8.5)*69/72,17*69/72,17*69/72,'#ffffa9',{stroke:'#000',strokeWidth:1.8}),C(x+(cx-2.2)*69/72,y+(cy-5)*69/72,4.4*69/72,4.4*69/72,'none',{stroke:'#000',strokeWidth:1.3}),Path(x+(cx-4)*69/72,y+(cy+.5)*69/72,8*69/72,5*69/72,'M0 5 V3 Q0 0 4 0 Q8 0 8 3 V5 Z',{viewBox:'0 0 8 5',fill:'none',stroke:'#000',strokeWidth:1.2})]),C(x+33*69/72,y+31*69/72,6*69/72,6*69/72,'none',{stroke:'#000',strokeWidth:1.7}),sketch(x,y,69,69,'M31 44 V41 Q31 37 36 37 Q41 37 41 41 V44')];
}
const slide=(n,title,elements)=>({id:`slide_${String(n).padStart(2,'0')}`,title,background:K.bg,elements:[...frame(n===30?'MIRI COMPANY':undefined),...elements]});
const pill=(x,y,w,h,text,fill=K.soft,size=21)=>[box(x,y,w,h,fill,{radius:h/2,el:'pill'}),ct(x,y-1,w,h+2,text,size,{weight:700,el:'pill'})];
function device(x,y,w=184,h=385){return [
 P(x-32,y+h-7,w+64,51,'',{clipPath:'polygon(8% 0, 94% 0, 100% 35%, 100% 100%, 0 100%, 1% 36%)',el:'image-frame'}),
 R(x,y,w,h,'#101010',{radius:26,stroke:'#777777',strokeWidth:1.7,el:'image-frame'}),
 P(x+6,y+6,w-12,h-12,'',{radius:20,el:'image-frame'}),
 R(x+68,y+10,49,14,'#000',{radius:7}),R(x-1,y+68,2,15,'#222'),R(x-2,y+94,3,25,'#222'),R(x-2,y+124,3,25,'#222'),R(x+w-1,y+106,2,34,'#222')
];}
const slides=[];

slides.push(slide(8,'사업설명',[
 ...title('사업설명',{x:0,w:1280,center:true,markX:542,markW:195}),
 ...[{x:140,name:'주요 특징',fill:K.pale,note:'시선은 왼쪽에서 오른쪽으로 이동합니다. 정보를 가\n로로 배치하여 내용을 편안하게 읽을 수 있습니다.'},{x:649,name:'핵심 역량',fill:K.soft,note:'핵심 내용을 가로로 나란히 배치하여 복잡한 정보를\n한눈에 비교할 수 있도록 정리해 보세요.'}].flatMap(c=>[box(c.x,255,490,328,K.gray,{el:'card'}),box(c.x,255,490,56,c.fill),ct(c.x,263,490,41,c.name,25,{weight:700}),P(c.x+17,326,456,148,'',{el:'image-frame'}),ct(c.x+29,492,432,66,c.note,20,{lineHeight:1.5})])
]));
slides.push(slide(9,'사업구조',[
 ...sideTitle('','', '우선순위에 따라 위에서 아래로\n배치해보세요.'),hi(128,162,194),tx(140,151,220,60,'사업구조',48,{weight:500,letterSpacing:-.3,lineHeight:1.15}),
 ...[{y:161,name:'핵심과제',en:'KEY TASKS',fill:K.pale,items:['키워드 옆에 디테일한 설명을 더해요.','텍스트만으로 읽는 이를 설득해 보세요.']},{y:305,name:'체크리스트',en:'CHECKLIST',fill:K.yellow,items:['단락을 나누면 줄글 보다 읽기 편해요.','세로 배열은 단계별 설명에 좋아요.','문단마다 번호를 매겨 순서를 잡아요.']},{y:451,name:'우선순위',en:'TOP PRIORITY',fill:K.pink,items:['배열의 논리적인 순서를 보여주세요.','여백을 주어 읽는 이가 숨 쉴 틈을 줘요.']}].flatMap(c=>[box(418,c.y,721,131,K.gray,{el:'list'}),box(418,c.y,221,131,c.fill),ct(432,c.y+30,193,38,c.name,25,{weight:700}),ct(432,c.y+72,193,22,c.en,16,{font:'Inter',weight:700,letterSpacing:0}),...bullets(680,c.y+(c.items.length===3?20:34),427,c.items,20,31)])
]));
slides.push(slide(10,'프로세스 예시',[
 ...sideTitle('프로세스','예시','단계별 과정을 순서대로 보여줘\n이해를 돕습니다.'),
 ...pill(477,160,661,41,'기획',K.gray,25),arrow(798,208,'d',18),...pill(477,233,661,41,'실행',K.yellow,25),
 ...[{x:477,fill:K.gray,title:'해결책 1',list:['이슈에 대한 원인을','분석하고 해결하기 위한','방법들을 적어보세요.','고객 피드백 적극 수용','예산 재설정 후 모니터링']},{x:700,fill:K.soft,title:'해결책 2',list:['이슈에 대한 원인을','분석하고 해결하기 위한','방법들을 적어보세요.','성과 좋은 채널에 집중','브랜드 가이드 라인 작성']},{x:924,fill:K.gray,title:'해결책 3',list:['이슈에 대한 원인을','분석하고 해결하기 위한','방법들을 적어보세요.','문제점, 이슈에 대한','해결책을 작성해주세요.']}].flatMap(c=>[box(c.x,287,214,214,c.fill,{el:'card'}),ct(c.x,302,214,35,c.title,25,{weight:700}),...bullets(c.x+18,348,185,c.list,16,26)]),
 arrow(798,511,'d',18),...pill(477,542,661,41,'완료',K.pale,25)
]));
slides.push(slide(11,'운영 전체흐름',[
 ...title('운영 전체흐름',{x:0,w:1280,center:true,markX:594,markW:185}),
 ...[{x:140,y:255,name:'노출',note:'전체 흐름을 한눈에\n파악할 수 있는 도표입니다.'},{x:487,y:255,name:'유입',note:'단계별 과정을 순서대로\n보여줘 이해를 돕습니다.'},{x:836,y:255,name:'활동',note:'복잡한 절차를 단순화하여\n명쾌하게 정리했어요.'},{x:140,y:442,name:'추천',note:'수행해야 할 핵심 키워드를\n요약해 보여주세요.',on:true},{x:487,y:442,name:'재구매',note:'각 단계 사이의 관계와\n변화를 설명하기 좋아요.'},{x:836,y:442,name:'전환',note:'프로젝트 진행 상황과\n미래 방향을 제시합니다.'}].flatMap(c=>[box(c.x,c.y,304,141,c.on?K.yellow:K.gray,{el:'cycle'}),...pill(c.x+87,c.y+19,130,34,c.name,c.on?K.gray:K.soft,22),ct(c.x+20,c.y+59,264,61,c.note,20,{lineHeight:1.4})]),
 arrow(456,316),arrow(805,316),arrow(979,410,'d'),arrow(805,503,'l'),arrow(456,503,'l'),arrow(282,410,'u')
]));
slides.push(slide(12,'업무 단계정리',[
 ...title('업무 단계정리',{x:0,w:1280,center:true,markX:594,markW:186}),
 ...[{x:164,name:'가설 설정',icon:'FilePenLine',note:'전체 흐름을 한눈에 파악할\n수 있는 도표입니다.'},{x:511,name:'시장 검증',icon:'Presentation',note:'단계별 과정을 순서대로 보여줘\n이해를 돕습니다.'},{x:859,name:'정식 런칭',icon:'Network',note:'프로젝트 진행 상황과\n미래 방향을 제시합니다.'}].flatMap((c,i)=>[C(c.x,255,257,257,i===2?K.yellow:K.gray,{stroke:'#000',strokeWidth:1.5,el:'steps'}),ct(c.x+35,288,187,30,`STEP 0${i+1}`,17,{font:'Inter',weight:700,letterSpacing:0}),ct(c.x+15,325,227,37,c.name,25,{weight:700}),...stageIcon(c.x+94,384,i),ct(c.x-18,532,293,60,c.note,20,{lineHeight:1.4})]),arrow(456,372),arrow(803,372)
]));
slides.push(slide(13,'이슈정리',[
 ...title('이슈정리',{x:0,w:1280,center:true,markX:547,markW:186}),
 ct(140,239,490,40,'|  프로젝트 우선순위  |',25,{weight:700}),ct(648,239,490,40,'|  핵심과제  |',25,{weight:700}),
 ...[{name:'순위 1',items:['중요 정보는 맨 위로 배치하세요.','키워드 옆에 디테일한 설명을 더해요.']},{name:'순위 2',items:['텍스트만으로 읽는 이를 설득해 보세요.','박스 크기를 일정하게 맞춰 정돈해요.']},{name:'순위 3',items:['배열의 논리적인 순서를 보여주세요.','여백을 주어 읽는 이가 숨 쉴 틈을 줘요.']}].flatMap((c,i)=>[box(140,296+i*99,490,89,K.gray,{el:'list'}),ct(161,313+i*99,103,56,c.name,23,{weight:700}),...bullets(289,310+i*99,329,c.items,20,31)]),
 ...[{name:'과제 1',items:['단락을 나누면 줄글 보다 읽기 편해요.','세로 배열은 단계별 설명에 좋아요.']},{name:'과제 2',items:['시선이 위에서 아래로 이동합니다.','문단마다 번호를 매겨 순서를 잡아요.']},{name:'과제 3',items:['핵심 메시지로 시선을 사로잡으세요.','우측 공간을 활용해 보세요.']}].flatMap((c,i)=>[box(648,296+i*99,490,89,K.yellow,{el:'list'}),ct(669,313+i*99,110,56,c.name,23,{weight:700}),...bullets(796,310+i*99,330,c.items,20,31)])
]));
slides.push(slide(14,'이슈대응 흐름',[
 ...sideTitle('이슈대응','흐름','단계별 과정을 순서대로 보여줘\n이해를 돕습니다.'),
 ...[{name:'프로젝트 착수',note:'전체 흐름을 한눈에 파악할 수 있는 도표입니다.'},{name:'기획 및 분석',note:'복잡한 절차를 단순화하여 명쾌하게 정리했어요.'},{name:'설계',note:'각 단계 사이의 관계와 변화를 설명하기 좋아요.'},{name:'구현',note:'목표 달성을 위한 논리적인 순서를 증명합니다.'},{name:'프로젝트 종료',note:'시작부터 종료까지의 전체 여정을 시각화해요.'}].flatMap((c,i)=>[box(430,161+i*89,710,67,K.gray,{el:'steps'}),box(430,161+i*89,260,67,i===4?K.yellow:K.pale),ct(444,176+i*89,38,37,`0${i+1}`,17,{font:'Inter',weight:700,letterSpacing:0}),ct(483,171+i*89,188,46,c.name,25,{weight:700}),ct(710,174+i*89,410,41,c.note,20)])
]));
function lineChart(x,y,w,h,values,labels,{area=false,boldLabels=false}={}){
 const e=[];const y0=y+h;const xs=values.map((_,i)=>x+(i+.5)*w/values.length);const ys=values.map(v=>y0-h*v/80);
 if(area)e.push(Path(x,y,w,h,`M ${xs[0]-x} ${h} ${values.map((v,i)=>`L ${xs[i]-x} ${ys[i]-y}`).join(' ')} L ${xs.at(-1)-x} ${h} Z`,{viewBox:`0 0 ${w} ${h}`,fill:'#e2eff4',el:'chart-line'}));
 for(let v=0;v<=80;v+=20){const py=y0-v/80*h;e.push(line(x,py,x+w,py,'#c8c8c8',1),tx(x-47,py-13,39,26,`${v}%`,17,{align:'right',letterSpacing:0,lineHeight:1.4}));}
 e.push(line(x,y,x,y0,'#ccc',1));
 values.forEach((v,i)=>{if(i)e.push(line(xs[i-1],ys[i-1],xs[i],ys[i],'#111',.75));e.push(C(xs[i]-5,ys[i]-5,10,10,'#000'),ct(xs[i]-37,y0+4,74,26,labels[i],17,{weight:boldLabels?700:400,letterSpacing:-.3}));if(area)e.push(ct(xs[i]-30,ys[i]-34,60,25,`${v}%`,17,{letterSpacing:0}));});return e;
}
slides.push(slide(15,'성과 추이예시',[
 ...title('성과 추이예시',{x:0,w:1280,center:true,markX:594,markW:186}),
 box(140,255,490,328,K.gray,{el:'chart-line'}),box(649,255,490,328,K.soft,{el:'chart-line'}),ct(140,273,490,41,'|  최근 5년 주가 변동  |',25,{weight:700}),ct(649,273,490,41,'|  분기별  |',25,{weight:700}),ct(140,318,490,34,'미래를 예측하기 좋아요.',20),ct(649,318,490,34,'변화의 흐름을 한눈에 봐요.',20),
 ...lineChart(232,394,347,127,[10,30,50,60,80],['2030','2031','2032','2033','2034'],{area:true,boldLabels:true}),...lineChart(741,365,347,157,[60,40,80],['1분기','2분기','3분기'])
]));
slides.push(slide(16,'일정개요',[
 ...title('일정개요',{x:0,w:1280,center:true,markX:547,markW:186}),line(231,281,1049,281),
 ...[{name:'법인 설립',icon:'Building2',note:'세부 계획을 세워\n일정을 빈틈없이\n관리하세요.'},{name:'서비스 출시',icon:'Target',note:'걸어온 길을 이야\n기하듯 자연스럽\n게 풀어내세요.'},{name:'특허 등록',icon:'FileBadge',note:'막대를 배치하고\n전체 일정의 흐름\n을 보세요.'},{name:'투자 유치',icon:'Handshake',note:'연도별 제목을 굵\n게 강조해 가독성\n을 높여보세요.'},{name:'시장 차지',icon:'Trophy',note:'아이콘으로 통일\n하고 사진을 넣어\n꾸며보세요.'}].flatMap((c,i)=>{const x=140+i*204.5;return [C(x+72,261,38,38,i%2?K.pale:K.soft,{stroke:'#000',strokeWidth:1.2}),ct(x+72,263,38,34,`0${i+1}`,17,{font:'Inter',weight:700,letterSpacing:0}),ct(x+15,306,152,30,'20XX',22,{font:'Inter',weight:700,letterSpacing:0}),box(x,347,182,236,i===2?K.soft:K.gray,{el:'timeline'}),I(x+66,370,50,50,c.icon,'#000',{strokeWidth:1.05}),...(i===1?[Path(x+94,369,26,28,'M0 25 L21 4 M12 6 L21 4 L20 13',{viewBox:'0 0 26 28',fill:'none',stroke:'#000',strokeWidth:3})]:[]),ct(x+8,432,166,38,c.name,25,{weight:700}),ct(x+14,475,154,85,c.note,20,{lineHeight:1.4})];})
]));
slides.push(slide(17,'프로젝트 일정',[
 ...sideTitle('프로젝트','일정','프로젝트의 전체 일정을 한눈\n에 파악할 수 있는 간트 차트 형\n식의 페이지입니다.'),
 ...['1분기','2분기','3분기','4분기'].map((t,i)=>ct(563+i*143.5,157,143.5,37,t,17,{weight:700})),
 ...['시장 조사','사업 기획','디자인 및 설계','마케팅 홍보운영','유지보수'].flatMap((t,i)=>[R(403,195+i*77.4,160,77.4,K.gray),ct(407,208+i*77.4,152,50,t,17,{weight:700}),line(403,195+i*77.4,1138,195+i*77.4)]),line(403,582,1138,582),
 ...[713,855,998].map(x=>line(x,198,x,582,'#e7e7e7',.7,{dash:'3 3'})),
 ...[{x:563,y:195,w:179,fill:K.soft,name:'화면 설계서 제작',note:'일정 관리를 한눈에.'},{x:643,y:273,w:141,fill:K.mint,name:'핵심 기능 구현',note:'성장 과정을 증명'},{x:661,y:351,w:264,fill:K.pink,name:'베타 테스트 진행',note:'목표를 적어보세요.'},{x:855,y:429,w:177,fill:K.pale,name:'결과 보고서 제출',note:'막대 길이로 흐름을 파악'},{x:998,y:508,w:140,fill:K.soft,name:'만족도 조사',note:'일정을 한눈에 관리'}].flatMap(c=>[R(c.x,c.y,c.w,c.y===508?74:76,c.fill,{el:'timeline'}),ct(c.x+3,c.y+8,c.w-6,34,c.name,21,{weight:700}),ct(c.x+2,c.y+43,c.w-4,26,c.note,16)])
]));
slides.push(slide(18,'월간운영 일정',[
 ...sideTitle('월간운영','일정','날짜 칸 안에 구체적인 일정이\n나 할 일을 키워드 위주로 짧게\n입력해 보세요.'),
 R(423,160,717,31,K.blue,{el:'table'}),...['SUN','MON','TUE','WED','THU','FRI','SAT'].map((t,i)=>ct(423+i*102.43,161,102.43,29,t,17,{font:'Inter',weight:700,color:i===0?'#cb000d':i===6?'#2e6096':'#000',letterSpacing:0})),
 ...[190,268,347,426,505,583].map(y=>line(423,y,1140,y,'#777',1)),
 ...[{n:5,col:5,row:0,name:'휴무',fill:K.pink},{n:15,col:1,row:2,name:'주간회의',fill:K.soft},{n:26,col:5,row:3,name:'급여일',fill:K.pale},{n:29,col:1,row:4,name:'결의서 마감',fill:K.mint},{n:31,col:3,row:4,name:'연말회의',fill:K.soft}].flatMap(c=>[R(423+c.col*102.43,191+c.row*78.4,102.43,77.4,c.fill),ct(425+c.col*102.43,216+c.row*78.4,98.43,47,c.name,21,{weight:700})]),
 ...Array.from({length:31},(_,i)=>{let n=i+1,offset=n, col=offset%7,row=Math.floor(offset/7);return tx(423+col*102.43,192+row*78.4,45,24,String(n),17,{font:'Inter',weight:600,letterSpacing:0,color:col===0?'#cb000d':col===6?'#2e6096':'#000'});})
]));
slides.push(slide(19,'계획일정 예시',[
 ...sideTitle('계획일정','예시','전체 로드맵을 보여줌으로써\n팀원들이 공통된 목표와 마감\n기한을 인지하게 하세요.'),
 R(394,163,746,35,K.blue,{el:'table'}),...Array.from({length:5},(_,i)=>ct(491+i*129.8,165,129.8,32,`${i+1} 주차`,17,{weight:700})),
 ...['Mon.','Tue.','Wed.','Thu.','Fri.','Sat.','Sun.'].flatMap((t,i)=>[R(394,198+i*55,746,55,i%2?K.gray:'#fff'),ct(394,198+i*55,97,55,t,17,{font:'Inter',weight:700,letterSpacing:0}),line(394,198+i*55,1140,198+i*55,'#888',1)]),line(394,583,1140,583,'#888',1),
 ...[{c:0,r:1,span:3,name:'시장 조사',fill:K.pink},{c:0,r:5,span:1,name:'사업 기획',fill:K.pink},{c:1,r:0,span:3,name:'디자인 및 설계',fill:K.soft},{c:2,r:0,span:3,name:'마케팅 홍보',fill:K.mint},{c:2,r:4,span:2,name:'테스트 진행',fill:K.pink},{c:3,r:1,span:4,name:'보고서 제출',fill:K.soft},{c:4,r:0,span:3,name:'운영, 유지보수',fill:K.mint},{c:4,r:4,span:2,name:'사용자\n만족도 조사',fill:K.pale}].flatMap(c=>[R(491+c.c*129.8,198+c.r*55,129.8,c.span*55,c.fill,{el:'timeline'}),ct(493+c.c*129.8,198+c.r*55,125.8,c.span*55,c.name,20,{weight:700,lineHeight:1.3})])
]));
slides.push(slide(20,'프로젝트 일정',[
 ...sideTitle('프로젝트','일정','프로젝트의 전체 일정을 한눈\n에 파악할 수 있는 간트 차트 형\n식의 페이지입니다.'),line(482,164,482,582),
 ...[{name:'팀 구성',note:'일정을 빈틈없이 관리',w:159,fill:K.gray,icon:'UsersRound'},{name:'기술 개발',note:'전체 일정의 흐름',w:296,fill:K.soft,icon:'Settings'},{name:'회원 유치',note:'제목을 굵게 강조',w:439,fill:K.pale,icon:'UsersRound'},{name:'대규모 마케팅',note:'여백에 이달의 목표를 기재',w:568,fill:K.gray,icon:'Handshake'},{name:'시장 1위 차지',note:'일정을 빈틈없이 관리',w:656,fill:K.soft,icon:'Award'}].flatMap((c,i)=>{const y=164+i*83.6;return [R(483,y,c.w,82,c.fill,{el:'timeline'}),ct(418,y+26,47,28,`${i+1}분기`,17,{weight:700}),C(475,y+34,12,12,K.soft,{stroke:'#000',strokeWidth:1}),ct(490,y+14,c.w-14,33,c.name,21,{weight:700}),ct(490,y+45,c.w-14,27,c.note,16),...(i<4?[line(483,y+83.6,1139,y+83.6,'#999',1,{dash:'1 3'})]:[]),I(1088,y+20,42,42,c.icon,'#dddddd',{strokeWidth:1.1})];})
]));
slides.push(slide(21,'실행단계 정리',[
 ...title('실행단계 정리',{x:0,w:1280,center:true,markX:675,markW:114}),
 ...[{x:140,name:'계획',icon:'FilePenLine',note:'프로젝트의 시작을 알리는 첫\n번째 단계로 배경이나 추진 목\n적을 명확하게 보여줘야 해요.'},{x:487,name:'실행',icon:'CalendarCheck2',note:'왜 이 프로젝트가 시작되었는지\n어떤 문제를 해결하고자 하는지\n구체적으로 서술해 보세요.'},{x:836,name:'개선',icon:'ChartNoAxesCombined',note:'전체적인 방향성을 제시하고 프\n로젝트에 대한 기대감을 심어주\n는 도입부 역할을 합니다.'}].flatMap(c=>[box(c.x,255,304,203,K.gray,{el:'steps'}),box(c.x,255,304,56,K.pale),I(c.x+116,273,23,23,c.icon),tx(c.x+144,267,112,35,c.name,25,{weight:700}),ct(c.x+24,338,256,86,c.note,20,{lineHeight:1.4})]),arrow(456,351),arrow(803,351),
 box(140,484,1000,99,K.yellow,{el:'callout'}),I(195,521,24,24,'SquareCheckBig','#b00000',{strokeWidth:1.6}),tx(236,517,70,39,'출시',25,{weight:700}),ct(317,507,798,54,'명확한 목표 의식을 보여주어 프로젝트가 올바른 방향으로 나아가고 있음을 첫 장에서 증명해요.',21)
]));
slides.push(slide(22,'업무분담 구조',[
 ...title('업무분담 구조',{x:0,w:1280,center:true,markX:675,markW:114}),
 ...[[266,415,289,415],[289,326,289,508],[289,326,311,326],[289,508,311,508],[493,326,523,326],[523,284,523,375],[523,284,546,284],[523,375,546,375],[493,508,523,508],[523,465,523,555],[523,465,546,465],[523,555,546,555],[728,284,753,284],[728,375,753,375],[728,465,753,465],[728,555,753,555],[935,284,958,284],[935,375,958,375],[935,555,958,555]].map(a=>line(...a)),
 C(140,354,126,125,K.hi,{stroke:'#000',strokeWidth:1.2,el:'hierarchy'}),ct(145,391,116,50,'대표이사',25,{weight:700}),
 ...[{x:311,y:299,w:182,text:'영업본부',fill:K.soft,bold:true},{x:311,y:480,w:182,text:'운영본부',fill:K.soft,bold:true},{x:546,y:255,w:182,text:'마케팅 팀',fill:K.pale,bold:true},{x:546,y:347,w:182,text:'영업 팀',fill:K.pale,bold:true},{x:546,y:438,w:182,text:'디자인 팀',fill:K.pale,bold:true},{x:546,y:527,w:182,text:'개발 팀',fill:K.pale,bold:true},{x:753,y:255,w:182,text:'김00 팀장'},{x:753,y:347,w:182,text:'이00 팀장'},{x:753,y:438,w:182,text:'김00 팀장'},{x:753,y:527,w:182,text:'최00 팀장'},{x:958,y:255,w:182,text:'박00 선임'},{x:958,y:347,w:182,text:'박00 대리'},{x:958,y:527,w:182,text:'정00 대리'}].flatMap(c=>[box(c.x,c.y,c.w,56,c.fill||K.gray,{el:'hierarchy'}),ct(c.x,c.y,c.w,56,c.text,c.bold?25:21,{weight:c.bold?700:400})])
]));
function connection(x,y,x2,y2,color='#000',width=1){const angle=Math.atan2(y2-y,x2-x),s=10;return [line(x,y,x2,y2,color,width),Path(x2-s/2,y2-s/2,s,s,'M0 0 L100 50 L0 100 Z',{fill:color,rotate:angle*180/Math.PI,el:'flowchart'})];}
slides.push(slide(23,'협업흐름',[
 ...sideTitle('','','쌍방향으로 이루어지는 소통\n구조를 화살표를 활용해 명확히\n설명해 보세요.'),hi(128,162,194),tx(140,151,220,60,'협업흐름',48,{weight:500,letterSpacing:-.3,lineHeight:1.15}),
 ...connection(751,265,590,455,'#ca0018',.8),...connection(1041,456,877,269,'#000',.8),...connection(624,533,996,533),...connection(1000,522,629,522),
 C(749,163,126,125,K.pale,{stroke:'#000',strokeWidth:1.2,el:'cycle'}),ct(749,195,126,61,'기업',22,{weight:700}),C(487,457,126,126,K.pale,{stroke:'#000',strokeWidth:1.2}),ct(487,491,126,57,'고객',22,{weight:700}),C(1011,457,126,126,K.pale,{stroke:'#000',strokeWidth:1.2}),ct(1011,491,126,57,'파트너',22,{weight:700}),
 C(729,309,166,166,K.hi,{stroke:'#000',strokeWidth:1.2,el:'hub'}),I(795,345,34,32,'Aperture','#000',{strokeWidth:3}),ct(741,381,142,54,'MIRI\nCOMPANY',23,{font:'Inter',weight:750,lineHeight:1.08,letterSpacing:-.4}),
 tx(604,320,117,25,'뗄 수 없는 사이',15,{color:'#ca0018',rotate:-50,letterSpacing:-.3}),tx(920,339,118,25,'긴밀한 협업 관계',15,{rotate:49,letterSpacing:-.3}),ct(699,492,226,25,'함께 만드는 시너지',16),ct(699,538,226,25,'유기적인 연결 고리',16)
]));
slides.push(slide(24,'구간전환',[
 ...sideTitle('','','준비된 디자인 시안을 목업에\n적용해 완성도를 높이세요.'),hi(128,162,194),tx(140,151,220,60,'구간전환',48,{weight:500,letterSpacing:-.3,lineHeight:1.15}),
 ...['디자인 시안을 목업에 적용해 완성도를 높이세요.','아이디어를 구체적인 실물 형태로 시각화합니다.','손에 잡힐 듯한 리얼리티로 설득력을 높이세요.','광고가 현장에 걸린 모습을 시뮬레이션해요.'].flatMap((t,i)=>[R(404,205+i*87,636,72,i===3?K.soft:K.gray,{radius:36,el:'agenda'}),ct(427,221+i*87,40,40,`0${i+1}`,17,{font:'Inter',weight:700,letterSpacing:0}),tx(470,224+i*87,467,42,t,20)]),...device(925,168)
]));
slides.push(slide(25,'운영 체크항목',[
 ...title('운영 체크항목',{x:0,w:1280,center:true,markX:593,markW:195}),
 R(140,254,1000,45,K.blue,{el:'table'}),...['모델명','화면크기','배터리 용량','저장공간','판매가'].map((t,i)=>ct([140,331,534,736,938][i],257,[191,203,202,202,202][i],39,t,22,{weight:700})),
 ...[['Model A','6.1인치','3,000mAh','128GB','90만원'],['Model B','6.5인치','4,000mAh','256GB','110만원'],['Model C','6.7인치','4,500mAh','512GB','130만원'],['Model D','7.0인치','5,000mAh','1TB','150만원']].flatMap((row,r)=>[R(140,299+r*71,191,71,K.gray),...row.map((t,c)=>ct([140,331,534,736,938][c],299+r*71,[191,203,202,202,202][c],71,t,23,{weight:c===0?700:400})),line(140,299+r*71,1140,299+r*71,'#888',1)]),line(140,254,1140,254,'#555',1),line(140,583,1140,583,'#888',1),...[331,534,736,938].map(x=>line(x,254,x,583,'#777',1))
]));
slides.push(slide(26,'일정 요약표',[
 ...title('일정 요약표',{x:0,w:1280,center:true,markX:609,markW:161}),
 R(140,254,1000,47,K.blue,{el:'table'}),ct(140,259,1000,37,'일정 요약 테이블',23,{weight:700}),R(140,301,1000,58,K.pale),ct(140,306,302,48,'구분',23,{weight:700}),ct(442,306,349,48,'개발',23,{weight:700}),ct(791,306,349,48,'출시',23,{weight:700}),
 R(140,359,142,235,K.soft),R(282,359,160,235,K.gray),ct(140,359,142,117,'운영본부',23,{weight:700}),ct(140,476,142,118,'영업본부',23,{weight:700}),
 ...['기획팀','디자인팀','영업팀','마케팅팀'].map((t,i)=>ct(282,359+i*58.75,160,58.75,t,22)),
 ...[[529,388],[1053,388],[878,447],[703,506],[703,565],[1053,565]].map(([x,y])=>ct(x-25,y-20,50,40,'O',22,{font:'Inter',letterSpacing:0})),
 ...[254,301,359,476,594].map(y=>line(140,y,1140,y,'#777',1)),...[418,535].map(y=>line(282,y,1140,y,'#777',1)),line(282,359,282,594,'#777',1),line(442,301,442,594,'#777',1),line(791,301,791,594,'#777',1),line(616,359,616,594,'#777',1),line(966,359,966,594,'#777',1)
]));
slides.push(slide(27,'리스크 관리흐름',[
 ...title('리스크 관리흐름',{x:0,w:1280,center:true,markX:611,markW:194}),
 ...[{x:140,name:'기획팀',items:['시장 조사','상품 기획'],checks:[true,true],foot:'계획 검증',icon:'ClipboardList'},{x:401,name:'물류팀',items:['생산','물류이동','입고'],checks:[false,false,true],foot:'품질 리스크',icon:'BadgeCheck'},{x:661,name:'디자인팀',items:['디자인','샘플 제작','인쇄 발주'],checks:[false,true,false],foot:'발주 오류 주의',icon:'TriangleAlert'},{x:920,name:'운영팀',items:['유통','판매'],checks:[true,false],foot:'CS 리스크 관리',icon:'Headset'}].flatMap((c,i)=>[box(c.x,260,220,231,K.gray,{el:'list'}),box(c.x,260,220,55,i===3?K.soft:K.pale),ct(c.x,266,220,42,c.name,25,{weight:700}),...c.items.flatMap((t,j)=>[tx(c.x+29,341+j*44,33,31,'01',17,{font:'Inter',weight:700,letterSpacing:0}),ct(c.x+66,336+j*44,96,37,t,22,{weight:700}),box(c.x+175,345+j*44,18,18,K.gray),...(c.checks[j]?[Path(c.x+174,340+j*44,26,25,'M2 10 L9 20 L25 0',{viewBox:'0 0 26 25',fill:'none',stroke:'#e12c4f',strokeWidth:3})]:[])]),arrow(c.x+101,501,'d',18),box(c.x,530,220,56,K.pink,{radius:28,el:'pill'}),I(c.x+32,547,22,22,c.icon),tx(c.x+61,541,153,38,c.foot,22,{weight:700})]),arrow(370,290)
]));
slides.push(slide(28,'실행 로드맵',[
 ...title('실행 로드맵',{x:0,w:1280,center:true,markX:610,markW:163}),line(233,420,1045,420),
 ...[{x:141,y:255,name:'신규 사업 부서',note:'성장 과정을\n증명하세요.',fill:K.soft,top:true},{x:346,y:474,name:'파트너사 업무 협약',note:'연속성을 강조할 수\n있습니다.',fill:K.pink,top:false},{x:550,y:255,name:'플랫폼 개발',note:'일정 관리를\n한눈에.',fill:K.soft,top:true},{x:755,y:474,name:'대규모 마케팅',note:'핵심 목표를 배치해\n보세요.',fill:K.pink,top:false},{x:953,y:255,name:'국내 시장 1위 차지',note:'일정을 한눈에\n관리하세요.',fill:K.soft,top:true}].flatMap(c=>{const cx=c.x+92;return [line(cx,c.top?364:425,cx,c.top?414:469,'#000',1.2,{dash:'4 3'}),box(c.x,c.y,187,109,K.gray,{el:'timeline'}),box(c.x,c.y,187,37,c.fill),ct(c.x,c.y+2,187,34,c.name,21,{weight:700}),ct(c.x+6,c.y+43,175,59,c.note,20,{lineHeight:1.2}),C(cx-6,413,12,12,c.fill,{stroke:'#000',strokeWidth:1}),ct(cx-46,c.top?429:381,92,30,'20XX',22,{font:'Inter',weight:700,letterSpacing:0})];})
]));
slides.push(slide(29,'운영포인트 정리',[
 ...sideTitle('운영포인트','정리','복잡한 이미지에서 핵심만 따로\n떼어내어 보여주면 정보 전달력\n이 훨씬 높아집니다.'),
 ...device(697,155,183,385),
 ...[[440,161,'메인 뷰'],[975,161,'디테일 뷰'],[440,385,'전체보기'],[975,385,'상세 보기']].flatMap(([x,y,t])=>[C(x,y,165,165,'#e5e5e5',{stroke:'#000',strokeWidth:1.1,el:'image-frame'}),ct(x,y+173,165,31,t,17,{weight:700})]),
 line(605,244,974,244,'#000',1.5,{dash:'5 4'}),line(605,466,727,466,'#000',1.5,{dash:'5 4'}),line(727,466,809,404,'#000',1.5,{dash:'5 4'}),line(849,461,973,461,'#000',1.5,{dash:'5 4'}),line(795,302,834,244,'#000',1.5,{dash:'5 4'}),...[[733,244],[795,302],[809,404],[849,461]].map(([x,y])=>C(x-6,y-6,12,12,K.soft,{stroke:'#000',strokeWidth:1.1}))
]));
slides.push(slide(30,'THANK YOU',[
 hi(311,266,660,28),ct(280,259,720,42,'"깨진 이미지는 깨진 신뢰와 같다. 선명함이 곧 설득력이다."',30,{weight:500,letterSpacing:-.7}),ct(280,301,720,120,'THANK YOU.',108,{font:'Inter',weight:800,letterSpacing:-1.2,lineHeight:1}),box(74,585,1132,65,K.blue,{el:'callout'}),ct(112,595,1056,44,'마케팅 1팀 / 김미리 대리    |    010-0000-0000    |    0000@00000.000',23,{letterSpacing:0})
]));

const libraryModules={
 8:{folder:'card',items:[{name:'주요 특징',note:'시선은 왼쪽에서 오른쪽으로 이동합니다. 정보를 가로로 배치하여 내용을 편안하게 읽을 수 있습니다.'},{name:'핵심 역량',note:'핵심 내용을 가로로 나란히 배치하여 복잡한 정보를 한눈에 비교할 수 있도록 정리해 보세요.'}]},
 9:{folder:'agenda',items:[{name:'핵심과제',kick:'KEY TASKS',note:'키워드 옆에 디테일한 설명을 더해요. 텍스트만으로 읽는 이를 설득해 보세요.',mark:'01'},{name:'체크리스트',kick:'CHECKLIST',note:'단락을 나누면 줄글 보다 읽기 편해요. 세로 배열은 단계별 설명에 좋아요.',mark:'02'},{name:'우선순위',kick:'TOP PRIORITY',note:'배열의 논리적인 순서를 보여주세요. 여백을 주어 읽는 이가 숨 쉴 틈을 줘요.',mark:'03'}]},
 10:{folder:'steps',items:[{name:'기획',note:'이슈에 대한 원인을 분석하고 해결하기 위한 방법들을 적어보세요.',mark:'01'},{name:'실행',note:'고객 피드백 적극 수용 · 성과 좋은 채널에 집중',mark:'02'},{name:'완료',note:'예산 재설정 후 모니터링 · 해결책을 작성해주세요.',mark:'03'}]},
 11:{folder:'cycle',items:[{name:'노출',note:'전체 흐름을 한눈에 파악할 수 있는 도표입니다.'},{name:'유입',note:'단계별 과정을 순서대로 보여줘 이해를 돕습니다.'},{name:'활동',note:'복잡한 절차를 단순화하여 명쾌하게 정리했어요.'},{name:'전환',note:'프로젝트 진행 상황과 미래 방향을 제시합니다.'},{name:'재구매',note:'각 단계 사이의 관계와 변화를 설명하기 좋아요.'},{name:'추천',note:'수행해야 할 핵심 키워드를 요약해 보여주세요.'}]},
 12:{folder:'steps',items:[{name:'가설 설정',note:'전체 흐름을 한눈에 파악할 수 있는 도표입니다.',mark:'01'},{name:'시장 검증',note:'단계별 과정을 순서대로 보여줘 이해를 돕습니다.',mark:'02'},{name:'정식 런칭',note:'프로젝트 진행 상황과 미래 방향을 제시합니다.',mark:'03'}]},
 13:{folder:'agenda',items:[{name:'순위 1',note:'중요 정보는 맨 위로 배치하세요. 키워드 옆에 디테일한 설명을 더해요.',mark:'01'},{name:'순위 2',note:'텍스트만으로 읽는 이를 설득해 보세요. 박스 크기를 일정하게 맞춰 정돈해요.',mark:'02'},{name:'순위 3',note:'배열의 논리적인 순서를 보여주세요. 여백을 주어 읽는 이가 숨 쉴 틈을 줘요.',mark:'03'}]},
 14:{folder:'steps',items:[{name:'프로젝트 착수',note:'전체 흐름을 한눈에 파악할 수 있는 도표입니다.',mark:'01'},{name:'기획 및 분석',note:'복잡한 절차를 단순화하여 명쾌하게 정리했어요.',mark:'02'},{name:'설계',note:'각 단계 사이의 관계와 변화를 설명하기 좋아요.',mark:'03'},{name:'구현',note:'목표 달성을 위한 논리적인 순서를 증명합니다.',mark:'04'},{name:'프로젝트 종료',note:'시작부터 종료까지의 전체 여정을 시각화해요.',mark:'05'}]},
 15:{folder:'chart-line',values:[10,30,50,60,80],labels:['2030','2031','2032','2033','2034'],items:[{name:'최근 5년 주가 변동',note:'미래를 예측하기 좋아요.'}]},
 16:{folder:'timeline',items:[{kick:'20XX',name:'법인 설립',note:'세부 계획을 세워 일정을 빈틈없이 관리하세요.'},{kick:'20XX',name:'서비스 출시',note:'걸어온 길을 이야기하듯 자연스럽게 풀어내세요.'},{kick:'20XX',name:'특허 등록',note:'막대를 배치하고 전체 일정의 흐름을 보세요.'},{kick:'20XX',name:'투자 유치',note:'연도별 제목을 굵게 강조해 가독성을 높여보세요.'},{kick:'20XX',name:'시장 차지',note:'아이콘으로 통일하고 사진을 넣어 꾸며보세요.'}]},
 17:{folder:'timeline',items:[{kick:'1분기',name:'화면 설계서 제작',note:'일정 관리를 한눈에.'},{kick:'2분기',name:'핵심 기능 구현',note:'성장 과정을 증명'},{kick:'2–3분기',name:'베타 테스트 진행',note:'목표를 적어보세요.'},{kick:'3분기',name:'결과 보고서 제출',note:'막대 길이로 흐름을 파악'},{kick:'4분기',name:'만족도 조사',note:'일정을 한눈에 관리'}]},
 18:{folder:'agenda',items:[{mark:'05',name:'휴무',note:'월간 운영 일정'},{mark:'15',name:'주간회의',note:'월간 운영 일정'},{mark:'26',name:'급여일',note:'월간 운영 일정'},{mark:'29',name:'결의서 마감',note:'월간 운영 일정'},{mark:'31',name:'연말회의',note:'월간 운영 일정'}]},
 19:{folder:'timeline',items:[{kick:'1 주차',name:'시장 조사',note:'사업 기획'},{kick:'2 주차',name:'디자인 및 설계',note:'전체 로드맵을 보여줍니다.'},{kick:'3 주차',name:'마케팅 홍보',note:'테스트 진행'},{kick:'4 주차',name:'보고서 제출',note:'공통된 목표와 마감 기한'},{kick:'5 주차',name:'운영, 유지보수',note:'사용자 만족도 조사'}]},
 20:{folder:'timeline',items:[{kick:'1분기',name:'팀 구성',note:'일정을 빈틈없이 관리'},{kick:'2분기',name:'기술 개발',note:'전체 일정의 흐름'},{kick:'3분기',name:'회원 유치',note:'제목을 굵게 강조'},{kick:'4분기',name:'대규모 마케팅',note:'여백에 이달의 목표를 기재'},{kick:'5분기',name:'시장 1위 차지',note:'일정을 빈틈없이 관리'}]},
 21:{folder:'steps',items:[{mark:'01',name:'계획',note:'프로젝트의 시작을 알리는 첫 번째 단계로 배경이나 추진 목적을 명확하게 보여줘야 해요.'},{mark:'02',name:'실행',note:'왜 이 프로젝트가 시작되었는지 어떤 문제를 해결하고자 하는지 구체적으로 서술해 보세요.'},{mark:'03',name:'개선',note:'전체적인 방향성을 제시하고 프로젝트에 대한 기대감을 심어주는 도입부 역할을 합니다.'}]},
 22:{folder:'hierarchy',items:[{name:'대표이사',note:'영업본부 · 운영본부'},{name:'마케팅 팀',note:'김00 팀장 · 박00 선임'},{name:'영업 팀',note:'이00 팀장 · 박00 대리'},{name:'디자인 팀',note:'김00 팀장'},{name:'개발 팀',note:'최00 팀장 · 정00 대리'}]},
 23:{folder:'cycle',items:[{name:'기업',note:'긴밀한 협업 관계'},{name:'파트너',note:'함께 만드는 시너지'},{name:'고객',note:'유기적인 연결 고리'}]},
 24:{folder:'agenda',items:[{mark:'01',name:'디자인 시안을 목업에 적용해 완성도를 높이세요.',note:'준비된 디자인 시안을 목업에 적용해 완성도를 높이세요.'},{mark:'02',name:'아이디어를 구체적인 실물 형태로 시각화합니다.'},{mark:'03',name:'손에 잡힐 듯한 리얼리티로 설득력을 높이세요.'},{mark:'04',name:'광고가 현장에 걸린 모습을 시뮬레이션해요.'}]},
 25:{folder:'table',rows:[['모델명','화면크기','배터리 용량','저장공간','판매가'],['Model A','6.1인치','3,000mAh','128GB','90만원'],['Model B','6.5인치','4,000mAh','256GB','110만원'],['Model C','6.7인치','4,500mAh','512GB','130만원'],['Model D','7.0인치','5,000mAh','1TB','150만원']],items:[{name:'운영 체크항목',note:''}]},
 26:{folder:'table',rows:[['구분','팀','개발 1','개발 2','출시 1','출시 2'],['운영본부','기획팀','O','','','O'],['운영본부','디자인팀','','','O',''],['영업본부','영업팀','','O','',''],['영업본부','마케팅팀','','O','','O']],items:[{name:'일정 요약 테이블',note:''}]},
 27:{folder:'steps',items:[{mark:'01',name:'기획팀',note:'시장 조사 · 상품 기획 / 계획 검증'},{mark:'02',name:'물류팀',note:'생산 · 물류이동 · 입고 / 품질 리스크'},{mark:'03',name:'디자인팀',note:'디자인 · 샘플 제작 · 인쇄 발주 / 발주 오류 주의'},{mark:'04',name:'운영팀',note:'유통 · 판매 / CS 리스크 관리'}]},
 28:{folder:'timeline',items:[{kick:'20XX',name:'신규 사업 부서',note:'성장 과정을 증명하세요.'},{kick:'20XX',name:'파트너사 업무 협약',note:'연속성을 강조할 수 있습니다.'},{kick:'20XX',name:'플랫폼 개발',note:'일정 관리를 한눈에.'},{kick:'20XX',name:'대규모 마케팅',note:'핵심 목표를 배치해 보세요.'},{kick:'20XX',name:'국내 시장 1위 차지',note:'일정을 한눈에 관리하세요.'}]},
 29:{folder:'card',items:[{name:'메인 뷰',note:'복잡한 이미지에서 핵심만 따로 떼어내어 보여줍니다.'},{name:'디테일 뷰',note:'정보 전달력이 훨씬 높아집니다.'},{name:'전체보기',note:'운영포인트 정리'},{name:'상세 보기',note:'운영포인트 정리'}]},
 30:{folder:'card',items:[{name:'THANK YOU.',note:'깨진 이미지는 깨진 신뢰와 같다. 선명함이 곧 설득력이다.',kick:'MIRI COMPANY'}]}
};
for(const s of slides)s.library=libraryModules[Number(s.id.slice(6))];
export default {id:'005',title:'Monthly Review — Miri Company',slides};
