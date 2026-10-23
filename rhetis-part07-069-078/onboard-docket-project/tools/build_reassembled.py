from pathlib import Path
import json,re
P=Path(__file__).parent;K='onboard-docket';C=P/K;R=P/'reassembled';R.mkdir(exist_ok=True);A=P/'assets';A.mkdir(exist_ok=True)
# A style provider, not a layout override: original deck colours occupy palette roles.
pal=json.loads(Path('/workspace/work/reference/contract/palette.json').read_text())['light'];pal.update({'--page':'#fdfdfd','--ink':'#080808','--a1':'#4383e6','--a1-on':'#ffffff','--a2':'#383c51','--a2-on':'#ffffff','--a3':'#333333','--a3-on':'#ffffff','--n-1':'#f5f5f5','--n-2':'#ececec','--n-3':'#dcdcdc','--n-4':'#c8c8c8','--n-5':'#b0b0b0','--n-6':'#969696','--n-7':'#717171','--n-8':'#383c51','--n-9':'#333333'})
for a in range(1,5):
 for n in range(1,10):
  v='#eef2f8' if n<3 else '#d5e2f6' if n<5 else '#4383e6' if n<7 else '#244d8c' if n<9 else '#1a365e'
  for tail in ['','-soft','-muted']:pal[f'--a{a}-{n}{tail}']=v
(A/'source-palette.css').write_text('.slide{'+''.join(k+':'+v+';' for k,v in pal.items())+'}\n')
steps=json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text());(A/'type-steps.css').write_text('.slide{'+''.join(f'--type-{n:g}:{n:g}px;' for n in steps)+'}\n')
def E(folder,root,inner,extra='',grid=None,attrs=''):
 st=f' style="grid-column:{grid[0]} / span {grid[1]};grid-row:{grid[2]} / span {grid[3]}"' if grid else ''
 return f'<div class="{root}{(" "+extra) if extra else ""}" data-el="{K}-{folder}"{st}{attrs}>{inner}</div>'
def g(col,span,row,h):return f'grid-column:{col} / span {span};grid-row:{row} / span {h}'
def parts(name,note='',fig='',kick='',mark=''):
 return '<div class="parts">'+(f'<p class="kick">{kick}</p>' if kick else '')+(f'<span class="mark">{mark}</span>' if mark else '')+(f'<p class="fig">{fig}</p>' if fig else '')+f'<p class="name">{name}</p>'+(f'<p class="note">{note}</p>' if note else '')+'</div>'
