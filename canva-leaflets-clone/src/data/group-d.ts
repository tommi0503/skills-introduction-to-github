import type {BrochureDraft,Element} from '../model'
import {T,B,I,C,L,IC,P,VP} from '../primitives'

const navy='#172651',sky='#7ab4e6',orange='#e89841',blue='#2a67b8',peach='#fcc1b1',green='#236557',lilac='#e3bfed'
const turquoise='#57aeba',brown='#66513d',pale='#edf8fa',cream='#fffef9',marketBrown='#6f3a1a'
const centered=(x:number,y:number,w:number,h:number,text:string,size:number,extra:Partial<Element>={})=>T(x,y,w,h,text,size,{align:'center',...extra})
const dotted=(x:number,y:number,w:number,color='#bcdde2')=>B(x,y,w,1,'transparent',{border:`1px dotted ${color}`})
function flower(x:number,y:number,w:number,color=orange):Element{
 const pts=Array.from({length:240},(_,i)=>{const a=i*Math.PI*2/240,r=w*(.35+.15*Math.cos(6*(a-Math.PI/6)));return[x+w/2+Math.cos(a)*r,y+w/2+Math.sin(a)*r]});return P(pts,color,0,color)
}
function roof(x:number,y:number,w:number,h:number):Element[]{
 const base=VP(x,y,w,h,`M 0 ${h*.45} Q ${w*.23} ${h*.41} ${w*.2} 0 L ${w*.25} 0 L ${w*.25} ${h*.12} L ${w*.75} ${h*.12} L ${w*.75} 0 L ${w*.8} 0 Q ${w*.77} ${h*.41} ${w} ${h*.45} L ${w} ${h*.66} Q ${w*.5} ${h*1.3} 0 ${h*.66} Z`,{fill:'#9ba1bd',color:'#343342',strokeWidth:3});
 return[base,VP(x+5,y+7,w-10,h-12,`M 0 ${(h-12)*.48} Q ${(w-10)*.27} ${(h-12)*.35} ${(w-10)*.24} 0 L ${(w-10)*.76} 0 Q ${(w-10)*.73} ${(h-12)*.35} ${w-10} ${(h-12)*.48} Q ${(w-10)*.5} ${h-12} 0 ${(h-12)*.48} Z`,{fill:'#858eae',color:'#343342',strokeWidth:2}),...Array.from({length:7},(_,i)=>L(x+w*(.24+i*.087),y+h*.15,2,h*.62,'#343342'))]
}
const studyNotes=['사진 및 세밀한 새·책·나무 일러스트는 원래 영역과 윤곽을 유지한 연한 회색 placeholder로 처리했습니다.','한글 본문은 판독 가능한 원문을 실제 텍스트로 복원했습니다. 서체의 정확한 원본 파일이 없어 로드한 고운돋움·Pretendard를 사용했습니다.']

