"""Coherent Korean business content for narrative and semantic diagrams."""
def fixtures(name,leaf):
 def root(cls,s):return '<div class="'+cls+'" data-el="'+name+'-'+leaf+'" style="grid-column:1 / span 12;grid-row:1 / span 6">'+s+'</div>'
 def item(cls,s):return '<div class="'+cls+'">'+s+'</div>'
 if leaf=='quote':
  q=[]
  for person,role,text in [('정하린','물류기획실 · 실증 담당','검수표를 한 번 정리하니, 협력 거점에서도 같은 기준으로 물량을 인계했습니다.'),('서도윤','운송운영실 · 배차 담당','차량의 남는 구간을 함께 확인한 뒤, 돌발 주문을 맡길 거점을 더 빨리 정했습니다.')]:
   q.append('<div class="quote" data-el="'+name+'-quote"><blockquote>'+text+'</blockquote><div class="by"><div class="seat avatar" data-ph="1"></div><span class="name">'+person+'</span><span class="note">'+role+'</span></div></div>')
  return [('6x4','<div class="group" style="grid-column:1 / span 12;grid-row:1 / span 6">'+''.join(q)+'</div>'),('4x4',root('quote big','<blockquote>도착 시각을 미리 공유하니,<br>검수 인력을 필요한 곳에 배치할 여유가 생겼습니다.</blockquote><div class="by"><div class="seat avatar" data-ph="2"></div><span class="name">노지안</span><span class="note">권역거점실 · 현장 총괄</span></div>'))]
 if leaf=='prose':
  p=['납품 요일을 권역별로 묶어 배차 횟수와 빈 차량의 이동 구간을 함께 살폈습니다.','정시 도착률은 높아졌지만 야간 인계가 몰리는 거점에는 별도의 검수표가 필요했습니다.','다음 회차에는 지연 사유를 접수 단계부터 구분하고, 예외 물량의 인계 기준을 먼저 맞춥니다.','실증 결과는 거래처별로 나누어 공유하고 추가 검증이 필요한 경로만 다시 조정합니다.']
  return [('6x4',root('prose cols',''.join('<p>'+s+'</p>'for s in p))),('4x2',root('prose lead','<p>납품 변동을 먼저 읽고,<br>현장의 배차를 함께 조정합니다.</p>'))]
 if leaf=='funnel':
  arr=[[('수송 상담','1,000건',100),('견적 협의','820건',82),('운영 합의','640건',64)],[('신규 문의','2,000건',100),('요건 확인','1,800건',90),('실증 협의','1,560건',78),('계약 검토','1,360건',68),('거점 도입','1,100건',55)]]
  return [('8x4',root('funnel',''.join('<div class="stage" style="--v:'+str(v)+'"><span class="name">'+a+'</span><b class="fig">'+b+'</b></div>'for a,b,v in xs)))for xs in arr]
 if leaf=='concentric':
  arr=[[('전체 거래처','12,000'),('정기 배송처','6,400')],[('협력 가능 거점','7,800'),('공동 배차 권역','3,800'),('실증 우선 거점','1,400'),('집중 운영 거점','620')]]
  return [('6x6',root('orbit',''.join('<div class="ring'+(' on'if i==len(xs)-1 else'')+'"><span class="name">'+a+'</span><b class="fig">'+b+'</b></div>'for i,(a,b)in enumerate(xs))))for xs in arr]
 if leaf=='matrix':
  cells=[('도심 협력 확대','짧은 회차를 묶어 정시 인계를 우선합니다.'),('권역 공동 배차','여러 거점의 잔여 차량을 한 번에 조정합니다.'),('단독 거점 운영','현장별 출하량과 인계 시간을 먼저 맞춥니다.'),('광역 예외 수송','돌발 주문의 담당 거점과 검수 인력을 미리 정합니다.')]
  s='<div class="axis-x"><span>단일 거점</span><span>광역 거점</span></div><div class="axis-y"><span>변동 큼</span><span>변동 작음</span></div>'+''.join('<div class="cell'+(' on'if i==1 else'')+'"><b class="name">'+a+'</b><p class="note">'+b+'</p></div>'for i,(a,b)in enumerate(cells))
  sw=[('S','정시 납품 역량',['권역별 전담 검수','표준화한 인계 기록']),('W','예외 수송 의존',['야간 대체 차량 부족','도착 알림 연동 지연']),('O','공동 집하 확대',['산지 협력 문의 증가','공동 배차 실증 추진']),('T','연료비 변동',['운임 조정 주기 단축','긴급 수송 비용 증가'])]
  t=''.join('<div class="cell'+(' on'if i==0 else'')+'"><span class="kick">'+k+'</span><b class="name">'+a+'</b><div class="list" data-el="'+name+'-list">'+''.join('<div class="item"><span class="name">'+z+'</span></div>'for z in ls)+'</div></div>'for i,(k,a,ls)in enumerate(sw))
  return [('6x4',root('matrix',s)),('6x4',root('matrix swot',t))]
 return None
