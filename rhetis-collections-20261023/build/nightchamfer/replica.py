from pathlib import Path
import json
W=Path('/workspace/work/nightchamfer'); R=Path('/workspace/output/nightchamfer-review'); P=R/'replica'
css='''*{box-sizing:border-box}html,body{margin:0;width:1280px;height:720px;overflow:hidden}body{font-family:'Pretendard Variable';color:#f8f8f8;background:#000;font-size:20px;letter-spacing:-.025em}section{width:1280px;height:720px;position:relative;background:radial-gradient(ellipse 100% 24% at 50% 105%,#3169bc 0%,#112846 47%,#000 100%)}p,h1,h2,h3{margin:0}p{line-height:1.65}b,strong{font-weight:700}.top{position:absolute;left:45px;top:46px;width:1190px;height:28px}.brand{position:absolute;right:68px;top:45px;font-size:14px;font-weight:600;letter-spacing:0}.brand b{color:#4089ec;margin-right:13px}.title{position:absolute;left:134px;top:100px;font-size:28px;font-weight:700;line-height:1.25}.orb{position:absolute;left:90px;top:103px;width:27px;height:27px;border-radius:50%;background:#e5e5e5}.lead{position:absolute;left:85px;top:155px;color:#ccc;font-size:21px;font-weight:350}.panel{position:absolute;background:#111e;border:1px solid #65676a;border-radius:24px}.box{position:absolute}.muted{color:#ccc}.center{text-align:center}.accent{color:#4f94ed}.chip{display:flex;align-items:center;justify-content:center;background:linear-gradient(90deg,#173467,#224f95);border-radius:16px;font-weight:700;padding:8px 16px;min-height:36px;line-height:1.2;text-align:center}.chip.gray{background:#292929}.ph{background:#e6e6e6;position:absolute;border-radius:18px;display:flex;align-items:center;justify-content:center;color:#666;font-size:16px;letter-spacing:0}.circle{position:absolute;border-radius:50%;background:linear-gradient(135deg,#2874e6,#173b88);display:flex;align-items:center;justify-content:center;text-align:center;font-weight:700}.ring{border:26px solid #0c1b37}.dotted{border-top:1px dotted #888}.arrow{position:absolute;background:linear-gradient(#3985fa,#17375c);clip-path:polygon(50% 0,100% 50%,77% 50%,77% 100%,23% 100%,23% 50%,0 50%)}.arrow.right{clip-path:polygon(0 25%,75% 25%,75% 0,100% 50%,75% 100%,75% 75%,0 75%);background:linear-gradient(90deg,#05233b,#0087ee)}.arrow.down{transform:rotate(180deg)}.small{font-size:17px}.row{display:flex;align-items:center;gap:24px}.cols{display:flex;gap:22px}.list{line-height:2}.barplot{position:absolute;border-bottom:1px solid #999;display:flex;align-items:flex-end;justify-content:space-around;padding:0 12px 0;background:repeating-linear-gradient(to top,transparent 0,transparent 64px,#666 65px,transparent 66px)}.bar{background:#bbb;position:relative;min-width:72px}.bar.on{background:#3982fb}.bar b{position:absolute;bottom:100%;width:100%;text-align:center;font-size:15px;white-space:nowrap;margin-bottom:5px}.bar span{position:absolute;top:100%;left:0;width:100%;text-align:center;font-size:16px;font-weight:700;margin-top:5px}.line{position:absolute;background:#666}.dot{position:absolute;width:14px;height:14px;border-radius:50%;background:#3f86fb}.cover{background:radial-gradient(ellipse 42% 60% at 0% 100%,#9dbedf 0,#13315b 36%,#000 82%),radial-gradient(ellipse 30% 40% at 100% 0,#194485,#000)}.cover h1{font-size:104px;line-height:1.1;letter-spacing:-.02em}.cover .ph{border-radius:0}.lift{background:linear-gradient(180deg,#fff,#5f91cb);background-clip:text;color:transparent}.risks p{padding:22px 0;border-bottom:1px dotted #777}.risks p:last-child{border:0}'''
(P/'replica.css').write_text(css)
def at(c,x,y,w=None,h=None,cl='box',sty=''):
 s=f'left:{x}px;top:{y}px;'+(f'width:{w}px;' if w is not None else '')+(f'height:{h}px;'if h is not None else '')+sty
 return f'<div class="{cl}" style="{s}">{c}</div>'