const l15s01:Element[]=[
 B(0,0,1600,1131,navy),B(0,0,533,1131,sky),
 T(54,110,430,34,'지원자격 셀프 체크리스트',23,{color:'#fff',weight:600}),L(54,146,426,1,'#f5f7fa'),
 ...['만 19 세 ~ 39 세 청년이다.','지역 거주 또는 창업 예정이다.','예비 창업자거나 창업 3년 이내다.','국세 · 지방세 체납이 없다.','동일 사업 중복 수혜 이력이 없다.'].flatMap((t,i)=>[
  B(56,195+i*57,425,56,'#fff'),B(84,214+i*57,19,19,'transparent',{border:'3px solid #111'}),L(129,195+i*57,3,56,sky),T(137,208+i*57,338,36,t,22,{lineHeight:1.4})]),
 T(54,500,444,35,'*지원사업은 5가지 모두 해당되어야 합니다.',21,{color:'#fff',weight:600}),
 B(54,761,426,134,'#fff'),C(78,783,92,91,'QR코드',20,navy,{radius:13,color:'#fff',weight:500}),
 T(191,782,284,102,'청년창업지원 안내\n상세 내용을 확인하시려면\nQR코드를 스캔해 주세요.',23,{weight:600,lineHeight:1.37}),
 B(54,906,425,135,'#fff'),B(78,928,91,91,navy,{radius:13}),IC(105,951,44,44,'PhoneCall','#fff',{strokeWidth:2.6}),
 T(190,927,280,102,'청년창업지원 상담안내\n운영시간\n오전 09:00 ~ 오후 17:00',23,{weight:600,lineHeight:1.36}),
 flower(762,444,96),centered(676,572,270,101,'청년 창업가와\n함께합니다.',39,{font:'NanumSquareRound',weight:800,color:'#fff',lineHeight:1.15}),
 centered(641,692,339,42,'www.umchungjoeun.kr',23,{color:'#fff'}),
 centered(1145,112,357,40,'YOUTH-STARTUP',24,{color:'#fff',letterSpacing:5.5}),
 T(1184,169,337,190,'청년창업\n지원안내',80,{font:'NanumSquareRound',color:'#fff',lineHeight:1.14,weight:800}),
 I(1107,662,410,334,{label:'창업가와 노트북·대시보드 복잡 일러스트',clipPath:'polygon(7% 0,96% 0,96% 60%,100% 88%,96% 100%,5% 100%,0 73%,5% 70%)'}),B(1067,996,478,22,sky),
]
const l15s02:Element[]=[
 B(0,0,1600,1131,'#152651'),...([267,800,1333].flatMap((x,i)=>[flower(x-21,54,42),centered(x-200,100,400,45,['지원내용','신청절차','자주묻는 질문'][i],30,{font:'NanumSquareRound',weight:800,color:'#fff'})])),
 B(54,195,427,824,'#fff'),L(153,195,3,824,navy),L(54,467,427,3,navy),L(54,743,427,3,navy),
 centered(62,313,83,47,'지원금',23),T(164,254,300,162,'최대 1,000만 원\n시제품 제작\n초기 운영비\n협약 후 2 회 분할 지급\n사용 내역 정산 필수.',22,{lineHeight:1.37}),
 centered(62,589,83,47,'공간',23),T(164,530,299,163,'입주 1 년 무상\n멘토링 12 회\n청년창업소 사무 공간\n세무 · 마케팅 · 투자분야\n멘토 매칭.',22,{lineHeight:1.37}),
 centered(62,865,83,47,'마케팅',23),T(164,821,300,139,'바우처 지원 300만 원\n온라인 광고\n브랜딩, 전시회 참가비\n바우처 지급.',22,{lineHeight:1.37}),
 ...['공고확인\n홈페이지에서 모집 공고 확인','신청 접수\n사업계획서 양식 작성 후 제출','서류 심사\n요건 확인과 계획서 평가(2주)','발표 심사\n10분 발표+질의 응답','선발 협약\n최종 선발 후 협약 체결','지원 개시\n지원금 지급, 공간 입주'].flatMap((t,i)=>[
  B(587,195+i*88.4,427,87,'#dfecfd'),L(677,195+i*88.4,3,87,navy),centered(594,226+i*88.4,72,39,String(i+1),23),T(687,207+i*88.4,318,66,t,22,{lineHeight:1.4})]),
 T(587,755,420,33,'유의사항',23,{color:'#fff',weight:600}),L(587,791,426,1,'#fff'),T(587,815,427,122,'지원금 목적 외 사용 시 환수\n중간 점검 미참여 시 협약 해지\n본 금액 및 일정은 지원팀에 따라 차등지급',22,{color:'#fff',weight:600,lineHeight:1.6}),
 ...['팀 창업도 되나요?','대표자가 청년이면 팀 신청 가능해요.','타 지역 사업자인데요?','협약 전까지 한빛시로 이전하면 돼요.','탈락하면 다시 못 하나요?','다음 회차 재도전 가능 · 피드백 제공'].flatMap((t,i)=>[
 B(1119,195+i*74.8,427,73.2,i%2?'#fff':'#dfecfd'),L(1209,195+i*74.8,3,73.2,navy),centered(1126,215+i*74.8,73,39,i%2?'A':'Q',23),T(1219,216+i*74.8,322,39,t,22,{lineHeight:1.4})]),
 I(1128,702,372,349,{label:'상담자·노트북·메시지 복잡 일러스트',clipPath:'polygon(5% 0,45% 0,53% 17%,80% 19%,100% 100%,25% 100%,16% 64%,1% 64%)'})
]