def card(name,note='',fig='',extra='',grid=None,mark=''):return E('card','card',parts(name,note,fig,mark=mark),extra,grid)
def hline(text,note='',extra='',grid=None,kick=''):return E('headline','headline',(f'<p class="kick">{kick}</p>' if kick else '')+f'<h2>{text}</h2>'+(f'<p class="note">{note}</p>' if note else ''),extra,grid)
def prose(*paras,extra='',grid=None):return E('prose','prose',''.join(f'<p>{t}</p>' for t in paras),extra,grid)
def image(num,grid):return E('image-frame','frame',f'<div class="seat" data-ph="{num}"></div>',grid=grid)
def callout(t,grid):return E('callout','callout',f'<p>{t}</p>',grid=grid)
def pill(t,extra='',grid=None):return E('pill','pill',parts(t),extra,grid)
def listel(items,extra='',grid=None):return E('list','list',''.join(f'<div class="item"><p class="name">{n}</p><p class="note">{v}</p></div>' for n,v in items),extra,grid)
def steps(items,extra='',grid=None):return E('steps','steps',''.join(f'<div class="step"><span class="mark">{i+1:02}</span><p class="name">{n}</p><p class="note">{v}</p></div>' for i,(n,v) in enumerate(items)),extra,grid)
def group(inner,grid,extra=''):return f'<div class="group {extra}" style="{g(*grid)}">{inner}</div>'
B={};titles={2:'INDEX',3:'',4:'환영 인사',5:'긴 글이 있는 레이아웃',6:'미리컴퍼니 인재상',7:'5줄 리스트 레이아웃',8:'미리컴퍼니의 이념',9:'미리컴퍼니 조직도',10:'3가지 핵심 업무 원칙',11:'3가지 핵심 업무 원칙',12:'4가지 핵심 업무 원칙',13:'4가지 핵심 업무 원칙',14:'상세 키워드 프로세스',15:'단계별 레이아웃',16:'일자별 리스트 레이아웃',17:'KPI 프로세스',18:'사진을 활용한 레이아웃',19:'사진을 활용한 레이아웃'}
B[2]=E('agenda','agenda',''.join(f'<div class="entry"><span class="mark">{i+1:02}</span><p class="name">목차를 이곳에 입력해주세요</p><p class="note"></p></div>' for i in range(8)),grid=(1,12,1,6))
B[3]=hline('CHAPTER<br><b>01</b>','해당 챕터의 핵심 키워드와 궁극적 목적 문장을 적어주세요.<br>주제에 대한 세부 내용을 기재해주세요.<br>페이지에서 말하고자하는 내용을 적어주세요.','big center',(1,12,1,6))
B[4]=E('quote','quote','<blockquote>이곳에 기업 철학이나 기업을<br><b>대표하는 핵심 메시지를 적어주세요</b></blockquote><div class="by"><p class="name">대표이사 김 미 리</p><p class="note">미리컴퍼니</p></div>',grid=(1,8,1,3))+prose('신입사원 여러분들, 미리컴퍼니에 오신 것을 진심으로 환영합니다.<br>이곳에 CEO 환영 인사말을 텍스트로 입력해주세요.<br>관련 내용을 이곳에 텍스트로 입력해주세요. 텍스트를 입력해주세요.','이곳에 CEO 환영 인사말을 텍스트로 입력해주세요.<br>관련 내용을 이곳에 텍스트로 입력해주세요. 텍스트를 입력해주세요.',extra='quiet',grid=(1,8,4,3))+image(1,(9,4,1,6))
B[5]=prose('<b>이 페이지의 핵심내용을 입력해주세요.</b>','해당 페이지는 많은 분량 텍스트를 입력할 때 쓰기 좋은 페이지입니다.<br>10줄 이상의 텍스트를 넣어야 할 때 이 페이지를 활용해보세요.<br>중요한 내용이나 길게 의견을 보여주어야 할 경우 해당 페이지를 활용해보세요.<br>가독성의 핵심은 얼마나 내용을 간결하게 전달하는가 입니다.<br>쉽게 읽을 수 있고, 눈에 잘 띄는 것이 중요해요.','전체적인 톤앤매너와 맞는 폰트와 색상 등을 활용해주세요.<br>강조하고 싶은 부분은 볼드체 또는 큰 사이즈로 표현해보세요.<br>구체적인 예시나 수치 등을 활용하면 좋습니다.',grid=(1,7,1,6))+image(1,(8,5,1,6))
B[6]=pill('전문성',grid=(2,2,1,1))+prose('이곳에 관련 내용을 텍스트로 간략하게 입력해주세요. 관련 내용을 이곳에 입력해주세요.',extra='quiet',grid=(4,8,1,1))+E('chart-donut','donut','<p class="fig">33<small>%</small></p><p class="name">인재상</p>',grid=(5,4,2,4),attrs=' style="--v:33"')+card('주도성','이곳에 관련 내용을 텍스트로 간략하게 입력해주세요. 관련 내용을 이곳에 입력해주세요.',extra='quiet',grid=(1,4,3,2))+card('책임감','이곳에 관련 내용을 텍스트로 간략하게 입력해주세요. 관련 내용을 이곳에 입력해주세요.',extra='quiet',grid=(9,4,3,2))+callout('미리인은 전문성을 바탕으로 주도적으로 목표를 달성하며 모든 과정에서 책임을 다하는 인재입니다.',(1,12,6,1))
items=[('조직 및 역할 이해','조직 구조 및 신입사원의 기본 역할을 이해합니다.'),('기초 역량 개발','사회적 기술과 대인 관계 능력을 키워 조직 적응력을 높입니다.'),('직무 능력 배양','기본적인 직무 기술과 실무 역량을 강화합니다.'),('협업 및 협력 능력 강화','팀 내 원활한 의사소통과 협업 능력을 증진합니다.'),('발전성 구축','지속적인 자기 개발을 통해 성장형 인재로 발전합니다.')]
B[7]=listel(items,'num',(1,12,1,6))
B[8]=E('venn','venn',''.join(f'<div class="set{(" on" if i==2 else "")}"><p class="name">{n}</p></div>' for i,n in enumerate(['VISION','MISSION','VALUES'])),grid=(1,5,1,6))+listel([('VISION','회사의 미래 목표와 지향점을 간결하고 명확하게 적어보세요. 텍스트를 간략하게 입력해주세요.'),('MISSION','회사의 존재 이유와 핵심 활동을 구체적으로 설명해보세요. 관련 내용을 입력해주세요.'),('VALUES','회사가 중요하게 여기는 핵심 가치에 대한 설명을 이곳에 입력해보세요.')],grid=(6,7,1,6))
B[9]=pill('CEO : 김미리','on',(6,2,1,1))+pill('COO','quiet',(3,2,2,1))+pill('CFO','quiet',(9,2,2,1))
for i in range(5):
 B[9]+=group(pill(f'부서 {i+1}','on' if i%2==0 else '')+listel([(f'팀 {j+1}','') for j in range(3)]),(1+i*2,2,3,4),'col')
