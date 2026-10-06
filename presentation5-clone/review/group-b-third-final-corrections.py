"""One atomic third/final correction batch from actual individual final comparisons."""
import json, math, hashlib, copy
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
src=ROOT/'src/decks/group-b-data.json'; data=json.loads(src.read_text()); before=copy.deepcopy(data); notes={}
def els(k):return data[k]['elements']
def remove(k,p):data[k]['elements']=[e for e in els(k) if not p(e)]
def add(k,*e):els(k).extend(e)
def under(k,*e):data[k]['elements']=list(e)+els(k)
def edit(k,p,**kw):
 for e in els(k):
  if p(e):e.update(kw)
def text(k,val,**kw):edit(k,lambda e:e.get('text')==val and e['kind']=='text',**kw)
def explain(k,s):notes.setdefault(k,[]).append(s)
def normal(k,x,y,w,size=14,color='#444',lines=3):add(k,para(x,y,w,size,color,lines))
def head(k,val,x,y,w,size,color='#111',weight=500,align='left'):
 remove(k,lambda e:e['kind']=='text' and e.get('text')==val);add(k,tx(val,x,y,w,size,weight=weight,color=color,align=align))
def circle(x,y,w,color):return box(x,y,w,w*16/9,color,'50%')
def loop(cx,cy,rx,color,width=4.5):return ring(cx-rx,cy-rx*16/9,rx*2,rx*32/9,[1],[color],1-width/rx)
def star(cx,cy,w,color):
 pts=[]
 for i in range(10):
  r=w/2*(1 if i%2==0 else .42);a=math.radians(-90+i*36);pts.append((cx+math.cos(a)*r,cy+math.sin(a)*r*16/9))
 return path(pts,color,0,color)
# Film image depth and right-aligned body.
k='p050/s02-09';edit(k,lambda e:e['kind']=='image',h=74);edit(k,lambda e:e['kind']=='text' and e.get('text','').startswith('Lorem'),align='right');explain(k,'Source photo ends at 74%; body matches four right-aligned lines.')
add('p050/s02-04',ic(28,78,3,5.34,'CircleArrowRight','#fff'));explain('p050/s02-04','Small outlined arrow restored.')
# Qivora four native segment colors / two-line title / readable timeline.
k='p051/s01-07';remove(k,lambda e:e['kind']=='path');text(k,'Sales\nDevelopment Plan',text='Sales\nDevelopment Plan',size=61,h=23,runs=[{'text':'Sales\n','color':'#eebc1c'},{'text':'Development Plan','color':'#fff'}]);under(k,*ring(7,43,26,46,[10,40,30,20],['#fff','#263d59','#cba315','#edbf16'],0),*ring(59,43,26,46,[18,42,25,15],['#fff','#263d59','#cba315','#edbf16'],0));
for i,(v,c) in enumerate(zip(['2018','2019','2020','2021'],['#fff','#263d59','#cba315','#edbf16'])):add(k,box(7+i*10,93,1.4,2.49,c),tx(v,9+i*10,92.7,8,12,color='#fff'))
explain(k,'Sales gold, Development Plan white on one line; four distinguishable pie colors and 2018–2021 legend restored.')
k='p051/s01-08';bs=[e for e in els(k) if e['kind']=='box' and e['y']==43]
for e,c in zip(bs,['#eabe14','#d5ab15','#aa8b17','#8d7518']):e['fill']=c
explain(k,'Four timeline cards use progressively darker native gold shades.')
k='p051/s01-09';remove(k,lambda e:e['kind']=='text' and e.get('text','').startswith('Lorem'))
for i,(v,y) in enumerate([('Focused on personal\nuse product',68),('Extended to commercial\nuse',85),('Web Design project begin',68),('UI/UX project introduced',85)]):add(k,tx(v,7+i*23,y,20,16,color='#fff',align='center'))
explain(k,'Timeline captions transcribed; centered at native alternating rows.')
# Creative steps: duplicate header, native white cards, actual path endpoints.
for k in [k for k in data if k.startswith('p064/')]:
 remove(k,lambda e:e.get('text')=='Creative Step Business');add(k,tx('Creative Step Business',3,4,40,13,color='#111'));explain(k,'Duplicate brand header reduced to one black native caption.')
k='p064/s04-06';remove(k,lambda e:e['kind']=='text' and (e.get('text','').startswith('Step ') or e.get('text','').startswith('Lorem')))
for x,y,label,c,ico in [(40.5,12,'Step One','#a269c6','Target'),(54.5,41,'Step Two','#e5ba12','Coins'),(70.5,72,'Step Three','#a269c6','HandCoins')]:
 add(k,box(x,y,26,15,'#fff',8),circle(x+1.5,y+2,5,c),ic(x+2.5,y+3.5,3,5.3,ico,'#fff'),tx(label,x+8.5,y+2,17,20,color=c,weight=500),tx('Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nSed do eiusmod tempor.',x+8.5,y+7,17,12,color='#444',leading=1.15))
