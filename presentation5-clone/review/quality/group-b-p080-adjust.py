import json,copy,os,math
P='src/decks/group-b-data.json';d=json.load(open(P));q=json.load(open('review/quality/group-b.json'));fm={t:(w,h)for t,w,h in json.load(open('review/quality/group-b-p080-font-metrics.json'))['Michroma']}
def es(s):return d['p080/'+s]['elements']
def up(s,i,r,**kw):
 e=es(s)[i];old=copy.deepcopy(e);e.update(kw);q['pages']['p080/'+s]['changes'].append({'element':i,'before':old,'after':copy.deepcopy(e),'reason':r})
def add(s,e,r):es(s).append(e);q['pages']['p080/'+s]['changes'].append({'added':copy.deepcopy(e),'reason':r})
def txt(s,text,x,y,w,size=14,font='DM Sans',weight=400,align='left',h=8,color='#fff',**kw):add(s,dict(kind='text',text=text,x=x,y=y,w=w,h=h,size=size,font=font,weight=weight,align=align,color=color,lineHeight=1.15,nowrap=True,**kw),'원문 가독 문구 또는 판독불가 정상 문구 DOM/원문 줄 수 보완')
def line(s,x,y,x2,y2,color='#777',stroke=1):add(s,dict(kind='path',x=0,y=0,w=100,h=100,points=[dict(x=x,y=y),dict(x=x2,y=y2)],color=color,strokeWidth=stroke,closed=False,fill=None),'원문 단순 구분선 복원')
def star(s,x,y,w=2.2,h=4):
 pts=[{'x':50+(48 if i%2==0 else 20)*math.cos(-math.pi/2+i*math.pi/5),'y':50+(48 if i%2==0 else 20)*math.sin(-math.pi/2+i*math.pi/5)}for i in range(10)]
 add(s,dict(kind='path',x=x,y=y,w=w,h=h,points=pts,fill='#645740',color='#645740',strokeWidth=.5,closed=True),'원문 filled 별 도형, 빈 Lucide 윤곽을 실제 단순 polygon으로 복원')
widths={'s02-01':364,'s02-02':334,'s02-03':214,'s02-04':482,'s02-05':493,'s03-01':384,'s03-02':333,'s03-03':252,'s03-04':239,'s03-05':554,'s03-06':382,'s03-07':316,'s03-08':315,'s03-09':365,'s06-03':364,'s06-04':552,'s06-05':233,'s06-06':373,'s06-07':373,'s06-08':458,'s06-09':479,'s08-02':333,'s08-03':252,'s08-04':214}
for s,sw in widths.items():
 i=next(i for i,e in enumerate(es(s))if e.get('font')=='Michroma' and e.get('size',0)>60);e=es(s)[i];nw=fm[e['text']][0]*60/58;track=(sw-nw)/max(1,len(e['text'])-1)
 up(s,i,'각 페이지 원문 native 주제목 ink 폭, actual Michroma600? weight400/크기60px·자간 개별 측정 대응. 높이는 원문47~50px 근접',size=60,letterSpacing=round(track,2),h=13,y=19,x=3.6)
 q['pages']['p080/'+s]['measurements'].append({'role':'primary-title','targetInkWidthPx':sw,'fontActualLoaded':'Michroma','fontSizePx':60,'canvasInkWidthPx':nw,'letterSpacingPx':round(track,2),'basis':'개별 원본/1280 PNG 관찰+actual canvas58px 측정'})
# Source thin geometric uppercase retains actual loaded Michroma. Header/source text repaired individually.
for k,p in d.items():
 if not k.startswith('p080/'):continue
 s=k.split('/')[1]
 for i,e in list(enumerate(p['elements'])):
  if e.get('text') in ['Presentation','Creative','Modern','Minimal']:up(s,i,'원문 작은 header label bold와 흰 strip 검정 글자',weight=600,color='#171717',size=14)
  if e.get('font')=='Kaushan Script' and e.get('text')=='Virginia Kelly':up(s,i,'원문 실제 signature 잉크폭 약13% 큰 handwriting: 실제 Kaushan Script 근사',size=39.5,h=8.2)
  if e.get('icon')=='Star':
   old=copy.deepcopy(e);e.clear();pts=[{'x':50+(48 if j%2==0 else 20)*math.cos(-math.pi/2+j*math.pi/5),'y':50+(48 if j%2==0 else 20)*math.sin(-math.pi/2+j*math.pi/5)}for j in range(10)];e.update(kind='path',x=old['x'],y=old['y'],w=old['w'],h=old['h'],points=pts,color=old['color'],fill=old['color'],strokeWidth=.5,closed=True);q['pages'][k]['changes'].append({'element':i,'reason':'원문 filled 단순 별을 실제 polygon 구현'})
 q['pages'][k]['remaining'].append({'reason':'실제 인물 사진 및 raster 브랜드 아이콘은 사용자 기준상 회색 단색. 서명은 실제 Kaushan Script, 주제목은 실제 Michroma로 가장 가까운 가용 서체 근사. 흐린 본문은 페이지별 원문 밀도에 맞춘 정상 영어 문구.'})
