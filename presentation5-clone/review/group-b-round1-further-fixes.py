from pathlib import Path
import json,math,copy
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
data=json.loads((ROOT/'src/decks/group-b-data.json').read_text())
G='#acd82d';O='#eb812e';W='#fff';K='#303030'
def add(d,s,els):data[d+'/'+s]['elements']+=els
def rule(x,y,w,c='#aaa'):return path([[x,y],[x+w,y]],c,1)
def button(x,y,w=9):return {**chip('Learn More',x,y,w,4.6,13,W,radius=30),'border':'1px solid #777'}
def rounded(e,r=30):return {**e,'radius':r}
# Individual source review: retain clean annular geometry and the original statistic labels.
for key,s in data.items():
 if key.startswith('p069'):
  for e in s['elements']:
   if e['kind']=='image':e['radius']=32
   if e['kind']=='text' and 45<e.get('size',0)<95:e['size']*=.89
  s['elements']=[e for e in s['elements'] if not(e['kind']=='box' and e.get('fill') in ['#e2efbb','#e6f3cf','#e8f3d4','#e8f6cd'])]
add('p069','s01-03',[{**box(30,13,22.5,36,W,30),'border':'2px solid #aaa'},tx('3758+',32,16,20,62),tx('High-level benefits',32,32,20,22),para(32,38,18,16,lines=3),tx('Community\nEngagement',71,44,20,23),tx('Influencer\nMarketing',71,69,20,23),rule(56,55,32),rule(56,80,32),para(57,59,31,16,lines=2),para(57,84,31,16,lines=2)])
add('p069','s01-04',[tx('Framing the Problem',10,15,39,27,color=W)])
add('p069','s01-06',[para(20,36,60,16,lines=2),tx('Key\nChallenges A',82,57,14,21),tx('Key\nChallenges B',82,80,14,21),rule(53,70,39)])
add('p069','s01-07',[tx('Smart ad campaigns\nto amplify your\nmessage',77,17,20,22),rule(54,30,42),ring(-9,57,33,58,[100],[G],.72)[0],para(65,79,31,16,W,3)])
for sid in ['s01-08']:
 s=data['p069/'+sid]
 for e in s['elements']:
  if e['kind']=='chip':e['y']=43 if e['y']<55 else 77;e['h']=4.5;e['border']='1px solid #999';e['radius']=30
 add('p069',sid,[para(50,62,40,17,lines=4)])
add('p069','s01-09',[tx('Job Position',6,77,24,16),tx('Job Position',33,29,22,16),tx('Team\nWork\nExperience',74,49,18,22),para(60,64,33,17,lines=3),button(60,77)])
add('p069','s02-01',[tx('Problem Statement',6,11,37,25,color=W),para(51,23,43,17,W,5),rule(5,54,80),tx('Results From\nSocial Media A',35,72,17,22,color=W),tx('Results From\nSocial Media B',80,72,16,22,color=W)])
add('p069','s02-02',[para(7,36,81,16,lines=2),tx('Value\nPositioning\nYour Brand A',28,55,14,19),tx('Value\nPositioning\nYour Brand B',28,77,14,19),para(43,55,49,16,lines=3),para(43,77,49,16,lines=3),rule(5,68,95)])
add('p069','s02-03',[para(5,51,38,17,lines=3),tx('Your\nPlatform\nPerformance',41,71,17,21)])
add('p069','s02-04',[tx('Framing the Problem\nStatement for Study\nSuccess',14,42,23,22),tx('Framing the Problem\nStatement for Study\nSuccess',14,59,23,22),tx('Framing the Problem\nStatement for Study\nSuccess',14,76,23,22)]+sum(([rule(5,y,90),para(71,y-12,23,16,lines=3)] for y in [56,73,90]),[])+[{**box(5.5,y,5,8.9,'transparent','50%'),'border':'1px solid #777'} for y in [43,60,77]])
add('p069','s02-05',[tx('01. Brand\nConsistency',29,20,20,23),tx('02. Maximize\nAudience',29,53,20,23),para(29,30,18,16,lines=3),para(29,63,18,16,lines=3),button(29,40),button(29,73),tx('Value\nYour\nBranding',80,68,14,23)])
s=data['p069/s02-06'];add('p069','s02-06',[rule(43,63,29),tx('Problem Statement',73,62,22,21),para(59,70,30,17,lines=3)])
for e in s['elements']:
 if e['kind']=='text' and e.get('size',0)>40:e['italic']=True