def txt(c,x,y,w=None,size=20,sty=''):return at(c,x,y,w,sty=f'font-size:{size}px;'+sty)
def panel(c,x,y,w,h):return at(c,x,y,w,h,'panel')
def ph(x,y,w,h,n=''):return at(n,x,y,w,h,'ph')
def chip(c,x,y,w,h=42,gray=False):return at(c,x,y,w,h,'chip'+(' gray'if gray else ''))
def circ(c,x,y,w,ring=False,sty=''):return at(c,x,y,w,w,'circle'+(' ring'if ring else ''),sty)
def arrow(x,y,w,h,cl=''):return at('',x,y,w,h,'arrow '+cl)
def title(t,l):return '<span class="orb"></span>'+f'<h2 class="title">{t}</h2><p class="lead">{l}</p>'
def common():return '<svg class="top" viewBox="0 0 1190 28"><path d="M0 .5 H985 L1014 27 H1190" fill="none" stroke="#a0a0a0" stroke-width="1"/></svg><div class="brand"><b>♧</b>MiRi COMPANY</div>'
def bars(vals,labs,x,y,w,h,maxv=1300):
 z=''
 for i,(v,l)in enumerate(zip(vals,labs)):z+=f'<div class="bar {"on"if i==len(vals)-1 else ""}" style="height:{v/maxv*(h-28)}px;width:{min(w/(len(vals)*1.5),142)}px"><b>{v:,}억</b><span>{l}</span></div>'
 return at(z,x,y,w,h,'barplot')
slides=[]
slides.append(txt("MIRIAI, 2080’S NEW GROWTH ENGINE",93,168,700,28)+txt('<h1>MIRICOMPANY</h1>',85,230,980)+txt('<b class="lift">사업 계획 설명회</b>',88,385,800,52)+txt('2080. 07. 11<br>www.miricompany.com',93,582,500,21, 'color:#ccc')+ph(637,301,643,419,'3D 그래픽 자리'))
s=txt('<b class="lift">Contents</b>',107,129,560,72)+txt('이곳에 프레젠테이션 목차에 관한<br>내용을 간략하게 작성해보세요.',107,236,540,20,'color:#ccc')+ph(0,535,376,185,'3D 그래픽 자리')
for i,(n,d)in enumerate([('사업 현황','현재 주요 사업 (미리워크)<br>신규 사업 추진 배경'),('시장·고객 분석','AI 시장 규모와 성장성<br>고객 타깃과 페인포인트'),('신규 사업 개요','미리AI 제품 개요<br>핵심 가치와 차별성'),('사업 전략','비즈니스 모델<br>시장 진입 전략 및 포지션')]):
 y=132+141*i;s+=txt(f'<b class="accent">0{i+1}</b>',800,y,48,22)+txt(f'<b>{n}</b>',859,y,300,22)+at('',791,y+40,368,cl='box dotted')+txt(d,859,y+49,350,17,'color:#ccc;line-height:1.5')
