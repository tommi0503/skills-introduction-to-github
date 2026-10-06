from pathlib import Path
import json,math,copy
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
data=json.loads((ROOT/'src/decks/group-b-data.json').read_text())
G='#acd82d';W='#fff';K='#303030';O='#eb812e'
def rule(x,y,w,c='#aaa'):return path([[x,y],[x+w,y]],c,1)
def button(x,y,w=9):return {**chip('Learn More',x,y,w,4.4,12,W,radius=30),'border':'1px solid #777'}
def dense_ring(x,y,w,h,inner=.73):
 pts=[]
 for rad,indices in [(1,range(129)),(inner,range(128,-1,-1))]:
  for i in indices:
   a=2*math.pi*i/128;pts.append([x+w/2+rad*w/2*math.cos(a),y+h/2+rad*h/2*math.sin(a)])
 return path(pts,G,0,G)
def add(s,els):data['p069/'+s]['elements']+=els
rings={'s01-01':[(6,-17,32,57),(-11,21,39,69)],'s03-01':[(6,-17,32,57),(-11,21,39,69)],'s01-02':[(-11,-16,35,63),(-2,37,45,80)],'s01-03':[(16,-10,24,43),(-5,53,33,59)],'s01-04':[(-8,-7,29,52),(69,52,30,54)],'s01-06':[(-2,31,22,39),(-5,53,32,57)],'s01-07':[(75,10,31,55),(-6,55,31,55)],'s01-08':[(68,-6,39,69)],'s01-09':[(22,21,13,23),(29,51,16,28)],'s02-01':[(72,50,40,71)],'s02-02':[(-5,-8,31,55),(84,67,23,41)],'s02-03':[(56,6,24,43),(65,39,42,75)],'s02-04':[(-1,32,23,41),(-4,57,24,43)],'s02-05':[(-6,28,28,50)],'s02-06':[(27,46,30,54)],'s02-08':[(-7,27,29,52)],'s04-06':[(77,25,13,23),(85,41,29,51)]}
for sid,rs in rings.items():
 s=data['p069/'+sid];s['elements']=[e for e in s['elements'] if not(e['kind']=='path' and e.get('fill')==G) and not(e['kind']=='box' and e.get('fill') in ['#e6f6d6','#e0f4b8','#e2efbb','#e6f3cf','#e8f3d4','#e8f6cd'])]
 s['elements']=[dense_ring(*r) for r in rs]+s['elements']
# Remove duplicate source OCR and manually reconstructed labels that share one visual region.
for key,s in data.items():
 if key.startswith('p069'):
  seen={};els=[]
  for e in s['elements']:
   text=e.get('text','')
   if e['kind']=='text' and text in seen and abs(e.get('x',0)-seen[text].get('x',0))<4 and abs(e.get('y',0)-seen[text].get('y',0))<5:continue
   if text:seen[text]=e
   els.append(e)
  s['elements']=els
  for e in els:
   if 'italic' in e:e.pop('italic');e['fontStyle']='italic'
# Clear overlapping bodies and restore all four centered CTA chips on the original cards.
s=data['p069/s01-08'];s['elements']=[e for e in s['elements'] if e['kind']!='chip' and not(e.get('text','').startswith('Lorem'))]
for x,y in [(7,31),(30,31),(7,64),(30,64)]:s['elements'] += [para(x,y,19,15,lines=3),button(x,y+12)]
s['elements'] += [para(50,62,40,17,lines=4)]
s=data['p069/s02-03'];s['elements']=[e for e in s['elements'] if e['kind']!='image'];s['elements'][2:2]=[photo(51,18,24,63),photo(70,15,24,62)]
s=data['p069/s02-06'];
for e in s['elements']:
 if e['kind']=='image':e['radius']=0
 if e['kind']=='text' and e.get('size',0)>40:e['fontStyle']='italic'
s=data['p069/s01-07']
for e in s['elements']:
 if e['kind']=='image' and e['w']>90:e['radius']=0
s=data['p069/s02-02']
for e in s['elements']:
 if e.get('text','').startswith('Value\nPositioning'):e['x']=30
 if e.get('text') in ['76.2K','89.7K']:e['size']*=.9
s=data['p069/s02-07'];s['elements']=[e for e in s['elements'] if e['kind']!='path' and not(e.get('text','').startswith('Lorem') and e.get('w',0)>40) and not(e.get('text','').startswith('Data '))]
for y in [39,47,55,63,71,79]:s['elements'] += [rule(8,y,36,'#ddd')]
for i,v in enumerate([14,12,9,6,3,0]):s['elements'] += [tx(str(v),4,38+i*8,3,12,align='right')]
for vals,col in [([54,53,56,43],'#111'),([60,59,64,58],'#777'),([67,72,69,67],G)]:
 pts=[[8+i*12,y] for i,y in enumerate(vals)];s['elements'] += [path(pts,col,2)]+[box(x-.35,y-.62,.7,1.24,col,'50%') for x,y in pts]