function seal(x:number,y:number):Element[]{return[
 B(x,y,90,90,blue,{radius:'50%',border:`3px solid ${peach}`}),
 ...[22,34,45,56,68].map(z=>L(x+z,y+5,2.5,80,peach)),...[22,34,45,56,68].map(z=>L(x+5,y+z,80,2.5,peach)),
 B(x+35,y+22,20,46,blue),L(x+44,y+4,2.5,80,peach),L(x+24,y+44,42,2.5,peach)
]}
const l16s01:Element[]=[
 B(0,0,800,1236,blue),B(800,0,800,1236,peach),L(0,197,800,3,peach),...seal(354,153),
 T(89,959,610,108,'INFO &\nCONTACT',50,{font:'Poppins',weight:900,color:peach,lineHeight:.97,letterSpacing:-1.5}),
 T(89,1078,605,50,'문의 : 라라나여행사',32,{color:peach,weight:600}),
 T(875,132,665,125,'HI',116,{font:'Poppins',weight:900,color:blue,lineHeight:1,letterSpacing:-5}),
 T(875,235,680,130,'WELCOME',119,{font:'Poppins',weight:900,color:blue,lineHeight:1,letterSpacing:0}),
 T(875,340,680,130,'TO KOREA',119,{font:'Poppins',weight:900,color:blue,lineHeight:1,letterSpacing:0}),
 T(890,468,650,54,'K-CULTURE',50,{font:'Poppins',weight:900,color:blue,lineHeight:1,letterSpacing:-1.7}),
 T(890,527,650,57,'TOUR GUIDE BOOK',41,{font:'Poppins',weight:400,color:blue,lineHeight:1}),
 T(890,596,650,50,'살아 숨 쉬는 한국문화 직접 느껴보세요',39,{color:blue,weight:700,letterSpacing:-.7}),
 I(800,766,800,470,{label:'한국 전통 궁궐 지붕·문 흑백 사진'})
]
const l16s02:Element[]=[
 B(0,0,800,1236,lilac),B(800,0,800,1236,green),I(593,0,207,1236,{label:'한복 체험 인물 흑백 세로 사진'}),I(870,0,660,183,{label:'한식 반찬 상차림 사진'}),
 T(122,261,438,185,'PRO\nGRAM',109,{font:'Poppins',weight:900,color:green,lineHeight:.82,letterSpacing:0}),
 T(902,266,651,189,'HIGH\nLIGHTS',109,{font:'Poppins',weight:900,color:lilac,lineHeight:.82,letterSpacing:0}),
 T(120,511,135,117,'01',112,{font:'Poppins',weight:800,color:green,lineHeight:1,letterSpacing:-2}),T(250,541,328,70,'한복 체험',49,{weight:800,color:green,letterSpacing:-2}),L(119,625,474,1,green),
 T(127,648,450,92,'전통 궁궐 배경 포토존\n남녀노소 누구나 착용 가능',30,{color:green,weight:700,lineHeight:1.25,letterSpacing:-1}),C(126,741,182,38,'체험시간 : 1시간',27,green,{radius:0,color:lilac,weight:600}),
 T(116,851,146,116,'02',112,{font:'Poppins',weight:800,color:green,lineHeight:1,letterSpacing:-2}),T(263,882,321,66,'부채 만들기',49,{weight:800,color:green,letterSpacing:-2}),L(114,965,479,1,green),
 T(123,988,452,90,'직접 그려보는 전통 문양\n소장 가치 100%',30,{color:green,weight:700,lineHeight:1.25,letterSpacing:-1}),C(123,1081,182,38,'체험시간 : 1시간',27,green,{radius:0,color:lilac,weight:600}),
 T(911,511,153,117,'03',112,{font:'Poppins',weight:800,color:lilac,lineHeight:1,letterSpacing:-2}),T(1071,541,462,69,'한식 쿠킹 클래스',45,{weight:800,color:lilac,letterSpacing:-1.3}),L(921,625,565,1,lilac),
 T(921,648,606,92,'김치, 비빔밥 직접 만들어 보기\n푸드 사진도 인생샷 각!',30,{color:lilac,weight:700,lineHeight:1.25,letterSpacing:-1}),C(921,741,182,38,'체험시간 : 1시간',27,lilac,{radius:0,color:green,weight:600}),
 T(912,851,154,116,'04',112,{font:'Poppins',weight:800,color:lilac,lineHeight:1,letterSpacing:-2}),T(1070,888,481,61,'K-뷰티 아이돌 메이크업',41,{weight:700,color:lilac,letterSpacing:-1.5}),L(911,965,565,1,lilac),
 T(921,988,630,90,'프로 메이크업 아티스트와 함께하는 K-아이돌 룩\n셀카존에서 바로 촬영 가능한 뷰티 부스 운영',30,{color:lilac,weight:700,lineHeight:1.25,letterSpacing:-1.4}),C(921,1081,182,38,'체험시간 : 1시간',27,lilac,{radius:0,color:green,weight:600})
]