slides.append(s)
s=title('현재 주요 사업',"미리컴퍼니는 협업 SaaS '미리워크'를 운영하며 누적 12만 팀, 유료 고객 3,200곳을 확보했습니다.")
s+= '<svg style="position:absolute;left:0;top:0" width="1280" height="720"><g fill="none" stroke="#555"><path d="M443 330H503L526 376M443 550H503L526 504M837 330H776L754 376M837 550H776L754 504"/></g></svg>'
for x,y,n,d in [(95,254,'할 일·프로젝트','문서·노트를 한 곳에서 작성·공유'),(837,254,'팀 메신저','칸반·일정으로 팀 업무 진행 관리'),(95,472,'유연한 연동','채널 기반 소통으로 대화와 업무 연결'),(837,472,'서비스 관련 키워드','이곳에 상세 내용을 입력해 보세요.')]:s+=panel(txt(f'<b>{n}</b>',0,39,348,23)+txt(d,0,82,348,20,'color:#ccc'),x,y,348,152)
s+=circ('UNIFIED<br>SERVICE',512,309,256,True,'font-size:30px')
for x,y in [(520,370),(748,370),(520,498),(748,498)]:s+=at('',x,y,12,12,'dot')
slides.append(s)
s=title('사업 추진 배경','이곳에 사업 추진 배경 방향성에 대한 내용을 간략하게 정리하여 작성해보세요.')+panel(chip('고객 수요 충족 목적',399,30,233,45)+txt('AI 성능 향상과 고객 요구 증대에 따른 실서비스 적용 시점이 도래',0,100,1036,24,'text-align:center;font-weight:600'),122,220,1036,169)+arrow(566,370,148,140)
s+=txt('<b>다음 성장 동력 발굴</b>',164,511,342,24,'text-align:center')+txt('쌓인 업무 데이터와 생성형 AI 기술을 결합해,<br>자연스러운 신규 성장 기회를 확보합니다.',121,557,430,21,'text-align:center;color:#ccc')+at('',641,554,1,64,'box','border-left:1px dotted #999')+txt('<b>고객의 요구</b>',741,509,400,24,'text-align:center')+txt("사용자의 약 70%가 ‘반복 업무 자동화’ 기능을 요청<br>(회의록 정리·문서 작성에 주당 평균 5시간 소모)",707,551,466,21,'text-align:center;color:#ccc');slides.append(s)
s=title('시장 분석','AI 업무 도구 시장이 협업툴보다 2배 이상 빠르게 성장하고 있습니다.')+txt('<b>국내 생산성 도구 시장 규모 추이</b>',166,218,410,24,'text-align:center')+bars([300,520,820,1300],['1Q','2Q','3Q','4Q'],116,287,457,196)+txt('<b>국내 시장 성장성 포인트</b>',793,218,400,24)
for i,(n,d)in enumerate([('AI 대중화','업무에 AI를 쓰는 것이 당연한 환경으로 전환'),('기업 도입 확대','생산성 향상을 위한 기업의 AI 도구 도입이 가속'),('자동화 ROI 입증','업무 시간 절감 효과가 수치로 증명되며 수요 견인')]):s+=panel(chip(n,14,14,145,34)+txt(d,181,20,320,17,'color:#ccc'),655,274+i*82,517,64)
s+=panel(txt('<b>AI 업무 도구 시장은 <span class="accent">연 60% 이상 고성장</span> 중이며, 협업툴 시장 대비 성장률이 2배를 넘습니다.</b>',0,33,1106,23,'text-align:center'),87,536,1106,98);slides.append(s)
s=title('사업 개요','미리워크 안에서 바로 쓰는 AI 생산성 서비스')+panel(txt('<b>미리AI <span class="lift">(MiriAI)</span></b>',55,44,500,30)+txt('<b>미리워크에 내장되는 AI 비서로 회의록 요약, 문서 초안,<br>할 일 추출, 업무 검색을 대화 한 번으로 처리합니다.</b>',55,102,500,20,'color:#ddd')+at('',51,196,486,cl='box dotted'),85,212,603,426)+ph(737,212,431,426,'사진 자리')
for i,(n,d)in enumerate([('회의록 자동 요약','녹취·메모를 핵심 요약과 할 일로 자동 변환'),('문서 초안 작성','주제만 입력하면 보고서·기획서 초안을 생성'),('업무 검색·질문','흩어진 문서·대화를 물어보면 AI가 즉시 답변')]):s+=chip(n,139,443+i*55,146,35,True)+txt(d,307,447+i*55,340,19,'color:#ddd')
slides.append(s)
s=title('고객 분석','');s+=txt('1차 타깃은 이미 미리워크를 쓰는 12만 팀입니다.',263,105,800,22,'color:#ccc')+panel(ph(28,24,124,112,'Mi')+txt('<b>미리워크 사용 팀</b>',190,41,270,24)+txt('<b>120,000</b>',191,76,270,40)+at('',408,32,1,97,'box','border-left:1px dotted #999')+chip('AI 미사용 고객',481,37,549,37,True)+chip('AI 사용 고객',481,90,549,37),92,164,1096,162)
s+=panel(txt('<b>주요 타깃: 반복 업무가 많은 운영·기획 팀</b>',54,31,450,23)+at('',43,85,461,cl='box dotted')+txt('• 회의·문서 작업 비중이 높음<br>• 인력 대비 업무량이 과다<br>• AI 도입 의향은 높으나 진입 장벽을 느낌<br>• 이곳에 주요 타깃 특징에 대한 내용을 작성해주세요.',54,111,451,20,'line-height:1.8;color:#ddd'),92,351,535,290)
s+=panel(txt('<b>이곳에 고객 분석 페인포인트를 작성하세요.</b>',49,31,470,23)+at('',37,85,461,cl='box dotted')+chip('시간 낭비',44,112,136,37,True)+txt('회의록·보고서 정리에 반복적으로<br>시간 소모된 시간을 작성해보세요',210,114,290,20,'color:#ddd')+chip('도구 이중화',44,194,136,37,True)+txt('별도 AI 툴을 따로 쓰며 미리워크와는<br>단절된 데이터 도출',210,196,290,20,'color:#ddd'),653,351,535,290);slides.append(s)
s=title('핵심 가치와 차별성',"미리AI는 '맥락·통합·보안'에서 범용 AI 도구와 다릅니다.")
for i,(n,d)in enumerate([('업무 맥락 이해','우리 팀의 문서·대화를 바탕으로<br>맥락에 맞게 답변'),('끊김 없는 통합','업무 데이터를 외부 학습에<br>쓰지 않고 격리 처리'),('안전한 보안','미리워크 안에서 앱 전환 없이<br>곧바로 사용')]):
 x=[87,471,859][i];s+=panel(chip(n,36,35,163,43,True)+txt(d,40,103,260,21,'color:#ccc')+ph(154,210,135,143,'3D 자리'),x,230,330,395)
