from pathlib import Path
import json,html
ROOT=Path(__file__).parent; REP=ROOT/'replica'; REF=Path('/workspace/work/ref'); SRC=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('058*'))
F='http://127.0.0.1:8765/fonts/fonts.css'
titles={4:('시장 환경의 변화','Why Marketing Matters','급변하는 디지털 시장에서 브랜드 인지도 확보는 기업 생존의 핵심입니다.'),5:('마케팅 목표 및 추진 방향','Marketing Objectives','브랜드와 소비자가 함께 연결되는 선순환 마케팅 체계를 구축합니다.'),6:('기업 및 프로젝트 팀 소개','About Our Agency','브랜드의 성장을 함께 만드는 데이터 기반의 마케팅 파트너입니다.'),7:('우리만의 핵심 차별화','Why Choose Us','브랜드의 목표와 시장 특성을 결합한 맞춤형 솔루션을 제공합니다.'),8:('타겟 세분화 및 계층 구조','Target Framework','고객의 관여도와 특성에 맞춘 단계별 마케팅 메시지를 전달합니다.'),9:('마케팅 실행 분야','Marketing Areas','기업의 목표에 맞추어 다양한 디지털 채널을 통합적으로 운영합니다.'),10:('연간 실행 로드맵','Annual Marketing Roadmap','분기별 단계적인 로드맵을 통해 지속 가능한 성장을 지원합니다.'),11:('프로젝트 운영 프로세스','Execution Process','기획부터 실행, 성과 분석까지 체계적인 단계별 프로세스로 운영합니다.'),12:('세부 실행 프로그램','Campaign Program','채널별 특성에 최적화된 전략적 실행 방안을 제공합니다.'),13:('채널별 집행 가이드','Media Mix & Channel Guide','목표에 따라 효율적인 매체 조합을 구성하여 마케팅 성과를 극대화합니다.'),14:('프로젝트 전담 인력','Our Experts','풍부한 실무 경험을 갖춘 전문 마케팅 팀이 프로젝트를 직접 담당합니다.'),15:('프로젝트 기대 효과','Expected Outcome','마케팅 집행을 통한 실질적인 데이터와 매출 성장을 이끌어냅니다.')}
css='''*{box-sizing:border-box}html,body{margin:0;width:1280px;height:720px;overflow:hidden}body{font-family:'Freesentation',sans-serif;color:#050908}.slide{width:1280px;height:720px;position:relative;overflow:hidden;background:#fff}.bg{position:absolute;inset:104px 0 0;background:radial-gradient(ellipse at 42% 18%,#e3e2de,transparent 47%),radial-gradient(ellipse at 8% 93%,#d8dbd8,transparent 44%),#f6f6f3}.top{position:absolute;left:54px;top:48px;font-size:16px}.brand{position:absolute;right:54px;top:47px;font-size:16px;font-weight:700}.brand:after{content:'';display:inline-block;width:14px;height:14px;border-radius:50%;background:#03c59a;margin-left:18px;box-shadow:-11px 0 #e2e4e2}.rule{position:absolute;left:54px;right:54px;top:103px;height:2px;background:#02c69a}.title{position:absolute;left:54px;top:127px;margin:0;color:#0cc39b;font-size:44px;font-weight:700;line-height:1.15}.sub{position:absolute;left:54px;top:195px;margin:0;color:#0bc199;font-size:22px;font-weight:600}.panel{position:absolute;border-radius:26px;background:#fff;box-shadow:4px 5px #d9d9d9;padding:32px}.card{position:absolute;background:#fff;border-radius:20px;padding:32px;box-shadow:2px 3px #dfdfdd}.kick{font-size:21px;color:#00c89d;font-weight:700;margin:0 0 15px}.name{font-size:27px;font-weight:700;line-height:1.25;margin:0 0 18px}.note{font-size:22px;line-height:1.5;margin:0}.small{font-size:15px;line-height:1.5;color:#727773}.seat{background:#e4e6e5;border-radius:8px;display:flex;align-items:center;justify-content:center;color:#7b8480;font-size:16px}.line{height:1px;background:#18c6a1;margin:18px 0}.badge{background:#00c699;color:#fff;display:flex;justify-content:center;align-items:center;border-radius:999px;font-size:19px;font-weight:600;line-height:1}.circle{border-radius:50%;border:1px solid #b9d8cd;display:flex;align-items:center;justify-content:center;text-align:center;background:#fff}.eyebrow{position:absolute;top:48px;left:54px;color:#fff;font-size:17px}.cover{background:linear-gradient(165deg,#aab6b7 12%,#00cda0 86%);color:white}.cover h1{font-size:88px;line-height:1.14;font-weight:400;position:absolute;left:54px;top:252px;margin:0;letter-spacing:-3px}.cover h1 b{font-weight:800}.cover .desc{position:absolute;left:55px;top:460px;font-size:23px;line-height:1.35;margin:0}.cover .num{position:absolute;left:55px;bottom:45px;font-size:150px;color:#0eb897}.star{color:#00c79b;font-size:40px;font-weight:700}.avatar{border-radius:0;background:#e5e7e5}.muted{color:#818681}.numtitle{color:#00c79d;font-size:58px;margin:0}.arrow{clip-path:polygon(0 0,85% 0,100% 50%,85% 100%,0 100%,15% 50%);background:#999;display:flex;align-items:center;justify-content:center;color:white;font-size:22px}.foot{font-size:15px;color:#777}.dot{border-radius:50%;background:#0dc79d}'''
(REP/'replica.css').write_text(css)
def el(x,y,w,h,content,cls='',style=''):
 return f'<div class="{cls}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;{style}">{content}</div>'
