"""Last root integration batch, based on individually opened hash-named final pairs."""
import json, math, hashlib, copy
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
src=ROOT/'src/decks/group-b-data.json'; old_bytes=src.read_bytes()
data=json.loads(old_bytes); before=copy.deepcopy(data); notes={}
def els(k):return data[k]['elements']
def remove(k,p):data[k]['elements']=[e for e in els(k) if not p(e)]
def add(k,*e):els(k).extend(e)
def edit(k,p,**kw):
 for e in els(k):
  if p(e):e.update(kw)
def txt(k,value,**kw):edit(k,lambda e:e['kind']=='text' and e.get('text')==value,**kw)
def note(k,s):notes.setdefault(k,[]).append(s)
def prose(k,p,value,**kw):
 for e in els(k):
  if p(e):
   e.update(text=value,**kw)
   e['h']=min(100-e['y'],(value.count('\n')+1.4)*e['size']*e.get('lineHeight',1.15)/7.2)
def circle(x,y,w,c):return box(x,y,w,w*16/9,c,'50%')
def bounds(e):
 p=e['points'];return min(a['x'] for a in p),min(a['y'] for a in p),max(a['x'] for a in p),max(a['y'] for a in p)
def star(cx,cy,w,color):
 pts=[]
 for i in range(10):
  a=math.radians(-90+i*36);r=w/2*(1 if i%2==0 else .42)
  pts.append((cx+math.cos(a)*r,cy+math.sin(a)*r*16/9))
 return path(pts,color,0,color)

# Original clockwise ordering and legend year/color associations.
k='p051/s01-07';right=[e for e in els(k) if e['kind']=='path' and bounds(e)[0]>40]
remove(k,lambda e:e['kind']=='path');data[k]['elements']=ring(7,43,26,46,[10,30,40,20],['#fff','#cba315','#263d59','#edbf16'],0)+right+els(k)
edit(k,lambda e:e['kind']=='box' and e['x']==17 and e['y']==93,fill='#cba315')
edit(k,lambda e:e['kind']=='box' and e['x']==27 and e['y']==93,fill='#263d59')
note(k,'Native left pie clockwise white/gold/navy/yellow restored, including year/color legend association.')

for k in [k for k in data if k.startswith('p064/')]:
 txt(k,'Creative Step Business',color='#9f78bc',weight=500)
 note(k,'Native small purple brand caption restored; only one caption remains.')
k='p064/s04-04';remove(k,lambda e:e['kind']=='text' and e['x']==75 and e['y']==79)
add(k,path([(71,76),(74,82),(71,88)],'#303030',0,'#303030'))
note(k,'Source final step has Finish rather than a fourth prose block; overlapping invented block removed and arrow tip restored.')
k='p064/s04-06'
for x,label,c in [(42,'Step One','#7365ef'),(56,'Step Two','#bc61ce'),(72,'Step Three','#f4b900')]:
 edit(k,lambda e:e['kind']=='box' and abs(e['x']-x)<.1 and e.get('radius')=='50%',fill=c)
 txt(k,label,color=c)
note(k,'Three native circle/title colors restored to purple, magenta, yellow.')
k='p064/s04-07';remove(k,lambda e:e['kind']=='path' and e.get('fill')=='#d3d3d3' or e['kind']=='icon' and e['x']==91 and e['y']==29)
add(k,path([(84,50),(84,42),(98,42)],'#d3d3d3',3))
note(k,'Duplicate gray trophy and large filled stair artifact removed; final gray stair is a clean thin connector.')
k='p069/s02-08';remove(k,lambda e:e['kind']=='box' and e.get('fill')=='#e6f6d2')
note(k,'Residual gradient-contour circle removed; graphic background stays flat as requested.')
k='p069/s02-09';remove(k,lambda e:e['kind']=='box' and e['y']==45 and e['w']==6)
edit(k,lambda e:e['kind']=='chip' and e.get('text') in ['01','02','03'],radius='50%',border='1px solid #777')
edit(k,lambda e:e['kind']=='text' and e['x']==20 and e['y']==30,align='center')
note(k,'Process numbers are actual bordered circular centered chips; centered introduction matches source.')