B[10]=steps([('Step 1 키워드 입력','이 페이지는 비즈니스 프로세스를 한눈에 볼 수 있는 페이지입니다. 각 단계가 진행됨에 따라 세부 내용을 입력해 보세요.'),('Step 2 키워드 입력','이 페이지를 사용하여 비즈니스의 흐름을 설계해 보세요. 확장 과정을 단계별로 입력해 주시기 바랍니다. 각 단계별 액션과 세부 내용을 입력하여 성장 과정을 시각화하세요.'),('Step 3 키워드 입력','단계를 나누어 각 단계가 전체 흐름에 어떻게 기여하는지 설명해 주세요. 비즈니스 프로세스의 시작부터 끝까지 시각적으로 구성해 보세요. 이해와 전달력이 향상됩니다.')],'col',(1,12,1,6))
for i in range(1,4):B[10]=B[10].replace(f'<span class="mark">{i:02}</span>',f'<span class="mark">Step {i}</span>')
B[11]=hline('상위 단계에 해당하는 내용을 입력하세요','업무 원칙과 관련된 단계별 내용','on center',(1,12,1,2))
for i in range(3):
 B[11]+=card('중간 단계에 해당하는 내용을 입력하세요.','2~3줄로 정리해봅시다.',extra='tone-3',grid=(1+i*4,4,3,2))+card('OOO 상승','세부 내용을 입력하세요. 2~3줄로 정리해봅시다.',grid=(1+i*4,4,5,2),mark=f'<span class="icon" data-icon="{["trending-up","chart-no-axes-column-increasing","lightbulb"][i]}"></span>')
B[12]=group(hline('기업의 존재의의를 명확하게<br>전달 해 보세요.',kick='Our Mission')+hline('기업의 존재의의를 명확하게<br>전달 해 보세요.',kick='Our Vision'),(1,5,1,6),'col')+prose('대표나 경영진 등의 메시지를 게재 해 보세요. 프레젠테이션 자료나 회사 소개 자료에서는 경영진의 한마디가 신뢰성과 스토리텔링을 높이는 효과가 있습니다.','예를 들면, 왜 창업을 하게 되었는지에 대한 이야기나, 비전이나 미션에 대한 자세한 설명 등도 기업이 사업을 통해 이루고 싶은 미래에 대해 상대에게 보다 효과적으로 전달할 수 있게 됩니다.',grid=(6,7,1,3))+prose('대표나 경영진 등의 메시지를 게재 해 보세요. 기업이 소중히 여기는 가치관이나 사원·고객·파트너에게 향하는 메시지 등을 기재 해 보세요.',grid=(6,4,4,3))+image(1,(10,3,4,3))
B[13]=E('hub','hub','<div class="core">KEYWORD</div>'+''.join(f'<div class="spoke{(" on" if i%2==0 else "")}"><span class="mark">{i+1:02}</span><p class="name">{n}</p><p class="note">이곳에 관련 내용을 텍스트로 간략하게 입력해주세요. 관련 내용을 이곳에 입력해주세요.</p></div>' for i,n in enumerate(['목적','열정','책임','보고'])),grid=(1,12,1,6))
for i,ic in enumerate(['target','hand-heart','lightbulb','clipboard-pen'],1):B[13]=B[13].replace(f'<span class="mark">{i:02}</span>',f'<span class="mark"><span class="icon" data-icon="{ic}"></span></span>')
B[14]=steps([(f'ENTER A KEY WORD','키워드를 입력해주세요') for i in range(4)],grid=(2,10,1,4))
for i in range(4):B[14]+=card('키워드 '+chr(65+i),'키워드와 관련된 상세 텍스트를 자유롭게 입력해주세요. 핵심 내용 위주로 나열해주세요.',extra='quiet',grid=(1+i*3,3,5,2))
B[15]=steps([('Step 1','이 페이지는 비즈니스 프로세스를 한눈에 볼 수 있는 페이지입니다. 각 단계가 진행됨에 따라 세부내용을 입력해 보세요.'),('Step 2','단계별로 주요 활동과 목표를 작성해 주세요. 이를 통해 프로세스의 완성도를 높일 수 있습니다.'),('Step 3','프로세스 전체의 흐름을 보다 간단하게 이해할 수 있도록 중요한 포인트를 간결하게 정리해 보세요.'),('Step 4','이 스텝에서 어떤 액션을 취할건지 알려주세요. 듣는 사람의 입장에서 프로세스의 상세한 내용을 적어보세요.')],grid=(1,12,1,6))
for i,ic in enumerate(['handshake','lightbulb','chart-no-axes-column-increasing','rocket'],1):B[15]=B[15].replace(f'<span class="mark">{i:02}</span>',f'<span class="mark"><span class="icon" data-icon="{ic}"></span></span>')
days=[['OT 및 회사 투어','회사 비전 및 조직 문화 이해','팀 빌딩 활동','선배와의 Q&A','교육명을 입력하세요'],['기본 비즈니스 매너','커뮤니케이션 스킬','사업부와 부서 이해','실습 활동','교육명을 입력하세요'],['보고 및 스피치 스킬','팀별 과제 발표','피드백 세션','교육 수료식','교육명을 입력하세요']]
B[16]=''
for i,day in enumerate(days):B[16]+=group(pill(f'{i+1}일차','on' if i!=1 else '')+listel([(t,'') for t in day],'divided'),(1+i*4,4,1,6),'col')
B[17]=''
for i in range(3):
 B[17]+=card('사업명을 입력',extra='on' if i==2 else 'tone-3',grid=(1,3,1+i*2,2))
 B[17]+=E('metric','stats',''.join(E('metric','stat',parts('키워드 입력','전년 동기 대비 00% 상승' if j==0 else '수치에 대한 부가 설명을 입력해주세요.',f'000<small>{unit}</small>')) for j,unit in enumerate(['원','개','명'])),grid=(4,9,1+i*2,2))