const l17s01:Element[]=[
 B(0,0,1600,1131,'#fbffff'),...Array.from({length:25},(_,i)=>L(i*22,0,1,1006,'#f1f5f5')),...Array.from({length:46},(_,i)=>L(0,i*22,534,1,'#f1f5f5')),
 B(582,82,436,988,pale,{radius:17}),
 I(130,177,130,105,{label:'책을 든 새 복잡 일러스트',clipPath:'polygon(10% 30%,40% 30%,64% 0,91% 3%,100% 64%,66% 100%,0 87%)'}),
 centered(85,327,360,80,'동네 도서관에서\n보내는 편안한 하루,',27,{color:brown,weight:700,lineHeight:1.25,letterSpacing:-1.1}),
 centered(76,433,375,85,'책과 이야기가 있는\n다정구 도서관으로 초대합니다.',27,{color:brown,weight:700,lineHeight:1.26,letterSpacing:-1.1}),
 centered(86,583,358,68,'운영시간 | 화–일 09:00–18:00\n(월요일·공휴일 휴관)',21,{font:'Gowun Dodum',color:turquoise,lineHeight:1.3,letterSpacing:-.9}),
 centered(82,657,367,37,'웹사이트 | www.umchungjoeun.kr',21,{font:'Gowun Dodum',color:turquoise,letterSpacing:-1.1}),centered(91,699,348,36,'문의 | 02.1234.5678',21,{font:'Gowun Dodum',color:turquoise,letterSpacing:-.8}),
 T(675,126,323,40,'공간 안내 및 이용 정보',29,{color:turquoise,weight:700,letterSpacing:-1.2}),IC(944,116,18,18,'Sparkle','#b7e2e8'),IC(941,140,31,31,'Sparkle','#b7e2e8'),B(932,167,10,10,'#b7e2e8',{radius:'50%'}),
 ...[
 ['자료실 (열람·대출)','1층 09:00–18:00\n대상: 전 연령'],['어린이자료실','1층 09:00–18:00\n대상: 유아~초등 전학년'],['스터디룸','2층 09:00–17:30 (예약제)\n대상: 성인·청소년'],['디지털자료실','2층 10:00–17:00\n대상: 전 연령'],['다목적홀 (프로그램 공간)','3층 프로그램별 상이\n대상: 프로그램 참가자'],['상호대차 서비스','안내데스크 상시 운영\n대상: 도서관 회원']
 ].flatMap(([title,body],i)=>[centered(609,[198,332,467,607,747,889][i],375,43,title,24,{font:'Gowun Dodum',color:brown,letterSpacing:-1}),centered(609,[239,373,508,648,788,930][i],375,62,body,19,{font:'Gowun Dodum',color:brown,lineHeight:1.28,letterSpacing:-.8}),...(i<5?[dotted(613,[310,446,587,727,869][i],370)]:[])]),
 VP(1096,82,449,543,'M 39 213 C -1 97 41 4 187 1 C 383 -5 425 1 426 64 C 436 117 411 136 363 141 C 474 165 474 248 412 283 C 470 354 452 403 392 468 C 367 506 279 527 166 541 C 83 551 14 489 58 440 C 86 407 112 402 120 408 C 29 416 -2 365 1 324 C 3 295 22 282 68 270 C 28 268 20 231 39 213 Z',{fill:'#dff2f6',color:'#dff2f6',strokeWidth:0}),
 VP(1443,84,68,62,'M 20 56 C -17 32 5 -8 34 18 C 77 58 29 59 26 18 C 24 -15 53 -7 68 32',{color:'#a9dfe7',strokeWidth:7}),T(1196,163,350,250,'다정구\n도서관',108,{color:brown,weight:800,lineHeight:1.07,letterSpacing:-3}),
 T(1201,427,336,80,'책과 사람이 만나는\n다정한 도서관',29,{font:'Gowun Dodum',color:brown,lineHeight:1.31,letterSpacing:-1.1}),T(1201,523,336,38,'2056년 도서관 이용 안내',26,{font:'Gowun Dodum',color:brown,letterSpacing:-1.6}),
 I(1404,561,100,84,{label:'표지 새 복잡 일러스트',clipPath:'polygon(14% 25%,62% 0,100% 20%,80% 77%,11% 100%,0 48%)'}),
 VP(0,1006,1600,125,'M 0 1 C 168 -6 373 9 534 25 C 722 47 852 24 1070 17 C 1262 10 1350 39 1600 15 L 1600 125 L 0 125 Z',{fill:'#bbde80',color:'#bbde80',strokeWidth:0}),
 I(270,772,222,294,{label:'책·나무·덤불 복잡 일러스트',clipPath:'polygon(0 39%,24% 32%,46% 61%,51% 26%,53% 0,85% 0,100% 48%,84% 83%,93% 100%,15% 100%)'}),I(576,989,239,83,{label:'하단 덤불 복잡 일러스트',clipPath:'ellipse(50% 50% at 50% 50%)'}),
 I(1127,861,255,230,{label:'표지 책 더미 복잡 일러스트',clipPath:'polygon(0 5%,46% 0,87% 3%,100% 47%,91% 90%,34% 100%,8% 89%)'}),
 VP(1185,785,54,48,'M 3 39 C -10 12 21 -4 27 20 C 33 47 7 30 16 14 C 33 -15 38 6 48 20',{color:'#efb282',strokeWidth:5}),VP(1378,835,45,48,'M 7 46 C 9 14 44 42 37 0',{color:'#a2dce4',strokeWidth:5}),
 flower(1405,919,23,'#c8e7eb'),flower(1403,953,41,'#c8e7eb'),B(1390,987,12,12,'#c8e7eb',{radius:'50%'}),flower(87,299,24,'#c8e7eb'),flower(108,325,16,'#c8e7eb'),B(108,281,9,9,'#c8e7eb',{radius:'50%'}),VP(384,302,38,40,'M 1 16 C 6 -7 41 8 24 22 C 2 38 8 3 29 17 C 46 27 35 33 26 40',{color:'#c8e7eb',strokeWidth:4})
]
function libraryProgram(x:number,y:number,title:string,body:string,details:string,w=425):Element[]{
 return[B(x,y+22,Math.min(w,title.length*14),7,'#bde1e6'),T(x,y-2,w,36,title,22,{color:brown,weight:700,letterSpacing:-.7}),T(x,y+43,w,62,body,18,{color:brown,lineHeight:1.34,letterSpacing:-.3}),T(x+11,y+111,w-10,70,details,17,{color:brown,lineHeight:1.45,letterSpacing:-.6})]
}
const l17s02:Element[]=[
 B(0,0,1600,1131,'#fff'),B(0,0,534,1131,pale),T(53,79,330,40,'인사말',29,{color:turquoise,weight:700,letterSpacing:-1}),
 T(52,162,441,195,'다정구 도서관은 지역 주민을 위한 열람·대출 공간\n이자, 다양한 프로그램이 열리는 작은 문화 공간입\n니다. 책을 매개로 어린이부터 어르신까지 자연스\n럽게 어우러질 수 있도록 공간과 프로그램을 마련\n하고 있습니다. 언제든 편하게 들러 주세요.',21,{font:'Gowun Dodum',color:turquoise,lineHeight:1.73,letterSpacing:-.9}),
 B(53,500,433,574,'#fff',{radius:14}),T(95,535,357,43,'공간 한눈에 보기',29,{color:brown,weight:700,letterSpacing:-1}),
 ...['1층 | 자료실 · 어린이자료실','2층 | 스터디룸 · 디지털자료실','3층 | 다목적홀'].flatMap((t,i)=>[T(95,600+i*48,365,37,t,24,{font:'Gowun Dodum',color:brown,letterSpacing:-.9}),dotted(96,638+i*48,352,'#c7c7c7')]),...Array.from({length:4},(_,i)=>dotted(96,781+i*48,352,'#c7c7c7')),
 VP(246,993,50,43,'M 6 36 C -12 12 4 0 21 22 C 40 49 31 -3 45 17',{color:'#efb282',strokeWidth:5}),I(34,959,250,136,{label:'책 더미·열린 책 복잡 일러스트',clipPath:'polygon(0 24%,62% 0,83% 37%,94% 41%,100% 71%,81% 100%,22% 89%,5% 77%)'}),I(389,452,80,65,{label:'인사말 새 복잡 일러스트',clipPath:'polygon(4% 32%,74% 0,100% 0,88% 50%,99% 99%,5% 75%)'}),
 T(600,77,715,45,'주요 서비스 및 프로그램 안내',29,{color:turquoise,weight:700,letterSpacing:-.8}),
 ...libraryProgram(600,169,'자료실 이용 (열람·대출)','회원 가입 시 도서 열람과 대출이 모두 가능합니다. 열람\n공간에서 원하는 책을 편하게 읽으실 수 있습니다.','•  장소 및 시간: 1층 자료실 · 09:00–18:00\n•  대상: 전 연령'),
 ...libraryProgram(600,367,'어린이 자료실','그림책과 어린이 도서로 구성된 공간으로, 아이들이 편하\n게 책을 고르고 읽을 수 있도록 눈높이에 맞춰 있습니다.','•  장소 및 시간: 1층 어린이자료실 · 09:00–18:00\n•  대상: 유아 및 초등 전학년'),
 ...libraryProgram(600,585,'스터디룸 예약','조용한 학습 공간이 필요하신 분들을 위한 개인·소그룹\n스터디룸입니다. 사전 예약을 통해 이용할 수 있습니다.','•  장소 및 시간: 2층 스터디룸 · 09:00–17:30 (예약제)\n•  대상: 성인 및 청소년'),
 ...libraryProgram(1134,169,'성인 독서모임','한 권의 책을 함께 읽고 생각을 나누는 정기 모임입니다.\n새로운 참가자는 언제든 환영합니다.','•  장소 및 시간: 다목적홀 · 격주 목요일 15:00–17:00\n•  대상: 성인'),
 ...libraryProgram(1134,367,'어린이 그림책 낭독회','그림책을 함께 읽고 이야기 나누는 어린이 대상 프로그\n램입니다. 매주 진행되어 꾸준히 참여하실 수 있습니다.','•  장소 및 시간: 어린이자료실 · 매주 토요일 10:00–12:00\n•  대상: 유아 및 초등 저학년 (보호자 동반)'),
 ...libraryProgram(1134,585,'저자 초청 강연','책 너머 저자의 이야기를 직접 듣는 특별한 자리입니다.\n좌석이 한정되어 있어 사전 신청을 권해드립니다.','•  장소 및 시간: 다목적홀 · 월 1회 사전 공지\n•  대상: 성인 및 청소년'),
 B(600,825,937,249,pale,{radius:16}),T(636,857,626,46,'이용 안내',31,{color:brown,weight:700,letterSpacing:-1}),
 T(636,911,727,92,'회원 가입을 하시면 1인당 도서 5권을 2주간 대출하실 수 있고, 연계 도서관의 도서를 상호 대\n차하여 대출할 수 있습니다. 프로그램 신청과 회원 가입은 홈페이지 또는 안내 데스크에서 가\n능합니다.',18.5,{font:'Gowun Dodum',color:'#897d6a',lineHeight:1.43,letterSpacing:-.5}),
 T(636,1018,731,33,'웹사이트  www.umchungjoeun.kr   전화문의 02–1234–5678',20,{font:'Gowun Dodum',color:brown,letterSpacing:-.6}),
 I(779,761,115,88,{label:'프로그램 책 든 새 복잡 일러스트',clipPath:'polygon(0 59%,58% 12%,65% 0,100% 38%,76% 67%,27% 100%)'}),I(1363,711,166,196,{label:'나무·덤불 복잡 일러스트',clipPath:'polygon(29% 19%,56% 24%,64% 0,88% 5%,97% 50%,81% 81%,100% 92%,100% 100%,0 100%,5% 90%,18% 64%,19% 26%)'}),
 ...[[1392,903,35,0],[1392,903,0,37],[1461,903,35,0],[1495,903,0,37],[1392,972,0,36],[1392,1006,35,0],[1460,1006,37,0],[1495,972,0,36]].map(([x,y,w,h])=>B(x,y,w||3.5,h||3.5,'#bdab90')),
 centered(1390,945,109,29,'QR코드',18,{color:'#bdab90',weight:700}),centered(1361,1017,170,31,'회원가입 페이지',18,{font:'Gowun Dodum',color:'#bdab90'}),
 I(1438,81,104,93,{label:'열린 책 복잡 일러스트',clipPath:'polygon(10% 44%,28% 0,57% 24%,87% 19%,100% 65%,68% 100%,0 65%)'}),flower(149,49,18,'#c8e7eb'),flower(164,67,29,'#c8e7eb'),B(162,104,9,9,'#c8e7eb',{radius:'50%'}),flower(1520,58,24,'#c8e7eb'),flower(1538,85,17,'#c8e7eb'),B(1510,68,7,7,'#c8e7eb',{radius:'50%'})
]

