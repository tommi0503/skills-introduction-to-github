from pathlib import Path
import json,copy,math
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
D=json.loads((ROOT/'src/decks/group-b-data.json').read_text());W='#fff';A='#292181';B='#4b4ecb';C='#8372c6';HL='#baacd6'
def p(s):return D['p091/'+s]
def add(s,els):p(s)['elements']+=els
for key,s in D.items():
 if not key.startswith('p091'):continue
 sid=key.split('/')[1];cover=sid in ['s02-04','s03-01'];es=s['elements'];seen={};out=[]
 for e in reversed(es):
  t=e.get('text','')
  if 'Contact Us' in t:continue
  if t and t in seen and (t=='Quantive' or abs(e.get('x',0)-seen[t].get('x',0))<8 and abs(e.get('y',0)-seen[t].get('y',0))<9):continue
  if t:seen[t]=e
  out.append(e)
 es=list(reversed(out));s['elements']=[e for e in es if e['kind'] in ['box','path','image']]+[e for e in es if e['kind'] not in ['box','path','image']]
 if not cover:s['elements'] += [tx('Contact Us',59,7,8,15),tx('About Us',70,7,8,15),tx('Home',80,7,6,15)]
 if cover:
  s['elements']=[e for e in s['elements'] if e.get('text')!='Quantive'];s['elements'] += [tx('Quantive',47,32,15,27,weight=700,color=W),ic(43,32,3,5.3,'ShieldCheck',W),ic(-3,8,9,16,'Asterisk',C,3),ic(87,-8,20,35.5,'Asterisk',C,3),ic(17,79,5,8.9,'Asterisk',C,2)]
 else:s['elements'] += [ic(5,9,4,7.1,'Asterisk',C,2),ic(91,85,4,7.1,'Asterisk',C,2)]
# Put title emphasis exactly behind its final line/word, and center full-width headings.
for sid in ['s02-02','s03-02','s03-06','s03-12']:
 s=p(sid)
 for e in s['elements']:
  if e['kind']=='text' and e.get('size',0)>40 and any(z in e.get('text','') for z in ['Financial plan','Management team','SMART goals','Unique value']):e.update(x=13,y=17,w=74,align='center')
for sid in ['s03-03','s03-05','s03-07','s03-09','s03-13','s03-14']:
 s=p(sid)
 for e in s['elements']:
  if e['kind']=='box' and e.get('fill')==HL:
   if sid=='s03-05':e.update(x=57,y=40,w=24)
   elif sid=='s03-07':e.update(x=43,y=49,w=16)
   elif sid=='s03-09':e.update(x=67,y=36,w=18)
   elif sid=='s03-13':e.update(x=74,y=31,w=19)
   elif sid=='s03-14':e.update(x=68,y=25,w=11)
# Restore the simple circular pointer icons and card controls visible in the references.
for x,col,icon in [(25,A,'CircleDollarSign'),(61,B,'Flame'),(87,C,'HandCoins')]:add('s02-02',[box(x-2,69,4,7.1,W,'50%'),ic(x-1,70,2,3.55,icon,col),path([[x-1,76],[x,78],[x+1,76]],W,0,W)])
for x,col in [(10,A),(32,B),(54,C)]:add('s02-03',[chip('Learn More',x+1,87,6,3,10,W,A,radius=20),ic(x+17,80,1.6,2.8,'ChevronDown',W),ic(x+17,88,1.6,2.8,'Circle',W)])
s=p('s03-04')
for e in s['elements']:
 t=e.get('text','')
 if t in ['Lack of Trust From Online Audience','Limited Integration Across Tools','Inefficient Workflow Management']:e['x']=60;e['y']-=3;e['w']=35
 if t.startswith('Lorem') and e.get('x',0)>50 and e.get('y',0)>55:e['x']=60;e['y']-=3;e['w']=34;e['size']=14