for i in [11,14,17,19]:up('s02-01',i,'원문 작은 01/ 숫자 크기',size=26)
for i in [12,15,18,20]:up('s02-01',i,'원문 subtitle은 geometric letter, 단순 sans를 교체',font='Michroma',size=16,y=es('s02-01')[i]['y']-2)
for i in [13,16]:up('s02-01',i,'원문 upper description 기준선은 약5% 위',y=43)
for i in [21,22]:up('s02-01',i,'원문 lower description 기준선은 약3% 위',y=83)
up('s02-02',1,'원문 divider는 chips 위 y44.5%',points=[{'x':0,'y':44.5},{'x':52,'y':44.5}]);line('s02-02',0,51.5,52,51.5)
for i in [12,13]:up('s02-02',i,'원문 실제 geometric 소제목19px',size=19)
up('s02-02',14,'원문 geometric 3줄 About our Creative Design 작은 size',font='Michroma',size=16,h=11)
up('s02-02',15,'원문 세 불릿 actual 문구',text='•  PROJECT NAME\n•  PROJECT PROPOSAL / 2022\n•  WWW.PROJECT.NET',size=13.5,h=10)
up('s02-02',16,'원문 upper right 4행 uppercase center',text='THERE ARE MANY VARIATIONS OF PASSAGES OF\nLOREM IPSUM AVAILABLE, BUT THE MAJORITY\nHAVE SUFFERED ALTERATION IN SOME FORM,\nBY INJECTED HUMOUR OR RANDOM WORDS.',size=13,align='center',h=12)
up('s02-02',17,'원문 Start Explore는 bold serif spacing4',font='Georgia',weight=700,size=18,letterSpacing=4,h=9)
for i in [21,22]:up('s02-02',i,'원문 4행 불릿 밀도',text='•  Strategic identity and brand concepts\n•  Clear creative direction and design\n•  Presentation systems and layouts\n•  Consistent project communication',size=12,h=10)
up('s02-02',25,'원문 작은03 circle: 제목과 겹침 해결',w=4.8,h=7,size=22)
for s in ['s02-03','s08-04']:
 up(s,13,'원문 project caption3행 작은22px',size=19,y=29,h=10)
 if s=='s02-03':
  up(s,14,'원문 4.40% lower right y74%',y=74,size=52,h=10)
  up(s,15,'원문 GOOD IDEA4행 y83%',y=83,size=21,h=13)
  txt(s,'Subtitle_',79,68,18,15,h=4)
 else:
  up(s,14,'원문 4.40% source native y74%: 기존 보정+6%',y=74,size=52,h=10)
  up(s,15,'원문 GOOD IDEA 시작은 source y83%',y=83,size=21,h=13)
  up(s,19,'원문 Subtitle_ y68%',y=68)
 up(s,11,'원문 paragraph upper boundary source72% (기존75%)',y=72)
 up(s,12,'원문 signature source87%',y=87)
