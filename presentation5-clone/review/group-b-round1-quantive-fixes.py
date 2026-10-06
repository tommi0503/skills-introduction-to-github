from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
data=json.loads((ROOT/'src/decks/group-b-data.json').read_text());W='#fff';A='#292181';B='#4b4ecb';C='#8372c6';HL='#baacd6'
def card(x,y,w,h,label,color=A,size=22):return [box(x,y,w,h,color,20),tx(label,x+2,y+3,w-4,size,weight=600,color=W),para(x+2,y+9,w-4,14,W,3)]
def summary(x,y,w,h):return [rounded(photo(x,y,w,h),20)]
def rounded(e,r):return {**e,'radius':r}
def rule(x,y,w,c='#eee'):return path([[x,y],[x+w,y]],c,1)
def chart(x,y,w,h,bar=False):
 g=[{**box(x,y,w,h,W,38),'border':'1px solid #eee'}]
 for i in range(6):g += [rule(x+4,y+5+i*(h-10)/5,w-7)]
 if bar:
  for i,v in enumerate([.5,.8,.35,.28]):g += [box(x+6+i*(w-10)/4,y+h-7-v*(h-13),3.5,v*(h-13),[A,A,B,C][i])]
 else:g += [path([[x+5,y+9],[x+w*.3,y+h-8],[x+w*.47,y+8],[x+w*.67,y+h-8],[x+w*.86,y+12]],A,3)]
 return g
