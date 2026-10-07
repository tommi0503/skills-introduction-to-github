import json,copy,os
p='src/decks/group-b-data.json';d=json.load(open(p));q=json.load(open('review/quality/group-b.json'))
def up(s,i,r,**kw):
 k='p051/'+s;e=d[k]['elements'][i];old=copy.deepcopy(e);e.update(kw);q['pages'][k]['changes'].append({'element':i,'before':old,'after':copy.deepcopy(e),'reason':r})
def add(s,e,r):k='p051/'+s;d[k]['elements'].append(e);q['pages'][k]['changes'].append({'added':e,'reason':r})
def t(s,text,x,y,w,size=20,color='#fff',weight=400,spacing=0):add(s,{'kind':'text','text':text,'x':x,'y':y,'w':w,'h':5,'font':'DM Sans','size':size,'weight':weight,'color':color,'lineHeight':1.15,'letterSpacing':spacing},'판독 가능한 원문 문구 실제 DOM 복원')
up('s01-01',2,'원문 QIVORA native 글폭/중심 x56% 복원',x=39.5,size=107)
for i in [4,5,6,7]:up('s01-01',i,'원문 띄어진 소형 대문자 자간',letterSpacing=1.8,weight=600,size=22)
up('s01-02',2,'원문 회사명은 굵은 소제목',weight=600,size=28)
up('s01-02',3,'원문 본문5줄 밀도와 실제 좌측 column 폭 복원, 판독 불가 정상 문구',size=17.5,text='The warmest greeting upon this beautiful day.\nAfter this whole year, we provide you with\nan infographic that requires attention and\nthoughtful planning. Follow each step to\ndevelop the company and its future.',h=15,lineHeight=1.18)
for i in [6,7,8,9]:up('s01-02',i,'원문 small allcaps 실제 자간',letterSpacing=1.6,weight=600,size=22)
for s in ['s01-03','s05-01']:
 up(s,17,'원문 Sales Report 잉크폭 약370px, 이전402px보다 작게',size=61,y=8)
 up(s,18,'원문 This Year 실제 두 줄 피치',lineHeight=1.0,y=8)
 up(s,19,'원문 caption 실제 글폭과 크기',size=32,weight=500)
 for i in [22,23,24,25]:up(s,i,'원문 도넛 제목은 작은 26px bold',size=24,weight=700,align='left',x=[6,29,52,75][i-22],w=22)
 for j in range(4):
  x=13+23*j
  add(s,{'kind':'box','fill':'#fff','radius':'50%','x':x,'y':79.3,'w':.4,'h':.71},'원문 작은 도넛 legend 점 복원')
  add(s,{'kind':'box','fill':'#eebc1c','radius':'50%','x':x+4,'y':79.3,'w':.4,'h':.71},'원문 작은 도넛 legend 점 복원')
  t(s,'2018',x+.7,78.8,3.5,11);t(s,'2019',x+4.7,78.8,3.5,11)
for s in ['s01-04','s05-02']:
 up(s,19,'원문 Target Market 글폭은 Montserrat bold 가까움: 실제 native width에 대응',font='Montserrat',size=53,weight=700,lineHeight=1.1,h=20)
 up(s,20,'원문 작은 3행 product caption은 굵기500',weight=500,size=29)
 up(s,32,'원문 3색 점 legend를 분리 DOM 구성',text='',size=13.5)
 for j,(label,c) in enumerate([('Product 1','#eebc1c'),('Product 2','#fff'),('Product 3','#ba9413')]):
  add(s,{'kind':'box','fill':c,'radius':'50%','x':53+9.5*j,'y':89.7,'w':.5,'h':.89},'원문 chart legend actual 색점')
  t(s,label,53.8+9.5*j,89.3,9,13.5)
up('s01-05',5,'원문 실제 타이틀 중심50%, y20%',x=31,y=19.5)
for i in [6,9,12,15]:up('s01-05',i,'원문 S/W/O/T 실제 잉크높이 약75px',size=105,h=20)
for i in [7,10,13,16]:up('s01-05',i,'원문 작은 label은 굵게',size=22,weight=600)
for i in [8,11,14,17]:up('s01-05',i,'원문 각 column 본문6줄 밀도',size=17.5,text='The warmest greeting upon\nyou on this beautiful day.\nMay the blessing of the\nLord be upon us every\ntime and every day. Plan\ntogether for tomorrow.',lineHeight=1.15,h=18)
for i,cs in [(1,['#e5b929','#cc9f15']),(2,['#27313c','#23303c']),(3,['#e5b929','#cc9f15']),(4,['#475465','#445363'])]:
 e=d['p051/s01-05']['elements'][i];e.update(kind='graphic',graphic='b-gradient-panel',colors=cs);e.pop('fill',None);e.pop('radius',None);q['pages']['p051/s01-05']['changes'].append({'element':i,'reason':'원문 column actual tone/gradient. simple graphic 직접 구현','colors':cs})
