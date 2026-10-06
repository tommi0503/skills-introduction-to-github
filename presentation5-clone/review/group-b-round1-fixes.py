from pathlib import Path
import json,math
ROOT=Path(__file__).resolve().parents[1]
# Reuse semantic primitive factories without reexecuting the preparation pipeline.
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
data=json.loads((ROOT/'src/decks/group-b-data.json').read_text())
BLACK='#080909';RED='#ed0015'
for n in range(1,17):
 key=f'p050/s02-{n:02}';s=data[key];texts=[e for e in s['elements'] if e['kind'] in ['text','chip']];s['background']=RED if n in [2,3,8,13,16] else BLACK;g=[]
 for e in texts:
  if e.get('font')=='Bebas Neue' and e.get('size',0)>70:e['size']*=1.23
 if n==1:g=[photo(54,0,46,50),box(54,50,46,50,RED)];texts += [tx('Movies That Changed the World',58,57,40,27,'Bebas Neue',color='#fff'),para(58,64,38,19,'#fff',2),tx('— 1990’S',58,74,18,39,'Bebas Neue',color='#fff'),para(73,74,24,17,'#fff',2),tx('— 2022’S',58,86,18,39,'Bebas Neue',color='#fff'),para(73,86,24,17,'#fff',2)]
 if n==2:g=[{**photo(66,0,26,94),'radius':30,'border':'3px solid #111'}];g+=[ic(48,57,11,19,'CircleArrowRight','#fff',1)];
 if n==3:g=[photo(57,0,43,100),ic(5,65,8,14,'CircleArrowRight','#fff',1)]
 if n==4:
  g=[photo(0,0,100,33)];texts=[title('INTRODUCTION TO FILM',5,35,92,123,'Bebas Neue',color=RED),tx('COMINGSOON',5,77,39,68,'Bebas Neue',color='#fff'),tx('A FILM MASTERPIECE INSPIRED BY VARIOUS CORNERS OF LIFE',5,91,88,27,'Bebas Neue',color='#fff'),para(49,62,45,22,'#fff',6)]
 if n==5:
  g=[photo(46,0,54,82),box(46,82,54,18,RED)];texts=[title('OUR CREATIVE TEAM',3,5,40,93,'Bebas Neue',color=RED),tx('ALBERTO GOTZE',49,89,25,51,'Bebas Neue',color='#fff'),tx('MARIANA LUIS',76,89,23,51,'Bebas Neue',color='#fff')]
 if n==6:g=[photo(0,0,100,100),ic(5,5,7,13,'CircleArrowRight','#fff',1)];texts += [tx('@2025 FILM INTRO',75,7,21,28,'Bebas Neue',color='#fff')]
 if n==7:
  g=[box(5,57,36,12,RED),box(41,57,54,12,'#fff')];texts=[e for e in texts if e.get('text') not in ['40,5%','59,5%']]+[title('40,5',5,33,31,178),title('%',34,42,11,109,color=RED),title('59,5',59,33,31,178,color='#fff'),title('%',88,42,10,109,color='#fff')];texts[-4]['color']=RED
 if n==8:
  g=[box(0,46,38,54,BLACK),ic(5,5,7,13,'CircleArrowRight','#fff',1)];texts=[]
  texts += [title('THE ART OF\nCINEMA',24,7,72,121,'Bebas Neue',color='#fff',align='right')]
  for i,v in enumerate([55,65,75]):texts += [tx(f'{v}%',3,50+i*18,13,53,'Bebas Neue',color='#fff'),para(12,52+i*18,23,19,'#fff',2)];g += [path([[2,63+i*18],[34,63+i*18]],'#aaa',1)]
 if n==9:g=[photo(0,0,60,91),box(60,0,40,8,RED)];texts += [tx('VISUAL STORYTELLING',64,11,31,24,'Bebas Neue',color='#fff',align='right'),para(61,19,34,23,'#fff',5)]
 if n==10:g=[box(0,33,23,67,RED),box(23,68,24,32,'#fff'),box(47,89,23,11,RED),ic(89,80,7,13,'CircleArrowRight','#fff',1)];texts += [para(54,43,41,21,'#fff',2)]
 if n==11:
  for y in range(32,91,6):g += [path([[5,y],[49,y]],'#424242',1)]
  points=[[9,83],[17,77],[24,66],[32,73],[40,60],[48,40]];g+=[path(points,'#fff',2),ic(5,7,7,13,'CircleArrowRight','#fff',1)]
  for i,(x,y) in enumerate(points):g += [box(x-.5,y-.88,1,1.77,RED,'50%')];texts += [tx(str(2020+i),x-3,91,7,19,'Bebas Neue',color='#fff',align='center')]
 if n==12:g=[ic(5,79,5,9,'CircleArrowRight','#fff',1)];texts += [tx('GLOBAL PERSPECTIVES ON FILM PRODUCTION AND DISTRIBUTION',5,86,90,23,'Bebas Neue',color='#fff'),para(5,93,90,17,'#fff',2)]
 if n==13:g=[photo(0,50,40,50)];texts += [title('1000+',78,77,22,96,'Bebas Neue',color='#fff')]
 if n==14:
  g=[path([[10,78],[91,78]],'#fff',1),path([[10,89],[91,89]],'#fff',1)]
  for i in range(5):g += [box(17+i*16,76.8,1.2,2.1,RED if i==1 else '#fff','50%')]
 if n==15:g=[path([[50,28],[50,96]],'#fff',1)];texts += [para(6,88,39,18,'#fff',2),para(55,88,39,18,'#fff',2)]
 if n==16:g=[photo(0,0,16,100)]
 s['elements']=g+texts
