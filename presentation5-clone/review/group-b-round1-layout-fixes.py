from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
data=json.loads((ROOT/'src/decks/group-b-data.json').read_text());W='#fff';K='#333333';S='#ded8c8'
def add(d,s,e):data[d+'/'+s]['elements']+=e
def rule(x,y,w,c='#666'):return path([[x,y],[x+w,y]],c,1)
def ptext(x,y,w,lines=4,color=W,size=15):
 e=para(x,y,w,size,color,lines)
 # A small two-paragraph source uses actual prose, never anonymous lines.
 if lines>4:
  second=para(x,y+8,w,size,color,lines-3);return [e,second]
 return [e]
# Evgeny editorial details manually rebuilt after viewing every cell.
for key,s in data.items():
 if not key.startswith('p080'):continue
 for e in s['elements']:
  if e['kind']=='text' and e.get('text')=='Virginia Kelly':e['size']=35;e['font']='Kaushan Script';e['x']=4;e['y']=87;e['w']=28;e['h']=8
  if e['kind']=='text' and e.get('text','').startswith('SELECTEDWORK'):
   e['size']=21;e['text']='SELECTEDWORK/\nDESIGN PORTFOLIO\nFOR 2030'
  if e['kind']=='text' and e.get('text','').startswith('Lorem ipsum') and e['x']<10:e['text']='THERE ARE MANY VARIATIONS OF PASSAGES OF LOREM\nIPSUM AVAILABLE, BUT THE MAJORITY HAVE SUFFERED\nALTERATION IN SOME FORM, BY INJECTED HUMOUR OR\nRANDOM WORDS WHICH DO NOT LOOK EVEN SLIGHTLY\nBELIEVABLE. IF YOU ARE GOING TO USE A PASSAGE.';e['w']=35;e['size']=14;e['h']=17
# Correct placeholder bounds from source grid, not text masks.
photos={'s02-02':[(55,56,20,39),(76,56,21,39)],'s02-03':[(25,21,16,34),(58,26,10,18),(51,65,24,30)],'s02-04':[(26,46,28,45)],'s02-05':[(30,38,17,29),(48,14,27,59),(76,14,21,25),(76,41,21,32)],'s03-01':[(0,37,40,63)],'s03-02':[(46,8,25,41),(73,8,27,92)],'s03-03':[(46,33,18,37),(64,33,18,37),(82,65,18,35)],'s03-04':[(51,33,24,62),(75,33,24,31),(75,65,14,30),(90,65,9,17)],'s03-06':[(62,12,10,17.8),(83,34,10,17.8),(62,56,10,17.8),(83,79,10,17.8)],'s03-08':[(4,69,30,31),(70,8,30,42),(70,62,20,30)],'s03-09':[(38,43,24,57)],'s06-06':[(45,40,28,60)],'s06-07':[(53,40,23,49)],'s06-08':[(56,8,39,40),(25,51,20,42)],'s06-09':[(42,41,24,49)]}
for sid,bounds in photos.items():
 s=data['p080/'+sid];s['elements']=[e for e in s['elements'] if e['kind']!='image'];s['elements']=[photo(*q) for q in bounds]+s['elements']
 if sid=='s03-06':
  for e in s['elements']:
   if e['kind']=='image':e['clipPath']='ellipse(50% 50% at 50% 50%)'
