from pathlib import Path
import shutil,html,json
R=Path('/workspace/work/deliverables/diecut');V=R/'review';P=V/'replica'
font=Path('/workspace/work/reference/fonts/artifacts/pretendard/PretendardVariable.woff2');shutil.copy(font,V/'assets/PretendardVariable.woff2')
for f in Path('/workspace/work/reference/fonts/artifacts/suite').glob('*.woff2'):shutil.copy(f,V/'assets'/f.name)
CSS='''@font-face{font-family:wordmark;src:url('../assets/PretendardVariable.woff2');font-weight:100 900}*{box-sizing:border-box}html,body{margin:0;width:1280px;height:720px;overflow:hidden}body{font-family:p,sans-serif;color:#000;background:#e0e0e0}.slide{position:relative;width:1280px;height:720px;overflow:hidden}.tx,.bx{position:absolute}.tx{margin:0;line-height:1.4;white-space:pre-line;word-break:keep-all}.ph{background:#dedede;position:absolute;display:flex;align-items:center;justify-content:center;color:#888;font-size:14px}.nav{position:absolute;left:277px;top:37px;width:726px;height:39px;background:#000;border-radius:999px;display:flex;align-items:center;justify-content:center;gap:20px;font-size:18px;color:#666}.nav span,.nav b{white-space:nowrap}.nav b{color:#deff3c;font-weight:700}.tri{width:0;height:0;border-top:6px solid transparent;border-bottom:6px solid transparent;border-left:10px solid #666}.center{text-align:center}table{border-collapse:collapse;width:100%;height:100%;font-size:18px;text-align:center;line-height:1.1}td,th{border:1px solid #aaa;font-weight:400}th,td:first-child{background:#e0e0e0}td{background:#fff}tr{height:53.5px}ul{padding:0;margin:0;list-style:none}li{margin:3px 0}li:before{content:'•';margin-right:9px}svg{position:absolute;overflow:visible}.shape{position:absolute}'''
CSS+='ul.check li:before{content: "";display:inline-block;width:6px;height:11px;border-right:2px solid #000;border-bottom:2px solid #000;transform:rotate(45deg);margin-right:8px}'
CSS+=''.join(f"@font-face{{font-family:p;src:url('../assets/SUITE-{name}.woff2');font-weight:{w};}}"for name,w in [('Light',300),('Regular',400),('Medium',500),('SemiBold',600),('Bold',700),('ExtraBold',800),('Heavy',900)])
CSS+="@font-face{font-family:wordmark;src:url('../assets/PretendardVariable.woff2');font-weight:100 900;}"
P.joinpath('replica.css').write_text(CSS)
def tx(s,x,y,w,h=None,size=20,weight=400,align='left',extra=''):
 return f'<div class="tx" style="left:{x}px;top:{y}px;width:{w}px;{f"height:{h}px;" if h else ""}font-size:{size}px;font-weight:{weight};text-align:{align};{extra}">{s}</div>'
def box(x,y,w,h,c='#fff',r=0,border='',extra=''):
 return f'<div class="bx" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{c};border-radius:{r}px;{f"border:{border};" if border else ""}{extra}"></div>'
def ph(x,y,w,h,n=1,r=0):return f'<div class="ph" data-ph="{n}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{r}px">{n}</div>'
def pill(s,x,y,w,h=42,size=26,c='#deff3c',weight=700):return box(x,y,w,h,c,999)+tx(s,x,y,w,h,size,weight,'center',f'display:flex;align-items:center;justify-content:center;line-height:1;')
def title(s,y=145):return tx(s,70,y,1140,size=40,weight=800,align='center',extra='line-height:1.15;letter-spacing:-1px;')
chap=['회사 소개','로봇 자동화의 필요성','솔루션 개요','협동로봇 라인업','산업용 로봇 라인업','적용 공정 ① 조립·검사','적용 공정② 용접·도장','적용 공정③ 포장·물류','도입 효과','구축 프로세스','고객 성공 사례','인증','파일럿 제안','문의&마무리']
def plate():
 return '<svg width="1280" height="720" viewBox="0 0 1280 720"><path fill="#f6f6f6" d="M50 20 H1230 Q1260 20 1260 50 V255 Q1260 272 1243 283 Q1230 292 1230 308 V410 Q1230 427 1243 438 Q1260 449 1260 465 V670 Q1260 700 1230 700 H50 Q20 700 20 670 V465 Q20 449 37 438 Q50 427 50 410 V308 Q50 292 37 283 Q20 272 20 255 V50 Q20 20 50 20Z"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="8.5" fill="#c9c9c9"/>'for x in [28,1252]for y in[304,416])+'</svg>'