s=p('s03-07');s['elements']=[e for e in s['elements'] if not(e.get('text') in ['Vision','Mission'] and e.get('y',0)<40) and not(e.get('text','').startswith('Lorem') and e.get('y',0)<40)]
s['elements'] += [ic(9,34,5,8.9,'Eye',W,2),ic(85,34,5,8.9,'Flag',W,2),chip('Long-term',43,33,8,3.5,11,A,W,radius=20),chip('Short-term',52,33,8,3.5,11,'#eee','#444',radius=20)]
s=p('s03-08')
for e in s['elements']:
 if e['kind']=='text' and ('Your service/' in e.get('text','') or 'product overview' in e.get('text','')):e.update(x=57,y=25,w=38,size=49)
 if e.get('text','').startswith('Lorem') and e.get('x',0)>50:e.update(x=57,y=45,w=37)
s=p('s03-09')
for e in s['elements']:
 if e.get('text')=='+45%':e.update(x=68,y=69,w=14,size=38)
 if e.get('text')=='Customer Reviews':e.update(x=78,y=68,w=17,size=15)
 if e.get('text')=='Market analysis':e.update(x=58,y=27)
 if e.get('text','').startswith('Industry size'):e.update(x=58,y=32,w=35,size=49)
s=p('s03-10')
for e in s['elements']:
 if e.get('text','').startswith('Lorem') and e.get('x',0)>50:e.update(x=62,y=41,w=29,size=16)
s['elements'] += [chip('Learn More',62,54,9,4.5,12,A,W,radius=25),chip('Learn More',73,54,9,4.5,12,C,W,radius=25)]
s=p('s03-11');s['elements']=[e for e in s['elements'] if not(e.get('text','').startswith('Lorem'))]
s['elements'] += [para(7,35,31,14,lines=2),para(59,34,24,15,lines=2),para(7,60,22,15,lines=2),para(71,60,24,15,lines=2),para(22,86,22,15,lines=2),para(63,86,31,15,lines=2)]
# Segment separators and actual small symbols in the four-quadrant infographic.
for x,y,icon in [(42,43,'Flame'),(55,43,'User'),(42,66,'Users'),(55,66,'HandCoins')]:add('s03-12',[ic(x,y,3,5.3,icon,W)])
add('s03-12',[path([[50,34],[50,80]],W,7),path([[36,57],[64,57]],W,7)])
s=p('s03-13')
for e in s['elements']:
 if e['kind']=='text' and e.get('text','').startswith('Organizational'):e.update(x=63,y=22,w=34,size=47,align='right')
 elif e.get('text','').startswith('Lorem') and e.get('x',0)>50:e.update(x=64,y=41,w=30,size=15)
 elif e['kind'] in ['image','chip'] and e.get('x',0)<64:e['x']*=.8;e['w']*=.8
 elif e['kind']=='path':
  for q in e.get('points',[]):q['x']*=.8
 elif e.get('text')=='+45%':e.update(x=74,y=76,w=15)
s['elements'] += [chip('Learn More',74,54,9,4.5,12,B,W,radius=20),chip('Learn More',85,54,9,4.5,12,C,W,radius=20)]
s=p('s03-14')
for e in s['elements']:
 if e.get('text','').startswith('Operations plan'):e.update(x=45,y=25,w=40,size=47)
 if e.get('text','').startswith('Lorem') and e.get('x',0)>40 and e.get('y',0)<50:e.update(x=45,y=36,w=49,size=15)
s=p('s03-15');s['elements']=[e for e in s['elements'] if e['kind']!='image'];s['elements'][0:0]=[photo(23,43,31,48),photo(55,35,20,44)]
s=p('s03-16')
for e in s['elements']:
 if e['kind']=='box' and e.get('fill') in [A,B,C] and e.get('x',0)<60 and e.get('w',0)<5 and e.get('y',0)>50:e['x']=12+(e['x']-12)*.4
for key,s in D.items():s['id']=key.split('/')[1]
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(D,ensure_ascii=False,separators=(',',':')))