for j,v in enumerate(['Create value through clear ideas','Build a stronger business strategy']):add(k,ic(7,80+j*5,1.4,2.49,'CircleChevronRight','#999'),tx(v,9,79.6+j*5,31,12,color='#666'))
explain(k,'Three white step cards restored over the stair ribbon; titles/body/circle icons separated; unreadable bullets replaced with normal prose.')
k='p064/s04-03';
for x in [22,40.5,59,77.5]:add(k,circle(x,63,1.6,'#fff'))
edit(k,lambda e:e['kind']=='path' and not e.get('fill') and len(e.get('points',[]))==2,dashed=True);explain(k,'Four small white milestone centers and dashed vertical connectors restored.')
k='p064/s04-04';
for e in els(k):
 if e['kind']=='text' and e.get('text','').startswith('Achieving'):e['runs']=[{'text':'Achieving\nSustainable\n','color':'#111'},{'text':'Success','color':'#a269c6'}]
add(k,tx('Finish',74,80,18,18,color='#888'));explain(k,'Sustainable stays black; Success purple; finish label restored.')
k='p064/s04-07';add(k,path([(79,54),(84,54),(84,42),(97,42),(97,50),(89,50),(89,62),(79,62)],'#d3d3d3',0,'#d3d3d3'),ic(91,29,4,7.11,'Trophy','#b7b7b7'));explain(k,'Final light gray step and trophy restored.')
# Problem statement: layer ordering, green data triangles, card spacing and green chart series.
for k in ['p069/s01-03','p069/s03-03']:
 remove(k,lambda e:e['kind']=='text' and (e.get('text') in ['3758+','High-level benefits'] or e['x']==32 and e['y']>=37 and e['y']<50));add(k,tx('3758+',32,17,19,64),tx('High-level benefits',32,32,20,22),tx('Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nAenean commodo ligula.',32,37,18,15,color='#444'));explain(k,'3758+ and High-level benefits moved above the white card in DOM; original three-line body preserved as plausible prose.')
for k in ['p069/s01-08','p069/s04-03']:
 for e in els(k):
  if e['kind']=='text' and e.get('text','').startswith(('01.','02.','03.','04.')):e.update(y=21 if e['y']<40 else 54,size=24,w=21,h=8.4,lineHeight=1.12)
  if e['kind']=='text' and e.get('text','').startswith('Lorem') and e['x']<48:e.update(y=32 if e['y']<50 else 65,size=14,h=9.5)
 explain(k,'Four card title and body rows separated; button centers retained.')
for k in ['p069/s01-07','p069/s04-04']:add(k,*loop(5,84,17,'#acd82d',4));explain(k,'Green loop restored in front of the lower photograph placeholder.')
for k in [k for k in data if k.startswith('p069/')]:
 for e in list(els(k)):
  if e['kind']=='text' and e.get('size',0)>40 and e.get('text','') in ['85,5K','3651+','4122+','$562','$679','76.2K','94.4K','94%','85.8K','3245+','3977+','4567+','$572','$685','$792']:
   x=max(0,e['x']-3);y=e['y']+2;add(k,path([(x,y+3.6),(x+2,y+3.6),(x+1,y)],'#acd82d',0,'#acd82d'));explain(k,'Native green increase triangle restored before the numeric KPI.')
k='p069/s02-08';remove(k,lambda e:e['kind']=='box' and e['x']>80 and e['y']>60 and e.get('fill')=='#e4f5ce');explain(k,'Spurious pale gradient contour removed; graphic background handled with the prescribed flat placeholder rule.')
k='p069/s02-09';remove(k,lambda e:e['kind']=='box' and e.get('fill')=='#e4f5ce');under(k,*loop(-2,48,17,'#acd82d',4))
for i in range(3):
 text(k,'Process 0'+str(i+1),x=6+i*31,y=59,size=31,h=6.5)
 edit(k,lambda e:e['kind']=='text' and e.get('text','').startswith('Lorem') and e['x']==6+i*31,text='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nAenean commodo ligula eget dolor.',y=66,size=15,h=9.8,lineHeight=1.2)
explain(k,'Green left loop and process row spacing restored; body no longer overlaps lower Learn More buttons.')
k='p069/s02-07';edit(k,lambda e:e['kind']=='path' and len(e.get('points',[]))==4,color='#b9ce58');edit(k,lambda e:e['kind']=='box' and e['w']<1,fill='#111');explain(k,'Three line series green; every data marker black.')
# Profit growth: branding alignment, missing devices / metrics, card placement.
for k in [k for k in data if k.startswith('p073/')]:
 edit(k,lambda e:e['kind']=='text' and 'GLOBAL' in e.get('text',''),text='PROFITTERA GLOBAL',x=88,y=6.3,w=9,size=10,h=2.8,align='right');remove(k,lambda e:e['kind']=='box' and e['x']==86 and e['w']<1);add(k,photo(86,6.3,1,1.78));explain(k,'Tiny brand caption and image logo placeholder separated.')
