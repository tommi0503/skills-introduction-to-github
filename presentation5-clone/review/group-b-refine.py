import json,sys,math,re
from pathlib import Path
sys.path.insert(0,'/tmp/envato-b-python')
import cmudict
ROOT=Path(__file__).resolve().parents[1]
raw=json.loads((ROOT/'review/group-b-page-data.json').read_text());manifest=json.loads((ROOT/'public/reference/groups/b.json').read_text());unreadable=json.loads((ROOT/'review/group-b-unreadable.json').read_text())
EXTRA={'p055','p060','p100','p105'}
WORDS=set(cmudict.words())|set('qivora infographic infographics lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt labore dolore magna aliqua montserrat quantive payone pitchdeck profitability fortberry evgenystudio creative branding subtitle portfolio mockup deliverable timeline strategic financial statement process powerpoint ppt ui ux www reallygoodsite text subtitle your'.split())
E=[]
def tx(text,x,y,w,size,font='DM Sans',weight=400,color='#171717',align='left',leading=1.15):
 lines=text.count('\n')+1
 return {'kind':'text','x':x,'y':y,'w':w,'h':min(100-y,size/720*100*leading*(lines+.4)),'text':text,'size':size,'font':font,'weight':weight,'color':color,'align':align,'lineHeight':leading,'nowrap':True}
def box(x,y,w,h,fill,radius=0):return {'kind':'box','x':x,'y':y,'w':w,'h':h,'fill':fill,'radius':radius}
def photo(x,y,w,h,clip=None):
 out={'kind':'image','x':x,'y':y,'w':w,'h':h,'text':'Photograph, device screen or complex illustration placeholder'}
 if clip:out['clipPath']=clip
 return out
def ic(x,y,w,h,icon,color='#111',stroke=1.5):return {'kind':'icon','x':x,'y':y,'w':w,'h':h,'icon':icon,'color':color,'strokeWidth':stroke}
def chip(text,x,y,w,h,size,fill,color='#111',font='DM Sans',weight=400,radius=0):return {'kind':'chip','x':x,'y':y,'w':w,'h':h,'text':text,'size':size,'font':font,'weight':weight,'fill':fill,'color':color,'align':'center','lineHeight':1,'radius':radius}
def path(points,color,width=1,fill=None):return {'kind':'path','x':0,'y':0,'w':100,'h':100,'points':[{'x':x,'y':y} for x,y in points],'color':color,'strokeWidth':width,'fill':fill,'closed':fill is not None}
def ring(x,y,w,h,values,colors,inner=.57,start=-90):
 els=[];total=sum(values);a=start
 for v,color in zip(values,colors):
  b=a+v/total*360;pts=[]
  for rr,angles in [(1,[a+(b-a)*i/30 for i in range(31)]),(inner,[b-(b-a)*i/30 for i in range(31)])]:
   pts += [(x+w/2+math.cos(math.radians(z))*w/2*rr,y+h/2+math.sin(math.radians(z))*h/2*rr) for z in angles]
  els.append(path(pts,color,0,color));a=b
 return els
P='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
def para(x,y,w,size=18,color='#444',lines=3):
 # Real prose rather than anonymous strokes; explicitly recorded where native words cannot be read.
 words=P.split();per=max(12,int(w*12.8/(size*.47)));out=[];line=''
 for word in words:
  if len(line)+len(word)+1>per:out.append(line);line=word
  else:line=(line+' '+word).strip()
 if line:out.append(line)
 return tx('\n'.join(out[:lines]),x,y,w,size,color=color,leading=1.25)
def title(text,x,y,w,size=75,font='DM Sans',weight=400,color='#171717',align='left',leading=1.12):return tx(text,x,y,w,size,font,weight,color,align,leading)
fixes={}
# Text repair: preserve readable words, replace unreadable native prose with ordinary legible words.
for key,page in raw.items():
 if key.split('/')[0] in EXTRA:continue
 els=[];rep=[]
 for e in page['elements']:
  if e['kind']=='text':
   if e['size']>=38:continue # Main headings and large numeric labels are authored explicitly below.
   val=e['text'];tokens=re.findall(r'[A-Za-z]{2,}',val)
   known=sum(t.lower() in WORDS for t in tokens)
   bad=len(tokens)==0 and not re.fullmatch(r'[0-9$%.,+\-/]+',val.strip()) or len(tokens)>0 and known/len(tokens)<.75 or '\\' in val or val in ['Lorem ipsum','Your Title Here','01']
   if bad:
    if e['w']<5 or e['h']>9:continue
    old=val;val='Your text here' if e['w']<17 else 'Lorem ipsum dolor sit amet.'
    size=min(e['size'],e['w']*12.8/(len(val)*.48),24)
    e={**e,'text':val,'size':max(8,size),'h':max(3,size/720*100*1.7),'color':'#f7f7f5' if page['background']<'#777777' else '#333333'}
    rep.append({'originalOCR':old,'replacement':val,'reason':'Native small text cannot be read reliably.','normalizedBox':[e[k] for k in ['x','y','w','h']]})
   els.append(e)
  else:
   # Protect actual headings from accidentally traced glyph fragments.
   if e['kind']=='path' and e.get('fill'):
    pts=e.get('points',[]);w=max((p['x']for p in pts),default=0)-min((p['x']for p in pts),default=0);h=max((p['y']for p in pts),default=0)-min((p['y']for p in pts),default=0)
    color=e['fill'];lum=sum(int(color[i:i+2],16) for i in [1,3,5])/3
    if h<20 and w<h*1.8 and (lum<65 or lum>235):continue
   if e['kind']=='path':
    pts=e.get('points',[])
    if len(pts)<3:continue
    xx=min(p['x'] for p in pts);yy=min(p['y'] for p in pts);ww=max(p['x'] for p in pts)-xx;hh=max(p['y'] for p in pts)-yy
    area=abs(sum(pts[i]['x']*pts[(i+1)%len(pts)]['y']-pts[(i+1)%len(pts)]['x']*pts[i]['y'] for i in range(len(pts)))/2)
    if ww<15 and hh<15:continue
    ratio=area/max(.001,ww*hh)
    if len(pts)>8:
     if ratio>.80:e=box(xx,yy,ww,hh,e.get('fill','#ddd'),min(ww*12.8,hh*7.2)*.08)
     elif .67<ratio<.83 and .75<ww*1.777/hh<1.25:e=box(xx,yy,ww,hh,e.get('fill','#ddd'),'50%')
     else:continue
   els.append(e)
 page['elements']=els;fixes[key]=rep

def setpage(deck,sid,textels,drop_text=False,extra=None,bg=None):
 key=f'{deck}/{sid}';page=raw[key]
 if drop_text:page['elements']=[e for e in page['elements'] if e['kind']!='text']
 page['elements']+=(extra or [])+textels
 if bg:page['background']=bg
 fixes[key].append({'manualTypography':'Headings, line breaks, alignment and main figures manually transcribed from the individual native crop.'})

