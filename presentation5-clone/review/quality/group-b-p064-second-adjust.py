import json,copy
p='src/decks/group-b-data.json';d=json.load(open(p));q=json.load(open('review/quality/group-b.json'))
def patch(k,e,reason,**kw):
 old=copy.deepcopy(e);e.update(kw);q['pages'][k]['changes'].append({'before':old,'after':copy.deepcopy(e),'reason':reason})
def text(k,t):return next(e for e in d[k]['elements']if e.get('text')==t)
k='p064/s04-01';patch(k,text(k,'Learn More'),'원문 실제 button 폭11.5%',w=11.5)
d[k]['elements'].extend([{'kind':'text','text':'Explore new ideas and opportunities.','font':'DM Sans','size':16,'weight':400,'color':'#a269c6','x':65,'y':29,'w':30,'h':4,'lineHeight':1.15},{'kind':'box','fill':'#a269c6','radius':'50%','x':63,'y':29.8,'w':.8,'h':1.42}]);q['pages'][k]['changes'].append({'reason':'실제 원문 오른쪽 bullet caption 누락 복원, 판독 불가 정상문구'})
k='p064/s04-02';patch(k,text(k,'Effective Marketing\nand Customer\nEngagement'),'원문 흰 headline은 700보다 얇은 굵기600, 같은 관측 폭',weight=600,size=52.3)
k='p064/s04-04';b=[e for e in d[k]['elements']if e.get('font')=='DM Sans' and e.get('size')==14]
for j,e in enumerate(b):patch(k,e,'원문 step 설명은 짧은 3줄 폭과 dashed connector',text='Lorem ipsum dolor sit\namet, consectetur\nadipiscing elit.',w=15,x=45+9*j)
for j in range(3):
 d[k]['elements'].extend([{'kind':'path','x':0,'y':0,'w':100,'h':100,'points':[{'x':39+10*j,'y':22+20*j},{'x':43+10*j,'y':22+20*j}],'color':'#b5a6c4','strokeWidth':1,'dashed':True,'closed':False},{'kind':'box','x':42.5+10*j,'y':21.6+20*j,'w':.5,'h':.89,'fill':'#aa7fb9','radius':'50%'}])
q['pages'][k]['changes'].append({'reason':'원문 리본과 설명 사이 점선 및 endpoint 3개 복원'})
k='p064/s04-05'
for e in d[k]['elements']:
 if e['kind'] in ['box','icon'] and e.get('y',0)>40:e['y']-=3 if e.get('x',0)<75 else -1
patch(k,text(k,'Your Step One'),'원문 첫 단계 caption y70%가 아닌 y76% 오류 정정',y=69)
# following paragraph directly after first caption
ix=d[k]['elements'].index(text(k,'Your Step One'));patch(k,d[k]['elements'][ix+1],'원문 첫 단계 본문 y74%',y=74)
patch(k,text(k,'Your Step Two'),'원문 두번째 caption y51%',y=51)
ix=d[k]['elements'].index(text(k,'Your Step Two'));patch(k,d[k]['elements'][ix+1],'원문 두번째 본문 y56%',y=56)
for x,y,c in [(28,74,'#7365ef'),(45,56,'#bc61ce'),(62,38,'#f4b900'),(79,21,'#303030')]:d[k]['elements'].append({'kind':'box','x':x,'y':y,'w':1,'h':1.78,'fill':c,'radius':'50%'})
q['pages'][k]['changes'].append({'reason':'원문 caption 옆 단순 원 bullet 복원 및 실제 contiguous step 높이'})
k='p064/s04-07'
for i,e in enumerate(d[k]['elements']):
 if e['kind']=='box' and e.get('radius')=='50%':
  n=round((e['x']-23)/17);delta=2+2.6*n;patch(k,e,'원문 원형 단계 4개의 실제 중심 y79/67.6/56.2/44.8%',y=74-11.4*n)
  icon=d[k]['elements'][i+1];patch(k,icon,'원형 단계 아이콘 중심 함께 이동',y=icon['y']+delta)
for n,t in enumerate(['Step One','Step Two','Step Three','Step Four']):
 e=text(k,t);patch(k,e,'원문 실제 단계 caption 피치11.4%',y=59.5-11.4*n)
 i=d[k]['elements'].index(e);patch(k,d[k]['elements'][i+1],'원문 실제 단계 본문 피치11.4%',y=64.5-11.4*n)
# observed footer source number transcription
for n,folio in [(1,'3'),(2,'9'),(3,'20'),(4,'11'),(6,'12'),(7,'23'),(8,'24'),(9,'25')]:
 k=f'p064/s04-{n:02}';e=next((e for e in d[k]['elements']if e['kind']=='text'and e.get('x')==95 and e.get('y')==94),None)
 if e is None:
  e={'kind':'text','x':95,'y':94,'w':3,'h':4,'text':folio,'font':'DM Sans','size':14,'weight':400,'color':'#888'};d[k]['elements'].append(e)
 patch(k,e,'원문 판독 가능한 footer folio',text=folio)
for n in [1,2,3,4,6,7,8,9]:
 k=f'p064/s04-{n:02}';d[k]['elements'].append({'kind':'box','x':94,'y':99,'w':3,'h':.6,'fill':'#a269c6'})
for n in [4,5]:
 k=f'p064/s04-{n:02}';d[k]['elements'].insert(0,{'kind':'graphic','graphic':'b-gradient-panel','colors':['#fff','#f0f0f0'],'x':0,'y':0,'w':100,'h':100});q['pages'][k]['changes'].append({'reason':'단순 흰색-회색 graphic background SVG gradient 실제 복원'})
json.dump(d,open(p+'.b.tmp','w'),ensure_ascii=False,indent=2);__import__('os').replace(p+'.b.tmp',p);json.dump(q,open('review/quality/group-b.json','w'),ensure_ascii=False,indent=2)
p='src/graphics/group-b.tsx';s=open(p).read().replace('y=82-i*12-(i===3?4:0)','y=79-i*12').replace('y=92-i*14','y=89-i*11.4').replace('M1062 353V305H1270','M1062 394V305H1270');open(p,'w').write(s)