for i,v in enumerate([2022,2023,2024,2025]):s['elements'] += [tx('Data '+str(v),6+i*12,84,12,12)]
s=data['p069/s02-09'];s['elements']=[e for e in s['elements'] if not(e.get('text') in ['01','02','03']) and not(e['kind']=='chip')]
for i in range(3):
 x=5+i*31;s['elements'] += [{**box(x,45,6,10.67,W,'50%'),'border':'1px solid #777'},chip('0'+str(i+1),x,45,6,10.67,24,W),button(x,80)]
for target,source in [('s03-02','s01-02'),('s03-03','s01-03'),('s03-04','s01-06'),('s04-01','s01-05'),('s04-02','s01-04'),('s04-03','s01-08'),('s04-04','s01-07'),('s04-05','s01-09')]:data['p069/'+target]=copy.deepcopy(data['p069/'+source]);data['p069/'+target]['id']=target
# Profittera: exact duplicate text removal, stronger rounded headings, and body columns.
for key,s in data.items():
 if not key.startswith('p073'):continue
 els=[];seen=set()
 for e in reversed(s['elements']):
  t=e.get('text','');signature=(e['kind'],t)
  if t and signature in seen:continue
  if t:seen.add(signature)
  if e['kind']=='text' and e.get('size',0)>39 and not(any(z in t for z in ['K','%','$'])):e['weight']=600
  els.append(e)
 s['elements']=list(reversed(els))
for sid,x,y,w,lines in [('s02-01',54,21,35,3),('s02-02',7,78,41,2),('s02-03',7,78,39,3),('s02-04',7,36,39,3),('s02-05',47,70,44,2),('s03-01',7,35,36,2)]:
 s=data['p073/'+sid];s['elements']=[e for e in s['elements'] if not(e.get('text','').startswith('Lorem'))];s['elements']+=[para(x,y,w,16,W if sid=='s02-04' else '#444',lines)]
s=data['p073/s02-03'];s['elements']=[e for e in s['elements'] if e.get('text')!='$25.130'];
for e in s['elements']:
 if e.get('text')=='$25,130':e.update(x=7,y=65,w=27,size=60)
s=data['p073/s02-05']
for e in s['elements']:
 if e.get('text')=='Profit growth':e.update(x=47,y=17)
 if e.get('text')=='$25,130':e.update(x=47,y=54,w=27,size=60)
 if e.get('text')=='Investment':e.update(x=68,y=59,w=8)
s=data['p073/s02-06']
for e in s['elements']:
 if e.get('text')=='Profit growth':e.update(x=52,y=66)
 if e.get('text')=='95.2K':e.update(x=69,y=15)
 if e.get('text','').startswith('Historical'):e.update(x=53,y=75)
 if e.get('text','').startswith('Lorem'):e.update(x=56,y=31,w=34,size=16)
s=data['p073/s02-07']
for e in s['elements']:
 if e.get('text') in ['Our Vision','Our Mission']:e['weight']=600
s=data['p073/s03-02'];
for e in s['elements']:
 if e['kind']=='chip':e['fill']=O if e.get('x',0)<15 else '#f8f8f8';e['color']=W if e.get('x',0)<15 else '#555'
s=data['p073/s03-03']
for e in s['elements']:
 if e.get('text')=='$18.250':e['runs']=[{'text':'$','color':O},{'text':'18.250','color':W}]
s=data['p073/s03-05'];s['elements'] += [box(77,16,4,7,O,'50%'),ic(78,17,2,3.6,'TrendingUp',W),box(77,56,4,7,K,'50%'),ic(78,57,2,3.6,'Target',W)]
s=data['p073/s03-06']
for e in s['elements']:
 if e.get('text')=='95.2K':e.update(x=18,y=16,w=20,size=64)
 if e.get('text')=='Profit growth':e.update(x=7,y=60)
 if e.get('text','').startswith('Lorem') and e.get('x',0)<50:e.update(x=9,y=31,w=31,size=16,align='right');e['text']='Profit growth improves business performance\nand creates opportunities for sustainable\nlong-term success.'
s['elements'] += [box(37,18,4,7,O,'50%'),ic(38,19,2,3.6,'TrendingUp',W)]
s=data['p073/s03-08']
for e in s['elements']:
 if e.get('text')=='95.2K':e.update(x=31,y=13,w=18,size=62)
 if e.get('text')=='Profit growth':e.update(x=7,y=60)
 if e.get('text','').startswith('Lorem'):e.update(x=15,y=28,w=37,size=16,align='right');e['text']='Profit growth supports informed decisions,\nstronger operations and sustainable\nbusiness success.'
s['elements'] += [box(48,14,4,7,O,'50%'),ic(49,15,2,3.6,'TrendingUp',W)]
# A source brand-image icon is a neutral solid placeholder, not a nonexistent Lucide icon.
for e in data['p080/s02-06']['elements']:
 if e.get('icon')=='Facebook':e.clear();e.update(kind='image',x=84,y=90,w=1.5,h=2.67,alt='Social brand icon placeholder')
for key,s in data.items():s['id']=key.split('/')[1]
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