def base(active=None,style='plate'):
 s=plate()if style=='plate' else box(0,0,1280,720,'#f6f6f6' if style=='plain' else '#e0e0e0')
 s+=tx('MIRIROBOTICS',97,47,170,size=14)+tx('SOLUTION PROPOSAL',1053,47,180,size=14)
 if active is not None:
  prev=f'{active:02}. {chap[active-1]}'if active>0 else ''
  cur=f'{active+1:02}. {chap[active]}'
  nxt=f'{active+2:02}. {chap[active+1]}'if active<13 else ''
  s+=f'<div class="nav"><span>{prev}</span><i class="tri"></i><b>{cur}</b>'+('<i class="tri"></i><span>'+nxt+'</span>' if nxt else '')+'</div>'
 return s

def ul(items,x,y,w,size=18,align='left',line=1.5):return tx('<ul>'+''.join('<li>'+a+'</li>'for a in items)+'</ul>',x,y,w,size=size,align=align,extra=f'line-height:{line};')
def svg(content,x,y,w,h,vb=None):return f'<svg xmlns="http://www.w3.org/2000/svg" style="left:{x}px;top:{y}px" width="{w}" height="{h}" viewBox="{vb or f"0 0 {w} {h}"}">{content}</svg>'
def icon(kind,x,y,size=82):
 paths={'shield':'<path d="M12 3 3 7v6c0 5 9 9 9 9s9-4 9-9V7Z"/><path d="M8 12h8v5H8z"/>','atom':'<ellipse cx="12" cy="12" rx="11" ry="4"/><ellipse cx="12" cy="12" rx="11" ry="4" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="11" ry="4" transform="rotate(120 12 12)"/><circle cx="12" cy="12" r="1"/>','tools':'<path d="m4 4 16 16M3 8l5-5m8 2 3-2 2 2-2 3-3 1-8 8-1 3-2 1-2-2 1-2 3-1 8-8Z"/><path d="M3 14v8h18v-8"/>','robot':'<path d="M2 21h20M4 21v-6h5l4-6-4-4 4-3 5 4-1 4-5 7v4M9 5l-3 5m-2 0 4 2 3-4m3 2 4 2 3-5"/><circle cx="14" cy="6" r="1"/><circle cx="9" cy="17" r="1"/>'}
 return svg('<g fill="none" stroke="#000" stroke-width=".8" stroke-linejoin="round" stroke-linecap="round">'+paths.get(kind,paths['robot'])+'</g>',x,y,size,size,'0 0 24 24')
slides={}
s=box(0,0,1280,720,'#f6f6f6')+ph(635,0,645,720)+tx('작업은 스마트하게',62,62,180,size=18)+box(198,71,126,1,'#000')+tx('성과는 압도적으로',334,62,200,size=18)
s+=tx('MIRIROBOTICS',48,211,1190,size=142,weight=400,extra='font-family:wordmark;letter-spacing:0;line-height:1.15;')+tx('사람과 함께 일하는 로봇',56,509,500,size=24,weight=550)
s+=tx('<span style="background:linear-gradient(transparent 55%,#deff3c 55%);padding:0 7px">미리로보틱스</span><br><span style="background:linear-gradient(transparent 55%,#deff3c 55%);padding:0 7px">협동로봇 솔루션 제안서</span>',49,554,660,size=44,weight=800,extra='line-height:1.2;')+tx('<b>2055. 00. 00.</b>\n미리로보틱스 마케팅팀 김미리',1008,610,250,size=20)
slides[1]=s
s=base(None,'plain').replace('left:97px','left:264px')+tx('CONTENTS',15,0,200,720,size=146,extra='font-family:wordmark;writing-mode:vertical-rl;transform:rotate(180deg);line-height:1;letter-spacing:-6px;')
labels=['회사 소개','로봇 자동화의 필요성','솔루션 개요','협동로봇 라인업','산업용 로봇 라인업','적용 공정 ① 조립·검사','적용 공정 ② 용접·도장','적용 공정 ③ 포장·물류','도입 효과 (ROI 포함)','파일럿 제안 & 문의']
for row in range(2):
 y=282+222*row;s+=box(266,y,935,1,'#000')
 for j in range(5):
  x=270+j*188;s+=tx(f'{row*5+j+1:02}',x,195+222*row,175,size=58,weight=250,align='center')+box(x+79,y-8,18,18,'#000',999)+tx(labels[row*5+j],x,318+222*row,175,size=18,align='center')