def svg(content,w=1280,h=720):return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="position:absolute;left:0;top:0;pointer-events:none" xmlns="http://www.w3.org/2000/svg">{content}</svg>'
def t(x,y,text,size=20,color='#050908',weight=400,anchor='start'):return f'<text x="{x}" y="{y}" fill="{color}" font-family="Freesentation" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{text}</text>'
def header(n):
 k,title,sub=titles[n];return f'<div class="bg"></div><div class="top">{k}</div><div class="brand">MIRICOM</div><div class="rule"></div><h1 class="title">{title}</h1><p class="sub">{sub}</p>'
def card(x,y,w,h,k,n,note,extra=''):
 return el(x,y,w,h,f'<p class="kick">{k}</p><p class="name">{n}</p><div class="line"></div><p class="note">{note}</p>'+extra,'card')
D={}
rings='<circle cx="960" cy="0" r="165" fill="none" stroke="#25bda1" stroke-width="36" opacity=".55"/><circle cx="960" cy="359" r="180" fill="#b7ead9" opacity=".22"/><circle cx="960" cy="359" r="200" fill="none" stroke="#bcebdc" stroke-width="1"/><circle cx="960" cy="720" r="180" fill="none" stroke="#bcebdc" stroke-width="1"/>'
D[1]=f'<section class="slide cover">{svg(rings)}<div class="eyebrow">Integrated Marketing Solution</div><h1>브랜드 가치를 높이는<br><b>마케팅 전략</b></h1><p class="desc">지속 가능한 성장을 위한 맞춤형 통합 마케팅<br>솔루션을 제안합니다.</p></section>'
contents=[('분석 및 기획',['시장 환경의 변화','마케팅 목표 및 추진 방향','기업 및 프로젝트 팀 소개','우리만의 핵심 차별화'],4),('마케팅 전략',['타겟 세분화 및 계층 구조','마케팅 실행 분야','연간 실행 로드맵','프로젝트 운영 프로세스'],8),('커리큘럼 & 실행',['세부 실행 프로그램','채널별 집행 가이드','프로젝트 전담 인력'],12),('성과 및 계획',['프로젝트 기대 효과'],15)]
s='<section class="slide"><div class="brand">MIRICOM</div><div class="rule"></div><h1 class="title" style="font-size:38px">CONTENTS</h1>'
for i,(name,ls,start) in enumerate(contents):
 x=54+i*300;s+=el(x,307,274,70,f'0{i+1}','numtitle')+el(x,374,274,300,f'<h2 style="font-size:28px;margin:26px 26px 22px">{name}</h2>'+''.join(f'<div style="font-size:18px;margin:0 26px 12px;display:flex;justify-content:space-between"><span>{v}</span><span style="color:#00be94">{start+j:02}</span></div>' for j,v in enumerate(ls)),style='border-top:2px solid #00c89d;background:linear-gradient(#e6e5e1,#fff)')
