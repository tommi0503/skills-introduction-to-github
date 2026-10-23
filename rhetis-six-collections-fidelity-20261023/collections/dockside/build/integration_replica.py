from pathlib import Path
from bs4 import BeautifulSoup
D=Path('/workspace/work/deliverables/dockside/review/replica')
def svg(paths):return '<svg viewBox="0 0 24 24" style="width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:1.5;flex:none">'+paths+'</svg>'
IC={
 'target':svg('<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><path d="m12 12 9-9M16 3h5v5"/>'),
 'hierarchy':svg('<rect x="8" y="2" width="8" height="5" rx="1"/><path d="M12 7v6M4 13h16M4 13v4m8-4v4m8-4v4"/><rect x="1" y="17" width="6" height="5" rx="1"/><rect x="9" y="17" width="6" height="5" rx="1"/><rect x="17" y="17" width="6" height="5" rx="1"/>'),
 'trophy':svg('<path d="M8 3h8v7a4 4 0 0 1-8 0V3zM8 5H4v3a4 4 0 0 0 4 4m8-7h4v3a4 4 0 0 1-4 4m-4 2v6m-4 1h8"/>'),
 'expand':svg('<path d="M3 9V3h6m6 0h6v6M3 15v6h6m6 0h6v-6M3 3l7 7m11-7-7 7M3 21l7-7m11 7-7-7"/>'),
 'money':svg('<rect x="4" y="3" width="12" height="18" rx="1"/><path d="M7 7h6m-6 4h6m-6 4h4"/><circle cx="18" cy="16" r="5"/><path d="m15 16 1 2 2-4 2 4 1-2"/>'),
 'users':svg('<circle cx="8" cy="8" r="3"/><path d="M2 20v-3a6 6 0 0 1 12 0v3"/><circle cx="19" cy="6" r="4"/><path d="M17 5h4m-4 2h3"/>'),
 'mail':svg('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>'),
 'phone':svg('<path d="M6 3 3 5c0 9 7 16 16 16l2-3-5-4-2 2-6-6 2-2-4-5z"/>'),
 'message':svg('<path d="M4 4h16v13H9l-5 4V4zM8 8h8M8 12h5"/>')}
for n in [2,5,9,10,16,17,20,21,23,25,28,30]:
 p=D/f'slide_{n:02}.html';b=BeautifulSoup(p.read_text(),'html.parser');sc=b.select_one('.slide');extra=''
 if n==2:
  q=[x for x in b.select('.capsule') if x.get_text().strip().startswith('Keyword')]
  for j,x in enumerate(q):x.insert(0,BeautifulSoup(IC[['target','hierarchy','trophy','expand'][j]],'html.parser'));x['style']+=';display:flex;gap:8px;align-items:center;justify-content:center;padding:0;color:#5897bf'
 if n==5:
  q=b.select_one('.donut');q['class']=['bubble'];q['style']+=';position:absolute;border-radius:50%;background:linear-gradient(#329cf5,#e6f0f7);border:0;display:grid;place-items:center;color:white';q.select_one('b')['style']='font-size:36px';q=b.select_one('.bubble .inside');q['style']='text-align:center'
 if n==9:
  texts=['타깃 고객의 실제 행동이나 구매 패턴에서 발견한 특이점을 작성합니다.','기존 서비스나 경쟁사가 놓치고 있는 영역이나 약점을 작성합니다.','최근 기술 발전이나 인프라 개선으로 새롭게 실현 가능해진 솔루션을 작성합니다.']
  for q,t in zip(b.select('.box p'),texts):q.string=t
 if n==10:
  for q in b.select('.pill'):q['style']+=';background:#ffffff90;color:#578bab;border:2px solid #fff;box-shadow:none'
 if n==16:
  for q in b.select('.box'):q['class'].append('folder')
  extra+='.folder::before{content:"";position:absolute;left:-2px;top:-40px;width:213px;height:43px;background:#f7f8f8;border:2px solid white;clip-path:polygon(0 0,75% 0,92% 95%,100% 100%,0 100%);border-radius:20px 18px 0 0}'
  for q in b.select('.pill'):
   if '○' in q.get_text():q.string=q.get_text().replace('　○','');q.append(BeautifulSoup('<i style="display:block;width:21px;height:21px;border-radius:50%;border:3px solid #c8edff;background:#fff;margin-left:12px"></i>','html.parser'))
 if n==17:
  q=b.select_one('.filled');q['class']=['solid-core'];q['style']+=';position:absolute;display:flex;align-items:center;justify-content:center;border-radius:50%;background:#329cf5;color:#fff';q.select_one('b')['style']='font-size:26px;color:#fff'
 if n==20:
  for j,q in enumerate(b.select('.inside')):
   ico=BeautifulSoup(IC['money' if j==0 else 'users'],'html.parser');ico.svg['style']+=';width:57px;height:57px;color:#429bda';q.insert(0,ico)
 if n==21:
  for q in b.select('.small'):
   if '예상되는 효과' in q.get_text():q['style']=q['style'].replace('left:514px','left:450px').replace('width:256px','width:330px');q.string='• 예상되는 효과를 구체적으로 작성합니다. 개선 전후 수치나 예시를 포함합니다.'
 if n==23:
  for q in b.select('.box'):
   k=q.select_one('.small')
   if k and k.get_text().strip().startswith('Step'):
    k['style']=k.get('style','')+';margin-top:29px';q.select_one('h3')['style']='font-size:18px;margin:4px 0';q.select_one('p')['style']='font-size:14px;line-height:1.5'
 if n==25:
  sc.append(BeautifulSoup('<svg viewBox="0 0 24 24" style="position:absolute;left:676px;top:447px;width:30px;height:30px;fill:none;stroke:#439bda;stroke-width:2"><path d="m5 4 7 7 7-7M5 12l7 7 7-7"/></svg>','html.parser'))
 if n==28:
  for q in b.select('.connector'):q.decompose()
  z=BeautifulSoup('<svg viewBox="0 0 1280 720" style="position:absolute;inset:0;width:1280px;height:720px;fill:none;stroke:#d4d4d4;stroke-width:2;z-index:0"><path d="M500 357h35q25 0 25 25v140q0 25-25 25h-35M560 452h28M865 357h-30q-25 0-25 25v140q0 25 25 25h30M810 452h-30"/></svg>','html.parser');sc.insert(1,z)
  for q in b.select('.pill'):
   if 'Team Name' in q.get_text():q.clear();q.append(BeautifulSoup('<span style="text-align:center">Team Name<br>팀이름</span>','html.parser'))
 if n==30:
  for j,q in enumerate(b.select('.capsule')):
   q.insert(0,BeautifulSoup('<span style="background:#303331;color:white;width:36px;height:36px;border-radius:50%;display:grid;place-items:center">'+IC[['mail','phone','message'][j]]+'</span>','html.parser'));q['style']+=';display:flex;align-items:center;justify-content:center;gap:15px;padding-top:0'
 if extra:
  st=b.new_tag('style');st.string=extra;sc.insert(0,st)
 p.write_text(str(b))
