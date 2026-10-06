from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
D=json.loads((ROOT/'src/decks/group-b-data.json').read_text());R='#df2718';K='#080808';W='#fff'
def p(s):return D['p092/'+s]
for k,s in D.items():
 if not k.startswith('p092'):continue
 for e in s['elements']:
  for prop in ['fill','color','stroke']:
   if e.get(prop)=='#d6160a':e[prop]=R
  if e.get('text')=='Financial Technology':e['size']=13;e['weight']=400
  if e.get('text')=='◉ PAYONE':e['size']=24;e['w']=14;e['x']=84
  if e.get('text')=='2025':e['size']=13
 if s['background']=='#d6160a':s['background']=R
 sid=k.split('/')[1]
 if sid in ['s01-02','s01-05','s01-06','s01-08','s01-09','s02-03','s02-05','s02-06','s02-08','s02-09','s04-01','s04-02','s04-03','s04-05','s04-07']:
  x={'s04-03':70,'s04-02':51,'s04-01':30,'s02-08':23,'s01-08':30,'s01-02':39,'s02-05':39}.get(sid,34)
  s['elements'].insert(0,box(x,0,10,2.4,R))
 if sid not in ['s02-01']:
  s['elements'] += [box(2,93,1.7,3.0,R,'50%'),{**box(1.4,92.0,2.9,5.15,'transparent','50%'),'border':'1px solid #cbb8b8'}]
for sid in ['s01-01','s02-04']:
 s=p(sid)
 for e in s['elements']:
  t=e.get('text','')
  if t.startswith('“Lorem'):e.update(text='Cashless is not\nthe future — it’s\nthe present.',x=2,y=59,w=31,size=31,leading=1.1)
  if t.startswith('Session '):e['text']='Session #'+t[-1];e['y']-=5
  if t.startswith('Lorem') and e.get('x')==76:e['y']-=5;e['text']='1. Lorem ipsum dolor\n2. Amet, consectetur\n3. Adipiscing elit aenean\n4. Commodo ligula eget';e['size']=16
for sid in ['s01-02','s02-05']:
 s=p(sid);s['elements']=[e for e in s['elements'] if e['kind']!='path' and not(e.get('x',0)>=42 and e.get('y',0)>30 and e['kind']=='text')]
 s['elements'] += [tx('70%',55,15,41,224,color=R,weight=400),tx('30%',55,60,41,224,color=R,weight=400),tx('of SMEs still find it difficult to manage digital payments',56,44,39,14),tx('Lorem ipsum dolor sit amet, consectetur adipiscing elit.',56,89,39,14)]
 for e in s['elements']:
  if e.get('text','').startswith('Lorem') and e.get('x')==2:e['y']=65;e['size']=16;e['text']='Lorem ipsum dolor sit amet, adipiscing elit. Aenean\ncommodo ligula eget dolor. Aenean massa. Cum sociis\nnatoque penatibus et magnis dis parturient montes,\nnascetur ridiculus mus. Donec quam felis, ultricies nec,\npellentesque eu, pretium quis, sem.'
for sid in ['s01-03','s02-07']:
 for e in p(sid)['elements']:
  if e.get('text','').startswith('“Lorem'):e.update(text='It Does Not Matter How\nSlowly You Go As Long As\nYou Do Not Stop.',size=28,y=63,w=32)
for sid in ['s01-06','s04-05']:
 for e in p(sid)['elements']:
  if e.get('text')=='Data 1':e.update(x=30,y=47,w=11)
  if e.get('text')=='Description' and e.get('x')==29:e.update(x=30,y=51,w=11)
s=p('s01-07')
s['elements'] += [tx('Description',2,49,28,26,weight=700,color=W),para(2,56,29,16,W,4),tx('2024 Plan',46,88,12,14),tx('2025 Plan',60,88,12,14),tx('Details',80,62,17,26,weight=700),tx('■    2025       $4500\n■    2024       $3250',80,68,18,16)]
for e in s['elements']:
 if e.get('text')=='2024-2025':e.update(x=2,y=77,size=58,w=31)
 if e.get('text','').startswith('Lorem') and e.get('x')==3:e['y']=56
 if e.get('text') in ['2500','4000']:e['size']=16
 if e.get('text')=='Description' and e.get('x')==77:e['y']=27
 if e.get('text','').startswith('Lorem') and e.get('x')==77:e['y']=33;e['size']=16
s=p('s01-08');s['elements']=[e for e in s['elements'] if not(e.get('text') in ['Diana Doe','Financial Expert','Financial\nExpert','diana@email.com'])]
for e in s['elements']:
 if e['kind']=='image':e['w']=10;e['h']=17.78;e['y']=25 if e.get('x')==43 else 61
for x,y,c in [(58,27,K),(16,63,W),(49,63,W),(82,63,W)]:s['elements'] += [tx('Diana Doe',x,y,17,25,weight=700,color=c),tx('Financial Expert',x,y+5,17,14,color=c),tx('✉  diana@email.com',x,y+10,17,14,color=c)]
s['elements'] += [para(77,27,19,16,lines=4),tx('A successful society still takes determined action and the courage to embrace change.',18,86,65,15,color=W,align='center')]
s=p('s01-09')
for e in s['elements']:
 t=e.get('text','')
 if t in ['200k','80k','30k']:e['text']={'200k':'200,000','80k':'80,000','30k':'30,000'}[t];e['w']=14;e['size']=31
 if t=='Financial\nProjection\nfor 2026':e['runs']=[{'text':'Financial\nProjection\nfor '},{'text':'2026','color':R}]
 if t in ['Revenue','Expenses','Net Profit']:e['text']={'Revenue':'2027          $30,000','Expenses':'2026          $80,000','Net Profit':'2025        $200,000'}[t];e.update(y=e['y']-17,w=27,size=20)
s['elements'] += [tx('2027',35,27,4,12),tx('2026',35,48,4,12),tx('2025',35,70,4,12)]
for i in range(6):s['elements'] += [path([[39+i*11,20],[39+i*11,85]],'#aaa',.8),tx(str(i*50000),38+i*11,86,10,12)]
# Persona legend is two compact entries rather than overlapping paragraph text.
s=p('s04-07');s['elements']=[e for e in s['elements'] if not(e.get('text','').startswith('Lorem') and e.get('x')==31) and not(e.get('text','').startswith('Men'))];s['elements'] += [tx('■   Men         40%\n■   Women    60%',31,64,18,16)]
for key,s in D.items():s['id']=key.split('/')[1]
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(D,ensure_ascii=False,separators=(',',':')))
