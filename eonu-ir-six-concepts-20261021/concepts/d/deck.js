(function(){
const C={deep:'#251044',purple:'#7044C5',lav:'#C8ACF4',paper:'#F6F2FC',ink:'#251044',gray:'#e5e5e5'};
const esc=s=>String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const pos=(x,y,w,h)=>`left:${x}px;top:${y}px;width:${w}px;height:${h}px;`;
const box=(x,y,w,h,cls='',extra='')=>`<div class="shape ${cls}" style="${pos(x,y,w,h)}${extra}"></div>`;
const txt=(x,y,w,h,s,size=24,cls='',extra='')=>`<div class="text ${cls}" style="${pos(x,y,w,h)}font-size:${size}px;line-height:${cls.includes('hero')?(size===52?64:80):cls.includes('brand')?52:Math.ceil(size*1.5/2)*2}px;${extra}">${s}</div>`;
const ph=(x,y,w,h,label,extra='')=>`<div class="placeholder" style="${pos(x,y,w,h)}${extra}"><span>${label}</span></div>`;
const svg=(x,y,w,h,s)=>`<svg class="diagram" style="${pos(x,y,w,h)}" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg">${s}</svg>`;
const line=(x1,y1,x2,y2,c=C.purple,sw=4)=>`<path d="M${x1} ${y1} L${x2} ${y2}" fill="none" stroke="${c}" stroke-width="${sw}"/>`;
const arrow=(x1,y1,x2,y2,c=C.purple)=>line(x1,y1,x2,y2,c)+`<path d="M${x2-12} ${y2-8} L${x2} ${y2} L${x2-12} ${y2+8}" fill="none" stroke="${c}" stroke-width="4"/>`;
const circle=(x,y,r,fill)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${fill}"/>`;
const st=(x,y,s,size=24,c=C.ink,anchor='middle',weight=600)=>`<text x="${x}" y="${y}" text-anchor="${anchor}" fill="${c}" font-size="${size}" font-weight="${weight}" font-family="Pretendard,sans-serif">${s}</text>`;
const titles={
'01':'함께 오지 못해도,<br>이야기는 함께.',
'02':'환자는 왔지만,<br><em>이야기는 오지 못했습니다.</em>',
'03':'<em>세 사람의 이야기,</em> 하나의 흐름으로.',
'04':'환자의 걱정이,<br><em>병원의 상담 기회로.</em>',
'05':'<em>병원이 묻고,</em> 일상에서 답합니다.',
'06':'기록은 편하게. <em>전달은 확인하고.</em>',
'07':'첫 매출의 출발점은 <em>병원 라이선스.</em>',
'08':'큰 시장에서, <em>먼저 살 고객을 좁힙니다.</em>',
'09':'일상 기록에서, <em>연결된 건강 정보로.</em>',
'10':'현장 피드백을, <em>첫 도입으로.</em>',
'11':'<em>1억 원,</em> 첫 유료 모델을 향한 실행 자금.',
'12':'환자에게 필요한 연결.<br>병원도 계속 쓸 이유.'};
const slides=window.IR_CONTENT.map(s=>({...s,title:titles[s.id],content:s.subtitle||s.caption||s.title}));
function head(s){return `<div class="section-label">${s.section}</div><div class="heading">${s.title}</div><div class="subheading">${s.subtitle}</div>`;}
function foot(s){return `<div class="slide-footer">${s.caption}</div><div class="page-number">${s.id}</div>`;}
function s01(){return box(0,0,1280,720,'deep')+box(556,-216,936,936,'orb')+txt(64,48,400,52,'EONU',40,'brand white')+txt(64,208,720,176,titles['01'],64,'hero white')+txt(68,424,500,76,'환자 · 보호자 · 의료진의<br>AI 소통을 잇는 이어온유',28,'white')+ph(812,64,320,332,'환자의 일상 이미지','border-radius:168px 168px 0 0;')+ph(660,436,360,216,'보호자 · 의료진 이미지','border-radius:0 0 112px 112px;')+txt(68,636,500,28,'EONU IR  /  2026.10.21',16,'muted-white');}
function s02(){return box(0,0,1280,720,'paper')+box(792,0,488,720,'lav')+head(slides[1])+ph(64,268,520,320,'아이 혼자 진료받는 장면')+ph(612,332,280,256,'함께하지 못한 보호자')+ph(920,244,296,344,'정보를 확인하는 의료진')+txt(80,608,880,40,'동행의 부재가 만드는 정보 전달의 공백',28,'strong')+txt(920,608,296,40,'재구성한 설명용 사례',16,'dim')+foot(slides[1]);}
function s03(){const d=svg(64,252,1152,360,
arrow(240,80,456,176)+arrow(240,280,456,196)+arrow(712,176,924,176)+`<path d="M1004 232V324H588V260" fill="none" stroke="${C.lav}" stroke-width="4"/>`+
`<rect x="0" y="20" width="240" height="120" rx="60" fill="${C.lav}"/>`+`<rect x="0" y="220" width="240" height="120" rx="60" fill="${C.lav}"/>`+circle(584,184,128,C.deep)+`<rect x="912" y="116" width="240" height="136" rx="68" fill="${C.purple}"/>`+
st(120,68,'환자',28)+st(120,108,'나의 경험',20,C.ink,'middle',400)+st(120,268,'보호자',28)+st(120,308,'관찰과 걱정',20,C.ink,'middle',400)+st(584,172,'EONU',44,'white')+st(584,212,'역할 · 공유 범위',20,C.lav)+st(1032,168,'의료진',28,'white')+st(1032,208,'질문과 관리 계획',20,'white','middle',400)+st(788,314,'진료 후 계획을 다시 일상으로',20,C.ink));return box(0,0,1280,720,'paper')+head(slides[2])+d+foot(slides[2]);}
function s04(){return box(0,0,1280,720,'paper')+box(804,0,476,720,'deep')+head(slides[3])+txt(844,80,360,40,'먼저 검증할 도입 가치',20,'white')+txt(844,148,340,64,'수익 기여',44,'white strong')+txt(844,240,328,104,'미해결 걱정이<br>자발적인 상담 요청으로<br>이어질 수 있을까?',28,'white')+txt(64,288,276,44,'진료 효율',28,'strong')+txt(64,344,276,80,'필요한 정보 확인과<br>전체 업무 부담',22)+txt(416,288,300,44,'임상적 유용성',28,'strong')+txt(416,344,300,80,'일상 정보의 의미와<br>진료 활용 가능성',22)+svg(64,448,680,140,`<rect width="680" height="140" fill="${C.lav}"/>`+st(112,60,'미해결 걱정',24)+arrow(224,72,272,72)+st(388,60,'병원 정보',24)+arrow(500,72,548,72)+st(616,60,'상담',24)+st(340,110,'정보 제공 → 환자가 자발적으로 요청',20,C.ink))+txt(844,424,324,80,'상담 요청 · 지불 의사<br>업무 부담을 함께 측정',22,'white')+txt(844,560,324,60,'AI가 치료 필요성을<br>판단하지 않습니다.',20,'muted-white')+foot(slides[3]);}
function s05(){const d=svg(64,276,1152,300,`<rect width="316" height="280" rx="24" fill="${C.deep}"/>`+st(158,68,'의료진이 먼저 설정',28,'white')+st(158,132,'질문',24,C.lav)+st(158,180,'서비스 정보',24,C.lav)+st(158,228,'진료 후 관리 안내',24,C.lav)+arrow(336,140,480,140)+circle(616,140,120,C.purple)+st(616,136,'EONU',40,'white')+st(616,176,'병원의 질문을 전달',20,'white')+arrow(752,140,844,140)+`<rect x="864" y="20" width="288" height="240" rx="120" fill="${C.lav}"/>`+st(1008,112,'환자 · 보호자',28)+st(1008,160,'QR로 사용 시작',24)+st(1008,200,'일상에서 응답',20,C.ink,'middle',400));return box(0,0,1280,720,'paper')+head(slides[4])+d+txt(64,608,1100,40,'병원 안내 QR은 진입 경로입니다. 실제 접속용 QR은 제공하지 않습니다.',20,'dim')+foot(slides[4]);}
function ui(x,y,w,h,num,heading,body){return `<div class="ui" style="${pos(x,y,w,h)}"><div class="ui-cap">${num} / ${heading}</div>${body}</div>`;}
function s06(){return box(0,0,1280,720,'lav')+head(slides[5])+txt(64,218,1152,32,'설명용 UI 도식 · 가상 데이터',16,'dim')+
ui(64,272,240,300,'01','병원 설정','<h3>다음 진료 전 질문</h3><p>요즘 수면은 어떤가요?</p><p>관찰할 변화 선택</p><div class="ui-bar">질문 · 안내 전달</div>')+
ui(352,304,240,300,'02','일상 기록','<h3>오늘의 기록</h3><div class="ui-tabs">일기　음성　체크</div><p>잠드는 시간이<br>평소보다 늦었어요.</p><div class="ui-bar">AI 요약 초안</div>')+
ui(640,272,288,332,'03','공유 전 확인','<h3>원문 ↔ 요약</h3><p>원문과 요약을 비교하고<br>직접 내용을 수정합니다.</p><div class="ui-check">✓ 공유할 항목 선택</div><div class="ui-check">✓ 보호자 · 의료진 범위</div><div class="ui-bar">확인 후 전달</div>')+
ui(976,304,240,300,'04','의료진 확인','<h3>전달된 기록</h3><div class="ui-check">작성자: 환자</div><div class="ui-check">당사자 확인 완료</div><p>진료 후 관리 계획을<br>다시 일상으로</p>')+
svg(304,376,672,104,arrow(4,16,40,16,C.deep)+arrow(292,40,328,40,C.deep)+arrow(628,16,664,16,C.deep))+foot(slides[5]);}
function s07(){return box(0,0,1280,720,'paper')+head(slides[6])+box(64,272,520,348,'deep')+txt(96,300,400,40,'01 / B2B FIRST',20,'muted-white')+txt(96,368,440,60,'병원 라이선스',44,'white strong')+txt(96,456,420,96,'일차의료기관의 도입 가치와<br>지불 의사를 먼저 확인합니다.',24,'white')+txt(96,568,420,28,'첫 병원군 · 가격 · 계약 상태 미확정',16,'muted-white')+svg(584,432,80,32,arrow(8,16,72,16))+txt(704,288,470,44,'02 / B2B2C',28,'strong')+txt(704,348,470,72,'유료 도입 검증 이후<br>환자·보호자의 추가 가치 탐색',24)+box(704,448,512,4,'lav')+txt(704,488,470,40,'별도 경로 / B2G',28,'strong')+txt(704,548,470,60,'실제 구매기관 · 예산 · 공공 계약<br>연구지원금과 민간 봉사활동은 구분',22)+foot(slides[6]);}
function s08(){const d=svg(64,256,576,376,`<path d="M0 376V264A264 264 0 0 1 528 264V376Z" fill="${C.lav}"/>`+`<path d="M80 376V272A184 184 0 0 1 448 272V376Z" fill="${C.purple}"/>`+`<path d="M160 376V280A104 104 0 0 1 368 280V376Z" fill="${C.deep}"/>`+st(264,76,'TAM',28)+st(264,184,'SAM',28,'white')+st(264,304,'SOM',28,'white')+st(264,344,'먼저 확보할 고객',18,'white'));return box(0,0,1280,720,'paper')+head(slides[7])+d+txt(704,264,488,40,'구매 단위로 산정합니다.',28,'strong')+txt(704,328,488,56,'B2B  /  기관 수 × 연간 가격',24)+txt(704,404,488,64,'B2B2C  /  사용자 × 전환율 × 연간 지출',22)+txt(704,488,488,56,'B2G  /  구매 건수 × 계약 금액',24)+txt(704,568,488,72,'입력값·가격은 미확정<br>하드웨어·연구지원금·중복 계약 제외',20,'dim')+foot(slides[7]);}
function s09(){return box(0,0,1280,720,'paper')+head(slides[8])+svg(64,244,1152,392,`<path d="M40 196H1004M560 196V56M560 196V336" fill="none" stroke="${C.lav}" stroke-width="4"/>`+circle(180,196,128,C.deep)+st(180,182,'환자의',32,'white')+st(180,226,'일상 기록',32,'white')+circle(560,56,56,C.lav)+st(560,64,'EMR',24)+circle(560,336,56,C.lav)+st(560,344,'외부 앱',22)+circle(1004,196,128,C.purple)+st(1004,182,'연결된',32,'white')+st(1004,226,'건강 정보',32,'white')+st(560,172,'의료진 도입 검증 이후',24)+st(560,220,'유용성 · 입력 부담 · 반복 사용',20,C.ink,'middle',400))+txt(64,640,1152,32,'후속 연구: ADHD · 노년층의 기기 연동, 디지털 바이오마커  /  권한·비용·임상적 의미 확인',18,'dim')+foot(slides[8]);}
function s10(){return box(0,0,1280,720,'paper')+head(slides[9])+box(64,260,1152,292,'lav')+txt(88,284,1000,32,'MD에 기재된 현재 접점',18,'strong')+ph(88,340,208,180,'현장 피드백 이미지')+txt(332,344,260,40,'전문의 피드백',28,'strong')+txt(332,408,240,88,'정신건강의학과<br>전문의의 지속적인 의견',22)+txt(632,344,240,40,'연구기관 접점',28,'strong')+txt(632,408,240,88,'기관과의 연락·협의<br>범위와 증빙 확인',22)+txt(932,344,240,40,'봉사 참여',28,'strong')+txt(932,408,240,88,'청년 우울증 관련<br>프로젝트 운영 경험',22)+txt(64,588,1152,36,'다음 검증  →  실제 활용  /  전체 업무 부담  /  반복 사용  /  구매 의사',26,'strong')+txt(64,636,1100,28,'현재 접점은 공식 제휴·실증·유료 계약 실적으로 합산하지 않습니다.',18,'dim')+foot(slides[9]);}
function s11(){return box(0,0,1280,720,'paper')+head(slides[10])+ph(64,272,316,336,'창업자 프로필 이미지','border-radius:160px 160px 0 0;')+txt(416,280,300,40,'직접 기획 · 개발 · 수정',28,'strong')+txt(416,348,300,112,'의료·AI 이해를 바탕으로<br>제품의 가설을 만들고<br>현장 피드백을 반영합니다.',22)+txt(416,508,300,88,'필요한 협력<br>임상 · 개인정보·보안 · 실증',22)+box(768,260,448,364,'deep')+txt(800,284,360,32,'사용계획 총액',20,'muted-white')+txt(800,332,360,92,'1억 원',64,'white strong')+txt(800,444,360,88,'제품 · 보안 · 실증<br>고객 확보 · 운영',28,'white')+txt(800,560,360,44,'배분 · 기간 · 기관·고객 목표 [ ]',18,'muted-white')+foot(slides[10]);}
function s12(){const d=svg(660,192,552,412,`<path d="M276 40L56 356H496Z" fill="none" stroke="${C.lav}" stroke-width="4"/>`+circle(276,40,40,C.lav)+circle(56,356,40,C.lav)+circle(496,356,40,C.lav)+st(276,48,'환자',22)+st(56,364,'보호자',20)+st(496,364,'의료진',20)+circle(276,228,92,C.purple)+st(276,240,'EONU',40,'white'));return box(0,0,1280,720,'deep')+box(-180,360,680,680,'orb')+txt(64,48,400,52,'EONU',40,'brand white')+txt(64,208,620,176,titles['12'],52,'hero white')+txt(68,440,520,88,'세 사람의 안심을 잇고,<br>첫 유료 모델의 가치를 검증합니다.',28,'white')+ph(76,580,440,92,'서비스 브랜드 이미지','border-radius:48px;')+d;}
const renderers=[s01,s02,s03,s04,s05,s06,s07,s08,s09,s10,s11,s12];
function renderSlide(s,mode='design'){return `<article class="slide ${mode==='wireframe'?'wireframe':'design'} page-${s.id}" data-slide="${s.id}">${renderers[Number(s.id)-1]()}</article>`;}
window.CONCEPT={slides,renderSlide};
})();