s+=svg('<path d="M0 90 90 0v90Z" fill="#deff3c"/>',1190,630,90,90);slides[2]=s
s=base(0)+ph(728,96,552,624)+tx('MIRIROBOTICS',190,127,440,size=56,extra='letter-spacing:-2px;')+pill('핵심 사업 영역',208,222,345)
s+=box(208,275,345,138,'#fff',24)+ul(['협동로봇·산업용 로봇 시스템 통합(SI)','자동화 라인 설계·구축 컨설팅','로봇 비전·AI 통합 솔루션','원격 모니터링·유지보수·A/S'],220,295,322,size=18,align='center',line=1.3)
s+=svg('<path d="M380 413v48H129v47m251-47h247v47M294 461v47m165-47v47" fill="none" stroke="#aaa"/>',0,0,700,660)
for i,(a,b)in enumerate([('납품','3,500대+'),('고객사','280개사+'),('업력','14년'),('고객만족도','98%')]):
 x=55+i*165;s+=box(x,508,150,150,'#deff3c',999)+tx(a,x,552,150,size=23,align='center')+tx(b,x,582,150,size=28,weight=750,align='center')
s+=pill('설립  2050년',747,577,250,54,24,'#000',600).replace('font-weight:600;','font-weight:600;color:#fff;')+pill('임직원  120명',1009,577,250,54,24,'#000',600).replace('font-weight:600;','font-weight:600;color:#fff;')+pill('본사  미리도 미리시 미래산업단지',747,646,512,54,23,'#000',600).replace('font-weight:600;','font-weight:600;color:#fff;');s+=svg('<g fill="none" stroke="#fff" stroke-width="2"><path d="M779 614v-21h18v21m-14-15h2m5 0h2m-9 5h2m5 0h2m-6 10v-5h4v5"/><circle cx="1030" cy="594" r="3"/><path d="M1025 612v-12h10v12m-8-8v10m6-10v10"/><path d="M790 657c-9 0-13 9-8 16l8 11 8-11c5-7 1-16-8-16Z"/><circle cx="790" cy="666" r="3"/></g>',0,0,1280,720)
slides[3]=s
s=base(1)+title('왜 지금 자동화인가?',160)
items=[('제조 인력난','심화되는 제조 인력난',['제조업 취업자 지속 감소 추세','3D 업종 기피로 숙련공 확보 난항','생산직 채용비·교육 기간 급증','월말 공석으로 납기 지연 반복 발생'],'핵심 수치: 제조업 구인 미충원율 18.7%'),('품질 기준 상승','초정밀 품질 기준 요구',['전기차·반도체·의료기기 등 고부가 산업 확대','0ppm 불량 기준 요구 증가','사람이 수행 불가한 반복·정밀 작업 증가','납품 품질 이슈 = 거래선 상실 직접 리스크'],'핵심 수치: 주요 OEM 불량 허용 3ppm 이하'),('인건비·운영비 급등','인건비·운영비 구조적 상승',['최저임금 연평균 5.2% 인상','4대 보험·복리후생 포함 실질 인건비 부담 가중','로봇 TCO 대비 경제성 역전 시점 도래','야간·특수 수당 없는 24시간 가동 실현 가능'],'핵심 수치: 제조업 구인 미충원율 18.7%')]
for j,(a,b,ls,foot)in enumerate(items):
 x=104+j*363;s+=pill(a,x,266,345)+box(x,319,345,296,'#fff',24)+tx(b,x+15,348,315,size=22,weight=700,align='center')+ul(ls,x+15,401,315,size=16,align='center',line=1.25)+box(x+35,532,290,1,'#000')+tx(foot,x+15,559,315,size=18,weight=700,align='center')
slides[4]=s
s=base(1)+tx('글로벌 로봇 시장 현황',148,156,480,size=40,weight=750)+tx('글로벌 산업용 로봇 설치 대수 & 시장 규모 추이\n(2020~2027E)',148,224,480,size=22)+pill('핵심 인사이트',148,318,345)+box(148,371,345,235,'#fff',24)+ul(['글로벌 로봇 시장 CAGR 13.2%','협동로봇 특히 CAGR 27.5% 성장','한국, 로봇 밀도 세계 1위\n(제조업 1만 명당 1,012대)','자동차·전자·물류 도입 급증','소형 협동로봇 가격 하락세 지속','2027년 시장 규모 145B$ 전망'],167,400,308,size=18,align='center',line=1.35)
vals=[38.4,51.7,55.3,59.1,63.5,68,73.2,79];line=[44,58,68,78,91,107,124,145];a=''
for v in [0,50,100,150]:
 y=602-v/150*425;a+=f'<path d="M631 {y}H1135" stroke="#ccc"/><text x="622" y="{y+6}" text-anchor="end" font-family="p" font-size="18">{v}</text>'