# Native monetary punctuation verified again against both full input sheets.
for k in ['p073/s02-03','p073/s02-08','p073/s03-09']:
 txt(k,'$25,130',text='$25.130')
 note(k,'Original full sheet clearly uses $25.130; decimal point restored. s02-02 comma retained.')
k='p073/s02-03'
for value,x,y,c in [('34%',53.4,44,'#fff'),('29%',72,28,'#555'),('37%',65,69,'#fff')]:add(k,tx(value,x,y,8,12,color=c,align='center'))
note(k,'Three ring annotations restored. Native tiny percentages partly blurred; 34/29/37 are readable/plausible normalized replacements, explicitly recorded.')
k='p073/s02-04';edit(k,lambda e:e['kind']=='text' and 'GLOBAL' in e.get('text',''),x=74,y=49,w=20,size=18,h=4.5)
edit(k,lambda e:e['kind']=='image' and e['x']==86,x=71.5,y=49,w=1.7,h=3.02)
note(k,'Break-page brand moved to its distinct native middle-right position above the headline.')
k='p073/s02-06';remove(k,lambda e:e['kind']=='chip')
for i,(v,c,fg) in enumerate([('Profit growth','#fff','#555'),('Revenue','#ef7c2b','#fff'),('Profitability','#333','#fff')]):add(k,chip(v,67+i*9,44,8,4,11,c,fg,radius=20))
note(k,'Duplicate old chip row removed; exactly three native white/orange/dark centered chips remain.')
k='p073/s02-07';add(k,tx('Profit growth drives revenue and\nstrengthens long-term business.',44,80,24,14,color='#444'))
note(k,'Missing two-line Our Vision body restored as ordinary prose; native tiny wording cannot be resolved reliably.')
k='p073/s03-03';edit(k,lambda e:e['kind']=='text' and e['x']==66 and e['y']==32,color='#fff')
note(k,'Restored 15% body changed to native white on the dark panel.')
for k in ['p073/s03-06','p073/s03-08']:
 remove(k,lambda e:e['kind']=='text' and e.get('text')=='Profit growth' and e['y']>50)
 add(k,tx('Profit growth',7,60,30,15,color='#777'))
 note(k,'Overlapping duplicate Profit growth caption removed; one gray caption and orange dot remain.')

k='p080/s02-01'
for e in els(k):
 if e['kind']=='text' and e.get('text','').startswith('Lorem'):
  e.update(text='THERE ARE MANY VARIATIONS OF\nPASSAGES OF LOREM IPSUM AVAILABLE,\nBUT THE MAJORITY.',size=12,align='center',x=47 if e['x']<70 else 76,w=21,h=7.45,lineHeight=1.15)
note(k,'Four native brown-cell descriptions are uppercase, three lines, centered; blurred prose replaced normally.')
k='p080/s02-02';remove(k,lambda e:e['kind']=='box' and e['x']==5 and e['y']==80)
edit(k,lambda e:e['kind']=='chip' and e.get('text')=='03',color='#fff',w=7,h=7,border='1px solid #666')
note(k,'Third badge is white on the dark background; duplicate empty border removed and number centered.')
for k in ['p080/s03-03','p080/s08-03']:
 remove(k,lambda e:e['kind']=='text' and e.get('text') in ['01','02','03'] or e['kind']=='box' and e.get('border')=='1px solid #666')
 for label,x,y in [('01',50,70),('02',68,70),('03',86,53)]:add(k,{**chip(label,x,y,10,9,27.74,'transparent','#fff','Michroma',radius='50%'),'border':'1px solid #666'})
 note(k,'All three oval numbers use actual centered chips matching native outlines; 03 no longer sits above its oval.')
