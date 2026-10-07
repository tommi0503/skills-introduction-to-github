import json,copy,os
P='src/decks/group-b-data.json';d=json.load(open(P));q=json.load(open('review/quality/group-b.json'));fm={t:w for t,w,h in json.load(open('review/quality/group-b-p073-font-metrics.json'))['Quicksand Variable']}
def es(s):return d['p073/'+s]['elements']
def up(s,i,r,**kw):
 e=es(s)[i];old=copy.deepcopy(e);e.update(kw);q['pages']['p073/'+s]['changes'].append({'element':i,'before':old,'after':copy.deepcopy(e),'reason':r})
def add(s,e,r):es(s).append(e);q['pages']['p073/'+s]['changes'].append({'added':copy.deepcopy(e),'reason':r})
def dot(s,x,y,c='#eb812e',w=.45):add(s,dict(kind='box',x=x,y=y,w=w,h=w*1280/720,fill=c,radius='50%'),'원문 simple bullet actual color/size')
# Match each source title's native ink width, not a uniform enlarged font.
target={'s02-01':(486,185),'s02-02':(464,161),'s02-03':(390,191),'s02-04':(557,466),'s02-05':(464,176),'s02-06':(322,542),'s02-07':(247,180),'s02-08':(469,173),'s02-09':(298,159),'s03-01':(432,161),'s03-02':(384,182),'s03-03':(462,162),'s03-04':(665,187),'s03-05':(318,175),'s03-06':(268,500),'s03-07':(986,287),'s03-08':(324,490),'s03-09':(469,173)}
for s,(width,top)in target.items():
 i=next(i for i,e in enumerate(es(s))if e.get('size',0)>35 and e.get('text','')[0]not in '0123456789$');e=es(s)[i];first=e['text'].split('\n')[0];sz=width/fm[first]*100
 y=(top-sz*.24)/7.2;lh=1.15
 if s=='s03-06':lh=1.02
 if s=='s03-07':lh=1.45
 if s=='s03-08':lh=1.25
 up(s,i,'개별 source native 첫행 ink폭과 실제 rounded glyph(a/g)을 Quicksand600으로 대응, 실제 font load. 비례 글씨 늘림 없음',font='Quicksand',size=round(sz,2),weight=600,y=round(y,2),lineHeight=lh,h=min(100-y,sz*lh*len(e['text'].split('\n'))/7.2+3))
 q['pages']['p073/'+s]['measurements'].append(dict(role='primary-title',targetInkWidthPx=width,targetInkTopPx=top,actualCanvasAt100Px=fm[first],fontSizePx=round(sz,2),font='Quicksand',weight=600))
for k,p in d.items():
 if not k.startswith('p073/'):continue
 s=k.split('/')[1]
 for i,e in enumerate(p['elements']):
  if e.get('text')=='Profit growth' and e['kind']=='text':
   up(s,i,'원문 upper brand caption dark muted, orange bullet 별개',color='#f4f4f4'if s in ['s02-04','s02-06','s03-03','s02-07']else'#777',font='Quicksand',size=15,weight=500)
   if s not in ['s03-06','s03-08']:dot(s,e['x']-1.8,e['y']+.9)
  if e['kind']=='chip'and e.get('size',0)<=11:up(s,i,'원문 작은 chip 글씨 가독 native11px, 실제 Quicksand500',font='Quicksand',size=11.5,weight=500)
  if e['kind']=='box'and e.get('fill')=='#fff'and e.get('radius')==12:up(s,i,'원문 raised whitecard shadow 실제 표면',border='1px solid #f4f4f4',shadow='0 4px 12px #00000009')
 q['pages'][k]['remaining'].append({'reason':'인물 사진/건물 사진/기기 화면은 사용자 범위상 회색만 유지. 단순 곡선·paper 모서리·cycle arrow는 SVG로 구현. 판독불가 본문은 각 페이지의 실제 행 밀도에 맞춘 정상 문구, 주제목 Quicksand 실제 로드.'})