slides.append(s)
s=title('비즈니스 모델','기존 구독에 얹는 AI 프리미엄 서비스로 고객 객단가를 높입니다.')+panel(chip('시장의 문제',190,33,145,43,True)+txt('범용 AI 도구는 업무 맥락을 모르고, 별도 구독·보안<br>우려로 기업 도입이 어렵습니다.',35,92,455,21,'text-align:center;color:#ccc'),91,222,526,191)+arrow(322,415,64,55,'down')+panel(chip('당사 전략',197,34,128,43,True)+txt("미리워크 유료 플랜에 '미리AI'를 추가로 제공해,<br>기존 고객 기반에서 즉시 매출을 확장합니다.",35,95,455,21,'text-align:center;color:#ccc'),91,450,526,192)
s+=panel(chip('미리 AI 추가 제공',169,33,197,43,True)+arrow(235,81,64,55,'down')+at('',36,125,464,260,'panel','background:#25282a;border:0')+chip('기존 플랜에 추가 과금',65,158,406,61),651,222,536,420)
for i,n in enumerate(['사용량<br>기반','팀 단위<br>정액','엔터프라<br>이즈 맞춤']):s+=circ(n,716+i*147,466,112,False,'font-size:21px')
slides.append(s)
s=title('시장 진입 전략','기존 고객에서 시작해 신규·기업 시장으로 확장합니다.')
for i,(n,d)in enumerate([('4단계','<b>외부 확장</b>  |　레퍼런스와 입소문을 지렛대로 신규, 기업 고객까지 확대'),('3단계','<b>조직 표준화</b>  |　팀을 넘어 회사 표준 도구로 정착시켜 객단가 상승'),('2단계','<b>팀 확산</b>  |　한 명의 사용 경험이 팀 전체로 번지는 협업 기반 자연 확산'),('1단계','<b>내부 침투</b>  |　기존 유저에게 무료로 노출해 진입 비용 최소화')]):
 width=214+i*100;y=261+i*78;s+=at(n,336-width/2,y,width,72+i*8,'circle','border-radius:50%;background:linear-gradient(#080b0e,#8b9db0);font-size:23px')+at('',466+i*31,y+28,168-i*31,cl='box dotted')+txt(d,670,y+16,535,20,'color:#ccc')