D[2]=s+'</section>'
D[3]=f'<section class="slide cover">{svg("<circle cx=\"1080\" cy=\"80\" r=\"165\" fill=\"none\" stroke=\"#22b99b\" stroke-width=\"60\" opacity=\".32\"/><circle cx=\"840\" cy=\"680\" r=\"350\" fill=\"none\" stroke=\"#a5dfd0\" stroke-width=\"5\"/><circle cx=\"840\" cy=\"680\" r=\"330\" fill=\"#b2e6d8\" opacity=\".22\"/>")}<div class="eyebrow">Marketing Proposal</div><h1 style="top:180px;font-size:72px;font-weight:700;line-height:1.15">시장 환경 분석 및<br>제안 배경</h1><div class="num">01</div></section>'
# 4 chart
s=header(4)+el(54,273,360,160,'<p class="name">마케팅 투자 비중과 매출 성장률</p><p class="note" style="font-size:22px">통합 마케팅을 지속한 기업일수록<br>브랜드 전환율과 장기 매출 성장세가<br>뚜렷하게 나타납니다.</p>')
chart='<line x1="0" y1="266" x2="690" y2="266" stroke="#999"/>'
vals=[120,200,310,580];pts=[]
for i,v in enumerate(vals):
 x=30+i*172;h=v/580*132;chart+=f'<rect x="{x}" y="{266-h}" width="114" height="{h}" rx="10" fill="#00c798"/>'+t(x+57,266-h+26,str(v),18,'#fff',400,'middle')+t(x+57,287,['2023','2024','2025','2026(예상)'][i],18,'#050908',400,'middle');py=[225,211,185,119][i];pts.append((x+57,py))
chart+='<polyline points="'+' '.join(f'{x},{y}' for x,y in pts)+'" stroke="#777" stroke-width="1" stroke-dasharray="2 2" fill="none"/>'
for (x,y),v in zip(pts,[180,240,350,650]):chart+=f'<circle cx="{x}" cy="{y}" r="5" fill="white" stroke="#666" stroke-width="2"/>'+t(x,y-15,str(v),17,'#555',400,'middle')
s+=el(460,269,766,399,'<p class="name" style="font-size:25px;margin:0">연도별 마케팅 투자 대비 매출 성과 추이</p><div class="line"></div><p style="text-align:center;font-size:16px">■마케팅 성과 매출액 ○평균 고객 전환율</p>'+el(38,48,690,300,svg(chart,700,300))+'<p class="foot" style="position:absolute;bottom:14px">* 최근 3개년 마케팅 데이터 및 2026년 예상 성과 지표 기준</p>','panel');D[4]='<section class="slide">'+s+'</section>'
# 5
s=header(5)
for i,(name,note) in enumerate([('브랜드 인지도 제고','타겟 고객 접점 확대 및 차별적<br>브랜드 이미지 구축'),('전환율 극대화','데이터 기반의 정밀 타겟팅을<br>통한 실질적 구매 전환'),('팬덤 형성','지속적인 소통 및 커뮤니티<br>운영을 통한 재구매율 향상')]):
 s+=card(54+i*407,269,360,400,f'Goal 0{i+1}.',name,note,'<p class="small" style="margin-top:26px">다양한 디지털 채널을 통해 브랜드 노출을<br>확대하고 고객 가치를 극대화합니다.<br><br>데이터 분석을 바탕으로 시장과 소비자의<br>변화를 빠르게 반영합니다.</p>')