for i in [14,16,18,20]:up('s02-04',i,'원문 오른쪽 설명 uppercase3행',text='THERE ARE MANY VARIATIONS OF\nPASSAGES OF LOREM IPSUM AVAILABLE,\nBUT THE MAJORITY HAVE SUFFERED.',size=12.5,h=8,lineHeight=1.15)
up('s02-04',21,'원문 왼쪽 Subtitle right aligned',x=10,w=14,align='right')
up('s02-04',23,'원문 왼쪽 설명 uppercase3행 오른쪽',text='THERE ARE MANY VARIATIONS OF\nPASSAGES OF LOREM IPSUM AVAILABLE,\nBUT THE MAJORITY.',align='right',size=12.5,x=3,w=21,h=8)
up('s02-05',17,'원문 quote의 굵은 실제 caption',weight=600)
up('s02-06',4,'원문 Contact 원래 native 잉크폭612',size=118,w=55,h=24,x=43)
up('s02-06',10,'원문 Portfolio cursive baseline 아래',y=37)
up('s02-06',2,'사진의 원문 ellipse envelope, 사진만 회색',x=5,y=20,w=30,h=60)
up('s02-06',22,'원문 quote 굵게',weight=600)
for i in [10,12,14,16]:up('s03-01',i,'원문 KPI 본문3행 굵기500',weight=500,size=15)
up('s03-01',17,'원문 upper centered uppercase2행',text='THERE ARE MANY VARIATIONS OF PASSAGES OF LOREM IPSUM\nAVAILABLE, BUT THE MAJORITY HAVE SUFFERED ALTERATION.',size=12.5,align='center',h=7)
up('s03-01',18,'원문 centered uppercase3행 두번째 문단',text='THERE ARE MANY VARIATIONS OF PASSAGES OF LOREM IPSUM\nAVAILABLE, BUT THE MAJORITY HAVE SUFFERED ALTERATION IN SOME\nFORM, BY INJECTED HUMOUR OR RANDOM WORDS.',size=12.5,align='center',h=9)
for s in ['s03-02','s08-02']:
 up(s,9,'원문 left selected stack y68%',y=68)
 up(s,10,'원문 left paragraph y80%',y=80,size=12.5,h=13)
 for i in [16,17]:up(s,i,'원문 별 stack y60%',y=60)
 up(s,11,'원문 right quote y54%',y=54)
 up(s,13,'원문 second subtitle는 두번째 본문과 x55 맞춤',x=55,w=16)
 for i in [14,15]:up(s,i,'원문 본문4행+빈행+2행 밀도',text='There Are Many More\nVariations Of Passages\nOf Lorem Ipsum Available,\nBut The Majority\n\nHave Suffered Alteration In\nSome Form, By Injected',size=12.5,h=19,lineHeight=1.2,x=35 if i==14 else 55,w=17)
for s in ['s03-03','s08-03']:
 up(s,13,'원문 Vision left selected y64%',y=64)
 up(s,14,'원문 Vision body y76%',y=76,size=12.5,h=14)
 up(s,15,'원문 Vision signature y89%',y=89)
 up(s,18,'원문 right upper prose uppercase7행 center',text='THERE ARE MANY VARIATIONS\nOF LOREM IPSUM AVAILABLE\nBUT THE MAJORITY HAVE\nSUFFERED IN SOME FORM, BY\nINJECTED HUMOUR OR RANDOM\nWORDS WHICH DO NOT LOOK\nEVEN SLIGHTLY BELIEVABLE.',size=10.5,align='center',h=13,w=16,x=83,y=37,lineHeight=1.05)
 for i in [16,17]:up(s,i,'원문 bottom descriptions uppercase6행 center',text='THERE ARE MANY VARIATIONS\nOF LOREM IPSUM AVAILABLE\nBUT THE MAJORITY HAVE\nSUFFERED BY INJECTED HUMOUR\nOR RANDOM WORDS WHICH DO\nNOT LOOK EVEN BELIEVABLE.',size=10.5,align='center',h=13,y=85,lineHeight=1.05)