slides.append(s)
s=title('경쟁 환경 및 자사 포지션',"범용 AI와 협업툴 사이, 미리AI는 '업무 맥락 특화' 영역을 차지합니다.")+panel(at('',82,218,900,cl='box dotted')+at('',555,76,1,295,'box','border-left:1px dotted #999')+chip('협업툴 통합도 높음',475,34,159,39)+chip('협업툴 통합도 낮음',475,368,159,39,True)+chip('업무 맥락 이해도 낮음',47,201,176,41,True)+chip('업무 맥락 이해도 높음',885,201,177,41),85,209,1102,446)
for x,y,n,on in [(382,362,'경쟁사 A',False),(510,501,'경쟁사 B',False),(790,385,'경쟁사 C',True),(857,544,'경쟁사 D',False)]:s+=txt(n,x-50,y-38,100,17,'text-align:center;color:#ccc')+at('',x-7,y-7,14,14,'dot','background:'+('#3982fb'if on else '#444'))
s+=circ('',998,290,51,True,'border-width:13px')+txt('<b>미리 AI</b>',964,253,120,26,'text-align:center')+txt('높은 맥락 이해 +<br>완전 통합으로 차별화',942,350,170,16,'text-align:center');slides.append(s)
s=title('추진 로드맵','하반기 베타부터 엔터프라이즈 출시까지 분기별로 추진합니다.')
for i,(n,d)in enumerate([('AI 베타 오픈','기존 고객을 대상으로 회의록·<br>문서 요약 기능을 우선 공개합니다.'),('유료 서비스 출시','사용량 기반 과금 모델을 적용<br>한 정식 서비스를 출시합니다.<br><br>핵심 기능을 고도화하고 안정<br>적인 수익 모델을 구축합니다.'),('신규 고객 확대','AI 기능을 활용한 마케팅을 강화<br>하여 신규 가입을 확대합니다.<br><br>다양한 프로모션과 콘텐츠를 통<br>해 서비스 이용률을 높입니다.'),('엔터프라이즈 진출','본격적으로 기업 전용 모델과 보<br>안 패키지를 기반으로 B2B 시장<br>을 공략합니다.<br><br>대규모 고객사를 확보하며 엔터프<br>라이즈 사업을 본격 확대합니다.')]):
 x=84+269*i;y=430-78*i;s+=circ(f'{i+1}분기',x,y,63,False,'font-size:21px')+txt(f'<b>{n}</b>',x+77,y-7,240,25)+at('',x+30,y+64,1,609-y-64,'box','border-left:1px dotted #888')+at('',x+62,y+35,230,1,'box','background:#ccc')+txt(d,x+69,y+65,237,20,'color:#ccc;line-height:1.45')
