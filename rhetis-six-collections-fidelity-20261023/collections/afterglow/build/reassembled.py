from pathlib import Path
import json,shutil
B=Path(__file__).resolve().parents[1];R=B/'review';C=B/'collection'/'afterglow';O=R/'reassembled'
# The source slide's blue is style data; all geometry is imported unmodified from the library.
pal=json.loads(Path('/workspace/work/reference/contract/palette.json').read_text())
for mode,colors in pal.items():
 colors['--a1']='#307efa';colors['--a1-on']='#ffffff';colors['--page']='#000000' if mode=='dark' else '#ffffff';colors['--ink']='#ffffff' if mode=='dark' else '#111111';colors['--n-2']='#161616' if mode=='dark' else '#e9e9e9';colors['--n-4']='#a2a2a2';colors['--n-6']='#ffffff' if mode=='dark' else '#666666'
 for i in range(1,10):
  import colorsys
  v=colorsys.hls_to_rgb(.61,.96-(i-1)*.095,.70)
  h='#'+''.join(f'{round(x*255):02x}' for x in v)
  colors['--a1-'+str(i)]=h;colors['--a1-'+str(i)+'-soft']=h;colors['--a1-'+str(i)+'-muted']=h
 colors['--a1-7']='#307efa';colors['--a1-3']='#307efa';colors['--n-8']='#e9e9e9' if mode=='dark' else '#333333'
scaffold='@font-face{font-family:Freesentation;src:url("fonts/artifacts/freesentation/Freesentation-4Regular.woff2");font-weight:400}@font-face{font-family:SUITE;src:url("fonts/artifacts/suite/SUITE-Regular.woff2");font-weight:400}@font-face{font-family:"Pretendard Variable";src:url("../assets/PretendardVariable.woff2");font-weight:100 900}html,body{margin:0;width:1280px;height:720px;overflow:hidden}'
scaffold+=''.join(('.slide.dark' if m=='dark' else '.slide')+'{'+''.join(k+':'+v+';' for k,v in cols.items())+'}' for m,cols in pal.items())
steps=json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text());scaffold+='.slide{'+''.join(f'--type-{s}:{s}px;' for s in steps)+'}'
scaffold+='.slide.on{--a1:#307efa}'
(R/'assets/deck-style.css').write_text(scaffold)
shutil.copytree(C,R/'assets/collection/afterglow',dirs_exist_ok=True)
styles=['../assets/collection/afterglow/kit/css/tokens.css','../assets/collection/afterglow/foundation/foundation.css']+['../assets/collection/afterglow/elements/'+p.name+'/element.css' for p in sorted((C/'elements').iterdir())]+['../assets/deck-style.css']
def el(folder,cls,inner,col,row,w,h,extra=''):
 return f'<div class="{cls}" data-el="afterglow-{folder}" style="grid-column:{col} / span {w}; grid-row:{row} / span {h}" {extra}>{inner}</div>'
def headline(k,t,col,row,w,h,big=False,note=''):
 return el('headline','headline'+(' big' if big else ''),(f'<p class="kick">{k}</p>' if k else '')+f'<h2>{t}</h2>'+ (f'<p class="note">{note}</p>' if note else ''),col,row,w,h)
def prose(text,col,row,w,h,cls='prose quiet'):
 return el('prose',cls,'<p>'+text+'</p>',col,row,w,h)
def frame(col,row,w,h,n=1):return el('image-frame','frame quiet',f'<div class="seat" data-ph="{n}"></div>',col,row,w,h)
def doc(n,body,section='Service',on=False):
 return '<!doctype html><html lang="ko"><meta charset="utf-8"><title>Afterglow / '+str(n)+'</title>'+''.join('<link rel="stylesheet" href="'+s+'">' for s in styles)+f'<body><section class="slide dark {"on" if on else ""}"><div class="page"><div class="top"><span class="deck">MIRI Service Introduction</span><span class="sec">{section}</span><span class="no">MIRI COMPANY</span></div><div class="body">{body}</div></div></section><script src="../assets/icons-runtime.js"></script></body></html>'