# Geometry: source each bar has independent segment widths and badge positions.
for i,vals in enumerate([(19.5,17.4),(37.6,7.6),(46,15.5),(19.5,41.9),(62.1,11.8),(74.6,12.7),(19.5,33.2),(53.4,13.6),(67.7,10.4),(19.5,23),(43.2,5.8),(49.7,17.5)]):up('s02-01',i,'각 source segmentedbar 실제 픽셀 좌표/길이',x=vals[0],w=vals[1])
for i,x,c in [(16,52,'#cfcfcf'),(18,78,'#eb812e'),(20,74,'#303030'),(22,58,'#cfcfcf')]:
 up('s02-01',i,'원문 작은 badge 실제 위치 및 dot 옆 text',x=x,size=16,w=9,h=5.5)
 dot('s02-01',x+1,es('s02-01')[i]['y']+2.1,c,w=.85)
for i in [15,23]:
 if i==15:up('s02-01',i,'원문 Revenue muted',color='#999')
up('s02-01',21,'원문 Return muted',color='#999')
for s in ['s02-02','s02-05']:
 i=4 if s=='s02-02'else 3;up(s,i,'원문금액actualfont600',font='Quicksand',weight=600)
 if s=='s02-02':up(s,5,'원문 Investment pill width약100native',w=8,size=11.5)
 i=12 if s=='s02-02'else 6;up(s,i,'원문 두 bullets 서로 독립',text='Increase profit margins        Reduce operational costs',size=12.5)
 dot(s,7.5 if s=='s02-02'else 46.5,es(s)[i]['y']+.9);dot(s,26 if s=='s02-02'else 66,es(s)[i]['y']+.9)
 if s=='s02-02':dot(s,7.5,79.9)
up('s02-03',17,'원문 left paragraph3행 density',text='Profit growth refers to the increase in a company’s net profit over\na specific period, reflecting improved financial performance and\nbusiness efficiency.',size=15.5,h=10,lineHeight=1.2)
up('s02-03',11,'원문 Investment 실제 작은 pill',w=7.7)
for i,x,y,c in [(20,55,23,'#cfcfcf'),(21,81,45,'#cfcfcf'),(22,41,61,'#eb812e'),(16,74,81,'#303030')]:dot('s02-03',x,y,c,w=.8)
up('s02-04',0,'원문 native title starts lower source66%',y=65.5,h=32,w=66,x=28)
up('s02-04',4,'원문 upper body3행',text='A short pause brings fresh ideas and thoughtful direction.\nTake a moment to reflect, gather your thoughts, and prepare\nto continue our presentation with renewed focus.',size=15.5,h=10)
up('s02-04',3,'원문 source brandlogo baseline lower',y=53)
up('s02-06',6,'원문95.2K actual roundedfontbold',font='Quicksand',weight=600,size=75)
up('s02-06',7,'원문 right paragraph RIGHT3행',text='Profit growth improves financial performance\nand supports consistent planning for future\nbusiness decisions.',align='right',font='Quicksand',size=15.5,h=10,x=56,w=34)
up('s02-06',16,'원문 FutureStrategies amount',text='$13.230',size=18)
up('s02-06',17,'원문 StrategicInvestment amount',text='$15.230',size=18)
up('s02-06',12,'원문 PerformanceAnalysis amount',text='$12.230',size=18)
for i in [16,17,12]:dot('s02-06',es('s02-06')[i]['x']-1.6,es('s02-06')[i]['y']+1.0,w=.75)
# original orange circle under right inline icon.
add('s02-06',dict(kind='box',x=87,y=16,w=4.6,h=8.18,fill='#eb812e',radius='50%'),'원문 source orange simple round icon badge')
for e in es('s02-06'):
 if e['kind']=='icon'and e.get('x',0)>85:e.update(x=88,y=17.5,w=2.6,h=4.6,color='#fff')
up('s02-07',12,'원문 Mission paragraph2행',text='A clear mission supports focused action\nand stronger business performance.',size=15.5,h=7)
up('s02-07',14,'원문 leftchip 작은 nativewidth127',w=10,size=15)
for s in ['s02-08','s03-09']:
 up(s,5,'원문 Investment chip width약100native',w=7.7,size=12)
 up(s,11,'원문 left body3행 density',text='Profit growth strengthens business performance,\nhelps teams plan their next steps, and supports\nthoughtful decisions for a stronger future.',size=15.5,h=10,lineHeight=1.2)