# CreativeStep nine distinct pages were missing large text in the initial browser render.
titles=['Building a Strong\nBrand Identity','Effective Marketing\nand Customer\nEngagement','Identifying Key Business Challenges','Achieving\nSustainable\nSuccess','The Path to\nCreative Business\nGrowth','Developing a\nUnique Value\nProposition','Developing a Unique\nValue Proposition','Building a\nStrong Brand\nIdentity','Thank You For\nWatching']
COL=['#7365ef','#bc61ce','#f4b900','#303030']
for n,text in enumerate(titles,1):
 s=data[f'p064/s04-{n:02}'];s['background']='#fff';g=[];arr=[tx('Creative Step Business',3,4,42,14,color='#ac86c8'),tx('www.yourwebsite.com',3,94,40,12,color='#aaa')]
 if n==1:g=[photo(35,42,65,44),ic(7,45,6,10,'Target')];arr += [title(text,7,17,85,69,weight=700),tx('Your Subtitle Here',7,62,31,23,weight=700),para(7,69,27,20,lines=3),chip('Learn More',7,80,15,6,17,COL[1],'#fff',radius=30),para(63,18,31,18,lines=4),chip('What Explains the Journey of Progress',61,38,34,6,17,'#fff',COL[1],radius=30)]
 if n==2:g=[photo(0,10,47,90),box(47,0,53,52,COL[0])];arr += [title(text,51,17,47,64,weight=700,color='#fff')]
 if n==3:
  arr += [title(text,14,13,83,55,weight=600)]
  for i in range(4):g += [box(17+i*18,27,10,18,COL[i],'50%'),ic(18+i*18,29,8,14,['Target','Coins','HandCoins','ChartNoAxesCombined'][i],'#fff'),path([[22+i*18,45],[22+i*18,61]],'#bbb',1),path([[12+i*18,59],[28+i*18,59],[31+i*18,63],[28+i*18,67],[12+i*18,67],[15+i*18,63]],COL[i],0,COL[i])];arr += [tx(['Step One','Step Two','Step Three','Step Four'][i],12+i*18,75,18,21,weight=600,color=COL[i]),para(12+i*18,83,18,17,lines=3)]
 if n==4:
  g += [photo(7,39,24,59)];arr += [title(text,70,12,29,74,weight=700)]
  for i in range(4):x=15+i*10;y=18+i*20;g += [path([[x,y],[x+19,y],[x+25,y+10],[x+19,y+20],[x,y+20],[x-5,y+10]],COL[i],0,COL[i])];arr += [tx(f'0{i+1}  Step Here',x,y+7,22,20,color='#fff'),para(x+26,y+4,24,17,lines=3)]
 if n==5:
  arr += [title(text,6,15,52,68,weight=700)]
  for i in range(4):x=32+i*13;y=83-i*17;g += [box(x,y,13,17,COL[i]),path([[x,y],[x+13,y],[x+11,y-4],[x-2,y-4]],COL[i],0,COL[i]),ic(x+3,y+2,7,11,['Target','Coins','HandCoins','ChartNoAxesCombined'][i],'#fff')];arr += [tx('Your Step '+['One','Two','Three','Four'][i],x-23,y-7,22,18,color=COL[i],align='right'),para(x-23,y-2,22,15,lines=2)]
 if n==6:
  arr += [title(text,7,50,48,70,weight=700)]
  for pts,c in [([[26,-5],[26,16],[33,22],[44,22],[44,31]],COL[0]),([[44,28],[44,49],[50,54],[59,54],[59,62]],COL[1]),([[59,61],[59,79],[67,87],[79,87],[79,103]],COL[2])]:g += [{**path(pts,c,74),'curved':True,'lineCap':'round'}]
  for i in range(3):arr += [tx('Step '+['One','Two','Three'][i],55+i*13,17+i*31,27,23,weight=600,color=COL[i]),para(55+i*13,25+i*31,23,17,lines=3)]
 if n==7:
  arr += [title(text,7,15,88,67,weight=700)];g += [photo(3,43,17,55),ic(85,21,10,18,'Trophy','#dfae00')]
  for i in range(4):x=18+i*17;y=92-i*14;g += [path([[x,y],[x+14,y],[x+14,y-14],[x+18,y-14]],COL[i],12),box(x+5,y-20,6,10.6,COL[i],'50%'),ic(x+6,y-19,4,7,['Target','Coins','HandCoins','ChartNoAxesCombined'][i],'#fff')];arr += [tx('Step '+['One','Two','Three','Four'][i],x,y-32,17,18,color=COL[i]),para(x,y-27,17,14,lines=2)]
 if n==8:
  g += [photo(27,10,73,47),box(6,24,27,29,'#fff')];arr += [title(text,9,29,26,63,weight=700)]
  for i in range(3):g += [box(8+i*31,65,5,9,COL[1])];arr += [tx(f'0{i+1}',8+i*31,66,5,18,color='#fff',align='center'),tx('Your Project Here',15+i*31,67,25,21,weight=600),para(8+i*31,80,27,17,lines=3)]
 if n==9:arr += [title(text,12,48,86,106,weight=700),para(62,17,33,18,lines=3)]
 s['elements']=g+arr