k='p073/s02-02';under(k,{**photo(49,-4,31,64),'radius':32});remove(k,lambda e:e['kind']=='text' and e['x']==7 and e['y']==78);edit(k,lambda e:e['kind']=='text' and e['y'] in [79,85],size=12.5);add(k,tx('Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.',55,80,20,12,color='#555'));explain(k,'Upper phone placeholder restored; overlapping duplicate bottom paragraph removed.')
k='p073/s02-03';remove(k,lambda e:e['kind']=='path' and e.get('fill'));under(k,*ring(52,21,32,56.89,[39,28,33],['#aaa','#222','#ed7c2d'],.73,-110));add(k,tx('$25,130',7,64,30,60));
for x,y in [(54,22),(80,44),(40,60)]:add(k,tx('$13.230',x,y,14,14))
explain(k,'Missing primary monetary figure and three card values restored; native orange-left ring orientation reconstructed.')
k='p073/s02-06';add(k,{**photo(15,17,5,8.89),'radius':'50%'},{**photo(27,43,5,8.89),'radius':'50%'},tx('$13.230',23,22,16,20),tx('$13.230',35,48,16,20),ic(89,18,2.5,4.44,'TrendingUp','#ef7c2b'));remove(k,lambda e:e['kind']=='chip' and e['y']>=60)
for i,(v,c,fg) in enumerate([('Profit growth','#fff','#555'),('Revenue','#ef7c2b','#fff'),('Profitability','#333','#fff')]):add(k,chip(v,67+i*9,44,8,4,11,c,fg,radius=20))
explain(k,'Two top circular portraits and $13.230 values restored; native white/orange/dark chip row at y44%.')
for k in ['p073/s02-08','p073/s03-09']:under(k,{**photo(0,0,44,54),'radius':20});text(k,'Profit growth',x=51,y=17);explain(k,'Wide upper left image placeholder and profit caption placement restored.')
k='p073/s03-02';under(k,{**photo(45,14,18,32),'radius':20});normal(k,67,34,27,16,lines=2);edit(k,lambda e:e['kind']=='text' and e.get('text','').startswith('Lorem') and e['x']<40,y=74);explain(k,'Sophia portrait and missing right caption restored; introduction paragraph separated from chip.')
k='p073/s03-03';normal(k,66,32,25,16,lines=3);edit(k,lambda e:e['kind']=='text' and e.get('text','').startswith('39'),y=62,size=58,h=12);edit(k,lambda e:e['kind']=='text' and e.get('text','').startswith('Lorem') and e['y']>60 and e['x']>50,y=75,size=15,h=10);explain(k,'Top KPI paragraph restored; lower number and paragraph separated.')
k='p073/s03-04';under(k,photo(74,18,26,82));explain(k,'Right building image replaced by its correctly positioned gray placeholder.')
k='p073/s03-05';normal(k,77,35,20,15,lines=3)
for i,e in enumerate([e for e in els(k) if e['kind']=='chip' and e['y']>70]):e.update(fill=['#ef7c2b','#222','#fff'][i%3],color=['#fff','#fff','#555'][i%3],y=81)
explain(k,'Upper KPI body restored and lower chips use native orange / black / white order.')
for k in ['p073/s03-06','p073/s03-08']:
 remove(k,lambda e:e['kind']=='chip' and e.get('text')=='Profit growth' and e['y']>50);add(k,tx('Profit growth',7,60,30,15,color='#777'),circle(5,60.5,1,'#ef7c2b'));explain(k,'Lower Profit growth caption is plain gray text with a simple orange dot.')
# Editorial portfolio.
k='p080/s02-02';add(k,{**chip('03',5,80,5,8.89,27,'transparent','#171717',radius='50%'),'border':'1px solid #aaa'});explain(k,'Empty third page badge receives the readable native number.')
for k in ['p080/s02-06','p080/s03-05','p080/s06-04']:
 edit(k,lambda e:e['kind']=='image' and e['w']>20 and e['w']<40,clipPath='ellipse(50% 50% at 50% 50%)');explain(k,'Main portrait placeholder follows the native oval silhouette instead of a rectangle; detailed portrait removed.')
add('p080/s02-06',tx('“we are the\nwhat we\nrepeatedly\ndo”.',26,79,11,16,color='#fff',align='right'));explain('p080/s02-06','Small white quote restored in normal readable text.')
for k in ['p080/s03-03','p080/s08-03']:
 for e in els(k):
  if e['kind']=='image':e['radius']=8;e['w']-=.4
 explain(k,'Adjacent numbered photographs remain separate gray regions with native small gaps and rounded corners.')
k='p080/s03-04';remove(k,lambda e:e['kind']=='image');under(k,photo(51,33,23,62),photo(75,33,23,31),photo(75,65,13,30),photo(89,65,9,17))
for i,v in enumerate(['BRAND IDENTITY','PRODUCT NAME','WHO WE ARE']):
 existing=[e for e in els(k) if e['kind']=='chip' and e.get('text')==v]
 if existing:existing[0].update(x=4+i*13,y=42,w=12,h=10,fill='transparent',border='1px solid #777')
 else:add(k,{**chip(v,4+i*13,42,12,10,12,'transparent','#fff',radius=22),'border':'1px solid #777'})
