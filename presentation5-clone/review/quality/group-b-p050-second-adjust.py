import json,copy
p='src/decks/group-b-data.json';d=json.load(open(p));q=json.load(open('review/quality/group-b.json'))
def up(s,i,reason,**kw):
 k='p050/'+s;e=d[k]['elements'][i];before=copy.deepcopy(e);e.update(kw);q['pages'][k]['changes'].append({'element':i,'before':before,'after':copy.deepcopy(e),'reason':reason})
for s,i,text in [('s02-02',7,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nUt enim ad minim veniam, quis nostrud exercitation.'),('s02-03',4,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nSed do eiusmod tempor incididunt ut labore et dolore.')]:
 es=d['p050/'+s]['elements'];idx=next(i for i,e in enumerate(es) if e.get('font')=='DM Sans' and e.get('y',0)>80);up(s,idx,'실제 native PNG에서 본문이 사진 영역에 침범하여 정상 대체문구 줄폭 보정',text=text,w=54 if s=='s02-02' else 49)
es=d['p050/s02-10']['elements'];idx=next(i for i,e in enumerate(es)if e.get('font')=='DM Sans');up('s02-10',idx,'원문 오른쪽 2줄 설명, 본문 우측 안전 폭 보정',text='Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nSed do eiusmod tempor incididunt ut labore et dolore magna.',w=43)
# actual painted text stays inside stage; box-height no longer derives empty font descent
for k,v in d.items():
 if not k.startswith('p050'):continue
 for i,e in enumerate(v['elements']):
  if e['kind']=='text' and e.get('font')=='Bebas Neue':
   if e['y']+e['h']<98: e['h']=min(100-e['y'],e['h']+3)
q['pages']['p050/s02-06']['measurements'].append({'actualFinalInk':'THANK YOU native PNG painted bottom 676px; empty font descent Range to741px excluded by root painted-ink audit','originalApproxInkBottom':669})
k='p050/s02-08';e={'kind':'text','x':42.5,'y':85.5,'w':52.5,'h':8,'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nSed do eiusmod tempor incididunt ut labore et dolore.','size':18,'font':'DM Sans','weight':400,'color':'#fff','align':'right','lineHeight':1.5,'nowrap':True};d[k]['elements'].append(e);q['pages'][k]['changes'].append({'added':e,'reason':'개별 native PNG 확인에서 원문 노출부 오른쪽 하단 설명의 실제 누락 확인·정상 2줄 복원'})
# native original chart vertices individually inspected
pts=[(9,80.5),(16.5,73.8),(23.5,62.4),(30.9,70.8),(38.3,58.9),(45.5,39)]
up('s02-11',10,'원문 선 차트 실제 6개 vertex 및 데이터 marker 위치 복원',points=[{'x':x,'y':y}for x,y in pts],strokeWidth=3)
for j,(x,y)in enumerate(pts):
 up('s02-11',12+j,'선 vertex 위 실제 marker 중심',x=x-.5,y=y-.885)
 up('s02-11',22+j,'원문 년도는 각 실제 vertex 아래 중앙',x=x-3.5)
for i in range(5):
 up('s02-14',i,'원문 날짜 카드 상단 y35%',y=35)
 # dates are chip elements for actual ink center: move y up3% independently
 up('s02-14',8+i*2,'원문 큰 날짜와 weekday 사이 여백 복원',y=d['p050/s02-14']['elements'][8+i*2]['y']-3)
 up('s02-14',9+i*2,'원문 weekday는 카드 하단 y60%',y=60)
up('s02-15',2,'원문 백분율 기호는 숫자보다 작음',text='80,2',x=11,w=28,h=31)
up('s02-15',3,'원문 백분율 기호는 숫자보다 작음',text='20,5',x=55,w=28,h=31)
for x,color in [(38,'#fff'),(82,'#ef0015')]:d['p050/s02-15']['elements'].append({'kind':'text','text':'%','font':'DM Sans','weight':400,'size':98,'color':color,'x':x,'y':50,'w':8,'h':22,'lineHeight':1.12,'nowrap':True})
up('s02-15',4,'원문 왼쪽 eyebrow 중앙 x31%',x=10,w=41)
up('s02-15',5,'원문 오른쪽 eyebrow 중앙 x70%',x=49,w=42)
q['pages']['p050/s02-15']['changes'].append({'reason':'원문 큰 숫자 대비 % 작은 크기98px DOM 별도 복원, actual PNG %과 숫자 baseline 확인 예정'})
for k,v in d.items():
 if k.startswith('p050'):
  for e in v['elements']:
   if e['kind']=='image':q['pages'][k]['remaining'].append({'placeholder':'film photograph / device screen','reason':'실사 인물·사진·기기 화면만 회색 유지','region':[e['x'],e['y'],e['w'],e['h']]})
e=d['p064/s04-01']['elements'][8];e.pop('borderColor',None);e.pop('borderWidth',None);e['border']='1px solid #e9e1ec'
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2);json.dump(q,open('review/quality/group-b.json','w'),ensure_ascii=False,indent=2)
