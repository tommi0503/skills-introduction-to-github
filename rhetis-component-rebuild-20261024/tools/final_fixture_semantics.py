"""Human editorial pass over inferred fixtures: retain shape/count, supply coherent business data."""
from pathlib import Path
from lxml import html as H
import re,json
B=Path('/workspace/work/rebuild-20261024')
LEAVES=['architecture','balance','decision-tree','flowchart','headline','hierarchy','journey','matrix-nine','mindmap','person','positioning','pricing','radar','slope','steps','swimlane','table','tag','timeline','bullet']
def nodes(e,c):return e.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," '+c+' ")]')
def text(q,s):
 for x in list(q):q.remove(x)
 q.text=s

def seq(qs,ss):
 assert len(qs)==len(ss),(len(qs),len(ss))
 for q,s in zip(qs,ss):text(q,s)
def apply(name,leaf,p):
 raw=p.read_text();e=H.fromstring(raw);i=int(p.stem.rsplit('-',1)[1]);a=lambda c:nodes(e,c)
 if leaf=='headline':
  q=e.find('h2');text(q,'거점 운영, ' if i==1 else '권역 배차, ');b=H.Element('b');b.text='인계를 정밀하게'if i==1 else'일정을 하나로';q.append(b)
  text(a('kick')[0],'현장 개선'if i==1 else'권역 실증')
 elif leaf=='person':
  ps=e.xpath('self::*[contains(concat(" ",@class," ")," person ")] | .//*[contains(concat(" ",@class," ")," person ")]')
  for j,q in enumerate(ps):
   text(nodes(q,'name')[0],['정하린','서도윤','노지안'][j]);text(nodes(q,'note')[0],['검수기획 담당','운송조정 담당','현장실증 담당'][j])
 elif leaf=='decision-tree':
  seq(a('name'),['수송 조건','냉장 전용','상온 직송','혼합 운송']if i==1 else['도착 일정','여유 차량','즉시 배정','협력 요청','회차 예약'])
  seq(a('cond'),['온도 고정','상온 유지','조건 혼합']if i==1 else['당일 납품','확보 가능','확보 불가','다음 회차'])
 elif leaf=='flowchart':seq(a('name'),['주문 접수','조건 확인','운영 합의','배차 완료']if i==1 else['현장 접수','수량 검수','인계 판단','배송 출발','차량 대기','재검수 요청'])
 elif leaf=='hierarchy':seq(a('name'),['운영 본부','운송 파트','배차 담당','검수 파트','현장 담당']if i==1 else['협력 본부','권역 운영','배차 조정','전표 담당','현장 지원','검수 담당','안전 담당','거점 기획','운임 담당','수요 담당','데이터실','지표 담당'])
 elif leaf=='architecture':
  layers=a('layer');names=['운영 화면','공유 기록','기반 연동','접근 제어','현장 단말'];chips=[['배차표','인계표','회수표'],['거점 원장','배송 이력','검수 이력','정산 장부'],['차량 위치','주문 연계'],['역할 권한','이력 보관'],['스캔 단말','기사 앱']]
  for j,q in enumerate(layers):text(nodes(q,'name')[0],names[j]);seq(nodes(q,'chip'),chips[j][:len(nodes(q,'chip'))])
 elif leaf=='balance':
  seq(a('name'),['단독 수송','회차 자율','거점 전담','예외 대응','공동 수송','차량 공유','수요 결합','구간 연계'])
  text(a('fulcrum')[0][0],'회차 균형'if i==1 else'공동 배차')
 elif leaf=='positioning':
  seq(e.xpath('.//*[contains(@class,"axis-x")]/span'),['낮은 비용','높은 비용']);seq(e.xpath('.//*[contains(@class,"axis-y")]/span'),['높은 빈도','낮은 빈도'])
 elif leaf=='matrix-nine':
  for axis in ['axis-x','axis-y']:
   qs=e.xpath('.//*[contains(@class,"'+axis+'")]/span')
   if not qs:
    q=H.Element('div',{'class':axis});e.append(q)
    for z in range(3):q.append(H.Element('span'))
    qs=list(q)
   seq(qs,['낮은 수요','중간 수요','높은 수요']if axis=='axis-x'else['변동 큼','보통','변동 작음'])
  seq([nodes(q,'name')[0]for q in a('cell')],['제한 검증','구간 실증','우선 확장','회차 정비','협력 조정','차량 증편','운임 점검','현장 표준','집중 운영'])
 elif leaf=='mindmap':
  seq(a('name'),['인계 개선','기록 통합','담당 조정']if i==1 else['회차 개선','운임','수요','차량','거점','알림','검수'])
  if i==1:seq(a('leaf'),['공유 원장','현장 교육'])
  if i==2:seq(a('leaf'),['비용 점검','주문 묶음','공차 절감','권역 배정','지연 예고','누락 점검'])
 elif leaf=='pricing':
  for j,q in enumerate(a('plan')):
   text(nodes(q,'name')[0],['거점형','권역형','전사형'][j]);text(nodes(q,'fig')[0],['29만','79만','149만'][j]);text(q.xpath('.//small')[0],'원 / 월')
   ls=nodes(q,'list')[0];n=len(nodes(ls,'name'));seq(nodes(ls,'name'),[['인계표 공유','검수 이력','주간 집계'],['차량 위치','권역 배정','거점 연계','전담 지원'],['통합 원장','권한 관리','맞춤 연동']][j][:n])
   if nodes(q,'tag'):text(nodes(q,'tag')[0],'추천')
 elif leaf=='radar':
  seq([nodes(q,'name')[0]for q in a('axis')],['정시율','검수율','회수율']if i==1 else['정시율','검수율','회수율','가동률','예측력','원가율','연계율','대응력'])
  seq([nodes(q,'name')[0]for q in a('series')],['실증 후']if i==1 else['실증 후','실증 전','협력 평균'])
 elif leaf=='slope':
  q=a('heads')[0]
  if len(q)==1:q.append(H.Element('span'))
  seq(q.xpath('./span'),['실증 전','실증 후'])
 elif leaf=='table':
  seq(e.xpath('.//thead//th'),['권역','2055년','2056년']if i==1 else['권역','거점','매출','증감','거래처','이익률'])
  for j,q in enumerate(e.xpath('.//tbody/tr')):
   cs=q.xpath('./td');text(cs[0],['도심권','서부권','동부권','남부권','북부권','산지권'][j])
   if i==2:text(cs[1],['역세권','공단권','연안권','중심권','외곽권','산간권'][j])
 elif leaf=='tag':
  q=e.find('p');q.text='이번 실증비는 ';q[0].text='162억 원';q[0].tail='으로, ';q[1].text='확정';q[1].tail=' 범위에 반영합니다.'
 elif leaf=='timeline':
  ss=a('stop')
  for j,q in enumerate(ss):text(nodes(q,'kick')[0],str(2052+j)if i==1 else str(j+1)+'분기')
 elif leaf=='steps':
  for j,q in enumerate(a('step')):text(nodes(q,'name')[0],['접수 확인','물량 검수','배차 확정','현장 인계'][j]);text(nodes(q,'note')[0],['접수 전표와 도착 조건을 대조합니다.','포장 수량과 보관 상태를 살핍니다.','권역별 차량과 운행 회차를 정합니다.','인계표에 도착 시각과 수량을 남깁니다.'][j])
 elif leaf=='journey':
  for j,q in enumerate(a('stage')):text(nodes(q,'name')[0],['수송 문의','견적 확인','배차 협의','검수 접수','현장 인계','도착 확인','운임 정산'][j]);text(nodes(q,'note')[0],['접수 조건을 온라인으로 남깁니다.','구간별 수송비를 함께 살핍니다.','납기와 차량 종류를 맞춥니다.','입고 수량을 담당자가 확인합니다.','인계표에 상태를 적습니다.','도착 시각을 거래처에 전합니다.','실제 운행 내역을 정산합니다.'][j])
 elif leaf=='swimlane':
  for j,q in enumerate(a('lane')):text(nodes(q,'name')[0],['접수 담당','배차 담당','검수 담당','거점 담당','정산 담당'][j])
  for j,q in enumerate(a('node')):text(nodes(q,'name')[0],['주문 접수','조건 확인','배차 배정','수량 검수','예외 협의','인계 완료'][j])
 elif leaf=='bullet':
  for q in a('bullet')or[e]:
   v=re.search(r'--v:\s*([\d.]+)',q.get('style',''))
   if v and nodes(q,'fig'):text(nodes(q,'fig')[0],v[1]+'%')
 else:return False
 p.write_text(raw.split('\n',1)[0]+'\n'+H.tostring(e,encoding='unicode')+'\n');return True
if __name__=='__main__':
 rows=[]
 for name in ['afterglow','confluence']:
  for leaf in LEAVES:
   for p in sorted((B/name/'collection'/name/'elements'/leaf/'fixtures').glob('business-*.html')):
    try:
     if apply(name,leaf,p):rows.append(str(p.relative_to(B)))
    except Exception as exc:raise RuntimeError((name,leaf,p.name))from exc
 (B/'fixture-editorial-pass.json').write_text(json.dumps(rows,indent=2));print(len(rows),'fixtures editorially revised')