pts=[]
for i,(v,t)in enumerate(zip(vals,line)):
 x=644+i*63;y=602-v/150*425;cy=602-t/150*425;pts.append(f'{x+18},{cy}')
 a+=f'<rect x="{x}" y="{y}" width="38" height="{602-y}"/><text fill="white" font-family="p" font-size="18" x="{x+19}" y="{y+25}" text-anchor="middle">{v:g}</text><text font-family="p" font-size="18" x="{x+19}" y="625" text-anchor="middle">{"2080E" if i==5 else str(2020+i)+("E" if i>3 else "")}</text><circle cx="{x+18}" cy="{cy}" r="4.5"/><text font-family="p" font-size="18" x="{x+18}" y="{cy-14}" text-anchor="middle">{t}</text>'
a+='<polyline points="'+' '.join(pts)+'" fill="none" stroke="black" stroke-width="1.5"/>';s+=svg(a,0,0,1280,720);slides[5]=s
s=base(2)+title('ONE-STOP 자동화 솔루션',135)
data=[('협동로봇\n공급','UR·FANUC·두산로보\n틱스 공식 파트너\n소형 3kg ~ 대형 25kg\n풀 라인업 보유','robot'),('산업용 로봇\n공급','6축·스카라·델타·갠트리\n전 기종\n수직·수평·병렬 타입\n맞춤 선정 공급','robot'),('자동화 라인\n설계','공정 분석·레이아웃·3D\nCAD 시뮬레이션\n안전 설계(Risk\nAssessment)\n포함 제공','robot'),('비전·AI\n시스템','2D·3D 비전 /\nAI 딥러닝 검사 통합\n외관결함·치수·바코드\nONE 솔루션','shield'),('안전 시스템\n통합','안전 펜스·레이저\n스캐너·라이트커튼\nISO 10218-2 준거\nSafety 설계 보증','atom'),('유지보수\n·A/S','24시간 원격 모니터링·\n현장 출동\n예방 PM·소모품 교체\n·SW 버전 업데이트','tools')]
for j,(a,b,k)in enumerate(data):
 x=101+j*182;s+=box(x,231,165,470,'#fff',85)+box(x,320,165,380,'#fff')+(ph(x+42,267,82,82,j+1)if j<3 else icon(k,x+42,267,82))+tx(a,x+8,371,149,size=23,weight=700,align='center',extra='line-height:1.1;')+tx(b,x+4,454,157,size=16,align='center',extra='line-height:1.38;')+tx(f'{j+1:02}',x,600,165,size=59,weight=250,align='center')
