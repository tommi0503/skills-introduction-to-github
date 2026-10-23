from pathlib import Path
from bs4 import BeautifulSoup
R=Path('/workspace/work/deliverables/dockside/review/replica')
p=R/'replica.css';s=p.read_text();s+='''\n/* Round 2: individual source comparisons */
.pill{white-space:nowrap;padding-left:12px;padding-right:12px;font-size:16px}.small,.box p,.box li{font-size:16px}.row .text{font-size:18px}.title{font-size:58px;top:133px}.chapter{top:65px}.box h3{font-size:23px}.aside p{font-size:16px}.intro{font-size:16px}.seat,.dock .seat,.rail .seat{background:#e7e7e7}.slide.cover{background:radial-gradient(ellipse at 30% 98%,#8fd1f2a0,transparent 43%),radial-gradient(ellipse at 85% 100%,#c5c5f085,transparent 38%),radial-gradient(ellipse at 10% 100%,#c8edce80,transparent 30%),#fafafa}.slide.cover:before{opacity:.55}.slide:before{clip-path:polygon(69% 0,100% 0,100% 100%,83% 100%);opacity:.65}.box{background:linear-gradient(150deg,#ffffff80,#f4f5f5e0);box-shadow:0 12px 23px #00000010}.title b{font-weight:600}.box h3 b{color:#409ae0}.rail{width:104px}.pill{box-shadow:0 5px 11px #2b8fe54a}.seat.circle{border:4px solid #fff}.image{height:302px}
''';p.write_text(s)
for n in range(1,31):
 p=R/f'slide_{n:02}.html';b=BeautifulSoup(p.read_text(),'html.parser')
 if n in [4,5,6,9,20,26,27]:
  for cls,y in [('chapter',109),('title',176)]:
   q=b.select_one('.'+cls)
   if q:q['style']=q.get('style','')+f';top:{y}px'
 if n==1:
  for q in b.find_all(style=True):q['style']=q['style'].replace('font-size:70px','font-size:76px').replace('font-size:88px','font-size:100px')
 if n==3:
  for q in b.find_all(style=True):q['style']=q['style'].replace('top:325px','top:302px').replace('top:181px','top:151px').replace('top:113px','top:91px')
 if n==6:
  for q in b.select('.box'):
   st=q['style'];st=st.replace('top:210px','top:148px').replace('top:168px','top:106px').replace('height:503px','height:519px');q['style']=st
 if n==11:
  q=b.select('.box')[0];q['style']+=';background:#329cf5;color:#fff;border-radius:7px';q.clear();q.append('이곳에 아이디어 또는 핵심 가치를 작성합니다.');q['style']+=';display:flex;align-items:center;justify-content:center;font-size:20px'
  for q in b.select('.pill'):q.decompose()
  for q in b.select('.box'):q['style']+=';border-radius:7px'
 if n==12:
  for q in b.select('.pill'):q['style']+=';height:68px;border-radius:6px;font-size:20px'
 if n==13:
  for q in b.select('.pill'):q.decompose()
  q=b.select('.box')[0];q['style']+=';background:#329cf5;color:#fff;border-radius:8px';
  for k in q.select('b,p'):k['style']=k.get('style','')+';color:#fff'
 if n==15:
  sc=b.select_one('.slide');sc.append(BeautifulSoup('<div class="line" style="left:279px;top:448px;width:923px;height:1px"></div><div class="line" style="left:689px;top:265px;width:1px;height:380px"></div>','html.parser'))
 if n==17:
  q=b.select_one('.donut');q['style']+=';background:#329cf5;border:20px solid #f6fbff';q['class'].append('filled')
  st=b.new_tag('style');st.string='.filled:before{background:#329cf5}.filled .inside b{color:white!important}';b.head.append(st) if b.head else b.insert(1,st)
 if n==19:
  for q in b.select('.box p'):q.insert(0,BeautifulSoup('<span class="check" style="width:18px;height:18px;background:#303331;border:0;margin-right:12px"></span>','html.parser'))
 if n==23:
  for q in b.select('.box h3'):q['style']=q.get('style','')+';margin-top:25px'
 if n==28:
  for q in b.select('.pill'):
   if 'Team Name' in q.get_text():q['style']+=';height:95px;border-radius:5px;white-space:normal;max-width:192px'
 if n==30:
  for q in b.find_all(style=True):q['style']=q['style'].replace('top:224px','top:194px').replace('top:442px','top:431px')
 p.write_text(str(b))