add(k,ic(8,81,2,3.56,'Asterisk','#a69375'),tx('www.reallygoodsite.com',11,81,28,12,color='#fff'));explain(k,'Four photo gutters retained; three native outlined category chips and small link restored.')
k='p080/s03-06';remove(k,lambda e:e['kind']=='text' and (e.get('text') in ['01','02','03','04','Syndey Clowney','Dora Cincora\nCindy','Louisa Herry','Margret Mcleod'] or e.get('text','').startswith('Lorem') and e['x']>50));names=['Syndey Clowney','Dora Cincora Cindy','Louisa Herry','Margret Mcleod']
for i,v in enumerate(names):
 x,y=(84,16) if i==0 else (58,37) if i==1 else (84,59) if i==2 else (57,80);add(k,tx(v,x,y,13,14,color='#fff'),tx(f'0{i+1}',79 if i%2==0 else 73,y,3.5,27,color='#fff'),tx('Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.',79 if i%2==0 else 57,y+6,19,11,color='#fff'))
add(k,tx('www.reallygoodsite.com',42,88,26,11,color='#fff'));explain(k,'Alternating names, numbers and small bodies separated at native rows; illegible names retain the page-specific prior plausible transcription.')
for k in ['p080/s03-08','p080/s03-02','p080/s08-02']:remove(k,lambda e:e['kind']=='text' and e.get('font')=='Kaushan Script');explain(k,'Extra signature removed where absent from the visible native source.')
k='p080/s06-06';add(k,tx('Virginia Kelly',79,85,18,32,'Kaushan Script',color='#fff'))
for y in [40,44,48]:add(k,photo(78,y,1.7,3.02))
add(k,ic(78,55,1.6,20,'ArrowDown','#fff'));explain(k,'Right signature, three prescribed gray social image placeholders and vertical arrow restored.')
k='p080/s06-08';add(k,tx('Subtitle_',15,73,9,15,color='#fff'),tx('Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nSed do eiusmod tempor.',4,87,18,11,color='#fff',align='right'));explain(k,'Missing KPI subtitle and readable lower caption restored.')
# Minimal presentation chart/caption cleanup.
for k in ['p081/s02-04','p081/s04-03']:
 edit(k,lambda e:e['kind']=='text' and e.get('text')=='Details :' and e['x']>60,y=35);edit(k,lambda e:e['kind']=='text' and e.get('text','').startswith('Lorem') and e['x']>60,y=41,size=12,h=7);explain(k,'Right Details heading and body use separate native rows.')
k='p081/s02-05';
for x,y,c in [(41,45,'#d1cbbb'),(80,40,'#bbb'),(63,69,'#d1cbbb')]:add(k,*ring(x-4.5,y-8,9,16,[1],[c],.67),circle(x-1,y-1.78,2,'#333'))
explain(k,'Simple map-region rings and dark centers restored over the complex-map placeholder.')
k='p081/s03-04';edit(k,lambda e:e['kind']=='text' and 'Table' in e.get('text',''),y=18);remove(k,lambda e:e['kind']=='text' and e.get('text','').startswith('Lorem') and e['x']<40);add(k,tx('Lorem ipsum dolor sit amet, consectetur\nadipiscing elit. Sed do eiusmod tempor.',11,68,28,13,color='#444'),tx('Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nSed do eiusmod tempor incididunt.',11,77,28,13,color='#444'));explain(k,'Contents heading native vertical alignment; left body reduced to two distinct ordinary paragraphs.')
for k in ['p081/s03-05','p081/s04-01']:
 for e in els(k):
  if e['kind']=='text' and 'Title Text' in e.get('text','') and e['x']>50:e.update(x=62 if e['x']<76 else 81,y=57,size=14,w=16,h=4)
  elif e['kind']=='text' and e.get('text','').startswith('Lorem') and e['x']>50:e.update(x=62 if e['x']<76 else 81,y=62,size=12,w=16,h=10)
 add(k,tx('Million',70,85,7,10),tx('Million',88,85,7,10));explain(k,'Two subtitle/caption columns restored below their icons; tiny Million captions added.')
k='p081/s03-06';add(k,tx('Position',14,56,14,10,align='center'),tx('Position',14,82,14,10,align='center'),box(35,42,4,.25,'#333'));explain(k,'Diamond statistics receive their native tiny Position captions and separator dash.')
k='p081/s03-07';remove(k,lambda e:e['kind']=='box' and e.get('radius')=='50%' and e.get('fill')=='#333333');edit(k,lambda e:e['kind']=='icon',color='#111');explain(k,'Dark offset circle artifact removed; simple icons appear black over the complete beige circles.')
k='p081/s03-09';
for i,x in enumerate([37,58,79]):add(k,box(x,30,12,1,'#ded8c8' if i==0 else '#333'))
explain(k,'Three small native horizontal accents restored over value cards.')
for k in ['p081/s04-04','p081/s05-08']:
 add(k,box(51,39,6,10.67,'#ded8c8'),ic(52,41,4,7.11,'Network','#222'));explain(k,'Native small network square restored; remaining ring segment angle approximation recorded.')
