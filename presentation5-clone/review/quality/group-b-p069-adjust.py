import json,os,copy
from datetime import datetime,timezone
path='src/decks/group-b-data.json';D=json.load(open(path));Q=json.load(open('review/quality/group-b.json'));M=json.load(open('review/quality/group-b-p069-font-metrics.json'));FM={t:(w,h) for t,w,h in M['Poppins']}
# Target first-line painted boundaries read at native page scale; rows overlapping captions/photos use manual isolated bounds.
primary={'s01-01':(618,180),'s01-02':(291,133),'s01-03':(437,94),'s01-04':(785,153),'s01-05':(361,154),'s01-06':(965,138),'s01-07':(444,92),'s01-08':(603,163),'s01-09':(296,164),'s02-01':(283,140),'s02-02':(981,82),'s02-03':(604,89),'s02-04':(952,95),'s02-05':(531,151),'s02-06':(694,115),'s02-07':(676,92),'s02-08':(292,89),'s02-09':(712,110),'s03-01':(618,179),'s03-02':(292,127),'s03-03':(438,95),'s03-04':(968,137),'s04-01':(358,150),'s04-02':(784,146),'s04-03':(600,164),'s04-04':(444,93),'s04-05':(294,165),'s04-06':(864,101)}
# Repeated reference pages retain separate measurements and independent records.
equiv={'s03-01':'s01-01','s03-02':'s01-02','s03-03':'s01-03','s03-04':'s01-06','s04-01':'s01-05','s04-02':'s01-04','s04-03':'s01-08','s04-04':'s01-07','s04-05':'s01-09'}
def g(name,x=0,y=0,w=100,h=100,**kw):return dict(kind='graphic',graphic=name,x=x,y=y,w=w,h=h,**kw)
def tx(text,x,y,w,h=8,size=18,**kw):return dict(kind='text',text=text,x=x,y=y,w=w,h=h,size=size,font='Poppins',weight=400,color='#111',align='left',lineHeight=1.18,nowrap=True)|kw
glows={'s01-01':'90,12,24;9,96,21','s01-02':'27,8,30;4,78,22','s01-03':'0,34,24;100,87,24','s01-04':'6,52,23','s01-05':'3,25,23;66,0,20','s01-06':'53,38,20','s01-07':'98,10,23;48,44,19','s01-08':'89,8,24;40,100,20','s01-09':'33,38,23;55,98,17','s02-01':'92,93,22','s02-02':'0,0,25;95,89,19','s02-03':'68,9,22','s02-04':'7,51,22','s02-05':'5,51,21','s02-06':'45,76,24','s02-07':'53,23,19;0,98,20','s02-08':'0,50,19;95,75,21','s02-09':'0,49,20;57,99,23','s04-06':'29,7,26;66,100,18'}
for key,p in D.items():
 if not key.startswith('p069'):continue
 sid=key.split('/')[1];typ=equiv.get(sid,sid);before=copy.deepcopy(p);es=p['elements'];main=next(e for e in es if e['kind']=='text' and e['size']>50 and not e['text'][0].isdigit() and e['text'][0]!='$');target,top=primary[sid];oldsize=main['size'];sz=round(target/FM[main['text'].split('\n')[0]][0]*100,2)
 main.update(font='Poppins',size=sz,y=round((top-sz*.2)/7.2,2),lineHeight=round(oldsize*main.get('lineHeight',1.12)/sz,3),h=max(main['h'],sz*len(main['text'].split('\n'))*1.3/7.2))
 if typ=='s01-01':main.update(x=27,w=66,lineHeight=1.1);es[3].update(size=17.5,y=73,w=48)
 if typ=='s01-06':main.update(x=0,w=100,align='center');es[10].update(align='center',size=17.5,text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean commodo ligula eget dolor.\nAenean massa sociis natoque.',h=8);es[5].update(size=103);es[6].update(size=103)
 if typ=='s01-08':main.update(w=50,lineHeight=1.08);es[17].update(text='Lorem ipsum dolor sit amet, consectetur adipiscing\nelit. Aenean commodo ligula eget dolor. Aenean\nmassa. Cum sociis natoque penatibus et magnis\nparturient.',size=17.5,h=15,w=42)
 if typ=='s02-01':main.update(w=47);es[8].update(size=18,text='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit. Aenean\ncommodo ligula eget dolor. Aenean\nmassa. Cum sociis natoque penatibus\net magnis parturient.',h=18,w=43);es[2].update(size=117);es[3].update(size=117)
 if typ=='s02-02':main.update(w=90,lineHeight=1.11);es[3].update(size=86);es[4].update(size=86);es[8].update(text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean commodo ligula eget dolor.\nAenean massa. Cum sociis natoque penatibus et magnis parturient.',size=17.5,h=8)
 if typ=='s02-03':main.update(lineHeight=1.18)
 if typ=='s02-04':main.update(x=0,w=100,align='center',lineHeight=1.08)
 if typ=='s02-05':main.update(lineHeight=1.1);es[4].update(x=54,size=107);es.append(dict(kind='path',x=0,y=0,w=100,h=100,points=[{'x':50,'y':70},{'x':51,'y':67},{'x':52,'y':70}],closed=True,fill='#acd82d',color='#acd82d',strokeWidth=0))
 if typ=='s02-06':main.update(lineHeight=1.08,w=57)
 if typ=='s02-07':main.update(x=0,w=100,align='center',lineHeight=1.05);[es[i].update(size=56,weight=600) for i in [1,2,3]]
 if typ=='s02-08':main.update(align='right',x=4,w=46,lineHeight=1.13);es[8].update(weight=600);es[9].update(align='right');[es[i].update(size=94) for i in [2,3,4]]
 if typ=='s02-09':main.update(x=0,w=100,align='center',lineHeight=1);es[12].update(text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean commodo ligula eget dolor.\nAenean massa. Cum sociis natoque penatibus et magnis dis parturient montes.\nDonec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.',size=17,h=10);[es[i].update(weight=600) for i in [3,5,7]]
 if typ=='s04-06':main.update(lineHeight=1.14);[es[i].update(weight=600) for i in [4,6]];[es[i].update(size=17.5) for i in [5,7]]
 # Only subtitle and paragraph roles observed in the reference, not an indiscriminate deck-wide font-size rule.
 for e in es:
  if e['kind'] not in ['text','chip']:continue
  t=e.get('text','')
  if e['kind']=='chip':e.update(size=15.5,weight=500)
  if t.startswith(('Community','Influencer','High-level','Framing The','Framing the','The Issue','Statement Overview','Key\n','Smart ad','01. Our','02. Our','03. Our','04. Our','Leonardo','Laurend','Team\n','Results From','Value\n','Your\n','01. Brand','02. Maximize')):e['weight']=600
  if typ=='s01-02' and t.startswith('Brief Overview'):e.update(weight=600,size=26)
  if typ=='s01-02' and t.startswith('Lorem'):e.update(size=17.5,text='Lorem ipsum dolor sit amet, consectetur adipiscing\nelit. Aenean commodo ligula eget dolor. Aenean\nmassa. Cum sociis natoque penatibus et magnis\nparturient.',h=14)
  if typ=='s01-04' and t=='Framing The\nProblem':e.update(size=23.5)
  if typ=='s01-04' and t.startswith('Lorem'):e.update(size=17.5)
  if typ=='s01-05' and t.startswith('Lorem'):e.update(size=18)
  if typ=='s01-07' and t=='7653+':e.update(size=89)
  if typ=='s01-07' and t.startswith('Lorem') and e['y']==32:e.update(size=18)
  if typ=='s01-08' and t.startswith('Lorem') and e['x']<40:e.update(size=17,text='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nAenean commodo ligula.',h=10)
  if typ=='s01-09' and t in ['Leonardo Martinez','Laurend Carrow']:e.update(size=24)
  if typ=='s02-02' and t.startswith('Lorem') and e['x']==43:e.update(size=17.5,text='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nAenean commodo ligula.',h=10)
  if typ=='s02-04' and t.startswith('Framing'):e.update(weight=600)
  if typ=='s02-04' and (t.startswith('$') or t.endswith('+')):e.update(weight=600)
  if typ=='s02-05' and t.startswith(('01. Brand','02. Maximize')):e.update(size=23)
  if typ=='s02-06' and t=='Problem Statement' and e['x']==73:e.update(weight=600)
  if typ=='s02-08' and t.startswith('Budget\n'):e.update(weight=600)
 # Replace the mathematically constructed old annular polygons with clean analytic SVG geometry and source gradients.
 newer=[]
 for e in es:
  if e['kind']=='path' and len(e.get('points',[]))>100 and e.get('fill'):
   pts=e['points'];x=min(v['x'] for v in pts);y=min(v['y'] for v in pts);w=max(v['x'] for v in pts)-x;h=max(v['y'] for v in pts)-y
   if typ=='s01-01':
    if x>0:y+=7
    else:x+=2;y-=6;w-=2;h-=3.5
   if typ=='s01-09':continue
   newer.append(g('b-neon-ring',x,y,w,h));continue
  newer.append(e)
 es=newer
 if typ=='s01-09':es.insert(0,g('b-neon-team-card',21.5,31,20,45))
 if typ=='s01-05':
  es.append(g('b-photo-lime-overlay',48,58,20,32));es.append(tx('Partnering With\nCreators To\nExpand Reach',51,74,16,12,18,color='#fff'))
 if typ=='s02-02':
  for y in [54,77]:es.append(dict(kind='path',x=0,y=0,w=100,h=100,points=[{'x':5,'y':y+3},{'x':6,'y':y},{'x':7,'y':y+3}],closed=True,fill='#acd82d',color='#acd82d',strokeWidth=0))
 es.insert(0,g('b-neon-glow',variant=glows.get(typ,'50,50,24')))
 # Readable page folios are UI elements, not embedded photographed lettering.
 folio={'s01-03':'3','s01-04':'4','s01-05':'5','s01-06':'4','s01-07':'7','s01-08':'8','s01-09':'9','s02-01':'11','s02-02':'12','s02-03':'13','s02-04':'15','s02-05':'13','s02-06':'14','s02-07':'17','s02-08':'18','s02-09':'20','s04-06':'10'}.get(typ)
 if folio:es.append(tx(folio,92.5,92,2,4,13,color='#fff' if p['background']=='#0d0d0d' else '#111',align='right'))
 p['elements']=es
 Q['pages'][key]['measurements'].append({'titleFirstLine':{'sourceInkWidth':target,'sourceInkTop':top,'loadedFont':'Poppins','canvasInkWidthAt100':FM[main['text'].split('\n')[0]][0],'newSize':sz},'method':'Native source isolated glyph row bounds and actually loaded canvas font metrics; caption/photo-contaminated bands manually isolated.'})
 Q['pages'][key]['changes'].append({'round':'quality-b','at':datetime.now(timezone.utc).isoformat(),'reason':'Individual original/native comparison: primary actual font/ink width/top, subtitle weight, paragraph line count, readable button typography, source neon ring shading/glows and missing simple overlays restored.','beforeElementCount':len(before['elements']),'afterElementCount':len(es)})
 for e in es:
  if e['kind']=='image':Q['pages'][key]['remaining'].append({'reason':'Original photograph, complex person or physical device screen retained as requested solid gray placeholder.','region':[e['x'],e['y'],e['w'],e['h']]})
 for e in es:
  if e['kind']=='text' and e.get('text','').startswith('Lorem'):Q['pages'][key].setdefault('unreadableReplacements',[]).append({'region':[e['x'],e['y'],e['w'],e['h']],'text':e['text'],'reason':'Tiny reference copy is not reliably readable; ordinary Latin prose reproduces observed line density.'})
for path,obj in [(path,D),('review/quality/group-b.json',Q)]:
 with open(path+'.tmp','w') as f:json.dump(obj,f,indent=2,ensure_ascii=False)
 os.replace(path+'.tmp',path)
print('adjusted 28 p069 pages')