up('s03-04',14,'원문 small geometric caption',size=20)
up('s03-04',16,'원문 4bullets+3+2 실제 밀도',text='•  Our creative direction and identity\n•  Consistent presentation principles\n•  Thoughtful project development\n•  Visual systems and communication\n\nTHERE ARE MANY VARIATIONS OF\nPASSAGES OF LOREM IPSUM AVAILABLE,\nBUT THE MAJORITY HAVE SUFFERED.\n\nCLEAR DESIGN BUILDS A\nCONSISTENT BRAND EXPERIENCE.',size=12,h=29,y=69,lineHeight=1.12)
up('s03-04',17,'3개 원문 outlined cells를 독립 chip 구현',text='')
for j,caption in enumerate(['BRANDING','PHOTO','PROPOSAL']):add('s03-04',dict(kind='chip',x=54+14*j,y=20,w=13.5,h=5,text=caption,size=10.5,font='Michroma',weight=400,fill='transparent',color='#fff',border='1px solid #777',radius=0),'원문 실제 outlined3cell chip 중앙정렬')
line('s03-04',0,42,50,42);line('s03-04',0,53,50,53)
up('s03-04',18,'원문 별2개로 교체',w=0,h=0)
up('s03-04',19,'원문 URL 아닌 View More badge',text='')
star('s03-04',6,82);star('s03-04',9.2,82)
add('s03-04',dict(kind='chip',x=11,y=83,w=8,h=5,text='View More',size=10.5,font='DM Sans',weight=400,color='#fff',fill='transparent',radius=30,border='1px solid #777'),'원문 outlined View More pill')
txt('s03-04','DESIGN PRESENTATION\nAND CREATIVE DIRECTION',5,71,18,9.5,align='center',h=6)
up('s03-05',10,'원문 uppercase4행 body',text='THERE ARE MANY VARIATIONS OF PASSAGES\nOF LOREM IPSUM AVAILABLE, BUT THE\nMAJORITY HAVE SUFFERED ALTERATION IN\nSOME FORM, BY INJECTED HUMOUR.',size=13.5,h=12,x=67)
up('s03-05',12,'원문 Valerie handwritten ink폭 약24% 작게·y74%',size=26.5,y=74,h=7)
for j in range(4):
 add('s03-05',dict(kind='box',x=57,y=53+j*5,w=2.1,h=3.73,fill='transparent',border='1px solid #888',radius='50%'),'원문 brandicon outlinecircle 실제 단순 도형')
 add('s03-05',dict(kind='image',x=57.55,y=54+j*5,w=1,h=1.78,text='브랜드 bitmap icon placeholder'),'이미지 브랜드 아이콘만 회색')
# cropped decorative outline CEO/FOUNDER remains actual DOM stroke, clipped to the visible edge.
txt('s03-05','CEO/FOUNDER',64,53,67,41,font='Michroma',h=8,color='transparent',rotate=-90,textStroke='1px #666')
for i,y in [(1,32),(2,54),(3,75)]:
 if es('s03-06')[i]['kind']=='path':up('s03-06',i,'원문 alternating team row separators',points=[dict(x=57,y=y),dict(x=100,y=y)])
for i,y in [(5,12),(6,34),(7,56),(8,78)]:up('s03-06',i,'원문 circleportrait envelope',y=y,w=9.3,h=16.5)
for i,text,y,x,align in [(20,'Sydney Clowney\nCreative Director',15,84,'left'),(23,'Dora Cincora\nCindy',37,57,'right'),(26,'Juliana Hermola\nDesigner',59,84,'left'),(29,'Margaret McCloud\nCamino',81,57,'right')]:up('s03-06',i,'원문 geometric2행 이름, 흐린 이름은 정상 대체 기록',text=text,font='Michroma',size=11,y=y,x=x,w=16 if align=='right'else 15,h=6,align=align)
for i in [22,25,28,31]:up('s03-06',i,'원문 2행 설명 밀도',y=es('s03-06')[i]['y']+1,size=10.5)
up('s03-06',16,'원문 left body y72%',y=72)
up('s03-06',32,'원문 View More badge 독립 구현',text='')
star('s03-06',42,85);star('s03-06',45.2,85)
add('s03-06',dict(kind='chip',x=41,y=91,w=8,h=5,text='View More',size=10.5,font='DM Sans',weight=400,color='#fff',fill='transparent',radius=30,border='1px solid #777'),'원문 outlined ViewMore pill')
for i,y in [(9,26),(11,47),(13,74)]:up('s03-07',i,'원문 section title y 및 굵기600',y=y,weight=600)
up('s03-07',10,'원문 Profile4행 body',text='Create a thoughtful and consistent presentation\nthat supports the team and its projects. Plan\nwith clear principles, develop each idea, and\ncommunicate the work with care.',h=12,y=33,size=13)
up('s03-07',12,'원문 EmploymentHistory4행 bullets',text='•  Developed new presentation systems\n•  Supported daily creative communication\n•  Coordinated project planning and delivery\n•  Worked with teams to meet shared goals',h=12,y=59,size=13)
up('s03-07',14,'원문 Education2행 bullets',text='•  Studied communication and visual design\n•  Completed a collaborative creative project',h=7,y=86,size=13)
up('s03-07',15,'원문 employment metadata y',y=52,size=14)
up('s03-07',16,'원문 education metadata y',y=78,size=14)
up('s03-07',2,'원문 photo height native약344',h=47.8)
up('s03-08',0,'원문 brown background width39%',w=39)
up('s03-08',14,'원문 quote 본문3행+3bullets',text='There are many variations of passages of\nLorem Ipsum available, but the majority\nhave suffered alteration in some form.\n\n•  Creative direction and design\n•  Clear brand communication\n•  Thoughtful presentation systems',size=11.8,h=19,lineHeight=1.13)
up('s03-08',16,'원문4.40% 실제 ink폭 약12% 더 큰 native size',size=54.5,h=11)
up('s03-08',17,'원문 lower quote uppercase2행',text='THERE ARE MANY VARIATIONS OF\nPASSAGES OF LOREM IPSUM AVAILABLE.',size=11.5,h=7)
for i in [12,13,14]:
 pass