k='p081/s05-02';add(k,tx('From By',63,81,10,10))
for x in [63,65,67,69]:add(k,photo(x,89,1.2,2.13))
explain(k,'Tiny From By caption and social image placeholders restored.')
k='p081/s05-03';remove(k,lambda e:e['kind']=='text' and '◎' in e.get('text',''))
for y in [55,91]:
 for x in [16,38,60,82]:
  for j in range(4):add(k,photo(x+j*1.6,y,1.1,1.96))
explain(k,'Fake social glyph strings replaced by four small gray image-icon placeholders per portrait.')
k='p081/s05-07';edit(k,lambda e:e.get('text')=='75%',x=77,w=10,align='center');explain(k,'75% labels optically centered inside their ring centers.')
# Quantive: displaced ornaments and native card/header overlaps.
placements={'s02-01':[(7,51),(96,70)],'s02-02':[(8,11),(91,46)],'s02-03':[(5,11),(93,62)],'s03-03':[(31,11),(63,90),(98,35)],'s03-04':[(-2,44),(98,89)],'s03-05':[(-2,12),(90,89)],'s03-06':[(12,12),(98,96)],'s03-07':[(30,7),(58,89),(-2,82)],'s03-08':[(20,61),(47,48)],'s03-09':[(13,8),(90,89)],'s03-10':[(15,61),(91,57)],'s03-11':[(7,83),(88,27)],'s03-12':[(7,12),(90,95)],'s03-13':[(48,12),(-2,82)],'s03-14':[(25,12),(73,85)],'s03-15':[(54,19),(1,92)],'s03-16':[(54,18),(58,85)]}
for sid,positions in placements.items():
 k='p091/'+sid;existing=[e for e in els(k) if e['kind']=='icon' and e.get('icon')=='Asterisk'];remove(k,lambda e:e['kind']=='icon' and e.get('icon')=='Asterisk')
 for (x,y),e in zip(positions,existing+[ic(0,0,4,7.1,'Asterisk','#4b4ecb')]):e.update(x=x,y=y);add(k,e)
 explain(k,'Six-ray simple star ornaments moved to their individual native positions; edge clipping intentional.')
k='p091/s02-01';add(k,circle(34,22,4.6,'#4b4ecb'),ic(35,23.5,2.6,4.62,'HandCoins','#fff'),tx('Financial growth',40,29,20,12));explain(k,'Small finance icon and caption restored.')
k='p091/s02-03';remove(k,lambda e:e['kind']=='text' and e.get('text','').startswith('Lorem') and e['y']>75)
for x in [13,35,57]:add(k,tx('Subtitle here',x,85,18,10,color='#fff'))
add(k,tx('Business performance',78,88,18,11));explain(k,'Three card captions no longer overlap Learn More; bottom KPI label restored.')
k='p091/s03-03';remove(k,lambda e:e['kind']=='text' and ('Vision Statement' in e.get('text','') or 'Mission Statement' in e.get('text','')));add(k,tx('Vision Statement',8,64,20,20,color='#fff'),tx('Mission Statement',30,64,20,20,color='#fff'));explain(k,'Duplicate outside card titles removed; one white title inside each card.')
k='p091/s03-04';add(k,chip('Learn More',9,22,7,3,10,'#fff','#4b4ecb',radius=10),ic(23,23,1.8,3.2,'CircleArrowRight','#fff'))
for i,v in enumerate([0,1,2,3,4,5,6]):add(k,tx(str(v),5,84-i*8,3,10,color='#777'))
explain(k,'Small Investing controls and chart numeric axis restored.')
k='p091/s03-06';text(k,'Objectives',x=40,y=17,w=23,size=15,h=3.5,align='center');text(k,'SMART goals',x=13,y=21,w=74,size=52,h=11,align='center');under(k,box(55.5,22,13,7.4,'#4b4ecb'))
for e in els(k):
 if e['kind']=='text' and e.get('text','').startswith('Lorem') and e['x'] in [24,46,68,35,57]:e.update(text='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.',size=12,h=5,y=64 if e['y']<70 else 84)