# Restore the actual Portfolio's neutral split panels and fine grid rules.
for key,s in data.items():
 if not key.startswith('p080'):continue
 sid=key.split('/')[1];pv=int(sid[1:3]);n=int(sid[-2:]);photos=[e for e in s['elements'] if e['kind']=='image'];texts=[e for e in s['elements'] if e['kind'] in ['text','chip','icon']];g=[];s['background']='#383838'
 for e in texts:
  if e.get('font')=='Michroma':e['size']*=.73
  if e.get('text')=='Services' and pv==2 and n==1:pass
 if pv==2 and n==1:g+=[box(44,17,56,83,'#665944'),path([[72,17],[72,100]],'#918370',1),path([[44,59],[100,59]],'#918370',1)];texts=[e for e in texts if not(e.get('text','').startswith('SELECTEDWORK') or e.get('font')=='Kaushan Script' or e.get('size',0)<17 and e.get('y',0)>55)]
 if pv==2 and n==2:g += [path([[52,8],[52,100]],'#666',1),path([[0,37],[52,37]],'#666',1),path([[52,49],[100,49]],'#666',1)]
 if pv==2 and n==4:g += [path([[59,24],[99,24]],'#777',1)]
 if pv==2 and n==6:
  g+=[box(0,8,40,92,'#665944')]
  for e in texts:
   if e.get('text')=='Contact':e.update(x=43,y=27,w=55,size=103)
 if pv==3 and n==1:g+=[box(43,48,57,52,'#fff')]
 if pv==3 and n==3:g+=[path([[46,8],[46,100]],'#777',1),path([[64,8],[64,100]],'#777',1),path([[82,8],[82,100]],'#777',1)]
 if pv==3 and n==6:
  g += [path([[56,8],[56,100]],'#777',1)]
  for y in [35,58,81]:g += [path([[56,y],[100,y]],'#777',1)]
 if pv==3 and n==7:g += [box(0,8,53,92,'#665944')]
 if pv==3 and n==8:g += [box(0,37,33,63,'#665944')]
 if pv==3 and n==9:g += [box(63,8,37,92,'#665944')]
 if pv==6 and n==1:g += [box(0,8,40,92,'#665944')]
 if pv==6 and n==2:g += [box(40,8,60,92,'#f1f1f1')]
 if pv==6 and n==3:g += [box(56,8,44,92,'#665944')]
 if pv==6 and n==8:g += [box(50,8,50,92,'#665944')]
 if pv==6 and n==9:g += [box(66,41,34,59,'#fff')]
 g += [box(0,0,100,8,'#fff')]
 if pv in [6,8] and n in [1,2]:
  for e in photos:e['clipPath']='ellipse(47% 50% at 50% 50%)'
 s['elements']=g+photos+texts
for dst,src in [('s08-01','s06-01'),('s08-02','s03-02'),('s08-03','s03-03'),('s08-04','s02-03')]:data['p080/'+dst]['elements']=json.loads(json.dumps(data['p080/'+src]['elements']))
# Minimal: match actual small type size and vertical sidebar writing.
for key,s in data.items():
 if not key.startswith('p081'):continue
 for e in s['elements']:
  if e['kind']=='text':
   if e.get('size',0)>=39 and e.get('text')!='MINI' and not(e.get('text')=='Thank You\nFor\nWatching'):e['size']*=.76
   if e.get('text') in ['Design','Minimal']:e.update(rotate=-90,x=3,y=42 if e['text']=='Design' else 85,w=19,h=4)
 s['elements']=[path([[5,0],[5,92]],'#e2e1dc',1)]+s['elements']
# Correct initial letterbox padding artefacts for incomplete reference cells.
manifest=json.loads((ROOT/'public/reference/groups/b.json').read_text())
for d in manifest:
 if d['id'] in EXTRA:continue
 for ref in d['slides']:
  if not ref.get('incomplete'):continue
  s=data[d['id']+'/'+ref['id']];x,y,w,h=ref['crop'];l,t,vw,vh=ref['visibleCrop'];left=(l-x)/w*100;top=(t-y)/h*100;right=left+vw/w*100;bottom=top+vh/h*100
  s['elements']=[e for e in s['elements'] if not(e['kind']=='box' and e.get('fill') in ['#ffffff','#fff'] and (e['x']+e['w']<=left+.2 or e['y']+e['h']<=top+.2 or e['x']>=right-.2 or e['y']>=bottom-.2))]
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(data,ensure_ascii=False))
print('first visual corrections written',len(data))