slides[6]=s
s=base(3,'grey')+title('코봇 제품 라인업',119)
products=[('3e','3 kg','500 mm','±0.03 mm','탁상형 소형 설치 최적. 정밀 조립·검사·납땜·반도체\n공정 특화. 클린룸 대응 가능.'),('10e','10 kg','1,300 mm','±0.03 mm','범용 협동로봇 대표 모델. 조립·포장·팔레타이징·\n머신텐딩 전방위 대응. 납기 최단.'),('16e','16 kg','900 mm','±0.05 mm','고하중 협동 작업 특화 모델. 중량 부품 이송·프레스·\n다이캐스팅 머신텐딩 최적.'),('25e','25 kg','1,700 mm','±0.05 mm','협동로봇 최대 하중 클래스. 팔레타이징·물류 자동화·\n야간 무인 운전에 최적화.')]
for j,(m,p,r,pr,n)in enumerate(products):
 x=20+(j%2)*630;y=208+(j//2)*255;s+=box(x,y,610,237,'#fff',20)+ph(x+375,y+8,220,225,j+1)+tx('MR-Cobot\n'+m,x+24,y+17,350,size=42,extra='line-height:1.15;letter-spacing:-1.5px;')+tx(f'가반하중: {p} / 도달거리: {r}\n반복정밀도: {pr} / 자유도: 6축 / IP등급: IP54\n특징: {n}',x+24,y+126,340,size=15,extra='line-height:1.45;')
 if j==1:s+=pill('BEST SELLER',x+100,y+77,120,30,14)
slides[7]=s
s=base(3)+tx('코봇 모델별 스펙 비교표',106,159,450,size=40,weight=750)+tx('공정별 추천 가이드',106,462,330,size=23,weight=700)+box(106,501,321,1,'#000')+tx('소형 정밀 작업(납땜·PCB 조립) → 3e 추천\n범용 조립·포장 공정 → 10e 추천\n중량물 머신텐딩·프레스 공정 → 16e 추천\n팔레타이징·물류·고하중 협동 → 25e / Pro 추천',106,518,410,size=18)
rows=[['모델명','MR-Cobot<br>3e','MR-Cobot<br>10e','MR-Cobot<br>16e','MR-Cobot<br>25e','MR-Cobot<br>Pro'],['가반 하중','3 kg','10 kg','16 kg','25 kg','30 kg'],['도달 거리','500 mm','1,300 mm','900 mm','1,700 mm','1,850 mm'],['반복 정밀도','±0.03 mm','±0.03 mm','±0.05 mm','±0.05 mm','±0.02 mm'],['자유도','6축','6축','6축','6축','7축'],['TCP 최고속도','1.0 m/s','1.5 m/s','1.5 m/s','1.0 m/s','2.0 m/s'],['동작 온도','0~50°C','0~50°C','0~50°C','0~50°C','-10~55°C'],['IP등급','IP54','IP54','IP54','IP54','IP67'],['협동 인증']+['ISO/TS<br>15066']*5]
s+=f'<div class="bx" style="left:554px;top:146px;width:620px;height:482px;border-radius:20px;overflow:hidden"><table><thead><tr>'+''.join('<th>'+a+'</th>'for a in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+a+'</td>'for a in row)+'</tr>'for row in rows[1:])+'</tbody></table></div>';slides[8]=s
s=base(4,'grey')+title('산업용 로봇 제품 라인업',119)
prods=[('6축 다관절 로봇','모델: MR-Arc 200\n가반하중: 200 kg / 도달거리: 2,700 mm\n반복정밀도: ±0.06 mm / 자유도: 6축\n주요 기능: 고속·고강성 설계. 아크용접 패키지 기본 탑재.\n협소 공간 경로 최적화. 용접 비드 품질 비전 자동 검사.\n적용: 자동차 부품 용접·도장·핸들링·머신텐딩. 철구조물·\n압력용기 용접. 선박 부재 가공.'),('스카라(SCARA) 로봇','모델: MR-Pick 6\n가반하중: 6 kg / 동작 반경: 650 mm\n사이클타임: 0.3초 / 반복정밀도: ±0.01 mm\n주요 기능: 수평 고속 반복 동작 특화. 클린룸 대응 전용 모\n델 라인업. 드라이버·나사 피더 통합 패키지.\n적용: PCB 조립·부품 공급·픽앤플레이스·검사. 전자·반도\n체·의료기기 제조.'),('델타(병렬) 로봇','모델: MR-Delta 2\n가반하중: 2 kg / 작업 직경: 800 mm\n사이클타임: 0.2초 / 반복정밀도: ±0.05 mm\n주요 기능: 초고속 반복 동작 최적화. IP69K 방수·방진 완\n전 대응. 식품 접촉 부품 SUS304 사용.\n적용: 식음료·제약 고속 선별·포장. PTP 픽앤플레이스. 이\n물 검출 비전 통합 솔루션.')]
for j,(a,b)in enumerate(prods):
 x=20+j*419;s+=box(x,196,401,504,'#f6f6f6',22)+ph(x+12,207,377,233,j+1,12)+tx(a,x+32,470,350,size=28,weight=650)+tx(b,x+32,516,350,size=15,extra='line-height:1.46;')
slides[9]=s
s=base(5,'plain')+title('조립·검사 공정 자동화',197)
stept=[('부품 공급·정렬','비전 카메라 + 델타로봇 연동.\n무작위 부품 자동 인식·정렬.\n사이클타임 0.2초/개 처리'),('정밀 조립','MR-Cobot 10e 힘제어\n(Force Control) 조립.\n체결 토크 실시간 모니터링.\n과토크 즉시 알람·정지 기능.'),('비전 외관 검사','2D+3D 비전 + AI 딥러닝 결함 검출.\n스크래치·이물·치수 불량 자동 판별.\n불량품 즉시 자동 배출 처리.'),('자동 마킹·이력 추적','레이저 마킹→RFID/바코드 부착 자동화.\nMES 품질 이력 실시간 DB 연동.\n완전 이력 추적(Traceability) 구현.'),('완제품 팔레타이징','MR-Cobot 25e 자동 혼재 적재.\nAI 팔레타이징 알고리즘 적용.\nWMS 출고 데이터 실시간 연동.')]
for j,(a,b)in enumerate(stept):
 x=j*256;s+=box(x,331,256,58,'#e0e0e0')+tx(f'STEP 0{j+1}.',x+75,342,180,size=30,extra='letter-spacing:-1.4px;')+tx(a,x+75,444,185,size=21,weight=650)+tx(b,x+60,488,195,size=13,extra='line-height:1.35;')
 if j<4:s+=svg('<path d="m0 0 28 29L0 58h30l28-29L30 0Z" fill="#deff3c"/>',x+227,331,58,58)