add(k,circle(11,77,3.5,'#4b4ecb'),ic(11.7,78.2,2.1,3.7,'HandCoins','#fff'),circle(95,77,3.5,'#4b4ecb'),ic(95.7,78.2,2.1,3.7,'HandCoins','#fff'),tx('Revenue performance',11,89,23,10),tx('Financial objectives',78,89,21,10));explain(k,'Objectives above SMART goals; highlight behind goals and readable compact card body; native bottom finance icon/captions restored.')
k='p091/s03-08';remove(k,lambda e:e['kind']=='box' and e.get('fill')=='#4b4ecb' and e['w']>10 and e['w']<30 and e['y']>30 and e['y']<60);under(k,box(74,33,19,8,'#4b4ecb'));add(k,tx('Solution',58,20,18,16),tx('Customer impact',7,79,20,12));explain(k,'Overview highlight aligns behind the title instead of beneath it.')
k='p091/s03-09';add(k,circle(8,20,4,'#4b4ecb'),ic(8.8,21.4,2.4,4.2,'TrendingUp','#fff'),tx('Customer confidence',8,41,20,11),tx('38',27,18,8,24),tx('44',38,18,8,24),chip('75%',32,42,9,4,14,'#292181','#fff',radius=18));explain(k,'Small original chart KPI annotations and percentage pill restored; tiny obscured caption replaced by ordinary text.')
k='p091/s03-10';add(k,circle(20,22,3.5,'#4b4ecb'),ic(20.7,23.2,2.1,3.7,'Users','#fff'),circle(20,38,3.5,'#4b4ecb'),ic(20.7,39.2,2.1,3.7,'Users','#fff'),circle(51,17,6,'#4b4ecb'),ic(52.2,19,3.6,6.4,'Users','#fff'),tx('Customer distribution',7,27,18,10),tx('Active customers',7,43,18,10));normal(k,69,83,24,12,lines=2);explain(k,'Native customer icon markers and lower caption restored.')
k='p091/s03-11';add(k,chip('Learn More',8,44,9,5,13,'#4b4ecb','#fff',radius=20));edit(k,lambda e:e['kind']=='path' and not e.get('fill') and len(e.get('points',[]))==2,dashed=True);explain(k,'Learn More restored; cross quadrant connectors dashed.')
k='p091/s03-12';
for e in els(k):
 if e['kind']=='path' and e.get('fill') in ['#4b4ecb','#292181']:e['fill']='#292181' if e['fill']=='#4b4ecb' else '#4b4ecb';e['color']=e['fill']
explain(k,'Four-ring quadrant order corrected to blue upper-left/lower-right and navy upper-right/lower-left.')
k='p091/s03-13';edit(k,lambda e:e['kind']=='text' and e.get('text') in ['Contact Us','About Us','Home'],color='#fff');edit(k,lambda e:e['kind']=='text' and 'Organizational' in e.get('text',''),x=63,w=32,align='right');edit(k,lambda e:e['kind']=='image' and e['w']<12,w=8,h=14.22,radius='50%');explain(k,'Dark-page navigation white; organization title anchored right; six native circular portrait placeholders.')
k='p091/s03-15';add(k,chip('34.5%',71,60,8,4,13,'#8372c6','#fff',radius=20),tx('Financial growth\nand performance',81,29,14,12));normal(k,79,80,18,12,lines=2);explain(k,'Chart percentage badge and right finance captions restored.')
k='p091/s03-16';add(k,tx('Outcomes & tactics',8,18,35,16),circle(70,18,3,'#4b4ecb'),ic(70.5,18.9,2,3.5,'HandCoins','#fff'),circle(70,30,3,'#4b4ecb'),ic(70.5,30.9,2,3.5,'Users','#fff'))
for x,v in zip([10,17,23,29],['Q1','Q2','Q3','Q4']):add(k,tx(v,x,80,5,11))
explain(k,'Native outcome subtitle, simple stat icons and Q1–Q4 axis restored.')
# Payone.
for k in ['p092/s01-01','p092/s02-04']:edit(k,lambda e:e['kind']=='text' and 'PAYONE' in e.get('text',''),color='#111');explain(k,'Payone cover logo caption matches native black.')
for k in ['p092/s01-03','p092/s02-07']:
 for x in [41,72]:add(k,{**circle(x,20,1.5,'transparent'),'border':'1px solid #fff'})
 explain(k,'Two tiny native outlined circle bullets restored.')
