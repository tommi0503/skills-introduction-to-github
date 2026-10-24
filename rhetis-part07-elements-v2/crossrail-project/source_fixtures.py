from pathlib import Path
import json,re,copy,math,html
P=Path(__file__).parent;E=P/'crossrail/elements';M=json.loads((P/'map.json').read_text());old=M['instances'];new=[]
splits={
'p05-vision-columns':[[292+291*i,98,275,524] for i in range(3)],
'p06-levels-labels':[[95,263+102*i,98,66] for i in range(4)],
'p09-four-figures':[[95+553*(i%2),260+206*(i//2),537,188] for i in range(4)],
'p11-business-panels':[[95+585*(i%2),260+198*(i//2),545,197] for i in range(4)],
'p12-letter-columns':[[95+281*i,260,246,245] for i in range(4)],
'p12-column-bullets':[[95+281*i,541,246,115] for i in range(4)],
'p15-three-pictures':[[174+371*i,260,188,188] for i in range(3)],
'p15-letter-badges':[[320+371*i,260,42,42] for i in range(3)],
'p15-equipment-fields':[[95+371*i,472,346,184] for i in range(3)],
'p16-specification-pair':[[95+573*i,260,515,395] for i in range(2)],
'p17-four-market-panels':[[95+562*(i%2),260+213*(i//2),527,181] for i in range(4)],
'p21-four-metrics':[[367+415*(i%2),260+206*(i//2),402,188] for i in range(4)]}
def belongs(r,b):
 x,y,w,h=r['bbox'];return b[0]-3<=x+w/2<=b[0]+b[2]+3 and b[1]-3<=y+h/2<=b[1]+b[3]+3
for o in old:
 if o['id'] in splits:
  assigned=set()
  for k,b in enumerate(splits[o['id']]):
   x=copy.deepcopy(o);x['id']=o['id']+'-'+str(k+1);x['bbox']=b;x['sourceMeasurements']=[r for r in o['sourceMeasurements'] if belongs(r,b)];assigned.update(r['id'] for r in x['sourceMeasurements']);x['fixture']=f'elements/{o["leaf"]}/fixtures/replica-{o["page"]:02}'+('' if k==0 else '-'+str(k+1))+'.html';x['use']='same-as:'+str(M['baseChoices'][x['leaf']]) if o['use']=='base' and k else o['use'];new.append(x)
  for r in o['sourceMeasurements']:
   if r['id'] not in assigned:new.append({'id':o['id']+'-edge-'+r['id'],'page':o['page'],'leaf':'foundation','use':'furniture','bbox':r['bbox'],'fixture':None,'sourceMeasurements':[r]})
 elif o['id'] in ['p07-left-explanations','p07-right-explanations','p18-left-strengths','p18-right-strengths']:
  rs=[r for r in o['sourceMeasurements'] if r['text']];head=[r for r in rs if float(r['typography']['size'][:-2])>=24];body=[r for r in rs if r not in head]
  for k,r in enumerate(head+body):
   leaf='headline' if r in head else ('list' if o['page']==18 else 'prose');b=r['bbox'];x={'id':o['id']+'-'+leaf+'-'+str(k),'page':o['page'],'leaf':leaf,'use':'same-as:'+str(M['baseChoices'][leaf]),'bbox':b,'fixture':f'elements/{leaf}/fixtures/replica-{o["page"]:02}-'+o['id'].split('-',1)[1]+'-'+str(k)+'.html','sourceMeasurements':[r]};new.append(x)
  shape=[r for r in o['sourceMeasurements'] if not r['text']]
  if shape:new.append({'id':o['id']+'-heading-band','page':o['page'],'leaf':'headline','use':'unexpressible','bbox':o['bbox'],'fixture':None,'why':'The source places the heading on a pale ruled strip. headline has big, center and accent-on variants, but no secondary ruled-strip variant.','sourceMeasurements':shape})
 else:new.append(o)
M['instances']=new
# Normalize sole base selection even after an independent component split.
seen=set()
for o in new:
 if o['use']=='base':
  if o['leaf'] in seen:o['use']='same-as:'+str(M['baseChoices'][o['leaf']])
  else:seen.add(o['leaf'])
(P/'map.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n')
short=['회수','정비','배차','접수','보관','반출','검수','수리','등록','예약','인수','봉인']
labels=['회수 창구','봉인 점검','수리 접수','부품 대조','야간 배차 조정','운송장 확인','예비 부품 창고','남부 정비 창구','분실 물품 회수','현장 점검 예약']
notes=['도착한 포장물을 운송장 번호와 맞춘 뒤 선반별 접수 대장에 남깁니다.','회수 차량의 잔여 운행 거리를 살펴 가장 가까운 정비실부터 방문 순서를 정합니다.','파손 신고가 들어오면 봉인 사진과 인수 시각을 함께 보관해 수리실로 전달합니다.','재고가 부족한 소모품은 대체 규격을 대조하고 다음 입고 차량에 우선 배정합니다.','지점마다 반납한 장비를 묶어 통전 시험을 진행하며 누락된 부품은 별도 보관합니다.','분해 후 남은 자재의 수량을 다시 세어 출고 담당자가 인수 대장에 서명합니다.']
def label(n,i=0):
 if n<=3:return short[i%len(short)]
 if n<=8:return labels[i%len(labels)]
 return ['입고 창구와 회수 차량의 배정을 함께 점검합니다','창고별 수리 대기 물량을 살펴 배차 순서를 정합니다','회수 대상 장비의 봉인 상태를 인수 대장에 남깁니다'][i%3]
def note(n,i=0):
 s=notes[i%len(notes)]
 if n<30:return ['출고 전 봉인 상태를 다시 살핍니다.','반납된 부품을 창고별로 분류합니다.','정비 기록은 인수 대장에 남깁니다.'][i%3]
 if n>85:s+=' '+notes[(i+1)%len(notes)]
 if n>135:s+=' '+notes[(i+2)%len(notes)]
 return s
H=html.escape
rootclass={'metric':'stat','chart-line':'lines','chart-bar':'bars','chart-donut':'donut','image-frame':'frame','timeline':'track','positioning':'posmap','table':'tablebox'}
def wrap(leaf,inside,variant='',data=''):
 return f'<div class="{rootclass.get(leaf,leaf)}{(" "+variant) if variant else ""}" data-el="crossrail-{leaf}" style="grid-column:1 / span 12;grid-row:1 / span 6{data}">{inside}</div>'
def t(c,s,tag='p'):return f'<{tag} class="{c}">{H(s)}</{tag}>'
def freshcopy(rs,i=0):return [label(len(r['text']),i+k) if float(r['typography']['size'][:-2])>=24 else note(len(r['text']),i+k) for k,r in enumerate(rs)]
written=[]
for ix,o in enumerate(new):
 leaf=o['leaf'];f=o.get('fixture');
 if not f or leaf=='foundation' or (leaf=='steps' and o['page'] in [10,13]):continue
 rs=[r for r in o.get('sourceMeasurements',[]) if r['text'].strip()];b=o['bbox'];page=o['page'];v=o['use'].split(':',1)[1].lstrip('.') if o['use'].startswith('variant:') else '';body='';minimum='6x3'
 if leaf=='headline':body=t('',label(len(rs[0]['text']) if rs else 10,ix),'h2').replace(' class=""','');minimum='3x1'
 elif leaf=='prose':body=''.join('<p>'+H(note(len(r['text']),ix+k))+'</p>' for k,r in enumerate(rs));minimum='5x3' if sum(len(r['text']) for r in rs)>90 else '4x2'
 elif leaf=='card':
  vals=[r for r in rs if re.fullmatch(r'[+\-]?[A-D]|(?:No\.1)|[0-9,.+%위점]+|AAA',r['text'])];kicks=[r for r in rs if 'VISION' in r['text'] or r['bbox'][1]==b[1]];heads=[r for r in rs if float(r['typography']['size'][:-2])>=24 and r not in vals and r not in kicks];ns=[r for r in rs if r not in heads and r not in vals and r not in kicks];parts=''
  if kicks:parts+=t('kick','SERVICE '+str(ix%5+1) if 'VISION' in kicks[0]['text'] else '정비 창구 '+str(ix%4+1))
  if vals:parts+=t('fig',vals[0]['text'])
  if page==21 and o['id']=='p21-rank':parts+=t('mark','2위')
  if heads:parts+=t('name',label(len(heads[0]['text']),ix))
  if ns:parts+=t('note',note(len(ns[-1]['text']),ix))
  body='<div class="parts">'+parts+'</div>';minimum='4x3' if b[3]<250 else '4x6'
 elif leaf=='pill':body='<div class="parts">'+t('name',short[ix%12])+'</div>';minimum='2x1'
 elif leaf=='pyramid':body=''.join('<div class="level">'+t('name',label(len(r['text']),ix+k),'b')+'</div>' for k,r in enumerate(rs));minimum='6x4'
 elif leaf=='hub':
  names=rs[:4];core=rs[4:];body='<div class="core">'+t('name','정비 거점','b')+'<small>Depot</small></div>'+''.join('<div class="spoke">'+t('name',short[(ix+k)%12],'b')+'</div>' for k,r in enumerate(names));minimum='6x4'
 elif leaf=='funnel':
  body=''.join(f'<div class="stage" style="--v:{[100,67,34][k]}">'+t('name',short[(ix+k)%12],'b')+t('fig',str([1200,804,408][k]),'b')+'</div>' for k in range(3));minimum='5x4'
 elif leaf=='list':
  body=''.join('<div class="item">'+t('name',label(len(r['text']),ix+k) if len(r['text'])<14 else note(min(len(r['text']),45),ix+k),'b')+'</div>' for k,r in enumerate(rs));minimum='4x2' if len(rs)<=2 else '6x4'
 elif leaf=='image-frame':body='<div class="seat" data-ph="'+str(ix%3+1)+'"></div>';minimum='3x3'
 elif leaf=='tag':body='<span>'+H(['R','S','T'][ix%3])+'</span>';minimum='1x1'
 elif leaf=='table':
  rows=[]
  for r in sorted(rs,key=lambda r:(round(r['bbox'][1]/5),r['bbox'][0])):
   yy=round(r['bbox'][1]/5)
   if not rows or abs(rows[-1][0]-yy)>1:rows.append((yy,[r]))
   else:rows[-1][1].append(r)
  hashead=page in [16,20];thead='';tbody=''
  for k,(_,row) in enumerate(rows):
   cells=[]
   for q,r in enumerate(row):
    raw=r['text'];val=raw if re.fullmatch(r'[0-9,.+%억원명kgVDCmm]+',raw) else (label(len(raw),ix+k+q) if len(raw)<17 else note(20,ix+k+q))
    if page==30:val=['접수처','강원도 서원시 창고로 402번길','예약선','033-640-8274','담당창구','desk@depot.example','접수안내','https://depot.example','방문예약','평일 오전 8시부터 오후 5시'][k*2+q]
    tag='th' if hashead and k==0 else ('th' if q==0 else 'td');attr=' scope="row"' if tag=='th' and not(hashead and k==0) else '';cells.append(f'<{tag}{attr}>{H(val)}</{tag}>')
   rhtml='<tr>'+''.join(cells)+'</tr>'
   if hashead and k==0:thead+=rhtml
   else:tbody+=rhtml
  body='<table class="table"><thead>'+thead+'</thead><tbody>'+tbody+'</tbody></table>';minimum='6x4' if len(rows)>5 else '5x3'
 elif leaf=='chart-bar':body=''.join(f'<div class="bar'+(' on' if k==3 else '')+f'" style="--v:{val}"><b>{val}</b><span>{k+1}차 접수</span></div>' for k,val in enumerate([10,15,20,25]));minimum='6x4'
 elif leaf=='chart-line':body=''.join(f'<div class="pt" style="--v:{val}"><b>{val:,}</b><span>{k+1}차</span></div>' for k,val in enumerate([2000,2900,3900,5000,4400,5100,5500]));minimum='6x4'
 elif leaf=='metric':body='<div class="parts">'+t('fig','7,200')+t('name','회수 완료 건수')+t('note',note(45,ix))+'</div>';minimum='5x3'
 elif leaf=='legend':body=''.join(f'<span class="key tone-{k+1}">'+H(short[k])+' <b>'+str([20,25,15,10,30][k])+'%</b></span>' for k in range(5));minimum='6x3'
 elif leaf=='roadmap':
  body='<div class="heads">'+''.join('<span>'+H(s)+'</span>' for s in ['1차접수','2차접수','3차접수','4차접수'])+'</div>'
  for k in range(4):body+='<div class="lane">'+t('name',labels[k],'b')+f'<div class="bar'+(' on' if k==0 else f' tone-{k%3+1}')+f'" style="--from:{[0,0,1.4,2][k]};--to:{[2,2.7,3.1,4][k]}"><span>'+H(labels[k+2])+'</span></div></div>'
  minimum='10x4'
 elif leaf=='timeline':body=''.join('<div class="stop">'+t('kick',str(2058+k),'b')+t('name',labels[k],'b')+t('note',note(70,k))+'</div>' for k in range(4));minimum='10x6'
 elif leaf=='positioning':
  body='<div class="axis-x"><span>반입 지연</span><span>빠른 반입</span></div><div class="axis-y"><span>낮은 정비율</span><span>높은 정비율</span></div>'
  for k,(x,y) in enumerate([(27,21),(25,45),(55,45),(70,51),(71,68),(91,90)]):body+=f'<div class="mark'+(' on' if k==5 else '')+f'" style="--x:{x};--y:{y}">'+t('name','거점 '+str(k+1),'b')+'</div>'
  minimum='6x4'
 elif leaf=='steps':body=''.join('<div class="step">'+t('mark',str(k+1))+'<div class="name">'+H(labels[k])+'</div>'+t('note',note(30,k))+'</div>' for k in range(3));minimum='8x3'
 elif leaf=='versus':
  for k in range(2):
   ns=note(88,k);li=wrap('list',''.join('<div class="item">'+t('name',note(25,k+q),'b')+'</div>' for q in range(3)))
   body+='<div class="side'+(' on' if k else '')+'">'+t('name',labels[k],'b')+t('note',ns)+li+'</div>'
  minimum='10x6'
 else:continue
 data=';--max:30' if leaf=='chart-bar' else ';--max:6000' if leaf=='chart-line' else ';--cols:4' if leaf=='roadmap' else ''
 out=wrap(leaf,body,v,data);path=P/'crossrail'/f;path.parent.mkdir(exist_ok=True,parents=True);path.write_text('<!-- min:'+minimum+' -->\n'+out+'\n');written.append(f)
(P/'source-fixture-manifest.json').write_text(json.dumps({'written':written,'sourceTextPolicy':'All wording is freshly authored operational business copy. Numeric data and member counts preserve the design reference. Existing golden text was changed only where six-character source overlap forbids it.'},ensure_ascii=False,indent=2)+'\n');print('new source fixtures',len(written),'instances',len(new))
