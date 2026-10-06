from pathlib import Path
import json,math,copy
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
d=json.loads((ROOT/'src/decks/group-b-data.json').read_text());V='#7946fd';O='#ff4826';K='#070707';W='#fff';BG='#f5f6f8'
def h(t,x,y,w,size=50,c=K,align='left'):return tx(t,x,y,w,size,weight=500,color=c,align=align,leading=1.07)
def sub(x,y,w,c=K):return [tx('Subtitle here',x,y,w,23,weight=500,color=c),para(x,y+6,w,17,c,4)]
def rr(x,y,w,ht,c):return box(x,y,w,ht,c,10)
def ph(x,y,w,ht):return {**photo(x,y,w,ht),'radius':10}
def star(x,y,w,ht,c):
 pts=[]
 for i in range(32):a=math.pi*i/16;f=1 if i%2==0 else .45;pts.append([x+w/2+math.cos(a)*w/2*f,y+ht/2+math.sin(a)*ht/2*f])
 return path(pts,c,0,c)
def dot(x,y,c,size=6):return box(x,y,size,size*1.777,c,'50%')
def dotted(p,c):return {**path(p,c,1),'dashed':True}
def arrow(x,y,w,ht,c,left=False):
 pts=[[x,y+ht*.18],[x+w*.74,y+ht*.18],[x+w*.74,y],[x+w,y+ht/2],[x+w*.74,y+ht],[x+w*.74,y+ht*.82],[x,y+ht*.82]]
 if left:pts=[[x+w-(xx-x),yy] for xx,yy in pts]
 return path(pts,c,0,c)