k='p092/s01-07';remove(k,lambda e:e['kind']=='text' and e['x']<35 and 50<e['y']<70 and e.get('text','').startswith('Lorem'));add(k,tx('Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nSed do eiusmod tempor incididunt\nut labore et dolore magna aliqua.',2,55,29,14,color='#fff'));explain(k,'Duplicate red-card paragraph replaced with one native-sized four-line body.')
k='p092/s01-09';remove(k,lambda e:e['kind']=='box' and e['x']==3 and e['y'] in [73,79,85]);remove(k,lambda e:e['kind']=='text' and '$' in e.get('text','') and e['x']==7)
for y,year,v,c in [(57,'2027','$30,000','#df2718'),(69,'2026','$80,000','#aaa'),(80,'2025','$200,000','#080808')]:add(k,box(2.5,y+1,1.5,2.67,c),tx(year,6,y,12,15),tx(v,19,y,14,20,weight=500))
for y in [65,76]:add(k,path([(2.5,y),(29.5,y)],'#aaa',.5))
for x,y in [(87,32),(61,54),(49,78)]:add(k,tx('Lorem ipsum',x,y,13,11))
explain(k,'Financial legend restored to three aligned rows with color box/year/value; readable original inconsistent values retained.')
k='p092/s02-02';add(k,tx('Read more',24,32,8,12,color='#fff'),ic(32,31.8,1.5,2.67,'CircleArrowRight','#fff'));explain(k,'Tiny Read more arrow caption restored.')
k='p092/s02-03';remove(k,lambda e:e['kind']=='text' and e.get('text','').startswith('Lorem') and e['x']<30 and e['y']>65);add(k,tx('Financial Technology Expert',2,72,27,12,color='#df2718'));edit(k,lambda e:e.get('text')=='Presentation date',text='Date and time');edit(k,lambda e:'December' in e.get('text',''),weight=400);explain(k,'Amanda role replaces extra lower prose; Date and time label and regular date weight.')
k='p092/s02-06';text(k,'30%',x=36,y=82,w=20,size=86,h=18,weight=400,color='#df2718');add(k,tx('Description',37,50,17,22,color='#fff'),tx('Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.',37,56,17,11,color='#fff'),ic(51,49,3,5.3,'ArrowUpRight','#df2718'));edit(k,lambda e:e['kind']=='text' and 'PAYONE' in e.get('text',''),color='#fff');explain(k,'Black-card description and red arrow restored; 30% native larger; white Payone caption on red.')
k='p092/s02-08';edit(k,lambda e:'Unique Value' in e.get('text',''),text='Unique Value\nProposition',size=22,h=8);explain(k,'Unique Value Proposition uses native two-line break.')
k='p092/s04-04';
for x,c,ico in [(42,'#df2718','CreditCard'),(70,'#111','Users'),(96,'#df2718','ChartNoAxesCombined')]:add(k,circle(x,5,2.3,c),ic(x+.45,5.8,1.4,2.49,ico,'#fff'))
explain(k,'Three tiny simple top-right data icons restored.')
# B2B simple shapes, star fills, burst clipping.
k='p101/s02-04';remove(k,lambda e:e['kind']=='icon' and e.get('icon')=='Triangle')
for x,y,c,up in [(59,36,'#070707',True),(33,71,'#7946fd',False),(85,71,'#ff4826',False)]:add(k,path([(x,y+2.8 if up else y),(x+1.6,y+2.8 if up else y),(x+.8,y if up else y+2.8)],c,0,c))
edit(k,lambda e:e['kind']=='text' and e['y']>15,align='center');explain(k,'Warning triangles replaced by actual filled arrowheads; card text centered.')
for k in ['p101/s02-06']:
 edit(k,lambda e:e['kind']=='text' and e['y']>20,align='center');explain(k,'Four section card subtitles and bodies centered.')
k='p101/s02-05';
for e in els(k):
 if e['kind']=='box' and e['w']<10 and e['h']>6:e['radius']='50%'
add(k,path([(90,33),(93,37.5),(90,42)],'#7946fd',0,'#7946fd'));explain(k,'Four simple top icon backgrounds circular; final purple ribbon has a clean right arrowhead.')
k='p101/s02-07';remove(k,lambda e:e['kind']=='text' and e.get('text')=='31');explain(k,'Calendar cell absent native day kept empty.')
k='p101/s02-09';edit(k,lambda e:e['kind']=='path' and len(e.get('points',[]))==32,clipPath='polygon(7% 45%,69% 45%,69% 80%,7% 80%)');explain(k,'Orange decorative burst clipped to native white contact card boundary.')
k='p101/s03-02';
for e in els(k):
 if e['kind']=='path' and len(e.get('points',[]))==32:
  pts=e['points'];cx=(min(p['x']for p in pts)+max(p['x']for p in pts))/2;cy=(min(p['y']for p in pts)+max(p['y']for p in pts))/2
  for p in pts:p['x']+=39-cx;p['y']+=7-cy
  e['clipPath']='polygon(1% 7%,49% 7%,49% 92%,1% 92%)'
explain(k,'Orange burst aligns with and clips at top edge of native contact card.')
k='p101/s03-03';
for e in els(k):
 if e['kind']=='path' and len(e.get('points',[]))==32:e['clipPath']='polygon(48% 40%,72% 40%,72% 100%,48% 100%)' if e.get('fill')=='#191919' else 'polygon(73% 25%,97% 25%,97% 100%,73% 100%)'