s+=arrow(964,520,220,77,'right');slides.append(s)
s=title('매출 및 성과 목표','')+txt('미리AI는 하반기 신규 매출의 핵심 동력입니다.',342,106,790,22,'color:#ccc')
for y,n,v in [(178,'AI 서비스 신규 매출','30억 원'),(420,'유료 고객 비율','25%')]:s+=panel(chip(n,39,31,179,43,True)+txt('이곳에 해당 수치<br>관련 상세 내용을<br>입력해 보세요.',45,96,183,20,'color:#ccc')+txt(f'<b class="lift">{v}</b>',240,124,180,49),94,y,434,216)
s+=panel(chip('객단가 상승',46,31,115,43,True)+txt('AI 도입 전 대비<br>330% 상승',53,97,160,21,'color:#ccc')+bars([15,50],['도입 전','도입 후'],37,152,540,240,55),560,178,614,458);slides.append(s)
s=title('팀 조직 역량','미리AI는 전담 AI 조직이 책임지고 실행합니다.')+circ('대표이사<br>(CEO)',552,186,176,True,'font-size:24px;border-width:18px')
s+='<svg style="position:absolute;left:0;top:0" width="1280" height="720"><path d="M640 362V397H215V430M640 397H1065V430M499 397V430M783 397V430" fill="none" stroke="#999" stroke-dasharray="1 3"/></svg>'
for i,(n,d)in enumerate([('AI 연구팀','LLM·ML 엔지니어<br>10명'),('프로덕트팀','AI 기능 기획·UX<br>8명'),('영업·마케팅팀','B2B 영업·그로스<br>8명'),('고객성공팀 (CS)','온보딩·기술지원<br>5명')]):s+=chip(n,129+i*283,430,173,48)+panel(txt(d,0,28,220,21,'text-align:center;color:#ccc'),104+i*284,506,220,117)
slides.append(s)
s=title('기대 효과','미리AI는 매출·고객·경쟁력 세 측면에서 효과를 만듭니다.')
for i,(n,d)in enumerate([('신규 매출','기존 유료 고객의 25%가 AI 애드온을<br>추가 구독해, 신규 획득 비용 없이 하반기<br>30억 원의 추가 매출을 확보합니다.'),('고객 생산성 향상','반복 업무를 자동화해 팀당 주 5시간<br>이상을 절감합니다. 고객 만족도와<br>재구독률 (리텐션) 상승으로 이어집니다.'),('경쟁 우위',"'AI가 내장된 협업툴'이라는 차별화로 신규<br>가입 전환을 끌어올리고, 전환 비용을 높여<br>고객 이탈을 방어합니다.")]):s+=panel(txt(f'Benefit 0{i+1}',0,38,343,18,'text-align:center;color:#4f94ed')+txt(f'<b>{n}</b>',0,74,343,27,'text-align:center')+ph(116,126,123,123,'3D 자리')+txt(d,18,274,307,18,'text-align:center;color:#ccc;line-height:1.6'),[87,468,850][i],225,343,402)
slides.append(s)
s=title('위험 요인 및 대응 방안','신규 AI 사업의 핵심 리스크에 대응 체계를 갖췄습니다.')+panel(txt('<b>AI 정확도</b><br><br><b>AI 비용</b><br><br><b>데이터 보안</b>',0,37,167,23,'text-align:center;line-height:1.7'),79,313,168,317)
s+=panel(chip('위험 요인',145,34,155,49,True)+txt('부정확한 답변(환각)으로 인한 신뢰 저하 우려<br><br><br>LLM 호출 비용이 수익성을 압박할 가능성 존재<br><br><br>업무 데이터의 외부 유출에 대한 고객 우려',31,120,385,20,'text-align:center;color:#ccc;line-height:1.35'),272,232,446,398)
s+=panel(chip('대응 방안',145,34,155,49,True)+txt('출처 표기·검증 단계·사용자 피드백 루프로 보완<br><br><br>사용량 과금·경량 모델 병행으로 마진 확보<br><br><br>데이터 격리·미학습 정책·보안 인증으로 신뢰 확보',31,120,385,20,'text-align:center;color:#ccc;line-height:1.35'),757,232,446,398)+arrow(716,440,56,60,'right');slides.append(s)
s=title('협력 제안','AI 모델·인프라 파트너와 함께 미리AI를 성장시킵니다.')+circ('협력사',189,220,258,True,'font-size:32px;background:linear-gradient(120deg,#fff,#73a0c4);color:#182733;border-color:#444')+circ('미리컴퍼니',824,220,258,True,'font-size:32px')+arrow(497,277,274,78,'right')+arrow(497,343,274,78,'right')+txt('사용자 접점·도메인',553,248,220,21)+txt('기타 인프라 지원',572,425,220,21)+panel(txt('클라우드 파트너에게는 <b>대규모 실사용 환경을 제공</b>하고, 미리컴퍼니는 <b>안정적 인프라와 기술을 확보</b>합니다.',0,39,1094,23,'text-align:center;color:#ddd'),87,523,1094,116);slides.append(s)
slides.append(txt('<h1 class="lift" style="font-size:120px">Thank you</h1>',85,137,920)+txt('경청해 주셔서 감사합니다.',86,290,790,36,'color:#ddd')+txt('⌂　미리컴퍼니 사업개발팀<br>☎　02.1234.5678<br>✉　제휴·투자 문의 partner@miridih.com<br>　　일반 문의 hello@miridih.com',85,500,530,21,'color:#ddd;line-height:1.8')+ph(599,292,681,428,'3D 그래픽 자리'))
for i,s in enumerate(slides,1):
 html=f'<!doctype html><html lang="ko"><meta charset="utf-8"><link rel="stylesheet" href="../../../work/reference/fonts/fonts.css"><link rel="stylesheet" href="replica.css"><section class="{"cover"if i in (1,2,18)else ""}">{common()}{s}</section></html>'
 (P/f'slide_{i:02}.html').write_text(html)
(R/'inventory.md').write_text('# 덱 005 전체 이미지 목록\n\n|원본|페이지 유형|해당 계약|\n|---|---|---|\n'+'\n'.join(f'|slide_{i:02}.png|{n}|{c}|' for i,(n,c)in enumerate([('사업계획 표지','foundation cover'),('목차','agenda'),('통합 서비스 허브','hub'),('사업 추진 배경','callout / versus'),('시장 막대 차트','chart-bar / pill / callout'),('제품 개요','card / image-frame'),('고객 분석','metric / gauge / list'),('핵심 가치 3카드','card'),('비즈니스 모델','flowchart / architecture'),('시장 진입 피라미드','pyramid'),('경쟁 포지셔닝','positioning'),('분기 로드맵','timeline'),('매출 목표','metric / chart-bar'),('팀 조직도','hierarchy'),('기대효과 3카드','card'),('리스크 비교','table / versus'),('파트너 제안','versus / delta / callout'),('감사 종료','foundation cover')],1)))
print('replica',len(slides))