D[5]='<section class="slide">'+s+'</section>'
# 6
s=header(6)+el(170,292,286,315,'',style='border:1px dashed #a6d3c3;border-radius:50%')
for x,y,note,latin in [(54,355,'실용성','PRACTICAL'),(320,259,'전문성','PROFESSIONAL'),(296,506,'협력','PARTNERSHIP')]:s+=el(x,y,172,172,f'<div><b style="font-size:23px">{note}</b><br><span style="font-size:14px;color:#00b98f">{latin}</span></div>','circle')
s+=el(555,276,670,370,'사진 placeholder','seat');D[6]='<section class="slide">'+s+'</section>'
#7
s=header(7)
for i,(name,note,icon) in enumerate([('맞춤형 전략 수립','철저한 데이터 분석 기반의 미디어 믹스 설계','presentation'),('실무 중심 실행','검증된 캠페인 제작을 활용한 신속한 운영','briefcase-business'),('크리에이티브 마케팅','시선을 사로잡는 독창적 콘텐츠 제작','lightbulb'),('성과 및 ROI 관리','실시간 리포팅을 통한 실행 성과 측정 및 최적화','chart-no-axes-combined')]):
 x=54+i%2*600;y=269+i//2*220;icon_svg=svg(['<rect x="10" y="15" width="65" height="50" rx="3"/><path d="M6 11h73v8H6zM42 65v13M30 78h24M22 30v16h16V30zM47 31h17M47 41h17M22 55h42"/>','<rect x="12" y="26" width="60" height="45" rx="4"/><path d="M29 26v-9h26v9M12 43h60M35 40v8h15v-8"/>','<path d="M29 58C5 31 22 8 42 8s37 23 13 50v14H29zM29 60h26M29 67h26M34 77h16M42 0v-8M12 8 6 2M72 8l6-6"/>','<path d="M10 75V43h14v32M35 75V29h14v46M60 75V10h14v65M9 29l22-12 20 3L72 0"/>'][i],85,85).replace('<svg ','<svg fill="none" stroke="#17251f" stroke-width="2" ')
 s+=el(x,y,574,184,f'<div class="badge" style="width:52px;height:52px;position:absolute;left:25px;top:0;border-radius:9px">0{i+1}</div><p class="name" style="margin-top:43px">{name}</p><p class="note">{note}</p><span style="position:absolute;right:32px;top:45px;width:90px;height:90px">{icon_svg}</span>','card')
D[7]='<section class="slide">'+s+'</section>'
#8
s=header(8);sh=''
for i,(a,b,name,sub) in enumerate([(286,174,'VIP (충성 고객)','브랜드 앰배서더 및 전용 혜택 제공'),(286,245,'LOYAL (재구매 고객)','리텐션 마케팅 및 리워드 프로그램'),(286,315,'POTENTIAL (잠재 고객)','프로모션 및 개인화 콘텐츠 연결'),(286,385,'NEW (신규 유입)','대중 노출 캠페인 및 인지도 확보')]):
 y=250+i*100;wid=100+i*110;sh+=f'<polygon points="{a-wid//2+35 if i else a},{y} {a+wid//2-35 if i else a},{y} {a+wid//2},{y+84} {a-wid//2},{y+84}" fill="{["#cbd1ce","#aeb3b0","#929794","#626965"][i]}"/>'
 sh+=f'<circle cx="{a}" cy="{y+55}" r="7" fill="#06c69b" stroke="white" stroke-width="3"/>'
 s+=el(565,y+30,265,38,name,'badge')+el(900,y+36,330,38,sub,style='font-size:17px')
s+=el(0,0,1280,720,svg(sh));D[8]='<section class="slide">'+s+'</section>'
#9
s=header(9)
for i,name in enumerate(['퍼포먼스 광고','SNS 브랜딩','SEO 최적화','콘텐츠 제작','바이럴 마케팅','CRM 관리']):
 x=65+i*192;s+=el(x,403,208,100,f'STEP 0{i+1}','arrow',f'background:{["#d8dad8","#bfc3c1","#a6abaa","#8c9390","#6e7773","#00c79b"][i]}')+el(x+10,278 if i%2==0 else 592,190,40,name,style='font-size:23px;font-weight:700;text-align:center')+el(x+103,330 if i%2==0 else 503,1,72,'',style='border-left:1px solid #777')+el(x+96,395 if i%2==0 else 495,15,15,'','dot')