up('s01-06',4,'원문 subtitle 잉크폭은 현재보다 약16% 작음',size=32,weight=500)
for i in [6,9,12]:up('s01-06',i,'원문 Range y62.5%',y=62.5,size=19,weight=500)
for i in [7,10,13]:up('s01-06',i,'원문 가격 실제 baseline y67%',y=67,size=42)
for i in [14,15,16,17]:up('s01-06',i,'원문 소형 대문자 실제 tracking',letterSpacing=1.5,weight=600,size=22)
up('s01-07',8,'원문 Development Plan의 실제 글폭: Montserrat700으로 원문 노출부 width 회복',font='Montserrat',size=61,lineHeight=1.04,h=24)
# source exploded first yellow pie, preserve original visible size. Other pie remains inferred where source cut.
k='p051/s01-07';old=d[k]['elements'][:8];d[k]['elements']=d[k]['elements'][8:];d[k]['elements'].insert(0,{'kind':'graphic','graphic':'b-exploded-pie','colors':['#fff','#cba315','#263340','#edbf16'],'variant':'marketing','x':8,'y':44.7,'w':23.5,'h':41.8});d[k]['elements'].insert(1,{'kind':'graphic','graphic':'b-exploded-pie','colors':['#fff','#263340','#cba315','#edbf16'],'variant':'community','x':59,'y':44.7,'w':23.5,'h':41.8});q['pages'][k]['changes'].append({'removed':old,'reason':'원문 pie 크기/outlined/exploded yellow slice는 semantic arc SVG로 직접 복원'})
for e in d[k]['elements']:
 if e['kind']=='box' and e.get('y')==93:e.update(w=.5,h=.89,radius='50%',x=12+[7,17,27,37].index(e['x'])*4.2,y=89.5)
 if e['kind']=='text' and e.get('text') in ['2018','2019','2020','2021']:e.update(x=12.8+['2018','2019','2020','2021'].index(e['text'])*4.2,y=89,size=11,w=3.5)
up('s01-08',5,'원문 timeline 제목 실제 width와 가족 Montserrat700 대응',font='Montserrat',size=56,lineHeight=1.1,h=22)
for i in [6,7,8,9]:up('s01-08',i,'원문 year KPI는 native 약31px',size=31.5)
for i in [10,11,12,13]:up('s01-08',i,'원문 card 본문 density와 글씨 굵기',weight=500,size=17.5)
up('s01-08',14,'원문 네 footer caption 위치가 기존 한 text 공백에서 크게 어긋남',text='')
for label,x in [('PROFESSIONAL',6),('INFOGRAPHIC',29),('STATISTIC',60),('PRESENTATION',78)]:t('s01-08',label,x,88,20,21,'#fff',600,1.6)
up('s01-09',14,'원문 subtitle 실제 글폭 약670px native',size=32,weight=500)
for i,y in [(15,55),(16,69),(17,55),(18,69)]:up('s01-09',i,'원문 timeline year 크기와 아래 row y70%',size=30,y=y)
for i,y in [(19,61.5),(20,76),(21,61.5),(22,76)]:up('s01-09',i,'원문 본문은 year 바로 아래 2% gap',y=y)
up('s01-10',1,'원문 연락처 card 실제 navy 색',fill='#2c3441')
up('s01-10',2,'원문 card Contact Info actual y34%',y=34,size=34,weight=500)
up('s01-10',3,'원문 연락처 actual y54%',y=54)
up('s01-10',4,'원문 세로 QIVORA top35%로 이동',y=65,size=56,x=27.5)
for label,x,y in [('PROFESSIONAL',6,8),('INFOGRAPHIC',33,8),('STATISTIC',54,88),('PRESENTATION',78,88)]:t('s01-10',label,x,y,22,22,'#fff',600,1.6)
# actual source regional RGB measurements (simple tonal gradients, not textures embedded as raster)
for s,cs,measured in [('s01-02',['#1d242e','#14202a'],'#1d242e'),('s01-04',['#272f38','#475464'],'#272f38'),('s05-02',['#3e4b5c','#506075'],'#475464'),('s01-06',['#3f4d5f','#506075'],'#465363'),('s01-07',['#3f4c5e','#4a5a6b'],'#495666'),('s01-09',['#222b35','#354352'],'#222b35')]:
 k='p051/'+s;e={'kind':'graphic','graphic':'b-gradient-panel','colors':cs,'x':0,'y':0,'w':100,'h':100};d[k]['elements'].insert(0,e);q['pages'][k]['changes'].append({'reason':'원본 평탄 navy영역 실제 RGB 중간값에 근거한 각 페이지 단순 gradient 복원','sourceMedianRGB':measured,'colors':cs});q['pages'][k]['measurements'].append({'region':'empty navy background patch','sourceMedianRGB':measured})
for k,v in d.items():
 if k.startswith('p051'):
  for e in v['elements']:
   if e['kind']=='image':q['pages'][k]['remaining'].append({'placeholder':'real photograph of sea/building/workplace/device','reason':'복잡 사진·기기 화면은 사용자 지시대로 회색 유지','region':[e['x'],e['y'],e['w'],e['h']]})
json.dump(d,open(p+'.b.tmp','w'),ensure_ascii=False,indent=2);os.replace(p+'.b.tmp',p);json.dump(q,open('review/quality/group-b.json','w'),ensure_ascii=False,indent=2)