s+=''.join(svg('<path d="m0 0 28 29L0 58h30l28-29L30 0Z" fill="#deff3c"/>',j*256+227,331,58,58)for j in range(4))
slides[10]=s
s=base(6,'grey')+svg('<ellipse cx="-7" cy="360" rx="630" ry="485" fill="#f6f6f6"/><ellipse cx="1287" cy="360" rx="630" ry="485" fill="#f6f6f6"/>',0,0,1280,720)
# redraw furnishing above circles
s+=tx('MIRIROBOTICS',97,47,170,size=14)+tx('SOLUTION PROPOSAL',1053,47,180,size=14)+base(6,'plain').split('<div class="nav">')[1].join(['<div class="nav">','']) if False else ''
s=base(6,'grey')+svg('<ellipse cx="-7" cy="360" rx="630" ry="485" fill="#f6f6f6"/><ellipse cx="1287" cy="360" rx="630" ry="485" fill="#f6f6f6"/>',0,0,1280,720)+base(6,'plain')[base(6,'plain').find('<div class="tx"'):]
for j,(head,sub,ls)in enumerate([('용접 자동화','아크용접 로봇 셀 (MR-Arc 200)',['3D 시임 트래킹 → 모재 변형 실시간 보정','용접 파라미터(전류·전압·속도) 자동 최적화','스패터·흄 흡진 시스템 통합','용접 비드 품질 비전 자동 검사','다층 용접·위빙 패턴 자동 생성','MES 용접 이력 실시간 DB 연동','적용 업종: 자동차 부품·철구조물·압력용기·선박부재·건설기계']),('도장 자동화','도장 로봇 시스템 (7축 MR-Cobot Pro)',['3D 포인트클라우드 기반 경로 자동 생성','도막 두께 실시간 측정·피드백 제어','분체·수성·UV 도료 건 자동 교체','도장 부스 연동 음압·온습도 자동 제어','도장 영역 3D 비전 사전 스캔·검증','도장 후 외관 자동 비전 검사 통합','적용 업종: 가전 외장·자동차 차체·산업기계·가구·건자재'])]):
 x=95+j*716;s+=tx(head,x,165,375,size=32,weight=650,align='center')+box(x,267,375,93,'#fff',20)+pill('SOLUTION',x+90,242,197,47,29,weight=400)+tx(sub,x+5,310,365,size=22,weight=650,align='center')+ul(ls,x-20,393,415,size=16,align='center',line=1.6).replace('<ul>','<ul class="check">')
slides[11]=s
s=base(7)+title('포장·물류 공정 자동화',148)+svg('<path d="M151 395v-9c0-65 51-117 116-117h745c65 0 117 52 117 117s-52 118-117 118H395" fill="none" stroke="#000" stroke-width="1.3"/>',0,0,1280,720)
for n,x,y,name in [(1,151,395,'제품 도착'),(2,395,269,'비전 인식'),(3,640,269,'픽앤플레이스'),(4,885,269,'자동 포장·실링'),(5,885,504,'라벨링'),(6,640,504,'팔레타이징'),(7,395,504,'출고')]:
 s+=box(x-19,y-19,38,38,'#deff3c',999)+tx(f'{n:02}',x-19,y-15,38,size=20,align='center')+svg(f'<path d="M{x} {y+19}v52" stroke="#000" stroke-dasharray="2 3" stroke-width="2"/><circle cx="{x}" cy="{y+72}" r="2.5"/>',0,0,1280,720)+tx(name,x-90,y+83,180,size=22,weight=650,align='center')
