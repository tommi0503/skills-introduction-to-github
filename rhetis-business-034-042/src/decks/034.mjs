import {T,R,C,L,PH,S,P,slide} from '../primitives.mjs';

const ink='#222222', purple='#7952c8', pale='#a78bdf', gray='#999999';
const bg='linear-gradient(102deg,#a98ae7 0%,#7751d2 75%,#6945c5 100%)';
const titleGradient={background:'linear-gradient(90deg,#ac8be2 0px,#7651c6 290px)',backgroundClip:'text',WebkitBackgroundClip:'text',WebkitTextFillColor:'transparent'};
const display='Gmarket Sans';
const tx=(x,y,w,h,s,z=24,c=ink,b=400,o={})=>T(x,y,w,h,s,z,c,b,{lineHeight:1.18,...o});
function header(){return [tx(67,52,280,18,'ⓒ MIRICOMPANY ALL RIGHTS RESERVED.',12,ink,400,{tracking:-.25}),tx(1060,54,154,16,'www.miricompany.com',12,ink,400,{align:'right'})];}
function twoToneTitle(x,y,lead,tail,leadW,total=800){return [tx(x,y,leadW,70,lead,50,ink,300,{font:display,tracking:-2.4}),tx(x+leadW,y,total-leadW,70,tail,50,purple,700,{font:display,tracking:-1.6,style:titleGradient})];}
function companyCard(x,y,label,side){let iconX=side==='left'?x+289:x+44;let textX=side==='left'?x+37:x+194;let align=side==='left'?'right':'left';return [R(x,y,452,159,'#fff',15,'none',1,{shadow:'0 9px 17px rgba(0,0,0,.14)'}),PH(iconX,y+20,120,120,60),tx(textX,y+40,221,38,label+' COMPANY',26,ink,700,{font:display,align,tracking:-.5}),tx(textX,y+89,221,44,'경쟁사의 특징에 관한 내용을\n입력해 주세요.',15,gray,400,{align,lineHeight:1.1})];}
function chevron(x,y,w,h,dir){const paths={up:'M8 31 L40 6 L72 31',down:'M8 6 L40 31 L72 6',left:'M31 7 L7 40 L31 73',right:'M7 7 L31 40 L7 73'};return S(x,y,w,h,`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${dir==='up'||dir==='down'?'80 40':'40 80'}"><path d="${paths[dir]}" fill="none" stroke="#e8e1f2" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/></svg>`);}
const strengthCopy='우리 회사만이 가지고 있는 경쟁력을 어필해 주세요.';
function strength(n,y){return [R(649,y,82,83,'#fff',8,'none',1,{shadow:'0 8px 7px rgba(0,0,0,.22)'}),tx(667,y+12,47,25,'장점',20,purple,700,{font:display,align:'center'}),tx(661,y+36,57,44,String(n).padStart(2,'0'),35,purple,700,{font:display,align:'center',tracking:-1}),tx(790,y+4,430,31,`우리 회사의 장점 ${String(n).padStart(2,'0')} 입니다.`,22,'#fff',500),...[0,1,2,3].flatMap(i=>[C(791,y+43+i*17,5,'#fff'),tx(805,y+37+i*17,415,20,strengthCopy,15,'#fff',400,{lineHeight:1.05,tracking:-.15})])];}
function testimonial(cx,name){return [C(cx-93,273,188,purple),PH(cx-96,270,187,187,93.5),tx(cx-167,501,334,48,name,33,purple,700,{font:display,align:'center',tracking:-1,style:titleGradient}),tx(cx-173,545,346,77,'"거래처의 후기에 대해 적어주세요.\n자사의 성과나 기여도 등을\n구체적으로 입력하면 좋습니다."',20,ink,500,{align:'center',lineHeight:1.05,tracking:-.7})];}

export default {id:'034',title:'보라색 입체 비즈니스 프레젠테이션',slides:[
 slide('slide_06','특별한 장점이 있어요',[
  R(692,0,588,720,bg),...header().map((n,i)=>i===1?{...n,color:'#fff'}:n),
  PH(-20,194,79,77,39),PH(1046,476,235,244,25),
  tx(67,313,311,76,'특별한 장점이',50,purple,700,{font:display,tracking:-1.8,style:titleGradient}),tx(377,313,225,76,'있어요',51,ink,300,{font:display,tracking:-3}),
  tx(67,527,505,48,'우리 회사의 장점에 대한 보충 내용을 적어주세요.\n우리 회사의 장점에 대한 보충 내용을 적어주세요.',14,gray,400,{lineHeight:1.15,tracking:-.3}),
  strength(1,134),strength(2,333),strength(3,535)
 ]),
 slide('slide_07','남들과는 다른 미리의 컨셉',[
  PH(1044,-116,298,306,145),...header(),
  ...twoToneTitle(319,139,'남들과는 다른','미리의 컨셉',311,700),
  chevron(599,218,82,44,'up'),tx(557,232,166,28,'Quality High',21,gray,800,{align:'center'}),
  chevron(598,618,83,45,'down'),tx(554,631,172,28,'Quality Low',21,gray,800,{align:'center'}),
  chevron(126,401,39,80,'left'),tx(86,422,74,53,'Cost\nLow',21,gray,800,{lineHeight:.95}),
  chevron(1111,400,39,81,'right'),tx(1141,422,91,53,'Cost\nHigh',21,gray,800,{lineHeight:.95}),
  companyCard(181,277,'A','left'),companyCard(646,277,'B','right'),companyCard(181,447,'C','left'),companyCard(646,447,'D','right')
 ]),
 slide('slide_08','만족도 98% 달성',[
  PH(1040,-119,300,304,146),PH(-25,605,123,88,19),...header(),
  ...twoToneTitle(439,143,'만족도','98% 달성',153,600),
  testimonial(253,'A 컴퍼니'),testimonial(643,'B 상사'),testimonial(1032,'C 물산')
 ]),
 slide('slide_09','THANK YOU',[
  PH(-95,-90,587,628,35),PH(1007,-26,128,150,38),PH(942,420,333,287,54),PH(49,586,105,75,13),
  P(522,148,232,40,'miricanvas.com','rgba(255,255,255,.35)','#fff',21,{stroke:'#fff',sw:1,weight:500,tracking:.1,style:{fontFamily:display}}),
  tx(355,258,570,132,'THANK',101,'#fffbb0',900,{font:'Montserrat',align:'center',tracking:1,lineHeight:1}),
  tx(438,360,402,132,'YOU',101,'#fff',900,{font:'Montserrat',align:'center',tracking:1,lineHeight:1}),
  tx(441,485,398,31,'미리 컴퍼니 신미리',24,'#fff',500,{align:'center',tracking:-.5}),
  tx(414,518,452,42,'연락처 | 010 . 0000 . 0000\n이메일 | miricompany.miri.com',16,'#fff',400,{align:'center',lineHeight:1.15,tracking:-.1})
 ],bg)
]};
