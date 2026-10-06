import json,math,pathlib,textwrap
ROOT=pathlib.Path(__file__).resolve().parents[1]
manifest=[d for d in json.load(open(ROOT/'public/reference/groups/b.json')) if d['id'] in ['p055','p060','p100','p105']]
DATA={}; NOTES={}
FONT='Roboto';E=[]
def text(x,y,w,h,t,size=2,color='#222',weight=400,align='left',font=None,lh=1.2):
 E.append(dict(kind='text',x=x,y=y,w=w,h=h,text=t,size=size*12.8,font=font or FONT,color=color,weight=weight,align=align,lineHeight=lh))
def box(x,y,w,h,c,r=0,border=None):
 e=dict(kind='box',x=x,y=y,w=w,h=h,fill=c,radius=r)
 if border:e['border']=border
 E.append(e)
def chip(x,y,w,h,t,size,c,fg='#fff',weight=500,r=5,font=None):E.append(dict(kind='chip',x=x,y=y,w=w,h=h,text=t,size=size*12.8,fill=c,color=fg,weight=weight,font=font or FONT,radius=r,lineHeight=1,align='center'))
def icon(x,y,w,h,name,c='#222'):
 if name in ['Facebook','Twitter','Youtube','Instagram']: image(x,y,w,h)
 else:E.append(dict(kind='icon',x=x,y=y,w=w,h=h,icon=name,color=c,strokeWidth=1.5))
def image(x,y,w,h):E.append(dict(kind='image',x=x,y=y,w=w,h=h,text='Image placeholder'))
def path(p,c='#aaa',fill=None,sw=1):E.append(dict(kind='path',x=0,y=0,w=100,h=100,points=[dict(x=x,y=y) for x,y in p],color=c,fill=fill,closed=bool(fill),strokeWidth=sw))
def line(x1,y1,x2,y2,c='#ddd',sw=1):path([(x1,y1),(x2,y2)],c,sw=sw)
def circle(cx,cy,r,c,border=None):box(cx-r,cy-r*16/9,2*r,2*r*16/9,c,999,border)
def arc(cx,cy,r,a,b,c,sw=3):path([(cx+r*math.cos(t),cy+r*16/9*math.sin(t)) for t in [math.radians(a+(b-a)*i/50) for i in range(51)]],c,sw=sw)
def sector(cx,cy,r,ri,a,b,c):path([(cx+r*math.cos(math.radians(a+(b-a)*i/30)),cy+r*16/9*math.sin(math.radians(a+(b-a)*i/30))) for i in range(31)]+[(cx+ri*math.cos(math.radians(b-(b-a)*i/30)),cy+ri*16/9*math.sin(math.radians(b-(b-a)*i/30))) for i in range(31)],c,c,0)
def hexagon(cx,cy,r,c,pointy=False,border=None):
 p=[(cx+r*math.cos(math.radians(i*60+(30 if pointy else 0))),cy+r*16/9*math.sin(math.radians(i*60+(30 if pointy else 0)))) for i in range(6)]
 path(p,border or c,c,2 if border else 0)
def para(x,y,w=22,h=17,size=1.45,color='#666',align='left',t=None):text(x,y,w,h,t or 'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit,\nsed do eiusmod tempor\nincididunt ut labore.',size,color,align=align)
def save(d,s,bg='#fff',title=''):
 DATA[d+'/'+s]=dict(id=s,title=title or s,background=bg,elements=list(E));NOTES[d+'/'+s]='Small reference body text is illegible: replaced with normal lorem ipsum of comparable line count; chart values approximated where unreadable.'
BLUE=['#0789bb','#105775','#2aa8df','#a3a3a3','#424242'];GREEN=['#3db58b','#00675c','#d9ad00','#bfbc00'];LAMP=['#242b75','#ed8737','#a7d900','#df6375','#0937e8','#36c800']
def heading55(center=False):text(4 if not center else 0,4,92 if not center else 100,8,'Capital Budgeting Infographics',3.5,weight=700,align='center' if center else 'left');text(4 if not center else 0,13,92 if not center else 100,4,'Enter your text headline here',1.35,align='center' if center else 'left')
def bars(x,y,w,h,values,cols=None,labels=True):
 for j in range(6):
  line(x,y+h-j*h/5,x+w,y+h-j*h/5,'#d8dcdd',1)
  if labels:text(x-5,y+h-j*h/5-1.5,4,3,str(j*10)+'%',.9,'#6d7274',align='right')
 bw=w/(len(values)*1.8)
 for i,v in enumerate(values):
  xx=x+3+i*(w-4)/len(values);box(xx,y+h-v*h/60,bw,v*h/60,(cols or BLUE)[i%len(cols or BLUE)])
  if labels:text(xx-2,y+h+2,bw+4,4,str(i+1).zfill(2),1.1,align='center')
def table(x,y,w,h,cols,rows,header=True,mode='standard'):
 cw=w/cols;rh=h/rows
 for r in range(rows):
  for c in range(cols):
   if mode=='phase' and r==rows-1:
    if c==0:box(x,y+r*rh,w,rh,'#777');chip(x,y+r*rh,w,rh,'Placeholder text',1.3,'transparent','#fff',600,0)
    continue
   colored=r==0 or (mode=='matrix' and c==0) or (mode=='finance' and r>=rows-3) or (mode=='phase' and r==rows-1)
   co=([BLUE[0],BLUE[1],BLUE[2],BLUE[3],BLUE[0],BLUE[4]][r] if mode=='matrix' and c==0 else BLUE[c%5]) if colored else (['#e4f0f5','#e0ebef','#e8f6fb','#f1f1f1'][c%4] if r%2 else '#fbfbfb')
   box(x+c*cw,y+r*rh,cw,rh,co,border='0.5px solid #d2dce1')
   t='Placeholder text' if colored else (('Your own text' if mode=='phase' else 'Write your text here') if c==0 else str(100+(r*13+c*7)%70) if mode=='finance' else str((r+c)%7))
   if mode=='matrix' and r and c:t='You can replace this text with\nyour own clear description here.'
   chip(x+c*cw,y+r*rh,cw,rh,t,1.5 if colored else 1.3,'transparent','#fff' if colored else '#626a70',600 if colored else 400,0)