# Film Intro: red/black editorial grid, narrow uppercase display typography.
film=[('FILM INTRODUCTION',5,5,90,105,'left'),('SMARTPHONE\nMOCKUP',5,4,62,104,'left'),('BREAK SLIDE',5,4,48,100,'left'),('INTRODUCTION TO FILM',5,30,90,100,'left'),('OUR CREATIVE TEAM',5,4,90,93,'left'),('THANK YOU',5,66,90,164,'left'),('DATA VISUAL COMPARISON',16,7,78,91,'left'),('THE ART OF\nCINEMA',45,7,49,98,'right'),('THE ROLE OF\nEFFECTS IN FILM',55,70,41,90,'left'),('INCREASING AUDIENCE\nEVERY YEAR',22,4,73,97,'right'),('GROWTH IN FILM\nPRODUCTION',40,5,55,98,'right'),('THE GLOBAL FILM\nINDUSTRY',5,5,90,96,'left'),('EXPLORING FILM\nPRODUCTION',15,3,80,105,'right'),('SCHEDULE BIG MOVIE',17,6,78,104,'left'),('DATA VISUAL COMPARISON',16,6,80,91,'left'),('THE FACES\nOF THE FILM\nINDUSTRY',21,46,77,93,'left')]
for n,(text,x,y,w,size,align) in enumerate(film,1):
 sid=f's02-{n:02}';page=raw[f'p050/{sid}'];color='#ffffff' if n in [2,3,8,13,16] else '#f00014'
 txt=[title(text,x,y,w,size,'Bebas Neue',400,color,align,1.03)]
 if n==2:txt += [title('80%',5,57,21,107,'Bebas Neue',color='#fff'),title('100+',26,57,22,107,'Bebas Neue',color='#fff'),tx('AUDIENCE RESPONSE',5,76,24,24,'Bebas Neue',color='#fff'),tx('THE FILM BEING SHOWN',26,76,31,24,'Bebas Neue',color='#fff'),para(5,85,54,17,'#fff',2)]
 if n==3:txt += [tx("IT IS TIME TO BREAK 10 MINUTE",5,22,48,28,'Bebas Neue',color='#fff'),para(5,84,47,17,'#fff',2)]
 if n==5:txt += [tx('ALBERTO GOTZE',5,88,43,48,'Bebas Neue',color='#fff'),tx('MARIANA LUIS',51,88,46,48,'Bebas Neue',color='#fff')]
 if n==6:txt += [tx('GET IN TOUCH WITH US',5,60,48,33,'Bebas Neue',color='#fff'),tx('PHONE\n+123 733 450',80,82,15,25,'Bebas Neue',color='#fff',align='right')]
 if n==7:txt += [title('40,5%',5,34,42,160,'DM Sans',color='#f00014'),title('59,5%',59,34,36,160,'DM Sans',color='#fff'),title('2024',5,72,30,68,'Bebas Neue',color='#fff'),title('2025',77,72,19,68,'Bebas Neue',color='#fff',align='right'),para(5,86,41,17,'#fff',2),para(57,86,38,17,'#fff',2)]
 if n==10:txt += [tx('2025',1,25,24,51,'Bebas Neue',color='#fff'),tx('2024',24,59,24,51,'Bebas Neue',color='#ef0015'),tx('2023',48,79,24,51,'Bebas Neue',color='#fff'),tx('85,2%',11,89,17,54,'Bebas Neue',color='#fff'),tx('45,2%',35,89,17,54,'Bebas Neue',color='#e90016'),tx('20,5%',60,93,17,30,'Bebas Neue',color='#fff')]
 if n==11:txt += [title('1000+',70,61,25,95,'Bebas Neue',color='#fff'),tx('FILM SHOWS YEAR AFTER YEAR',59,78,36,24,'Bebas Neue',color='#fff',align='right'),para(53,86,42,17,'#fff',2)]
 if n==14:
  for i,num in enumerate([24,25,26,27,28]):txt += [chip(str(num),11+i*16,33,13,36,98,'#e70014' if i==1 else '#fff','#fff' if i==1 else '#e70014','Bebas Neue'),tx(['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY'][i],12+i*16,60,12,21,'Bebas Neue',color='#fff' if i==1 else '#e70014',align='center')]
 if n==15:txt += [title('80,2%',10,46,37,155,'DM Sans',color='#fff'),title('20,5%',54,46,43,155,'DM Sans',color='#ef0015'),tx('GOOD RESPONSE FROM THE AUDIENCE',16,39,30,22,'Bebas Neue',color='#fff'),tx('BAD RESPONSE FROM THE AUDIENCE',55,39,38,22,'Bebas Neue',color='#ef0015')]
 setpage('p050',sid,txt,True)
# Qivora business deck. Every photographic backdrop is a single flat placeholder.
for sid in ['s01-01','s01-03','s01-08','s01-10','s05-01']:
 raw[f'p051/{sid}']['elements']=[photo(0,0,100,100)]
Y='#e9b21a';W='#fff';N='#344150'
setpage('p051','s01-01',[title('QIVORA',37,40,60,103,weight=700,color=Y),title('Presents',48,56,35,44,weight=700,color=W),tx('PROFESSIONAL',21,9,30,23,color=W),tx('INFOGRAPHIC',49,9,30,23,color=W),tx('STATISTIC',50,87,20,24,color=W),tx('PRESENTATION',73,87,25,24,color=W),tx('20\n22',4,9,12,28,color=Y)],True)
setpage('p051','s01-02',[title('About us',6,26,41,70,weight=700,color=Y),tx('Qivora Business Company',6,44,40,29,color=W),para(6,52,38,20,W,4),tx('www.reallygoodsite.com',6,87,42,20,color=W)],True)
for sid in ['s01-03','s05-01']:
 arr=[title('Sales Report',25,9,43,77,weight=700,color=Y),title('This\nYear',67,9,29,73,color=W),tx('Sales Chart for the Past Year',41,32,55,37,color=W),tx('www.reallygoodsite.com',40,88,50,23,color=W),tx('20\n22',6,9,12,30,color=W)]
 geom=[]
 for i,label in enumerate(['Layout Design','Web Design','UI/UX','Digital Artwork']):
  arr.append(tx(label,6+i*23,48,22,29,weight=700,color=W,align='center'));geom+=ring(9+i*23,58,14,25,[64,36] if i==0 else [43,57] if i==1 else [50,50] if i==2 else [25,75],[W,Y],.58)
 setpage('p051',sid,arr,True,geom)
setpage('p051','s01-04',[title('Target\nMarket',6,31,35,87,weight=700,color=Y),tx('Product\nMarketing\nReach',6,75,31,46,weight=700,color=W)],True)
setpage('p051','s05-02',[title('Target\nMarket',6,31,35,87,weight=700,color=Y),tx('Product\nMarketing\nReach',6,75,31,46,weight=700,color=W)],True)
setpage('p051','s01-05',[title('S.W.O.T Analysis',18,16,70,72,weight=700,color=W)],True)
for i,label in enumerate(['S','W','O','T']):raw['p051/s01-05']['elements'] += [title(label,10+i*25,47,20,112,color='#222' if i%2==0 else '#fff',align='center'),tx(['Strength','Weakness','Opportunities','Threat'][i],4+i*25,65,20,28,color='#222' if i%2==0 else '#fff',align='center'),para(4+i*25,74,20,20,'#222' if i%2==0 else '#fff',5)]
setpage('p051','s01-06',[title('Price Adjustment Plan',9,18,82,68,weight=700,color=W,align='center'),tx('Adjustment to suit the market',10,30,80,38,color=W,align='center')],True)
for i,(label,value) in enumerate([('Personal Use Only','$15 - $35'),('Commercial','$25 - $75'),('Extended Commercial','$125 - $1,500')]):raw['p051/s01-06']['elements'] += [tx(label,8+i*30,55,26,22,align='center'),tx('Range',10+i*30,65,25,22),tx(value,8+i*30,70,26,45,weight=700,color=N,align='center')]
setpage('p051','s01-07',[title('Sales\nDevelopment Plan',6,9,88,72,weight=700,color=Y)],True,ring(7,43,26,46,[44,35,15,6],[Y,'#be9112',N,W],0)+ring(59,43,26,46,[54,22,18,6],[Y,N,'#be9112',W],0))