slides[12]=s
s=base(8)+tx('로봇 도입 정량 효과',121,170,440,size=40,weight=750)+tx('로봇 자동화 도입 전후 핵심 KPI 비교\n(실제 고객사 평균값 기준)',121,237,440,size=22)
vals=[('생산 UPH',120,218,'120개','218개','+82%'),('불량률',320,40,'3.2%','0.4%','-87.5%'),('설비 가동률',145,195,'72%','97%','+25%p'),('야간 가동 시간',0,320,'','16시간',''),('공정 리드타임',240,140,'48시간','28시간','-42%'),('산재 발생',335,0,'연4.2건','0건','')]
for j,(name,a,b,la,lb,d)in enumerate(vals):
 y=186+j*64;s+=tx(name,475,y+3,105,size=18,align='right')
 for k in range(5):s+=box(589+k*106,y-8,1,47,'#d5d5d5')
 s+=box(589,y,a,31,'#e0e0e0')+box(589+a,y,b,31,'#000')
 if a:s+=tx(la,589,y+4,a,size=18,align='center',extra='color:#fff;')
 s+=tx(lb,589+a,y+4,b or 45,size=18,align='center',extra='color:'+('#fff' if b else '#000')+';')
 if d:s+=pill(d,1047,y-6,112,44,23)
s+=box(585,581,22,22,'#e0e0e0',999)+tx('Before',617,584,70,size=16)+box(680,581,22,22,'#000',999)+tx('After',712,584,70,size=16);slides[13]=s
s=base(8)+title('투자 수익성(ROI) 분석',138)
for j,(a,b)in enumerate([('투자 가치','초기 투자비 8,000만원\n(협동로봇 4대 패키지)'),('회수 기간','18개월 후 투자비 회수\n(업계 평균 대비 6개월 단축)'),('기대 수익','5년 누적 순익 1.86억원\n(투자 대비 수익률 233%)')]):
 x=225+j*267;s+=svg('<ellipse cx="150" cy="154" rx="173" ry="132" transform="rotate(-45 150 154)" fill="none" stroke="#000" stroke-width="1.3"/>',x,260,312,310)+box(x+66,264,55,55,'#deff3c',999)+tx(f'{j+1:02}',x+66,273,55,size=30,align='center')+tx(a,x+13,363,255,size=26,weight=650,align='center')+tx(b,x+15,409,260,size=20,align='center')
slides[14]=s
s=base(9,'plain')+tx('로봇 자동화 구축 프로세스',756,147,490,size=40,weight=750)+tx('전체 기간 : 총 약 10~16주 (공정 규모에 따라 조정)',796,207,465,size=18)
step=[('현장 진단·컨설팅','(1~2주)','공정 현황 분석·병목 구간 파악\n자동화 우선순위 도출·범위 확정\nROI 사전 시뮬레이션 보고서 제공\n초도 방문 무상 컨설팅 제공'),('솔루션 설계','(2~3주)','로봇·주변기기 선정 및 레이아웃 설계\n안전 설계(Risk Assessment) 수행\n3D CAD 시뮬레이션·경로 검증\n제안서·견적서 최종 확정'),('제작·조달','(4~8주)','로봇 셀·제어반·전장 제작\nPLC·비전 소프트웨어 개발·테스트\n공장 내 사전 검수(FAT: Factory\nAcceptance Test)'),('설치·통합','(1~2주)','현장 설치·배선·배관 완료\nPLC·MES·ERP 인터페이스 연동\n안전 검증·현장 시운전(SAT: Site\nAcceptance Test)'),('시운전·교육','(1주)','양산 조건 성능 검증·확인\n운전자·관리자 교육(이론+실습)\n비상 대응 절차·운전 매뉴얼 제공'),('유지보수·A/S','(상시)','24시간 원격 모니터링·예방 알림\n정기 예방 PM·소모품 교체\nSW 버전 업데이트·기능 개선 지원')]
for j,(a,b,c)in enumerate(step):
 x=j*213.33;y=239+j*48;s+=box(x,0,1,720,'#bbb')+svg(f'<path d="M{x} {y}h211m-8-8 8 8-8 8" fill="none" stroke="#000" stroke-width="2.5"/>',0,0,1280,720)+box(x+85,y-50,42,42,'#deff3c',999)+tx(f'STEP 0{j+1}.',x+56,y-47,150,size=30,extra='letter-spacing:-1.5px;')+tx(a+'\n'+b,x+8,y+29,197,size=19,weight=650,align='center')+tx(c,x+8,y+100,197,size=14,align='center',extra='line-height:1.35;')
