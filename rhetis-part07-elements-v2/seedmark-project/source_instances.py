"""Contract markup for measured instances; fixture copy is newly worded."""
from pathlib import Path
import json,re,math
from lxml import html
import fixtures as F
P=F.P;C=F.C;A=json.loads((P/'map.json').read_text());RAW={p['page']:p['nodes']for p in A['rawMeasurements']}
ROOTS={'chart-donut':'donut','chart-bar':'bars','chart-line':'lines','chart-area':'areas','steps':'steps','flowchart':'flowchart','agenda':'agenda','concentric':'orbit','positioning':'posmap','venn':'venn','person':'person','timeline':'track','list':'list','legend':'legend'}
def E(leaf,cl,body,attrs=''):return f'<div class="{cl}" data-el="seedmark-{leaf}" {attrs}>{body}</div>'
def ico(n='briefcase-business'):return f'<span class="icon" data-icon="{n}"></span>'
def p(cl,t):return f'<p class="{cl}">{t}</p>'
def card(name,note='',kick='',mark='',cl=''):
 return E('card','card '+cl,'<div class="parts">'+(f'<span class="mark">{mark}</span>'if mark else'')+(p('kick',kick)if kick else'')+p('name',name)+p('note',note)+'</div>')
def prose(t,cl=''):return E('prose','prose '+cl,'<p>'+t+'</p>')
def original_html(n):
 e=html.fromstring(n['html']);s=(e.text or'')+''.join(html.tostring(q,encoding='unicode',method='html')for q in e)
 s=re.sub(r' class="[^"]*"','',s);s=re.sub(r' style="[^"]*"','',s);s=s.replace('<span>','<b>').replace('</span>','</b>');return s

def normalized_output(s):
 from contract_markup_review import normalize_markup
 return normalize_markup(s)

