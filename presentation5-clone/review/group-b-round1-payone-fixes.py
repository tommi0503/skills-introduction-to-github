from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
d=json.loads((ROOT/'src/decks/group-b-data.json').read_text());R='#d6160a';K='#080808';G='#d4d4d4';W='#fff'
def head(t,x=2,y=17,w=43,size=62,color=K):return tx(t,x,y,w,size,weight=700,color=color,leading=1.03)
def body(x,y,w,color=K,lines=3,size=15):return para(x,y,w,size,color,lines)
def desc(x,y,w=25,color=K):return [tx('Description',x,y,w,23,weight=700,color=color),body(x,y+5,w,color)]
def logo(color=K):return [tx('Pitchdeck',2.3,5,22,27,weight=700,color=color),tx('Financial Technology',2.3,11,25,9,color=color),tx('◉ PAYONE',86,5,12,17,weight=700,color=color,align='right'),tx('2025',93,10,5,10,color=R,align='right')]
def circle(x,y,w,fill):return box(x,y,w,w*1.777,fill,'50%')
def smallbullet(x,y,c=R):return [circle(x,y,1.4,c)]
for k,s in d.items():
 if not k.startswith('p092/'):continue
 sid=k.split('/')[1];s['background']=G;e=[];g=[]
 if sid in ['s01-01','s02-04']:
  g=[box(0,0,38.5,54,R),box(0,54,38.5,46,K),photo(38.5,0,31.5,100)]
  e=[head('This Time’s\nTopic of\nDiscussion',2,17,35,62,W),head('“Lorem ipsum\ndolor sit amet,\nconsectetur.”',2,60,34,40,W),body(18,81,17,W,4,13)]
  for y,t in [(25,'Session 01'),(50,'Session 02'),(74,'Session 03')]:e += [tx(t,76,y,21,24,weight=700),body(76,y+6,21,lines=4,size=13)]
 elif sid in ['s01-02','s02-05']:
  e=[head('Problem\nStatement\n(Main)'),head('70%',42,40,23,100),head('30%',72,40,23,100),body(2,79,29)]
  g=[path([[68,40],[68,80]],'#aaa',1)];e += desc(42,62,22)+desc(72,62,23)
 elif sid in ['s01-03','s02-07']:
  g=[box(0,0,100,55,R),photo(35.5,55,64.5,45)];e=[head('Solutions',color=W)]
  for x in [36,68]:e += [tx('Lorem ipsum dolor sit amet',x,26,29,21,weight=700,color=W),body(x,32,28,W,4)]
  e += [head('“Lorem ipsum dolor sit\namet, consectetur\nadipiscing elit.”',2,60,32,33),body(2,81,31,size=13)]
 elif sid in ['s01-04','s04-03']:
  e=[head('Target Market',31,4,46,64)]
  for y,t,icon in [(19,'SMEs and Retail','Store'),(42,'Merchant online','ShoppingCart'),(65,'Freelancer','Briefcase')]:
   g += [photo(2.5,y,67,21),circle(73,y+3,4,R),ic(74,y+5,2,3.5,icon,W)];e += [tx(t,5,y+14,50,21,weight=600,color=W)]+desc(79,y+3,18)
 elif sid in ['s01-05','s02-09']:
  g=[photo(33,16,31,84)];e=[head('Product /\nDemo')]+desc(2,61,26)
  for y,icon in [(23,'Smartphone'),(46,'ShieldCheck'),(70,'CreditCard')]:g += [circle(70,y,4,R),ic(71,y+2,2,3.5,icon,W)];e += desc(77,y,20)
 elif sid in ['s01-06','s04-05']:
  e=[head('Market Trends',49,17,48,60)];g=ring(3,20,37,66,[41,33,14,12],[K,R,'#e47870','#b5b5b5'],.47)
  for t,x,y,c in [('Data 1',29,46,W),('Data 2',13,73,W),('Data 3',5,44,W),('Data 4',15,27,K)]:e += [tx(t,x,y,12,21,weight=700,color=c),tx('Description',x,y+4,12,11,color=c)]
  for x,y,v,c in [(49,39,'41%',K),(74,39,'33%',R),(49,66,'14%','#e47870'),(74,66,'12%','#b5b5b5')]:e += [head(v,x,y,22,48,c)]+desc(x,y+10,22)
 elif sid=='s01-07':
  g=[box(0,44,34,56,R),box(46,48,10,38,K),box(60,26,10,60,R),path([[42,86],[75,86]],K,1)]
  e=[head('Marketing\n& Sales Plan'),head('2024-2025',3,67,29,52,W),body(3,80,29,W),head('2500',46,42,14,31),head('4000',60,20,14,31)]+desc(77,48,20)
  for i in range(5):e += [tx(str(i*1000),36,84-i*12,8,12,align='right')]
 elif sid=='s01-08':
  g=[box(0,53,100,47,R)];e=[head('Seeking\nProfessional\nAdvice')]
  for x,y in [(43,8),(4,58),(38,58),(72,58)]:g += [photo(x,y,20,35.55,'ellipse(50% 50% at 50% 50%)')];e += [tx('Diana Doe',x+21,y+11,24,27,weight=700,color=K if y==8 else W),tx('Financial Expert',x+21,y+17,24,14,color=K if y==8 else W),tx('diana@email.com',x+21,y+22,24,12,color=K if y==8 else W)] if y==8 else [tx('Diana Doe',x+21,y+9,10,17,weight=700,color=W),tx('Financial\nExpert',x+21,y+15,10,12,color=W)]
 elif sid=='s01-09':
  e=[head('Financial\nProjection\nfor 2026')]
  for y,w,t,c in [(20,45,'200k',R),(42,18,'80k','#aaa'),(65,7,'30k',K)]:g += [box(39,y,w,17,c)];e += [head(t,40+w,y+4,13,35)]
  for i,(t,c) in enumerate([('Revenue',R),('Expenses','#aaa'),('Net Profit',K)]):g += [box(3,73+i*6,2,3,c)];e += [tx(t,7,73+i*6,25,19)]
 elif sid=='s02-01':
  s['background']=R;g=[photo(26,20,32,57)];e=[head('PAYONE',65,42,34,100,W),head('Fintech Startup\nPresentation',2,44,24,31,W)]
 elif sid=='s02-02':
  s['background']=R;g=[photo(0,41,100,59)];e=[head('Welcome',24,3,53,66,W),body(24,16,47,W,5,18),head('Seamless Payment,\nSmarter Business',9,52,83,86,W)]
 elif sid=='s02-03':
  g=[box(41,60,59,40,R),photo(31,40,21,46)];e=[head('Your Financial\nSolution'),head('December 10,\n2025',64,75,35,51,W),tx('Presentation date',64,68,32,17,color=W),tx('Amanda Doe',2,66,27,30,weight=700),body(2,75,27),body(65,17,31,lines=6)]
 elif sid=='s02-06':
  g=[box(56,0,44,100,R),box(34,44,22,56,K)];e=[head('Impact of\nProblems')]+desc(2,61,28)+[head('30%',36,85,18,52,R)]
  for y in [20,48,76]:e += [tx('Lorem ipsum dolor sit amet',66,y,31,23,weight=700,color=W),body(66,y+7,31,W,3)]
 elif sid=='s02-08':
  s['background']=K;g=[photo(36,40,62,33)];e=[head('UPV',2,17,25,62,W),head('Small Businesses Grow,\nEconomies Thrive.',36,17,62,59,W),tx('Unique Value Proposition',2,61,29,23,weight=700,color=W),body(2,68,29,W)]
  for x in [36,67]:g += smallbullet(x,80);e += [tx('Lorem ipsum',x+3,80,26,22,weight=700,color=W),body(x+3,86,26,W,3,13)]
 elif sid=='s04-01':
  g=[photo(39,0,61,100)];e=[head('Friendly\nUser\nInterface',2,17,33,61)]+desc(2,60,32)
 elif sid=='s04-02':
  e=[head('How We Works',2,17,53,60),body(71,17,26,lines=4,size=12)]
  for i in range(4):x=2.5+i*24;g += [box(x,38,22.5,44,K if i==0 else R),ic(x+17,42,3,5,['Flag','Handshake','Plane','CreditCard'][i],W)];e += [tx(f'0{i+1}',x+2,42,12,43,color=W),tx('Lorem ipsum',x+2,59,19,22,weight=700,color=W),body(x+2,65,19,W,4,13)]
 elif sid=='s04-04':
  g=[box(21,0,26.5,45,'#bfbfbf'),box(47.5,0,26.5,67,R),box(74,0,26,90,K)];e=[head('Market Size',2,70,46,60)]+desc(37,70,34)
  for x,y,t,name,c in [(23,26,'65\nMillion','Retails',K),(49,47,'170\nMillion','Users',W),(76,69,'100\nBillion','Transaction',W)]:e += [head(t,x,y,23,57,c),tx(name,x,5,22,23,weight=700,color=c),tx('Lorem ipsum dolor sit amet.',x,10,23,10,color=c)]
 elif sid=='s04-06':
  e=[head('Business Model',29,4,55,63)];g=[photo(2,50,95,36)]
  for i,c in enumerate([K,R,'#cd5c56','#bcbcbc']):x=2+i*24;g += [box(x,17,24,33,c),ic(x+2,20,4,7,['Search','Network','CircleDollarSign','Truck'][i],W if i<3 else K)];e += [tx(f'0{i+1}',x+2,37,10,42,weight=700,color=R if i==3 else W),body(x+11,38,11,W if i<3 else K,3,12)]
 elif sid=='s04-07':
  g=ring(3,42,24,43,[60,40],[K,R],.44)+[photo(41,5,21,41),photo(77,48,21,41)];e=[head('Customer\nPersona',2,17,39,60)]
  for x,y,t,age in [(66,12,'Thomas Doe','37 years old'),(57,57,'Amanda Doe','24 years old')]:e += [chip(age,x,y-6,10,5,12,R,W),tx(t,x,y,30,28,weight=700),tx('Coffee Shop Owner',x,y+6,30,15,color=R),body(x,y+12,30,lines=3)]
  e += desc(31,58,22);e += [tx('Men       40%\nWomen   60%',33,64,23,16)]
 elif sid=='s04-08':
  e=[head('Pricing Strategy',2,17,53,62),body(52,17,44,lines=4,size=14)]
  for y,name,p,c in [(35,'Standard','45',K),(61,'Premium','59',R)]:g += [box(3,y,94,25,c)];e += [tx(name,7,y+8,24,26,weight=700,color=W),tx('Simple transactions',7,y+14,24,11,color=W),tx('$',27,y+8,5,23,color=W),head(p,32,y+6,13,73,W),tx('.90' if p=='45' else '.00',43,y+7,8,24,weight=700,color=W),body(52,y+8,20,W,3,13),body(75,y+8,20,W,3,13)]
 elif sid=='s04-09':
  e=[head('Go-to-Market\nStrategy',58,17,40,61)];g=[circle(15,18,23,K),circle(4,50,23,'#bcbcbc'),circle(26,51,23,R)]
  for t,x,y,c in [('Integration\nwith major\nmarketplaces',17,34,W),('Referral\nprogram for\nmerchants',6,66,K),('Partnership\nwith SME\nassociations',28,66,W)]:e += [tx(t,x,y,19,20,weight=600,color=c,align='center')]
  for y in [44,61,78]:g += smallbullet(58,y);e += desc(61,y,34)
 e += logo(W if sid in ['s01-01','s02-04','s01-03','s02-07','s02-01','s02-02','s02-08'] else K)
 if sid!='s02-01':e += [tx('www.payone.com',6,94,37,9,color='#888'),tx(sid.split('-')[1],95,94,3,10,color=R)]
 s['elements']=g+e
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(d))
