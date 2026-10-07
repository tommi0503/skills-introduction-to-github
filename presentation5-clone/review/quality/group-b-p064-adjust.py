import json,copy
p='src/decks/group-b-data.json';d=json.load(open(p));q=json.load(open('review/quality/group-b.json'))
def update(sid,i,reason,**kw):
 k='p064/'+sid;e=d[k]['elements'][i];old=copy.deepcopy(e);e.update(kw);q['pages'][k]['changes'].append({'element':i,'before':old,'after':copy.deepcopy(e),'reason':reason})
def replace(sid,remove,scene,reason):
 k='p064/'+sid;es=d[k]['elements'];old=[es[i] for i in remove];g={'kind':'graphic','graphic':scene,'x':0,'y':0,'w':100,'h':100};d[k]['elements']=[g]+[e for i,e in enumerate(es) if i not in remove];q['pages'][k]['changes'].append({'removedElements':old,'addedGraphic':g,'reason':reason})
titles=[('s04-01',3,51,7,15.8,1.12),('s04-02',3,51,51.7,17,1.29),('s04-03',17,46.3,14.8,11.9,1.12),('s04-04',13,47,70.5,12,1.24),('s04-05',0,45,7,15.3,1.21),('s04-06',4,46,7,48.3,1.2),('s04-07',15,46.2,7.5,15.8,1.27),('s04-08',6,45,10,28.7,1.22),('s04-09',1,92,12.8,47.8,1.14)]
metrics=json.load(open('review/quality/group-b-title-metrics.json'))
for sid,i,size,x,y,lh in titles:
 update(sid,i,'原본 굵은 grotesk 글폭/잉크높이와 대조: 실제 로드 Montserrat 700, 제목 행 피치/왼쪽 위치 개별 조정',font='Montserrat',weight=700,size=size,x=x,y=y,lineHeight=lh,h=(len(d['p064/'+sid]['elements'][i]['text'].split('\n'))*size*lh+12)/7.2)
 q['pages']['p064/'+sid]['measurements'].append({'region':'mainTitle','inkBands1280':metrics[sid],'candidateFont':'Montserrat 700','canvasMeasuredAt50px':True})
update('s04-01',5,'원문 왼쪽 본문 실제 3줄 폭 약225px에 맞춤',size=18,w=27,text='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit. Sed\neiusmod tempor incididunt.',h=11,lineHeight=1.3)
update('s04-01',8,'원문 pill 옅은 윤곽 복원',borderColor='#e9e1ec',borderWidth=1)
# panel at original region, not full-page
e=d['p064/s04-02']['elements'][1];old=copy.deepcopy(e);e.clear();e.update(kind='graphic',graphic='b-gradient-panel',x=47,y=0,w=53,h=52);q['pages']['p064/s04-02']['changes'].append({'element':1,'before':old,'after':copy.deepcopy(e),'reason':'원문 보라-분홍 대각 그라데이션 직접 SVG 복원'})
for i in [19,21,23,25]:update('s04-03',i,'원문 각 단계 설명 두 줄 밀도 복원: 판독 불가 정상문구',text='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.',size=15.5,lineHeight=1.3,h=7)
for i in [0,4,8,12]:
 e=d['p064/s04-03']['elements'][i];old=copy.deepcopy(e);e.update(kind='graphic',graphic='b-medallion',colors=[e.pop('fill')]);e.pop('radius');q['pages']['p064/s04-03']['changes'].append({'element':i,'before':old,'after':copy.deepcopy(e),'reason':'원문 입체 원형 배지의 명암·테두리·그림자 SVG 복원'})
replace('s04-04',[1,2,4,6,8,10,11,12],'b-ribbon-four','원문 리본 접힘/후면색/검정 화살표 끝단 및 명암 SVG 복원')
# staircase captions must be before replacement preserving original indices
for title,body,x,y in [(7,8,9,76),(14,15,26,53),(21,22,43,35),(28,29,60,17)]:
 update('s04-05',title,'원문 단계 설명은 각 계단 왼쪽 위 오른쪽 정렬',x=x,y=y,w=17,align='right',size=18,weight=600)
 update('s04-05',body,'원문 설명 각 2줄, 단계별 원래 계단 위치와 맞춤',x=x,y=y+5,w=17,align='right',size=13.5,text='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.',h=6,lineHeight=1.3)