for i in range(1,17):
 E=[];FONT='Roboto';center=i in [3,4,7,9,11,12,14,15,16];heading55(center)
 if i==1:
  for j in range(4):
   y=23+j*18;box(4,y,88,15,'#f2f2f2',4)
   pts=[(67-j*6,y),(74+j*5,y),(79+j*6,y+15),(62-j*6,y+15)];path(pts,BLUE[j],BLUE[j],0);icon(67,y+4,6,10,['ChartNoAxesCombined','Network','Users','ChartColumn'][j], '#d0e8f3');
   text(6,y+3,41,4,'You can replace this text with your own text' if j==0 else 'Place your own text',1.5,weight=500)
   if j:para(6,y+7,42,10,1.15,t='For simple explanations. This is a sample text for financial analysis.\nCreate a clear narrative with useful insights and decision frameworks.')
 elif i==2:
  text(4,23,43,5,'You simply add your own',1.8,weight=700);para(4,29,43,14,1.3,t='You simply add your own text and description here.\nThe screen has sections to give content. A simple starting point\nfor your presentation. Keep your ideas clear and your\naudience focused on the information.');box(4,44,43,25,BLUE[0]);icon(7,49,7,13,'Target','#fff');text(17,47,24,9,'79%',4.1,'#fff',700);para(17,56,28,11,1.1,'#eaf5ff',t='You can add your own text here.\nThis content is a short description of the\nfinancial overview.');
  for j in range(2):box(4+j*22,70,21,23,'#fff',border='1px solid #ddd');text(6+j*22,77,19,5,'Text Placeholder',1.7,weight=700);para(6+j*22,82,19,10,1.2,t='A financial text goes here.\nYour key information and data.\nThis is a sample text.')
  box(71,43,5,34,'#444',99);chip(71,53,5,13,'Title',1.15,'transparent')
  for j in range(3):
   for k in range(2):chip(52+k*28,27+j*25,16,15,'You can use this\ncontent',1.45,BLUE[(j*2+k)%5],r=99);line(68 if k==0 else 76,34+j*25,71 if k==0 else 80,34+j*25,'#aaa');line(70 if k==0 else 77,35,70 if k==0 else 77,84,'#aaa')
 elif i in [3,13,15]:table(4,22,92,71,4 if i!=15 else 3,17 if i==15 else 14 if i==3 else 6,mode='matrix' if i==13 else 'finance' if i==15 else 'standard')
 elif i==4:
  for j in range(7):
   a=-115+j*360/7;sector(50,50,16,15.3,a,a+49,BLUE[j%5]);x=50+12*math.cos(math.radians(a+24));y=50+12*16/9*math.sin(math.radians(a+24));circle(x,y,3,BLUE[j%5]);icon(x-1.4,y-2.5,2.8,5,['Target','BarChart3','Users','CalendarDays','Archive','CircleDollarSign','Network'][j],'#def3fc')
  circle(50,50,8,'#f2f2f2');chip(43,43,14,14,'Add Text Here\nThis is a sample text\nplaceholder',1.35,'transparent','#333',500,0)
  for j,(x,y) in enumerate([(6,23),(4,46),(6,69),(70,23),(72,46),(70,69),(38,86)]):chip(x,y,24,10,'You simply add your own\ntext and description here',1.3,BLUE[j%5],r=4)
 elif i==5:
  for j in range(5):
   y=53-j*8.5;box(4+j*18.6,y,18,39+j*8.5,'#efefef');chip(4+j*18.6,y,18,6.8,'Add Description',1.25,BLUE[j%4],r=0);para(6+j*18.6,y+10,14,34+j*8.5,1.45,align='center',t='\n'.join(textwrap.wrap('You can use this content in any context where you are delivering a creative and meaningful message. For example, write about management and share information for useful insights and better ideas. Use clear financial information to develop a simple story for your audience and provide meaningful details for the project.',18)[:7+2*j]));line(7+j*18.6,91,19+j*18.6,91,BLUE[j%4],1)
 elif i==6:
  bars(8,23,48,53,[55,38,49,27,55],[BLUE[0],BLUE[1],BLUE[2],BLUE[3],BLUE[0]]);
  for j in range(4):
   chip(59,22+j*20,36,15,'',1,BLUE[j],r=99);circle(62.5,29.5+j*20,3,'#fff');icon(60.5,26+j*20,4,7,['CircleDollarSign','Boxes','Flower','Network'][j],BLUE[j]);text(66,24+j*20,27,4,'Description Text',1.6,'#fff',500);para(66,28.5+j*20,27,7,1.15,'#fff',t='You can add text and information here to explain\nthe key financial information.')
  for j in range(4):text(4+j*13,86,14,5,'Phase 0'+str(j+1),1.65,weight=500,align='center')
 elif i==7:
  for j in range(5):box(4+j*18.6,25,17.8,30,'#f4f4f4');chip(5+j*18.6,23,15.5,6,['First stage','Second stage','Third stage','Fourth stage','Last stage'][j],1.1,BLUE[j%4],r=99);para(6+j*18.6,32,14,21,1.15,align='center')
  for j in range(4):x=4+(j%2)*46;y=59+(j//2)*19;box(x,y,44,17,'#f4f4f4');circle(x+5,y+8,3,BLUE[0]);icon(x+3.5,y+5.5,3,5,'CircleDollarSign','#fff');text(x+10,y+3,33,4,'This text is fully editable',1.5,weight=700);para(x+10,y+8,33,9,1.1,t='All information and your presentation can be edited\nfor clear statements and useful information here.')
 elif i==8:
  box(4,21,20,71,BLUE[1]);circle(14,45,4.5,'#fff');icon(11,40,6,10,'TriangleAlert','#999');text(7,58,14,9,'You can use this\ncontent',1.6,'#fff',600,'center');para(6,70,16,20,1.15,'#fff','center')
  for j in range(5):x=34+j*13.4;circle(x,57,5.2,BLUE[j%4]);arc(x,57,6.7,0,360,'#dedede',1);icon(x-2.8,52,5.6,10,['ClipboardList','Network','FileText','Bike','Files'][j],'#e0f4ff');y=26 if j%2==0 else 75;text(x-7,y,14,5,'Description Text',1.25,weight=600,align='center');para(x-7,y+5,14,12,1.05,align='center',t='Your key information here\nwith a short description\nand clear financial insights\nfor your audience.')
 elif i==9:
  for j in range(7):x=14+j*10.5;y=21 if j%2==0 else 58;chip(x,y,9,35,'',1,BLUE[j%5],r=99);circle(x+4.5,y+7 if j%2==0 else y+28,3.6,'#fff');chip(x+.7,y+1 if j%2==0 else y+22,7.6,12,str(j+1).zfill(2),1.7,'transparent','#333');text(x+2,y+13 if j%2==0 else y+1,5,18,'Add text\nhere',1.1,'#fff',align='center')
  path([(4,54),(10,46),(10,50),(90,50),(90,46),(96,54),(90,62),(90,58),(10,58),(10,62)],'#ddd','#ddd',0);text(20,52,60,5,'For example, if you are writing a paper about writing techniques',1.35,align='center')
 elif i==10:
  box(4,21,1.5,73,BLUE[2]);line(18.5,21,18.5,93,'#aaa');
  for j,v in enumerate([44,38,34,30,25,24,22,20]):text(6,23+j*9,12,5,'Add Text Here',1.25);box(18.5,24+j*9,v,6,BLUE[1]);text(19.5,25+j*9,8,4,str(v)+'%',1,'#dff3fb')
  box(64,21,3.5,73,'#aaa');
  for j in range(4):icon(64.7,24+j*18,2,4,'Circle','#eee');text(70,24+j*18,26,4,'Replace with your own text',1.4,weight=600);para(70,29+j*18,25,12,1.1,t='You can add information. This is a sample text for\nyour content. Use your own information with\ncreative insights and financial knowledge.')
 elif i==11:
  for j in range(5):box(4+j*18.5,23,17.5,35,'#eaf2f6');bars(7+j*18.5,27,13,24,[48,53,48],BLUE[:3]);chip(5+j*18.5,58,15.5,6,'Your own text',1.1,BLUE[j%4],r=99)
  text(4,70,40,5,'You can use this content',1.6,weight=600);para(4,76,38,17,1.1,t='You can use this content in any context when you are adding a\ncreative and meaningful message. For example in your\nfinancial reports or insights presentation, use this content\nand give a clear overview of your project.');
  for j in range(2):chip(55,72+j*13,40,10,'',1,BLUE[1] if j==0 else '#aaa',r=99);chip(56,73+j*13,34,8,'70' if j==0 else '60',1.25, 'transparent','#ddd',r=99);text(43,75+j*13,11,8,'Replace with\nyour own text',1.1,align='right')
 elif i==12:
  for j in range(8):x=4+(j%4)*23.5;y=23+(j//4)*44;chip(x,y,21.5,26,'You simply add your own\ntext and description here.\nThis text is fully editable',1.45,BLUE[[0,1,2,3,0,4,1,0][j]],r=28)
  chip(21,53,57,10,'You simply add your own text and description here',1.45,'#555',r=99)
 elif i==14:
  for j in range(4):x=4+j*23.4;table(x,22,22,46 if j!=1 else 73,2,9 if j!=1 else 15,mode='phase');chip(x,22,22,5,'Phase 0'+str(j+1),1.4,BLUE[j],r=0)
  text(8,77,17,5,'Text Placeholder',1.35,align='center');para(5,82,21,11,1.05,align='center');text(51,73,41,5,'Text Placeholder',1.6);para(51,78,43,15,1.15,t='Place your own information.          Your own text here\n\nSample text     +                   Sample text     +\n\nSample text     +                   Sample text     +')
 elif i==16:
  circle(50,56,13.5,'#f8f8f8');
  for j in range(4):sector(50,56,18,17,-135+j*90,-47+j*90,BLUE[j]);sector(50,56,11.5,11,-135+j*90,-47+j*90,BLUE[j]);a=math.radians(-90+j*90);icon(48+14*math.cos(a),52+25*math.sin(a),4,8,['Users','Banknote','Network','LockKeyhole'][j],BLUE[j])
  chip(40,49,20,13,'You simply add\nyour own',1.7,'transparent','#333',600,0)
  for j in range(4):x=4+(j%2)*67;y=22+(j//2)*52;box(x,y,24,23,'#f6f6f6',4);text(x+2,y+3,21,4,'Write your Title here',1.55,weight=700);para(x+3,y+7,20,14,1.3,t='• You simply add your own text\n  and description here. This text\n  is fully editable.')
 save('p055',f's02-{i:02}',title='Capital Budgeting Infographics')
H60=['Balancing Six Elements','The Power of Hexagon','Pillar of Strength','The Hexagonal Key','Hexagonal Framework','A Hexagonal Approach','A Hexagonal Approach','Honeycomb Happenings','The Hexagonal Key','Connecting the Dots','A 6-Step Plan','The Power of Hexagon','Six Key Ingredients','Six Sides of Success','A Hexagonal Exploration','Hexagonal Infographic']
def htext(x,y,w=22,c='#3fa88a',align='left',sz=1.6):text(x,y,w,4,'Your Text Here',sz,c,600,align)
def hbody(x,y,w=22,h=12,c='#888',align='left'):
 content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
 rows=2 if h<9 else 3;cols=max(20,int(w/(1.2*.55)));t='\n'.join(textwrap.wrap(content,cols)[:rows]);para(x,y,w,h,1.2,c,align,t=t)

def badgehex(cx,cy,r,c,lab=None,ico=None):
 hexagon(cx,cy,r+1,'#f2f2f2');hexagon(cx,cy,r,c)
 if lab:chip(cx-r*.7,cy-r*.6*16/9,r*1.4,r*1.2*16/9,lab,2.6,'transparent','#fff',600,0)
 if ico:icon(cx-r*.48,cy-r*.85,r*.96,r*1.7,ico,'#fff')
for i in range(1,17):
 E=[];FONT='Montserrat';text(4,9,92,10,H60[i-1] if i!=13 else '',3.55,'#393b3a',700,'center');text(6,94,35,4,'Hexagonal Infographic',.95,'#9c9c9c');text(90,94,4,4,str(22-i),1,'#aaa');
 if i in [1,5,9,13]:# missing left part is reconstructed, retaining visible right text and objects
  pass
 if i==1:
  cx,cy,r=50,53,16
  hexagon(cx,cy,r+1.5,'#f4f4f4',True)
  for j in range(6):
   a=-90+j*60;p=[(cx+6*math.cos(math.radians(a)),cy+6*16/9*math.sin(math.radians(a))), (cx+r*math.cos(math.radians(a)),cy+r*16/9*math.sin(math.radians(a))),(cx+r*math.cos(math.radians(a+60)),cy+r*16/9*math.sin(math.radians(a+60))),(cx+6*math.cos(math.radians(a+60)),cy+6*16/9*math.sin(math.radians(a+60)))];co=[GREEN[0],GREEN[1],GREEN[2],GREEN[3],'#7975ad','#0996b5'][j];path(p,co,co,0);aa=math.radians(a+30);chip(cx+11*math.cos(aa)-3,cy+11*16/9*math.sin(aa)-4,6,8,str(j+1).zfill(2),2.5,'transparent',r=0)
  icon(47,48,6,11,'House','#777')
  for j in range(6):x=5 if j>2 else 71;y=23+(j%3)*24;co=[GREEN[0],GREEN[1],GREEN[2]][j%3];htext(x,y,23,co);hbody(x,y+5,23,10);line(28 if j>2 else 66,y+4,34 if j>2 else 69,y+4,co)
 elif i==2:
  for j,(x,y) in enumerate([(26,43),(50,66),(74,43)]):
   badgehex(x,y,11,GREEN[j]);badgehex(x,y-18,3,GREEN[j],str(j+1).zfill(2));htext(x-9,y-6,18,'#fff','center');para(x-8,y,16,16,1.3,'#e1f6ed','center',t='Lorem ipsum dolor\nsit amet, consectetur\nadipiscing elit, sed\ndo eiusmod tempor.');line(x,y+18 if j!=1 else y-18,x,y+26 if j!=1 else y-26,GREEN[j]);badgehex(x,y+34 if j!=1 else y-38,4.5,GREEN[j],ico=['Rocket','Zap','FlaskConical'][j])
 elif i==3:
  for j in range(4):cx=19+j*22;hexagon(cx,54,10.3,GREEN[j],True);box(cx-9,31,18,47,GREEN[j]);path([(cx-9,31),(cx,21),(cx+9,31)],GREEN[j],GREEN[j],0);path([(cx-9,78),(cx,88),(cx+9,78)],GREEN[j],GREEN[j],0);y=35 if j%2==0 else 73;hexagon(cx,y,7,'#fff',True);circle(cx,y,4.5,'#fff');icon(cx-3,y-5,6,10,['HandCoins','HandHeart','Building2','Cpu'][j],GREEN[j]);yy=53 if j%2==0 else 30;htext(cx-8,yy,16,'#fff','center',1.4);para(cx-8,yy+6,16,21,1.3,'#fff',t='➊ Lorem ipsum dolor\n   sit amet, consectetur\n   adipiscing elit.\n\n➋ Lorem ipsum dolor\n   sit amet, consectetur\n   adipiscing elit.')
 elif i==4:
  for j in range(3):cx=17+j*22;badgehex(cx,43,9,GREEN[j]);path([(cx-1,33),(cx+5,33),(cx+8,43),(cx+5,53),(cx-1,53)],'#fff','#fff',0);chip(cx,35,6,16,str(j+1).zfill(2),2.9,'transparent',GREEN[j],700,0);icon(cx-6,39,4,8,['TreePine','Sprout','Flower2'][j],'#d1eee1');htext(cx-9,61,18,GREEN[j],'center');hbody(cx-9,66,18,11,align='center');chip(cx-9,78,18,6,['90%  |  340','80%  |  200','84%  |  250'][j],2,'transparent','#333',600,0)
 elif i==5:
  for j in range(2):y=31+j*34;path([(5,y-4),(55,y-4),(60,y+11),(55,y+27),(5,y+27)],'#f4f4f4',None,1);htext(30,y);hbody(30,y+6,28,17)
  badgehex(78,33,7.5,GREEN[2]);circle(78,33,4,'#fff');icon(75,28,6,10,'Wheat',GREEN[2]);htext(70,49,16,GREEN[2],'center');para(72,55,13,29,1.05,'#888',align='center',t='Lorem ipsum dolor\nsit amet, consectetur\nadipiscing elit, sed\ndo eiusmod tempor\nincididunt ut labore\net dolore magna\naliqua. Ut enim ad\nminim veniam.')
 elif i==6:
  for j,(x,y) in enumerate([(16,44),(38,66),(60,44),(82,66)]):hexagon(x,y,11,'#f5f5f5',True);hexagon(x,y,9,GREEN[j],True);badgehex(x,y-12,2.5,'#fff',str(j+1).zfill(2));chip(x-2,y-16,4,8,str(j+1).zfill(2),1.3,'transparent',GREEN[j],600,0);htext(x-8,y-1,16,'#fff','center');para(x-7,y+4,14,11,1.25,'#fff','center',t='Lorem ipsum dolor\nsit amet, consectetur\nadipiscing elit.')
 elif i==7:
  for j in range(3):x=16+j*13;y=32+j*23;path([(x,y-10),(x+43,y-10),(x+47,y),(x+43,y+10),(x,y+10)],'#f4f4f4','#f4f4f4',0);badgehex(x,y,6,GREEN[j]);hexagon(x,y,4,'#fff');icon(x-2.5,y-4.5,5,9,['HandHeart','Cpu','Building2'][j],GREEN[j]);htext(x+9,y-6,33,'#333');hbody(x+9,y,35,12)
 elif i==8:
  for j,(x,y,lab) in enumerate([(20,39,'150'),(38,46,'340'),(27,71,'200')]):badgehex(x,y,9,GREEN[j]);path([(x-6,y),(x+6,y),(x+6,y+8),(x,y+14),(x-6,y+8)],'#fff','#fff',0);chip(x-6,y+1,12,11,lab,3.1,'transparent',GREEN[j],700,0);text(x-7,y-6,14,4,'Your Text Here',1.4,'#fff',align='center')
  for j in range(3):circle(60,39+j*19,3,GREEN[j]);icon(58.5,36+j*19,3,6,['User','Sprout','Flower2'][j],'#fff');htext(65,33+j*19,25,GREEN[j]);hbody(65,39+j*19,25,9)
 elif i==9:
  for j,(x,y) in enumerate([(20,47),(41,61),(59,47),(77,61)]):badgehex(x,y,8,GREEN[j]);circle(x,y,4.3,'#fff');icon(x-2.5,y-4.5,5,9,['Leaf','Wheat','Building2','CloudSun'][j],GREEN[j]);htext(x-9,76 if j%2==0 else 26,18,GREEN[j],'center');hbody(x-10,81 if j%2==0 else 32,20,11,align='center');line(x,y+16 if j%2==0 else y-16,x,y+21 if j%2==0 else y-22,GREEN[j]);
  line(20,47,41,61,GREEN[1],5);line(41,61,59,47,GREEN[2],5);line(59,47,77,61,GREEN[3],5)
 elif i==10:
  pts=[(18,36),(39,59),(53,32),(70,53),(61,80)];
  for j in range(4):line(*pts[j],*pts[j+1],'#75c5a8',1.5)
  for j,(x,y) in enumerate(pts):badgehex(x,y,8 if j==0 else 4.8,GREEN[0]);icon(x-3 if j==0 else x-2,y-5 if j==0 else y-3.5,6 if j==0 else 4,10 if j==0 else 7,['Recycle','ShoppingBag','PlugZap','Fuel','House'][j],'#fff');htext(x-10 if j==0 else x+6,y+19 if j==0 else y-5,20);hbody(x-10 if j==0 else x+6,y+24 if j==0 else y+1,20,13)
 elif i==11:
  for j in range(6):x=10+(j//3)*46;y=33+(j%3)*22;badgehex(x+3,y,6,GREEN[0] if j<3 else GREEN[2]);hexagon(x,y,4,'#fff');icon(x-2.5,y-4.5,5,9,['House','ShoppingBag','Recycle','Fuel','PlugZap','User'][j],GREEN[0] if j<3 else GREEN[2]);htext(x+14,y-6,29,GREEN[0] if j<3 else GREEN[2]);hbody(x+14,y,29,10)
 elif i==12:
  for j,(x,y,v) in enumerate([(20,61,'90%'),(34,47,'60%'),(60,61,'35%'),(74,47,'80%')]):badgehex(x,y,9,GREEN[0] if j<2 else GREEN[2]);icon(x-2,y-9,4,8,['Files','Wheat','Heart','Lightbulb'][j],'#def1e8');chip(x-7,y+1,14,8,v,3.2,'transparent','#fff',600,0);text(x-7,y+9,14,4,'Your Text Here',1.3,'#e5f0eb',align='center');htext(x-10,20 if j%2 else 80,20,GREEN[0] if j<2 else GREEN[2],'center');hbody(x-10,25 if j%2 else 85,20,8,align='center')
 elif i==13:
  circle(50,51,12,'#fafafa');text(42,44,16,17,'Six Key\nIngredients',2.5,'#333',700,'center')
  for j in range(6):a=math.radians(-90+j*60);x=50+13*math.cos(a);y=51+13*16/9*math.sin(a);circle(x,y,3.3,GREEN[j%4]);icon(x-1.5,y-3,3,6,['TreePine','Sprout','Flower2','CookingPot','Wheat','Leaf'][j],'#fff');xx=44 if j in [0,3] else (x+5 if j<3 else x-27);yy=y-17 if j==0 else (y+8 if j==3 else y-4);htext(xx,yy,23,GREEN[j%4],'center' if j in [0,3] else 'left');hbody(xx,yy+5,23,12,align='center' if j in [0,3] else 'left')
 elif i==14:
  badgehex(50,52,13,GREEN[0]);icon(45,44,10,18,'Trophy','#fff')
  for j in range(6):a=math.radians(-120+j*60);x=50+18*math.cos(a);y=52+18*16/9*math.sin(a);badgehex(x,y,3,GREEN[0],str(j+1).zfill(2));xx=x-28 if x<50 else x+5;htext(xx,y-5,24,GREEN[0],'right' if x<50 else 'left');hbody(xx,y+1,24,12,align='right' if x<50 else 'left')
 elif i==15:
  badgehex(27,54,16,GREEN[0]);arc(27,52,7.5,135,405,'#fff',17);arc(27,52,6.5,140,400,GREEN[1],8);chip(19,62,16,7,'99%',3.1,'transparent','#fff',600,0);text(20,71,14,5,'Your Text Here',1.4,'#e5f8ed',align='center');chip(22,47,10,7,'80%',2,'transparent',GREEN[1],600,0)
  for j in range(2):y=38+j*31;badgehex(49,y,5,GREEN[0]);hexagon(49,y,3,'#fff');chip(46,y-4,6,8,str(j+1).zfill(2),2,'transparent',GREEN[0],700,0);line(53,y,58,y,GREEN[0],8);hexagon(59,y,2.8,GREEN[0]);htext(64,y-6,29,'#333');hbody(64,y,29,12)
 elif i==16:
  for j,(x,y) in enumerate([(20,39),(40,73),(60,39)]):hexagon(x,y,10,'#f2f2f2',True);hexagon(x,y,9,GREEN[j],True);hexagon(x,y,7,'#fff',True);icon(x-4,y-7,8,14,['TreePine','CookingPot','Sprout'][j],GREEN[j]);badgehex(x,65 if j!=1 else 45,3.5,GREEN[j],str(j+1).zfill(2));line(x,54 if j!=1 else 57,x,60 if j!=1 else 52,GREEN[j],22);yy=76 if j!=1 else 25;htext(x-9,yy,18,GREEN[j],'center');hbody(x-11,yy+5,22,11,align='center')
 save('p060',f's02-{i:02}',title=H60[i-1])
def bulb_points(cx,cy,r):
 return [(cx+r*math.cos(math.radians(a)),cy+r*16/9*math.sin(math.radians(a))) for a in range(180,416,4)]+[(cx+r*.42,cy+r*2.05),(cx+r*.42,cy+r*2.4),(cx-r*.42,cy+r*2.4),(cx-r*.42,cy+r*2.05),(cx+r*math.cos(math.radians(125)),cy+r*16/9*math.sin(math.radians(125)))]+[(cx+r*math.cos(math.radians(a)),cy+r*16/9*math.sin(math.radians(a))) for a in range(125,181,4)]
def bulb(cx,cy,r,fill='#fff',stroke='#b6b6b6',sw=3):
 path(bulb_points(cx,cy,r),stroke,fill,sw)
 for j in range(3):box(cx-r*.43,cy+r*2.48+j*r*.22,r*.86,r*.15,stroke,5)
 circle(cx,cy+r*3.18,r*.20,stroke)
 path([(cx-r*.19,cy+r*2.35),(cx-r*.29,cy+r*.50),(cx-r*.37,cy),(cx-r*.20,cy-r*.20),(cx-r*.05,cy+r*.30),(cx+r*.05,cy+r*.30),(cx+r*.20,cy-r*.20),(cx+r*.37,cy),(cx+r*.29,cy+r*.50),(cx+r*.19,cy+r*2.35)],stroke,sw=max(1,sw*.6));E[-1]['curved']=True

def clipped_polygon(poly,axis,bound,greater):
 out=[]
 for a,b in zip(poly,poly[1:]+poly[:1]):
  ai=a[axis]>=bound if greater else a[axis]<=bound;bi=b[axis]>=bound if greater else b[axis]<=bound
  if ai:out.append(a)
  if ai!=bi:
   v=(bound-a[axis])/(b[axis]-a[axis]);pt=[a[0]+v*(b[0]-a[0]),a[1]+v*(b[1]-a[1])];pt[axis]=bound;out.append(tuple(pt))
 return out

def bulb_cells(cx,cy,r,colors,rows=2):
 poly=bulb_points(cx,cy,r);top=cy-r*16/9;bottom=cy+r*2.4
 for j,c in enumerate(colors):
  col=j%2;row=j//2;a=top+(bottom-top)*row/rows;b=top+(bottom-top)*(row+1)/rows
  pp=clipped_polygon(poly,0,cx,col==1);pp=clipped_polygon(pp,1,a,True);pp=clipped_polygon(pp,1,b,False)
  path(pp,c,c,0)

def bulb_outline(cx,cy,r):bulb(cx,cy,r,'#fff','#bbb',2)
def lamp_label(x,y,c,w=20,left=True,boxed=False):
 if boxed:box(x,y,w,15,'#fff',10,'1px solid '+c)
 text(x+(1 if boxed else 0),y+1,w-(2 if boxed else 0),4,'YOUR TEXT',1.7,c,700,'center' if boxed else 'right' if left else 'left','Roboto')
 para(x+(1 if boxed else 0),y+6,w-(2 if boxed else 0),9,1.2,'#999','center' if boxed else 'right' if left else 'left',t='Lorem ipsum is simply\ndummy text of the printing.')
LABELS={
 (2,2):[(14,16,0,True),(69,16,1,False),(14,48,2,True),(69,48,3,False)],
 (2,6):[(5,43,0,True),(5,67,1,True),(76,43,2,False),(76,67,3,False)],
 (2,7):[(10,29,0,True),(10,49,1,True),(10,71,2,True),(74,29,3,False),(74,49,4,False),(74,71,5,False)],
 (2,9):[(11,35,2,True),(7,55,4,True),(12,76,1,True),(68,26,5,False),(76,48,3,False),(72,76,0,False)],
 (2,11):[(9,34,0,True),(9,70,1,True),(76,34,2,False),(76,70,3,False)],
 (2,12):[(6,27,2,True),(3,52,1,True),(6,78,0,True),(74,27,4,False),(77,52,3,False),(74,78,5,False)],
 (2,14):[(16,31,0,True),(16,63,1,True),(70,31,3,False),(70,63,2,False)],
 (2,16):[(7,33,0,True),(7,52,1,True),(7,73,2,True),(76,33,3,False),(76,52,4,False),(76,73,5,False)],
 (4,1):[(3,38,5,True),(3,57,0,True),(3,75,3,True),(79,36,5,False),(79,56,0,False),(79,75,3,False)],
 (4,3):[(7,39,0,True),(7,60,1,True),(7,79,2,True),(76,39,3,False),(76,60,4,False),(76,79,5,False)],
 (4,5):[(23,32,0,True),(23,66,2,True),(63,27,1,False),(60,72,3,False)],
 (4,6):[(10,29,0,True),(10,49,1,True),(10,71,2,True),(74,29,3,False),(74,49,4,False),(74,71,5,False)],
 (4,7):[(16,31,0,True),(16,63,2,True),(70,31,1,False),(70,63,3,False)],
 (4,8):[(5,35,0,True),(5,78,2,True),(78,38,1,False),(78,78,3,False)],
 (4,9):[(10,29,0,True),(10,49,1,True),(10,71,2,True),(74,29,3,False),(74,49,4,False),(74,71,5,False)],
 (4,10):[(11,34,0,True),(11,54,2,True),(11,73,4,True),(73,34,1,False),(73,54,3,False),(73,73,5,False)],
 (4,11):[(11,29,0,True),(11,49,1,True),(11,71,2,True),(74,29,3,False),(74,49,4,False),(74,71,5,False)],
 (4,12):[(11,29,0,True),(11,49,1,True),(11,71,2,True),(74,29,3,False),(74,49,4,False),(74,71,5,False)],
 (4,13):[(7,32,4,True),(7,52,2,True),(7,72,0,True),(77,32,5,False),(77,52,3,False),(77,72,1,False)],
 (4,14):[(14,29,0,False),(14,51,1,False),(14,73,2,False),(69,29,3,True),(69,51,4,True),(69,73,5,True)],
 (4,15):[(9,26,0,True),(9,72,4,True),(75,26,2,False),(75,72,0,False)],
}
def standardlabels(six=False,boxed=False):
 labs=LABELS.get((pv,i),[(8,30+j*21,LAMP.index(LAMP[j]),True) for j in range(3)]+[(72,30+j*21,j+3,False) for j in range(3)] if six else [(8,30,0,True),(8,62,1,True),(72,30,2,False),(72,62,3,False)])
 for j,(x,y,k,left) in enumerate(labs):
  co=LAMP[k];lamp_label(x,y,co,17,left,boxed)
  if boxed:
   icon(x+18 if left else x-6,y-6,4,7,['PanelTop','Building2','ChartColumn','Archive','ThumbsUp','Building'][k],co)
   continue
  xx=x+20 if left else x-6
  if (pv,i) in [(2,7),(2,9),(4,3),(4,6),(4,8),(4,9),(4,11),(4,12)]:
   box(xx-.25,y+2,4.5,8,co,4) if (pv,i) in [(2,7),(4,6),(4,9),(4,11),(4,12)] else circle(xx+2,y+6,2.5,co);icon(xx+.6,y+3.5,2.8,5,['PanelTop','Building2','ChartColumn','Archive','ThumbsUp','Building'][k],'#fff')
  elif (pv,i) in [(2,16),(4,13),(4,14)]:
   box(xx+1.5,y+3,1,9,co)
   if (pv,i)==(4,14):
    E.pop();bx=x-5 if k<3 else x+22;box(bx,y+3,1,9,co);text(bx-6 if k<3 else bx+3,y+3,4,8,str(k+1),3,co,700)
  else:icon(xx,y+2,4,7,['PanelTop','Building2','ChartColumn','Archive','ThumbsUp','Building'][k],co)

def lamphead(top=True):
 if top:text(6,5,86,11,'Lamp Infographic',3.9,'#111',800,font='Poppins');text(6,17,86,4,'Infographic Powerpoint Template',1.35,'#aaa')
 else:text(6,1,86,5,'Infographic Powerpoint Template',1.35,'#aaa')
for pv in [2,4]:
 for i in range(1,17):
  E=[];FONT='Roboto';lamphead(i>4);bg='#ffbf00' if pv==4 and i==15 else '#fff'
  if i<=4: # sheet partially cuts off the deck heading in these cells
   pass
  placeholder=(pv==2 and i in [1,2,7,8,9,14,16]) or (pv==4 and i in [1,5,7,10,11,12,14,16])
  if placeholder:
   # These central collages, 3D, pictorial gear/brain illustrations are image regions.
   if pv==2 and i==1:
    image(34,34,34,55)
    for j,(x,y) in enumerate([(14,10),(63,10),(6,33),(73,33)]):lamp_label(x,y,LAMP[[0,2,1,3][j]],18,j%2==0);circle(40 if j<2 and j%2==0 else 58 if j<2 else 32 if j%2==0 else 66,y+7,2.5,LAMP[[0,2,1,3][j]]);icon((40 if j<2 and j%2==0 else 58 if j<2 else 32 if j%2==0 else 66)-1.3,y+4.5,2.6,5,'ChartNoAxesCombined','#fff')
   elif pv==4 and i==1:
    image(25,39,50,61);standardlabels(True)
   elif pv==4 and i==16:
    image(19,23,62,77);lamp_label(4,46,LAMP[1],17,False);lamp_label(52,19,LAMP[0],22,False);lamp_label(76,33,LAMP[2],22,False)
   else:
    image(*({(2,2):(40,17,22,59),(2,9):(39,36,23,59),(2,8):(29,32,44,61),(2,14):(38,21,25,74),(2,16):(33,23,31,68),(4,5):(42,32,21,57),(4,7):(33,29,27,57),(4,10):(39,21,25,73),(4,11):(39,22,23,65),(4,12):(39,23,23,62),(4,14):(39,26,22,61)}.get((pv,i),(38,24,26,65))));standardlabels(i not in [2,8,14] if pv==2 else i not in [7,10]);
  elif (pv==2 and i==4) or (pv==4 and i in [2,13]):
   cols=[LAMP[5],LAMP[3],LAMP[2],LAMP[1],LAMP[0]] if pv==2 else [LAMP[0],LAMP[3],LAMP[1],LAMP[2],LAMP[4]]
   if i==13:
    bulb(50,54,11,'#fff','#aaa',0);bulb_cells(50,54,11,[LAMP[4],LAMP[5],LAMP[2],LAMP[3],LAMP[0],LAMP[1]],3)
    for j in range(6):
     x=43 if j%2==0 else 53;y=39+(j//2)*15;icon(x,y,3,6,'PanelTop','#fff')
    for j in range(3):box(45,81+j*5,10,3,'#aaa',5)
    standardlabels(True)
   else:
    # Five bands follow the curved bulb rather than approximating its pixels.
    widths=[16,24,25,20,13];ys=[15,26,37,48,59]
    for j in range(5):
     w=widths[j];path([(50-w/2,ys[j]+11),(50-w/2-1,ys[j]+4),(50-w*.35,ys[j]),(50+w*.35,ys[j]),(50+w/2+1,ys[j]+4),(50+w/2,ys[j]+11)],cols[j],cols[j],0);chip(45,ys[j]+2,10,7,str(j+1).zfill(2),1.8,'transparent','#fff',600,0)
    for j in range(3):box(45,73+j*5,10,3,'#ddd',5)
    for j,(x,y,left) in enumerate([(68,20,False),(13,30,True),(68,40,False),(13,54,True),(68,64,False)]):lamp_label(x,y,cols[j],22,left)
  elif pv==2 and i==3:
   bulb(48,17,5.5,'#fff','#555',1.5)
   for j in range(8):a=math.radians(j*45);line(48+7*math.cos(a),17+12*math.sin(a),48+8.5*math.cos(a),17+15*math.sin(a),'#777')
   icon(60,61,14,25,'Plug','#999');
   for j,(x,y) in enumerate([(5,41),(5,58),(48,48),(82,64)]):
    co=LAMP[[0,2,1,3][j]];lamp_label(x,y,co,14 if j<2 else 17,j<2);cx=x+18 if j<2 else x-3;circle(cx,y+6,2.2,co);icon(cx-1.2,y+3.8,2.4,4.4,['PanelTop','ChartColumn','Building2','Archive'][j],'#fff')
   line(24,52,44,52,'#eee');line(24,67,59,67,'#eee');line(48,32,48,46,'#eee')
  elif pv==2 and i==5:
   for j in range(5):x=13+j*18;bulb(x,41,5.2,'#fff','#aaa',2);box(x-4.5,42+j,9,8-j*.5,LAMP[j],clipPath='ellipse(50% 100% at 50% 0%)') if False else None;sector(x,41,5,0,0,180,LAMP[j]);chip(x-5,67,10,7,str(j+1).zfill(2),1.7,LAMP[j],r=3);para(x-8,79,16,15,1.25,'#999','center')
  elif pv==2 and i==6:
   standardlabels();bulb(50,55,8,'#fff','#ddd',9);chip(45,49,10,16,'!',8,'transparent',LAMP[1],800,0);circle(50,67,1.4,LAMP[2]);
   for j in range(9):a=math.radians(180+j*22.5);line(50+11*math.cos(a),55+19.5*math.sin(a),50+13*math.cos(a),55+23*math.sin(a),LAMP[j%6],6)
  elif pv==2 and i==8:
   standardlabels();icon(29,42,24,50,'Lightbulb','#888');icon(49,42,24,50,'Lightbulb','#888');
   for j in range(5):line(40+j*5,43,38+j*6,36,'#c8d63b',4)
  elif pv==2 and i==10:
   box(5,27,90,25,'#f3f3f3',22);box(5,54,90,25,'#f3f3f3',22);bulb(50,49,12,'#fff','#ddd',1)
   for j in range(4):
    co=[LAMP[2],LAMP[1],LAMP[3],LAMP[0]][j];sector(50,49,12,0,180+j*90,270+j*90,co);lamp_label(14 if j%2==0 else 68,33 if j<2 else 61,co,20,j%2==0);icon(43 if j%2==0 else 53,39 if j<2 else 62,4,7,'PanelTop','#fff')
  elif pv==2 and i==11:
   standardlabels(boxed=True);bulb(51,54,8,'#fbe64f','#555',3)
   for pts,co in [([(35,29),(40,30),(43,37)],LAMP[0]),([(61,37),(65,29),(68,27)],LAMP[2]),([(41,67),(37,73),(34,72)],LAMP[1]),([(61,64),(65,69),(69,74)],LAMP[3])]:path(pts,co,sw=2.5);E[-1]['curved']=True;E[-1]['arrow']=True
  elif pv==2 and i==12:
   standardlabels(True)
   for j in range(6):sector(50,64,22,12,135+j*45,179.5+j*45,LAMP[[0,1,2,4,3,5][j]]);a=math.radians(157.5+j*45);chip(50+17*math.cos(a)-4,64+30*math.sin(a)-4,8,8,str(j+1).zfill(2),3,'transparent','#fff',700,0)
   bulb(50,66,6,'#fff','#aaa',2);icon(47,61,6,10,'Users','#aaa')
  elif pv==2 and i==13:
   for j in range(4):sector(50,57,16,9,-90+j*90,j*90,[LAMP[2],LAMP[3],LAMP[1],LAMP[0]][j]);x=3 if j>=2 else 74;y=34 if j%2==0 else 64;chip(x,y,23,21,'YOUR TEXT\nLorem ipsum is simply\ndummy text of the\nprinting.',1.45,LAMP[[2,3,0,1][j]],r=99)
   icon(45,49,10,18,'Lightbulb','#e9b736')
  elif pv==2 and i==15:
   for j in range(4):text(6,31+j*18,5,6,str(j+1),1.6,LAMP[j],600);chip(13,27+j*18,46,10,'Lorem ipsum is simply dummy text of the printing and typesetting',1.2,LAMP[j],r=99)
   for j in range(3):arc(81,50,12,135+j*90,225+j*90,LAMP[j],7);a=math.radians(135+j*90);circle(81+12*math.cos(a),50+12*16/9*math.sin(a),1.5,LAMP[j]);path([(76,69),(88,69),(88,75),(75,75),(75,81),(86,81),(86,87),(77,87),(77,93),(84,93)],LAMP[3],sw=9);E[-1]['curved']=True;path([(77,68),(75,55),(79,62),(82,57),(85,61),(87,55),(85,68)],'#e3e600',sw=8)
  elif pv==4 and i==3:
   standardlabels(True);bulb(50,47,10,'#fff','#aaa',1.5)
   for j,(pts,co) in enumerate([([(42,35),(57,41),(57,30),(48,26),(41,33)],LAMP[0]),([(58,37),(40,50),(41,56),(55,56),(58,43)],LAMP[1]),([(56,55),(44,68),(45,72),(54,72),(44,68)],LAMP[2])]):path(pts,co,sw=8)
   for j in range(3):box(44,81+j*4,12,3,LAMP[3],3)
  elif pv==4 and i==4:
   for j,(x,y,co) in enumerate([(34,53,LAMP[2]),(50,73,LAMP[1]),(66,53,LAMP[0])]):line(x,8,x,y-18,'#ddd',1);path([(x-4,y-9),(x-8,y+9),(x-5,y+22),(x,y+26),(x+5,y+22),(x+8,y+9),(x+4,y-9)],co,co,0);box(x-4,y-17,8,8,'#ddd');E[-2]['curved']=True;icon(x-4,y-5,8,25,'Lightbulb','#dce2c4')
   lamp_label(3,29,LAMP[2],24,True);lamp_label(76,29,LAMP[0],23,False);lamp_label(27,88,LAMP[1],23,False)
  elif pv==4 and i==6:
   standardlabels(True);bulb(50,50,10,'#ffff00','#363620',4)
   for j in range(7):a=math.radians(180+j*30);line(50+13*math.cos(a),50+23*math.sin(a),50+16*math.cos(a),50+28.5*math.sin(a),LAMP[j%6],9)
  elif pv==4 and i==8:
   standardlabels();bulb(50,49,11,'#fff','#aaa',9);bulb_cells(50,49,9,[LAMP[0],LAMP[1],LAMP[5],LAMP[3]])
  elif pv==4 and i==9:
   standardlabels(True);bulb(50,47,9,'#ffe600','#fff074',3)
   for j in range(9):a=math.radians(180+j*22.5);line(50+12*math.cos(a),47+21*math.sin(a),50+15*math.cos(a),47+27*math.sin(a),'#e3ed00',5)
   for j,co in enumerate(LAMP):path([(47+j,79),(48+j,79),(53+j*5,100),(18+j*10,100)],co,co,0)
  elif pv==4 and i==15:
   standardlabels();bulb(50,44,13,'#fff','#3d3d3d',0);bulb_cells(50,44,13,['#fff',LAMP[2],LAMP[4],'#111'])
   for j,co in enumerate(['#fff',LAMP[2],'#111',LAMP[4]]):a=math.radians(225+j*90);chip(50+6*math.cos(a)-4,44+11*math.sin(a)-4,8,8,'25%',1.8,'transparent','#fff' if j else '#bd8b00',700,0)
  save('p100',f's{pv:02}-{i:02}',bg,'Lamp Infographic')
DARK='#404d56';MUTED='#91a4af';CYAN='#13c8d6';MINT='#3be2bf';PINK='#e63686';YELLOW='#f4d646';LIGHT='#d7e1e4';GREEN2='#8fe876';SERIES=[PINK,YELLOW,MINT,MUTED]
def pitchhead(t="Let's talk about data"):
 icon(2,4,2,4,'Menu',LIGHT);text(6,4,90,7,t,2.7,LIGHT,font='Roboto');text(2,94,8,5,'Pitch',1.9,LIGHT,font='Kaushan Script');text(10,95,48,3,'Good Presentation for Your Pitch',.9,'#7d8f99');text(83,95,15,3,'www.goodpitch.co',.8,'#7d8f99',align='right')
def ptitle(t,x=8,y=20,w=84,size=3):text(x,y,w,max(8,size*2.2),t,size,LIGHT)
def pbody(x,y,w,h=15,t=None,align='left',size=1.3):
 if not t:
  words='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus vulputate laoreet nibh aliquam. Aenean vestibulum neque eu metus interdum, non consequat nisl facilisis. Keep your information clear.'
  cols=max(12,int(w/(size*.55)));rows=max(1,min(2 if w>=60 else 3,int(h*7.2/(size*12.8*1.2))))
  t='\n'.join(textwrap.wrap(words,cols)[:rows])
 para(x,y,w,h,size,LIGHT,align,t)

def pmetric(x,y,w=19,h=23,pct='58%',title='Online shop',c=MUTED):
 box(x,y,w,h,'transparent',3,'1px solid #66737c');text(x,y+3,w,7,pct,3.3,c,400,'center');text(x,y+11,w,5,'$12,000K',1.8,LIGHT,600,'center');text(x,y+18,w,4,title,1.4,LIGHT,400,'center')
def pdonut(x,y,r=10,percent=.58,c=CYAN,lab=None):
 arc(x,y,r,0,360,'#6e8794',max(13,r*1.6));arc(x,y,r,-90,-90-360*percent,c,max(13,r*1.6))
 if lab:chip(x-r,y-r*16/9,r*2,r*32/9,lab,2.8,'transparent',LIGHT,600,0)
def pline(x,y,w,h,variant=0,labels=True):
 seqs=[[15,23,32,50,60,38,51,73,80,95],[53,41,22,13,35,31,43,40,48,66]]
 if variant==1:seqs=[[25,40,50,80],[80,60,30,20]]
 elif variant==2:seqs=[[55,70,40,60],[20,43,40,56]]
 elif variant==3:seqs=[[40,65,70,85],[30,28,37,58]]
 for j in range(5):line(x,y+j*h/4,x+w,y+j*h/4,'#59666f',.6);text(x-3.5,y+j*h/4-1.5,3,3,str(100-j*25),.85,MUTED,align='right')
 for j,seq in enumerate(seqs):
  pts=[(x+k*w/(len(seq)-1),y+h-v*h/100) for k,v in enumerate(seq)];path(pts,MINT if j==0 else '#3ea8c0',sw=5)
  for xx,yy in pts:circle(xx,yy,.5,DARK,'3px solid '+(MINT if j==0 else '#3ea8c0'))
 if labels:
  for k in range(len(seqs[0])):text(x+k*w/(len(seqs[0])-1)-2,y+h+2,4,3,(['Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec'] if len(seqs[0])==10 else ['Mar','Jun','Sept','Dec'])[k],.85,LIGHT,align='center')
def pbars(x,y,w,h,groups=1,icons=False,teal=False):
 for j in range(5):line(x,y+j*h/4,x+w,y+j*h/4,'#59666f',.6);text(x-4,y+j*h/4-1,3,3,str(80-j*20),.8,MUTED,align='right')
 for g in range(groups):
  vals=[30,45,72,52] if g%2==0 else [52,76,41,89]
  for j,v in enumerate(vals):
   xx=x+g*w/groups+3+j*w/groups/5;co=([LIGHT,MUTED,GREEN2,MUTED] if teal else SERIES)[j];box(xx,y+h-v*h/100,w/groups/9,v*h/100,co)
   if icons:circle(xx+w/groups/18,y+h-v*h/100,2.5,DARK,'1px solid #eee');icon(xx+w/groups/18-1.5,y+h-v*h/100-2.7,3,5.4,['Share2','Flag','User','ShoppingBag'][j],LIGHT)
  text(x+g*w/groups,y+h+2,w/groups,4,str(2000+g*5),1.1,LIGHT,align='center')
def pmoney(x,y,t='$12,000K',ico='Share2',w=42):
 circle(x+3,y+6,2,DARK,'1px solid '+MUTED);icon(x+1.7,y+3.6,2.6,4.8,ico,MUTED);text(x+8,y+2,17,6,t,2.5,LIGHT,600);text(x+25,y+3,max(17,w-25),6,'Market Growth\nOpportunity',1.05,MUTED);pbody(x,y+13,w,11,size=1.2)
def phbars(x,y,w=30,h=30):
 for j in range(5):line(x+j*w/4,y,x+j*w/4,y+h,'#56636c',.6);text(x+j*w/4-2,min(y+h+2,96),4,3,str(j*25),.75,MUTED,align='center')
 for j,v in enumerate([.20,.29,1,.55]):text(x-9,y+j*h/4+1,8,4,'Phase '+str(j+1),.85,MUTED,align='right');box(x,y+j*h/4,w*v,1.7,GREEN2);box(x,y+j*h/4+2.3,w*[.59,.46,.61,.69][j],1.7,CYAN)
def pstats(x,y):
 for j,pct in enumerate(['21%','32%','17%','14%']):circle(x+j*8.6+3,y,3.6,'transparent','3px solid '+[YELLOW,CYAN,MINT,GREEN2][j]);chip(x+j*8.6-.5,y-6,7,12,pct,2,'transparent',LIGHT,400,0)
def pdevices(x,y):
 for j in range(2):box(x+j*17,y,15,23,'#46535e');icon(x+4+j*17,y+3,7,12,'Laptop' if j==0 else 'Smartphone',CYAN if j==0 else PINK);text(x+j*17,y+16,15,5,'32,456,384' if j==0 else '82,281,183',1.4,LIGHT,align='center')
def team(six=False):
 pitchhead('our team')
 for j in range(6 if six else 3):x=21+(j%3)*29;y=(26 if six else 38)+(j//3)*37;hexagon(x,y,6.8,DARK,True,[MINT,GREEN2,YELLOW,PINK,CYAN,'#bb99dd'][j]);hexagon(x,y,6.2,'#e5e5e5',True); # flat gray portrait, genuine frame only
 # Draw portrait placeholders over the clean frame.
 for j in range(6 if six else 3):
  x=21+(j%3)*29;y=(26 if six else 38)+(j//3)*37
  if not six:pbody(x-10,y+15,20,19,t='Aenean vulputate laoreet nibh\ninterdum. Maecenas sed diam\neget risus varius blandit sit amet\nnon magna. Aenean lacinia\nbibendum nulla sed.',align='center',size=1.2)
  text(x-11,y+17 if six else y+38,22,5,['John Backman','Greg Marshall','Jack Byrne'][j%3],1.5,LIGHT,600,'center');text(x-11,y+22 if six else y+43,22,4,'Creative Design Officer',1.1,LIGHT,align='center')
def quote_page(bottom=False):
 pitchhead('our services' if not bottom else '')
 text(8,35 if not bottom else 17,48 if not bottom else 84,23,"This company has the\nbest portfolio I've\never seen." if not bottom else "This company has the best portfolio I've\never seen.",3.6,LIGHT,align='center',lh=1.15)
 text(22 if not bottom else 40,68 if not bottom else 39,20,4,'Billy Kogan',1.4,LIGHT,700,'center');text(17 if not bottom else 35,72 if not bottom else 43,30,4,'CEO of Creative Tools',1.05,LIGHT,align='center')
 if bottom:
  for j in range(4):image(j*25,55,25,45)
 else:
  for j in range(5):image(59+(j%2)*20.5,0 if j==0 else 33+(j//3)*34,41 if j==0 else 20.5,33 if j==0 else 34)
for pv in [3,4]:
 for i in range(1,41 if pv==3 else 39):
  E=[];FONT='Roboto';bg=DARK;title='Pitch';pitchhead()
  if pv==3:
   if i in [9,15,37]:E=[];team(i==15);title='Our team'
   elif i in [10,38]:
    E=[];pitchhead('our guarantee');image(8,14,33,86);text(44,23,24,7,'3 Things we',3.5,LIGHT);text(65,21,30,10,'Guaranteed',3.6,LIGHT,font='Kaushan Script')
    for j in range(3):box(44,36+j*17,47,14,'transparent',4,'1px solid #687780');icon(47,40+j*17,3,6,'Award',[MINT,GREEN2,YELLOW][j]);text(52,41+j*17,38,6,'Project done on time with no excuse',1.9,LIGHT,500)
    title='Our guarantee'
   elif i in [14,28]:E=[];quote_page(i==28);title='Customer quote'
   elif i in [1,7]:
    E=[];pitchhead('');ptitle('Investment Package',20,15,72,4.8)
    for j in range(3):x=7+j*30;box(x,29,27,32,'#485761');icon(x+10,36,7,12,['Star','Spade','Zap'][j],MINT);text(x,51,27,7,['Basic','Angelist','Angelist Pro'][j],2.9,LIGHT,align='center');icon(x,64,4,7,'CircleDollarSign',MUTED);text(x+5,65,22,5,['$200K - $400K','$400K - $1000K','Above $2000K'][j],1.8,LIGHT,600);pbody(x,73,27,17,size=1.25)
    title='Investment Package'
   elif i in [8,13,19,20,24]:
    E=[];pitchhead('our services' if i<20 else '')
    if i==8:
     image(0,24,100,44);icon(47,33,6,10,'Network','#fff');text(11,47,78,17,'As strong as 1545 professional supports\nfrom across the globe.',3,LIGHT,align='center');pbody(8,77,84,9,align='center',size=1.2)
    elif i==13:image(42,16,58,69);icon(6,29,5,8,'Flag',LIGHT);text(6,42,35,23,'Comprehensive idea\nfor the best solution\nfor your business.',3.4,LIGHT,lh=1.16)
    elif i==19:image(0,16,58,69);icon(66,29,5,8,'ChartPie',LIGHT);text(66,39,33,7,'Product knowledge',3,LIGHT);pbody(66,50,29,17,t='12,000K development cost\n\n58% marketing ratio\n\n17% maintenance',size=1.7)
    else:
     for j in range(3 if i==24 else 4):image(j*(100/(3 if i==24 else 4)),0,100/(3 if i==24 else 4),68)
     text(9,74,80,5,'Project for WINDING WORLD',1.6,LIGHT,600);pbody(9,80,82,10,size=1.2)
    title='Our services'
   elif i in [3,23,32,36]:
    E=[];image(0,0,100,100);bg='#e5e5e5'
    if i in [3,32]:
     hexagon(50,27,5,'#e5e5e5',True,'#fff');text(10,46,80,8,'Fashion fades, only style remains the same.',3.4,'#fff',align='center');pbody(17,57,66,15,align='center',size=1.3);text(40,78,20,5,'Billy Kogan',1.5,'#fff',600,'center');text(35,84,30,4,'Creative Design Officer',1.1,'#fff',align='center')
    else:
     icon(47,34,6,11,'Presentation','#fff');text(10,47,80,15,"Let's Talk About Data" if i==23 else 'Creative Infographics',5.7,'#fff',align='center',font='Kaushan Script');box(30,64,40,8,'transparent',border='1px solid #fff');chip(30,64,40,8,'DATA DRIVEN AND NUMBERS' if i==23 else 'VECTOR AND NUMBERS',1.3,'transparent','#fff',600,0);text(2,93,8,5,'Pitch',2,'#fff',font='Kaushan Script')
    title='Photo section divider'
   elif i in [4,25,29,33]:
    E=[];pitchhead('timeline');line(50,14,50,98,'#61717b',1)
    for j in range(2):
     x=10 if j==0 else 64;y=22 if j==0 else 36;image(x,y,27,31);box(x+27 if j==0 else x-8,y,8,18,'#4b5b66');text(x+27 if j==0 else x-8,y+2,8,4,'JUNE',1.3,LIGHT,align='center');text(x+27 if j==0 else x-8,y+7,8,8,"'14",3.7,LIGHT,align='center');circle(50,y,1,'#fff');text(x,y+34,27,5,(['Build more team','Company Kick-off'] if i==25 else ['We bought micro, Inc.','Big projects started'] if i==29 else ['#1 Ranked on Google','Prepare for bright 2016'])[j],2.1,LIGHT,600,'right' if j==0 else 'left');
     if (i==29 and j==1):pline(x,y+44,27,20,1)
     elif (i in [4,33] and j==0):phbars(x+1,y+46,25,19)
     else:pbody(x,y+43,27,13,align='right' if j==0 else 'left',size=1.2)
    title='Timeline'
   elif i==16:
    E=[];pitchhead('');ptitle('Simple & powerful work process',15,18,79,3.7)
    for j in range(3):x=8+j*28;box(x,39,25,45,'transparent',20,'1px solid #63747e');icon(x+10,33,5,9,'Check',LIGHT);text(x,49,25,5,['01 DEVELOPMENT','02 BETA TEST','03 FINAL PRODUCT'][j],1.9,[YELLOW,MINT,CYAN][j],600,'center');pbody(x+3,58,19,23,t='Project done on time\nwith no excuse for\ncompromise, fully\nfocused. Your perfect\nproduct is ready\nto present.',align='center',size=1.5)
    title='Work process'
   elif i in [11,6,12,17,18]:
    if i==11 or i==6:
     ptitle('2000 - 2015 Data Comparison',24,16,75,3.7);pbars(9,32,83,31,4);text(8,74,84,5,'Online shop',1.8,LIGHT,600);pbody(8,80,84,10,size=1.15)
    elif i==12:
     ptitle('Data comparison',34,15,60,3.8)
     for j in range(4):pmetric(8+(j%2)*20,30+(j//2)*27,19,25,['58%','13%','17%','12%'][j],['Online shop','Market Promotion','Local business','Social media ads'][j],SERIES[j]);
     pbars(57,30,35,53)
    elif i==17:
     ptitle('How the market works',8,22,43,2.7)
     for j in range(2):box(8,34+j*28,15,23,'#43545f');icon(13,37+j*28,5,9,'Share2' if j==0 else 'Flag',LIGHT);text(8,48+j*28,15,6,'$12,987',2.3,LIGHT,align='center');text(27,34+j*28,26,5,'Data name',1.7,LIGHT,600);pbody(27,41+j*28,24,14,size=1.15)
     pbars(61,24,29,55,icons=True,teal=True)
    else:
     pbars(9,20,82,32,4,teal=True)
     for j in range(4):x=18+j*21;circle(x,66,3.6,DARK,'1px solid #eee');icon(x-2,62.5,4,7,['Share2','ShoppingBag','User','Flag'][j],LIGHT);text(x-9,77,18,5,'Net earnings',2,LIGHT,600,'center');text(x-9,84,18,4,'earnings and knowledge',1.1,LIGHT,align='center')
    if i in [6,11,18]:
     for j in range(4):box(29+j*15,95,1.5,2,SERIES[j]);text(31+j*15,94,12,4,'Region '+str(j+1),1,LIGHT)
    title='Bar chart'
   elif i in [21,22,26,27]:
    if i==21:
     for j in range(2):pline(9+j*46,22,38,33);pmoney(7+j*46,68,w=40)
    elif i==22:
     pline(9,22,82,38)
     for j,(x,y) in enumerate([(38,55),(46,35),(74,26)]):circle(x,y,3,DARK,'1px solid #eee');chip(x-3,y-5.4,6,10.8,str(j+1),1.6,'transparent',LIGHT,400,0)
     for j in range(3):text(9+j*29,74,25,5,['1. Lowest number','2. Rising up','3. Average number'][j],1.8,LIGHT,600);pbody(9+j*29,81,25,13,size=1.15)
    elif i==26:
     pline(9,23,35,54);ptitle('How the market works',51,22,44,2.9)
     for j in range(2):box(51,33+j*27,15,23,'#43545f');icon(56,37+j*27,5,9,'Share2' if j==0 else 'Flag',MUTED);text(51,49+j*27,15,5,'$12,987',2.3,LIGHT,align='center');text(70,34+j*27,26,5,'Data name',1.7,LIGHT,600);pbody(70,42+j*27,24,12,size=1.1)
    else:
     for j in range(3):pline(7+j*31,20,25,34,j+1);circle(20+j*31,69,3.6,DARK,'1px solid #eee');icon(18+j*31,65.5,4,7,['Share2','User','Flag'][j],LIGHT);text(7+j*31,77,25,6,'$12,000K',2.7,LIGHT,600,'center');text(7+j*31,84,25,4,'Market Growth Opportunity',1.3,MUTED,align='center')
    title='Line chart'
   elif i in [2,5,30,31,34,35,39,40]:
    if i==2:
     ptitle('The best investment in 2014 by TechWorld',35,24,51,2.6);pmoney(8,43,w=26);pbody(36,43,45,18,size=1.5);box(82,38,13,24,'#465763');text(82,42,13,9,'34%',4.3,MINT,align='center');text(82,54,13,4,'5 Years',1.4,LIGHT,align='center')
    elif i in [5,39]:
     for j in range(2):pdunut=0;pdonut(22,33+j*35,7,[.22,.45][j],[PINK,GREEN2][j],['22%','45%'][j]);box(33,19+j*35,14,25,'#43545f');icon(37,24+j*35,5,8,'Share2' if j==0 else 'User',LIGHT);text(33,37+j*35,14,5,'$12,987',2.1,LIGHT,align='center');text(51,23+j*35,42,5,'Data name',1.7,LIGHT,600);pbody(51,30+j*35,42,16,size=1.3)
    elif i in [30,31,40]:
     ptitle('Those who rules this business',50,22,47,2.7)
     if i==30:
      sector(23,54,16,0,-90,90,CYAN);sector(23,54,16,0,90,270,MINT);chip(11,46,12,10,'46%',2.2,'transparent',LIGHT,600,0);chip(25,51,12,10,'54%',2.2,'transparent',LIGHT,600,0)
     elif i==31:phbars(11,32,30,45)
     else:pbars(9,25,33,54,1,teal=True)
     pmoney(50,32,w=42);pmoney(50,60,'$78,999K',w=42)
    elif i==34:
     for j in range(4):pmetric(7+(j%2)*20,24+(j//2)*28,18,25,['58%','13%','17%','12%'][j],['Online shop','Market Promotion','Local business','Social media ads'][j],SERIES[j])
     for j in range(3):sector(73,53,15,13,-90+j*120,30+j*120,[PINK,YELLOW,CYAN][j]);chip(63,46,20,14,'$58,289.718\nNet Market Volume',1.8,'transparent',LIGHT,600,0)
    elif i==35:
     for j,(x,y) in enumerate([(20,35),(64,35),(20,70),(64,70)]):pdonut(x,y,7,[.35,.72,.69,.2][j],CYAN,['2010','2014','2012','2016'][j]);text(x+10,y-11,24,5,'$12,911',2.1,CYAN);text(x+10,y-5,24,5,'Market shares after tax',1.3,LIGHT,600);pbody(x+10,y+2,25,15,size=1.15)
    title='Market data infographic'
  else:
   E=[];pitchhead('Creative Infographics');title='Creative Infographics'
   if i in [1,2,5,6]:
    E=[];image(0,0,100,100);bg='#e5e5e5';icon(47,32,6,10,'MapPin' if i==5 else 'Monitor','#fff');text(7,46,86,16,'Maps & Data' if i in [2,5] else 'Devices Mockup' if i==6 else 'Creative Infographics',5.7,'#fff',align='center',font='Kaushan Script');box(30,61,40,8,'transparent',border='1px solid #fff');chip(30,61,40,8,'SMARTPHONE, TABLET, AND MORE',1.3,'transparent','#fff',600,0);text(2,93,8,5,'Pitch',2,'#fff',font='Kaushan Script');title='Photo section divider'
   elif i==3:
    for j in range(12):x=6+j*7.5;box(x,27,4,59,'#465560');text(x-1,88,6,4,['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec'][j],.95,LIGHT,align='center')
    for x,y,w,h,co in [(6,26,28,20,'#586d7b'),(40,26,22,20,'#586d7b'),(20,46,35,21,PINK),(47,66,36,20,CYAN),(76,46,21,20,'#586d7b')]:box(x,y,w,h,'#586d7b' if co=='#586d7b' else DARK,border=None if co=='#586d7b' else '1px solid '+co);text(x+2,y+3,w-4,5,'Text goes here',1.55,LIGHT,600);pbody(x+2,y+8,w-4,h-8,size=1.1)
   elif i==4:
    arc(42,36,11,20,335,PINK,8);chip(30,26,24,20,'70%',6.1,'transparent',LIGHT,400,0);arc(61,69,11,210,520,YELLOW,8);chip(49,59,24,20,'41%',6.1,'transparent',LIGHT,400,0)
    for j in range(10):icon(47+j*3.5,29,3.5,14,'PersonStanding',LIGHT if j<7 else MUTED);icon(19+j*3.5,62,3.5,14,'PersonStanding',MUTED if j<6 else LIGHT)
    pbody(8,29,19,19,t='70% marketers have\nsuccessfully gained new\ncustomers via social\nnetworks',align='right',size=1.7);pbody(73,64,21,19,t='41% of marketers have\nsuccessfully gained new\ncustomers via social\nnetworks',size=1.7)
   elif i==7:
    for j in range(5):line(8,20+j*10,92,20+j*10,'#5b6b73',.7);text(5,19+j*10,3,4,str(40-j*10),.8,MUTED)
    for j in range(9):circle(13+j*5,55-[0,6,4,7,13,17,23,29,33][j],1.4,CYAN)
    for j in range(8):circle(17+j*10,49-[0,-6,3,-1,11,17,12,22][j],1,MINT)
    for j in range(7):circle(26+j*11,58-j*6,1.8,'transparent','1px solid #e1dca1')
    for j in range(3):x=8+j*31;circle(x+1,71,1,CYAN if j==0 else MINT if j==1 else YELLOW);text(x+3,69,25,4,'Your text goes here',1.5,LIGHT,600);pbody(x,77,27,14,size=1.25)
   elif i==8:
    for j in range(11):x=13+j*7.5;circle(x,38,2.5,'#728ba2' if j%3==0 else '#a1b7cd');line(x,29 if j%2==0 else 47,x+3 if j%2==0 else x-3,22 if j%2==0 else 54,'#647885',2);text(x-1 if j%2==0 else x-5,26 if j%2==0 else 55,12,4,'Text here',1.05,MUTED);E[-1].update(rotate=-45,nowrap=True)
    for j,co in enumerate([CYAN,MINT,GREEN2]):arc(28+j*23,38,4.5,0,360,co,10);text(27+j*23,53,12,4,'Text Here',1.1,LIGHT,rotate=45) if False else None;circle(28+j*23,67,1,co);text(31+j*23,65,24,4,'Your text goes here',1.5,LIGHT,600);pbody(8+j*31,73,27,16,size=1.25)
   elif i in [9,10,15,16,21,22,27,28,33,34]:
    leftmap=i in [9,10,15,16];geo='United States' if leftmap else 'Europe' if i in [33,34] else 'Asia';E=[];pitchhead('US Map' if leftmap else geo+' map');image(5 if leftmap else 43,18 if leftmap else 10,53 if leftmap else 52,65 if leftmap else 77);x=(59 if i in [15,16] else 62) if leftmap else 7;y={9:37,10:41,15:53,16:43,21:36,22:43,27:52,28:43,33:40,34:40}[i];ptitle(geo,x,y,35,3);pbody(x,y+9,33,13,size=1.2)
    variant={9:0,10:1,15:2,16:3,21:0,22:1,27:2,28:3,33:1,34:3}[i]
    if variant==0:
     phbars(x+5,y+22,27,24)
     for j,(xx,yy,pct) in enumerate([(11,34,'21%'),(24,25,'34%'),(31,50,'52%'),(43,32,'56%')] if leftmap else [(53,42,'21%'),(68,31,'34%'),(83,39,'56%'),(69,67,'52%')]):hexagon(xx,yy,4.2,'#2cd2ca',True);chip(xx-4,yy-5,8,10,pct,1.6,'transparent','#fff',600,0);line(xx,yy+8,xx,yy+17,'#fff',1);circle(xx,yy+18,.5,'#fff')
    elif variant==1:pstats(x+1,y+28)
    elif variant==2:
     for xx,yy,r,lab in ([(13,56,6,'12,839'),(42,55,5.5,'12,839'),(34,25,4,'932'),(33,69,4,'235')] if leftmap else [(53,42,6,'12,839'),(75,28,4,'932'),(83,58,5.5,'12,839'),(72,72,4,'235')]):line(24 if leftmap else 66,48 if leftmap else 59,xx,yy,'#fff',1);circle(xx,yy,r,'#e9786b');chip(xx-r,yy-r*16/9,2*r,2*r*16/9,'Revenue\n'+lab,1.7,'transparent','#fff',600,0)
    else:pdevices(x,y+21)
    title=geo+' infographic'
   elif i in [11,12,17,18,23,24,29,30,35,36]:
    E=[];pitchhead('');title='Device Mockup'
    if i==11:
     for x,y,w,h in [(44,7,36,42),(75,0,25,40),(47,50,35,43),(77,42,23,40)]:image(x,y,w,h)
     ptitle('United States',7,31,36,3);pbody(7,42,33,13,size=1.25);phbars(12,58,27,25)
    elif i==12:image(0,0,52,64);ptitle('United Kingdom',59,40,36,2.6);pbody(59,49,33,11,size=1.2);pdevices(59,63)
    elif i==17:
     for x,y,w,h in [(0,14,14,71),(62,14,20,71),(85,14,15,71)]:image(x,y,w,h)
     circle(35,30,3.5,DARK,'2px solid '+CYAN);icon(33,26.5,4,7,'Quote',CYAN);text(20,43,34,20,"If you're puzzled by what\ndark energy is, you're in\ngood company.",3.1,LIGHT,align='center',lh=1.1)
    elif i in [18,29]:image(11 if i==18 else 7,12 if i==18 else 10,33 if i==18 else 37,76 if i==18 else 90);ptitle('Mobile data',53,29,38,3);pbody(53,38,34,12,size=1.2);pstats(53,62);text(52,72,37,4,'Rate         Rate         Rate         Rate',1.1,LIGHT)
    elif i==23:image(50,9,43,82);ptitle('The business area',8,42,39,2.7);pbody(8,50,33,11,size=1.25);phbars(9,62,30,23)
    elif i==24:
     image(32,5,28,95)
     for j,(x,y) in enumerate([(4,30),(9,66),(70,17),(70,57)]):text(x,y,26,5,'Text goes here',1.6,[YELLOW,MINT,CYAN,PINK][j],600);pbody(x,y+7,26,13,size=1.15);line(30 if j<2 else 60,y+7,33 if j<2 else 69,y+7,MUTED,1)
    elif i in [30,35]:
     if i==30:image(5,9,36,91);x=47;y=28
     else:
      for x,y,w,h in [(39,0,56,25),(49,27,51,46),(89,62,11,31)]:image(x,y,w,h)
      x=8;y=33
     ptitle('Accurate mobile data last year',x,y,47,2.7)
     for j in range(2):box(x,y+11+j*27,15,23,'#44565f');icon(x+5,y+15+j*27,5,9,'Share2' if j==0 else 'Flag',CYAN);text(x,y+27+j*27,15,5,'$12,987',2.1,LIGHT,align='center');text(x+18,y+13+j*27,27,5,'Data name',1.6,LIGHT,600);pbody(x+18,y+21+j*27,20 if i==35 else 27,12,size=1.1)
    else:image(31,47,69,53);ptitle('Mobile data',8,15,39,3);pbody(8,24,35,13,size=1.2);pdevices(8,40)
   elif i==13:
    ptitle('Social media data',34,17,60,3.7)
    for j in range(6):x=7+(j%3)*31;y=31+(j//3)*21;circle(x+2,y+6,3.5,'#4f5e69');icon(x,y+2,4,8,['Facebook','Twitter','Youtube','Cloud','Instagram','MapPin'][j],[CYAN,CYAN,PINK,YELLOW,YELLOW,PINK][j]);box(x+7,y,19,13,'transparent',border='1px solid #65747d');chip(x+7,y,19,13,['1,203','1,203','3,451','1,643','1,643','1,943'][j],3.1,'transparent',LIGHT,400,0)
    pbody(8,78,85,13,align='center',size=1.3)
   elif i in [14,26,32]:
    if i==14:
     for j,(x,y) in enumerate([(15,62),(33,41),(50,62),(67,41),(84,62)]):hexagon(x,y,7.5,'transparent',True,'#71818c');icon(x-3,y-6,6,10,['Share2','Link','Crop','Backpack','ChartColumn'][j],[YELLOW,PINK,'#aba4d6',CYAN,MINT][j]);text(x-6,y+7,12,4,'Text Here',1.5,LIGHT,600,'center');pbody(x-9,25 if j%2==0 else 76,20,17,size=1.2)
    elif i==26:
     pts=[(49,29),(64,47),(59,74),(42,74),(35,47)];
     for j in range(5):line(*pts[[0,2,4,1,3][j]],*pts[[0,2,4,1,3][(j+1)%5]],'#6b7f8a',10)
     for j,(x,y) in enumerate(pts):circle(x,y,5.1,DARK,'3px solid #7a8d99');icon(x-2,y-6,4,8,['UserRound','Link','MapPin','Briefcase','Users'][j],[YELLOW,PINK,CYAN,MINT,'#b2a9d4'][j]);text(x-5,y+3,10,4,'Data name',1.3,LIGHT,600,'center');xx=58 if j==0 else 73 if j in [1,2] else 5;yy=18 if j==0 else 40 if j in [1,4] else 70;text(xx,yy,26,4,'Description goes here',1.5,LIGHT,600);pbody(xx,yy+6,26,13,size=1.1)
    else:
     for j in range(6):a=math.radians(-120+j*60);x=50+13*math.cos(a);y=51+13*16/9*math.sin(a);hexagon(x,y,7.8,'#4c5e6b',True);icon(x-3,y-8,6,11,['MapPin','ShoppingBag','ThumbsUp','MessageCircle','Network','Check'][j],[YELLOW,PINK,CYAN,'#dc7b87','#a99bdd',GREEN2][j]);text(x-6,y+6,12,4,'Text Here',1.5,LIGHT,600,'center');xx=8 if x<50 else 74;yy=18+(j%3)*24;text(xx,yy,20,4,'Description goes here',1.4,LIGHT,600,'right' if x<50 else 'left');pbody(xx,yy+5,20,17,align='right' if x<50 else 'left',size=1.1)
   elif i in [19,25]:
    # Simple donut data is redrawn from analytical segments, without source contours.
    cx=50 if i==19 else 31;cy=54
    for j,(a,b,c) in enumerate([(-170,-40,'#829dab'),(-40,50,CYAN),(50,110,MINT),(110,190,'#9c91d0')]):sector(cx,cy,16,10,a,b,c)
    if i==19:
     for j,(x,y) in enumerate([(7,33),(73,33),(7,65),(73,65)]):icon(x+10,y-10,4,7,['Share2','Crop','Link','Network'][j],[LIGHT,CYAN,'#9992d4',MINT][j]);box(x,y,21,20,'#44555f');text(x+2,y+3,18,4,'Description goes here',1.4,LIGHT,600);pbody(x+2,y+8,18,12,size=1.1)
    else:
     for j in range(2):text(63,25+j*36,28,7,'56%' if j==0 else '21%',3.4,LIGHT);text(63,34+j*36,30,4,'Description goes here',1.5,LIGHT,600);pbody(63,41+j*36,28,19,size=1.3)
   elif i==20:
    for j in range(4):x=17+j*23;circle(x,37,9,DARK,'1px solid #788e9c');arc(x,37,9,0,180,['#a99be5',MINT,GREEN2,CYAN][j],11);icon(x-2.5,30,5,9,['Share2','Link','Crop','Backpack'][j],LIGHT);chip(x-7,43,14,6,'STEP '+str(j+1).zfill(2),1.5,'transparent',LIGHT,600,0);line(x,53,x,59,['#a99be5',MINT,GREEN2,CYAN][j],4);circle(x,59,1.7,['#a99be5',MINT,GREEN2,CYAN][j]);text(x-10,66,20,4,'Your text here',1.5,LIGHT,600,'center');pbody(x-10,72,20,17,align='center',size=1.1)
   elif i==31:
    for j,(x,y,co,pct) in enumerate([(14,20,CYAN,'42%'),(63,42,PINK,'32%')]):box(x,y,20,26,co,15);path([(x+7 if j==0 else x+9,y+26),(x+4 if j==0 else x+16,y+36),(x+13 if j==0 else x+14,y+26)],co,co,0);chip(x,y,20,26,pct,5.8,'transparent','#fff',400,0);xx=x+24 if j==0 else 27;yy=y+5 if j==0 else 58;text(xx,yy,40,5,pct+' of marketers',1.7,LIGHT,600);pbody(xx,yy+7,40 if j==0 else 31,19,align='left' if j==0 else 'right',size=1.4)
   elif i==37:
    box(7,19,27,34,'#495b68');icon(9,24,5,8,'Shield',LIGHT);text(9,35,22,15,'The\nOrganization',2.7,LIGHT,600)
    for j in range(4):x=35+(j%2)*30;y=20+(j//2)*35;box(x,y,29,34,'transparent',border='1px solid #71818b');text(x+3,y+5,24,5,['Strengths (S)','Weaknesses (W)','Opportunities (O)','Threats (T)'][j],2,[MINT,YELLOW,CYAN,'#64b3d2'][j],600);pbody(x+3,y+12,24,19,t='• Clear and measurable presentation\n  of your information and ideas.\n• Better decisions and useful\n  resources for your organization.',size=1.2)
    pbody(8,63,24,24,t='Positive strategies, protection\nand development, with clear goals\nand knowledge. Explore the steps\nyou can take to build success.',size=1.6)
   elif i==38:
    E=[];pitchhead('Data comparison');image(6,15,86,70)
    for x,y,r in [(20,28,5),(30,57,4),(54,49,8),(75,29,6),(82,66,5)]:circle(x,y,r,'#15c5bf');chip(x-r,y-r*16/9,2*r,2*r*16/9,'79%',2.4,'transparent','#fff',500,0);circle(x-r*.8,y+1,r*.6,'#ed5869');chip(x-r*1.4,y+1-r*.6*16/9,r*1.2,r*1.2*16/9,'21%',1.8,'transparent','#fff',500,0)
   else:raise ValueError((pv,i))
  save('p105',f's{pv:02}-{i:02}',bg,title)
# Corrected irregular-sheet cells. Reassign semantic pages by stable crop identity.
old={k:v for k,v in DATA.items() if k.startswith('p105/s03-')}
for m in json.load(open(ROOT/'review/group-b-p105-crop-correction.json')):
 if m['old'] and m['new']!='s03-25':
  v=json.loads(json.dumps(old['p105/'+m['old']]));v['id']=m['new'];DATA['p105/'+m['new']]=v
for i in [25,31,32,34]:
 E=[];FONT='Roboto';pitchhead()
 if i==25:
  # A native218×377 vertical slide is centered with equal scale in both directions.
  E=[];box(0,0,100,100,'#fff');box(33.7,0,32.6,100,DARK);text(35,2,28,3,'☰  timeline',.9,LIGHT);line(50,7,50,96,'#687983',.5)
  for j in range(6):
   x=37 if j%2==0 else 54.5;y=8+(j//2)*33+(4 if j%2 else 0);image(x,y,8.5,10.5);xx=x+8.5 if j%2==0 else x-2.4;box(xx,y,2.4,6.5,'#4b5b66');text(xx,y+.5,2.4,1.5,'JUNE',.4,LIGHT,align='center');text(xx,y+2.1,2.4,3,"'14",1.3,LIGHT,align='center');circle(50,y,.33,'#fff');title=['Build more team','Company Kick-off','We bought micro, Inc.','Big projects started','#1 Ranked on Google','Prepare for bright 2016'][j];text(x,y+11.8,8.5,2,title,.64,LIGHT,600,'right' if j%2==0 else 'left')
   if j==3:pline(x,y+17,8.5,5.8,1)
   elif j==4:phbars(x+.7,y+17,7.8,6)
   else:pbody(x,y+15,8.5,6,align='right' if j%2==0 else 'left',size=.37)
  text(34.6,97.7,4,1.5,'Pitch',.7,LIGHT,font='Kaushan Script');bg='#fff'
 elif i in [31,32]:
  x=74 if i==31 else 25;pdonut(x,53,16,.58,CYAN);sector(x,53,16,14,-170,-120,PINK);sector(x,53,16,14,-120,-90,YELLOW);icon(x-3,40,6,10,'Archive',LIGHT);chip(x-11,51,22,9,'$58,289.718',2.9,'transparent',LIGHT,600,0);text(x-12,62,24,4,'Net Market Volume',1.1,LIGHT,align='center')
  if i==31:
   ptitle('Those who rules this business',8,22,43,2.9)
   for j in range(4):pmetric(8+(j%2)*20,30+(j//2)*28,19,25,['58%','13%','17%','12%'][j],['Online shop','Market Promotion','Local business','Social media ads'][j],SERIES[j])
  else:
   ptitle('Those who rules this business',49,21,48,2.9)
   for j in range(3):text(50,31+j*20,12,8,['58%','17%','13%'][j],3.3,[MUTED,CYAN,PINK][j]);text(50,40+j*20,12,4,'$12,000K',1.5,LIGHT,600);text(65,32+j*20,31,5,['Online shop','Local store','Social media promotion'][j],1.7,LIGHT,600);pbody(65,39+j*20,29,12,size=1.1)
  bg=DARK
 else:
  for j,(a,b,c) in enumerate([(-180,-90,PINK),(-90,55,YELLOW),(55,180,GREEN2)]):sector(50,51,16,14,a,b,c)
  chip(40,43,20,16,'market\nshare',3.4,'transparent',LIGHT,400,0)
  for j,(x,y,ico) in enumerate([(35,29,'Share2'),(65,29,'Flag'),(38,73,'User')]):circle(x,y,3.7,DARK,'1px solid #eee');icon(x-2,y-3.5,4,7,ico,LIGHT)
  for j,(x,y,w,t,pct) in enumerate([(7,19,23,'Earnings','21%'),(7,58,23,'Geo location','31%'),(70,32,25,'Gender','17%')]):text(x,y,w,5,t,2.3,LIGHT,600,'right' if j<2 else 'left');box(x,y+7,w,25,'#44545f');text(x+2,y+10,w-4,5,'Data name  '+pct,2.2,LIGHT);pbody(x+2,y+18,w-4,12,size=1.1)
  bg=DARK
 save('p105',f's03-{i:02}',bg,'Vertical timeline' if i==25 else 'Market data infographic')
# Semantic corrections from the first individual comparison round.
for key,slide in DATA.items():
 if key.startswith('p105/'):
  for e in slide['elements']:
   if e['kind']=='chip' and e.get('text') in ['SMARTPHONE, TABLET, AND MORE','DATA DRIVEN AND NUMBERS','VECTOR AND NUMBERS']: e['letterSpacing']=3
   if e['kind']=='path' and e.get('fill')=='transparent':e['strokeWidth']=4
   if e['kind']=='text' and e.get('text')=='12,000K development cost\n\n58% marketing ratio\n\n17% maintenance':e['h']=20
   if e['kind']=='text' and e.get('text')=='Investment Package':e['h']=12
for pv in [2,4]:
 for i in range(1,17):
  s=DATA[f'p100/s{pv:02}-{i:02}']
  if pv==4 and i<=4:
   for e in s['elements']:
    if e.get('text')=='Infographic Powerpoint Template': e['y']=21
  if (pv==2 and i in [1,2,3,4,7,8]) or (pv==4 and i in [1,2,3,4,7,8,10]):
   s['background']='#e5e5e5'
   s['elements'].insert(0,dict(kind='image',x=0,y=0,w=100,h=100,text='Graphic background placeholder'))
   NOTES[f'p100/s{pv:02}-{i:02}']+=' Source gradient/graphic background is represented by a flat light gray placeholder.'
# Rebuild banded bulbs at their own source positions.
for pv in [2,4]:
 i=4 if pv==2 else 2;E=[];FONT='Roboto';lamphead(False)
 if pv==4:E[0]['y']=21
 cols=[LAMP[5],LAMP[3],LAMP[2],LAMP[1],LAMP[0]] if pv==2 else [LAMP[0],LAMP[3],LAMP[1],LAMP[2],LAMP[4]]
 ys=[7,19,31,42,54] if pv==2 else [31,42,53,64,75]
 widths=[16,23,25,22,14]
 for j in range(5):
  y=ys[j];w=widths[j]
  if j==0:
   path([(50+w/2*math.cos(math.radians(a)),y+11+w/2*16/9*math.sin(math.radians(a))) for a in range(180,361,6)]+[(50+w/2,y+11),(50-w/2,y+11)],cols[j],cols[j],0)
  else:path([(50-w/2,y),(50+w/2,y),(50+w/2-.7,y+10),(50-w/2+.7,y+10)],cols[j],cols[j],0)
  if pv==2:icon(48,y+3,4,7,['Share2','PanelTop','ChartColumn','Archive','Building'][j],'#fff')
  else:chip(45,y+2,10,7,str(j+1).zfill(2),1.8,'transparent','#fff',600,0)
 for j in range(3):box(45,(69 if pv==2 else 89)+j*4,10,2.8,'#ccc',6)
 labs=[(67,12,False),(11,21,True),(67,31,False),(11,44,True),(67,61,False)] if pv==2 else [(69,29,False),(15,42,True),(69,54,False),(15,64,True),(69,79,False)]
 for j,(x,y,left) in enumerate(labs):lamp_label(x,y,cols[j],20,left)
 E.insert(0,dict(kind='image',x=0,y=0,w=100,h=100,text='Graphic background placeholder'))
 save('p100',f's{pv:02}-{i:02}','#e5e5e5','Lamp Infographic')
# Colored glass follows an analytical bulb silhouette rather than separate circles.
for key,colors in [('p100/s02-10',[LAMP[2],LAMP[1],LAMP[3],LAMP[0]]),('p100/s04-08',[LAMP[0],LAMP[1],LAMP[5],LAMP[3]]),('p100/s04-15',['#fff',LAMP[2],LAMP[4],'#111'])]:
 s=DATA[key];cx,cy,r=(50,49,12) if key.endswith('s02-10') else (50,49,9) if key.endswith('s04-08') else (50,44,13)
 s['elements']=[e for e in s['elements'] if not(e['kind']=='path' and e.get('fill') in colors and len(e.get('points',[]))==62)]
 E=[];bulb_cells(cx,cy,r,colors)
 insertion=next((j for j,e in enumerate(s['elements']) if e['kind']=='path' and len(e.get('points',[]))>65),len(s['elements']))+1
 s['elements'][insertion:insertion]=E
# Three independent plant illustrations preserve their individual gray bounds.
s=DATA['p100/s04-16'];s['elements']=[e for e in s['elements'] if e['kind']!='image']
s['elements'][1:1]=[dict(kind='image',x=x,y=y,w=w,h=h,text='Plant illustration placeholder') for x,y,w,h in [(19,33,17,64),(35,23,16,74),(65,45,15,52)]]
# Small source social artwork remains imagery, while diagrams stay semantic.
for x,y in [(10,43),(72,65)]:DATA['p105/s04-31']['elements'].insert(3,dict(kind='image',x=x,y=y,w=15,h=20,text='Social image icon placeholder'))
# The market ring has a thick muted remainder and three short actual chart arcs.
for i in [31,32]:
 s=DATA[f'p105/s03-{i:02}'];cx=74 if i==31 else 25
 s['elements']=[e for e in s['elements'] if not(e['kind']=='path' and (e.get('color') in ['#6e8794',CYAN] and e.get('fill') is None or e.get('fill') in [PINK,YELLOW] and len(e.get('points',[]))==62))]
 E=[];arc(cx,53,16,0,360,'#6e8794',26);arc(cx,53,16,90,180,CYAN,26);arc(cx,53,16,180,225,PINK,26);arc(cx,53,16,225,270,YELLOW,26)
 s['elements'][4:4]=E
# Portrait timeline charts use their own small typographic and geometric scale.
s=DATA['p105/s03-25']
for e in s['elements']:
 if e['kind']=='text' and e.get('size',0)>7 and e.get('text') in ['100','75','50','25','0','Mar','Jun','Sept','Dec','Phase 1','Phase 2','Phase 3','Phase 4']:e['size']*=.45
 if e['kind']=='path' and e.get('strokeWidth',0)>1:e['strokeWidth']=.65
 if e['kind']=='box' and e.get('fill') in [CYAN,GREEN2] and e['w']<9 and e['h']<3:e['h']=.35
 if e['kind']=='box' and e.get('radius')==999 and e['w']>1:e['w']*=.35;e['h']*=.35
# This partial upper cell exposes a gauge at 25%, not the 33% position of another template.
s=DATA['p105/s03-39']
for e in s['elements']:
 if e['kind']=='path':
  for p in e.get('points',[]):
   if p['y']<50:p['y']-=8
 elif e['y']<50 and e.get('text') not in ["Let's talk about data",'Pitch','Good Presentation for Your Pitch','www.goodpitch.co'] and e.get('icon')!='Menu':e['y']-=8
# Source upper strip: a bar chart and a right-side shop metric, completed in the same style.
E=[];FONT='Roboto';pitchhead();pbars(9,25,33,54,1,teal=True);ptitle('Those who rules this business',49,18,48,2.9)
for j in range(3):
 text(50,29+j*20,12,8,['58%','17%','13%'][j],3.3,[MUTED,CYAN,PINK][j]);text(50,38+j*20,12,4,'$12,000K',1.5,LIGHT,600);text(65,30+j*20,31,5,['Online shop','Local store','Social media promotion'][j],1.7,LIGHT,600);pbody(65,37+j*20,29,12,size=1.1)
save('p105','s03-40',DARK,'Market bar data infographic')
# Add legible geographic labels visible below the data bubbles.
E=[]
for x,y,w,t in [(8,36,24,'NORTH AMERICA'),(16,65,25,'SOUTH AMERICA'),(69,21,21,'EAST ASIA'),(50,62,28,'EUROPE AND EAST ASIA'),(78,54,15,'AFRICA'),(82,76,16,'OCEANIA')]:text(x,y,w,3,t,.9,LIGHT,600)
DATA['p105/s04-38']['elements']+=E
# Caption labels in device bars are single series in the source.
s=DATA['p105/s04-23'];s['elements']=[e for e in s['elements'] if not(e['kind']=='path') and not(e['kind']=='box' and e.get('fill') in [CYAN,GREEN2]) and not(e['kind']=='text' and e.get('size',100)<12)]
E=[]
for j,(v,c) in enumerate([(1,YELLOW),(.9,MINT),(.72,MUTED),(.86,CYAN)]):box(9,61+j*5.2,22*v,1.3,c);text(10+22*v,60.7+j*5.2,11,3,'Data average',.7,MUTED)
s['elements']+=E
# Keep the social origin icons around the source donut, using gray image placeholders.
for x,y in [(16,20),(42,21),(45,59),(27,62)]:DATA['p105/s04-25']['elements'].append(dict(kind='image',x=x-2.5,y=y-4.5,w=5,h=9,text='Social image icon placeholder'))


# Final typography and clean connector corrections from round 2.
s=DATA['p055/s02-09']
for e in s['elements']:
 if e.get('text')=='Add text\nhere':
  cx=e['x']+2.5;cy=e['y']+9;e.update(x=cx-.7,y=cy+7,w=8,h=2.4,text='Add text here',rotate=-90,nowrap=True)
s=DATA['p055/s02-06'];s['elements']=[e for e in s['elements'] if not(e['kind']=='path' and e.get('color')=='#d8dcdd') and not(e['kind']=='text' and e.get('color')=='#6d7274')]
E=[]
for j in range(5):line(8,76-j*53/4,56,76-j*53/4,'#d8dcdd',1);text(3,74.5-j*53/4,4,3,str(20+j*10)+'%',.9,'#6d7274',align='right')
s['elements'][3:3]=E
s=DATA['p055/s02-11'];E=[]
for j in range(2):
 box(55.8,73+j*13,31 if j==0 else 27,8,'#7c96a4' if j==0 else '#b8b8b8',99,'2px solid #d5e1e7')
for e in s['elements']:
 if e.get('text') in ['70','60']:e['w']=5
s['elements'][3:3]=E
# Connectors draw beneath solid hexagons, so they never cross icon glyphs.
s=DATA['p060/s02-09'];connect=[e for e in s['elements'] if e['kind']=='path' and len(e.get('points',[]))==2 and e.get('strokeWidth')==5]
s['elements']=[e for e in s['elements'] if e not in connect]
for e in connect:e['strokeWidth']=12
s['elements'][4:4]=connect
s=DATA['p060/s02-10'];E=[];hexagon(18,36,6.3,'#fff',True);ri=next(j for j,e in enumerate(s['elements']) if e.get('icon')=='Recycle');s['elements'][ri]['color']=GREEN[0];s['elements'][ri:ri]=E
# Source circle colors follow the six ingredient positions.
s=DATA['p060/s02-13']
for e in s['elements']:
 if e['kind']=='box' and e.get('radius')==999 and e.get('fill') in GREEN:
  cx=e['x']+e['w']/2;cy=e['y']+e['h']/2;e['fill']=GREEN[2] if cx<48 else GREEN[1] if cx>52 and cy>51 else GREEN[0]
# Complex decorative honeycomb backgrounds use the requested gray flat placeholder.
for key,rect in [('p060/s02-06',(4,25,90,63)),('p060/s02-08',(6,22,43,67))]:
 DATA[key]['elements'].insert(4,dict(kind='image',x=rect[0],y=rect[1],w=rect[2],h=rect[3],text='Decorative graphic background placeholder'))

# Preserve known visible lower coordinates in the cropped investment cell.
s=DATA['p105/s03-02']
for e in s['elements']:
 if e.get('text')=='The best investment in 2014 by TechWorld':e['y']=66;e['size']=2.2*12.8
 elif e.get('text')=='$12,000K':e['y']=66;e['size']=2*12.8
 elif e.get('text')=='34%':e['y']=66
 elif e.get('text')=='5 Years':e['y']=77
 elif e.get('text')=='Market Growth\nOpportunity':e['text']='';e['y']=66
 elif e['kind']=='text' and e.get('text','').startswith('Lorem ipsum'):e['y']=75 if e['x']<20 else 75;e['size']=1.15*12.8;e['h']=11
 elif e['kind']=='box' and e['x']==82:e['y']=63
 elif e['kind']=='box' and e.get('radius')==999 and e['x']<15:e['y']+=23
 elif e['kind']=='icon' and e['x']<15:e['y']+=23
NOTES['p105/s03-02']+=' Original top two-thirds are missing. Preserved the visible lower investment line and reconstructed unseen upper space.'
# The cropped comparison exposes a two-group bar chart and right information rows.
E=[];FONT='Roboto';pitchhead();ptitle('Data comparison',9,16,82,3.6);pbars(9,26,34,54,2)
for j,(pct,co,lab) in enumerate([('58%',LIGHT,'Online shop'),('17%',CYAN,'Local store'),('13%',PINK,'Solid media promotion')]):
 text(50,30+j*20,11,8,pct,3,co);text(50,40+j*20,11,4,'$12,000K',1.5,LIGHT,600);text(60,31+j*20,34,5,lab,1.8,LIGHT,600);pbody(60,38+j*20,33,11,size=1.1)
save('p105','s03-06',DARK,'Data comparison')
NOTES['p105/s03-06']+=' Only the lower portion is visible; reconstructed the unseen upper chart while retaining visible two chart groups and right promotion row.'
# Correct the relative single-series chart heights and visible percentage colors.
for key in ['p105/s03-12','p105/s03-17','p105/s03-31']:
 s=DATA[key]
 for e in s['elements']:
  if key.endswith('s03-12') or key.endswith('s03-31'):
   if e.get('text')=='58%':e['color']=LIGHT
   elif e.get('text')=='13%':e['color']=PINK
   elif e.get('text')=='12%':e['color']=YELLOW
 if key.endswith('s03-12'):
  bars0=[e for e in s['elements'] if e['kind']=='box' and e['x']>50 and e.get('fill') in SERIES and not e.get('radius')]
  for e,v in zip(bars0,[23,40,18,58]):base=e['y']+e['h'];e['h']=53*v/80;e['y']=base-e['h']
 if key.endswith('s03-17'):
  bars0=[e for e in s['elements'] if e['kind']=='box' and e['x']>50 and e.get('fill') in [LIGHT,MUTED,GREEN2] and not e.get('radius')]
  for e,v in zip(bars0,[43,60,33,72]):base=e['y']+e['h'];old=e['y'];e['h']=55*v/80;e['y']=base-e['h'];delta=e['y']-old
  # Icon badges follow the top of each source bar.
  for e in s['elements']:
   if e['kind']=='box' and e.get('radius')==999 and e['x']>50 and e['w']<7:
    b=min(bars0,key=lambda b:abs((b['x']+b['w']/2)-(e['x']+e['w']/2)));e['y']=b['y']-e['h']/2
   elif e['kind']=='icon' and e['x']>50:
    b=min(bars0,key=lambda b:abs((b['x']+b['w']/2)-(e['x']+e['w']/2)));e['y']=b['y']-e['h']/2
# True simple human pictograms match source filled/outlined rows.
s=DATA['p105/s04-04'];s['elements']=[e for e in s['elements'] if e.get('icon')!='PersonStanding'];E=[]
for row in range(2):
 for j in range(10):
  x=(49+j*3.25 if row==0 else 19+j*3.5);y=32 if row==0 else 65;filled=j<7 if row==0 else j>=6;co=LIGHT if filled else MUTED
  circle(x+1.5,y,.48,co if filled else DARK,None if filled else '1.3px solid '+co)
  pp=[(x+.85,y+1.3),(x+2.15,y+1.3),(x+2.6,y+4),(x+2.1,y+4.1),(x+1.95,y+2.5),(x+1.95,y+7.8),(x+1.35,y+7.8),(x+1.35,y+5),(x+1.1,y+7.8),(x+.5,y+7.8),(x+1.05,y+2.5),(x+.9,y+4.1),(x+.4,y+4)]
  path(pp,co,co if filled else DARK,0 if filled else 1.3)
s['elements']+=E
# Large ring interiors stay dark, and map leaders end with real text captions.
s=DATA['p105/s04-08'];E=[]
for x in [28,51,74]:circle(x,38,4.05,DARK)
s['elements']+=E
for key in ['p105/s04-09','p105/s04-21']:
 s=DATA[key];E=[]
 for e in s['elements']:
  if e['kind']=='box' and e.get('radius')==999 and e['w']==1:
   cx=e['x']+.5;cy=e['y']+e['h']/2;text(cx-7,cy+1.5,14,3,'Regional sales',.85,LIGHT,align='center')
 s['elements']+=E
for key,cx,cy in [('p105/s04-15',24,48),('p105/s04-27',66,59)]:E=[];circle(cx,cy,1.15,DARK,'2px solid #fff');DATA[key]['elements']+=E
E=[]
for x,y,up in [(15,41,True),(32,58,False),(50,41,True),(67,58,False),(85,41,True)]:path([(x-3,y+2 if up else y-2),(x,y),(x+3,y+2 if up else y-2)],'#586b76',sw=7)
DATA['p105/s04-14']['elements']+=E
E=[];icon(78,10,14,22,'Quote','#4e5e68');DATA['p105/s03-28']['elements'][4:4]=E
# Preserve the page's core chart proportions with lighter source sector colors.
s=DATA['p100/s02-13']
for e in s['elements']:
 if e['kind']=='path' and e.get('fill') in LAMP:e['fill']=e['color']={LAMP[0]:'#757acb',LAMP[2]:'#b2df34',LAMP[1]:'#dd9950',LAMP[3]:'#d0647e'}.get(e['fill'],e['fill'])
 if e['kind']=='chip' and e.get('text','').startswith('YOUR TEXT'):e['text']='YOUR TEXT\nLorem ipsum is simply\ndummy text of the printing.';e['size']=1.35*12.8
# Approved third integration corrections: only these two pages change.
for e in DATA['p055/s02-07']['elements']:
 if e['kind']=='chip' and e.get('text')=='Last stage':e['fill']=BLUE[3]
s=DATA['p055/s02-11'];bars0=[e for e in s['elements'] if e['kind']=='box' and e.get('fill') in ['#7c96a4','#b8b8b8']];labels0=[e for e in s['elements'] if e.get('text') in ['70','60']]
s['elements']=[e for e in s['elements'] if e not in bars0 and e not in labels0]+bars0+labels0
# Approved final integration fixes for clear colors and overlapping caption.
s=DATA['p055/s02-02'];labels0=[e for e in s['elements'] if e['kind']=='chip' and e.get('text')=='You can use this\ncontent']
for e,k in zip(labels0,[0,1,4,2,0,3]):e['fill']=BLUE[k]
s=DATA['p055/s02-04'];labels0=[e for e in s['elements'] if e['kind']=='chip' and e.get('text')=='You simply add your own\ntext and description here']
for e,k in zip(labels0,[0,3,4,1,2,3,0]):e['fill']=BLUE[k]
s=DATA['p055/s02-09'];pill=[e for e in s['elements'] if e['kind']=='chip' and e.get('text')=='' and e['h']==35]
for e,k in zip(pill,[0,1,2,3,0,4,1]):e['fill']=BLUE[k]
s=DATA['p060/s02-13']
for e in s['elements']:
 if e['kind']=='text' and e.get('align')=='center' and e.get('text')=='Your Text Here':e['x']=38.5;e['color']=GREEN[0]
 elif e['kind']=='text' and e.get('align')=='center' and e.get('text','').startswith('Lorem ipsum'):
  e['x']=38.5;e['text']='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.';e['h']=7
 elif e['kind']=='text' and e.get('text')=='Your Text Here' and e['x']<30:e['color']=GREEN[2]
# Integration correction of numbered box colors and connector crossings.
for e in DATA['p100/s04-02']['elements']:
 if e['kind']=='chip' and e.get('text') in ['2','3','4']:e['fill']={'2':LAMP[3],'3':LAMP[1],'4':LAMP[2]}[e['text']]
for e in DATA['p100/s04-05']['elements']:
 if e['kind']=='path' and e.get('color')=='#aaa' and len(e.get('points',[]))==3:
  pp=e['points']
  if pp[0]['x']==18:pp[0]['y']=37;pp[1]['y']=37
  elif pp[0]['x']==61:pp[1]['y']=32;pp[2]['y']=32
# Five simple source rays around the six-cell bulb.
E=[]
for x1,y1,x2,y2 in [(50,27,50,20),(39,32,35,25),(61,32,65,25),(35,51,30,51),(65,51,70,51)]:line(x1,y1,x2,y2,'#aaa',3)
DATA['p100/s04-13']['elements'][3:3]=E
# Approved third integration legend follows the actual four-series bar palette.
legend0=[e for e in DATA['p105/s03-18']['elements'] if e['kind']=='box' and e['y']==95 and e['w']==1.5]
for e,co in zip(legend0,[LIGHT,MUTED,GREEN2,MUTED]):e['fill']=co
# Approved final integration: percentage glyphs stay above all overlapping circles.
s=DATA['p105/s04-38'];numbers0=[e for e in s['elements'] if e.get('text') in ['79%','21%']]
s['elements']=[e for e in s['elements'] if e not in numbers0]+numbers0
# Persist only clean semantic primitive data owned by this worker.
# Final refinements after second individual comparison, preserving semantic geometry.
for key in ['p100/s02-06','p100/s04-09','p100/s02-12']:
 s=DATA[key];s['elements']=[e for e in s['elements'] if not(e['kind']=='path' and not e.get('fill') and len(e.get('points',[]))==10) and not(key.endswith('s02-12') and e['kind']=='icon' and e.get('icon')!='Users')]
for key in ['p100/s04-06','p100/s04-09']:
 for e in DATA[key]['elements']:
  if e['kind']=='box' and e.get('fill') in ['#363620','#fff074'] and e['y']>70:e['fill']='#aaa'
  if key.endswith('s04-06') and e['kind']=='path' and len(e.get('points',[]))==10:e['strokeWidth']=7
for s in [v for k,v in DATA.items() if k.startswith('p100/')]:
 for e in s['elements']:
  if e['kind']=='icon' and e.get('color')=='#fff' and e['w']>=4:e['x']+=e['w']*.1875;e['y']+=e['h']*.1875;e['w']*=.625;e['h']*=.625
s=DATA['p100/s04-03']
for e in s['elements']:
 if e['kind']=='path' and e.get('color') in LAMP and not e.get('fill'):e['curved']=True
s=DATA['p100/s04-02'];E=[]
for x,y,k,left in [(15,42,1,True),(15,64,3,True),(69,29,0,False),(69,54,2,False),(69,79,4,False)]:chip(x-7 if left else x+23,y,4.5,8,str(k+1),1.5,LAMP[k],r=1)
s['elements']+=E
s=DATA['p100/s04-15']
for e in s['elements']:
 if e.get('text')=='Infographic Powerpoint Template':e['color']='#333'
for j,e in enumerate([e for e in s['elements'] if e['kind']=='text' and e.get('text')=='YOUR TEXT']):e['color']='#fff' if j==0 else e['color']
# Simple straight callout rules remain genuine geometry.
s=DATA['p100/s04-05'];E=[]
for pp in [[(18,37),(41,37),(41,46)],[(61,42),(61,32),(81,32)],[(24,72),(44,72),(44,62)],[(60,68),(60,77),(83,77)]]:path(pp,'#aaa',sw=1)
s['elements']+=E
# Apply numbered chip colors after the final label append.
for e in DATA['p100/s04-02']['elements']:
 if e['kind']=='chip' and e.get('text') in ['2','3','4']:e['fill']={'2':LAMP[3],'3':LAMP[1],'4':LAMP[2]}[e['text']]
# Root third-integration restoration of the source arrow, two columns, and card corners.
s=DATA['p055/s02-01'];s['elements']=[e for e in s['elements'] if not(e['kind']=='text' and e['y'] in [80,84])];E=[];FONT='Roboto'
for x in [6,25]:
 text(x,80,18,4,'Place your own text',1.4,'#222',500)
 para(x,84,18,9,1.08,'#666',t='Add your financial ideas.\nShare a useful description.\nPresent your results clearly.')
line(76,22.5,98.2,89.5,'#999',2);path([(76,22.5),(75.8,25.5),(77.5,24.1)],'#999','#999',0);circle(98.2,89.5,.35,'#555')
s['elements']+=E
for e in DATA['p055/s02-16']['elements']:
 if e['kind']=='box' and e.get('fill')=='#f6f6f6' and e['w']==24:e['radius']=15
(ROOT/'src/decks/group-b-extra-data.json').with_suffix('.json.tmp').write_text(json.dumps(DATA,ensure_ascii=False,separators=(',',':')))
(ROOT/'src/decks/group-b-extra-data.json.tmp').replace(ROOT/'src/decks/group-b-extra-data.json')
(ROOT/'review/group-b-extra-notes.json').with_suffix('.json.tmp').write_text(json.dumps(NOTES,indent=2))
(ROOT/'review/group-b-extra-notes.json.tmp').replace(ROOT/'review/group-b-extra-notes.json')
(ROOT/'src/decks/group-b-extra.ts.tmp').write_text("import type {Deck, Slide} from '../model'\nimport {D} from '../primitives'\nimport manifest from '../../public/reference/groups/b.json'\nimport data from './group-b-extra-data.json'\n// Per-page data uses reusable semantic charts, shapes, tables and actual DOM text.\nconst owned = new Set(['p055','p060','p100','p105'])\nconst pages = data as unknown as Record<string,Slide>\nconst decks:Deck[] = manifest.filter(d => owned.has(d.id)).map(d => D(d.id,d.title,d.slides.map(s => pages[d.id+'/'+s.id])))\nexport default decks\n")
(ROOT/'src/decks/group-b-extra.ts.tmp').replace(ROOT/'src/decks/group-b-extra.ts')
print(len(DATA))
