from pathlib import Path
import json,math
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
data=json.loads((ROOT/'src/decks/group-b-data.json').read_text());Y='#eebc1c';N='#354351';W='#fff';BG='#e5e5e5'
for key,s in data.items():
 if key.startswith('p050'):
  for e in s['elements']:
   if e['kind']=='chip' and e.get('text') in ['24','25','26','27','28']:e['h']=36
 if not key.startswith('p051'):continue
 sid=key.split('/')[1];texts=[e for e in s['elements'] if e['kind']=='text'];g=[];s['background']=N
 for e in texts:
  if e.get('size',0)>50 and e.get('text')!='QIVORA':e['size']*=.86
  if e.get('text') in ['About us','Target\nMarket','Sales\nDevelopment Plan']:
   a,b=e['text'].split(' ',1) if ' ' in e['text'] else e['text'].split('\n',1);e['runs']=[{'text':a+'\n' if '\n' in e['text'] else a+' ','color':Y},{'text':b,'color':W}]
  if e.get('text')=='Price Adjustment Plan':e['runs']=[{'text':'Price ','color':W},{'text':'Adjustment ','color':Y},{'text':'Plan','color':W}]
  if e.get('text')=='S.W.O.T Analysis':e['runs']=[{'text':'S.W.O.T ','color':W},{'text':'Analysis','color':Y}]
  if e.get('text')=='Business Development\nTimeline':e['runs']=[{'text':'Business ','color':W},{'text':'Development\n','color':Y},{'text':'Timeline','color':W}]
  if e.get('text')=='Project Journey Now\nand Then':e['runs']=[{'text':'Project ','color':W},{'text':'Journey Now\n','color':Y},{'text':'and Then','color':W}]
 if sid=='s01-01':g=[photo(0,0,100,100),box(0,0,11,100,'#152331')];texts += [{**tx('Infographic Presentation',4,92,60,26,color=Y),'rotate':-90}]
 if sid=='s01-02':g=[photo(47,8,47,84)];texts += [tx('20\n22',6,9,12,28,color=W),tx('PROFESSIONAL',52,15,22,23,color=W),tx('INFOGRAPHIC',77,15,22,23,color=W),tx('STATISTIC',52,83,22,23,color=W),tx('PRESENTATION',77,83,22,23,color=W)]
 if sid in ['s01-03','s05-01']:
  g=[photo(0,0,100,100)]
  for i,(vals,cols) in enumerate([([220,25,65,50],[W,BG,Y,BG]),([140,35,145,40],[W,BG,Y,BG]),([180,35,105,40],[W,BG,Y,BG]),([70,35,215,40],[W,BG,Y,BG])]):g += ring(9+i*23,55,14,25,vals,cols,.55)
 if sid in ['s01-04','s05-02']:
  g=[]
  for j in range(7):g += [path([[31,84-j*12.3],[94,84-j*12.3]],'#85909b',1)];texts += [tx(str(j),28,83-j*12.3,3,16,color=W,align='right')]
  for i,row in enumerate([[4,2,2],[3,4,2],[4,2,3],[5,2,5]]):
   for j,v in enumerate(row):g += [box(34+i*15.5+j*3.4,84-v*12.3,2.8,v*12.3,[Y,W,'#b18809'][j])]
   texts += [tx(str(2018+i),34+i*15.5,87,11,16,color=W,align='center')]
  texts += [tx('Product1  •  Product2  •  Product3',49,93,45,17,color=W),tx('20\n22',6,9,12,28,color=W)]
 if sid=='s01-05':g=[photo(0,0,100,41)]+[box(i*25,41,25,59,Y if i%2==0 else N) for i in range(4)];texts += [tx('20\n22',6,9,12,28,color=W)]
 if sid=='s01-06':
  g=[box(5.5+i*30,42,27.5,40,Y) for i in range(3)];texts += [tx('PROFESSIONAL',6,8,28,23,color=W),tx('INFOGRAPHIC',33,8,28,23,color=W),tx('STATISTIC',55,88,24,23,color=W),tx('PRESENTATION',78,88,22,23,color=W)]
 if sid=='s01-07':g=ring(8,45,25,44.4,[20,40,30,10],[Y,N,'#c59712',W],0)+ring(59,45,25,44.4,[30,20,40,10],[Y,N,'#c59712',W],0);texts += [tx('Marketing',6,38,29,24,color=W),tx('Community',56,38,29,24,color=W)]
 if sid=='s01-08':
  g=[photo(0,0,100,100)]+[box(5.5+i*23,43,20,27.5,Y,6) for i in range(4)]
  texts=[e for e in texts if not(e.get('text','').startswith('Lorem ipsum'))]
  for i,t in enumerate(['Recognize products’\nprice and hire more\nemployees','Reach more than 1M\nsales with a profit of\nmore than 2M','Optimize online sales\non own website','Dominate the creative\nindustry market']):texts += [tx(t,8+i*23,57,16,17,color='#333',leading=1.2)]
  texts += [tx('PROFESSIONAL     INFOGRAPHIC               STATISTIC     PRESENTATION',6,88,90,22,color=W)]
 if sid=='s01-09':
  pts=[[15,47],[38,64],[61,47],[84,64]];g=[{**path(pts,Y,1),'dashed':True}]
  for x,y in pts:g += [box(x-2,y-3.56,4,7.12,'transparent','50%'),{**box(x-2,y-3.56,4,7.12,'transparent','50%'),'border':'1px solid #999'},box(x-1,y-1.78,2,3.56,Y,'50%')]
  for e in texts:
   if e.get('text') in ['2018','2020']:e['y']=55
   if e.get('text') in ['2019','2021']:e['y']=72
 if sid=='s01-10':
  g=[photo(0,0,100,100),box(25,26,41,49,N)];texts=[e for e in texts if e.get('text')!='QIVORA'];texts += [{**tx('QIVORA',29,67,34,51,weight=700,color=Y),'rotate':-90}]
  for e in texts:
   if e.get('text','').startswith('123 Anywhere'):e['size']=16;e['w']=27
 s['elements']=g+texts