D[9]='<section class="slide">'+s+'</section>'
#10
s=header(10)
for i,(name,note) in enumerate([('기반 구축','브랜드 리뉴얼<br>및 타겟팅'),('인지도 확산','대규모 퍼포먼스<br>캠페인 집행'),('전환 극대화','시즌 프로모션 및<br>CRM 운영'),('성과 분석 & 재정비','연간 데이터 리포트 도출<br>및 내년도 기획')]):
 x=54+i*300;s+=el(x,288,275,50,f'<span class="badge" style="width:58px;height:34px;display:inline-flex">{i+1}Q</span> <b>{name}</b>',style='font-size:20px')+el(x,346,300,3,'',style='background:#789b8d')+el(x,382,275,278,f'<p class="name" style="font-size:25px;text-align:center">{note}</p><p class="small" style="margin-top:30px;color:#333;font-size:19px">• 시장 현황 진단 및 경쟁사 미디어<br>　믹스 분석<br><br>• 고객 데이터 분석 및 핵심 메시지<br>　도출<br><br>• 실행 과제 우선순위와 세부 일정<br>　확정</p>',style='border-right:1px solid #ddd;padding-right:24px')
D[10]='<section class="slide">'+s+'</section>'
#11
s=header(11)
for i,(name,note) in enumerate([('니즈 분석','사전 진단·인터뷰 및<br>브랜드 과제 도출'),('전략 기획','맞춤형 미디어 믹스<br>설계 및 예산안 수립'),('캠페인 집행','광고 소재 제작 및<br>실시간 최적화 운영'),('성과 평가','주간/월간 성과 지표<br>점검 및 개선 도출'),('사후 관리','핵심 데이터 기반의<br>고객 관계 강화 전략')]):
 x=110+i*205;s+=el(x,275,240,240,f'<div style="font-size:23px;font-weight:700">{i+1}. {name}</div>','circle',f'border:30px solid {"#65d5b6" if i==4 else "#c9ccca"};background:transparent')+el(x,554,240,90,note,style='font-size:20px;text-align:center;line-height:1.4')
D[11]='<section class="slide">'+s+'</section>'
#12
s=header(12)+el(54,247,1172,45,'<span class="badge" style="width:240px;height:40px;margin:auto">캠페인 목표</span>',style='border:1px solid #c5c9c6;border-radius:22px')+el(200,307,880,35,'온라인 매출 전년 대비 150% 증대 및 브랜드 인지도 강화',style='font-size:24px;font-weight:700;text-align:center')
for i,name in enumerate(['검색 광고','디스플레이','숏폼 콘텐츠','체험단 운영']):
 x=54+i*300;s+=el(x,360,275,310,f'<div class="badge" style="width:70px;height:35px">0{i+1}</div><p class="name" style="font-size:24px;margin-top:14px">{name}</p><div class="seat" style="height:170px">이미지 placeholder</div>','card','padding:22px')
