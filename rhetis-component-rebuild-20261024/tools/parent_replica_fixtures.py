from pathlib import Path
import json
B=Path('/workspace/work/rebuild-20261024')
def fixture(n,leaf,stem,markup,mn):
 p=B/n/'collection'/n/'elements'/leaf/'fixtures'/(stem+'.html');p.write_text('<!-- min: '+mn+' -->\n'+markup+'\n')
def root(n,cls,leaf,inside,extra=''):
 return '<div class="'+cls+'" data-el="'+n+'-'+leaf+'" style="grid-column:1 / span 12;grid-row:1 / span 6"'+extra+'>'+inside+'</div>'
# AFTERGLOW: source counts, lengths and hierarchy; entirely new copy.
n='afterglow'
fixture(n,'headline','replica-04',root(n,'headline','headline','<p class="kick">Dispatch</p><h2>도심 권역을 잇는 정시 운송,<br>리프웨이브 배송망</h2>'),'6x3')
fixture(n,'headline','replica-09',root(n,'headline center','headline','<h2>창고 입고부터,<br>고객 인계 완료까지</h2>'),'6x3')
fixture(n,'prose','replica-08',root(n,'prose','prose','<p>수집한 전표를 읽고, 신규 배차 기준을<br>순서대로 살펴봅니다. 권역별 묶음 규칙을 나누어 확인하면,<br>검수 담당자가 인계 지점을 쉽게 찾습니다.<br>야간 운송의 예외 구간도 함께 기록하고, 중요한 요청부터<br>다음 작업표에 반영합니다.</p>'),'4x4')
fixture(n,'prose','replica-01-lead',root(n,'prose lead','prose','<p>납품 도착 시각을<br>예측할 수 있도록.</p>'),'4x3')
fixture(n,'prose','replica-01-quiet',root(n,'prose quiet','prose','<p>노스퀘어는 거래처의 납품 요일을 함께 조정합니다.<br>공동 배차를 활용해 긴급 요청에 대응할 여유를 확보합니다.<br>물량이 몰리는 주간에는 임시 거점을 우선 가동하고,<br>각 구간의 완료 기록을 다음 발주 기준에 반영합니다.</p>'),'5x3')
fixture(n,'prose','replica-03',root(n,'prose quiet','prose','<p>주간 인계 결과를 간추려 다음 운송의 기준을 마련합니다.<br>거점별 특이 사항은 짧은 관측 메모로 공유합니다.</p>'),'5x2')
fixture(n,'prose','replica-07',root(n,'prose quiet','prose','<p>리프웨이브는 권역별 마감 시각을 나누고,<br>확정된 물량에 맞춰 운송 자원을 배정합니다.<br>실제 도착 이력을 점검해 다음 배차표를 다듬고,<br>검수 담당자에게 변경 사항을 전달합니다.</p>'),'4x3')
fixture(n,'list','replica-04',root(n,'list','list','<div class="item"><span class="mark"><span class="icon" data-icon="chevron-right"></span></span><span class="name">공동 배차를 활용한 권역별 납기 조정</span><span class="note">노스퀘어는 주문 밀도가 높은 구간을 모아<br>하역 지연을 줄이는 배차표를 마련합니다.<br>인계 누락이 잦은 품목은 별도 검수하고,<br>거래처의 도착 요청 시각에 맞춰<br>다음 회차의 집하 순서를 확정합니다.</span></div>'),'5x4')
fixture(n,'list','replica-03',root(n,'list check','list',''.join('<div class="item"><span class="name">'+x+'</span></div>'for x in ['주간 집하 내역','분류 구간 점검','다음 회차 배정'])),'4x3')
fixture(n,'card','replica-05','<div class="group" style="grid-column:1 / span 12;grid-row:1 / span 6">'+''.join('<div class="card" data-el="afterglow-card"><div class="parts"><div class="mark"><div class="seat" data-ph="'+str(i)+'"></div></div><div class="kick">'+str(i)+'</div><div class="name">'+title+'</div><div class="note">권역의 물량 편차를 세밀하게 구분합니다.<br>다음 회차에 반영할 인계 기준을 정합니다.</div></div></div>'for i,title in enumerate(['도심 공동 배송','냉장 집하 거점','지역별 검수 및 인계','긴급 보충과 회수 운영'],1))+'</div>','12x6')
fixture(n,'agenda','replica-02',root(n,'agenda','agenda',''.join('<div class="entry"><span class="name">'+a+'</span><span class="note">'+b+'</span></div>'for a,b in [('Dispatch','배차 기준'),('Warehouse','거점 운영'),('Inspection','검수 흐름'),('Delivery','인계 절차'),('Partnership','협력 문의')])),'12x3')
fixture(n,'tag','replica-07',root(n,'tag','tag','집하 1. 분류'),'3x1')
fixture(n,'image-frame','replica-04',root(n,'frame','image-frame','<div class="seat" data-ph="1"></div>'),'5x4')
fixture(n,'image-frame','replica-07',root(n,'frame','image-frame','<div class="seat" data-ph="2"></div>'),'5x4')
fixture(n,'steps','replica-08',root(n,'steps col','steps',''.join('<div class="step"><div class="mark"><span class="icon" data-icon="'+icon+'"></span></div><div class="name">'+title+'</div><div class="note">먼저 권역별 출하 전표를 모읍니다.<br>검수 기록을 살펴 다음 배차의 순서를 확정합니다.<br>거점 담당자가 인계 상태를 차례로 확인합니다.</div></div>'for icon,title in [('package-open','1. 출하 전표 분류'),('key-round','2. 배차 권한 확인'),('shield-check','3. 인계 기록 검증')])),'6x6')
fixture(n,'chart-area','replica-06',root(n,'areas','chart-area','<div class="series tone-1"><span class="name"></span>'+''.join('<div class="pt" style="--v:'+str(v)+'"></div>'for v in [54.68,57.97,62.28,69.62,80.25,100])+'</div><div class="axis">'+''.join('<span></span>'for _ in range(6))+'</div>',extra=' data-note="unlabelled trend"'),'12x4')
# --max is a contract data attribute, placed on the same root style.
p=B/n/'collection'/n/'elements/chart-area/fixtures/replica-06.html';p.write_text(p.read_text().replace('grid-row:1 / span 6"','grid-row:1 / span 6;--max:100"'))
# CONFLUENCE: three independent contract components are visible across the four pages.
n='confluence'
fixture(n,'agenda','replica-02',root(n,'agenda','agenda',''.join('<div class="entry"><span class="mark">'+f'{i:02}'+'</span><span class="name">'+title+'</span><span class="note">권역의 운영 이력을 먼저 살펴보고<br>인계 기준을 차례로 정비합니다.</span></div>'for i,title in enumerate(['산지 집하망','권역별 배차','거점 검수','납기 예측','회수 운영','다음 실험'],1))),'12x6')
values=[('협력 일정','운영 기간','2027년 2월 9일<br>~ 4월 2일 (53일간)',[('1차 실증','2027년 2월 9일~3월 5일'),('2차 확장','2027년 3월 6일~4월 2일')]),('배차 재원','총 배정액','3억 8천',[('거점 운영비','196,820,000원'),('운송 정비비','183,180,000원')]),('운영 조직','총괄 담당','정하린',[('검수 담당','서도윤 / 인계 정합<br>노지안 / 출하 점검<br>박다은 / 권역 조정<br>윤태오 / 실증 분석')])]
fixture(n,'card','replica-03','<div class="group" style="grid-column:1 / span 12;grid-row:1 / span 6">'+''.join('<div class="card" data-el="confluence-card"><div class="parts"><div class="kick">'+a+'</div><div class="name">'+b+'</div><div class="fig">'+v+'</div><div class="note">'+''.join('<p><b>'+a+'</b>'+b+'</p>'for a,b in notes)+'</div></div></div>'for a,b,v,notes in values)+'</div>','12x6')
core='<div class="core"><div class="mark"><div class="seat" data-ph="1"></div></div><div class="name">공동 배차<br><b>핵심</b></div><div class="kick">JOINT NETWORK</div><div class="note">산지와 도심을 잇는<br>인계 체계를 설계합니다.</div></div>'
spokes=''.join('<div class="spoke"><div class="mark"><span class="icon" data-icon="'+icon+'"></span></div><div class="name">'+title+' <b>'+f'{i:02}'+'</b></div><div class="note">도착 시각의 편차를 줄이고,<br>검수 이력을 권역별로 나눕니다.<br>예외 물량은 임시 거점에 배정해<br>다음 작업의 기준을 마련합니다.</div></div>'for i,(icon,title)in enumerate([('chart-no-axes-combined','납기 정합'),('messages-square','인계 연동'),('mail-open','전표 공유'),('arrow-down-up','물량 조정')],1))
fixture(n,'hub','replica-04',root(n,'hub','hub',core+spokes),'12x6')
# Bind every mapping instance to its exact fixture, retaining source variants and repeated designs.
for n in ['afterglow','confluence']:
 p=B/n/'review/map.json';d=json.loads(p.read_text())
 for x in d['instances']:
  if not x.get('leaf'):continue
  leaf=x['leaf'];pp=x['page'];use=x['use']
  if n=='afterglow' and leaf=='headline' and pp not in ['04','09']:stem='replica-04'
  elif n=='afterglow' and leaf=='list' and pp=='06':stem='replica-04'
  elif n=='afterglow' and leaf=='prose' and pp in ['01','09']:stem='replica-'+pp+('-lead'if use=='variant:.lead'else'-quiet')
  else:stem='replica-'+pp
  if (B/n/'collection'/n/'elements'/leaf/'fixtures'/(stem+'.html')).exists():x['fixture']=stem
  if n=='afterglow' and leaf=='chart-area':x['bbox']=[60.5,228.5,1161,398.5];x['source_metrics'].append({'source_path':'M37 384 L268 371 L499 354 L730 325 L960 283 L1191 205 L1191 600 L37 600 Z','source_baseline':600,'source_plot_bounds':[37,205,1154,395]})
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
print('source-shaped fixtures with new business text complete')