def section(x=7,y=8,align='left'):return h('Section Infographic',x,y,86,50,align=align)
for k,s in d.items():
 if not k.startswith('p101/'):continue
 sid=k.split('/')[1];s['background']=BG;e=[];g=[]
 if sid=='s02-01':
  s['background']='#e5e5e5';e=[h('B2B Pitch',5,10,84,176,W),para(5,84,37,17,W,2)]
 elif sid in ['s02-02','s03-01']:
  e=[h('Welcome to the World of B2B\nPitching Turning Business Ideas into\nStrategic Partnerships',12,11,78,49,V,'center')];e[0]['runs']=[{'text':'Welcome to the World of B2B\n','color':V},{'text':'Pitching Turning Business Ideas','color':K},{'text':' into\nStrategic Partnerships','color':V}]
  g=[star(-8,0,20,46,'#e5e5e5'),ph(3,43,30.5,47)]
  for x,t,c in [(35,'01',V),(67,'02',O)]:g += [rr(x,43,30.5,47,c)];e += sub(x+2.5,48,25,W)+[h(t,x+15,65,15,151,W)]
 elif sid=='s02-03':
  e=[section(25,7,'center')]
  for i,y in enumerate([22,40,58,76]):c=V if i%2==0 else O;left=i%2==1;x=33 if left else 38;g += [arrow(x,y,29,16,c,left),dot(x+(20 if left else -1),y+.6,W,9),dot(x+(20.8 if left else -.2),y+2,c,7.5),ic(x+(23 if left else 2),y+5,4,7,['CalendarDays','Contact','Laptop','Store'][i],W)]
  for i,y in enumerate([26,44,62,80]):left=i%2==1;x=3 if left else 70;e += sub(x,y,26);e += [tx('Your title',42 if left else 48,y+3,17,23,weight=500,color=W,align='center')]
 elif sid=='s02-04':
  e=[section()];g += [dotted([[19,54],[85,54]],'#aaa')]
  for x,c,icon in [(14,V,'Building2'),(40,K,'Store'),(66,O,'Building')]:pts=[[x+3,44],[x+9,44],[x+12,54],[x+9,64],[x+3,64],[x,54]];g += [path(pts,c,0,c),ic(x+4,50,4,7,icon,W)]
  for x,y,c in [(33,54,V),(59,54,K),(85,54,O)]:g += [dot(x-1.5,y-2.7,c,3),dot(x-.75,y-1.3,W,1.5),dotted([[x,y],[x,36 if c==K else 73]],c),ic(x-1.5,34 if c==K else 71,3,5,'Triangle',c)];e += sub(x-13,21 if c==K else 79,26,c)
 elif sid=='s02-05':
  e=[section()]
  for i,(x,y,c,v,icon) in enumerate([(8,64,V,'45%','Aperture'),(29,54,O,'67%','CircleDollarSign'),(50,44,K,'82%','PaintRoller'),(71,34,V,'90%','Bell')]):g += [rr(x,y,22,10,c),path([[x,y],[x,y-4],[x+2,y]],c,0,c),dot(x+7,y-20,c,6),ic(x+8.5,y-17,3,5.3,icon,W),dotted([[x+10,y-9],[x+10,y]],c),path([[x+2,y+25],[x+15,y+25]],c,2)];e += [tx('Subtitle Here',x+2,y+2,18,21,weight=500,color=W,align='center'),para(x+2,y+15,19,15,lines=2),tx(v,x+16,y+23,8,22,color=c)]
 elif sid=='s02-06':
  e=[section(25,9,'center')]
  for i,(x,c,v,icon) in enumerate([(6,V,50,'Droplet'),(28,O,60,'Send'),(50,K,70,'Zap'),(72,V,80,'Moon')]):ht=4+i*3;g += [box(x,41-ht,22,ht,c),dotted([[x+11,41],[x+11,52]],c),dot(x+10,51,c,2),dot(x+10.6,52,W,.8),dot(x+8,59,c,6),ic(x+9.6,62,3,5,icon,W)];e += [tx(f'{v}%',x+7,24-i*3,14,33,color=c),tx('Subtitle Here',x+2,74,19,22,color=c,align='center'),para(x+2,81,19,15,lines=3)]
 elif sid=='s02-07':
  g=[rr(3,11,53,74,W),rr(3,11,53,7,K)];e=[h('Desember',61,12,36,52,V),h('Calendar',61,21,36,52)]+sub(61,38,34)
  for j,t in enumerate(['Su','Mo','Tu','We','Th','Fr','Sa']):e += [chip(t,5+j*7.1,12,6.5,5,22,K,W)]
  for row in range(6):
   for col in range(7):n=row*7+col;e += [chip(str(n) if 1<=n<=31 else '',5+col*7.1,21+row*10,6.5,8.7,21,V if n==1 else K if n==5 else O if n==24 else '#e3e3e3',W if n in [1,5,24] else K)]
  for y,c,w,icon in [(60,V,12,'Timer'),(70,O,18,'Mic'),(80,K,24,'Lightbulb')]:g += [dot(61,y,c,4),ic(62,y+2,2,3.5,icon,W),rr(68,y+1,25,4,'#ddd'),rr(68,y+1,w,4,c)]
 elif sid=='s02-08':
  for i,c in enumerate([K,V,W]):x=4+i*31;g += [rr(x,2,29,88,c),star(x+19,37,20,40,'#e5e5e5'),ph(x+2,77,5,8.9)];e += sub(x+2.5,7,24,W if i<2 else K)+[tx('★★★★☆',x+2.5,29,15,27,color='#e4d34b'),tx('4.7',x+16,30,6,18,color=W if i<2 else K),tx('Customer B2B Name',x+8,79,20,21,color=W if i<2 else K),tx('Vice President & Co.',x+8,84,20,13,color=W if i<2 else K)]
 elif sid=='s02-09':
  g=[ph(61,5,38,83),rr(7,45,62,35,W),star(6,49,9,29,O)];e=[h('Thank You For',6,7,56,83,V),h('Attention!!',6,22,55,83)]+sub(19,50,43)+[tx('+123 456 7890       12 New Street Name       www.YourName.com',19,73,46,15)]
 elif sid=='s03-02':
  g=[rr(1,7,48,85,W),ph(51,7,47,85),star(28,4,22,25,O)];e=[chip('Learn More',4,17,12,5,18,K,W,radius=30),h('Winning Over\nBusinesses The Power\nof a Strong B2B Pitch',4,28,45,49),para(4,78,43,17,lines=2)];e[1]['runs']=[{'text':'Winning Over\n','color':V},{'text':'Businesses The Power\n','color':K},{'text':'of a Strong B2B Pitch','color':V}]
 elif sid=='s03-03':
  g=[ph(4,56,43,44),rr(48,40,24,60,K),rr(73,25,24,75,O),star(63,49,14,40,'#e5e5e5'),star(90,40,17,40,'#e5e5e5')];e=[h('Crafting Compelling B2B\nPitches That Convert',4,7,76,49)]+sub(4,29,43)+[h('+78.1',50,44,22,66,W),h('89,88K',75,28,20,61,W),para(50,87,20,14,W),para(76,87,19,14,W)];e[0]['runs']=[{'text':'Crafting Compelling B2B\n','color':K},{'text':'Pitches That Convert','color':V}]
 elif sid=='s03-04':
  g=[rr(3,7,30.5,41,V),ph(35,7,31,41),rr(67,7,30.5,41,O),ph(3,50,30.5,42),rr(35,50,31,42,K),ph(67,50,30.5,42)]
  e=sub(5.5,13,25,W)+sub(69,13,25,W)+[h('+31M',38,54,27,65,W),para(38,66,26,15,W)]
  for x,y,icon in [(27,36,'Presentation'),(91,36,'BarChart3'),(59,80,'TrendingUp')]:g += [dot(x,y,W,4),ic(x+.9,y+1.6,2.3,4,icon,K)]
 elif sid=='s03-05':
  g=[rr(3,10,24,39,V),ph(28,10,29,39),ph(3,51,29,38),rr(33,51,24,38,K)];e=[h('Meet the Team\nThat Turns Ideas\ninto Impactful\nB2B Partnerships',61,12,37,50)]+[tx('Your Progress Here',5,14,21,20,color=W),para(5,20,20,16,W,3),h('+75%',5,36,20,61,W),tx('Your Progress Here',36,54,20,20,color=W),para(36,60,20,16,W,2),tx('★★★★☆',36,80,16,26,color='#e4d34b'),tx('4.7',51,81,5,17,color=W),chip('Learn More',84,85,12,5,18,K,W,radius=30)];e[0]['runs']=[{'text':'Meet the Team\n','color':V},{'text':'That Turns Ideas\n','color':K},{'text':'into Impactful\n','color':V},{'text':'B2B Partnerships','color':K}]
 elif sid=='s03-06':
  g=[ph(-1,21,15,68),ph(86,21,15,68),rr(14,44,47,42,K),rr(63,44,25,42,V)];e=[h('A Glimpse into the Future of\nB2B Communication Through\nOur Pitch Mockups',20,9,59,49,V,'center'),h('87%',40,47,20,115,W),tx('Subtitle Here',18,65,38,22,color=W),para(18,71,38,17,W,3),tx('Your Overview',66,51,19,22,color=W),h('+49,8K',65,56,22,58,W),tx('★★★★☆  4.3',66,68,20,22,color='#e4d34b'),para(66,76,19,15,W,2)]
 elif sid=='s03-07':
  e=[h('Performance and Progress\nAnalysis',22,6,56,50,V,'center'),tx('Revenue',28,30,24,22,weight=500),tx('Market Data',66,30,27,22),tx('Sample Text Here',66,67,27,22)];g=[rr(3,28,57,65,W),rr(64,28,33,35,W),rr(64,64,33,29,W),box(65,71,31,21,V)]
  for i in range(8):g += [path([[9,82-i*6],[58,82-i*6]],'#eee',1)];e += [tx(str(i*50),4,80-i*6,4,11,align='right')]
  for j,vals in enumerate([[100,150,175],[300,210,270],[100,120,260],[250,280,225]]):
   for i,v in enumerate(vals):g += [box(10+j*12+i*3,82-v*.10,2.6,v*.10,[V,O,K][i])]
   e += [tx(str(2020+j),11+j*12,84,9,13)]
  for i,(v,c) in enumerate([(8,V),(10,K),(8,V),(17,K)]):g += [box(69,39+i*4,v,2,c)]
  g += [path([[69,82],[76,79],[84,84],[92,80]],W,2)];e += [tx('60        83        65        104',68,78,27,15,color=W)]
 elif sid=='s03-08':
  e=[h('Performance and Progress\nAnalysis',22,6,56,50,V,'center')];g=[rr(6,28,54,61,W),rr(64,28,31,27,V),rr(64,59,31,27,O)]
  for i,v in enumerate([60,78,68,76,102,65,91]):c=[K,V,O][i%3];g += [box(12,34+i*6.5,v*.43,2.3,c)];e += [tx(str(2025-i),7,33+i*6.5,5,12)]
  e += [h('526+',67,31,25,61,W),para(67,42,25,16,W,3),h('35%',67,62,25,61,W),para(67,73,25,16,W,3)]
 s['elements']=g+e
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(d))