P={}
P[1]=doc(1,headline('','사진 넣고 바로 설명하는,<br><b>서비스 소개 PPT</b>',1,1,9,3,True)+prose('우리 서비스 자랑이<br>차고 넘칠 때.',5,5,3,1,'prose lead')+prose('미리컴퍼니는 급변하는 환경에서도, 인프라 안정성을 바탕으로 한<br>최신 보안 기술을 제공합니다. 이곳에 회사의 서비스를 소개하는 문장을<br>입력해 주세요. 차별화된 지점이나 앞서간 지점에 관해 설명한다면<br>보다 임팩트 있는 소개 자료를 완성할 수 있습니다.',8,5,5,2),'Presentation ver.1')
entries=[('Serviece','서비스 소개'),('Technology','기술력 소개'),('Process','프로세스 소개'),('How to Use','사용 방법 안내'),('Contact','문의처')]
P[2]=doc(2,headline('','<b>Contents</b>',1,2,5,1,True,'목차')+el('agenda','agenda',''.join(f'<div class="entry"><b class="name">{a}</b><p class="note">{b}</p></div>' for a,b in entries),1,4,12,2),'Contents',True)
P[3]=doc(3,headline('','Service',1,1,8,3,True,'서비스 소개')+prose('이곳에 이어질 내용의 주제를 입력해 보세요. 본문 사이사이에 들어가는<br>페이지이므로 상세 내용 또한 짧고 간결하게 작성하는 것이 좋습니다.',8,5,5,1,'prose')+el('list','list',''.join('<div class="item"><b class="name">소제목을 작성하세요</b></div>' for _ in range(3)),8,6,5,1),'Service',True)
t='글로벌 규모의 안정적 서비스,<br>미리 클라우드'
intro='미리컴퍼니는 급변하는 환경에서도, 인프라 안정성을<br>바탕으로 한 최신 보안 기술을 제공합니다. 이곳에 회사의<br>서비스를 소개하는 문장을 입력해 주세요. 차별화된 지점이나<br>앞서간 지점에 관해 설명한다면 보다 임팩트 있는<br>소개 자료를 완성할 수 있습니다.'
P[4]=doc(4,headline('Service',t,1,1,5,2)+el('list','list','<div class="item"><span class="mark"><span class="icon" data-icon="chevron-right"></span></span><b class="name">확장 네트워크를 통한 통합 응용 솔루션 제공</b><p class="note">'+intro+'</p></div>',1,3,4,3)+frame(6,2,7,5))
names=['하이브리드 솔루션','데이터 스토리지','컴퓨팅 & 서버 및 시스템','IT 인프라 & 네트워킹']
P[5]=doc(5,headline('Service',t,1,1,5,2)+''.join(el('card','card',f'<div class="parts"><div class="seat" data-ph="{i+1}"></div><span class="mark">{i+1}</span><p class="name">{name}</p><p class="note">해당 서비스와 관련된 설명을 입력해 주세요.<br>핵심 키워드나 특징을 간단히 적어주세요.</p></div>',1+i*3,3,3,4) for i,name in enumerate(names)))
pts=''.join(f'<div class="pt" style="--v:{v}"></div>' for v in [38.16,40.46,43.46,48.59,56.01,69.79])
P[6]=doc(6,el('chart-area','areas quiet','<div class="series"><b class="name"></b>'+pts+'</div><div class="axis">'+''.join('<span></span>' for _ in range(6))+'</div>',1,1,12,6).replace('grid-row:1 / span 6"','grid-row:1 / span 6; --max:100"')+headline('Technology','환경 최적화를 위한,<br>하이브리드 클라우드 사용',1,1,5,2)+el('list','list','<div class="item"><span class="mark"><span class="icon" data-icon="chevron-right"></span></span><b class="name">최대 30% 증가</b><p class="note">기존의 복잡했던 IT 환경을 개선하고 클라우드의 장점을 보완해,<br>워크로드 간 데이터를 간단히 공유할 수 있도록 합니다.<br>이곳에 회사의 기술력에 대해 입력해 주세요. 해당 기술력을 바탕으로<br>고객사에서 얻을 수 있는 이익이 무엇인지 알려주세요.<br>기존의 문제를 해결하는 전개가 좋습니다.</p></div>',1,3,5,2)+el('metric','stat quiet','<div class="parts"><b class="fig">30<small>% 증가</small></b></div>',9,1,4,2),'Technology')
ptxt='미리 클라우드는 미리 MR12를 탑재해, 사이트의 속도 및 성능을 향상 시키고 유저에게 더욱 빠르게 콘텐츠를 제공합니다. 이곳에 회사 서비스의 사용 과정에 대해 입력해 보세요.'
P[7]=doc(7,frame(5,2,5,5)+headline('Process','심플하고 강력한,<br>클라우드 서비스 프로세스',1,1,5,2)+''.join(el('prose','prose quiet'+(' line' if i<2 else ''),f'<p><b>Process {i+1}. 소제목</b></p><p>'+ptxt+'</p>',1 if i%2==0 else 10,3 if i<2 else 5,3,2) for i in range(4)),'Process')
steps=''.join(f'<div class="step"><span class="mark"><span class="icon" data-icon="{icon}"></span></span><b class="name">Step{i+1}. {name}</b><p class="note">첫번째로는 서버를 생성해야 합니다.<br>서버에 설치할 이미지를 클릭하고 하단의 생성하기 버튼을 클릭해 주세요.<br>이곳에는 클라우드 사용 방법을 안내하는 줄글을 입력해 주세요.</p></div>' for i,(name,icon) in enumerate([('서버 생성','lock-keyhole-open'),('인증키 설정','key-round'),('네트워크 접근','shield-check')]))
P[8]=doc(8,headline('How to Use','쉽고 간단한,<br>미리클라우드 사용 방법 안내',1,1,5,2)+prose('다음의 설명을 읽고, 미리클라우드 사용 방법을<br>차근차근 익혀보세요.이렇게 단계별로 문단을 나누어 설명하면,<br>고객이 보기 편한 자료가 완성됩니다. 사용 방법에는<br>접속하는 과정을 하나하나 설명해도 좋고, 큼지막한 내용 위주로<br>설명해도 좋습니다.',1,3,4,2,'prose')+el('steps','steps col',steps,6,2,7,5),'How to Use')
P[9]=doc(9,el('headline','headline center','<h2><b>서버생성부터,<br>데이터베이스 구축까지</b></h2><p class="note">가장 편안한 방식으로,<br>가장 복잡한 성능을 제공하겠습니다.</p>',4,2,6,3)+el('callout','callout quiet','<p>미리컴퍼니 미리 클라우드 서비스<br>-<br>사용 문의<br><b>e-mail.</b> kimmiri@gmail.com　 <b>adress.</b> 미리특별시 미리구 미리로 3길 미리빌딩 8층　 <b>homepage.</b> www.miricompany.com</p>',1,5,12,2),'Inquiry')
for i,t in P.items():(O/f'slide_{i:02}.html').write_text(t)
print('Reassembled',len(P),'pages with collection only geometry')