for key,s in data.items():
 if not key.startswith('p091'):continue
 sid=key.split('/')[1];es=[e for e in s['elements'] if e['kind'] in ['text','chip']];g=[];s['background']=W
 for e in es:
  if e['kind']=='text' and 45<e.get('size',0)<95:e['size']*=.84
  if e['kind']=='chip':e['h']=5;e['radius']=40
  if e.get('text')=='Contact Us    About Us    Home':e['y']=7
 # Uniform actual source navigation. Cover pages intentionally omit this nav.
 es=[e for e in es if not(e.get('text') in ['Contact Us','About Us','Home'])]
 es += [tx('Contact Us       About Us       Home',59,7,28,15)]
 g += [box(91,6,4.5,8,B,'50%'),ic(92.2,8,2,3.6,'Menu',W,2)]
 def highlight(x,y,w,h=8):return box(x,y,w,h,HL,5)
 if sid=='s02-01':
  g += summary(8,12,21,77)+summary(32,36,21,64)+card(48,68,21,20,'Tools user',A)+card(71,68,22,20,'Platforms used',B)+[box(60,53,5,9,A,12),ic(61,55,3,5,'MessagesSquare',W),highlight(83,29,10)]
  es += [tx('Platforms used',59,24,32,20),para(59,41,34,16,lines=3),tx('Customer Reviews',78,55,18,16,weight=700),tx('with trusted association',78,60,18,13)]
 if sid=='s02-02':
  g += summary(8,34,22,31)+summary(31,34,39,31)+summary(71,34,22,31)+[box(8,77,22,5,A),box(30,77,41,5,B),box(71,77,22,5,C),highlight(55,17,20)]
  es += [para(14,27,72,14,lines=1)]
 if sid=='s02-03':
  g += summary(10,32,44,42)+card(10,78,20,14,'Investing',A,18)+card(32,78,20,14,'Finance',B,18)+card(54,78,20,14,'Budgeting',C,18)+[highlight(59,35,29)]
  es += [tx('Use of funds',59,23,33,18),para(59,47,32,16,lines=4),{**chip('Learn More',59,64,10,5.5,14,B,W,radius=40)}]
 if sid in ['s02-04','s03-01']:
  s['background']=A;es=[e for e in es if e.get('text') not in ['Contact Us       About Us       Home']];g=[]
  label='Thank You' if sid=='s02-04' else 'Business Plan';es=[e for e in es if e.get('text')!=label and e['kind']!='chip'];es += [tx('Quantive',41,32,22,29,weight=700,color=W,align='center'),tx(label,10 if sid=='s03-01' else 20,39,80 if sid=='s03-01' else 64,115,weight=700,color=W,align='center'),chip('Learn More',38,60,24,8,20,W,'#555',weight=600,radius=10)]
  g += [highlight(61 if sid=='s03-01' else 56,37,26 if sid=='s03-01' else 23,20)]
 if sid=='s03-02':
  g += sum((summary(8+i*21,35,19,42) for i in range(4)),[])+[highlight(58,17,14)]
  es += [para(17,27,65,14,lines=1)]
  for i in range(4):es += [tx('Company team member',9+i*21,88,19,13,align='center')]
 if sid=='s03-03':
  es=[e for e in es if not e.get('text','').startswith('Lorem ipsum')]
  for e in es:
   if e.get('text','').startswith('Brief overview'):e.update(x=7,y=28,w=35,size=50,h=20)
  g += summary(44,18,27,71)+card(6,61,21,20,'Vision Statement',A,20)+card(28,61,21,20,'Mission Statement',B,20)+[highlight(20,37,17)]
  es += [tx('Executive Summary',7,23,34,18),para(7,46,32,16,lines=3),tx('Achieve KPI',75,41,22,18,weight=700),para(75,46,19,14,lines=3),tx('Get 100 million',75,68,22,18,weight=700),para(75,73,19,14,lines=3),ic(75,31,4,7,'Network',A),ic(75,58,4,7,'Users',B)]
 if sid=='s03-04':
  g += card(6,12,20,17,'Investing',A,18)+card(28,12,20,17,'$44.588',B,33)
  for j in range(7):g += [rule(9,85-j*8,37)]
  for i,v in enumerate([42,33,25,17]):g += [box(11+i*9.4,85-v,4.5,v,[A,B,C,HL][i])];es += [tx('Category '+str(i+1),8+i*9.4,88,9,12,align='center')]
  g += [highlight(71,28,21)]
  for i,icon in enumerate(['ShieldCheck','Wrench','Grid2X2']):g += [box(53,50+i*13,5,9,[A,B,C][i],8),ic(54,52+i*13,3,5,icon,W)]
  es += [tx('What customer problems are you solving?',53,20,42,18),para(53,38,40,16,lines=3)]
 if sid=='s03-05':
  g += [{**box(6,15,47,76,W,38),'border':'2px solid #eee'},rule(9,34,41),highlight(58,41,24)]
  es += [tx('Department',11,29,18,21,weight=700),tx('Budget',30,29,10,21,weight=700),tx('Actual',42,29,10,21,weight=700)]
  for i,label in enumerate(['Marketing','HR','Research']):es += [tx(label,12,41+i*10,17,18),chip('$45.78',29,40+i*10,8,5,17,'#f8f8f8'),chip('$16.76',40,40+i*10,9,5,17,'#f8f8f8')]
  for i,value in enumerate([46,63]):g += [rule(11,76+i*9,37,'#ddd'),rule(11,76+i*9,value*.37,A),box(10+value*.37,74.5+i*9,1.6,2.84,A,'50%')];es += [tx(str(value)+'%',43,72+i*9,8,14),tx('Your Text Here',11,72+i*9,25,14)]
  es += [tx('Pricing strategy',58,27,32,18),para(58,52,34,16,lines=3),para(58,74,18,14,lines=2),para(80,74,17,14,lines=2)]
 if sid=='s03-06':
  g += summary(0,54,17,16)+summary(88,54,12,16)
  for x,y,w,label,col in [(22,54,20,'Specific',A),(44,54,20,'Measurable',A),(66,54,20,'Achievable',B),(33,74,20,'Relevant',HL),(55,74,20,'Time based',C)]:g += card(x,y,w,16,label,col,20)
  es += [tx('Objectives',40,17,23,17,align='center'),para(14,32,76,15,lines=2),chip('Long-term',43,42,10,5,14,B,W,radius=30),chip('Short-term',54,42,10,5,14,C,W,radius=30)]
 if sid=='s03-07':
  es=[e for e in es if not(e.get('text','').startswith('Lorem ipsum'))]
  g += card(6,20,26,69,'Vision',A,29)+card(69,20,26,69,'Mission',B,29)
  es=[e for e in es if e.get('text') not in ['Vision','Mission']]
  es += [tx('Vision',9,47,21,25,weight=600,color=W),para(9,54,20,18,W,6),tx('Mission',74,47,19,25,weight=600,color=W),para(72,54,19,18,W,6),para(38,60,25,16,lines=3),chip('Learn More',9,79,10,6,16,W,radius=40),chip('Learn More',82,79,10,6,16,W,radius=40),chip('Learn More',46,72,10,6,16,B,W,radius=40),highlight(43,51,16)]
  for e in es:
   if e.get('text','').startswith('Vision &'):e.update(x=38,y=40,w=28,size=53,h=20,align='center')
 if sid=='s03-08':
  g += summary(28,10,14,62)+summary(36,27,16,63)+[highlight(74,37,20)]
  for i,(x,y,label,col) in enumerate([(57,59,'Online purchase',A),(76,59,'Benefits customers',W),(57,76,'Working flexibility',W),(76,76,'Team collaboration',B)]):
   g += [box(x,y,18,15,col,15),ic(x+7,y+2,4,5,['Users','Asterisk','Circle','Grid2X2'][i],W if col!=W else A)];es += [tx(label,x+1,y+9,16,13,weight=600,color=W if col!=W else '#111',align='center')]
  es += [tx('Social app for business',7,22,21,18,weight=600),tx('Reduce bad fatigue',7,37,21,18,weight=600)]
 if sid=='s03-09':
  g += summary(7,56,44,31)+chart(25,29,23,39)+[highlight(68,37,13),box(58,66,7,12,A,18),ic(60,69,3,6,'MessagesSquare',W)]
  es += [tx('Market analysis',58,29,32,18),para(58,48,33,16,lines=3),tx('Customer Reviews',78,70,18,17,weight=700)]
 if sid=='s03-10':
  g += [box(28,0,12,48,C),photo(22,12,40,88),highlight(62,29,30),box(49,71,43,16,C,22),photo(52,74,13,10)]
  es=[e for e in es if e.get('text')!='Customer'];es += [tx('Demographics',7,21,17,18,weight=600),tx('Psychographics',7,38,17,18,weight=600),tx('Target persona',62,19,30,18),tx('Customer Base',67,74,20,19,weight=600,color=W),chip('View More',81,77,9,5,14,W,radius=3)]
  for e in es:
   if e.get('text','').startswith('Customer\nsegment'):e.update(x=62,y=23,w=35,size=51)
 if sid=='s03-11':
  for x,y,icon,col in [(46,33,'TrendingUp',A),(57,53,'Shield',B),(46,74,'Lightbulb',C),(34,53,'Network',HL)]:g += ring(x,y,8,14.2,[100],[col],.82)+[ic(x+2,y+3.6,4,7,icon,col),path([[50,59],[x+4,y+7]],'#aaa',1)]
  g += [ic(48,57,4,7,'Briefcase','#333'),highlight(8,20,18)]
  es += [tx('SWOT',8,10,30,18)]
  for e in es:
   if e.get('text','').startswith('Competitive'):e.update(x=8,y=14,w=33,h=18,size=51)
   if e.get('text')=='Strengths':e.update(x=60,y=30,w=28)
   if e.get('text')=='Weaknesses':e.update(x=72,y=54,w=25)
   if e.get('text')=='Threats':e.update(x=14,y=55,w=17)
   if e.get('text')=='Opportunities':e.update(x=26,y=82,w=19)
  es += [tx('Competition',62,81,31,19,weight=700),para(62,86,31,14,lines=2)]
 if sid=='s03-12':
  g += ring(36,33,28,49.8,[25,25,25,25],[B,A,B,A],.48)+summary(0,47,25,24)+summary(75,47,25,24)+[highlight(52,17,24),ic(48,52,5,9,'MessagesSquare','#666')]
  es=[e for e in es if e.get('text','').startswith('STEP')==False]
  for x,y,n in [(34,32,'01'),(61,32,'02'),(34,78,'03'),(61,78,'04')]:es += [tx('STEP\n'+n,x,y,7,27,color=C,align='center')]
  for x,y,label in [(13,31,'Fast onboarding'),(73,31,'Automatic insights'),(11,77,'Seamless integrations'),(71,77,'Optimize productivity')]:es += [tx(label,x,y,20,17,weight=700),para(x,y+5,20,14,lines=2)]
 if sid=='s03-13':
  s['background']=A
  for x,y,label in [(18,15,'CEO & Founder'),(18,38,'Lead Manager'),(44,26,'Chief Officer'),(59,48,'Operations'),(18,74,'Sales Manager'),(44,74,'Chief Advisor')]:g += [{**photo(x,y,8,14.2),'clipPath':'ellipse(50% 50% at 50% 50%)'},box(x-12,y+3,14,5,'#7fb5d4',30)];es += [tx(label,x-11,y+4,13,12,weight=600,color=W)]
  g += [path([[27,21],[29,21],[29,45],[27,45]],C,1),path([[31,33],[43,33]],C,1),path([[54,33],[55,33],[55,57]],C,1),path([[27,81],[29,81],[29,90]],C,1),path([[54,81],[55,81],[55,63]],C,1),highlight(75,30,18)]
  es += [tx('Description',27,58,27,19,weight=700,color=W)]
  for e in es:
   if e.get('text')=='Contact Us       About Us       Home':e['color']=W
 if sid=='s03-14':
  g += [path([[9,25],[9,85]],'#888',1),box(45,52,18,34,A,20),ic(50,55,8,13,'Wrench',W)]+summary(65,52,35,34)+[highlight(69,27,14)]
  for i in range(3):g += [box(7,36+i*17,4,7.1,[B,C,HL][i],'50%')];es += [chip(str(i+1),7,36+i*17,4,7.1,18,[B,C,HL][i],W,radius='50%')]
  es += [tx('Capabilities',47,67,15,22,weight=600,color=W,align='center'),para(47,74,14,14,W,3),tx('Day-to-day operations',45,19,42,18),para(45,37,43,16,lines=3)]
 if sid=='s03-15':
  g += [photo(22,44,52,48),box(6,63,28,18,A,12)]+chart(68,43,23,30)+[highlight(17,17,17),ic(9,67,4,7,'Laptop',W)]
  es += [tx('Social Media',16,67,17,22,weight=600,color=W),para(16,73,17,13,W,2),tx('Sales process',7,10,31,18),para(7,31,40,16,lines=2),chip('Learn More',7,40,10,5,14,B,W,radius=30)]
  for e in es:
   if e.get('text')=='Sales strategy':e.update(x=7,y=16,w=36,size=51)
 if sid=='s03-16':
  g += chart(6,44,59,44,True)+summary(69,44,25,44)+[highlight(26,20,20)]
  es += [tx('Digital marketing',77,20,20,18,weight=600),tx('Paid advertising',77,31,20,18,weight=600),para(7,33,48,16,lines=2),para(40,75,23,14,lines=2)]
  for e in es:
   if e.get('text')=='Marketing strategy':e.update(x=7,y=19,w=50,size=51)
   if e.get('text')=='90%':e.update(x=40,y=62,w=22)
   if e.get('text')=='Content marketing':e.update(x=40,y=69,w=22)
 s['elements']=g+es
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(data,ensure_ascii=False))
print('20 Quantive individual pages rebuilt with semantic charts and cards')