slides[15]=s
s=base(10)+title('고객사 도입 성공 사례',146)
for j,(head,sol,q)in enumerate([('사례 1 : 자동차 부품 제조사','도입 솔루션: MR-Delta 2 ×6대\n+ MR-Cobot 25e ×2대 + AGV 연동','"야간 무인 운전으로 납기 지연 Zero,\nOEM 품질 기준 완벽 충족했습니다."\n— A자동차부품 생산기술팀장 (가명)'),('사례 2 : 식음료 포장·물류 기업','도입 솔루션: MR-Arc 200 ×4대\n+ MR-Cobot 10e ×2대\n+ AI 비전 검사 시스템','"계절 피크에도 풀가동, 납기 100% 달성.\n식품안전 인증까지 획득했습니다."\n— B식품 SCM본부장 (가명)')]):
 x=277+j*381;s+=pill(head,x,246,345)+box(x,300,345,297,'#fff',22)+tx(sol,x+10,365 if j==0 else 346,325,size=21,weight=650,align='center',extra='line-height:1.35;')+tx(q,x+10,456 if j==0 else 468,325,size=18,align='center',extra='font-style:italic;line-height:1.4;')
slides[16]=s
s=base(11)+title('인증 현황',168)
cert=['ISO 9001:2015\n품질경영시스템','ISO 45001:2018\n안전보건경영시스템','CE 마킹 기계지침\n2006/42/EC','KS Q ISO 10218-2\n로봇 안전 설계·통합 인증','산업통상자원부\n로봇전문기업 지정','고용노동부 스마트공장\n구축지원 파트너']
for j,t in enumerate(cert):
 x=165+(j%3)*329;y=278+(j//3)*161;s+=ph(x,y,35,117,j+1)+ph(x+254,y,35,117,j+1)+tx(t,x+35,y+28,219,size=22,weight=550,align='center',extra='line-height:1.3;')
slides[17]=s
s=base(12)+title('파일럿 도입 패키지 제안',151)+tx('패키지 안내',520,240,240,size=26,weight=700,align='center')+box(314,254,255,1,'#000')+box(711,254,255,1,'#000')+ul(['타깃: 자동화 첫 도입·ROI 검증 기업','구성: 협동로봇 1대 + 그리퍼 + 기본 S/W','기간: 2주 현장 무상 체험 후 도입 결정','포함 서비스: 현장 진단 컨설팅 1회, 실제 공정 데모 운전 실시, 기본 프로그래밍 교육 (1일)','특징: 초기 투자 최소화, 효과 검증 후 확장 결정','가격: 별도 협의'],300,291,680,size=19,align='center',line=1.25)+box(314,482,651,1,'#000')+pill('지금 무료 현장 진단 신청하기',448,541,384)+tx('02-1234-5678 | robot@mirirobotics.com',450,602,470,size=23)
slides[18]=s
s=box(0,0,1280,720,'#e0e0e0')+box(23,0,1234,561,'#f6f6f6',28)+box(23,582,1234,138,'#f6f6f6',28)+base(13,'plain')[base(13,'plain').find('<div class="tx"'):]+title('자동화의 첫 걸음,\n미리로보틱스와 함께 시작하세요.',134)+tx('현장 진단부터 ROI 시뮬레이션까지 전문 엔지니어가 무상으로 지원합니다.\n도입 결정 전, 부담 없이 문의하세요.',260,258,760,size=21,align='center',extra='line-height:1.25;')+box(640,330,1,98,'#000')+tx('<b>영업 문의</b> : 영업팀 | 기술 문의: 솔루션사업팀\n<b>담당자</b> : [이름] | [직책] | [직통번호]',385,446,510,size=23,align='center')
for j,(a,c)in enumerate([('MiriIn','#198aba'),('Miritube','#c00'),('Blog','#49c500')]):s+=pill(a,272+j*250,605,236,50,29,'#fff',550).replace('font-weight:550;','font-weight:550;color:'+c+';')
s+=tx('© 2055 미리로보틱스 주식회사. All rights reserved.',470,676,390,size=14,align='center',extra='color:#888;')
for x in [50,1229]:
 for y in [533,606]:s+=box(x-8,y-8,16,16,'#d8d8d8',999)
slides[19]=s
for n,s in slides.items():
 P.joinpath(f'slide-{n:02}.html').write_text(f'<!doctype html><html lang="ko"><meta charset="utf-8"><title>Diecut replica {n:02}</title><link rel="stylesheet" href="replica.css"><body><main class="slide">{s}</main></body></html>')
json.dump({'pages':len(slides),'size':[1280,720]},open(R/'build/replica-manifest.json','w'),indent=2)
print('Built',len(slides),'replicas')