arr=[title('Business Development\nTimeline',10,14,80,67,weight=700,color=W,align='center')]
for i,year in enumerate([2021,2022,2023,2024]):arr+=[box(6+i*23,43,20,29,Y),tx(str(year),6+i*23,50,20,40,weight=700,color=N,align='center'),para(9+i*23,63,15,20,N,3)]
setpage('p051','s01-08',arr,True)
setpage('p051','s01-09',[title('Project Journey Now\nand Then',12,9,76,68,weight=700,color=W,align='center'),tx('How the project develop from the beginning',12,30,76,39,color=W,align='center')],True)
for i,(year,y) in enumerate([(2018,60),(2019,77),(2020,60),(2021,77)]):raw['p051/s01-09']['elements'] += [tx(str(year),8+i*23,y,16,35,weight=700,color=W,align='center'),para(8+i*23,y+8,17,18,W,3)]
setpage('p051','s01-10',[title('QIVORA',29,41,30,75,weight=700,color=Y),tx('Contact Info',38,36,40,37,color=W),tx('123 Anywhere St. Any City ST12345\n+123-456-7890\nhello@reallygreatsite.com\nwww.reallygreatsite.com',38,56,36,23,color=W)],True,[box(25,26,41,49,N)])
# Problem Statement exact headings and intentional duplicate cover/detail slides.
problem={1:('Problem\nStatement',30,24,66,151,'#fff'),2:('Problem\nIdentification And\nImpact Analysis',42,15,55,90,'#111'),3:('Defining The\nProblem',56,12,41,87,'#111'),4:('Research Context And\nObjectives',11,20,85,86,'#fff'),5:('A Problem\nStatement\nOverview',6,19,39,87,'#111'),6:('Identifying Key Challenges',8,18,86,86,'#111'),7:('The Problem\nThat Drives Our\nProject',5,12,47,86,'#111'),8:('The Why And What\nOf Our Problem\nStatement',49,22,48,85,'#111'),9:('Our Best\nTeam',60,22,38,89,'#111')}
for n,(text,x,y,w,size,color) in problem.items():
 arr=[title(text,x,y,w,size,color=color)]
 if n==1:arr+=[para(31,73,51,22,color,2)]
 if n==2:arr+=[tx('Brief Overview of problem',50,60,43,30),para(50,68,43,22,lines=4)]
 if n==3:arr += [title('3758+',31,16,21,74),tx('High-level benefits',32,30,20,22),title('75%',57,43,23,76,color='#a5ce33'),title('95%',57,69,23,76,color='#a5ce33')]
 if n==4:arr += [title('85,5K',22,48,40,102,color='#fff'),tx('Framing The\nProblem',47,53,21,28,color='#fff'),para(22,67,40,22,'#fff',3)]
 if n==5:arr += [tx('The Issue At Hand',6,13,37,26),tx('Statement Overview',10,64,36,28),para(10,73,34,21,'#333',4)]
 if n==6:arr += [tx('Problem Statement',30,12,40,29,align='center'),title('3651+',57,51,38,112),title('4122+',57,73,38,112)]
 if n==7:arr += [title('7653+',54,14,40,90,color='#add532'),para(54,32,41,23,'#333',3)]
 if n==8:
  for i in range(4):arr += [tx(f'0{i+1}. Our Problem\nStatement',7+(i%2)*23,23+(i//2)*34,21,28),para(7+(i%2)*23,35+(i//2)*34,20,21,'#333',3),chip('Learn More',7+(i%2)*23,56+(i//2)*32,11,4,14,'transparent',radius=15)]
 if n==9:arr += [title('15+',60,48,35,98,color='#a8ce37'),tx('Leonardo Martinez',34,23,29,26),tx('Laurend Carrow',7,73,29,26)]
 setpage('p069',f's01-{n:02}',arr,True)
for n,src in enumerate([1,2,3,6],1):raw[f'p069/s03-{n:02}']['elements']=json.loads(json.dumps(raw[f'p069/s01-{src:02}']['elements']));raw[f'p069/s03-{n:02}']['background']=raw[f'p069/s01-{src:02}']['background']
for n,src in enumerate([5,4,8,7,9],1):raw[f'p069/s04-{n:02}']['elements']=json.loads(json.dumps(raw[f'p069/s01-{src:02}']['elements']));raw[f'p069/s04-{n:02}']['background']=raw[f'p069/s01-{src:02}']['background']
setpage('p069','s04-06',[title('Problem Statement As A\nRoadmap To Innovation',5,13,91,84),tx('01. Innovation 01',6,38,40,25),para(6,47,42,21,lines=3),tx('02. Innovation 02',6,64,40,25),para(6,72,42,21,lines=3)],True)
prob2=[('Aligning\nStakeholder\nPerspectives',6,16,47,84),('Articulating The Problem In\nResearch Topic',6,11,87,76),('Problem Definition\nAnd Research\nQuestions',5,9,57,78),('Identifying The Problem To\nUnlock Opportunities',5,11,90,75),('Breaking Down\nThe Problem\nStatement',51,18,47,86),('“Clarifying Business\nChallenges\nThrough Problem\nStatements.”',42,14,55,78),('Understanding The\nCore Issue',9,11,82,80),('Problem\nStatement For\nEffective Project\nPlanning',5,10,47,80),('Process Infographic',8,12,85,82)]
for n,(text,x,y,w,size) in enumerate(prob2,1):
 col='#fff' if n==1 else '#111';arr=[title(text,x,y,w,size,color=col,align='center' if n in [4,7,8,9] else 'left')]
 if n==1:arr += [title('$562',8,60,43,105,color=col),title('$679',52,60,43,105,color=col)]
 if n==2:arr += [title('76,2K',9,49,30,98),title('94,4K',9,72,30,98)]
 if n==3:arr += [title('94%',20,65,34,105)]
 if n==4:
  for i,(cash,count) in enumerate([('$365.000','1912+'),('$429.000','2827+'),('$512.000','3931+')]):arr += [tx(f'0{i+1}',7,47+i*16,13,28),tx(cash,41,47+i*16,25,28),tx(count,62,47+i*16,25,28)]
 if n==5:arr += [title('85,8K',57,64,39,108)]
 if n==7:
  for i,val in enumerate(['3245+','3977+','4567+']):arr += [title(val,57,41+i*17,31,71)]
 if n==8:
  for i,val in enumerate(['$572','$685','$792']):arr += [title(val,55,12+i*29,41,103)]
 if n==9:
  for i in range(3):arr += [tx(f'Process 0{i+1}',6+i*31,63,27,34),para(6+i*31,73,27,20,lines=3)]
 setpage('p069',f's02-{n:02}',arr,True)
# Orange profit deck: independent photo/chart arrangements are retained page by page.
profit2=[('Performance Metrics',7,22,83),('Industry Trends in\nGlobal Markets',7,21,54),('Risk Assessment\nand Mitigation',7,22,53),('A Short Break\nBefore We Continue',31,63,62),('Industry Trends in\nGlobal Markets',47,21,49),('Historical Profit\nPerformance Analysis',51,70,46),('Our Vision\nand Mission',7,23,36),('The Projected Profit\nForecast Analysis',51,24,47),('Our Contact\nInformation Details',7,22,50)]
profit3=[('Table of Content',7,22,53),('People Powering\nOur Success',7,24,43),('Industry Trends in\nGlobal Markets',7,21,50),('Cost Optimization Initiatives\nin Business Operation',7,24,76),('Opportunities\nfor Growth',7,23,35),('Historical\nProfit Performance',7,69,45),('Profit growth reflects strategy, efficiency,\nand long-term business success\nacross industries.',10,39,80),('Projected Profit\nForecast for Lasting\nBusiness Growth Globally',7,67,48),('The Projected Profit\nForecast Analysis',51,24,47)]
for pv,items in [(2,profit2),(3,profit3)]:
 for n,(text,x,y,w) in enumerate(items,1):
  sid=f's{pv:02}-{n:02}';dark=pv==2 and n in [4,6,7] or pv==3 and n in [3,7];col='#fff' if dark else '#151515'
  arr=[title(text,x,y,w,59,weight=500,color=col),tx('Profit growth',7,15,35,18,color='#c98557')]
  if pv==2 and n==2 or pv==2 and n==5 or pv==2 and n==8 or pv==3 and n==9:arr += [title('$25,130',x,64,42,83),chip('Investment',x+27,68,14,3,14,'#f37824','#fff',radius=20),para(x,78,41,18,lines=3)]
  if pv==2 and n==3:arr += [title('$25.130',7,64,45,83),para(7,78,47,18,lines=3)]
  if pv==2 and n==4:arr += [title('30',7,12,31,180,color='#fff'),para(7,35,44,18,'#fff',3)]
  if pv==2 and n==6 or pv==3 and n==6 or pv==3 and n==8:arr += [title('95.2K',65 if pv==2 else 32,13,31,89,color=col),para(52 if pv==2 else 15,29,41,18,col,3)]
  if pv==2 and n==7:
   arr += [title('90%',51,22,25,87),title('75%',79,22,21,87),tx('Our Vision',44,72,26,30),tx('Our Mission',72,72,26,30),para(44,80,24,17,lines=3),para(72,80,24,17,lines=3)]
  if pv==2 and n==9:
   for i,label in enumerate(['Phone Number','Email Address','Website Link']):arr += [ic(7+i*21,66,6,10,['Phone','Mail','Globe'][i],'#ed7c36'),tx(label,7+i*21,78,21,20),tx(['+123-456-7890','admin@yourmail.com','www.yourwebsite.com'][i],7+i*21,85,21,14)]
  if pv==3 and n==1:
   for i,label in enumerate(['Profit Growth Overview','Performance Analysis','Key Growth Drivers','Future Business Strategies']):arr += [tx(f'0{i+1}',9+(i%2)*46,60+(i//2)*18,9,30,color='#d16d2c'),tx(label,17+(i%2)*46,60+(i//2)*18,38,21)]
  if pv==3 and n==2:arr += [tx('Sophia Carren',67,23,31,40),tx('Daniel Hidayat',67,61,31,40),para(67,36,27,18,lines=2),para(67,73,27,18,lines=2),para(7,68,36,18,lines=3)]
  if pv==3 and n==3:arr += [title('$18.250',7,63,45,90,color='#e3782a'),title('15%',65,22,29,79,color='#fff'),title('39%',65,65,29,79,color='#fff')]
  if pv==3 and n==4:arr += [title('$15.230',36,66,34,68),para(28,77,42,17,lines=3)]
  if pv==3 and n==5:arr += [title('95.2K',7,62,35,79),title('70%',78,22,22,65),title('35%',78,65,22,65)]
  setpage('p073',sid,arr,True)
# Portfolio: a thin display font, compact editorial body, common white navigation strip.
portfolio2=['Services','Package','Work','Deliverable','Mood Brand','Contact']
portfolio3=['Overview','Mission','Vision','Goals','CEO/Founder','Our Team','Resume','Clients','Services']
portfolio6=['Design\nPortfolio','Design\nPortfolio','Welcome','Introduction','Index','About Us','About Us','Our Studio','Who We Are']
portfolio8=['Design\nPortfolio','Mission','Vision','Work']
def portfolio_body(x=4,y=58,w=32):return [tx('SELECTEDWORK/\nDESIGN PORTFOLIO\nFOR 2030',x,y,w,25,color='#fff',leading=1),para(x,y+16,w,12,'#fff',6),tx('Virginia Kelly',x,y+39,w,32,'Kaushan Script',color='#fff')]
for pv,items in [(2,portfolio2),(3,portfolio3),(6,portfolio6),(8,portfolio8)]:
 for n,text in enumerate(items,1):
  sid=f's{pv:02}-{n:02}';cover=text=='Design\nPortfolio';headx=42 if cover else 4;heady=31 if cover else 19;headw=56 if cover else 90;size=108 if cover else 91
  arr=[title(text,headx,heady,headw,size,'Michroma',400,'#161616' if pv==6 and n==2 else '#fff',leading=1.01),tx('evgenystudio',3.5,2.4,25,18,weight=700),tx('Presentation',27,2.6,25,15),tx('Creative',72,2.6,14,15),tx('Modern',83,2.6,12,15),tx('Minimal',93,2.6,7,15)]
  if cover:arr += [title('Template',70,49,29,77,'Kaushan Script',color='#d27835'),tx('Mary\nChristine',50,83,20,19,color='#fff'),tx('DESIGN PORTFOLIO',80,80,19,18,color='#fff'),tx('“we are the\nwhat we\nrepeatedly\ndo”.',27,78,13,21,color='#fff',align='right')]
  if text in ['Work','Mood Brand','Welcome','Our Team','About Us','Who We Are','Mission','Vision','Clients','Services']:arr+=portfolio_body(y=60 if text=='Services' else 59)
  if pv==2 and n==1:
   for i in range(4):arr += [tx(f'0{i+1}/',53+(i%2)*29,31+(i//2)*43,21,44,'Michroma',color='#fff',align='center'),tx('Subtitle Here',49+(i%2)*29,39+(i//2)*43,29,22,color='#fff',align='center'),para(49+(i%2)*29,48+(i//2)*38,24,12,'#fff',4)]
  if pv==2 and n==4:
   for i in range(4):arr += [tx(f'0{i+1}/',60,30+i*18,13,38,'Michroma',color='#fff'),para(68,30+i*18,28,12,'#fff',4)]
  if pv==2 and n==6:arr += [title('Portfolio',68,35,31,79,'Kaushan Script',color='#d27835')]
  if text=='Work':arr += [tx('PROJECT NAME\nPROJECT PROPOSAL / 2022\nWWW.PROJECT.NET',71,25,27,23,color='#fff'),title('4.40%',79,61,20,59,color='#fff'),tx('GOOD IDEA\nMAKES\nEVERYTHING IS\nBETTER',79,71,20,23,color='#fff',leading=1)]
  if pv==3 and n==1:
   for i,v in enumerate(['120+','2B','560K','160%']):arr += [tx(v,47+(i%2)*31,57+(i//2)*24,28,36,weight=700),para(47+(i%2)*31,65+(i//2)*24,23,15,lines=3)]
  if text=='Mission':arr += [tx('GOOD IDEA MAKES\nEVERYTHING IS BETTER',35,52,42,27,color='#fff',leading=1),tx('# Subtitle_',35,66,26,18,color='#fff'),para(35,75,26,15,'#fff',4),tx('# Subtitle_',66,66,27,18,color='#fff'),para(66,75,24,15,'#fff',4)]
  if text=='Vision':
   for i in range(3):arr += [tx(f'0{i+1}',48+i*18,65 if i<2 else 51,17,38,'Michroma',color='#fff',align='center')]
  if text=='CEO/Founder':arr += [tx('Valerie\nWarrington',53,43,20,29,weight=700,color='#fff',align='center'),tx('SELECTEDWORK/\nDESIGN PORTFOLIO\nFOR 2030',67,50,29,25,color='#fff'),para(67,64,28,17,'#fff',5)]
  if text=='Our Team':
   for i,name in enumerate(['Syndey Clowney','Dora Cincora\nCindy','Louisa Herry','Margret Mcleod']):arr += [tx(f'0{i+1}',85 if i%2==0 else 71,15+i*23,12,30,color='#fff'),tx(name,73 if i%2==0 else 60,16+i*23,24,18,color='#fff')]
  if text=='Resume':arr += [tx('Profile',57,28,39,24,weight=700,color='#fff'),para(57,35,37,14,'#fff',5),tx('Employment History',57,50,39,24,weight=700,color='#fff'),para(57,58,37,14,'#fff',5),tx('Education',57,78,39,24,weight=700,color='#fff'),para(57,85,37,14,'#fff',3)]
  if text=='Introduction':arr += [tx('Design Portfolio',45,43,51,31,'Michroma',color='#fff'),para(45,53,48,15,'#fff',8)]
  if text=='Index':
   for i,t in enumerate(['COVER PAGE','INTRODUCTION','WELCOME','CONTENTS','OUR STUDIO','OUR GOALS','ABOUT US','SERVICES','PREVIEW','PORTFOLIO']):arr += [tx(f'{i+1:02}  •  {t}',77,57+i*3.2,21,14,color='#fff')]
  if text=='Our Studio':arr += [title('4.40%',7,77,24,65,color='#fff'),tx('GOOD IDEA MAKES\nEVERYTHING IS BETTER',55,54,44,27,color='#fff',leading=1),para(55,65,40,14,'#fff',8)]
  setpage('p080',sid,arr,True)
# Minimal design deck retains different photography, diagrams and inset neutral panels.
minimal2=['Our\nPortfolio','Our\nWorking','Market\nAnalysis','Device','World Map','Thank You\nFor\nWatching']
minimal3=['MINI','MINI','Introduction','Table\nof Contents','Minimal\nAbout Us ?','Minimal\nAbout Us ?','Our\nMission','Our\nVision','Our\nValues']
minimal4=['Minimal\nAbout Us ?','Our\nWorking','Device','Market\nStrategy']
minimal5=['Our\nServices','Our\nTeam Leader','Our\nTeam Members','Creative\nProject','Our\nPhilosophy','Timeline','Our\nPartners','Market\nStrategy','']
for pv,items in [(2,minimal2),(3,minimal3),(4,minimal4),(5,minimal5)]:
 for n,text in enumerate(items,1):
  sid=f's{pv:02}-{n:02}';dark=pv==3 and n==2;col='#fff' if dark else '#111';arr=[]
  cover=text=='MINI';thanks=pv==2 and n==6
  if text:arr += [title(text,18 if cover else 33 if thanks else 11,23 if cover else 32 if thanks else 12,74 if cover else 60,127 if cover else 96 if thanks else 57,weight=800 if cover else 500,color=col,align='center' if thanks else 'left')]
  arr += [tx('04.09 - 03.07',82,6,15,14,color=col),tx('BY: ALASKA ETHAN - 377',10,8,42,17,color=col) if cover else tx('Design',4,41,20,14,color=col),tx('Minimal',4,81,17,14,color=col)]
  if cover:arr += [tx('Minimal\nPresentation\nTemplate',24,42,17,32,color=col,align='right',leading=1),tx('Create By:\nDESIGNS - STOCK',10,82,28,19,color=col)]
  if text in ['Our\nPortfolio','Device','Our\nMission','Our\nValues','Creative\nProject']:arr += [tx('The\nCreative\npower behind\nart projects',11,37,25,32,leading=1.12),tx('Details :',11,62,25,22),para(11,68,25,15,lines=8)]
  if text=='Our\nWorking':
   arr += [tx('Minimal\nPresentation\nTemplate',24,38,25,43,leading=1),tx('Details :',11,62,25,22),para(11,68,30,16,lines=5)]
   for i,v in enumerate(['72K','126K','$47K']):arr += [title(v,49,46+i*19,24,54),tx('Million',62,49+i*19,10,14),ic(66,44+i*19,8,12,['Layers','Lightbulb','HandCoins'][i]),tx('Your Title Text Here',75,45+i*19,23,17,weight=700),para(75,51+i*19,23,13,lines=2)]
  if text=='Our\nPortfolio':
   for i,v in enumerate(['72K','126K','$47K']):arr += [title(v,35+i*25,22,22,47),tx('Million',47+i*25,25,8,12)]
  if text=='Device':arr += [title('$47K',14,65,25,54),title('$10.0K',14,79,25,54),tx('Details :',71,43,25,22),para(71,50,25,15,lines=3)]
  if text in ['Minimal\nAbout Us ?','Our\nVision']:arr += [tx('Details :',11,36,30,22),para(11,44,30,15,lines=8)]
  if pv==3 and n==3:arr += [tx('Minimal\nPresentation\nTemplate',72,35,25,31,leading=1),tx('“This presentation make it clear what\nproblems your company solves and\nwhy it matters.”',43,72,51,29,leading=1.2),tx('Details :',11,66,22,22),para(11,74,22,15,lines=5)]
  if pv==3 and n==4:
   for i,t in enumerate(['Welcome','Executive Summary','About','Situation Analysis','Marketing Objectives','Product']):arr += [tx(f'{i+1:02}   >  {t}',68,42+i*7,28,23)]
  if pv==3 and n==6:arr += [title('70.01K',14,47,25,54),title('$34%',14,74,25,54),tx('The\nCreative\npower behind\nart projects',43,39,26,32),para(43,70,24,16,lines=6)]
  if pv==3 and n==9:
   for i,v in enumerate(['$47K','77.23K','32.11K']):arr += [title(v,37+i*23,41,21,52,align='center'),ic(43+i*23,53,9,15,['Layers','Lightbulb','HandCoins'][i],'#fff' if i==0 else '#222'),tx('Your Title Text Here',38+i*23,77,20,16,weight=700,align='center'),para(38+i*23,82,20,13,'#fff' if i==0 else '#333',3)]
  if text=='Our\nServices':
   for i in range(4):arr += [title(f'{i+1}.',11+(i%2)*22,34+(i//2)*35,20,61,weight=300),tx('Your Title Text Here',11+(i%2)*22,47+(i//2)*35,21,16,weight=700),para(11+(i%2)*22,53+(i//2)*35,21,13,lines=4)]
  if text=='Our\nTeam Leader':arr += [tx('Hello I’m\nCompany Managers',53,36,41,28),para(62,57,31,18,lines=5),tx('Alaska Ethan',62,84,31,23,letterSpacing=2) if False else tx('Alaska Ethan',62,84,31,23)]
  if text=='Our\nTeam Members':
   for j in range(2):
    for i,name in enumerate(['Anthony Mike','Anthony Mike','Robertson','Anthony Mike']):arr += [tx(name,16+i*22,49+j*36,20,19,align='center'),tx('f  ◎  ♥',16+i*22,55+j*36,20,18,align='center')]
  if text=='Our\nPhilosophy':
   for i,v in enumerate(['150K','126M','73K','$15','83+B']):arr += [title(v,10+i*18,51,17,39,align='center'),tx('Subtitle Here',10+i*18,63,17,19,weight=700,align='center'),para(10+i*18,71,17,16,lines=5)]
  if text=='Timeline' or text=='':
   vals=[('2025','150M'),('2026','126K')] if n==6 else [('2027','23K'),('2028','69M'),('2029','47K')]
   for i,(year,value) in enumerate(vals):arr += [title(year,47 if i%2==0 else 33,51+i*23 if n==6 else 16+i*29,24,50),title(value,29 if i%2==0 else 50,51+i*23 if n==6 else 16+i*29,25,43)]
  if text=='Our\nPartners':
   for j in range(2):
    for i,name in enumerate(['Network','Briefcase','Monitor','Heart'] if j==0 else ['Layers','Lightbulb','HandCoins','Send']):arr += [ic(15+i*15,36+j*30,8,12,name,'#fff' if (i+j)%2 else '#222'),tx('Our\nPartners',12+i*15,49+j*30,15,18,color='#fff' if (i+j)%2 else '#222',align='center')]
   for y in [46,76]:arr += [title('75%',78,y,20,38,align='center')]
  if text=='Market\nStrategy':arr += [title('$11.37',19,51,30,49,align='center'),title('$47K',79,40,18,50),title('126K',79,73,18,50)]
  setpage('p081',sid,arr,True)
# Quantive: purple dashboard details, charts and separate business diagram pages.
Q='#251e80';qp='#7d70cf';purpletitles=['Business Plan','Management team','Brief overview\nof the business','Problem statement','Product/Service\nDescription','SMART goals','Vision &\nmission','Your service/\nproduct overview','Industry size\nand trends','Customer\nsegmentation','Competitive\nAnalysis','Unique value proposition','Organizational\nstructure','Operations plan','Sales strategy','Marketing strategy']
for n,text in enumerate(purpletitles,1):
 sid=f's03-{n:02}';x=14 if n==1 else 51 if n in [3,4,5,8,9,10,13,14] else 7;y=36 if n==1 else 12 if n in [2,6,12] else 30 if n in [3,4,5,8,9,10,11,14,15,16] else 43 if n==7 else 25;w=76 if n==1 else 46 if x==51 else 87
 arr=[title(text,x,y,w,113 if n==1 else 66,weight=700,color='#fff' if n in [1,13] else '#111',align='center' if n in [2,6,12] else 'left'),tx('Contact Us      About Us      Home',61,7,31,16),ic(93,5,5,9,'Circle',qp)]
 if n==1:arr += [tx('Quantive',42,23,30,28,weight=700,color='#fff'),chip('Learn More',38,65,27,7,18,'#fff',radius=6)]
 if n==2:
  for i,name in enumerate(['ERIC LONDON','FRANCIS BERA','ELLA WILLIAM','MAXIM HERA']):arr += [tx(name,10+i*22,83,21,16,weight=700,align='center')]
 if n==3:arr += [para(8,40,38,18,lines=3),tx('Problem Statement',8,59,32,18,weight=700,color='#fff'),para(8,66,29,16,'#fff',4),tx('Mission Statement',34,59,25,18,weight=700,color='#fff')]
 if n==4:
  for i,t in enumerate(['Lack of Trust From Online Audience','Limited Integration Across Tools','Inefficient Workflow Management']):arr += [tx(t,57,58+i*13,40,19,weight=700),para(57,63+i*13,38,13,lines=2)]
 if n==5:arr += [title('+987',56,66,22,62),title('+345',78,66,22,62),tx('Table Overview',8,19,38,29,weight=700,align='center')]
 if n==6:arr += [title('$68,76',11,77,27,64),title('$67,2',78,77,21,64)]
 if n==7:arr += [tx('Vision',8,42,26,30,weight=700,color='#fff'),para(8,54,24,18,'#fff',5),tx('Mission',74,42,25,30,weight=700,color='#fff'),para(74,54,23,18,'#fff',5)]
 if n==8:arr += [title('90%',7,71,29,80,color=Q),para(56,54,41,17,lines=3)]
 if n==9:arr += [title('90%',7,39,31,82),title('+45%',62,75,30,69,color=Q)]
 if n==10:arr += [title('Customer',55,37,43,73,weight=700),para(55,62,40,18,lines=3)]
 if n==11:
  for i,t in enumerate(['Strengths','Weaknesses','Opportunities','Threats']):arr += [tx(t,8+(i%2)*63,48+(i//2)*29,30,22,weight=700),para(8+(i%2)*63,56+(i//2)*29,26,15,lines=3)]
 if n==12:
  for i in range(4):arr += [tx(f'STEP\n0{i+1}',37+(i%2)*24,39+(i//2)*36,23,28,color='#fff',align='center')]
 if n==13:arr += [para(58,51,38,18,'#fff',4),title('+45%',55,81,24,57,color='#fff')]
 if n==14:
  for i,t in enumerate(['Team collaboration','Project development','Sales & marketing']):arr += [tx(t,13,39+i*18,31,23,weight=700),para(13,46+i*18,31,15,lines=2)]
 if n==15:arr += [title('+98,65',73,23,27,63),tx('Social Media',12,66,35,25,weight=700,color='#fff')]
 if n==16:arr += [title('90%',51,60,31,72),tx('Content marketing',52,74,33,24,weight=700)]
 setpage('p091',sid,arr,True)
for n,(text,x,y,w) in enumerate([('Technology plan',59,29,39),('Financial plan overview',14,17,80),('Funding\nrequirements',59,26,39),('Thank You',21,36,72)],1):
 arr=[title(text,x,y,w,65 if n<4 else 130,weight=700,color='#fff' if n==4 else '#111'),tx('Contact Us      About Us      Home',59,7,36,16,color='#111')]
 if n==1:arr += [title('$68,76',40,22,30,65),title('+45%',65,55,29,55,color=Q)]
 if n==2:
  for i,t in enumerate(['User Growth','Cost assumptions','Monetization']):arr += [tx(t,9+i*31,72,28,25,weight=700),para(9+i*31,86,25,18,lines=2)]
 if n==3:arr += [title('+56,5',29,18,27,50),title('+71,3 ↗',79,80,21,52)]
 if n==4:arr += [chip('Learn More',38,63,25,8,22,'#fff','#222',radius=6),tx('Quantive',41,30,35,26,weight=700,color='#fff')]
 setpage('p091',f's02-{n:02}',arr,True)
# PAYONE red pitch: each screenshot cell stays a separate page.
RED='#de291c';BLACK='#161616'
red1=['This Time’s\nTopic of\nDiscussion','Problem\nStatement\n(Main)','Solutions','Target Market','Product /\nDemo','Market Trends','Marketing\n& Sales Plan','Seeking\nProfessional\nAdvice','Financial\nProjection\nfor 2026']
red2=['PAYONE','Welcome','Your Financial\nSolution','This Time’s\nTopic of\nDiscussion','Problem\nStatement\n(Main)','Impact of\nProblems','Solutions','UPV','Product /\nDemo']
red4=['Friendly\nUser\nInterface','How We Works','Target Market','Market Size','Market Trends','Business Model','Customer\nPersona','Pricing Strategy','Go-to-Market\nStrategy']
for pv,items in [(1,red1),(2,red2),(4,red4)]:
 for n,text in enumerate(items,1):
  sid=f's{pv:02}-{n:02}';cover=pv==2 and n==1;sol=text=='Solutions';color='#fff' if sol or cover else '#151515'
  x=52 if cover else 25 if text in ['Target Market','Business Model'] else 53 if text=='Market Trends' else 7
  y=34 if cover else 7 if text in ['Target Market','Business Model'] else 12 if text=='Welcome' else 18 if text in ['Solutions','How We Works','Pricing Strategy','Go-to-Market\nStrategy'] else 49 if text=='Market Size' else 17
  w=47 if cover else 73 if text in ['Target Market','Business Model','How We Works','Pricing Strategy'] else 43 if text in ['Market Trends','Go-to-Market\nStrategy'] else 49
  arr=[title(text,x,y,w,80 if text!='PAYONE' else 94,weight=700,color=color),tx('Pitchdeck',2.5,5,27,27,weight=700,color='#fff' if sol or cover or text=='Welcome' or text=='UPV' else BLACK),tx('Financial Technology',2.5,10,28,12,color='#fff' if sol or cover else '#999'),tx('PAYONE',86,5,13,24,color=RED),tx('2026',93,11,7,13,color=RED)]
  if text=='This Time’s\nTopic of\nDiscussion':arr[0]['color']='#fff';arr += [tx('Cashless is not\nthe future — it’s\nthe present.',2.5,59,33,28,weight=700,color='#fff')]+[tx(f'Session #{i+1}',77,20+i*30,22,26,weight=700) for i in range(3)]
  if text=='Problem\nStatement\n(Main)':arr += [title('70%',54,15,45,201,color=RED),title('30%',54,58,45,201,color=RED),para(3,68,32,19,lines=5)]
  if text=='Solutions':arr += [tx('It Does Not Matter How\nSlowly You Go As Long As\nYou Do Not Stop.',3,62,39,29,weight=700),para(44,21,25,18,'#fff',4),para(74,21,25,18,'#fff',4)]
  if text=='Product /\nDemo':arr += [tx('Description',3,67,28,29,weight=700),para(3,74,28,17,lines=4)]
  if text=='Market Trends':arr += [title('41%',53,39,22,70,weight=700),title('33%',78,39,22,70,weight=700,color=RED),title('14%',53,70,22,70,weight=700,color=RED),title('12%',78,70,22,70,weight=700,color='#bababa')]
  if text=='Marketing\n& Sales Plan':arr += [title('2024-2025',3,81,32,59,weight=700,color='#fff'),tx('Description',3,49,32,23,weight=700,color='#fff'),para(3,57,30,17,'#fff',4)]
  if text=='Seeking\nProfessional\nAdvice':
   for i in range(3):arr += [tx('Diana Doe',17+i*33,68,20,26,weight=700,color='#fff'),tx('Financial Expert',17+i*33,76,22,18,color='#fff')]
  if text=='Financial\nProjection\nfor 2026':arr += [title('200,000',87,33,13,37,weight=700),title('80,000',62,54,22,37,weight=700),title('30,000',48,77,22,37,weight=700)]
  if text=='Welcome':arr += [title('Seamless Payment,\nSmarter Business',9,51,82,91,weight=700,color='#fff')]
  if text=='Your Financial\nSolution':arr += [tx('Amanda Deratosa',3,65,29,24,weight=700),tx('Date and time',63,66,32,22,color='#fff'),title('December 10,\n2025',63,76,34,43,color='#fff')]
  if text=='Impact of\nProblems':arr += [title('30%',40,80,29,81,color=RED),tx('Description',3,61,31,24,weight=700)]
  if text=='UPV':arr[0]['color']='#fff';arr += [title('Small Businesses Grow,\nEconomies Thrive.',36,18,63,86,weight=700,color='#fff'),tx('Unique Value\nProposition',3,59,31,29,weight=700,color='#fff')]
  if text=='Friendly\nUser\nInterface':arr += [tx('Description',3,59,32,24,weight=700),para(3,67,32,17,lines=5)]
  if text=='How We Works':
   for i in range(4):arr += [tx(f'0{i+1}',5+i*24,40,22,47,color='#fff'),tx('Lorem ipsum',5+i*24,61,22,24,weight=700,color='#fff'),para(5+i*24,70,20,17,'#fff',3)]
  if text=='Market Size':arr += [title('65\nMillion',25,25,25,62,weight=700),title('170\nMillion',51,47,26,62,weight=700,color='#fff'),title('100\nBillion',77,66,23,62,weight=700,color='#fff')]
  if text=='Business Model':
   for i in range(4):arr += [tx(f'0{i+1}',3+i*25,37,24,44,color='#fff' if i<3 else '#111')]
  if text=='Customer\nPersona':arr += [tx('Thomas Doe',66,16,34,26,weight=700),tx('Amanda Doe',58,67,37,26,weight=700)]
  if text=='Pricing Strategy':arr += [title('$ 45.90',36,49,43,81,color='#fff'),title('$ 59.00',36,72,43,81,color='#fff'),tx('Standard',6,48,25,28,color='#fff'),tx('Premium',6,72,25,28,color='#fff')]
  if text=='Go-to-Market\nStrategy':
   for i in range(3):arr += [tx('Description',58,44+i*17,40,24,weight=700),para(58,50+i*17,38,16,lines=2)]
  if text in ['Target Market','Product /\nDemo']:
   for i in range(3):arr += [tx('Description',79 if text=='Target Market' else 77,25+i*24,21,21,weight=700),para(79 if text=='Target Market' else 77,33+i*24,20,14,lines=3)]
  setpage('p092',sid,arr,True)
# B2B chart and diagram slides, including calendar and separate testimonial cards.
B='#7749ff';O='#ff4b20'
b2b2=['B2B Pitch','Welcome to the World of B2B\nPitching Turning Business Ideas into\nStrategic Partnerships','Section Infographic','Section Infographic','Section Infographic','Section Infographic','Desember\nCalendar','','Thank You For\nAttention!!']
b2b3=['Welcome to the World of B2B\nPitching Turning Business Ideas into\nStrategic Partnerships','Winning Over\nBusinesses The Power\nof a Strong B2B Pitch','Crafting Compelling B2B\nPitches That Convert','','Meet the Team\nThat Turns Ideas\ninto Impactful\nB2B Partnerships','A Glimpse into the Future of\nB2B Communication Through\nOur Pitch Mockups','Performance and Progress\nAnalysis','Performance and Progress\nAnalysis']
for pv,items in [(2,b2b2),(3,b2b3)]:
 for n,text in enumerate(items,1):
  sid=f's{pv:02}-{n:02}';center=text.startswith('Welcome') or text.startswith('Performance') or pv==3 and n==6
  x=6 if not center else 9;y=9 if center else 12;w=88 if center else 44 if pv==3 and n==2 else 65
  if pv==2 and n==1:x=5;y=13;w=95
  if pv==3 and n==5:x=60;w=39
  if text:arr=[title(text,x,y,w,168 if pv==2 and n==1 else 73 if pv==2 and n==9 else 59,weight=400,color='#fff' if pv==2 and n==1 else B if center or pv==2 and n==9 else '#111',align='center' if center else 'left')]
  else:arr=[]
  if text.startswith('Welcome'):
   for i in range(2):arr += [tx('Subtitle here',36+i*33,47,29,30,color='#fff'),para(36+i*33,56,28,20,'#fff',3),title(f'0{i+1}',47+i*33,72,27,160,color='#fff')]
  if pv==2 and n in [3,4,5,6]:
   for i in range(4):
    if n==3:xx=42 if i%2 else 7;yy=37+i*14
    elif n==4:xx=7+i*24;yy=58 if i%2 else 28
    elif n==5:xx=7+i*24;yy=76-i*11
    else:xx=7+i*24;yy=72
    arr += [tx('Subtitle Here',xx,yy,23,22),para(xx,yy+7,22,17,lines=3)]
  if pv==2 and n==6:
   for i,v in enumerate(['50%','60%','70%','80%']):arr += [tx(v,14+i*22,31-i*3,20,37,color=[B,O,'#111',B][i])]
  if pv==2 and n==7:
   arr += [tx('Subtitle Here',58,42,37,25),para(58,49,36,18,lines=3)]
   days=['Su','Mo','Tu','We','Th','Fr','Sa']
   for i,d in enumerate(days):arr += [tx(d,5+i*7.3,18,7,17,color='#fff',align='center')]
   for j in range(5):
    for i in range(7):
     v=j*7+i;arr += [tx(str(v) if 0<v<32 else '',5+i*7.3,27+j*10,7,17,align='center')]
  if pv==2 and n==8:
   for i in range(3):arr += [tx('Subtitle here',8+i*30,19,26,29,color='#fff' if i<2 else '#111'),para(8+i*30,27,26,20,'#fff' if i<2 else '#111',4),tx('★★★★★ 4.9',8+i*30,49,26,22,color='#d4c426'),tx('Customer B2B Name',14+i*30,84,23,22,color='#fff' if i<2 else '#111')]
  if pv==2 and n==9:arr += [tx('Subtitle here',20,67,40,24),para(20,75,40,18,lines=3)]
  if pv==3 and n==2:arr += [para(4,79,44,23,lines=2)]
  if pv==3 and n==3:arr += [title('+78,1',52,42,22,75,color='#fff'),title('89,88K',76,26,24,75,color='#fff'),tx('Subtitle here',5,27,44,23),para(5,34,42,19,lines=3)]
  if pv==3 and n==4:arr += [title('+31M',35,53,28,95,color='#fff')]
  if pv==3 and n==5:arr += [title('+75%',5,26,24,80,color='#fff'),tx('★★★★★ 4.7',38,77,20,22,color='#e4d936')]
  if pv==3 and n==6:arr += [title('87%',40,49,22,122,color='#fff'),title('+49,8K',68,60,23,61,color='#fff')]
  if pv==3 and n==8:arr += [title('526+',66,28,32,68,color='#fff'),title('35%',66,60,32,68,color='#fff')]
  setpage('p101',sid,arr,True)
# Fundraising deck: compact bold condensed headings and differently colored cards.
fund2=['BUSINESS MODEL.','MARKET & SALES STRATEGY.','COMPETITIVE\nANALYSIS.','Technology / IP.','FUTURE PLANS.','FINANCIAL PROJECTIONS.','OUR TEAM.','THE ASK.','Let’s chat.']
fund3=['PITCH DECK.','MISSION\n& VISION.','PROBLEM.','MARKET\nOPPORTUNITY.','SOLUTION.','PRODUCT\nOVERVIEW.','CORE VALUES.','HOW IT WORKS.','OUR OBJECTIVE.']
for pv,items in [(2,fund2),(3,fund3)]:
 for n,text in enumerate(items,1):
  dark=pv==2 and n in [4,9] or pv==3 and n in [2,5,9];col='#fff' if dark else '#16123c';x=5 if n not in [2,6,7] or pv==3 else 12;y=10;w=89
  if pv==3 and n==1:x=6;y=29;w=51
  if pv==3 and n==6:x=56;y=20;w=44
  arr=[title(text,x,y,w,100 if pv==3 and n==1 else 90,'Anton',400,col,align='center' if pv==2 and n in [2,6,7] or pv==3 and n==8 else 'left'),tx('SLIDE.DECK',6,3,31,13,color=col),tx('PRESENTATION',43,3,36,13,color=col),tx('STRATEGY' if n==2 else 'REVENUE' if n==1 else 'BUSINESS',89,3,11,13,color=col)]
  if pv==2 and n==1:
   for i,(h,v) in enumerate([('Single Purchase','$15 – 5'),('Product Bundles','$45'),('Membership','$20/mo')]):arr += [tx(h,7+i*29,72,25,32,'Anton',align='center'),tx(v,7+i*29,86,25,26,weight=700,align='center')]
  if pv==2 and n==2:arr += [tx('Go-to-Market Approach',58,34,38,21,weight=700),para(58,43,38,17,lines=3),tx('Sales Strategy',58,64,38,21,weight=700),para(58,73,38,17,lines=4)]
  if pv==2 and n==3:
   for i,t in enumerate(['COMPETITOR','KEY STRENGTHS','KEY WEAKNESSES']):arr += [tx(t,8+i*29,52,27,17,weight=700,align='center')]
   for j,row in enumerate([['Competitor A','Established brand, large scale','Complex, not user-friendly'],['Competitor B','Low-cost accessible','Limited customization'],['Competitor C','Feature-rich','Overwhelming UX, expensive'],['Our Product','Niche focused, simple to use','Tailored, affordable, fast']]):
    for i,t in enumerate(row):arr += [tx(t,8+i*29,61+j*8,27,17,align='center')]
  if pv==2 and n==5:
   for i,t in enumerate(['Q4 2025','Q1 2026','Q2 2026','Q3 2026']):arr += [tx(t,5+(i%2)*22,37+(i//2)*34,22,29,'Anton',align='center'),para(7+(i%2)*22,49+(i//2)*34,18,15,lines=3)]
  if pv==2 and n==6:
   for i,t in enumerate(['2025','2026','2027']):arr += [tx(t,8+i*30,42,28,37,'Anton'),para(8+i*30,53,25,16,lines=3)]
  if pv==2 and n==7:
   for i,t in enumerate(['John McConnell','Harry Peace','Theo Crosby']):arr += [tx(t,7+i*30,73,25,21,weight=700,color='#fff',align='center'),para(7+i*30,85,25,14,'#fff',3)]
  if pv==2 and n==8:arr += [tx('Expand',9,35,23,35),tx('Scale',39,35,26,35),tx('Develop',39,72,26,35)]
  if pv==2 and n==9:arr += [tx('Tell us about your project\nand goals.',8,48,32,28,weight=700),para(8,65,23,16,lines=4),para(29,65,16,16,lines=4)]
  if pv==3 and n==1:arr += [tx('“ Design That Shapes\nBrands for the Digital Age',10,61,43,33)]
  if pv==3 and n==2:arr += [tx('OUR VISION.',43,74,23,33,'Anton'),para(43,84,22,15,lines=3),tx('OUR MISSION.',72,74,23,33,'Anton'),para(72,84,22,15,lines=3)]
  if pv==3 and n==3:
   for i,t in enumerate(['Inconsistent Branding','Limited Resources','Low Engagement']):arr += [tx(t,6,33+i*22,35,24,weight=700),para(6,42+i*22,32,15,lines=2)]
  if pv==3 and n==4:arr += [title('$7B+',72,20,26,76,'Anton',align='center'),title('$5B+',44,50,27,76,'Anton',align='center'),title('$5B+',72,77,27,52,'Anton',align='center'),tx('Data-Driven &\nStraightforward',8,55,31,37,color='#fff')]
  if pv==3 and n==5:
   for i,t in enumerate(['Maintain Consistent, On-Brand Content','Save Time & Resources','Engage Their Online Presence']):arr += [tx(f'STEP {i+1}',52,35+i*19,13,29,'Anton',align='center'),tx(t,65,33+i*19,31,17,weight=700),para(65,40+i*19,31,15,lines=2)]
  if pv==3 and n==6:arr += [tx('Not Just a Tool—A Solution',56,53,41,26),tx('+ Slide-based Instagram template packs\n+ Custom brand kits (logos, typography, palettes)\n+ Social media content calendars\n+ Easy-to-edit assets for non-designers',56,65,41,22,leading=1.7)]
  if pv==3 and n==7:
   for i,t in enumerate(['Purpose-Driven','Integrity','Creativity','Growth-Oriented']):arr += [tx('• '+t,69,17+i*22,29,21,weight=700),para(69,24+i*22,28,16,lines=2)]
  if pv==3 and n==8:
   for i,t in enumerate(['Phase 1:\nResearch &\nPlanning','Phase 2:\nDesign &\nDevelopment','Phase 3:\nLaunch &\nOptimization']):arr += [tx(t,9+i*30,49,27,33,weight=700),para(9+i*30,76,26,17,lines=3)]
  if pv==3 and n==9:
   for i,t in enumerate(['CREATE MEASURABLE VALUE\nTHROUGH PRODUCT/SERVICE\nFOCUS','ADDRESS AN UNDERSERVED MARKET\nWITH INNOVATIVE, USER-CENTRIC\nSOLUTIONS','CREATE SUSTAINABLE GROWTH FOR OUR\nSTAKEHOLDERS AND COMMUNITY.']):arr += [tx(f'0{i+1}.',8,39+i*22,8,39,'Anton'),tx(t,17,37+i*22,31,19,leading=1.3)]
  setpage('p104',f's{pv:02}-{n:02}',arr,True)
# Brand Proposal is built as the same visible fine ruled grid, with distinct regions for every page.
brand2=['PRODUCT MOCKUP','BRAND\nPROPOSAL','BRAND IDENTITY','THANK        YOU'];brand5=['BRAND\nPROPOSAL','BRAND IDENTITY','BRAND CULTURE','BRAND VISION','BRAND PHILOSOPHY','BRAND GOALS','BRAND STORY','BRAND VALUES','MARKETING SUPPORT']
for pv,items in [(2,brand2),(5,brand5)]:
 for n,text in enumerate(items,1):
  dark=pv==2 and n in [2,3,4] or pv==5 and n<=3;col='#fff' if dark else '#211815'
  x,y,w,size=(24,43,55,124) if text=='BRAND\nPROPOSAL' else (50,25,46,75) if text=='PRODUCT MOCKUP' else (6,61,90,166) if pv==2 and n==4 else (39,17,54,68) if text=='MARKETING SUPPORT' else (41,83,52,67) if text in ['BRAND PHILOSOPHY','BRAND VALUES'] else (6,81,89,67) if text in ['BRAND STORY','BRAND VISION'] else (31,40,66,67)
  arr=[title(text,x,y,w,size,weight=700,color='#2f211b' if text=='BRAND\nPROPOSAL' else col,align='center' if text in ['BRAND\nPROPOSAL','BRAND GOALS','MARKETING SUPPORT'] else 'left'),tx('BRAND PROPOSAL',42,4,33,20,weight=700,color=col),tx('202\n5',91,4,6,16,weight=700,color=col),ic(4,4,3,5,'Menu',col),ic(95,4,3,5,'ArrowUpRight',col)]
  if text=='BRAND\nPROPOSAL':arr += [tx('POWERFUL\nMARKETING SUPPORT',7,24,27,28,weight=700,color='#fff'),tx('2026',10,94,15,20),tx('PRESENTATION',50,94,37,20)]
  if text=='PRODUCT MOCKUP':arr += [para(53,48,38,26,'#777',4),para(53,74,38,26,'#777',4),ic(45,47,5,9,'UserRoundCheck'),ic(45,72,5,9,'ChartNoAxesCombined')]
  if text=='BRAND IDENTITY':arr += [tx('Creating Strong Recognition',42,30,25,26,weight=700,color='#fff',align='center'),para(42,41,25,24,'#c9c1ba',4),tx('Effective Identity Strategy',42,69,25,26,weight=700,color='#fff',align='center'),para(42,79,25,21,'#c9c1ba',4),tx('Unified Brand Communication',73,17,25,23,weight=700,color='#fff'),para(73,31,24,21,'#c9c1ba',4)]
  if text=='BRAND CULTURE':
   for i in range(4):arr += [tx('ABCD'[i]+'.',57,24+i*18,7,44,weight=700,color='#fff'),para(65,24+i*18,32,21,'#c9c1ba',3)]
  if text=='BRAND VISION':arr += [tx('Inspiring\nGrowth\nThrough Shared\nVision',10,29,26,24,weight=700),para(48,25,46,21,'#777',3),tx('Building Trust Across Every\nTouchpoint',48,68,45,24,weight=700),para(48,79,46,21,'#777',3)]
  if text=='BRAND PHILOSOPHY':arr += [title('86,2%',10,31,23,48,weight=700),title('92,2%',76,31,24,48,weight=700),tx('Passion Fuels Innovation',6,43,27,22,weight=700,align='center'),tx('Principles Lead Forward',75,43,24,22,weight=700,align='center'),para(7,53,26,22,'#999',6),para(75,53,23,22,'#999',6)]
  if text=='BRAND GOALS':arr += [title('+750K',6,61,26,50,weight=700,align='center'),title('+125K',76,61,24,50,weight=700,align='center'),para(6,73,25,22,'#999',4),para(76,73,23,22,'#999',4)]
  if text=='BRAND STORY':arr += [para(12,31,41,24,'#999',5),tx('›  More Information...',12,64,41,24,weight=700),tx('Transforming Ideas Into\nLasting Brands',70,83,26,24,weight=700,align='right')]
  if text=='BRAND VALUES':
   for i in range(3):arr += [ic(7,24+i*13,5,7,['Target','Medal','ChartColumn'][i]),para(12,24+i*13,37,20,'#999',2)]
  if text=='MARKETING SUPPORT':
   for i,t in enumerate(['Powerful Marketing Support','Marketing Support Solutions','Marketing Support Strategy']):arr += [tx(t,6+i*31,41,30,20,weight=700,align='center'),ic(16+i*31,56,8,12,['PanelsTopLeft','HandCoins','Store'][i]),para(6+i*31,70,29,21,'#999',3),tx('More Information...',6+i*31,87,29,20,weight=700,align='center')]
  setpage('p107',f's{pv:02}-{n:02}',arr,True)
# Semantic diagram additions supersede rounded contour seeds completely.
for key,page in raw.items():
 did,sid=key.split('/');
 if did in EXTRA:continue
 if did=='p069':
  green='#acd82d';add=[]
  if sid in ['s01-01','s03-01']:add=ring(-13,-21,51,91,[100],[green],.73)+ring(-26,21,51,91,[100],[green],.73)
  if sid in ['s01-02','s03-02']:add=ring(-8,-8,38,68,[100],[green],.78)+ring(3,43,42,74,[100],[green],.78)
  if sid in ['s01-03','s03-03']:add=ring(18,-13,24,43,[100],[green],.75)+ring(-8,53,42,74,[100],[green],.8)
  if sid in ['s01-04','s04-02']:add=ring(-4,-16,32,57,[100],[green],.76)+ring(71,53,31,55,[100],[green],.76)
  if sid in ['s01-06','s03-04']:add=ring(0,30,26,46,[100],[green],.75)+ring(0,64,26,46,[100],[green],.75)
  if sid in ['s01-07','s04-04']:add=ring(70,5,36,64,[100],[green],.8)+ring(-8,61,33,59,[100],[green],.8)
  if sid in ['s01-08','s04-03']:add=ring(71,-19,34,60,[100],[green],.8)
  if sid=='s02-01':add=ring(73,42,45,80,[100],[green],.82)
  if sid=='s02-02':add=ring(-8,-12,32,57,[100],[green],.83)+ring(77,66,31,55,[100],[green],.83)
  if sid=='s02-08':add=ring(-14,28,35,63,[100],[green],.81)
  if sid=='s04-06':add=ring(70,34,27,48,[100],[green],.8)+ring(85,48,34,61,[100],[green],.8)
  page['elements']=add+page['elements']+[ic(83,4,4,5,'Link2',green),tx('Problem Statement',87,5,12,14,color='#111' if page['background']>'#888888' else '#fff'),tx('Problem Statement   |   2026',5,94,50,14,color='#111' if page['background']>'#888888' else '#fff')]
 if did=='p081':
  if sid in ['s04-04','s05-08']:page['elements']=ring(13,36,31,55,[17,30,23,30],['#181919','#d9d5c5','#f6f5ef','#8d8d87'],.67)+page['elements']
  if sid=='s02-03':page['elements']=ring(67,31,27,48,[50,21,20,9],['#d7d4c9','#333333','#8a8a85','#c9c9c3'],0)+page['elements']
  if sid=='s02-06':page['elements']=[box(0,0,100,100,'#dcd7c9'),box(21,23,58,55,'#343432')]+page['elements']
  if sid in ['s05-06','s05-09']:
   page['elements']=[path([[49,17],[49,93]],'#d8d7d1',1)]+page['elements']
   for i in range(2 if sid=='s05-06' else 3):page['elements'] += [ic(45,46+i*25 if sid=='s05-06' else 12+i*29,8,12,['Lightbulb','HandCoins','Network'][i])]
 if did=='p092':
  if sid in ['s01-06','s04-05']:page['elements']=ring(4,25,34,60,[41,33,14,12],['#171717',RED,'#eb796f','#bfbfbf'],.54)+page['elements']
  if sid=='s04-07':page['elements']=ring(3,39,24,43,[70,30],['#171717',RED],.46)+page['elements']
  if sid=='s04-09':page['elements']=[box(13,21,27,48,'#171717','50%'),box(0,52,27,48,'#bababa','50%'),box(27,52,27,48,RED,'50%')]+page['elements']
 if did=='p091' and sid=='s03-12':page['elements']=ring(32,34,34,60,[25,25,25,25],[Q,qp,Q,qp],.42)+page['elements']
 if did=='p050' and sid in ['s02-02','s02-03','s02-04','s02-06','s02-10','s02-11','s02-12']:page['elements']+=[ic(5 if sid!='s02-02' else 48,78 if sid in ['s02-02','s02-03','s02-12'] else 5,8,13,'CircleArrowRight','#fff')]
 if did=='p107':
  # Clean rule lines, never pixel contours around letters.
  color='#baafa8' if page['background']<'#888888' else '#bdb7b1';page['elements']=[path([[0,11],[100,11]],color,1)]+page['elements']
 if did=='p104':page['elements']+=[ic(2,3,2,3,'Asterisk','#f06c64')]
# Ensure coordinates are plain finite values, and semantic data includes no references or raster source.
output={k:v for k,v in raw.items() if k.split('/')[0] not in EXTRA}
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(output,ensure_ascii=False))
(ROOT/'src/decks/group-b.ts').write_text("import type { Deck, Slide } from '../model'\nimport {D} from '../primitives'\nimport pages from './group-b-data.json'\nconst data=pages as unknown as Record<string,Slide>\nexport default [\n"+',\n'.join("D("+json.dumps(d['id'])+','+json.dumps(d['title'])+",["+','.join("data["+json.dumps(d['id']+'/'+s['id'])+"]" for s in d['slides'])+"])" for d in manifest if d['id'] not in EXTRA)+"\n] satisfies Deck[]\n")
(ROOT/'review/group-b-typography-repairs.json').write_text(json.dumps(fixes,ensure_ascii=False,indent=2))
print('authored independent pages',len(output),'elements',sum(len(p['elements'])for p in output.values()))
