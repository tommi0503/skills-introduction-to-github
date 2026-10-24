"""New Korean business content for source-shaped component fixtures."""
from pathlib import Path
P=Path(__file__).parent;K=P/'vectorbox'
def icon(n):return '<span class="icon" data-icon="'+n+'"></span>'
def root(leaf,cls,inner,data=''):return f'<div class="{cls}" data-el="vectorbox-{leaf}" style="grid-column:1 / span 12;grid-row:1 / span 6{data}">{inner}</div>'
def put(leaf,n,cls,inner,mini='4x3',suffix='',data=''):(K/'elements'/leaf/'fixtures'/f'replica-{n:02}{suffix}.html').write_text(f'<!-- min: {mini} -->\n'+root(leaf,cls,inner,data)+'\n')
def card(inner,cls='card'):return root('card',cls,'<div class="parts">'+inner+'</div>')
put('agenda',2,'agenda',''.join(f'<div class="entry"><span class="mark">{i+1:02}</span><p class="name">{t}</p><p class="note">{n}</p></div>' for i,(t,n) in enumerate([('권한 배정','승인 범위를 조정합니다.'),('납품 기록','거래 누락을 찾습니다.'),('재고 경보','부족 품목을 알립니다.'),('매장 실험','신규 채널을 검증합니다.'),('채권 점검','미수 잔액을 확인합니다.'),('원가 배분','지점 손익을 나눕니다.')])), '6x4')
put('card',3,'card line','<div class="parts"><span class="mark">'+icon('scan-search')+'</span><p class="name">계약 누락 탐지</p><p class="note">변경 이력을 모아<br>승인 대기 건을 찾습니다.</p></div>','3x4')
put('card',4,'card on','<div class="parts"><b class="fig">78<small>%</small></b></div>','3x3','-on')
put('card',4,'card line','<div class="parts"><span class="mark">'+icon('badge-dollar-sign')+'</span><p class="name">채권 회수율</p></div>','3x3','-line')
put('card',5,'card quiet','<div class="parts"><span class="mark">'+icon('package-check')+'</span><p class="name">납품 오차 축소</p><p class="note">출고 증빙을 대조해<br>반품 원인을 줄입니다.</p></div>','3x4')
put('card',8,'card','<div class="parts"><span class="mark">'+icon('warehouse')+'</span><p class="name">지점 발주 통합</p><p class="note">매장별 재고를 묶어<br>품절 위험과 잔여 물량을<br>함께 조정합니다.</p></div>','3x4')
put('card',10,'card','<div class="parts"><span class="mark">'+icon('coins')+'</span></div>','3x3','-mark')
put('card',10,'card','<div class="parts"><p class="name">정산 기한 단축</p><p class="note">주문 증빙을 연결하고<br>담당 권한을 나누어<br>미승인 거래를 줄입니다.</p><span class="mark">'+icon('receipt-text')+'</span></div>','4x4','-text')
put('card',11,'card','<div class="parts"><span class="mark">'+icon('headphones')+'</span></div>','3x3','-mark')
put('card',12,'card line','<div class="parts"><p class="kick">입점 담당</p><span class="mark">'+icon('contact-round')+'</span><p class="note">운영 2조 / 매니저</p><p class="name">윤서진</p></div>','3x5')
put('legend',4,'legend','<span class="key tone-1">입점 승인 건수</span><span class="key tone-2">정산 대기 잔액</span>','4x2')
put('legend',10,'legend',''.join('<span class="key tone-'+str((i%5)+1)+'">'+n+'</span>' for i,n in enumerate(['물류 28%','정산 21%','교육 19%','점검 14%','상담 11%','기타 7%'])),'4x3')
hub='<div class="core"><span class="name">거래 통합 허브</span></div>'
for n,t,ic in [('승인 배정','담당 권한을 나눠<br>미처리 건을 줄입니다.','workflow'),('거래 대조','증빙 이력을 묶어<br>정산 잔액을 찾습니다.','files'),('채권 경보','갱신 기한 전에<br>담당자에게 알립니다.','bell-ring'),('재고 연동','매장별 잔여 물량을<br>발주 순서에 반영합니다.','boxes')]:hub+='<div class="spoke"><span class="mark">'+icon(ic)+'</span><p class="name">'+n+'</p><p class="note">'+t+'</p></div>'
put('hub',6,'hub',hub,'9x4')
put('table',7,'tablebox','<table class="table"><thead><tr><th>검토 항목</th><th>현행 절차</th><th class="pick">개편 절차</th><th>확인 지표</th></tr></thead><tbody>'+''.join('<tr><td>'+n+'</td><td>수동 대조</td><td class="pick">자동 연계</td><td>'+t+'</td></tr>' for n,t in [('납품 증빙','반품 12건 감소'),('미수 잔액','회수 기간 8일 단축'),('권한 이력','재승인 6건 감소'),('교육 수료','점검 누락 9건 축소')])+'</tbody></table>','8x4')
seq=''
for n,t,ic in [('접수','요청 범위를 모읍니다.','inbox'),('대조','증빙 이력을 연결합니다.','scan-line'),('배정','승인 권한을 나눕니다.','git-branch'),('점검','미승인 건을 살핍니다.','list-checks'),('회수','잔액 갱신을 알립니다.','banknote'),('종결','변경 기록을 보관합니다.','archive')]:seq+='<div class="step"><span class="mark">'+icon(ic)+'</span><p class="name">'+n+'</p><p class="note">'+t+'</p></div>'
put('steps',9,'steps',seq,'9x4')
put('callout',11,'callout',icon('message-square-text')+'<p>납기 편차를 줄일 방안을<br>함께 논의합니다.</p>','6x3')
lis=''
for n,t,ic in [('입점 상담','070-8421-6930','phone'),('담당 메일','partners@branch.co','mail'),('지원 주소','경기도 수원시 권선로 92','map-pinned'),('예약 창구','branch.co/visit','globe'),('정산 문의','billing@branch.co','receipt')]:lis+='<div class="item"><span class="mark">'+icon(ic)+'</span><p class="name">'+n+'</p><p class="note">'+t+'</p></div>'
put('list',12,'list divided',lis,'6x4')
put('headline',13,'headline big','<h2><b>납기 편차를 줄이고</b>거래 신뢰를 쌓습니다</h2><p class="note">증빙 연동과 승인 배정으로 정산 지연을 낮춥니다.</p>','8x3')
put('image-frame',13,'frame','<div class="seat portrait" data-ph="7">7</div>','3x3')
put('prose',13,'prose quiet','<p>BRANCH OPERATIONS<br>partners@branch.co</p>','4x2')
print('Source-shaped fixtures use new Korean business prose.')
