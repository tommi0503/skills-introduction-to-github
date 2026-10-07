from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
d=json.loads((ROOT/'src/decks/group-b-data.json').read_text());N='#171342';V='#d49afa';C='#bce6ed';L='#ecffa6';R='#ef6b62';W='#fff'
def h(t,x=5,y=8,w=90,size=88,c=N,align='left'):return tx(t,x,y,w,size,'Anton',400,c,align,1.04)
def ph(x,y,w,ht):return {**photo(x,y,w,ht),'radius':30}
def b(x,y,w,ht,c):return box(x,y,w,ht,c,30)
def small(t,x,y,w,c=N):return tx(t,x,y,w,17,weight=600,color=c)
def circle(x,y,w,c):return box(x,y,w,w*1.777,c,'50%')
headers={'s02-01':'REVENUE','s02-02':'STRATEGY','s02-03':'ANALYSIS','s02-04':'APPROACH','s02-05':'SERVICES','s02-06':'TARGET','s02-07':'TEAM','s02-08':'ADVANTAGE','s02-09':'','s03-01':'','s03-02':'VAS','s03-03':'PROBLEM','s03-04':'OPPORTUNITY','s03-05':'SOLUTION','s03-06':'PRODUCT','s03-07':'CORE','s03-08':'TIMELINE','s03-09':'OBJECTIVE'}
for k,s in d.items():
 if not k.startswith('p104/'):continue
 sid=k.split('/')[1];e=[];g=[];s['background']=W
 if sid=='s02-01':
  e=[h('BUSINESS MODEL.',w=62),para(67,11,29,16,lines=3)]
  for i,(t,p,bodytxt,c) in enumerate([('Single Purchase','$15 – 5','One-off template sales\nReady-to-use templates',V),('Product Bundles','$45','Themed packs to increase\naverage order value',C),('Membership','$20/mo','Monthly template drops\nUnlimited download',L)]):x=8+i*29;g += [b(x,27,26.5,78,c),ph(x+1.4,29.5,23.7,39)];e += [h(t,x+2,72,23,34,align='center'),tx(bodytxt.split('\n')[0],x+2,79,23,16,align='center'),tx(p,x+2,85,23,23,weight=700,align='center'),tx(bodytxt.split('\n')[1],x+2,91,23,13,align='center')]
 elif sid=='s02-02':
  e=[h('MARKET & SALES STRATEGY.',12,8,83,86),tx('We’re using a multi-channel strategy to reach, engage, and convert our target customers.',20,24,77,16,align='center')];g=[ph(5,29,44,67),b(54,29,51,29,V),b(54,60,51,36,C)]
  for y,t,lines in [(33,'Go-to-Market Approach',['Attract – Paid ads, SEO, social proof','Engage – Email nurturing, free resources, webinars','Convert – Clear CTAs, limited offers, easy checkout']),(64,'Sales Strategy',['Inbound Sales: Content, SEO, and lead magnets','Affiliate Sales: Building our influencer partnerships','Upsell & Bundles: Increase average order value with','strategic product packs'])]:e += [chip(t,57,y,23,5,16,N,W,radius=30)]
  for y,lines in [(41,['Attract – Paid ads, SEO, social proof','Engage – Email nurturing, free resources, webinars','Convert – Clear CTAs, limited offers, easy checkout']),(73,['Inbound Sales: Content, SEO, and lead magnets','Affiliate Sales: Building our influencer partnerships','Upsell & Bundles: Increase average order value','with strategic product packs'])]:e += [tx('\n'.join('→ '+x for x in lines),58,y,41,16,leading=1.8)]
 elif sid=='s02-03':
  e=[h('COMPETITIVE\nANALYSIS.',w=59),para(65,13,30,16,lines=3)];g=[box(0,72,100,28,R)]
  labels=['COMPETITOR','KEY STRENGTHS','KEY WEAKNESSES'];cols=[['Competitor A','Competitor B','Competitor C','Our Product'],['Established brand, large scale','Low-cost, accessible','Feature-rich','Niche-focused, simple to use'],['Complex, not user-friendly','Limited customization','Overwhelming UX, expensive','Tailored, affordable, fast']]
  for j,c in enumerate([V,C,L]):x=6+j*29.5;g += [b(x,47,29.5,41,c)];e += [chip(labels[j],x+8,50,13.5,4,14,N,W,radius=30)]
  for i in range(5):g += [path([[6,56+i*8],[94.5,56+i*8]],'#777',1)]
  for j in range(3):
   for i,t in enumerate(cols[j]):e += [tx(t,7+j*29.5,58+i*8,27.5,17,weight=700 if i==3 else 400,align='center')]
 elif sid=='s02-04':
  s['background']=N;e=[h('Technology / IP.',w=57,c=W),para(62,12,33,16,W,3)]
  for i,(t,c) in enumerate([('Proprietary template\ndesigns & layouts',V),('Custom design systems\nfor brand scalability',C),('Digital rights management\nfor product protection',L)]):x=6+i*30;g += [b(x,28,28,64,c),ph(x+1.4,30,25.2,46)];e += [tx(t,x+2,80,24,18,weight=600,align='center')]
 elif sid=='s02-05':
  e=[h('FUTURE PLANS.',w=62),chip('Roadmap / Future Plans',78,12,17,5,17,R,W,radius=30)];g=[box(71,0,29,100,L),ph(48,29,52,63)]
  for x,y,t,c,bodytxt in [(4,28,'Q4 2025',V,'Launch subscription\nmodel'),(24,28,'Q1 2026',C,'Expand into\nvideo templates'),(4,63,'Q2 2026',L,'Strategic B2B\nbranding partnerships'),(24,63,'Q3 2026','#d6d6d6','Academy – design\nlearning platform')]:g += [circle(x,y,19,c)];e += [h(t,x+2,y+10,15,32,align='center'),tx(bodytxt,x+2,y+18,15,16,align='center')]
 elif sid=='s02-06':
  e=[h('FINANCIAL PROJECTIONS.',18,8,79,86),chip('3-Year Forecast',44,26,12,4.5,16,N,W,radius=30)]
  for i,(yr,t,c) in enumerate([('2025','$50K revenue (templates + custom\nservices)',R),('2026','$80K revenue (subscriptions &\nexpanded services)',V),('2027','$150K revenue (B2B partnerships +\nacademy)',L)]):x=5+i*30.5;g += [b(x,36,28,68,c),ph(x+1.5,59,25,45)];e += [h(yr,x+2,40,24,40,W if i==0 else N),tx(t,x+2,49,24,15,color=W if i==0 else N)]
 elif sid=='s02-07':
  s['background']=L;g=[box(0,48,100,52,N)];e=[h('OUR TEAM.',36,6,40,83),tx('Our talented and diverse team works together for one purpose—to unlock the\npotential of those around us.',25,23,53,16,weight=600,align='center')]
  for i,(name,job,c) in enumerate([('John McConnell','Head of Strategy & Clients',R),('Harry Pearce','Lead Designer & Technical Advisor',V),('Theo Crosby','Founder & Creative Director',C)]):x=10+i*30;g += [b(x,33,20,39,c),ph(x,33,20,30)];e += [tx(name,x-2,76,24,18,weight=700,color=W,align='center'),tx(job,x-3,80,26,12,color=W,align='center'),para(x-2,87,24,13,W,3)]
 elif sid=='s02-08':
  e=[h('THE ASK.',w=58),tx('Seeking $25,000 in funding to:',71,13,25,18,weight=600)];g=[b(6,27,29,67,V),b(36,27,29,33,C),b(36,62,29,32,L),ph(66,27,29,67)]
  for t,x,y,bodytxt in [('Expand',9,31,'Product catalog (200+\ntemplates)'),('Scale',39,31,'Marketing campaigns\ninternationally'),('Develop',39,66,'SaaS video\nplatform')]:e += [tx(t,x,y,24,29,weight=600),tx(bodytxt,x,85 if t=='Expand' else y+17,23,17)]
 elif sid=='s02-09':
  s['background']=N;g=[b(5.5,14,38,45,V),b(5.5,63,18,30,C),b(25,63,18.5,30,L),ph(49,14,51,79)];e=[h('Let’s chat.',8.5,18,35,95,N),tx('Tell us about your project\nand goals.',9,47,31,25,weight=700),small('VC PARTNERSHIPS',8,66,15),small('vc@slide.deck',8,72,15),small('NEW BUSINESS',8,81,15),small('hello@slide.deck',8,87,15),small('OR JUST SAY HELLO',27,66,15),small('hello@slide.deck\n+1 (512) 228 823\nSan Diego, CA',27,72,15)]
 elif sid=='s03-01':
  g=[b(2,3,54,80,C),b(2,86,54,11,V),ph(58,3,41,94)];e=[h('PITCH DECK.',6,30,48,121),tx('❝ Design That Shapes\n    Brands for the Digital Age',6,60,47,31,weight=700),small('PREPARED BY: DESIGN TEAM',6,91,22),small('BRAND STRATEGY',29,91,15),small('PRESENTATION',46,91,10)]
 elif sid=='s03-02':
  s['background']=N;g=[b(-2,14,40,83,R),b(40,14,27,83,C),b(69,14,27,83,L),ph(41.5,16,24,54),ph(70.5,16,24,54)];e=[h('MISSION\n& VISION.',4,19,34,85,W),h('OUR VISION.',42.5,74,24,36),h('OUR MISSION.',71,74,24,36),para(42.5,83,23,16,lines=3),para(71,83,23,16,lines=3)]
 elif sid=='s03-03':
  e=[h('PROBLEM.',w=55),tx('Small to mid-sized businesses\nstruggle to:',57,12,36,21,weight=600,align='center')];g=[ph(42,27,53,67)]
  for i,(t,c,bodytxt) in enumerate([('Inconsistent Branding',V,'Lack of cohesive visual identity that resonates\nwith users.'),('Limited Resources',C,'Small teams or solo entrepreneurs often lack time\nfor a custom design.'),('Low Engagement',L,'Unpolished visuals fail to drive performance on social\nmedia and other platforms.')]):y=27+i*23;g += [b(-3,y,39,21,c)];e += [tx(t,6,y+4,28,23,weight=700),tx(bodytxt,6,y+10,29,15)]
 elif sid=='s03-04':
  e=[h('MARKET\nOPPORTUNITY.',w=49)];g=[b(5,49,33,56,R),circle(41,36,27,C),circle(68,6,29,V),circle(69,63,23,L)];e += [tx('Data-Driven &\nStraightforward',8,53,29,33,color=W)]
  for t,x,y,w,subtxt in [('$7B+',70,17,25,'Total\nAddressable Market'),('$5B+',43,46,23,'Serviceable\nAvailable Market'),('$5B+',71,73,19,'Serviceable\nAvailable Market')]:e += [h(t,x,y,w,57 if w>20 else 40,align='center'),tx(subtxt,x,y+12,w,19,weight=700,align='center'),tx('Revenue potential we can\nserve based on our strategy\nand region.',x,y+21,w,14,align='center')]
 elif sid=='s03-05':
  s['background']=N;e=[h('SOLUTION.',w=58,c=W),tx('●  HOW WE SOLVE IT',76,12,23,23,weight=700,color=W)];g=[ph(-2,27,58,64)]
  for i,(t,c) in enumerate([('Maintain Consistency, On-Brand Content',V),('Save Time & Resources',C),('Elevate Their Online Presence',L)]):y=31+i*20;g += [circle(51,y-1,9,c),b(62,y,32,16,c)];e += [chip(f'STEP {i+1}',51,y,9,14,29,c,N,font='Anton',radius='50%'),small(t,65,y+3,28),para(65,y+7,28,15,lines=2)]
 elif sid=='s03-06':
  g=[circle(-29,-14,59,V),circle(81,-35,38,L),ph(6,22,41,56)];e=[h('PRODUCT\nOVERVIEW.',56,17,41,86),chip('Not Just a Tool—A Solution',56,52,28,6,18,C,N,weight=700,radius=30),tx('→ Slide-based Instagram template packs\n→ Custom brand kits (logos, typography, palettes)\n→ Social media content calendars\n→ Easy-to-edit assets for non-designers',56,65,41,21,leading=1.7)]
 elif sid=='s03-07':
  e=[h('CORE VALUES.',w=40),para(42,12,20,16,lines=3)];g=[ph(5.5,25,56,68)]
  for i,(t,c) in enumerate([('Purpose-Driven',V),('Integrity',C),('Creativity',L),('Growth-Oriented','#ddd')]):y=8+i*22;g += [b(66,y,29.5,19,c)];e += [tx('• '+t,68,y+4,26,23,weight=700),para(68,y+10,26,15,lines=2)]
 elif sid=='s03-08':
  e=[h('HOW IT WORKS.',30,10,60,88)]
  for i,(t,c,week,icon) in enumerate([('Phase 1:\nResearch &\nPlanning',R,'Week 1-2','Search'),('Phase 2:\nDesign &\nDevelopment',V,'Week 3-5','Pencil'),('Phase 3:\nLaunch &\nOptimization',L,'Week 6','Rocket')]):x=5+i*30.5;g += [b(x,36,28.5,53,c),b(x,32,17.5,9,c),circle(x+23,40,4,W),ic(x+24,42,2,3.5,icon,N)];e += [chip(week,x+3,36,8,4,13,N,W,radius=30),tx(t,x+3,49,23,32,weight=700,color=W if i==0 else N),tx('• Market analysis\n• Content strategy\n• Design concept development' if i==0 else '• Template creation\n• Brand kit assembly\n• Feedback & revisions' if i==1 else '• Product upload (website)\n• SEO & keyword optimization\n• Launch marketing (email, social)',x+3,75,24,16,color=W if i==0 else N,leading=1.6)]
 elif sid=='s03-09':
  s['background']=N;e=[h('OUR OBJECTIVE.',w=54,c=W),para(60,11,34,16,W,3)];g=[ph(54,28,40,67)]
  for i,(t,c) in enumerate([('CREATE MEASURABLE VALUE\nTHROUGH PRODUCT/SERVICE\nFOCUS',V),('ADDRESS AN UNDERSERVED MARKET\nWITH INNOVATIVE, USER-CENTRIC\nSOLUTIONS.',C),('DRIVE SUSTAINABLE GROWTH FOR OUR\nSTAKEHOLDERS AND COMMUNITY.',L)]):y=28+i*23;g += [b(6,y,43,21,W),b(13,y,36,21,c)];e += [h(f'0{i+1}.',8.5,y+5,6,40),tx(t,17,y+6,30,19,weight=700)]
 col=W if s['background']==N else N
 if sid not in ['s03-01','s02-09']:e += [tx('SLIDE DECK',5,3,22,13,weight=700,color=col),tx('PRESENTATION',43,3,20,13,weight=700,color=col),tx(headers[sid],84,3,11,13,weight=700,color=col,align='right')]
 else:e += [ic(6,10 if sid=='s03-01' else 5,3,5.3,'Asterisk',N if sid=='s03-01' else R),tx('SLIDE DECK',10,10 if sid=='s03-01' else 6,20,18,weight=700,color=N if sid=='s03-01' else W)]
 s['elements']=g+e
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(d))