add('p080','s02-02',[tx('BRAND DESIGN',5,57,24,24,'Michroma',color=W),tx('PACKAGE B',32,57,22,24,'Michroma',color=W),tx('ABOUT OUR\nCREATIVE\nDESIGN',11,81,21,24,color=W),tx('PROJECT NAME\nPROJECT PROPOSAL / 2022\nWWW.PROJECT.NET',32,80,23,17,color=W),para(61,15,30,17,W,4),tx('START\nEXPLORE',67,32,20,21,'Michroma',color=W,align='center'),ic(74,43,4,5,'ArrowDown',W),chip('01',5,44,7,6,25,'transparent',W,radius=40),chip('02',32,44,7,6,25,'transparent',W,radius=40),para(5,64,22,13,W,4),para(32,64,22,13,W,4)])
add('p080','s02-03',[tx('Subtitle_   •   Creative direction\n               •   Brand design\n               •   Strategic thinking',51,55,24,14,color=W)])
add('p080','s02-04',[rule(60,23,40),rule(60,41,40),rule(60,59,40),rule(60,78,40),tx('Subtitle_',15,73,12,18,color=W),tx('4.40%',10,78,14,49,color=W,align='right'),para(4,85,22,14,W,3)])
add('p080','s02-05',[tx('GOOD IDEA\nMAKES EVERYTHING\nIS BETTER',48,82,27,24,color=W),box(76,83,6,5,W,'50%'),box(83,83,6,5,'#736550','50%'),box(90,83,6,5,'#db823b','50%')])
add('p080','s02-06',[tx('ADDRESS',50,67,18,17,weight=700,color=W),tx('2345 Street Name City Name\nCountry Name 00',50,71,22,14,color=W),tx('PHONE',77,67,17,17,weight=700,color=W),tx('+00 123 4567890\n+00 123 456789',77,71,20,14,color=W),tx('SOCIAL MEDIA',50,83,20,17,weight=700,color=W),tx('www.socialmedia.com\nwww.portfolio.com',50,87,22,14,color=W),tx('WEB',77,83,18,17,weight=700,color=W),tx('www.company.com\nwww.example.com',77,87,20,14,color=W)]+[ic(x,y,3,5,icon,W,1) for x,y,icon in [(45,67,'MapPin'),(72,67,'Phone'),(45,83,'Facebook'),(72,83,'Mail')]])
add('p080','s03-01',[para(47,20,45,14,W,2),para(47,28,45,14,W,2)])
for sid in ['s03-02']:
 s=data['p080/'+sid]
 s['elements']=[e for e in s['elements'] if not(e['kind']=='text' and e.get('text','').startswith('Lorem ipsum'))]
 add('p080',sid,[para(4,79,25,14,W,5),para(34,73,14,14,W,5),para(55,73,15,14,W,5)])
add('p080','s03-03',[para(47,86,16,12,W,4),para(65,86,16,12,W,4),para(83,37,15,12,W,4)])
add('p080','s03-04',[chip('BRAND IDENTITY',4,42,13,11,12,'transparent',W,radius=50),chip('PRODUCT NAME',17,42,13,11,12,'transparent',W,radius=50),chip('WHO WE ARE',30,42,13,11,12,'transparent',W,radius=50),tx('Brand Name\nOur Studio',6,60,16,24,'Michroma',color=W),tx('GOOD IDEA MAKES\nEVERYTHING IS BETTER',25,59,25,23,color=W),para(25,71,23,15,W,5),tx('BRANDING        PHOTO        PROPOSAL',55,24,41,13,color=W)])
add('p080','s03-05',[tx('Subtitle_',63,42,23,17,color=W),tx('Valerie Warrington',63,79,26,35,'Kaushan Script',color=W)])
add('p080','s03-06',[para(78,22,19,13,W,2),para(58,45,19,13,W,2),para(78,66,19,13,W,2),para(58,90,19,13,W,2)])
add('p080','s03-07',[tx('Sales Associate, Big Apple Bookstore, New York\nSeptember 2022 – June 2023',58,51,38,15,color=W),tx('Bachelor of Communication, New York University\nAugust 2023 – June 2030',58,80,38,15,color=W)])
add('p080','s03-08',[tx('GOOD IDEA MAKES\nEVERYTHING IS BETTER',42,42,27,24,color=W),para(42,52,26,14,W,4),tx('Subtitle_',42,73,21,18,color=W),tx('4.40%',42,78,20,49,color=W),para(42,87,21,13,W,2)])
for i,label in enumerate(['HOW WE WORK','PROJECT NAME','PROJECT DATE']):add('p080','s03-09',[tx(label,71,23+i*26,27,24,'Michroma',color=W),para(71,29+i*26,25,15,W,3),rule(62,43+i*26,38)])
for sid in ['s06-01','s06-02']:
 color=K if sid=='s06-02' else W
 add('p080',sid,[tx('ON THE OTHER HAND WE\nWORK WITH RIGHTEOUS\nDESIGN AND CREATIVE IDEAS',49,91,26,12,color=color),para(80,83,17,14,color,4)]+[{**chip(v,49+i*2.6,77,2,3.56,12,'transparent',color,radius=50),'border':'1px solid '+color} for i,v in enumerate(['O','P','T'])])
 for e in data['p080/'+sid]['elements']:
  if e['kind']=='text' and e.get('x',0)>43:e['color']=color