const pen={font:'Gaegu',weight:700,color:marketBrown,lineHeight:1.2}
const l18s01:Element[]=[
 B(0,0,1600,1131,cream),VP(0,861,1600,270,'M 0 0 L 1600 130 L 1600 270 L 0 270 Z',{fill:'#3f6f25',color:'#3f6f25',strokeWidth:0}),
 B(89,127,634,891,'#fff',{radius:22,border:'2px dashed #c7c7d0'}),...roof(331,82,149,62),
 T(158,205,500,53,'라라나 전통시장 방문 안내',39,{...pen,weight:400,letterSpacing:1}),
 C(158,286,195,43,'운영 시간',31,marketBrown,{...pen,color:'#fff',radius:25}),T(166,353,491,73,'•  오전 9시 ~ 저녁 8시\n•  휴무일: 첫째/셋째 일요일',24,{lineHeight:1.3}),
 C(158,451,195,43,'오시는 길',31,marketBrown,{...pen,color:'#fff',radius:25}),T(166,520,491,94,'•  지하철 00역 도보 5분\n•  00버스 정류장 하차\n•  00주차장 이용',24,{lineHeight:1.22}),
 C(158,654,195,43,'문의',31,marketBrown,{...pen,color:'#fff',radius:25}),T(166,723,491,75,'•  전화:123–456–7890\n•  홈페이지: www.reallygreatsite.com',24,{lineHeight:1.25}),
 B(158,839,496,1,'transparent',{border:'1px dashed #c7c7d0'}),T(158,887,501,80,'신선하고 정직한 먹거리, 사람 냄새 나는\n정겨운 라라나 전통시장으로 오세요!',29,{...pen,color:'#7f849c',letterSpacing:-1.3,lineHeight:1.4}),
 centered(909,118,601,130,'라라나 전통시장',84,{...pen,letterSpacing:-5}),centered(1000,273,430,102,'정겨움 가득\n사람 냄새 나는 장터',47,{...pen,color:'#0b0b0b',letterSpacing:1.5,lineHeight:1.18}),
 I(974,478,539,516,{label:'농부·야채·바구니 복잡 일러스트',clipPath:'polygon(0 19%,9% 1%,42% 0,49% 26%,68% 4%,83% 5%,95% 21%,100% 33%,91% 66%,76% 70%,75% 100%,18% 100%,7% 79%,0 46%)'}),
 I(873,640,78,75,{label:'방울토마토 복잡 일러스트',clipPath:'polygon(0 10%,86% 0,100% 30%,74% 65%,58% 100%,19% 100%,35% 49%)'}),I(1408,794,101,108,{label:'잎채소 복잡 일러스트',clipPath:'polygon(0 71%,39% 5%,80% 0,100% 44%,68% 100%,26% 88%)'})
]
const l18s02:Element[]=[
 B(0,0,1600,1131,cream),VP(0,914,1600,217,'M 0 131 L 1600 0 L 1600 217 L 0 217 Z',{fill:'#be852c',color:'#be852c',strokeWidth:0}),
 ...roof(113,127,88,36),T(224,122,124,44,'전통과 정(',30,{...pen,letterSpacing:-.6}),T(344,126,31,36,'情',27,{font:'Noto Serif KR',weight:700,color:marketBrown,lineHeight:1.2}),T(373,122,235,44,')이 살아 숨 쉬는 곳',30,{...pen,letterSpacing:-.6}),B(113,189,584,1,'transparent',{border:'1px dashed #c7c7d0'}),
 T(112,239,615,63,'우리 전통시장은 지역 주민들의 삶과 함께해온 오랜 장터입니다.',22,{lineHeight:1.3,letterSpacing:-.7}),
 T(112,298,615,129,'수십 년을 한 자리를 지켜온 상인의 손길,\n갓 수확한 채소의 싱그러움,\n솜씨 좋은 어머니의 반찬 냄새가 가득한 이곳은\n단순한 시장을 넘어, 마을의 기억이 담긴 공간입니다.',24,{lineHeight:1.22,letterSpacing:-.2}),
 ...roof(113,527,88,36),T(225,523,491,55,'전통시장만의 매력',42,{...pen,letterSpacing:1}),B(113,589,584,1,'transparent',{border:'1px dashed #c7c7d0'}),
 T(113,639,615,73,'신선하고 정직한 먹거리, 사람 냄새 나는 정겨운 상인들,\n손맛 가득한 먹거리 골목, 소소하지만 확실한 즐거움이 있습니다.',24,{lineHeight:1.4,letterSpacing:-.6}),
 ...roof(902,127,88,36),T(1013,121,491,55,'시장 속 즐길거리',42,{...pen,letterSpacing:1}),B(902,189,584,1,'transparent',{border:'1px dashed #c7c7d0'}),
 T(902,238,586,47,'먹거리 골목',37,{...pen,color:'#080808'}),T(910,283,601,70,'•  수제 어묵, 국수, 빈대떡, 찐빵 등\n•  따끈한 향기 따라 걷다 보면 미소가 절로',24,{lineHeight:1.22}),
 T(902,400,586,47,'알뜰 쇼핑 거리',37,{...pen,color:'#080808'}),T(910,447,601,69,'•  싱싱한 채소와 과일, 제철 해산물\n•  손으로 고른 생활잡화, 의류, 주방용품',24,{lineHeight:1.22}),
 T(902,564,586,47,'쉼터와 문화공간',37,{...pen,color:'#080808'}),T(910,610,434,99,'•  벽화 골목\n•  전통놀이 체험\n•  시장 음악회',24,{lineHeight:1.22}),
 I(94,815,236,252,{label:'채소 가판대·상인 복잡 일러스트',clipPath:'polygon(12% 0,81% 0,100% 20%,88% 31%,100% 100%,2% 100%,0 78%,12% 19%)'}),I(410,885,99,173,{label:'장바구니를 든 인물 복잡 일러스트',clipPath:'polygon(0 0,69% 0,76% 45%,100% 56%,97% 100%,0 100%)'}),
 I(902,890,111,128,{label:'채소 바구니 복잡 일러스트',clipPath:'polygon(8% 18%,40% 0,80% 18%,100% 37%,92% 100%,17% 100%,0 46%)'}),I(1068,827,86,192,{label:'앞치마 상인 복잡 일러스트',clipPath:'polygon(17% 0,74% 0,80% 39%,100% 57%,81% 65%,85% 100%,22% 100%,21% 68%,0 55%)'}),
 I(1192,592,408,494,{label:'시장 가게·하늘·채소 복잡 일러스트',clipPath:'polygon(17% 2%,48% 0,91% 2%,100% 6%,100% 100%,76% 96%,61% 91%,39% 89%,12% 78%,16% 65%,0 57%,0 22%,8% 13%)'})
]