k='p080/s08-04';txt(k,'4.40%',y=68,size=52,h=10.4)
txt(k,'GOOD IDEA\nMAKES\nEVERYTHING IS\nBETTER',y=81,size=21,h=13.5)
add(k,tx('Subtitle_',79,66,18,15,color='#fff'))
note(k,'Source right KPI block moved down approximately 50 output pixels; missing Subtitle_ restored and native four-line slogan separated.')

# Dense native Details prose is intentionally page-specific, not a deck template override.
details='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nMauris consectetur fermentum\naugue quis vitae. Sed eget.\n\nFelis neque dui. Sed varius\nsollicitudin metus. Nam\nconvallis consectetur justo\nvel hendrerit. Morbi vitae\nnisi imperdiet lorem metus,\nac imperdiet consectetur.'
for k in ['p081/s02-01','p081/s03-09','p081/s03-07']:
 prose(k,lambda e:e['kind']=='text' and e['x']==11 and e['y']==68,details,size=12,lineHeight=1.12,w=19)
 note(k,'Left Details source density restored as 4 lines, blank line, 6 lines; tiny native prose replaced normally.')
k='p081/s03-06';prose(k,lambda e:e['kind']=='text' and e['x']==40 and e['y']==70,details,size=11,lineHeight=1.12,w=21)
note(k,'Central Details native two-paragraph 4+6-line density restored using recorded normal prose.')
k='p081/s02-01'
for labelx,newx in [(47,40.3),(62,56.3),(86,82.2)]:
 edit(k,lambda e:e.get('text')=='Million' and e['x']==labelx,x=newx,size=10,h=2.6,w=5)
note(k,'Three Million labels moved inline just after their real numeric glyph width, using small native-size text.')
for k in ['p081/s02-04','p081/s04-03']:
 bodies=[e for e in els(k) if e['kind']=='text' and e['x']==78 and e.get('text','').startswith('Lorem')]
 for e,y in zip(bodies,[59,77]):e.update(y=y,text='There are many variations of passages.\nIdeas create thoughtful experiences.',size=12,h=5.5,w=20,lineHeight=1.15)
 note(k,'Two icon-row bodies returned to their own rows; duplicated overlay under Details removed; replacements recorded.')
for k in ['p081/s03-05','p081/s04-01']:
 for e in els(k):
  if e.get('text')=='Subtitle Here':e.update(x=62 if e['x']<80 else 81,y=57,w=16)
 note(k,'Two native subtitles moved below their icon squares; body rows and metrics kept separate.')
k='p081/s05-03';edit(k,lambda e:e['kind']=='text' and e.get('text') in ['Anthony Mike','Robertson'],w=10,align='center',size=17)
note(k,'Eight member names centered beneath their actual circles instead of offset half a circle to the right.')

k='p091/s02-01';txt(k,'+45%',x=67,w=11,size=43)
note(k,'+45% separated from the purple icon by roughly 22 output pixels; Customer Reviews remains clear.')
k='p091/s03-03';remove(k,lambda e:e['kind']=='text' and e.get('text')=='Problem Statement' and e['y']==59)
note(k,'Obsolete clipped white card heading removed; one Vision Statement and one Mission Statement remain.')
k='p091/s03-04';prose(k,lambda e:e['kind']=='text' and e['x']==8 and e['y']==21,'Text here',size=10,h=2.5,y=19)
edit(k,lambda e:e['kind']=='chip' and e['x']==9 and e.get('text')=='Learn More',y=23.5)
note(k,'Investing card body shortened to native small subtitle, clearing its Learn More chip.')
k='p091/s03-06';txt(k,'$68,76',x=17,w=18,size=44);txt(k,'$67,2',x=78,w=15,size=44)
edit(k,lambda e:e['kind']=='box' and e['x']==55.5 and e['y']==22,fill='#baacd6')
note(k,'Native lavender goals highlight restored; left financial icon/number overlap removed, both side metrics fit.')
k='p091/s03-07';edit(k,lambda e:e['kind']=='text' and e['x']>70 and e['y']>=45 and e['y']<75,align='right')
note(k,'Mission heading/body returned to native right alignment.')
k='p091/s03-09';txt(k,'Customer confidence',y=48)
note(k,'90% caption moved below the number instead of being drawn across its glyphs.')
k='p091/s03-10';edit(k,lambda e:e['kind']=='text' and e['x']==69 and e['y']==83,color='#fff',y=79.5,w=14,size=11,h=5.5)
note(k,'Customer Base small body sits within its purple card in native white, clear of View More.')
k='p091/s03-13';txt(k,'Organizational\nstructure',text='Organizational\nStructure')
add(k,tx('Clear roles connect people and\nstrengthen thoughtful collaboration.',7,64,28,11,color='#fff',align='right'))
for x,y in [(8,26),(8,49),(34,37),(49,60),(8,85),(34,85)]:
 for j in range(5):add(k,star(x+j*1.2,y,0.65,'#fff'))