B[18]=image(1,(1,6,1,6))+listel([(f'POINT {i+1:02}','사진의 상세 내용을 이 곳에 요약하여 명확하게 적어보세요. 텍스트를 간략하게 입력해주세요.') for i in range(3)],grid=(7,6,1,6))
B[19]=card('주요<br>이미지',extra='on',grid=(1,1,1,6))
B[19]+=group(''.join(E('image-frame','frame',f'<div class="seat" data-ph="{i+1}"></div>') for i in range(3)),(2,11,1,4))
B[19]+=group(''.join(card('사진의 상세 내용','사진의 상세 내용을 이 곳에 요약하여 명확하게 적어보세요. 텍스트를 간략하게 입력해주세요.',extra='quiet') for i in range(3)),(2,11,5,2))
#19 last column start10+span3 legal; first begin2, second6,third10.
(A/'runtime.css').write_text('html,body{margin:0;padding:0}\n')
links=['../assets/runtime.css','../assets/fonts/fonts.css','../assets/type-steps.css',f'../{K}/kit/css/tokens.css',f'../{K}/foundation/foundation.css','../assets/source-palette.css']+[f'../{K}/elements/{x.name}/element.css' for x in sorted((C/'elements').iterdir()) if x.is_dir()]
head='<!doctype html><html lang="ko"><meta charset="utf-8">'+''.join(f'<link rel="stylesheet" href="{x}">' for x in links)
for n in range(1,20):
 ch=1 if n<10 else 2 if n<14 else 3 if n<18 else 4
 if n==1:body='<section class="slide cover"><div class="page"><div class="lockup at-left"><p class="kicker">MIRICOMPANY</p><h1 class="title">MIRICOMPANY<br><b>ONBOARDING BOOK</b></h1><p class="lead">미리컴퍼니 사내 교육 입문 프로그램</p></div><p class="meta">ONBOARDING　 인사팀 김미리 대리　 |　 010.1234.5678　 |　 miri_kim@miri.com　 |　 www.miricompany.com</p><div class="deco"></div></div></section>'
 else:
  title=titles[n];hdr=(f'<header class="head{(" center" if n==2 else "")}"><p class="kicker">{ch:02}</p><h1 class="title">{title}</h1>{('' if n==2 else '<p class="lead">|　 MIRICOMPANY</p>')}</header>' if title else '')
  body=f'<section class="slide"><div class="page"><div class="top"><span class="deck">MIRICOMPANY</span><span class="sec">{("CHAPTER "+str(ch).zfill(2)) if n>=4 else ""}</span></div>{hdr}<div class="body">{B[n]}</div></div></section>'
 # merge duplicate style attrs so numeric chart values coexist with placement.
 body=re.sub(r'style="([^"]*)" style="([^"]*)"',lambda m:'style="'+m[1]+';'+m[2]+'"',body)
 (R/f'slide_{n:02}.html').write_text(head+f'<title>078 / reassembled {n:02}</title><body>'+body+'</body></html>')
print('reassembled',19)