export const groupD:BrochureDraft[]=[
 {id:'l15',sides:[{id:'s01',elements:l15s01,notes:['표·체크박스·꽃 도형·연락 아이콘을 실제 요소로 구현했습니다. 인물 일러스트만 placeholder 처리했습니다.','판독 가능한 원문을 모두 복원했습니다. 원본의 둥근 고딕 제목은 실제 NanumSquareRound 800으로 구현했습니다.']},{id:'s02',elements:l15s02,notes:['표의 15개 데이터 셀 및 안내 문구를 실제 텍스트로 복원했습니다. 상담자 복잡 일러스트는 placeholder 처리했습니다.']}]},
 {id:'l16',sides:[{id:'s01',elements:l16s01,notes:['원본은 1600×1236입니다. 가로세로 동일 배율로 1280×720 안에 contain합니다.','Poppins 900/400을 실제 로드하여 영문 제목 굵기를 구현했습니다. 궁궐 사진만 placeholder 처리했습니다.']},{id:'s02',elements:l16s02,notes:['프로그램 네 가지의 번호·이름·설명·시간을 실제 텍스트로 구현했습니다. 인물·한식 사진만 placeholder 처리했습니다.','원본의 한글 제목은 Pretendard 실제 굵기로 근접했습니다.']}]},
 {id:'l17',sides:[{id:'s01',elements:l17s01,notes:studyNotes},{id:'s02',elements:l17s02,notes:[...studyNotes,'6개 서비스·프로그램 설명과 시간·대상, 인사말·이용 안내 원문을 모두 구현했습니다.']}]},
 {id:'l18',sides:[{id:'s01',elements:l18s01,notes:['실제 Gaegu 700을 로드하여 제목·배지·손글씨 문구를 구현했습니다. 원본 손글씨와 세부 획 차이가 남습니다.','지붕 장식·단색 경사 배경은 SVG와 CSS로 구현했습니다. 복잡 인물·채소 일러스트만 placeholder 처리했습니다.']},{id:'s02',elements:l18s02,notes:['전통시장 소개·특징·즐길거리 원문을 실제 텍스트로 구현했습니다.','시장 가게·인물·채소 복잡 일러스트는 같은 배치·윤곽의 placeholder 처리했습니다.']}]}
]
