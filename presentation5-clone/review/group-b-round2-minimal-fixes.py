from pathlib import Path
import json,copy,math
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
D=json.loads((ROOT/'src/decks/group-b-data.json').read_text());W='#fff';B='#dedbcb';K='#333'
def p(s):return D['p081/'+s]
def add(s,els):p(s)['elements']+=els
for key,s in D.items():
 if not key.startswith('p081'):continue
 es=s['elements'];s['elements']=[e for e in es if e['kind'] in ['box','path']]+[e for e in es if e['kind']=='image']+[e for e in es if e['kind'] not in ['box','path','image']]
 # Source left metadata rail uses separate short lines, a tiny outlined tag, and a dot.
 s['elements']=[e for e in s['elements'] if not(e['kind']=='path' and e.get('fill') is None and len(e.get('points',[]))==2 and e.get('points',[{'x':100}])[0].get('x',100)<5)]
 c='#aaa' if s.get('background')==K else '#ddd'
 s['elements'] += [path([[3.5,0],[3.5,13]],c,1),path([[3.5,20],[3.5,62]],c,1),path([[3.5,87],[3.5,100]],c,1),{**box(1.6,20,4,22,'transparent'),'border':'1px solid '+c},box(3.05,34,.9,1.6,c,'50%')]
 for e in s['elements']:
  t=e.get('text','')
  if e['kind']=='text' and e.get('size',0)>25:e['weight']=600
  if t=='Design':e['y']=31;e['size']=12
  if t=='Minimal':e['y']=80;e['size']=12
  if t=='Details :':e['size']=16;e['weight']=600
  if t=='The\nCreative\npower behind\nart projects':e['size']=27;e['weight']=500;e['w']=21
 # Replace overlapping copies of tiny unreadable prose with a single ordinary paragraph.
 es=s['elements'];kept=[]
 for e in es:
  if e.get('text','').startswith('Lorem'):
   if any(q.get('text','').startswith('Lorem') and abs(e['x']-q['x'])<4 and abs(e['y']-q['y'])<8 for q in kept):continue
   if e.get('x')==11:e['w']=21;e['size']=14;e['text']='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nSed do eiusmod tempor.\n\nStrong ideas build thoughtful\nexperiences and lasting value.'
  kept.append(e)
 s['elements']=kept
add('s02-01',[photo(35,29,24,71),photo(60,29,18,28),photo(60,59,18,41),photo(79,29,18,41),photo(79,72,18,28)])
for e in p('s02-01')['elements']:
 if e.get('text') in ['126K','$47K','Million'] and e.get('x',0)>55:e['x']-=10 if e['x']>80 else 10
 if e.get('text')=='Million' and e.get('x',0)>80:e['x']=86
for e in p('s02-02')['elements']:
 if e.get('text')=='Our\nWorking':e['text']='Our\nWorking';e['y']=12
 if e.get('text')=='Working':e['text']='Our\nWorking';e['y']=12
 if e['kind']=='icon' and e.get('x',0)>50:e.update(x=e['x']+1,y=e['y']+2,w=e['w']*.65,h=e['h']*.65)
for sid in ['s02-04','s04-03']:
 for e in p(sid)['elements']:
  if e.get('text','').startswith('Lorem') and 65<e.get('x',0)<75 and e.get('y',0)<55:e.update(y=41,w=24,size=13);e['text']='There are many variations of\nideas for business innovation.'
for e in p('s03-03')['elements']:
 if e.get('text')=='Introduction':e['size']=37
for sid in ['s03-08','s03-09','s05-02']:
 for e in p(sid)['elements']:
  if e.get('text') in ['Vision','Values','Team Leader']:e['text']='Our\n'+e['text'];e['y']=12
s=p('s03-09');s['elements']=[e for e in s['elements'] if not(e.get('x',0)>35 and e['kind'] in ['text','icon'] and e.get('text')!='04.09 - 03.07')]
for x,val,col,icon in [(33,'$47K',W,'Layers'),(55,'77.23K','#111','Lightbulb'),(76,'32.11K','#111','HandCoins')]:
 s['elements'] += [tx(val,x+1,42,18,37,weight=600,color=col,align='center'),ic(x+6,53,7,12.4,icon,col),tx('Your Title Text Here',x+1,70,18,13,weight=600,color=col,align='center'),tx('Thoughtful ideas support\nstronger business outcomes\nand long-term growth.',x+1,76,18,13,color=col,align='center')]
for y in [41,58,76]:p('s03-07')['elements'].insert(2,box(60,y-4,6,10.67,B,'50%'))
for sid in ['s05-01']:
 for e in p(sid)['elements']:
  if e.get('text') in ['1.','2.','3.','4.']:e['size']=70;e['weight']=300;e['y']-=4
  elif e.get('text')=='Your Title Text Here':e['y']-=4
  elif e.get('text','').startswith('Lorem'):e['y']-=4;e['w']=18;e['size']=14
for e in p('s05-05')['elements']:
 if e.get('text')=='Subtitle Here':e['y']=74;e['size']=14;e['weight']=600
 elif e.get('text','').startswith('Lorem'):e['y']=80;e['size']=13;e['text']='Lorem ipsum dolor sit\namet, consectetur\nadipiscing elit. Ideas\ncreate lasting value.'
for sid in ['s05-07']:
 for e in p(sid)['elements']:
  if e.get('text')=='75%':e['x']-=3;e['align']='center';e['w']=10;e['size']=30
# Matching duplicated reference pages are still independent cells.
for dst,src in [('s04-01','s03-05'),('s04-02','s02-02'),('s04-03','s02-04'),('s05-08','s04-04')]:p(dst)['elements']=copy.deepcopy(p(src)['elements'])
for key,s in D.items():s['id']=key.split('/')[1]
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(D,ensure_ascii=False,separators=(',',':')))
