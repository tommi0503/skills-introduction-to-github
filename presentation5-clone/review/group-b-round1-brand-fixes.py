from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
d=json.loads((ROOT/'src/decks/group-b-data.json').read_text());N='#38241d';F='#f3ece2';W='#fff';RULE='#a19c97'
def rule(x,y,x2,y2):return path([[x,y],[x2,y2]],RULE,1.5)
def h(t,x,y,w,c=N,size=50,align='left'):return tx(t,x,y,w,size,'Inter',500,c,align,1.04)
def small(t,x,y,w,c=N,align='left'):return tx(t,x,y,w,20,'Inter',600,c,align)
def body(x,y,w,c='#aaa',lines=3):return para(x,y,w,17,c,lines)
def vertical(t,x,y,c=W):
 e=h(t,x,y,65,c,49);e['h']=8;e['rotate']=-90;return e
for k,s in d.items():
 if not k.startswith('p107/'):continue
 sid=k.split('/')[1];g=[];e=[];s['background']=N if sid in ['s02-02','s02-03','s02-04','s05-01','s05-02','s05-03'] else W;c=W if s['background']==N else N
 g += [rule(0,11,100,11)];e += [small('BRAND PROPOSAL',43,4,22,c,'center'),tx('202\n5',91,3.5,4,18,'Inter',600,c,align='center')];g += [ic(3.5,4,2,3.6,'Menu',c),ic(95,4,2,3.6,'ArrowUpRight',c)]
 if sid=='s02-01':
  g += [photo(13,20,20,72),box(38,22,62,12,F),rule(8,11,8,100),rule(38,11,38,100),rule(38,22,100,22),rule(38,34,100,34),rule(94,34,94,100),ic(47,46,3,5.3,'BadgeCheck'),ic(47,71,3,5.3,'ChartNoAxesCombined'),ic(48,54,1,8,'ArrowDown'),ic(48,79,1,8,'ArrowDown')];e += [h('PRODUCT MOCKUP',46,24,48,size=49,align='center'),body(53,47,36,lines=4),body(53,72,36,lines=4)]
 elif sid in ['s02-02','s05-01']:
  g += [photo(33.5,11,61,89),box(8,46,55.5,54,W),rule(11,50,61,50),rule(33.5,11,33.5,46),rule(94.5,11,94.5,100),rule(64,90,100,90)];e += [small('POWERFUL\nMARKETING SUPPORT',7.5,24,24,W),h('BRAND\nPROPOSAL',11,56,50,N,112,'center'),small('2026',10,95,10),small('PRESENTATION',50,95,12),body(70,74,20,W,4)]
 elif sid in ['s02-03','s05-02']:
  g += [photo(0,11,25.5,89),photo(69.5,56,30.5,44),rule(25.5,11,25.5,100),rule(34.5,11,34.5,100),rule(69.5,11,69.5,100),rule(34.5,56,100,56),rule(69.5,20,100,20),ic(49,19,4,7,'UsersRound',W),ic(50,64,4,7,'Goal',W)]
  e += [vertical('BRAND IDENTITY',28,84),small('Creating Strong Recognition',40,29,24,W,'center'),body(41.5,35,22,'#aaa',3),small('Effective Identity Strategy',41,76,22,W,'center'),body(41.5,82,22,'#aaa',3),small('Unified Brand Communication',72,14,25,W,'center'),body(74,28,22,'#aaa',3),small('Read More...',78,44,18,W)]
 elif sid=='s02-04':
  g += [photo(0,11,67,89),rule(67,11,67,100),rule(98,11,98,100),box(54,49,37.5,40,W),{**box(55.2,51,35,36,W),'border':'1px solid '+RULE},rule(83,23,90,23)];e += [h('THANK',6,59,47,W,145),h('YOU',59,59,31,N,145),small('BRAND PROPOSAL 2026',6,53,34,W),body(74,27,17,'#aaa',3)]
 elif sid=='s05-03':
  g += [photo(5.5,11,35,77),rule(5.5,11,5.5,100),rule(40.5,11,40.5,100),rule(49.5,11,49.5,100),rule(5.5,88,100,88)]
  e += [vertical('BRAND CULTURE',43,83)]
  for y,t in [(25,'A.'),(40,'B.'),(55,'C.'),(70,'D.')]:e += [h(t,57,y,8,W,40),body(64,y,30,'#aaa',2)]
 elif sid=='s05-04':
  g += [photo(0,42,38,58),box(38,42,62,15,F),rule(8,11,8,42),rule(38,11,38,100),rule(0,42,100,42),rule(38,57,100,57),rule(46,23,54,23),rule(46,74,92,74),ic(90,68,2,3.5,'ArrowDownRight')];e += [small('Inspiring\nGrowth\nThrough Shared\nVision',10,27,22),body(46,27,46,lines=2),h('BRAND VISION',48,46,47,size=49,align='center'),small('Building Trust Across Every\nTouchpoint',46,67,42),body(46,79,46,lines=3)]
 elif sid=='s05-05':
  g += [photo(29.5,11,41,68),box(15,79,70,14,F),rule(29.5,11,29.5,79),rule(70.5,11,70.5,79),rule(0,79,100,79),rule(0,93,100,93),rule(15,79,15,93),rule(85,79,85,93)]
  for x,t,subt in [(4,'86,2%','Passion Fuels Innovation'),(75,'92,2%','Principles Lead Forward')]:e += [h(t,x,25,21,size=40,align='center'),small(subt,x,34,21,align='center'),body(x,42,21,lines=6)]
  e += [h('BRAND PHILOSOPHY',26,82,57,size=49,align='center')]
 elif sid=='s05-06':
  g += [box(27,36,45,14,F),photo(27,50,45,50),rule(0,36,100,36),rule(0,50,100,50),rule(27,36,27,100),rule(72,36,72,100)];e += [body(10,19,80,lines=2),h('BRAND GOALS',31,40,38,size=49,align='center'),small('Strengthen Brand Identity',3,42,21,align='center'),small('Elevate Customer Experience',75,42,22,align='center'),h('+750K',4,63,19,size=41,align='center'),h('+125K',78,63,19,size=41,align='center'),body(4,74,19,lines=4),body(78,74,19,lines=4)]
 elif sid=='s05-07':
  g += [photo(56,11,38,61),box(0,72,56,14,F),rule(5,11,5,72),rule(56,11,56,100),rule(94,11,94,100),rule(0,72,100,72),rule(0,86,56,86),rule(13,22,21,22)];e += [body(13,27,36,lines=3),body(13,43,36,lines=2),small('›   More Information...',13,57,32),h('BRAND STORY',11,76,43,size=49),small('Transforming Ideas Into\nLasting Brands',70,77,21,align='right')]
 elif sid=='s05-08':
  g += [photo(51,11,24,68),photo(75,35,25,65),box(0,65,51,14,F),rule(51,11,51,100),rule(75,11,75,100),rule(75,35,100,35),rule(0,65,51,65),rule(0,79,75,79)]
  for y,icon in [(22,'Target'),(34,'Medal'),(46,'ChartNoAxesCombined')]:g += [ic(7,y,3,5.3,icon)];e += [body(12,y,34,lines=2)]
  e += [h('BRAND VALUES',9,69,40,size=49),small('Defining Principles\nFor Lasting Growth',80,20,18),small('Excellence Becomes Our\nDaily Standard',54,88,18,align='center')]
 elif sid=='s05-09':
  g += [box(0,11,100,27,F),rule(0,38,100,38),rule(0,48,100,48),rule(0,93,100,93),rule(33.3,38,33.3,93),rule(66.6,38,66.6,93)];e += [h('MARKETING SUPPORT',24,20,63,size=49)]
  for i,(t,icon) in enumerate([('Powerful Marketing Support','PanelsTopLeft'),('Marketing Support Solutions','MessagesSquare'),('Marketing Support Strategy','Store')]):x=i*33.3;e += [small(t,x+3,41,27,align='center'),body(x+5,67,23,lines=3),small('More Information...',x+9,83,23)];g += [ic(x+14,55,4,7,icon)]
 s['elements']=g+e
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(d))