line('s03-09',0,43,100,43)
for e in es('s03-09'):
 if e.get('text','').startswith(('HOW WE WORK','PROJECT NAME','DATE')) and e.get('size',0)>20:e['size']=19
 if e.get('text','').startswith('THERE ARE MANY VARIATIONS') and e.get('x')==4:e['y']=72
 if e.get('text')=='Virginia Kelly':e['y']=90
for s in ['s06-01','s06-02','s08-01']:
 original=copy.deepcopy(es(s)[3]);up(s,3,'원문 Design/Portfolio는 서로 다른 실제 크기의 독립2줄',text='Design',size=81.5,lineHeight=1,h=17,y=31)
 txt(s,'Portfolio',42,39,57,124,font='Michroma',h=23,color=original['color'])
 up(s,9,'원문 cursive Template 원문밑행 y50%',y=50,x=71)
 up(s,10,'원문 Mary Christine bold caption',weight=600,size=18)
 up(s,11,'원문 DesignPortfolio bold footer',weight=700,size=16)
 up(s,12,'원문 quote bold',weight=600)
 up(s,14,'원문 footeruppercase5행 prose',text='ON THE OTHER HAND WE GO\nWITH THE RIGHTEOUS AND\nTHOUGHTFUL IDEAS FOR DAILY\nDESIGN AND COMMUNICATION\nBY THE CREATIVE PROJECT.',size=11.5,h=13,lineHeight=1.05)
 for i in [15,16,17]:
  old=copy.deepcopy(es(s)[i]);es(s)[i]=dict(kind='image',x=old['x']+.4,y=old['y']+.7,w=1.2,h=2.13,text='Bitmap socialmedia icon placeholder');add(s,dict(kind='box',x=old['x'],y=old['y'],w=old['w'],h=old['h'],fill='transparent',border='1px solid '+original['color'],radius='50%'),'원문 소셜 브랜드 icon만 gray, outline circle실제')
 line(s,40,82,40,89,color=original['color'])
 up(s,2,'원문 원형 사진 envelope',x=5,y=20,w=30,h=60)