add('p080','s06-03',[tx('Virginia Kelly',68,75,29,30,color=W,align='center'),tx('CEO',71,82,23,21,color=W,align='center')])
add('p080','s06-04',[para(45,43,46,14,W,4),para(45,61,46,14,W,3),para(45,77,46,14,W,2),tx('Virginia Kelly',45,85,25,35,'Kaushan Script',color=W)])
add('p080','s06-05',[tx('SELECTEDWORK/\nDESIGN PORTFOLIO\nFOR 2030',52,64,25,21,color=W),tx('Virginia Kelly',52,77,27,35,'Kaushan Script',color=W)])
add('p080','s06-06',[tx('Virginia Kelly',4,86,29,23,color=W),para(4,90,30,12,W,2),tx('Signature',79,79,18,17,color=W),tx('Virginia Kelly',79,83,20,29,'Kaushan Script',color=W)])
add('p080','s06-07',[tx('Subtitle_',80,61,17,18,color=W),tx('4.40%',80,67,19,49,color=W),tx('GOOD IDEA\nMAKES\nEVERYTHING IS\nBETTER',80,78,19,24,color=W)])
add('p080','s06-08',[para(56,67,37,14,W,5),tx('•  Design presentation and proposals\n•  Web, graphic and creative direction\n•  Materials and development\n•  Visual identity and style\n•  Strategic design',56,80,38,14,color=W)])
for i in range(4):add('p080','s06-09',[tx(str(i+1)+'.',73,50+i*13,6,27,'Michroma'),para(78,50+i*13,19,13,'#333',3)])
for target,source in [('s08-01','s06-01'),('s08-02','s03-02'),('s08-03','s03-03'),('s08-04','s02-03')]:data['p080/'+target]=copy.deepcopy(data['p080/'+source])
# MINI deck: explicitly rebuild flat panels, ordinary icons and charts; remove irregular seed outlines.
for key,s in data.items():
 if not key.startswith('p081'):continue
 sid=key.split('/')[1];es=[e for e in s['elements'] if e['kind'] in ['text','icon']];g=[];s['background']='#fcfcfb' if sid!='s03-02' else '#353533'
 def sub(x,y,w,col='#222',icon='Box',tile=False):
  return [box(x,y,5,8.9,S if tile else K,'50%' if not tile else 0),ic(x+1,y+1.8,3,5.3,icon,'#222' if tile else W),tx('Subtitle Here',x+8,y, w-8,15,weight=700,color=col),para(x+8,y+4,w-8,14,col,3)]
 if sid in ['s02-02','s04-02']:g=[box(46,37,54,63,S),box(10,37,11,19.5,K),ic(13,42,5,9,'FolderClosed',W)]
 if sid=='s02-03':
  g=[box(8.5,0,28,100,S)]+ring(67,32,27,48,[58,23,12,7],[S,K,'#aaa','#eee'],0)
  for j in range(6):g += [rule(39,85-j*10,23,'#eee')]
  for i,(h,c) in enumerate([(20,K),(20,S),(30,K),(50,'#aaa')]):g += [box(42+i*5.6,85-h,1.8,h,c)]
  es += sub(11,37,23,icon='HandCoins')+sub(11,68,23,icon='Lightbulb')+[tx('1st Qtr   •   2nd Qtr   •   3rd Qtr   •   4th Qtr',68,84,28,14)]
 if sid in ['s02-04','s04-03']:
  g=[box(8.5,0,39,100,S),photo(28,33,38,60)];es=[e for e in es if not(e.get('text')=='Details :' and e.get('x',0)<35) and not(e.get('text','').startswith('Lorem ipsum') and e.get('x',0)<35)]
  es += sub(70,54,27,icon='FolderClosed',tile=True)+sub(70,72,27,icon='Network',tile=True)
 if sid=='s02-05':g=[photo(30,30,67,62)]+ring(40,38,9,16,[75,25],['#aaa','#deddd6'],.8)+ring(78,33,9,16,[75,25],['#aaa','#deddd6'],.8)+ring(59,61,9,16,[75,25],['#aaa','#deddd6'],.8);es += sub(11,35,18,icon='FolderClosed',tile=True)+sub(11,67,18,icon='Network',tile=True)
 if sid=='s02-06':
  s['background']=S;g=[{**box(21,22,58,55,K),'border':'2px solid white'}]
  for e in es:
   if e.get('text','').startswith('Thank You'):e.update(x=25,y=29,w=50,h=42,size=75,color=W,align='center')
 if sid in ['s03-01','s03-02']:g=[photo(41,25,55,67)]
 if sid=='s03-03':
  g=[photo(30,14,39,49),box(69,39,28,55,S),box(42,63,55,31,S)]
  for e in es:
   if e.get('text')=='Introduction':e['y']=30
   if e.get('text','').startswith('“This presentation'):e.update(x=48,y=72,w=45,size=30,weight=600,h=20)
   if e.get('text','').startswith('Minimal\nPresentation'):e.update(x=72,y=50,w=22,size=27)
 if sid=='s03-04':g=[box(33,0,32.5,100,'#eeece4'),photo(44,40,21.5,52)];es += [tx('Details :',11,64,26,16,weight=700),para(11,69,26,14,lines=3),para(11,77,29,14,lines=3)]+[rule(68,50+i*7,26,'#ddd') for i in range(6)]
 if sid in ['s03-05','s04-01']:
  g=[photo(38,32,20.5,55),photo(27.5,58,9.5,18),box(24,78,13.5,22,S),ic(27,82,8,14,'MessagesSquare','#222')];es += sub(62,45,17,icon='FolderClosed',tile=True)+sub(81,45,17,icon='Network',tile=True)+[tx('$47K',62,82,15,36,weight=700),tx('72K',81,82,13,36,weight=700)]
 if sid=='s03-06':
  g=[box(32,0,31,100,S),photo(63,14,32,86),{**box(11,45,14,25,S,20),'rotate':45},{**box(11,73,14,25,S,20),'rotate':45}]
  for e in es:
   if e.get('text','').startswith('Minimal\nAbout'):e.update(x=40,y=13,w=22)
   if e.get('text')=='Details :':e.update(x=40,y=63,w=22)
   if e.get('text','').startswith('Lorem ipsum') and e['x']<35:e.update(x=40,y=70,w=22)
 if sid=='s03-07':g=[photo(31,27,22,66),box(55,27,41,66,K)];es += sub(61,37,32,W,'Box')+sub(61,54,32,W,'Network')+sub(61,72,32,W,'PanelsTopLeft')
 if sid=='s03-08':g=[box(38.5,16,58,74,S)];es += sum((sub(x,y,25,icon=icon) for x,y,icon in [(42,29,'Box'),(69,29,'PanelsTopLeft'),(42,65,'Network'),(69,65,'PieChart')]),[])+[rule(51,52,7,K),rule(78,52,7,K)]
 if sid=='s03-09':
  g=[box(33,32,20,55,K,48),{**box(55,32,19,55,W,48),'border':'1px solid #eee'},box(76,32,20,55,S,48)]
  for e in es:
   if e.get('text')=='$47K':e['color']=W
   if e.get('x',0)>=34 and e.get('x',0)<54:e['color']=W
   if e.get('x',0)>=55 and e.get('text')=='Your Title Text Here':e['w']=18
 if sid in ['s04-04','s05-08']:
  g=ring(12,35,23,41,[13,27,13,23,24],[K,S,K,'#eee','#aaa'],.76)+[photo(58,26,14,25),photo(44,55,28,45),box(73,26,18.5,58,S)]
  for e in es:
   if e.get('text')=='$11.37':e.update(x=17,y=54,w=14,size=33,align='center')
   if e.get('text')=='$47K':e.update(x=76,y=35,w=15)
   if e.get('text')=='126K':e.update(x=76,y=59,w=15)
  es += [tx('Billion',17,50,14,15,align='center'),tx('Million',76,31,16,13),tx('Million',76,57,16,13),para(76,43,15,13,lines=3),para(76,67,15,13,lines=3),rule(74,53,16,'#aaa'),tx('Details :',12,83,24,16,weight=700),para(12,88,25,13,lines=2)]
 if sid=='s05-01':g=[photo(52.5,29,24,63),photo(78,29,18.5,42),box(78,74,18.5,18,S)];es += [tx('Minimal\nPresentation\nTemplate',79,76,16,27,weight=700,align='right')]
 if sid=='s05-02':
  g=[box(18,29,75,71,S),photo(18,29,27,63),box(53,48,7.5,13.3,K,'50%'),ic(55,52,3.5,6.2,'Network',W),rule(60,48,25),path([[57,64],[57,79]],K,1)]
  es += [tx('Write Your Subtitle\nText Here',62,50,26,16,weight=700),para(62,60,25,15,lines=5)]
 if sid=='s05-03':
  for y in [29,66]:
   for x in [16,38,60,82]:g += [{**photo(x,y,10,17.8),'clipPath':'ellipse(50% 50% at 50% 50%)'}]
 if sid=='s05-04':g=[photo(47.5,14,45,32),photo(38,49,24,38),photo(63.5,49,14,38)];es += [tx('70.01K',80,55,15,36,weight=700),para(80,62,15,13,lines=2),tx('10.1K',80,74,15,36,weight=700),para(80,81,15,13,lines=2)]
 if sid=='s05-05':
  for i,icon in enumerate(['Network','PieChart','Layers','PanelsTopLeft','Globe']):g += [{**box(11+i*18,42,8,14.2,'transparent'),'border':'1px solid #deddd7'},ic(13+i*18,45,4,7.1,icon,'#d0d0c8')]
  for e in es:
   if e.get('size',0)>=24 and e.get('y',0)>40:e['y']+=12
 if sid in ['s05-06','s05-09']:
  es=[e for e in es if e.get('text') in ['Design','Minimal','04.09 – 03.07','Timeline']];g=[path([[50,0 if sid=='s05-09' else 35],[50,99]],'#ddd',1)]
  entries=[(2025,54,'150M',False),(2026,80,'126K',True)] if sid=='s05-06' else [(2027,21,'23K',True),(2028,53,'69M',False),(2029,84,'47K',True)]
  for year,y,value,right in entries:
   g += [{**box(47,y-4,6,10.6,K if year%2==0 else S,9),'rotate':45},ic(48,y-2,4,7.1,'Lightbulb' if year%2 else 'HandCoins',W if year%2==0 else K)]
   es += [chip(str(year),56 if not right else 34,y-2,10,7,35,W,radius=30),tx(value,35 if not right else 59,y-3,12,32,weight=700),tx('Your Title Text Here',20 if not right else 67,y-4,14,12,weight=700),para(20 if not right else 67,y,14,12,lines=3)]
  es += [tx('Start' if sid=='s05-06' else 'End',45,30 if sid=='s05-06' else 95,10,18,weight=600,align='center')]
 if sid=='s05-07':
  g=[box(11,28,58,67,K)]
  for i in range(8):
   x=11+(i%4)*14.5;y=32+(i//4)*29;g += [box(x,y,14.5,29,S if (i+i//4)%2==0 else K)]
  g += ring(78,41,12,21.3,[75,25],['#aaa','#eee'],.9)+ring(78,71,12,21.3,[75,25],[K,'#eee'],.9)
  es += [tx('Positive Feedback',78,34,17,16),tx('Positive Feedback',78,65,17,16)]
 # Page-sized native gradient becomes a flat white/beige field; sidebar stays a simple rule.
 g += [path([[3.5,0],[3.5,100]],'#deddd6',1)]
 s['elements']=g+es
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(data,ensure_ascii=False))
print('28 editorial and 28 MINI cells corrected from individual comparison')