explain(k,'Two decorative bursts clipped independently to their native dark/orange card columns.')
k='p101/s03-06';remove(k,lambda e:e['kind']=='text' and '★' in e.get('text',''));add(k,tx('4.3',73,62,7,20,color='#edb643'))
for i in range(5):add(k,star(80+i*2,64,1.5,'#edb643' if i<4 else '#fff'))
explain(k,'Rating glyph string replaced by five clean simple star polygons with native four gold / one white fills.')
k='p101/s03-07';remove(k,lambda e:e['kind']=='text' and 'Revenue' in e.get('text','') and '●' in e.get('text',''))
for x,v,c in [(11,'Revenue','#7946fd'),(24,'Profit','#ff4826'),(34,'Cost','#070707')]:add(k,circle(x,87,1,c),tx(v,x+2,86.8,10,12))
for v,x,y in [('60',71,83),('83',78,79),('65',84,85),('104',91,80)]:text(k,v,x=x,y=y,size=12,h=3)
for i,v in enumerate(['1st','2nd','3rd','4th']):add(k,tx(v,71+i*6.5,93,5,10,color='#fff'))
add(k,tx('Item 1',66,41,7,10),tx('Item 2',66,52,7,10));explain(k,'Revenue legend colors and line chart value/axis labels restored.')
k='p101/s03-08';edit(k,lambda e:e['kind']=='box' and e['x']==12 and e['y']==73,fill='#7946fd');add(k,ic(87,31,2,3.56,'UserRound','#fff'),ic(87,62,2,3.56,'UserRound','#fff'));explain(k,'2019 bar purple, native two tiny card icons restored; heading retained exactly as authored.')
# Fundraising readable native paragraphs and simple accents.
k='p104/s02-01';edit(k,lambda e:e['kind']=='text' and e.get('text')=='Average order value' and e['x']>60,text='20 templates');edit(k,lambda e:e['kind']=='text' and e.get('text','').startswith('Lorem') and e['y']<30,text='Repeatable. Scalable. Digital-first. We\ngenerate revenue through multiple scalable\nand predictable income streams.',size=16,h=10,w=44);explain(k,'Readable introductory copy transcribed; Product Bundles caption 20 templates.')
k='p104/s02-03';edit(k,lambda e:e['kind']=='text' and e['x']>45 and e['y']<30 and e.get('text','').startswith('Lorem'),text='The digital market is crowded with legacy tools and\ngeneric solutions — but none fully meet the needs\nof your target audience the way we do.',size=15,w=46,h=10);explain(k,'Readable competition introduction transcribed with native three-line layout.')
k='p104/s02-07';edit(k,lambda e:e['kind']=='text' and e.get('text','').startswith('Lorem'),align='center');explain(k,'Three team body captions centered.')
k='p104/s03-02';ps=[e for e in els(k) if e['kind']=='text' and e.get('text','').startswith('Lorem')]
for e,v in zip(ps,['To become the go-to global design\npartner for businesses seeking a\nmodern, impactful brand identity.','We craft premium digital assets that\nhelp brands stand out, connect\nemotionally, and grow sustainably.']):e.update(text=v,size=16,h=11)
explain(k,'Readable vision and mission prose transcribed with native line breaks.')
k='p104/s03-04';ps=[e for e in els(k) if e['kind']=='text' and e.get('text','').startswith('Lorem')]
if ps:ps[0].update(text='Represents the full revenue\npotential across all markets\nglobally.',size=13,h=8.5)
if len(ps)>2:ps[2].update(text='Revenue potential we can earn\nthrough focused customers\nand regional growth.',size=13,h=8.5)
explain(k,'TAM distinct native definition restored; unreadable SOM description replaced by ordinary page-specific prose.')
k='p104/s03-05';edit(k,lambda e:e['kind']=='box' and e['w']<2 and e['y']<30,fill='#ed6a63');explain(k,'How we solve it accent dot native coral.')
k='p104/s03-06';edit(k,lambda e:e['kind']=='box' and e.get('radius')=='50%' and e['x']<0,x=-43,y=-15.8,w=74,h=131.6);explain(k,'Large left purple circle continues through the full native slide height.')
k='p104/s03-07';ps=[e for e in els(k) if e['kind']=='text' and e.get('text','').startswith('Lorem')];vs=['These values shape our culture, guide\nour decisions, and define how we work\nwith every client and collaborator.','Everything we create is rooted in clarity,\nintention, and impact.','We prioritize honesty, transparency, and trust\nin all our relationships.','We believe in fresh ideas, original thinking, and\nbeautiful execution.','We’re always learning, evolving, and pushing\nboundaries — for ourselves and our clients.']
for e,v in zip(ps,vs):e.update(text=v,size=14,h=10,w=max(e['w'],27))
explain(k,'Readable native culture and values descriptions transcribed; browser checks preserve original text areas.')
# Brand proposal native numeric punctuation and centered captions.
k='p107/s05-05';text(k,'86.2%',text='86,2%');explain(k,'First percentage retains native comma punctuation.')
for k in ['p107/s05-06','p107/s05-09']:
 edit(k,lambda e:e['kind']=='text' and (e.get('text','').startswith('Lorem') or e.get('text') in ['+750K','+125K','More Information']),align='center');explain(k,'Native KPI/body/More Information captions centered.')
# Preserve shape clipping declarations and write all pages atomically once.
modified=[k for k in data if data[k]!=before[k]]
for k in modified:
 for e in els(k):
  if e['kind']!='text' and (e['x']<0 or e['y']<0 or e['x']+e['w']>100 or e['y']+e['h']>100):e['allowClip']=True;e['clipReason']='Native decorative shape or image continues beyond slide edge.'
(tmp:=src.with_suffix('.json.tmp')).write_text(json.dumps(data));tmp.replace(src)
records={'round':3,'basis':'Every one of 234 final individual comparison images actually opened and inspected before this atomic correction. No fourth visual correction round.','modifiedIDs':modified,'pages':[{'id':k,'fixes':notes.get(k,[]),'remainingDifferences':['Detailed photographs, complex graphics and image brand icons are solid #e5e5e5 placeholders by instruction.','Native miniature text and font rasterization remain approximate where resolution prevents exact transcription.']}for k in modified],'sourceSha256Before':hashlib.sha256(json.dumps(before,separators=(',',':')).encode()).hexdigest(),'sourceSha256After':hashlib.sha256(src.read_bytes()).hexdigest(),'createdAt':datetime.now(timezone.utc).isoformat()}
(ROOT/'review/group-b-final-third-round-modified.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
print('atomic third-round pages',len(modified));print(' '.join(modified))