for i,dy in [(9,-3),(10,-7),(11,-5)]:up('s06-03',i,'원문 left stack 개별 source y',y=es('s06-03')[i]['y']+dy)
up('s06-03',12,'원문 이름captionbold tracking2.5',weight=600,size=29,letterSpacing=2.5)
up('s06-03',13,'원문 CEO wide smallcaps',letterSpacing=3)
up('s06-04',8,'원문 DesignPortfolio subhead ink폭 약27% 복원',size=28.8)
up('s06-04',10,'원문 uppercase4행 문단',text='THERE ARE MANY VARIATIONS OF PASSAGES OF LOREM IPSUM AVAILABLE,\nBUT THE MAJORITY HAVE SUFFERED ALTERATION IN SOME FORM, BY\nINJECTED HUMOUR OR RANDOM WORDS WHICH DO NOT LOOK EVEN\nSLIGHTLY BELIEVABLE. IF YOU ARE GOING TO USE A PASSAGE.',size=11.5,h=12,y=48)
for i,y in [(11,61),(12,74)]:up('s06-04',i,'원문 uppercase3행 문단',text='THERE ARE MANY VARIATIONS OF PASSAGES OF LOREM IPSUM AVAILABLE,\nBUT THE MAJORITY HAVE SUFFERED ALTERATION IN SOME FORM, BY\nINJECTED HUMOUR OR RANDOM WORDS.',size=11.5,h=9,y=y)
up('s06-04',1,'원문 oval image 실제 envelope',x=7.8,w=25.8)
for i in range(8,18):up('s06-05',i,'원문 목록 실제 row pitch27px와 bold',weight=600,y=57+(i-8)*3.75)
up('s06-06',1,'원문 portrait photo 오른쪽 경계72%',w=27)
up('s06-06',10,'원문 작은 이름caption bold',size=21,weight=700)
up('s06-06',11,'원문 Signature label y81%',y=81)
up('s06-06',14,'원문 signature actualink폭 source163display',size=39,h=9)
txt('s06-06','CONSISTENT IDEAS AND CLEAR DESIGN\nBUILD THOUGHTFUL COMMUNICATION.',4,77,35,11.5,h=6)
txt('s06-06','CREATIVE DIRECTION AND DESIGN\nPRESENTATION PORTFOLIO',4,91,29,9,h=5)
# source long thin arrow, rather than stretched Lucide arrow icon.
up('s06-06',18,'원문 세로 단순 linearrow SVG 실제선',w=0,h=0);add('s06-06',dict(kind='path',x=0,y=0,w=100,h=100,points=[dict(x=78.8,y=56),dict(x=78.8,y=76)],color='#ddd',strokeWidth=.7,arrow=True,closed=False,fill=None),'원문 긴 arrow stem restored')
for i,dy in [(8,-3),(9,-7),(10,-5)]:up('s06-07',i,'원문 left stack 개별 y',y=es('s06-07')[i]['y']+dy)
up('s06-07',11,'원문 lower right subtitle y62%',y=62)
up('s06-08',12,'원문 right uppercase5행 paragraph density',text='THERE ARE MANY VARIATIONS OF PASSAGES OF LOREM\nIPSUM AVAILABLE, BUT THE MAJORITY HAVE SUFFERED\nALTERATION IN SOME FORM, BY INJECTED HUMOUR OR\nRANDOM WORDS WHICH DO NOT LOOK EVEN SLIGHTLY\nBELIEVABLE. IF YOU ARE GOING TO USE A PASSAGE.',size=11.5,h=13,y=64)
up('s06-08',13,'원문6bullets smallerfont',text='•  Our presentation and design concepts\n•  Creative portfolio and proposals\n•  Graphic and communication systems\n•  Clear visual direction and typography\n•  Thoughtful concepts for the team\n•  Consistent project development',size=11.5,h=15,y=79,lineHeight=1.12)
up('s06-08',15,'원문 left lower quote uppercase3행/right',text='THERE ARE MANY VARIATIONS OF\nPASSAGES OF LOREM IPSUM AVAILABLE,\nBUT THE MAJORITY.',size=11,align='right',h=7)
up('s06-09',10,'원문 left paragraph y70%',y=70)
up('s06-09',11,'원문 signature y83%',y=83)
for i,n in [(13,4),(15,4),(17,2),(19,4)]:
 prose='THERE ARE MANY VARIATIONS\nOF LOREM IPSUM AVAILABLE,\nBUT THE MAJORITY HAVE\nSUFFERED IN SOME FORM.' if n==4 else 'THERE ARE MANY VARIATIONS\nOF LOREM IPSUM AVAILABLE.'
 up('s06-09',i,'원문 right uppercase행수4/4/2/4 복원',text=prose,size=11.5,h=10,lineHeight=1.1)
# one known genuine italic preserved using actual loaded DM Sans italic, avoiding synthetic Poppins.
k='p069/s02-06';e=d[k]['elements'][1];before=copy.deepcopy(e);e.update(font='DM Sans',size=77.4,lineHeight=1.1,h=49);q['pages'][k]['changes'].append({'before':before,'after':copy.deepcopy(e),'reason':'원문 실제 italic은 actual loaded DM Sans italic 사용, Poppins normal-only synthetic 감사 실패 해결. original quote inkwidth 약694px 대응'})
for path,data in [(P,d),('review/quality/group-b.json',q)]:
 with open(path+'.tmp','w')as f:json.dump(data,f,ensure_ascii=False,indent=2)
 os.replace(path+'.tmp',path)
print('p080 modified28; p069 actual italic1')
