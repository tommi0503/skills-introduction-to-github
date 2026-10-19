import{T,R,L,S,slide}from'../primitives.mjs';
const INK='#333974',BG='#fcfdf5';
const tx=(x,y,w,h,text,size=20,weight=400,opts={})=>T(x,y,w,h,text,size,INK,weight,{lineHeight:1.35,...opts});
const footer=R(0,713,1280,7,INK);
const grid=S(43,485,1194,160,`<svg viewBox="0 0 1194 160" preserveAspectRatio="none"><rect width="1194" height="160" fill="#fbfcf7"/>${Array.from({length:16},(_,i)=>`<path d="M${3+i*79.4} 0V160" stroke="#62668f" stroke-width="3.3"/>`).join('')}${Array.from({length:15},(_,i)=>`<path d="M0 ${10+i*10.7}H1194" stroke="#777a99" stroke-width=".5"/>`).join('')}</svg>`);
export default{id:'077',title:'심플한 사업 결과 보고서',slides:[
slide('slide_01','Business Presentation',[tx(975,44,75,30,'DATE :',18),R(1036,41,200,31,'#fffef5'),L(967,73,1236,73,INK,1.2),tx(47,219,700,47,'심플한 사업 결과 보고서',34,600,{tracking:-1.3}),tx(44,274,1150,207,'BUSINESS\nPRESENTATION',92,900,{font:'Pretendard',lineHeight:.9,tracking:-.2}),L(967,431,1236,431,INK,1.1),L(1217,418,1236,431,INK,1.1),grid,tx(43,671,265,22,'MIRICOMPANY',14,300),tx(430,671,420,22,'MIRIKIM@MIRICOMPANY.COM',14,300,{align:'center'}),tx(971,671,265,22,'MIRICOMPANY.COM',14,300,{align:'right'}),footer],'#f2f7f8'),
slide('slide_02','Index',[L(49,71,277,71,INK,4.5),tx(51,78,323,77,'INDEX',64,900,{font:'Pretendard',tracking:-.6}),tx(53,177,327,100,'이곳에 부제목격의 텍스트를 입력해 주세요. 해\n당 페이지를 요약하는 내용도 좋습니다. 더미텍\n스트를 넣을 수 있는 곳입니다.',18,300,{lineHeight:1.5}),Array.from({length:8},(_,i)=>{let y=67+i*71.5;return[R(460,y+25,24,24,i<5?'#d3e2ee':'transparent',0,INK,1.2),i<5?tx(509,y+19,343,40,['사업 개요','세부 사업 내용','숫자로 보는 사업 성과','표로 보는 사업 성과','향후 계획'][i],26,600,{tracking:-.6}):null,i<5?tx(864,y+27,373,27,i===1?'이곳에 목차에 대한 설명을 간결하게 입력해 주세요.':'해당 목차에 대한 설명을 요약해 주세요.',16,300):null,L(440,y+72,1241,y+72,INK,.8)]}),footer],BG)
]};