note(k,'Native Structure capitalization, six small rating rows and Description prose restored; tiny body replaced normally.')
k='p091/s03-16';txt(k,'Content marketing',y=71);edit(k,lambda e:e['kind']=='text' and e['x']==40 and e['y']==75,y=77)
for value,x in [('Q1',11.25),('Q2',16.15),('Q3',21.05),('Q4',25.95)]:txt(k,value,x=x,y=82,w=5,align='center')
txt(k,'Outcomes & tactics',y=15.5)
note(k,'90%/subtitle/body separated vertically; Q1–Q4 each centered below its native bar; top eyebrow clears title.')

for k in ['p092/s01-01','p092/s02-04']:
 prose(k,lambda e:e['kind']=='text' and e['x']==76 and e['y']==26,'1. Lorem ipsum dolor\n2. Amet, consectetur\n3. Adipiscing elit aenean\n4. Commodo ligula eget\n5. Aenean massa.',size=16)
 prose(k,lambda e:e['kind']=='text' and e['x']==76 and e['y']==51,'1. Lorem ipsum dolor\n2. Amet, consectetur\n3. Adipiscing elit aenean',size=16)
 note(k,'Native numbered Session row counts restored to 5/3/4; tiny words retained or normally replaced.')
for k in ['p092/s01-03','p092/s02-07']:
 for e in els(k):
  if e['kind']=='text' and e.get('text')=='Lorem ipsum dolor sit amet':e.update(text='Lorem ipsum sit',x=44 if e['x']<60 else 75,y=18,w=23,h=5,size=24)
  elif e['kind']=='text' and e['y']==32 and e['x']>35:e.update(text='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nAenean commodo ligula eget dolor.\nCum sociis natoque penatibus.',x=44 if e['x']<60 else 75,y=24,w=23,size=14,h=12,lineHeight=1.2)
 note(k,'Top solution title/body returned to native inline bullet positions; small prose remains a recorded approximation.')
k='p092/s01-07';remove(k,lambda e:e['kind']=='text' and e['x']==80 and e['y']==68)
add(k,box(80,68,1,1.78,'#df2718'),box(80,71,1,1.78,'#080808'),tx('2025     $4500\n2024     $3250',82.5,67.6,15,16))
note(k,'Details legend now uses native red 2025 and black 2024 markers.')
k='p092/s01-09';remove(k,lambda e:e['kind']=='box' and e['x']==34 and e['y']==0)
note(k,'Stray top red contour bar removed; original financial projection header has no bar.')
k='p092/s02-06';edit(k,lambda e:e['kind']=='text' and e.get('text')=='Lorem ipsum dolor sit amet',text='Description here')
note(k,'Three readable source titles transcribed as Description here.')
k='p092/s04-09';prose(k,lambda e:e['kind']=='text' and e['x']==61 and e.get('text','').startswith('Lorem'),'Lorem ipsum dolor sit amet, consectetur adipiscing\nelit. Aenean commodo ligula eget dolor.',size=15,lineHeight=1.2)
note(k,'Each of three Description bodies matches native two-line density with shorter ordinary prose.')