up('s02-09',19,'원문 right body RIGHT3행',align='right',text='Profit growth helps teams understand their\nperformance and plan for the future with\nclear goals and thoughtful decisions.',size=15.5,h=10)
for i in [9,11,13]:up('s02-09',i,'원문 contactcaption600',weight=600,size=19,font='Quicksand')
for i in [8,9,10,11,12,13,14,15]:up('s03-01',i,'원문 TOC actual roundedfont600',font='Quicksand',weight=600)
for i in [4,5]:up('s03-02',i,'원문 names actual bold600 size34',font='Quicksand',weight=600,size=34)
up('s03-02',10,'원문 secondchip Investment',text='Investment')
up('s03-03',6,'원문금액 실제 Quicksand600',font='Quicksand',weight=600,size=68)
up('s03-03',7,'원문15% ysource19%',y=19,weight=600,font='Quicksand')
up('s03-03',8,'원문39% ysource59%',y=59,weight=600,font='Quicksand')
up('s03-04',4,'원문금액600 actual width',font='Quicksand',weight=600,size=52)
up('s03-04',5,'원문 3행 density',text='Profit growth refers to the increase in a company’s net profit\nover a specific period, reflecting improved financial\nperformance and business efficiency.',size=15.5,h=10,lineHeight=1.2)
up('s03-05',7,'원문 number 다음 문구 gap약20native',y=73,h=7,size=15.5)
up('s03-05',4,'원문70% actual y26%',y=26,weight=600,font='Quicksand')
up('s03-05',3,'원문95.2K bold actualfont',font='Quicksand',weight=600,size=63.2)
up('s03-06',2,'원문95.2K bold600 rounded',font='Quicksand',weight=600,y=17)
up('s03-06',6,'원문 first lowerchip Profitability',text='Profitability',x=73,fill='#f2f2f2',color='#777')
add('s03-06',dict(kind='chip',x=84,y=72,w=8,h=4,text='Investment',size=11.5,font='Quicksand',weight=500,fill='#eb812e',color='#fff',radius=30),'원문 orange Investment actual chip 복원')
up('s03-08',2,'원문95.2K bold600 actualfont',font='Quicksand',weight=600)
up('s03-08',3,'원문 right-aligned 3행 normalcopy',text='Profit growth supports informed decisions,\nstronger business performance and thoughtful\nplanning for the future.',align='right',size=15.5,h=10)
add('s03-08',dict(kind='chip',x=29,y=41,w=8,h=4,text='Profit growth',size=11.5,font='Quicksand',weight=500,fill='#eb812e',color='#fff',radius=30),'원문 3개chip 중 누락된 ProfitGrowth 복원')
# Replace source simple circular cycle with explicit semantic SVG arrows; keep photo disk separate.
s='s02-03';old=es(s)[:3];es(s)[:3]=[dict(kind='graphic',graphic='b-profit-cycle',x=50.5,y=20.5,w=35,h=62.2)];q['pages']['p073/'+s]['changes'].append({'removed':old,'reason':'원문3색 cyclearrow 실제 outer/inner annular arc+arrowhead 수작업SVG, 회색sector tone 복원'})
for k,p in d.items():
 if not k.startswith('p073/'):continue
 s=k.split('/')[1]
 if s in ['s02-04','s02-06']:
  p['elements'].insert(0,dict(kind='graphic',graphic='b-profit-curves',variant='rings'if s=='s02-06'else'plain',x=0,y=0,w=100,h=100));q['pages'][k]['changes'].append({'reason':'원문 단순 darkgradient+4동심원 원문대로 SVG, graphic배경 gray placeholder제외'})
 elif s not in ['s03-03','s03-07']:
  p['background']='#ededed';p['elements'].insert(0,dict(kind='graphic',graphic='b-profit-paper',x=0,y=0,w=100,h=100));q['pages'][k]['changes'].append({'reason':'원문 whitepaper 둥근모서리·아주 옅은 그림자 실제 SVG surface'})
for path,data in [(P,d),('review/quality/group-b.json',q)]:
 with open(path+'.tmp','w')as f:json.dump(data,f,ensure_ascii=False,indent=2)
 os.replace(path+'.tmp',path)
print('p073 modified18')