add('p069','s02-07',[para(19,40,64,16,lines=3),para(74,42,21,16,lines=3),para(74,59,21,16,lines=3),para(74,75,21,16,lines=3)]+[tx('Data '+str(y),10+i*11,85,12,14) for i,y in enumerate([2022,2023,2024,2025])])
add('p069','s02-08',[tx('Budget Breakdown',31,64,20,22),para(21,71,29,17,lines=3)]+sum(([tx('Budget\nPlanning '+chr(65+i),81,22+i*28,15,21),rule(53,34+i*28,39)] for i in range(3)),[]))
add('p069','s02-09',[para(20,30,61,16,lines=3)])
add('p069','s04-06',[tx('70%   Performance',6,59,22,17),tx('62%   Performance',6,84,22,17),rule(21,60,18),rule(21,85,18),button(40,58),button(40,83)])
# Duplicate visible reference cells remain distinct pages, sharing the same corrected data.
for target,source in [('s03-02','s01-02'),('s03-03','s01-03'),('s03-04','s01-06'),('s04-01','s01-05'),('s04-02','s01-04'),('s04-03','s01-08'),('s04-04','s01-07'),('s04-05','s01-09')]:data['p069/'+target]=copy.deepcopy(data['p069/'+source])
# Profittera: compact rounded typography and explicitly authored progress charts/cards.
for key,s in data.items():
 if not key.startswith('p073'):continue
 sid=key.split('/')[1];texts=[e for e in s['elements'] if e['kind'] in ['text','chip']];g=[];s['background']='#fcfcfc'
 for e in texts:
  if e.get('size',0)>39:e['size']*=.80
  if e['kind']=='chip':e['h']=4;e['radius']=30
  if e.get('text')=='Profit growth':e['y']+=3
  if e['kind']=='text' and 'Industry Trends' in e.get('text',''):e['y']+=2
 dark=sid in ['s02-04','s02-06','s03-03','s03-07']
 if dark:s['background']=K
 texts += [tx('PROFITTERA GLOBAL',83,6,14,11,color=W if dark else '#333'),box(86,6.8,.65,1.15,O,'50%')]
 def tags(x,y,n=4):return [chip(z,x+i*9,y,8,4,11,'#f8f8f8','#555',radius=20) for i,z in enumerate(['Profit growth','Revenue','Profitability','Productivity'][:n])]
 if sid=='s02-01':
  texts += [para(54,21,35,16,lines=3)]
  for i,(name,value,col) in enumerate([('Revenue',47,'#f1f1f1'),('Profit',77,O),('Annual',72,K),('Return',52,'#f1f1f1')]):
   y=41+i*13;g += [box(19,y,value*.55,9,col,14),box(20+value*.55,y,13,9,col if i not in [1,2] else '#f5d7c6' if i==1 else '#999',14),box(34+value*.55,y,9,9,'#eee',14)];texts += [tx(name,8,y+3,10,17,weight=600),chip(str(value)+'%',35+value*.55,y+1.5,9,6,17,W,'#333',weight=600,radius=25)]
 if sid=='s02-02':
  g=[rounded(photo(50,-15,22,72),32),rounded(photo(78,43,20,65),32)];texts += tags(8,42)+[tx('Profit growth drives informed business decisions',8,79,39,15),tx('Increase profit margins     •     Reduce operational costs',8,85,42,14)]
 if sid=='s02-03':
  g=ring(51,20,32,57,[35,25,20,20],[O,K,'#eee','#ddd'],.73)+[rounded(photo(59,35,16,28),300)]
  texts=[e for e in texts if e.get('text')!='.130']+[tx('$25.130',7,64,27,58),chip('Investment',28,67,9,4,11,O,W,radius=20),para(7,77,39,16,lines=3)]
  for x,y,label in [(53,16,'Customer Retention'),(79,38,'Cost Efficiency'),(39,54,'Strategic Investment'),(72,74,'Product Innovation')]:g += [box(x,y,16,11,W,12)];texts += [tx(label,x+1,y+2,15,13,weight=600),tx('$13.230',x+2,y+6,14,14)]
 if sid=='s02-04':
  texts=[e for e in texts if e.get('text')!='Profit growth'];texts += [chip('MINUTES',23,24,10,5,15,O,W,radius=30),tx('PROFITTERA GLOBAL',73,50,24,22,color=W)]
  for e in texts:
   if e.get('text','').startswith('A Short Break'):e['x']=30;e['y']=62;e['w']=63;e['size']=76;e['align']='right';e['runs']=[{'text':'A ','color':W},{'text':'Short Break','color':O},{'text':'\nBefore We Continue','color':W}]
 if sid=='s02-05':g=[photo(9,10,31,78)];texts += [para(47,70,44,16,lines=2),tx('Increase profit margins     •     Reduce operational costs',47,82,45,15)]
 if sid=='s02-06':
  for x,y,label in [(13,13,'Future Strategies'),(25,39,'Strategic Investment'),(8,66,'Performance Analysis')]:
   g += [box(x,y,27,16,W,15),rounded(photo(x+2,y+3,6,10.6),300)];texts += [tx(label,x+10,y+4,16,15,weight=600),tx('$13.230',x+10,y+9,15,17)]
  texts += tags(69,45,3)
 if sid=='s02-07':
  g=[photo(0,0,39,100),box(70,0,30,100,'#f4f4f4')];texts += [chip('Profit growth',7,73,13,5,17,O,W,radius=30),para(7,83,25,15,W,2),para(48,33,15,16,lines=2),para(78,33,16,16,lines=2)]
  for x,icon in [(44,'Users'),(74,'Target')]:g += [box(x,63,4,7,O if x==74 else K,'50%'),ic(x+1,64,2,3.6,icon,W)]
 if sid in ['s02-08','s03-09']:
  g=[rounded(photo(0,0,44,54),27),rounded(photo(60,64,40,36),27)];texts=[e for e in texts if not(e.get('text','').startswith('Lorem ipsum'))]
  for e in texts:
   if e.get('text')=='$25,130':e['x']=7;e['y']=65;e['w']=30;e['size']=63
   if e['kind']=='chip':e['x']=29;e['y']=69;e['w']=9
  texts += tags(51,42)+[para(7,78,43,16,lines=3)]
 if sid=='s02-09':
  g=[rounded(photo(53,0,47,50),27)];texts += tags(8,39,3)+[para(64,59,28,16,lines=3)]
  texts=[e for e in texts if e['kind']!='icon']
  for i,icon in enumerate(['Phone','Mail','Globe']):g += [box(7+i*21,67,4,7,O if i==0 else K,'50%'),ic(8+i*21,68,2,3.6,icon,W)]
 if sid=='s03-01':
  g=[rounded(photo(50,10,41,33),27)]
  for x,y,num,label in [(7,55,'01','Profit Growth Overview'),(54,55,'03','Performance Analysis'),(7,75,'02','Key Growth Drivers'),(54,75,'04','Future Business Strategies')]:g += [box(x,y,38,13,W,12)];texts += [tx(num,x+2,y+3,6,34,color=O),tx(label,x+9,y+4,28,23)]
  texts=[e for e in texts if not(e.get('text') in ['01','02','03','04'] and e.get('size',0)<34)];texts += [para(7,35,36,16,lines=2)]
 if sid=='s03-02':g=[rounded(photo(45,14,18,31),18),rounded(photo(45,53,18,31),18)];texts += tags(8,65,2)
 if sid=='s03-03':
  texts += [para(7,77,38,16,W,2),para(66,30,23,16,W,3),para(66,73,23,16,W,3)]
  for x,y,col,icon in [(57,18,W,'Users'),(57,61,O,'TrendingUp')]:g += [box(x,y,6,10.6,col,'50%'),ic(x+1.5,y+2.6,3,5.3,icon,O if col==W else W)]
 if sid=='s03-04':g=[photo(74,17,26,83),photo(0,60,26,40)];texts += tags(8,43)+[box(30,65,4.5,8,O,'50%'),ic(31,67,2.5,4.4,'Users',W)]
 if sid=='s03-05':g=[photo(41,0,30,100)];texts += [para(7,70,31,16,lines=2),para(77,36,17,16,lines=3),para(77,76,17,16,lines=3)]+tags(8,81,3)
 if sid=='s03-06':g=[rounded(photo(44,0,56,65),32)];texts += [para(64,80,29,16,lines=2)]+tags(74,72,2)
 if sid=='s03-07':
  texts=[e for e in texts if e.get('text')!='Profit growth'];texts += [tx('Driving efficiency and long-term success',25,26,53,24,color=W,align='center'),tx('www.yourwebsite.com',31,87,38,23,color=O,align='center')]
  for e in texts:
   if e.get('size',0)>35:e['x']=10;e['y']=38;e['w']=80;e['align']='center';e['text']='Profit growth reflects strategy, efficiency,\nand long-term business success\nacross industries.';e['runs']=[{'text':'Profit growth','color':O},{'text':' reflects strategy, efficiency,\nand long-term ','color':W},{'text':'business success','color':O},{'text':'\nacross industries.','color':W}]
 if sid=='s03-08':g=[rounded(photo(57,5,40,90),32)];texts += tags(29,41,3)
 s['elements']=g+texts
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(data,ensure_ascii=False))
print('p069 statistic details and p073 semantic layouts corrected')
