// Semantic reassembly: no replica coordinates or primitive-node wrappers.
const title='타이틀을 입력하세요';
const lead='전달하고자 하는 핵심 내용을 입력하세요. 간결한 문장으로 발표 내용을 명확하게 전달해보세요.';
const example='이것은 예시 문구입니다. 실제 내용이 들어갈 영역을 확인하기 위한 텍스트입니다.';
const keyword='키워드를 입력하세요';
const callout='해당 키워드에 대한 내용을 간략하게 입력하세요. 핵심 내용을 요약해 보세요.';
const entry=(n,name,blocks,rest={})=>({id:'slide_'+String(n).padStart(2,'0'),title:name,kicker:'심플한 발표 PPT',blocks,...rest});
export default [
 entry(1,'심플한 발표 PPT',[],{cover:true,kicker:'2099 - 01 - 01',lead:': 타이틀을 보충 설명하는 부제를 입력하세요.',meta:'email@email.com      김미리'}),
 entry(2,'Contents',[{kind:'agenda',at:[1,7,2,5],items:['이미지 레이아웃','텍스트 레이아웃','데이터 레이아웃','표 레이아웃','인포그래픽 레이아웃'].map((name,i)=>({mark:'0'+(i+1),name}))}]),
 entry(3,title,[{kind:'cards',at:[1,6,2,4],variant:'quiet',items:[{fig:'01',name:title,note:'간지입니다. 해당 섹션에 대한 내용을 간략하게 설명해 주세요.'}]},{kind:'cards',at:[8,4,2,4],items:[{name:'',icon:'lightbulb'}]}],{kicker:title}),
 entry(4,title,[{kind:'image',at:[1,6,1,6]},{kind:'list',at:[7,6,2,5],variant:'check',items:Array.from({length:3},()=>({name:'핵심 내용을 요약하여 입력하세요'}))}],{kicker:'01 이미지 레이아웃',lead:example}),
 entry(5,title,[{kind:'cards',at:[1,4,1,4],variant:'quiet',items:[{name:'',note:'전달하고자 하는 핵심 내용을 입력하세요.\n간결한 문장으로 발표 내용을 명확하게 전달해보세요.'}]},{kind:'image',at:[5,8,1,6]}],{kicker:'01 이미지 레이아웃'}),
 entry(6,'이미지 레이아웃',[{kind:'cards',at:[2,10,1,6],variant:'line',items:[{name:title,note:example,image:true,imageHeight:200},{name:title,note:example,image:true,imageHeight:200}]}],{kicker:'01 이미지 레이아웃'}),
 entry(7,title,[{kind:'cards',at:[1,12,2,5],items:Array.from({length:4},()=>({name:'Keyword',image:true,imageHeight:180}))}],{kicker:'01 이미지 레이아웃',lead}),
 entry(8,title,[{kind:'quote',at:[2,10,2,4],text:'강조하고 싶은 내용을 입력하세요.중요한 메시지나 인용구를 입력하세요.\n텍스트의 크기와 색상을 조절하여 강조하세요.'}],{kicker:'02 텍스트 레이아웃',lead}),
 entry(9,title,[{kind:'cards',at:[2,10,2,4],variant:'quiet',items:[{name:keyword,icon:'lightbulb',note:'이것은 레이아웃과 가독성을 확인하기 위한 예시 문장입니다. 실제 내용이 들어가기 전 임시로 배치되는 텍스트이며, 문단의 길이와 줄바꿈, 글자 크기, 여백 등을 미리 확인하는 데 사용됩니다.'},{name:keyword,icon:'list-todo',note:'이것은 예시 문구입니다. 실제 내용이 들어갈 영역을 확인하기 위한 더미 텍스트입니다. 제목과 본문, 강조 문구의 배치와 가독성을 검토할 수 있습니다.'}]}],{kicker:'02 텍스트 레이아웃'}),
 entry(10,title,[{kind:'cards',at:[1,12,2,5],items:[{kick:'01',name:keyword,note:'이것은 더미 텍스트입니다. 제목과 본문, 강조 문구의 배치와 가독성을 검토할수 있습니다.'},{kick:'02',name:keyword,note:'이것은 예시 문구입니다. 실제 내용이 들어갈 영역을 확인하기 위한 더미 텍스트입니다. 제목과 본문, 강조 문구의 배치와 가독성을 검토할 수 있습니다.'},{kick:'03',name:keyword,note:'제목과 본문, 강조 문구의 배치와 가독성을 검토할 수 있는 예시 문구입니다. 실제 내용이 들어갈 영역을 확인하기 위한 더미 텍스트입니다.'}]}],{kicker:'02 텍스트 레이아웃'}),
 entry(11,title,[{kind:'bars',at:[1,7,2,5],horizontal:true,max:400,items:[{name:'1Q',value:280},{name:'2Q',value:220},{name:'3Q',value:340},{name:'4Q',value:365}]},{kind:'metrics',at:[9,4,2,2],items:[{name:'항목 01',fig:'42.8%'}]},{kind:'metrics',at:[9,4,4,2],items:[{name:'항목 02',fig:'8,570'}]}],{kicker:'03 데이터 레이아웃',lead}),
 entry(12,title,[{kind:'donuts',at:[2,5,1,6],items:[{name:'타이틀 입력',value:45}]},{kind:'list',at:[8,4,2,4],variant:'divided',items:[{name:'항목 01',note:'45%'},{name:'항목 02',note:'25%'},{name:'항목 03',note:'15%'},{name:'항목 04',note:'15%'}]}],{kicker:'03 데이터 레이아웃',lead}),
 entry(13,title,[{kind:'table',at:[1,12,1,6],headers:['-','항목','항목','항목','항목'],rows:Array.from({length:5},()=>['항목',...Array(4).fill('내용을 입력하세요')])}],{kicker:'04 표 레이아웃'}),
 entry(14,title,[{kind:'table',at:[1,6,1,6],headers:['항목','내용을 입력하세요'],rows:Array.from({length:6},(_,i)=>['키워드 '+(i+1),'내용을 입력하세요'])},{kind:'list',at:[7,6,1,6],variant:'check',items:Array.from({length:3},()=>({name:callout}))}],{kicker:'04 표 레이아웃',lead}),
 entry(15,'인포그래픽 레이아웃',[{kind:'cards',at:[1,4,1,6],column:true,variant:'quiet',items:[{name:'Keyword',note:example,icon:'rocket'},{name:'Keyword',note:example,icon:'globe'}]},{kind:'cards',at:[5,4,2,4],items:[{name:'',icon:'monitor-cog'}]},{kind:'cards',at:[9,4,1,6],column:true,variant:'quiet',items:[{name:'Keyword',note:example,icon:'calendar-check'},{name:'Keyword',note:example,icon:'coins'}]}],{kicker:'05 인포그래픽 레이아웃'}),
 entry(16,title,[{kind:'cards',at:[1,12,1,6],variant:'quiet',items:['shield-check','clipboard-list','pencil-ruler'].map(icon=>({name:'Keyword',note:example,icon}))}],{kicker:'05 인포그래픽 레이아웃'}),
 entry(17,title,[{kind:'cards',at:[1,4,1,6],items:[{name:'Keyword',icon:'settings'}]},{kind:'cards',at:[6,7,1,6],column:true,variant:'quiet',items:['building-2','user-search','messages-square'].map(icon=>({name:'',note:callout,icon}))}],{kicker:'05 인포그래픽 레이아웃'}),
 entry(18,title,[{kind:'timeline',at:[1,12,2,4],items:Array.from({length:4},(_,i)=>({kick:'0'+(i+1),name:'해당 단계에 대한',note:'내용을 입력하세요'}))}],{kicker:'03 인포그래픽 레이아웃',lead}),
 entry(19,'Q&A',[{kind:'cards',at:[1,6,2,4],variant:'quiet',items:[{name:'질의응답',note:'궁금하신 사항이 있으시면\n편하게 질문해 주세요.'}]},{kind:'cards',at:[8,4,1,5],items:[{name:'',icon:'mic'}]}],{kicker:title}),
 entry(20,'경청해주셔서\n감사합니다',[],{cover:true,kicker:'2099 - 01 - 01',meta:'email@email.com      김미리'})
];