D[12]='<section class="slide">'+s+'</section>'
#13
s=header(13);rows=[('SNS 매체 (인스타그램/페북)','2030 세대 / 감성 소비층','트렌디한 숏폼 및 카드뉴스 기반 브랜드 브랜딩','매일 상시'),('검색 매체 (네이버/구글)','제품 의도가 명확한 유저','콘텐츠 검색 키워드를 통한 전환 & 구매 유도','상시 집행'),('디스플레이 (카카오/GDA)','브랜드 타겟 유저층','핵심 소구 메시지를 통한 관심 유발 및 도달 확장','주 3–4회'),('영상 매체 (유튜브)','전 연령층 / 고관여 유저','브랜드 스토리텔링 및 제품정보 콘텐츠 활용','주 2회'),('커뮤니티 (카페/블로그)','정보 탐색형 유저','실제 사용 후기 기반 신뢰도 및 전환율 제고','주 4–8회'),('CRM 채널 (알림톡/메일)','기존 충성 및 재구매 유저군','개인화 쿠폰 제공 및 시즌 프로모션 알림 발송','주/월 2회')]
s+=el(54,258,1172,411,'<table style="width:100%;border-collapse:collapse;font-size:20px"><thead><tr style="background:#00c89b;color:white">'+''.join(f'<th style="height:44px;border-right:1px solid white">{x}</th>' for x in ['주요 채널','주 타겟층','핵심 집행 전략','진행 주기'])+'</tr></thead><tbody>'+''.join('<tr style="background:'+('#eeefed' if i%2==0 else '#f7f8f5')+'">'+''.join(f'<td style="height:61px;padding:8px 12px;border-right:1px solid #ddd">{x}</td>' for x in row)+'</tr>' for i,row in enumerate(rows))+'</tbody></table>');D[13]='<section class="slide">'+s+'</section>'
#14
s=header(14)
for i,(name,role,note) in enumerate([('김미리','총괄 디렉터','퍼포먼스 마케팅 10년 경력 /<br>대기업 캠페인 총괄'),('박미리','수석 컨설턴트','콘텐츠 기획 및 브랜딩 전문가 /<br>누적 매출 300억+'),('이미리','미디어 플래너','데이터 기반 및 디지털 매체 운영<br>전문가')]):
 s+=el(54+i*400,269,380,400,f'<span class="star">*</span><div class="seat avatar" style="position:absolute;left:110px;right:32px;top:30px;height:258px">인물 placeholder</div><p style="position:absolute;left:32px;top:238px;font-size:16px">{role}<br><b style="font-size:29px">{name}</b></p><div style="position:absolute;left:32px;right:32px;bottom:95px;border-top:1px solid #00bd92"></div><p class="note" style="position:absolute;left:32px;bottom:26px">{note}</p>','card')
D[14]='<section class="slide">'+s+'</section>'
#15 gauges
s=header(15)
for i,(name,v,note,pct) in enumerate([('ROI','320%','브랜드 인지도 및<br>선호도 상승',80),('전환율','4.5%','신규 고객 유입량 및<br>구매 전환율 대폭 개선',1),('신규 유입','10만+','자사몰 데이터 확보를 통한<br>장기적 자산화',100)]):
 x=54+i*390;arc=f'<path d="M 40 180 A 140 140 0 0 1 320 180" fill="none" stroke="#fff" stroke-width="50" stroke-linecap="round"/><path d="M 40 180 A 140 140 0 0 1 320 180" fill="none" stroke="#00c89b" stroke-width="50" stroke-linecap="round" pathLength="100" stroke-dasharray="{pct} 100"/>'
 s+=el(x,272,370,230,svg(arc,370,230))+el(x,384,370,100,f'<span style="font-size:25px">{name}</span><br><b style="font-size:54px;line-height:1">{v}</b>',style='text-align:center')+el(x+180,492,1,60,'',style='border-left:1px dashed #888')+el(x,579,370,80,note,style='font-size:26px;font-weight:700;line-height:1.25;text-align:center')
D[15]='<section class="slide">'+s+'</section>'
for n,body in D.items():(REP/f'slide_{n:02}.html').write_text(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><link rel="stylesheet" href="{F}"><link rel="stylesheet" href="replica.css"></head><body>{body}</body></html>')
(ROOT/'slides.json').write_text(json.dumps({str(k):v for k,v in titles.items()},ensure_ascii=False,indent=2))
types=[('표지','foundation.cover, headline, prose'),('목차','agenda, card'),('섹션 표지','foundation.cover, headline'),('복합 막대·선 차트','chart-bar, chart-line, legend, prose'),('목표 3카드','card, tag'),('기업 소개 및 사진','cycle, image-frame'),('차별화 4카드','card, tag'),('고객 피라미드','pyramid, pill'),('실행 단계','steps'),('연간 실행 로드맵','roadmap, timeline'),('원형 프로세스','cycle, steps'),('프로그램 4카드','card, image-frame'),('채널 가이드 표','table'),('전문가 프로필','person'),('성과 반원 게이지','gauge, metric')]
(ROOT/'inventory.md').write_text('# 058 이미지 목록 및 작업 범위\n\n원본 15장, 각 1280×720. 컬렉션 `halo-field`: foundation 및 56개 요소 전체.\n\n| 이미지 | 페이지 유형 | 계약 대응 |\n|---|---|---|\n'+''.join(f'| slide_{i:02}.png | {a} | {b} |\n' for i,(a,b) in enumerate(types,1)))
print('replica',len(D))