# Correct cover ring geometry and right aligned cover headline (both source appearances).
for sid in ['s01-01','s03-01']:
 s=data['p069/'+sid];s['elements']=[e for e in s['elements'] if not(e['kind']=='path' and e.get('fill')=='#acd82d')];s['elements']=ring(6,-17,32,57,[100],['#acd82d'],.73)+ring(-11,21,39,69,[100],['#acd82d'],.73)+s['elements']
 for e in s['elements']:
  if e.get('text')=='Problem\nStatement':e['align']='right'
# The green infographics retain clean rules, symbols and the small source text.
s=data['p069/s02-07']
for j in range(8):s['elements'].insert(0,path([[8,82-j*5],[49,82-j*5]],'#d6d6d2',1))
for vals,c in [([5,5.2,4.8,9],'#9cbd43'),([3.5,3.7,2.2,4.5],'#becf36'),([1.7,1.1,.2,1.7],'#d2d946')]:s['elements'].insert(0,path([[8+i*13.7,82-v*3.5] for i,v in enumerate(vals)],c,1.5))
s=data['p069/s02-09'];s['elements'].insert(0,path([[7,51],[91,51]],'#888',1))
for i in range(3):s['elements'] += [chip(f'0{i+1}',6+i*31,46,7,12,27,'#fff',radius='50%')]
# Missing small figures in the map remain legible above the designated gray map placeholder.
s=data['p081/s02-05']
for x,y,name in [(42,44,'America'),(80,39,'Asia'),(60,65,'Europe')]:s['elements'] += ring(x,y,8,14.2,[75,25],['#a29e91','#e1e0da'],.8)+[tx(name,x-3,y+5,14,15,align='center')]
# CreativeStep loaded font and the source purple words.
for key,s in data.items():
 if not key.startswith('p064'):continue
 for e in s['elements']:
  if e['kind']=='text' and e.get('size',0)>48:
   e['font']='Poppins';e['size']*=.90
   txt=e['text'];mark=next((w for w in ['Brand Identity','Watching','Sustainable\nSuccess','Growth','Proposition','Business Challenges'] if w in txt),None)
   if mark:
    a,b=txt.split(mark,1);e['runs']=[{'text':a},{'text':mark,'color':'#a269c6'},{'text':b}]
# Restore button heights before their painted glyphs are optically centered.
for key,s in data.items():
 for e in s['elements']:
  if e['kind']=='chip' and e.get('text')=='Learn More':e['h']=4 if key.startswith('p069') else 7 if key.startswith('p091') else e['h']
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(data,ensure_ascii=False))
print('semantic geometry and loaded typography corrections saved')
