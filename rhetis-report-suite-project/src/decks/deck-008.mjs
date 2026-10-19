import {T,R,C,L,P,I,Path,Chip} from '../primitives.mjs';
const c={frame:'#9baca9',accent:'#7f8d8a',mid:'#acbdb9',pale:'#e3e8e7',paler:'#f1f3f2',dark:'#383838',white:'#ffffff',line:'#9eaaa7',soft:'#b9c5c3'};
const tx=(x,y,w,h,text,size=18,o={})=>T(x,y,w,h,text,size,{font:'Pretendard',color:c.dark,lineHeight:1.48,letterSpacing:-0.35,wordBreak:'break-all',...o});
const bold=(x,y,w,h,text,size=22,o={})=>tx(x,y,w,h,text,size,{weight:700,...o});
const rect=(x,y,w,h,fill=c.pale,o={})=>R(x,y,w,h,fill,{el:'card',...o});
const head=(en,ko,desc)=>[rect(40,40,1200,640,c.white,{el:'foundation'}),tx(67,63,1075,27,en,20,{font:'Inter',weight:600,color:c.mid,letterSpacing:-.3}),bold(67,89,1100,64,ko,44,{color:c.accent,lineHeight:1.2,letterSpacing:-.2}),bold(1184,63,32,34,'00',22,{color:c.accent,font:'Inter'}),tx(67,163,1146,63,desc,20,{weight:500,lineHeight:1.35}),L(67,267,1213,267,c.line,1.2)];
const section=(x,y,w,text,col=c.accent)=>[rect(x,y+5,3,20,col),bold(x+18,y,w-20,34,text,23,{color:col,lineHeight:1.2})];
const ph=(x,y,w,h,o={})=>P(x,y,w,h,'',{el:'image-frame',...o});
const icon=(x,y,w,h,name,color=c.mid)=>I(x,y,w,h,name,color,{strokeWidth:1.7});
const bullet=(x,y,w,text,size=18,col=c.dark)=>[C(x,y+11,6,6,col),tx(x+17,y,w-17,63,text,size,{color:col})];
const bullets=(x,y,w,items,size=18,gap=29,col=c.dark)=>items.flatMap((t,i)=>bullet(x,y+i*gap,w,t,size,col));
const arrow=(x,y,w=20,h=80)=>rect(x,y,w,h,`linear-gradient(to right,#fff,${c.accent})`,{clipPath:'polygon(0 0,100% 50%,0 100%)',el:'steps'});
const S=(n,title,elements)=>({id:`slide_${String(n).padStart(2,'0')}`,title,background:c.frame,elements});
const generic='텍스트 박스를 더블 클릭해 내용을 입력해 주세요.\n이곳에 본문 내용을 입력해주세요.';
const photoBullets=['텍스트 무게를 줄이고 이미지를 더하세요.','사진 아래 핵심 요약으로 이해를 돕습니다.','이미지로 내용을 직관적으로 전달해 보세요.','주제와 잘 어울리는 사진을 배치해 보세요.'];
const slides=[];
slides.push(S(1,'BUSINESS PRESENTATION',[
 rect(40,40,1200,640,c.white),tx(97,104,900,49,'경쟁사 비교 분석 시 효과적인',33,{weight:500}),bold(95,154,1080,231,'BUSINESS\nPRESENTATION',104,{font:'Inter',weight:800,color:c.accent,lineHeight:1.03,letterSpacing:-.5}),bold(1148,66,70,33,'2080',22,{font:'Inter',color:c.accent}),L(67,397,1213,397,c.line,1.2),tx(97,429,1000,65,'비즈니스용으로 사용할 때 효과적인 프레젠테이션 입니다.\n프레젠테이션에 관한 설명을 간단하게 1~2줄로 기재해주세요.',20,{weight:500,lineHeight:1.45}),C(98,620,26,26,c.accent),...[2,6,11,15,20].map((a,i)=>L(98+a,619-i%2*2,98+a,648+i%2*2,c.white,1)),bold(130,619,280,35,'MIRI Company',20,{font:'Inter',color:c.accent,letterSpacing:-.5})
]));
slides.push(S(2,'Contents',[
 rect(40,40,1200,640,c.white),bold(67,66,1075,102,'Contents',86,{font:'Inter',weight:800,color:c.accent,lineHeight:1.05,letterSpacing:0}),tx(67,163,1145,65,'많은 데이터를 한 번에 정리하기 좋은 표 페이지입니다.\n동일한 기준에 따른 데이터를 입력해 칸별로 쉽게 비교 분석해 보세요.',20,{weight:500,lineHeight:1.35}),L(67,267,1213,267,c.line,1.2),...[1,2,3,4,5].flatMap((n,i)=>[rect(553,321+i*64,658,49,c.pale),rect(553,321+i*64,72,49,c.accent),bold(553,321+i*64,72,49,String(n).padStart(2,'0'),22,{font:'Inter',color:c.white,align:'center',valign:'middle'}),tx(644,329+i*64,545,36,'여기에 서브타이틀을 입력하세요.',22)])
]));
slides.push(S(3,'Competitor Overview',[
 R(41,41,1198,638,'none',{stroke:c.white,strokeWidth:2}),bold(67,66,1120,190,'Competitor\nOverview',92,{font:'Inter',weight:800,color:c.white,lineHeight:1.0,letterSpacing:-1}),L(67,267,1213,267,c.white,1.2),rect(79,299,54,54,c.accent),icon(88,311,34,30,'ArrowRight',c.white),bold(162,293,800,41,'경쟁사 개요',23,{color:c.white}),tx(162,336,940,65,'제목에 설명을 더해 완성도를 높이세요.\n챕터가 존재하는 이유를 명확하게 설명해 보세요.',20,{color:c.white,weight:500,lineHeight:1.4}),bold(960,460,270,230,'01',224,{font:'Inter',color:c.soft,lineHeight:1,letterSpacing:0})
]));
{
 const es=head('Competitor Overview','경쟁사 개요','많은 데이터를 한 번에 정리하기 좋은 표 페이지입니다.\n동일한 기준에 따른 데이터를 입력해 칸별로 쉽게 비교 분석해 보세요.');
 es.push(rect(67,267,1146,44,c.frame));
 const xs=[67,244,729],ws=[177,485,484];
 ['','A사','B사'].forEach((v,i)=>es.push(bold(xs[i],269,ws[i],42,v,24,{color:c.white,align:'center',valign:'middle'})));
 const rows=[['설립 연도','2080년','텍스트'],['사업 분야','텍스트를 넣어주세요','텍스트를 넣어주세요'],['직원 수','34명','56명'],['제품 및 서비스','텍스트를 넣어주세요','텍스트를 넣어주세요'],['주요 고객','텍스트를 넣어주세요','텍스트를 넣어주세요']];
 rows.forEach((row,i)=>{const y=311+i*68.5;es.push(rect(67,y,177,68.5,c.paler),L(67,y+68.5,1213,y+68.5,'#bcc5c2',.8));row.forEach((v,j)=>es.push(tx(xs[j]+8,y+17,ws[j]-16,38,v,20,{weight:j?500:700,color:j?c.dark:c.accent,align:'center',valign:'middle'})));});
 [244,729].forEach(x=>es.push(L(x,267,x,653,'#b8c3bf',.8)));
 slides.push(S(4,'경쟁사 개요',es));
}
{
 const es=head('Benchmarking and Goal Setting','벤치마킹 및 목표 설정','전체 내용을 요약하거나 주요 특징을 나열하는 페이지로 활용하세요.\n세부 사항으로 들어가기 전 핵심 포인트를 짚어줄 때 효과적입니다.');
 es.push(...section(68,278,550,'벤치마킹 요약'),...section(659,278,554,'자사 목표'),rect(67,318,273,120,c.accent),rect(348,318,273,120,c.dark),bold(83,329,245,32,'회사 A의 강점',20,{color:c.white}),bold(364,329,245,32,'회사 B의 강점',20,{color:c.white}),tx(83,371,240,59,'이곳에 회사 A의 주요 강점을 요약\n하여 적어보세요.',18,{color:c.white}),tx(364,371,240,59,'이곳에 회사 B의 주요 강점을 요약\n하여 적어보세요.',18,{color:c.white}),arrow(631,338,20,80),rect(659,318,554,120,c.pale));
 ['기술 혁신','서비스 개선','비용 효율화'].forEach((t,i)=>es.push(bold(680,337+i*29,100,30,t,18,{color:c.accent}),tx(783,337+i*29,418,29,i<2?'이곳에 기술 혁신과 관련된 목표를 적어보세요.':'비용 절감 및 최적화와 관련된 목표를 적어보세요.',18)));
 es.push(L(67,460,1213,460,c.line,1.2),...section(68,477,1000,'목표 달성을 위한 전략적 제언'));
 [1,2,3].forEach((n,i)=>es.push(rect(67,520+i*47,1146,40,c.pale),rect(67,520+i*47,123,40,c.accent),bold(67,520+i*47,123,40,`제언 ${n}`,18,{color:c.white,align:'center',valign:'middle'}),tx(205,527+i*47,990,29,`이곳에 ${['첫','두','세'][i]} 번째 전략적 제언을 적어보세요.`,18)));
 slides.push(S(5,'벤치마킹 및 목표 설정',es));
}
{
 const es=head('Paragraph Organization Page','문단 정리 페이지','핵심 내용을 가로로 나열해 강조하세요.\n단계별 진행 과정을 순서대로 배치하기 좋습니다.');
 es.push(...section(68,278,568,'주요 특징'),...section(646,278,568,'체크 포인트'));
 const cols=[{x:67,fill:c.paler,bar:c.frame,title:'핵심 내용을 가로로 나열해 강조하세요.',body:'글자의 위치와 간격을 조절하여 여백의 미를 살려보세요. 빽빽하게 채우기보다 적절한 숨 쉴 공간을 두어야 정보가 눈에 더 잘 들어옵니다. 텍스트 자체가 디자인 요소가 되어, 내용의 밀도와 시각적인 균형을 동시에 잡을 수 있는 세련된 레이아웃입니다. 여백은 비어있는 공간이 아니라, 정보를 돋보이게 만드는 중요한 디자인 장치임을 기억하세요.\n\n긴 본문의 내용을 핵심만 간추려 요약하는 공간으로 활용해 보세요. 모든 정보를 다 담기보다는, 꼭 기억해야 할 메시지를 중심으로 문장을 다듬는 것이 좋습니다. 불필요한 수식어를 덜어내고 명료하게 작성하면 전달력이 배가됩니다.'},{x:645,fill:c.pale,bar:c.accent,title:'시각적으로 정돈된 느낌을 주는 구조입니다.',body:'대등한 중요도를 가진 정보들을 나란히 배치할 때 유용합니다. 여러 가지 항목을 병렬로 구성하여 각각의 독립적인 내용을 설명해 보세요. 이때 각 텍스트 박스의 크기와 줄 수를 비슷하게 맞추면 디자인적으로 안정감을 줍니다. 시각적인 통일성을 유지하면서 다양한 정보를 한 번에 보여주세요.\n\n긴 문장보다는 개조식 구성을 추천합니다. 명사형으로 문장을 끝맺거나 글머리 기호를 활용하면 가독성이 크게 향상됩니다. 읽는 사람이 한눈에 요점을 파악할 수 있도록 배려하는 글쓰기 방식입니다. 빠르고 정확한 정보 전달이 필요할 때 이 레이아웃을 적극 활용해 보세요.'}];
 cols.forEach(a=>es.push(rect(a.x,318,568,335,a.fill),rect(a.x,318,568,49,a.bar),bold(a.x+16,329,534,32,a.title,20,{color:c.white}),tx(a.x+16,386,536,257,a.body,18,{lineHeight:1.51})));
 slides.push(S(6,'문단 정리 페이지',es));
}
{
 const es=head('List-type Array Page','리스트형 배열 페이지','정보의 위계와 순서가 세로로 구성되도록 표현해보세요.\n각 항목에 대한 상세한 설명을 덧붙이기 좋습니다.');
 es.push(...section(68,278,1000,'주요 특징'));
 const names=['중요 정보는 맨 위로 배치하세요.','키워드 옆에 디테일한 설명을 더해요.','시선이 위에서 아래로 이동합니다.'];
 names.forEach((name,i)=>{let y=318+i*114.5;es.push(rect(67,y,554,107,c.pale),rect(67,y,98,107,c.accent),bold(67,y,98,107,String(i+1).padStart(2,'0'),20,{color:c.white,font:'Inter',align:'center',valign:'middle'}),bold(186,y+13,425,31,name,18,{color:c.accent}),tx(186,y+42,425,58,generic,18),arrow(631,y+13,20,80),rect(659,y,554,107,c.paler),bold(681,y+13,510,31,name,18,{color:c.accent}),tx(681,y+42,510,58,generic,18));});
 slides.push(S(7,'리스트형 배열 페이지',es));
}
{
 const es=head('Five forces analysis','5가지 힘 분석','시선은 왼쪽에서 오른쪽으로 이동합니다.\n정보를 가로로 배치하면 내용을 편안하게 읽을 수 있습니다.');
 const names=['잠재 진입자','공급자','구매자','대체자'];const nouns=['잠재 진입자의 위협을','공급자의 협상력을','구매자의 협상력을','대체 상품의 위협을'];const icons=['CircleUserRound','Truck','ShoppingCart','Copy'];
 names.forEach((v,i)=>{const x=68+i*286;es.push(rect(x,268,286,385,i%2?c.pale:c.paler),...section(x+18,282,250,v));for(let j=0;j<3;j++)es.push(...bullet(x+12,336+j*60,263,[`이곳에 잠재 진입자의 위협을 간략\n하게 분석해보세요.`,`이곳에 공급자의 협상력을 간략하게\n분석해보세요.`,`이곳에 구매자의 협상력을 간략하게\n분석해보세요.`,`이곳에 대체 상품의 위협을 간략하\n게 분석해보세요.`][i],18));es.push(icon(x+219,588,53,53,icons[i]));});
 slides.push(S(8,'5가지 힘 분석',es));
}
{
 const es=head('Key Performance Indicators in Numbers','숫자로 보는 핵심 성과','숫자가 주인공인 페이지입니다.\n가장 자랑하고 싶은 핵심 성과를 크게 적어 시선을 사로잡으세요.');
 es.push(...section(68,283,1000,'재무 실적'));
 const cards=[{x:67,y:332,w:376,h:321,fill:c.mid,label:'매출',fig:'500',unit:'억 원',icon:'Presentation'},{x:453,y:332,w:375,h:156,label:'영업이익',fig:'300',unit:'억 원',icon:'BriefcaseBusiness'},{x:838,y:332,w:375,h:156,label:'당기 순이익',fig:'10',unit:'억 원',icon:'Tag'},{x:453,y:498,w:375,h:155,label:'누적 투자액',fig:'100',unit:'억 원',icon:'Layers'},{x:838,y:498,w:375,h:155,label:'기업 가치',fig:'1',unit:'조 원',icon:'Building2'}];
 cards.forEach(a=>{es.push(rect(a.x,a.y,a.w,a.h,a.fill||c.pale),bold(a.x+15,a.y+10,a.w-30,40,a.label,23,{color:a.fill?c.dark:c.accent}),icon(a.x+13,a.y+a.h-66,a.fill?67:46,a.fill?58:46,a.icon,a.fill?c.accent:c.mid));const right=a.x+a.w-16,unitW=68,numW=a.fig.length===3?108:a.fig.length===2?69:36;es.push(bold(right-unitW-numW,a.y+a.h-84,numW,80,a.fig,54,{font:'Inter',align:'right',lineHeight:1.48,letterSpacing:-1}),bold(right-unitW,a.y+a.h-55,unitW,55,a.unit,34,{align:'right',lineHeight:1.48,letterSpacing:-1.5}));});
 slides.push(S(9,'숫자로 보는 핵심 성과',es));
}
slides.push(S(10,'키 메시지 전달하기',[
 ...head('Key Message','키 메시지 전달하기','구구절절한 설명 대신 강렬한 한 문장으로 청중을 설득해 보세요.\n여백을 충분히 두어 시선이 오직 텍스트에만 집중되도록 하세요.'),ph(68,268,1145,385),Path(255,377,20,166,'M100 0 H0 V100 H100',{fill:'none',stroke:c.dark,strokeWidth:3}),Path(1006,377,20,166,'M0 0 H100 V100 H0',{fill:'none',stroke:c.dark,strokeWidth:3}),bold(300,381,680,100,'텍스트와 사진만 잘 배치해도\n잘 만든 프레젠테이션처럼 보인다.',40,{align:'center',lineHeight:1.35}),bold(322,492,636,54,'With just a few well-placed text and photos,\nit looks like a well-crafted presentation.',19,{font:'Inter',align:'center',lineHeight:1.4})
]));
{
 const es=head('Key Message','데이터 시각화 페이지','단순한 나열을 넘어 데이터를 스토리텔링하는 도구로 활용하면 딱딱한 숫자의 이해를 도울 수 있습니다.\n넉넉한 여백을 활용해 답답함 없이 시원한 느낌을 연출해 보세요.');
 es.push(...section(68,282,550,'비전'),...section(651,282,560,'목표'),rect(68,325,562,112,c.paler),rect(650,325,563,112,c.pale),rect(81,338,86,86,c.white),rect(664,338,86,86,c.white),icon(97,350,54,60,'Lightbulb'),icon(681,352,52,58,'Pin'),...bullets(185,340,430,['이곳에 기업의 비전에 대한 내용을 입력해주세요.','아이콘과 함께 배치해서 꾸며보세요.','한눈에 쏙 들어옵니다.'],18,27),...bullets(767,340,433,['이곳에 기업의 목표에 대한 내용을 입력해주세요.','아이콘과 함께 배치해서 정보를 시각화해요.','텍스트 무게를 줄여요.'],18,27),...section(68,460,1000,'솔루션'),rect(68,506,1145,147,c.mid),rect(81,520,119,119,c.white),icon(110,550,61,61,'SquarePen'),...bullets(219,527,977,['이곳에 기업의 비전과 목표를 위한 솔루션에 대한 내용을 입력해주세요.','인간의 뇌는 글자보다 이미지를 훨씬 빠르게 처리하므로 복잡한 정보를 빠르고 정확하게 전달해 보세요.','내용을 카테고리별로 나누고 아이콘을 배치하면 정보의 구획이 명확해져 읽는 이가 빠르게 파악합니다.','글자보다 이미지를 더 오래 기억한다는 원리를 이용해 픽토그램으로 핵심 메시지를 확실히 각인시키세요.'],18,27));
 slides.push(S(11,'데이터 시각화 페이지',es));
}
{
 const es=head('Photo and Text Layout','사진과 텍스트 레이아웃','주제와 관련된 사진을 넣고 핵심 내용을 요약해 적어보세요.\n시각 자료를 활용하면 이해도를 높일 수 있습니다.');
 es.push(rect(68,268,1145,385,c.paler),ph(83,280,537,359),...section(640,278,560,'눈길을 끄는 시각 자료'),bold(655,349,540,40,'주제와 가장 잘 어울리는 사진을 배치해 보세요.',20),tx(655,389,540,246,"사진을 순서대로 배치하여 이야기를 만들어보세요. 'Before & After' 비교나, '기획-실행-결과'의 과정을 이미지로 보여줄 수 있습니다. 좌에서 우로 시선이 흐르도록 배치하고, 각 단계에 맞는 설명을 덧붙이면 자연스러운 스토리텔링이 완성됩니다.\n\n텍스트만으로는 지루할 수 있는 내용에 생동감을 불어넣는 페이지입니다. 사진의 톤 앤 매너를 전체 템플릿 색상과 맞추면 디자인 완성도가 올라갑니다. 이미지와 텍스트 박스의 끝선을 맞춰 정렬하면 보이지 않는 그리드가 생겨 깔끔해 보입니다. 비주얼과 구체적인 정보가 균형을 이루도록 구성하세요.",18,{lineHeight:1.51}));
 slides.push(S(12,'사진과 텍스트 레이아웃',es));
}
{
 const es=head('Image Description Page','이미지 설명 페이지','사람의 시선은 본능적으로 텍스트보다 이미지에 꽂힙니다.\n강조하고 싶은 정보를 이미지와 가깝게 배치해 보세요.');
 es.push(...section(68,278,567,'사진과 글의 찰떡 조화'),...section(646,278,567,'한눈에 들어오는 배치'));
 [{x:67,fill:c.paler,bar:c.mid,title:'이미지와 텍스트의 균형이 아주 중요해요.',body:'현장 사진이나 제품의 실물 이미지를 배치하여 정보의 신뢰도를 높여보세요. 텍스트가 설명하고 이미지가 증명하는 구조는 읽는 사람에게 가장 확실한 믿음을 줍니다.',list:photoBullets},{x:645,fill:c.pale,bar:c.accent,title:'제품의 디테일 컷으로 매력을 보여주세요.',body:'복잡한 설명 대신 직관적인 사진 한 장을 보여주는 것이 훨씬 효과적입니다. 사진 아래에는 핵심 내용을 요약한 캡션을 달아 이해를 돕는 페이지를 만들어보세요. 제품의 디테일 컷을 배치하면 장점을 더 명확히 설명할 수 있죠.',list:photoBullets.slice(1)}].forEach(a=>es.push(rect(a.x,318,568,335,a.fill),rect(a.x,318,568,49,a.bar),bold(a.x+16,328,536,32,a.title,20,{color:c.white}),tx(a.x+16,387,315,139,a.body,18,{lineHeight:1.5}),L(a.x+17,a.x===67?514:539,a.x+330,a.x===67?514:539,c.line,1),...bullets(a.x+18,a.x===67?531:556,321,a.list,18,27),ph(a.x+354,382,201,252)));
 slides.push(S(13,'이미지 설명 페이지',es));
}
{
 const es=head('Product Details','제품 상세 소개','제품의 외관 디자인을 설명하기 좋은 레이아웃입니다.\n전체 샷과 디테일 컷을 배치해 장점을 텍스트로 보충해 보세요.');
 ['설명은 짧고 명확하게','신뢰를 주는 증거 사진','비주얼이 곧 경쟁력'].forEach((t,i)=>{let x=68+i*385;es.push(...section(x,282,374,t),rect(x,328,375,325,[c.paler,c.pale,c.mid][i]),ph(x+16,345,342,172),...bullets(x+17,532,343,photoBullets,18,27));});
 slides.push(S(14,'제품 상세 소개',es));
}
{
 const es=head('Gallery-style Description Page','갤러리형 설명 페이지','여러 장의 이미지를 나열하여 시각적인 풍성함을 주세요.\n행사 스케치를 보여줄 때 크기를 통일하면 깔끔해 보입니다.');
 es.push(...section(68,278,512,'눈길을 끄는 시각 자료'),rect(68,318,513,335,c.paler),bold(84,334,480,36,'이미지와 텍스트의 균형이 아주 중요해요.',20),tx(84,379,480,83,'백 마디 말보다 한 장의 사진이 강력합니다. 현장 사진이나 제품의 실물 이미지를 배치하여 정보의 신뢰도를 높여보세요. 텍스트가 설명하고 이미지가 증명하는 구조는 읽는 사람에게 가장 확실한 믿음을 줍니다.',18,{lineHeight:1.51}),rect(84,486,482,150,c.mid),...bullets(103,508,447,photoBullets,18,27),ph(597,277,245,183),ph(852,277,361,183),ph(597,470,415,183),ph(1023,470,190,183));
 slides.push(S(15,'갤러리형 설명 페이지',es));
}
{
 const es=head('Image-centric Content','이미지 중심의 내용 전달','텍스트가 설명하고 이미지가 증명하는 구조는 읽는 사람에게 믿음을 줍니다.\n한 장의 사진으로 신뢰를 얻으세요.');
 es.push(ph(67,277,461,376),...section(543,278,670,'주인공은 크게 배치'));
 [{y:318,fill:c.paler,bar:c.mid,title:'01. 한 장으로 끝내요',text:'이미지와 설명을 함께 배치하여 내용을 전달하는 페이지입니다. 주제와 관련된 사진을 넣고, 그 아래 핵심 내용을 요약해 적어보세요. 시각 자료는 이해도를 높여줍니다.\n텍스트 분량을 조절하여 이미지와의 균형을 맞추는 것이 핵심입니다.'},{y:490,fill:c.pale,bar:c.accent,title:'02. 딱 보면 알게 돼요',text:"가장 알리고 싶은 핵심 정보가 담긴 이미지를 화면의 가장 눈에 띄는 곳에 크게 배치하세요. 이를 '메인 비주얼'로 삼아 시선을 고정시킨 후, 주변에 작은 서브 이미지나 텍스트를 배치하여 자연스럽게 정보를 읽어 내려가게 합니다."}].forEach(a=>es.push(rect(542,a.y,671,163,a.fill),rect(542,a.y,671,49,a.bar),bold(559,a.y+10,640,33,a.title,20,{color:c.white}),tx(566,a.y+65,623,88,a.text,18,{lineHeight:1.51})));
 slides.push(S(16,'이미지 중심의 내용 전달',es));
}
{
 const es=head('Project Results Report','프로젝트 결과 보고','텍스트가 설명하고 이미지가 증명하는 구조는 읽는 사람에게 믿음을 줍니다.\n한 장의 사진으로 신뢰를 얻으세요.');
 es.push(ph(67,277,330,376),...section(414,278,799,'백 마디 말보다 한 장'));
 [1,2,3].forEach((n,i)=>{const y=318+i*115;es.push(rect(413,y,800,105,c.paler),rect(413,y,70,105,[c.mid,c.frame,c.accent][i]),bold(413,y+10,70,34,String(n).padStart(2,'0'),20,{font:'Inter',color:c.white,align:'center'}),tx(504,y+12,689,87,'이미지와 설명을 함께 배치하여 내용을 전달하는 페이지입니다. 주제와 관련된 사진을 넣고, 그 아래에 핵심 내용을 요약해 적어보세요. 시각 자료는 이해도를 높여줍니다.\n텍스트 분량을 조절하여 이미지와의 균형을 맞추는 것이 핵심입니다.',18,{lineHeight:1.51}));});
 slides.push(S(17,'프로젝트 결과 보고',es));
}
{
 const es=head('Semicircular Keyword Deployment','반원형 키워드 전개','가장 중요한 주제를 정중앙에 배치하여 시선을 사로잡으세요.\n중앙으로 모이거나 뻗어 나가는 구조는 프레젠테이션의 핵심 메시지를 강조하기 좋습니다.');
 [282,245,205,160,116].forEach((r,i)=>es.push(Path(640-r,653-r,r*2,r,`M0 ${r} A${r} ${r} 0 0 1 ${r*2} ${r} Z`,{viewBox:`0 0 ${r*2} ${r}`,fill:['#f3f5f4','#e9eeec','#bccbc7','#96aaa4',c.accent][i],el:'pyramid'})));
 es.push(L(257,458,257,606,c.line,1),L(257,606,369,606,c.line,1),L(1019,458,1019,606,c.line,1),L(908,606,1019,606,c.line,1),C(254,454,7,7,c.line),C(1016,454,7,7,c.line));
 ['매출 증대','비용 절감','효율 개선'].forEach((t,i)=>{const x=68+i*383;es.push(rect(x,277,372,177,i===1?c.pale:c.paler),...section(x+21,297,299,t,c.dark),icon(x+306,288,53,53,['Store','CircleArrowDown','Settings'][i]),...bullets(x+21,380,330,['좌우 대칭으로 시각적 균형을 맞춰요.','여러 특징을 동등하게 보여줍니다.'],18,28));});
 es.push(icon(621,558,37,37,'CircleCheck',c.white),bold(550,601,180,48,'기대 효과',34,{color:c.white,align:'center'}));
 slides.push(S(18,'반원형 키워드 전개',es));
}
{
 const es=head('Venn diagram layout','벤 다이어그램 레이아웃','경쟁사와의 비교 우위를 점하고 싶다면 이 레이아웃을 활용해 차별점이 명확하게 드러나는 분석을 해보세요.\n독보적인 영역을 한눈에 파악할 수 있어요.');
 const panel=(x,title,fill,body,list)=>[rect(x,277,350,376,fill),rect(x,277,350,49,x===68?c.mid:c.frame),bold(x+16,285,320,34,title,20,{color:c.white}),tx(x+16,346,319,110,body,18,{lineHeight:1.51}),L(x+19,471,x+332,471,c.line,1),...bullets(x+18,495,319,list,18,27)];
 es.push(...panel(68,'공통점과 차이점',c.paler,'교집합 영역은 단순히 두 가지를 더한 것이 아니라 새로운 가치가 탄생하는 공간입니다. 색상을 강조하여 이곳이 결론임을 시각적으로 암시하세요.',['교집합에 색을 칠해 시선을 집중해요.','교집합으로 생기는 시너지를 보여주세요.','공통점과 차이점을 한눈에 비교해요.','새로운 가치가 탄생하는 공간입니다.','겹치는 곳이 바로 핵심 결론 영역이에요.']),...panel(862,'균형 잡힌 원의 배치',c.pale,'여러 원이 겹치는 교집합 영역은 전략적 결론이나 핵심 가치가 도출되는 곳입니다. 테두리를 강조해 돋보이게 만드는 것이 작성의 핵심입니다. 내용을 입력해주세요.',['논리적인 분석 과정을 시각화해 봐요.','원 크기를 비슷하게 맞춰 균형을 줘요.','관계를 직관적인 도형으로 정리합니다.','텍스트가 많으면 원 밖으로 빼내세요.']));
 es.push(Path(456,288,366,346,'M185 0 C251 0 297 54 297 116 C297 163 270 198 231 219 C225 182 206 147 179 133 C152 121 112 111 71 121 C69 54 120 0 185 0 Z',{viewBox:'0 0 366 346',fill:c.mid,el:'venn'}),Path(456,288,366,346,'M176 138 C142 163 125 194 127 239 C128 279 147 309 178 327 C132 361 67 353 30 312 C-7 269 -7 209 27 166 C67 116 124 107 176 138 Z',{viewBox:'0 0 366 346',fill:c.accent,el:'venn'}),Path(456,288,366,346,'M302 130 C363 166 382 239 347 294 C312 350 239 365 188 326 C149 297 126 258 136 218 C169 237 204 237 241 220 C277 202 296 170 302 130 Z',{viewBox:'0 0 366 346',fill:c.pale,el:'venn'}),icon(621,325,38,38,'AlarmClock',c.white),bold(600,364,80,38,'시간',23,{align:'center',color:c.white}),icon(518,484,35,35,'ShoppingCart',c.white),bold(497,521,80,37,'비용',23,{align:'center',color:c.white}),icon(699,524,40,35,'Crown',c.accent),bold(680,562,80,37,'품질',23,{align:'center',color:c.accent}));
 slides.push(S(19,'벤 다이어그램 레이아웃',es));
}
{
 const es=head('Project Roadmap','프로젝트 로드맵','단순한 나열을 넘어 데이터를 스토리텔링하는 도구로 활용하면 딱딱한 숫자의 이해를 도울 수 있습니다.\n넉넉한 여백을 활용해 답답함 없이 시원한 느낌을 연출해 보세요.');
 const names=['인지','탐색','구매','리뷰'],icons=['CircleAlert','MousePointerClick','ShoppingCart','MessageCircle'];
 const texts=[['아이디어를 구체적 기획안으로 만들어요.','세부 전략과 예산 인력을 확정하세요.','체계적인 실행 계획으로 구체화해요.'],['프로젝트 진행 방향을 명확히 제시하세요.','실현 가능한 구체적인 액션을 적어요.','성공 가능성을 명확히 보여주는 단계입니다.'],['막연한 계획이 아닌 실행안을 짜세요.','세부 일정을 수립해 로드맵을 그려요.','필요한 자원과 리소스를 배분합니다.'],['설계 도면을 그리듯 꼼꼼하게 기획하세요.','프로젝트 진행 상황과 미래 방향을 제시합니다.','목표 달성을 위한 논리적인 순서를 증명합니다.']];
 names.forEach((t,i)=>{const x=68+i*289;es.push(C(x+63,291,153,153,i%2?c.pale:c.paler,{el:'steps'}),icon(x+112,321,54,54,icons[i],c.accent),bold(x+63,382,153,43,t,24,{color:c.accent,align:'center'}),rect(x,467,279,186,i%2?c.pale:c.paler),...bullets(x+17,480,248,texts[i],18,53));if(i<3)es.push(arrow(x+275,329,20,77));});
 slides.push(S(20,'프로젝트 로드맵',es));
}
{
 const es=head('Compare Representative Products','대표 제품 비교','복잡한 표 대신 막대그래프 하나로 승부하세요.\n수치만 나열하면 지루하지만 높낮이가 있는 그래프는 흥미를 유발합니다.');
 es.push(rect(513,268,254,412,'#e0e6e4'),bold(389,290,125,39,'A 제품',24,{color:c.accent,align:'center'}),bold(767,290,114,39,'B 제품',24,{color:c.accent,align:'center'}));
 const names=['사용자 만족도','가격 대비 성능','디자인 및 품질','기능 다양성','고객 지원 및 서비스'],a=[82,75,88,90,85],b=[78,80,85,87,80],left=[158,199,85,71,141],right=[1080,1137,1194,1208,1137];
 names.forEach((t,i)=>{const y=349+i*62.3,co=[c.pale,'#cfd7d4',c.mid,c.accent,c.dark][i];es.push(rect(left[i],y,513-left[i],56,co),rect(767,y,right[i]-767,56,co),bold(left[i]+14,y+7,80,42,a[i]+'%',28,{font:'Inter',color:i<2?c.accent:c.white}),bold(right[i]-99,y+7,84,42,b[i]+'%',28,{font:'Inter',color:i<2?c.accent:c.white,align:'right'}),bold(525,y+8,230,42,t,24,{color:c.accent,align:'center'}));});
 slides.push(S(21,'대표 제품 비교',es));
}
function donutSegments(x,y,diam,values,colors,inner=.4){let a=-Math.PI/2;const r=diam/2;const e=[];for(let i=0;i<values.length;i++){let b=a+values[i]/100*Math.PI*2;let p=(q,rr)=>[r+Math.cos(q)*rr,r+Math.sin(q)*rr];const A=p(a,r),B=p(b,r),D=p(b,r*inner),E=p(a,r*inner);let d=`M ${A} A ${r} ${r} 0 ${b-a>Math.PI?1:0} 1 ${B} L ${D} A ${r*inner} ${r*inner} 0 ${b-a>Math.PI?1:0} 0 ${E} Z`;e.push(Path(x,y,diam,diam,d,{viewBox:`0 0 ${diam} ${diam}`,fill:colors[i],el:'chart-donut'}));a=b;}return e;}
{
 const es=head('Bar and Pie Charts','막대 및 원형 차트','전체 데이터 안에서 각 항목이 차지하는 비율을 보여줄 때\n원 그래프만큼 확실하고 직관적인 것은 없습니다.');
 es.push(L(639,267,639,660,c.line,1.2),...section(70,282,552,'주요 재무 지표 비교'),...section(659,282,553,'시장 점유율 비교'));
 const plot={x:126,y:379,w:478,h:237};[0,100,200,300].forEach(v=>{const y=plot.y+plot.h-v/300*plot.h;es.push(L(plot.x,y,604,y,'#c7ccca',.8),tx(72,y-14,46,30,String(v),18,{align:'right'}));});
 const vals=[300,250,90,60,50,35];const xpos=[143,215,302,374,461,533];vals.forEach((v,i)=>{let h=v/300*237;es.push(rect(xpos[i],616-h,56,h,i%2?c.dark:c.accent,{el:'chart-bar'}),tx(xpos[i]-5,584-h,66,32,String(v),18,{font:'Inter',color:i%2?c.dark:c.accent,align:'center'}));});['매출','영업이익','R&D 투자'].forEach((t,i)=>es.push(tx(139+i*159,622,135,32,t,18,{align:'center'})));
 es.push(...donutSegments(686,345,296,[20,10,70],[c.accent,c.dark,c.pale],.4));
 [[933,408,'회사 A','20%',c.accent],[957,493,'회사 B','10%',c.dark],[929,578,'기타','70%','#cfd5d3']].forEach(a=>es.push(C(a[0]-2,a[1]-2,4,4,c.line),L(a[0],a[1],1045,a[1],c.line,1.2),tx(1058,a[1]-13,72,30,a[2],18),bold(1115,a[1]-28,86,55,a[3],36,{font:'Inter',color:a[4]})));
 slides.push(S(22,'막대 및 원형 차트',es));
}
{
 const es=head('Trend Chart','꺾은선 그래프','데이터를 점으로 찍고 선으로 연결하여 윤곽을 드러냅니다.\n시간 경과에 따른 수치 변화를 파악하기 가장 좋습니다.');
 es.push(...section(69,278,738,'분기별 매출 현황'),rect(867,277,346,376,c.pale));
 const xs=[200,373,546,719],vals=[10,12,8,15];[0,5,10,15].forEach(v=>{let y=591-v/15*252;es.push(L(113,y,806,y,'#c8cecb',.8),tx(70,y-14,34,30,String(v),18,{align:'right'}));});es.push(L(113,339,113,591,'#b9c2be',.8),rect(200,339,519,252,'linear-gradient(to bottom,#dce4e1,#fff)',{clipPath:'polygon(0 33.333%,33.333% 20%,66.666% 46.666%,100% 0,100% 100%,0 100%)',el:'chart-line'}),Path(200,339,519,252,'M0 84 L173 50.4 L346 117.6 L519 0',{viewBox:'0 0 519 252',fill:'none',stroke:c.accent,strokeWidth:.8,el:'chart-line'}));
 vals.forEach((v,i)=>{let y=591-v/15*252;es.push(C(xs[i]-5,y-5,10,10,c.accent),tx(xs[i]-23,y-36,46,30,String(v),18,{font:'Inter',color:c.accent,align:'center'}),tx(xs[i]-42,595,84,35,`${i+1}분기`,18,{align:'center'}));});
 es.push(tx(893,306,294,165,'시간의 흐름에 따라 데이터가 어떻게 변하는지 보여주는 데 최적화된 페이지입니다. 막대가 양의 크기를 비교한다면 꺾은선은 변화의 추이를 이야기합니다. 점들을 연결한 선의 기울기를 통해 상승세인지 하락세인지 직관적으로 파악해 보세요.',18,{lineHeight:1.51}),L(880,493,1200,493,c.line,1.2),...bullets(892,520,300,['변화의 흐름을 한눈에 봐요.','상승과 하락이 보여요.','데이터를 점으로 찍고 선으로 연결해 흐름을 보여줍니다.'],18,27));
 slides.push(S(23,'꺾은선 그래프',es));
}
{
 const es=head('Organizational Chart','조직 구성도','회사의 위계질서를 파악하는 데 필수적인 레이아웃입니다.\n최상단에 결정권자를 배치하고 연결선을 통해 하위 부서로 이어지는 체계를 보여주세요.');
 es.push(L(639,334,639,367,c.line,2),L(167,368,1113,368,c.line,2));
 [167,481,797,1113].forEach(x=>es.push(L(x,368,x,440,c.line,2)));
 es.push(rect(514,277,252,56,'#000000'),bold(514,277,252,56,'대표이사',28,{color:c.white,align:'center',valign:'middle'}),rect(224,340,200,55,c.accent),rect(855,340,199,55,c.accent),bold(224,340,200,55,'전무이사',28,{color:c.white,align:'center',valign:'middle'}),bold(855,340,199,55,'상무',28,{color:c.white,align:'center',valign:'middle'}));
 [['영업팀','국내 영업 매니저','해외 영업 담당'],['마케팅팀','마케팅 실장','콘텐츠 마케터','퍼포먼스 마케터'],['기획팀','기획팀장','전략 기획 담당','서비스 기획자'],['CS팀','CS 매니저','운영 매니저']].forEach((list,i)=>{let x=[67,381,697,1012][i];es.push(rect(x,440,200,213,c.paler),rect(x,440,200,56,c.mid),bold(x,440,200,56,list[0],28,{color:c.white,align:'center',valign:'middle'}));list.slice(1).forEach((t,j)=>{es.push(tx(x+9,505+j*52,182,43,t,20,{align:'center',valign:'middle'}));if(j<list.length-2)es.push(L(x+9,548+j*52,x+190,548+j*52,c.line,1));});});
 slides.push(S(24,'조직 구성도',es));
}
{
 const es=head('Project Team Formation','프로젝트 팀 구성','긴 문장보다는 단추형 목록으로 간결하게 작성하는 것을 추천합니다.\n주요 업무를 짧게 끊어 나열하면 가독성이 좋아지고 많은 인원도 효율적으로 소개하죠.');es[0]=rect(36,47,1200,640,c.white);
 const roles=['기획팀 팀장','영업팀 본부장','마케팅팀 대리','디자인팀 선임'],names=['김미리','최미리','정미리','이미리'];
 roles.forEach((role,i)=>{let x=68+i*289;es.push(rect(x,277,279,376,i%2?c.pale:c.paler),C(x+55,298,169,169,'#e5e5e5',{stroke:i%2?'#e5e5e5':'#dce1df',strokeWidth:4,el:'person'}),tx(x+26,481,138,39,role,20,{weight:500}),bold(x+169,479,99,42,names[i],24),L(x+9,520,x+270,520,c.accent,.8),...bullets(x+21,533,246,['주요 업무를 짧게 요약해요.','역할과 책임을 명확히 해요.','전문 자격증 정보를 기입해요.','보유 기술과 강점을 소개해요.'],18,27));});
 slides.push(S(25,'프로젝트 팀 구성',es));
}
{
 const es=head('Cause and Effect','원인과 결과','결과를 유발한 근본적인 원인을 입력해 주세요.\n사건의 발생 배경과 진행 과정을 요약해 기재하면 읽는 이의 이해를 돕습니다.');
 es.push(...section(69,278,550,'원인'),...section(662,278,550,'결과'),rect(67,318,554,335,c.paler),rect(659,318,554,335,c.mid),bold(89,334,500,32,'근본적인 원인을 써보세요.',18,{color:c.accent}),bold(681,334,500,32,'원인으로 인한 결과를 상세히 적어요.',18));
 [1,2,3].forEach((n,i)=>{let x=89+i*190;es.push(C(x,376,133,133,'#e0e6e4',{el:'cycle'}),bold(x,376,133,133,`원인 ${n}`,24,{align:'center',valign:'middle',color:c.accent}));if(i<2)es.push(C(x+150,431,24,24,c.mid),bold(x+150,430,24,24,'+',18,{color:c.white,align:'center',valign:'middle'}));});
 es.push(arrow(631,447,20,78),C(681,376,133,133,c.white),icon(727,407,42,42,'CircleCheck',c.accent),bold(706,447,83,43,'결과',24,{align:'center',color:c.accent}),...bullets(834,390,352,['결과를 유발한 근본 원인을 적어요.','사건의 발생 배경과 과정을 요약해요.','여러 원인을 항목별로 나누어 봐요.','주요 원인을 중요도 순으로 둬요.'],18,27),tx(89,528,510,112,'결과를 유발한 근본적인 원인을 입력하고 사건의 발생 배경과 진행 과정을 요약해 기재하세요. 여러 가지 원인이 복합적이라면 항목을 나누어 나열하고, 주요 원인을 중요도 순서대로 배치하는 것이 좋습니다. 핵심 키워드 위주로 간결하게 작성하여 가독성을 높여야 합니다.',18,{lineHeight:1.51}),tx(681,528,510,112,'원인으로 인한 결과를 상세히 설명하고 원인과 결과 사이의 논리적 연관성을 보여주세요. 결과에 미친 긍정적 혹은 부정적 영향을 기술하고, 과거의 원인이 현재의 결과로 이어진 흐름을 정리합니다. 결론적으로 도출된 핵심 메시지를 한 문장으로 요약하면 완벽해지게 됩니다.',18,{lineHeight:1.51}));
 slides.push(S(26,'원인과 결과',es));
}
{
 const es=head('Item Comparison Table','항목별 대조표','비교할 대상과 객관적인 지표로 비교하여 강점을 부각하세요.\n기준이 되는 비교군의 데이터를 명확히 입력해야 합니다.');
 const cols=[{x:67,w:463,title:'BEFORE',bar:c.mid,fill:c.paler,rows:['개선 전 상황입니다.','핵심 데이터를 적어요.','비교 기준점을 잡아요.','비교군의 특징을 적어요.']},{x:540,w:200,title:'항목',bar:c.accent,fill:c.frame,rows:['항목 1','항목 2','항목 3','항목 4']},{x:750,w:463,title:'AFTER',bar:c.mid,fill:c.paler,rows:['개선된 후를 보여줘요.','차이점을 상세히 적어요.','변화의 폭을 강조해요.','합리적 결론을 도출해요.']}];
 cols.forEach((a,i)=>{es.push(rect(a.x,277,a.w,376,a.fill),rect(a.x,277,a.w,56,a.bar),bold(a.x,277,a.w,56,a.title,28,{color:c.white,align:'center',valign:'middle'}));a.rows.forEach((t,j)=>{es.push(tx(a.x+8,344+j*79,a.w-16,61,t,20,{weight:i===1?700:400,color:i===1?c.white:'#101010',align:'center',valign:'middle'}));if(j<3)es.push(L(a.x+7,412+j*79,a.x+a.w-7,412+j*79,i===1?c.white:c.line,1));});});
 slides.push(S(27,'항목별 대조표',es));
}
{
 const es=head('Formula Relationships Page','수식 관계 페이지','비교할 대상과 객관적인 지표로 비교하여 강점을 부각하세요.\n기준이 되는 비교군의 데이터를 명확히 입력해야 합니다.');
 const items=['결과값을 구성하는 요소들을 나열해 보세요.','각 항목이 더해져 창출되는 가치를 설명해요.','성공적인 결과를 만들기 위한 필수 조건입니다.','개별 요소가 모여 더 큰 힘을 발휘하게 돼요.','목표 달성을 위해 투입된 자원을 보여주세요.'];
 ['비용 절감','효율화','최적화'].forEach((t,i)=>{let x=68+i*383;es.push(rect(x,277,372,243,i===0?c.paler:c.pale),...section(x+15,292,342,t),L(x+10,342,x+362,342,c.line,1),...bullets(x+15,364,344,items,18,27));});
 es.push(rect(601,533,79,20,`linear-gradient(to bottom,#fff,${c.accent})`,{clipPath:'polygon(0 0,100% 0,50% 100%)',el:'flowchart'}),rect(67,560,1146,93,c.frame),...section(103,590,218,'수익 증대',c.dark),bold(333,589,861,47,'여러 기능이 통합되어 사용자에게 제공하는 궁극적인 혜택이 무엇인지 요약하세요.',23));
 slides.push(S(28,'수식 관계 페이지',es));
}
{
 const es=head('Positioning Map','포지셔닝 맵','가로축과 세로축으로 이루어진 좌표 위에 위치를 표시하는 페이지입니다.\n각 축의 양 끝에는 서로 반대되는 성격의 키워드를 배치해 공간을 정의하세요.');
 es.push(rect(67,268,1146,292,'#e0e6e4'),L(197,416,1071,416,c.line,1.3),L(634,326,634,506,c.line,1.3),bold(548,291,172,36,'높은 가격',18,{align:'center',color:c.accent}),bold(548,514,172,36,'낮은 가격',18,{align:'center',color:c.accent}),bold(96,402,100,37,'낮은 기술력',18,{color:c.accent}),bold(1091,402,111,37,'높은 기술력',18,{color:c.accent}),C(870,307,23,23,c.accent),bold(900,301,260,43,'Company A',26,{font:'Inter',color:c.accent}),C(582,366,23,23,c.dark),bold(441,358,141,43,'Company B',25,{font:'Inter',color:c.dark}),rect(67,560,1146,93,c.frame),bold(166,574,948,70,'회사 A는 고기술력과 고가격을 바탕으로 프리미엄 시장 공략,\nB는 중기술력과 합리적 가격으로 대중 시장 공략',24,{align:'center',lineHeight:1.35}));
 slides.push(S(29,'포지셔닝 맵',es));
}
{
 const es=head('SWOT Analysis','타사 SWOT 분석','목표 달성에 도움이 되는 내부적 요소인 강점을 명확히 적으세요.\n기업의 내부 역량을 객관적으로 진단합니다.');
 es.push(rect(67,268,1146,385,'#e0e6e4'),L(640,267,640,653,c.line,1.4),L(67,460,1213,460,c.line,1.4),bold(80,274,66,45,'강점',31,{color:c.accent}),tx(145,289,220,30,'Strength',18,{font:'Inter',color:c.accent}),bold(1143,274,66,45,'약점',31,{color:c.accent}),tx(1019,289,114,30,'Weakness',18,{font:'Inter',color:c.accent,align:'right'}),bold(80,500,66,45,'기회',31,{color:c.accent}),tx(145,515,220,30,'Opportunity',18,{font:'Inter',color:c.accent}),bold(1143,500,66,45,'위협',31,{color:c.accent}),tx(1022,515,111,30,'Threat',18,{font:'Inter',color:c.accent,align:'right'}));
 const texts=[['이곳에 회사 A의 내부 환경에서의 강점을 적어보세요.','이곳에 회사 A의 내부 환경에서의 강점을 적어보세요.','이곳에 회사 A의 내부 환경에서의 강점을 적어보세요.'],['이곳에 회사 A의 내부 환경에서의 약점을 적어보세요.','이곳에 회사 A의 내부 환경에서의 약점을 적어보세요.','이곳에 회사 A의 내부 환경에서의 약점을 적어보세요.'],['이곳에 회사 A의 외부 환경에서 비롯된 기회를 적어보세요.','이곳에 회사 A의 외부 환경에서 비롯된 기회를 적어보세요.','이곳에 회사 A의 외부 환경에서 비롯된 기회를 적어보세요.'],['이곳에 회사 A의 외부 환경에서 비롯된 위협을 적어보세요.','이곳에 회사 A의 외부 환경에서 비롯된 위협을 적어보세요.','이곳에 회사 A의 외부 환경에서 비롯된 위협을 적어보세요.']];
 texts.forEach((a,i)=>es.push(...bullets(i===3?781:i%2?815:82,i<2?334:560,i===3?432:i%2?390:499,a,18,27)));
 es.push(rect(567,387,146,147,c.frame),L(640,394,640,527,c.white,1.2),L(574,460,707,460,c.white,1.2));
 [['S',567,387],['W',640,387],['O',567,460],['T',640,460]].forEach(a=>es.push(bold(a[1],a[2],73,73,a[0],54,{font:'Inter',color:c.white,align:'center',valign:'middle'})));
 slides.push(S(30,'타사 SWOT 분석',es));
}
// Semantic content for reassembling the same source data through the Rhetis collection.
const libraries={
  4:{folder:'table',rows:[['항목','A사','B사'],['설립 연도','2080년','텍스트'],['사업 분야','텍스트를 넣어주세요','텍스트를 넣어주세요'],['직원 수','34명','56명'],['제품 및 서비스','텍스트를 넣어주세요','텍스트를 넣어주세요'],['주요 고객','텍스트를 넣어주세요','텍스트를 넣어주세요']]},
  9:{folder:'metric',items:[{name:'매출',fig:'500억 원'},{name:'영업이익',fig:'300억 원'},{name:'당기 순이익',fig:'10억 원'},{name:'누적 투자액',fig:'100억 원'},{name:'기업 가치',fig:'1조 원'}]},
  18:{folder:'card',items:[{name:'매출 증대',note:'좌우 대칭으로 시각적 균형을 맞춰요. 여러 특징을 동등하게 보여줍니다.'},{name:'비용 절감',note:'좌우 대칭으로 시각적 균형을 맞춰요. 여러 특징을 동등하게 보여줍니다.'},{name:'효율 개선',note:'좌우 대칭으로 시각적 균형을 맞춰요. 여러 특징을 동등하게 보여줍니다.'}]},
  19:{folder:'venn',items:[{name:'시간'},{name:'비용'},{name:'품질'}]},
  20:{folder:'steps',items:[{name:'인지',note:'아이디어를 구체적 기획안으로 만들어요. 세부 전략과 예산 인력을 확정하세요. 체계적인 실행 계획으로 구체화해요.'},{name:'탐색',note:'프로젝트 진행 방향을 명확히 제시하세요. 실현 가능한 구체적인 액션을 적어요. 성공 가능성을 명확히 보여주는 단계입니다.'},{name:'구매',note:'막연한 계획이 아닌 실행안을 짜세요. 세부 일정을 수립해 로드맵을 그려요. 필요한 자원과 리소스를 배분합니다.'},{name:'리뷰',note:'설계 도면을 그리듯 꼼꼼하게 기획하세요. 프로젝트 진행 상황과 미래 방향을 제시합니다. 목표 달성을 위한 논리적인 순서를 증명합니다.'}]},
  21:{folder:'table',rows:[['항목','A 제품','B 제품'],['사용자 만족도','82%','78%'],['가격 대비 성능','75%','80%'],['디자인 및 품질','88%','85%'],['기능 다양성','90%','87%'],['고객 지원 및 서비스','85%','80%']]},
  22:{folder:'chart-bar',max:300,values:[300,250,90,60,50,35],labels:['매출 A','매출 B','영업이익 A','영업이익 B','R&D 투자 A','R&D 투자 B'],secondary:[{folder:'chart-donut',values:[20,10,70],labels:['회사 A','회사 B','기타']}]},
  23:{folder:'chart-line',max:15,values:[10,12,8,15],labels:['1분기','2분기','3분기','4분기']},
  24:{folder:'hierarchy',root:'대표이사',items:[{name:'영업팀',leaves:['국내 영업 매니저','해외 영업 담당']},{name:'마케팅팀',leaves:['마케팅 실장','콘텐츠 마케터','퍼포먼스 마케터']},{name:'기획팀',leaves:['기획팀장','전략 기획 담당','서비스 기획자']},{name:'CS팀',leaves:['CS 매니저','운영 매니저']}]},
  27:{folder:'table',rows:[['BEFORE','항목','AFTER'],['개선 전 상황입니다.','항목 1','개선된 후를 보여줘요.'],['핵심 데이터를 적어요.','항목 2','차이점을 상세히 적어요.'],['비교 기준점을 잡아요.','항목 3','변화의 폭을 강조해요.'],['비교군의 특징을 적어요.','항목 4','합리적 결론을 도출해요.']]},
  28:{folder:'architecture',items:[{name:'비용 절감',chips:['결과값을 구성하는 요소들을 나열해 보세요.','각 항목이 더해져 창출되는 가치를 설명해요.','성공적인 결과를 만들기 위한 필수 조건입니다.','개별 요소가 모여 더 큰 힘을 발휘하게 돼요.','목표 달성을 위해 투입된 자원을 보여주세요.']},{name:'효율화',chips:['결과값을 구성하는 요소들을 나열해 보세요.','각 항목이 더해져 창출되는 가치를 설명해요.']},{name:'최적화',chips:['개별 요소가 모여 더 큰 힘을 발휘하게 돼요.','목표 달성을 위해 투입된 자원을 보여주세요.']}]}
};
for(const [n,library]of Object.entries(libraries))slides[Number(n)-1].library=library;
export default {id:'008',title:'Sage Business Presentation',slides};