k='p101/s02-04';prose(k,lambda e:e['kind']=='text' and e.get('text','').startswith('Lorem'),'Lorem ipsum dolor sit amet, consectetur\nadipiscing elit. Aenean commodo ligula eget\ndolor. Aenean massa.',size=15,lineHeight=1.15)
note(k,'Three native prose blocks are three lines; top arrow no longer intersects the fourth line.')
k='p101/s02-05';remove(k,lambda e:e['kind']=='path' and e.get('fill')=='#7946fd' and len(e['points'])==3 and bounds(e)[0]==90)
edit(k,lambda e:e['kind']=='box' and e['x']==71 and e['y']==34,w=19)
add(k,path([(90,34),(94,39),(90,44)],'#7946fd',0,'#7946fd'))
note(k,'Final purple stair ribbon restored as a real projecting arrow tip instead of a triangle hidden behind its rectangle.')
k='p101/s02-09';remove(k,lambda e:e['kind']=='path' and e.get('fill')=='#ff4826')
pts=[]
for i in range(32):
 a=math.radians(-90+i*360/32);r=8.5*(1 if i%2==0 else .45)
 pts.append((max(7,7+math.cos(a)*r),63+math.sin(a)*r*16/9))
add(k,path(pts,'#ff4826',0,'#ff4826'))
note(k,'Contact card burst is the native half polygon clipped at its left card edge; no raster graphic used.')
k='p101/s03-03';txt(k,'+78.1',text='+78,1')
note(k,'Native +78,1 comma punctuation restored.')
k='p101/s03-06';remove(k,lambda e:e['kind']=='path' and len(e.get('points',[]))==10)
for j in range(5):add(k,star(68+j*2.2,68,1.8,'#edb643' if j<4 else '#fff'))
txt(k,'4.3',x=79,y=66.5,w=5,size=17)
note(k,'Stars and 4.3 placed in native left-to-right order beneath the value, entirely within the purple KPI card.')
k='p101/s03-08';remove(k,lambda e:e.get('text')=='●  Speed       ●  Handling')
add(k,circle(20,92.5,1,'#7946fd'),tx('Speed',21.8,92,9,15),circle(31,92.5,1,'#ff4826'),tx('Handling',32.8,92,12,15),box(47,26.5,9,1.3,'#ff4826'))
note(k,'Native purple Speed / orange Handling dots and short orange Analysis underline restored.')

changed=sorted(k for k in data if data[k]!=before[k])
src.write_text(json.dumps(data,separators=(',',':')))
out={'integrationRound':3,'reviewBasis':'Each final source/result pair opened individually at a path containing PNG/reference/comparison SHA; then source object inspection. Last root integration batch, not an additional deck correction round.','sourceBeforeSha256':hashlib.sha256(old_bytes).hexdigest(),'sourceAfterSha256':hashlib.sha256(src.read_bytes()).hexdigest(),'modifiedIDs':changed,'changes':{k:notes.get(k,[]) for k in changed},'recordedAt':datetime.now(timezone.utc).isoformat()}
(ROOT/'review/group-b-final-integration-modified.json').write_text(json.dumps(out,indent=2))
with (ROOT/'review/group-b.md').open('a') as f:
 f.write('\n## Root final integration repairs after individual production comparison\n\n')
 for k in changed:f.write('- '+k+': '+' '.join(notes.get(k,[]))+'\n')
 f.write('\nFinal native font remains an approximation where tiny sheet typography cannot identify its exact family. Photos, brand image icons and graphic backgrounds remain the required flat placeholders.\n')
print(len(changed),out['sourceAfterSha256']);print(' '.join(changed))