def make(inst,original=False):
 page=inst['page'];leaf=inst['leaf'];idx=[int(re.search(r'nth-child\((\d+)\)',s).group(1))-1 for s in inst['selectors']if 'main >'in s];ns=[RAW[page][i]for i in idx];seed=page*19
 def tx(n):return original_html(n)if original else F.fresh(n.get('text',''),seed+n.get('index',0))
 def at(i):return tx(RAW[page][i])
 ts=[n for n in ns if n.get('text','').strip()]
 def T(i,default=''):return tx(ts[i])if i<len(ts)else default
 if leaf=='prose'and inst['id']in['sm-03-01','sm-18-02']and not original:
  lines={3: ['각 부서의 승인 흐름을 살펴보고 이번 분기 KPI 기준을 합의합니다.', '현장 접수 항목을 묶어 P1 작업부터 정리하고 담당 권한을 나눕니다.', '팀 간 의존 업무에는 ETA를 기록해 변경 내역을 빠르게 공유합니다.', '제품 검토 회의는 실증 자료와 고객 응답을 기반으로 준비합니다.', '납기 준수율과 결함 수치를 함께 읽어 개선할 지점을 골라냅니다.', '새 운영안은 한 곳에서 시험한 뒤 검증한 범위부터 넓혀갑니다.', '부서별 실행 내역과 예산을 연결해 분기별 손익 변화를 살핍니다.', '정리한 근거는 차기 로드맵과 영업 제안에 다시 반영합니다.'], 18: ['보유한 운영 절차와 검증 근거를 투자 검토 자료로 함께 정리합니다.', '팀 내부 검토 기준은 외부 협업사도 이해할 수 있게 풀어씁니다.', '핵심 설계와 서비스 경계를 나누고 각 책임 범위를 분명히 묶습니다.', '상용화에 필요한 권한 관리와 데이터 품질 기준을 먼저 합의합니다.', '실증 과정에서 얻은 개선 내역은 분기별 제품 로드맵에 반영합니다.', '같은 문제를 되풀이하지 않도록 변경 기록과 승인 내역을 보관합니다.', '이 체계를 기반으로 신규 거래망과 장기 협업 범위를 넓혀갑니다.']}[page]
  return E(leaf,'prose','<p>'+'<br>'.join(lines)+'</p>'),('8x3'if page==3 else'6x2')
 if leaf=='headline'and page in[7,15]and not original:
  s='이번 분기에는 고객별<br><b>요구와 납기 일정부터</b><br>차근차근 조율해 봅시다.'if page==7 else'부서마다 달랐던 기준을<br><b>하나의 협업 체계로</b><br>깔끔하게 정리해 봅시다.'
  return E(leaf,'headline','<h2>'+s+'</h2>'),'6x3'
 if leaf=='card'and page==10:
  k=6+(int(inst['id'][-2:])-1)*6
  pricing=E('list','list check',''.join('<div class="item">'+p('name',t if original else [['기본 운영안 적용','분기 개선안 실행'],['납기 준수율 98%'],['검토 주기별 예산 배정'],['조율한 일정대로 납품']][int(inst['id'][-2:])-1][j])+p('note','')+'</div>'for j,t in enumerate(RAW[10][k+4]['text'].splitlines())))
  return normalized_output(E(leaf,'card '+inst.get('contractVariant',''),'<div class="parts">'+p('kick',at(k))+p('name',at(k+1))+p('note',at(k+3))+pricing+'</div>')),'4x4'
 if leaf=='headline'and page==2:
  return E(leaf,'headline big','<h2>'+at(2)+'<br>'+(at(3)if '<b>'in at(3)else'<b>'+at(3)+'</b>')+'</h2>'+p('note',at(4))),'6x4'
 if leaf=='pill'and page==20:
  if inst['id']=='sm-20-01':
   lines=RAW[20][5]['text'].splitlines();name=lines[0]if original else F.fresh(lines[0],seed);note=lines[1]if original else F.fresh(lines[1],seed+1)
   return E(leaf,'pill','<div class="parts">'+p('mark',at(6))+p('name','<b>'+name+'</b>')+p('note',note)+'</div>'),'4x3'
  return E(leaf,'pill line','<div class="parts">'+p('mark',at(8))+p('name',at(9))+'</div>'),'4x3'
 if leaf=='card'and page==20:
  if inst['id']=='sm-20-03':
   return card(at(12),at(20),at(13)),'4x5'
  chart=next(i for i in A['instances']if i.get('id')=='sm-20-bars')
  bar='' if chart['use']=='unexpressible' else make(chart,original)[0]
  return E(leaf,'card','<div class="parts">'+p('name',at(14))+p('kick',at(15))+bar+'</div>'),'4x5'
 if leaf in ['headline','prose','metric','tag','callout','card','pill'] and not original:
  got=F.semantic(inst)
  if got:return got
 if leaf=='headline':return E(leaf,'headline '+(inst.get('contractVariant','')),'<h2>'+T(0)+'</h2>'+(''if len(ts)<2 else p('note',T(1)))),'6x2'
 if leaf=='prose':return E(leaf,'prose '+inst.get('contractVariant',''),''.join('<p>'+tx(n)+'</p>'for n in ts[:4])),'4x2'
 if leaf=='metric':return E(leaf,'stat','<div class="parts">'+p('fig',T(0))+p('name',T(1))+p('note',T(2))+'</div>'),'6x2'
 if leaf=='tag':return E(leaf,'tag','<span>'+T(0)+'</span>'),'2x1'
 if leaf=='callout':return E(leaf,'callout','<p>'+T(0)+'</p>'),'8x2'
 if leaf=='pill':return E(leaf,'pill '+inst.get('contractVariant',''),'<div class="parts">'+p('mark',T(1))+p('name',T(0))+p('note',T(2))+'</div>'),'4x2'
 if leaf=='card':
  mark=any('icon'in n.get('classes','')for n in ns)
  kick=next((tx(n)for n in ts if float(n.get('fontSize','18px').replace('px',''))<16),'')
  name=next((tx(n)for n in ts if float(n.get('fontSize','18px').replace('px',''))>=22),T(0))
  note=next((tx(n)for n in ts if len(n['text'])>30),T(len(ts)-1))
  cl=inst.get('contractVariant','')
  return card(name,note,kick,ico()if mark else'',cl),('6x2'if inst['bbox'][2]/inst['bbox'][3]>2.5 else'4x4')
 if leaf=='legend':return E(leaf,'legend',''.join(f'<span class="key tone-{5 if j==0 else 1}">{n["text"] if original else F.fresh(n["text"],seed+j)}</span>'for j,n in enumerate(inst['sourceMeasurements']))),'3x2'
 if leaf=='agenda':
  entries=[]
  for n in ns:
   if re.fullmatch(r'\d{2}',n.get('text','').strip()):
    z=n['index'];entries.append('<div class="entry">'+p('mark',n['text'])+p('name',at(z+1))+p('note','')+'</div>')
  return E(leaf,'agenda',''.join(entries)),'8x5'
 if leaf=='steps':
  items=[]
  if page==3:
   for name,note in [(11,12),(16,17)]:items.append('<div class="step"><span class="mark">'+ico('gem'if name==11 else'lightbulb')+'</span>'+p('name',at(name))+p('note',at(note))+'</div>')
   return E(leaf,'steps col',''.join(items)),'8x4'
  for j in range(5):
   base=6+j*5;items.append('<div class="step"><span class="mark">'+ico(['users','gem','gift','target','lightbulb'][j])+'</span>'+p('name',at(base+2))+p('note',at(base+3))+'</div>')
  return E(leaf,'steps',''.join(items)),'12x3'
 if leaf=='concentric':
  return E(leaf,'orbit',''.join('<div class="ring">'+p('name',('TAM','SAM','SOM')[j]if original else('총수요','유효량','초기량')[j])+p('fig',at(7+j).split('<br>')[-1]if original else('(전체 범주)','(유효 범주)','(우선 범주)')[j])+ '</div>'for j in range(3))),'6x5'
 if leaf=='chart-donut':
  ds=[]
  for k,j in enumerate([6,8,10]):
   v=re.search(r'--v:([\d.]+)',RAW[page][j]['html']).group(1)
   ds.append(E(leaf,'donut',p('fig',at(j))+'<div class="name">'+E('tag','tag','<span>'+at(j+1)+'</span>')+'</div>',f'style="--v:{v}"'))
  return E(leaf,'donuts',''.join(ds)),'10x4'
 if leaf in ['chart-bar','chart-area','chart-line']:
  ps=[q for n in ns for q in n.get('primitives',[])];labels=[q['text']for q in ps if q['tag']=='text'and('년'in q.get('text','')or'월'in q.get('text',''))]
  if not original:labels=[f'{j+1}월'for j in range(len(labels))]
  if leaf=='chart-bar':
   rect=[]
   for q in ps:
    if q['tag']=='rect':
     el=html.fromstring(q['source']);h=float(el.get('height','0'))
     if h>10:rect.append((h,el.get('fill','')))
   mx=max((h for h,_ in rect),default=100);bars=[]
   paired=len(rect)==len(labels)*2
   for j,(h,color)in enumerate(rect):
    lab=labels[j//2]if paired and j%2 else(''if paired else(labels[j]if j<len(labels)else''))
    tone='tone-1'if color.lower()in ['#2b2b2a','#333','#2b2b2b','#2c2c2b']else'tone-5'
    bars.append(f'<div class="bar {tone}" style="--v:{h/mx*100:.3f}"><b></b><span>{lab}</span></div>')
   return E(leaf,'bars',''.join(bars),'style="--max:100"'),'6x4'
  circles=[]
  for q in ps:
   if q['tag']=='circle':circles.append(float(html.fromstring(q['source']).get('cy','0')))
  baseline=max(circles,default=173)+10;peak=min(circles,default=20);vals=[(baseline-y)/(baseline-peak)*100 for y in circles]or[18,12,29,55,80,95]
  labels=labels[:len(vals)]or[f'{j+1}월'for j in range(len(vals))]
  if leaf=='chart-line':return E(leaf,'lines',''.join(f'<div class="pt" style="--v:{v:.3f}"><b></b><span>{lab}</span></div>'for v,lab in zip(vals,labels)),'style="--max:100"'),'6x3'
  return E(leaf,'areas','<div class="series tone-1"><p class="name"></p>'+''.join(f'<div class="pt" style="--v:{v:.3f}"><b></b></div>'for v in vals)+'</div><div class="axis">'+''.join(f'<span>{lab}</span>'for lab in labels)+'</div>','style="--max:100"'),'6x3'
 if leaf=='positioning':
  labels=[at(k)for k in[8,9,6,7]];xs=[27,28,67,77];ys=[72,22,28,87];names=[at(k)for k in[11,13,15,16]]
  return E(leaf,'posmap','<div class="axis-x"><span>'+labels[0]+'</span><span>'+labels[1]+'</span></div><div class="axis-y"><span>'+labels[2]+'</span><span>'+labels[3]+'</span></div>'+''.join(f'<div class="mark {"on"if j==3 else""}" style="--x:{x};--y:{y}">'+p('name',names[j])+'</div>'for j,(x,y)in enumerate(zip(xs,ys)))),'6x5'
 if leaf=='list':
  return E(leaf,'list divided',''.join('<div class="item"><span class="mark">'+ico(ic)+'</span>'+p('name',at(k))+p('note','')+'</div>'for k,ic in[(20,'check-check'),(24,'crosshair'),(28,'gem')])),'6x4'
 if leaf=='venn':return E(leaf,'venn',''.join('<div class="set">'+p('name',at(k))+'</div>'for k in[19,20,21])+'<div class="core">'+at(18)+'</div>'),'6x5'
 if leaf=='person':
  ph=next((n for n in ns if 'photo'in n['classes']),None);role=next((n for n in ts if 'mini'in n['classes']),None);name=next((n for n in ts if 'bold'in n['classes']),None);career=next((n for n in ts if '•'in n['text']),None)
  bits='<div class="seat avatar" data-ph="'+('' if original else '1')+'"></div>'+p('name',tx(name))+p('note',tx(role))
  if career:bits+=E('list','list',''.join('<div class="item">'+p('name',F.fresh(x,seed+j)if not original else x)+p('note','')+'</div>'for j,x in enumerate(career['text'].replace('\n',' ').split('•'))if x.strip()))
  return normalized_output(E(leaf,'person',bits)),'3x4'
 if leaf=='timeline':
  stops=[]
  for j in range(5):
   media=E('image-frame','frame','<div class="seat" data-ph="'+('' if original else str(j+1))+'"></div>')
   stops.append('<div class="stop">'+p('kick','')+'<div class="name">'+media+'</div>'+p('note',at(7+j*3))+'</div>')
  return E(leaf,'track',''.join(stops)),'10x4'
 if leaf=='flowchart':
  nodes=[]
  def node(content,c,r,w=1,h=1,cl=''):return f'<div class="node {cl}" style="grid-column:{c} / span {w};grid-row:{r} / span {h}">{content}</div>'
  if page==6:
   for j in range(4):
    top=E('pill','pill on','<div class="parts">'+p('mark',at(7+j*5))+p('name',at(6+j*5))+'</div>')
    nodes.append(node(top,j+1,1,1,2,'start to-d'+(' to-r'if j<3 else'')))
    nodes.append(node(card('',at(10+j*5)),j+1,3,1,4))
   return E(leaf,'flowchart',''.join(nodes)),'12x6'
  if page==12:
   for j in range(3):
    v=[60,20,20][j];nm=('수익원 '+str(j+1))if original else('사업 부문 '+str(j+1));d=E('chart-donut','donut',p('fig',str(v)+'%')+p('name',nm),f'style="--v:{v}"')
    nodes.append(node(d,j+1,1,1,3,'to-d'));nodes.append(node(prose(at(15+j*3)),j+1,4,1,2))
   return E(leaf,'flowchart',''.join(nodes)),'6x5'
  if page==9:
   def tiles(start):return '<div class="group">'+''.join(card(at(k+2),'','',ico('settings'),'quiet')for k in range(start,start+9,3))+'</div>'
   nodes=[node(tiles(16),1,1,3,3,'to-r'),node(card('',at(34)),1,4,3,3),node(card('',at(35)),8,1,3,3),node(tiles(25),8,4,3,3),node('<!-- unexpressible: cylindrical stores, see GAPS.md -->',4,1,4,4,'to-d to-r'),node(E('pill','pill on','<div class="parts">'+p('name',at(36))+'</div>'),4,5,4,2,'to-r')]
   return E(leaf,'flowchart',''.join(nodes)),'12x6'
 return None

for inst in A['instances']:
 if inst['use']=='unexpressible'or inst['leaf']=='foundation'or not inst.get('fixture'):continue
 got=make(inst)
 if not got:continue
 markup,mini=got
 if inst['leaf']=='prose'and inst['id']not in['sm-03-01','sm-18-02']and len(re.sub('<[^>]*>','',markup))>110:mini='6x3'
 if inst['leaf']=='headline'and inst['bbox'][3]>150 and inst['page']!=2:mini='6x3'
 if 'style="'in markup.split('>')[0]:markup=re.sub(r'style="', 'style="grid-column:1 / span 12;grid-row:1 / span 6;',markup,count=1)
 else:markup=markup.replace('>',' style="grid-column:1 / span 12;grid-row:1 / span 6">',1)
 (C/inst['fixture']).write_text(f'<!-- min: {mini} -->\n'+markup+'\n')
# Context components in format fixtures retain their own scope registration.
for f in (C/'elements/tag/fixtures').glob('*.html'):
 s=f.read_text()
 if '<div class="prose"'in s and 'data-el="seedmark-prose"'not in s:s=s.replace('<div class="prose"','<div class="prose" data-el="seedmark-prose"',1);f.write_text(s)
# A strict stable series exercises the positive rectangle line formula without a value-specific CSS branch.
f=C/'elements/chart-line/fixtures/stability-6.html';f.write_text('<!-- min: 6x3 -->\n'+E('chart-line','lines',''.join(f'<div class="pt" style="--v:44"><b>44</b><span>{j+1}월</span></div>'for j in range(6)),'style="--max:100;grid-column:1 / span 12;grid-row:1 / span 6"'))
print('Wrote replica-instance fixtures from map; original source files unchanged.')

from contract_markup_review import fix_collection
fix_collection()