for i in [26,27]:update('s04-05',i,'원문 마지막 계단 상승 위치 y 약4% 복원',y=d['p064/s04-05']['elements'][i]['y']-4)
replace('s04-05',[2,3,4,9,10,11,16,17,18,23,24,25,30],'b-isometric-stairs','원문 4개 단순 입체 계단 위/옆/앞면 명암과 끝 화살표 SVG 구현')
for i in [10,15,20]:update('s04-06',i,'원문 card 제목 굵기',weight=600)
for i in [11,16,21]:update('s04-06',i,'원문 설명은 두 줄',text='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.',size=13,lineHeight=1.25,h=6)
for i in [7,12,17]:update('s04-06',i,'원문 흰 카드 입체 그림자',shadow='0 4px 14px #00000012')
for i in [23,25]:update('s04-06',i,'원문 왼쪽 bullet 실제 작은 글씨 크기 복원',size=16,h=4)
replace('s04-06',[0,1,2],'b-elbow-trail','원문 직각 둥근 접힘 리본 경로 SVG 복원. 이전 곡선 S 형태 오류 제거')
for i,y in [(16,59),(18,46),(20,34),(22,25)]:update('s04-07',i,'원문 단계명 위치·굵기 개별 복원',y=y,weight=600)
for i,y in [(17,64),(19,51),(21,39),(23,30)]:update('s04-07',i,'원문 단계 본문 두 줄 위치 복원',y=y)
replace('s04-07',[2,5,8,11,26],'b-step-ribbon','원문 계단형 얇은 3D 접힌 리본 복원. 단순12px 선 대체')
update('s04-08',1,'원문 흰 제목 카드 약31% 폭',x=8,w=31,h=32)
for i in [7,10,13]:
 e=d['p064/s04-08']['elements'][i];update('s04-08',i,'숫자의 실제 칩 중심 정렬',kind='chip',y=65,h=9,fill='transparent',lineHeight=1,weight=500)
for i in [2,3,4]:
 e=d['p064/s04-08']['elements'][i];update('s04-08',i,'원문 보라 배지 그라데이션',kind='graphic',graphic='b-gradient-panel',colors=['#7664e7','#bc63d3']);e.pop('fill',None);e.pop('radius',None)
for i in [9,12,15]:update('s04-08',i,'원문 본문 2줄 밀도 복원',text='Lorem ipsum dolor sit amet, consectetur\nadipiscing elit. Sed do eiusmod tempor.',size=16.5,lineHeight=1.3,h=7)
update('s04-09',2,'원문 오른쪽 본문 2줄 복원',text='Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nSed do eiusmod tempor incididunt ut labore et dolore.',size=17,w=35,x=61,y=18,h=7,lineHeight=1.3)
k='p064/s04-09';d[k]['elements'].insert(0,{'kind':'graphic','graphic':'b-faint-fold','x':0,'y':0,'w':100,'h':100});q['pages'][k]['changes'].append({'reason':'원문 연한 회색 접힌 리본 배경은 단순 벡터로 복원','graphic':'b-faint-fold'})
d[k]['elements'].append({'kind':'text','text':'Discover the path to your creative success.','font':'DM Sans','weight':400,'size':17,'color':'#444','x':63,'y':28,'w':34,'h':4,'lineHeight':1.15});d[k]['elements'].append({'kind':'box','x':61,'y':28.8,'w':.8,'h':1.42,'radius':'50%','fill':'#8f67c5'});q['pages'][k]['changes'].append({'reason':'원문 오른쪽 작은 보라 bullet caption 누락 복원. 판독 불가 정상 문장 대체'})
for k,v in d.items():
 if k.startswith('p064'):
  for e in v['elements']:
   if e['kind']=='image':q['pages'][k]['remaining'].append({'placeholder':'photograph of a person / realistic work meeting','reason':'사진·인물은 사용자 지시대로 회색 유지','region':[e['x'],e['y'],e['w'],e['h']]})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2);json.dump(q,open('review/quality/group-b.json','w'),ensure_ascii=False,indent=2)
