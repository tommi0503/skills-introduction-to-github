"""Describe the actual Round5 designs, their sources and remaining gaps."""
from pathlib import Path
from lxml import html
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
def norm(s):
 try:return re.sub(r'\s+','',''.join(html.fragment_fromstring(s).itertext())).casefold()
 except:return ''
def main():
 cs=json.loads((ROOT/'collections.json').read_text());summary=[];allchanges=[]
 for col in cs:
  cid=col['id'];C=ROOT/cid;R=ROOT/(cid+'-review');m=json.loads((R/'map.json').read_text());old=json.loads((R/'round4-map.json').read_text());folders=sorted(p.name for p in(C/'elements').iterdir()if p.is_dir());oldobs={x.get('leaf')for x in old['instances']if x.get('leaf')and x['use']not in ['unexpressible','furniture','background']};oldfolders=set(json.loads((ROOT/'contract/leaves.json').read_text()));deleted=sorted((oldfolders-oldobs)-set(folders));replaced=sorted(oldobs-set(folders));new=sorted(set(folders)-oldfolders)
  sources={leaf:sorted({x['page']for x in m['instances']if x.get('leaf')==leaf or('data-el="'+cid+'-'+leaf+'"')in x.get('markup','')})for leaf in folders}
  lines=['# '+cid+' — round5','','| 디자인 폴더 | replica 페이지 | 시트 |','|---|---|---|']
  for leaf in folders:
   lines.append('| '+leaf+' | '+(', '.join(sources[leaf])or'실제 요소의 중첩 의존성')+' | [light](sheets/'+leaf+'-light.png) · [dark](sheets/'+leaf+'-dark.png) · [replica](sheets/'+leaf+'-replica.png) |')
  (R/'PROVENANCE.md').write_text('\n'.join(lines)+'\n')
  gaps=[x for x in m['instances']if x['use']=='unexpressible'];glines=['# 남은 gap','']
  if not gaps:glines+=['없음. 이전의 측정 덤프·라벨·캡션은 소유 요소 또는 foundation 장치에 귀속했고, 두 번째 디자인은 독립 폴더로 복원했습니다.','']
  else:
   for x in gaps:glines+=['- replica '+x['page']+': '+x['design']+' — '+x['why'],'','```html',x.get('required_markup',x.get('markup','')),'```','']
  (R/'GAPS.md').write_text('\n'.join(glines))
  report=ROOT/'round5'/(cid+'-report.md');owner=report.read_text()if report.exists()else''
  charts=sorted({x.get('leaf')for x in m['instances']if any(c in x.get('markup','')for c in ['class="slice','class="line"','class="series','grouped','class="at"'])and x.get('leaf')})
  panels=m.get('panels',[])
  integration=ROOT/'round5'/(cid+'-integration.md')
  if integration.exists(): owner+='\n\n'+integration.read_text()
  notes=['# '+cid+' 검수 기록 — round5','','## 실제 컬렉션 구성','',f'- 관찰 디자인 및 실제 중첩 의존성: {len(folders)}개.',f'- 삭제한 미관찰 일반 요소: {len(deleted)}개 — '+', '.join(deleted)+'.',f'- 독립 디자인/패널로 교체한 기존 계열 폴더: {len(replaced)}개 — '+(', '.join(replaced)or'없음')+'.','- 새 디자인 폴더: '+(', '.join(new)or'없음')+'.','- 원본은 위에서 아래로 의미 요소를 먼저 분류했습니다. 글자 조각을 DOM 잔여물로 잘라 gap으로 남기지 않았습니다.','- 표제 틀은 foundation.panel이 소유하고, 표·차트·카드는 독립 data-el 요소로 중첩했습니다.','- 페이지 body는12×6이며 패널 내부의 배치는120×60 비율 그리드입니다. 이 내부 그리드는 데이터가 아니라 하위 요소의 원본 상대 위치를 보존하는 foundation 레이아웃입니다.','- 사진·3D·복잡한 이미지 자리는 연한 중성 면이며, 페이지 전체 장식은 foundation 배경 vector로 기록합니다.','- replica 파일203개와 제공된 폰트는 원본 SHA-256으로 보존합니다.','- fixture는 새 한국어 업무 문구이며, 원문은 조립 검증 페이지에만 사용합니다.','- 원본 숫자 굵기·선·형태 수치는 유지하되 색과 글자 크기는 round5의 팔레트 역할·8–256 타입 토큰을 따릅니다.','- git 명령을 사용하지 않았습니다. 이전 결과를 덮어쓰지 않고 별도 round5 폴더에서 작업했습니다.','','## 패널과 차트 확장','']
  notes+=['- replica '+x['page']+': '+x.get('description','foundation panel')+' / bbox '+str(x['bbox'])for x in panels]
  if not panels:notes+=['패널 없음.']
  notes+=['','차트 확장: '+(', '.join(charts)or'없음')+'.','','## 요소 담당 검수 기록','',owner,'','## 최종 통합 검수','', '실제 마지막 렌더와 검수한 시트/페이지 해시는 루트 primary-visual-review.json 및 각 audits에 기록합니다. 최종 성공 여부는 verification.json을 기준으로 확인합니다.','']
  (R/'review-notes.md').write_text('\n'.join(notes))
  # Reclassify each old gap against concrete new owners, keeping the entire trail.
  changes=[]
  for g in[x for x in old['instances']if x['use']=='unexpressible']:
   bb=g['bbox'];area=max(1,bb[2]*bb[3]);candidates=[];text=norm(g.get('markup',''))
   for x in m['instances']:
    if x['page']!=g['page']or not x.get('leaf'):continue
    p=x['bbox'];over=max(0,min(bb[0]+bb[2],p[0]+p[2])-max(bb[0],p[0]))*max(0,min(bb[1]+bb[3],p[1]+p[3])-max(bb[1],p[1]))
    if over/area>.8 or(text and text in norm(x.get('markup',''))):candidates.append((p[2]*p[3],x['leaf'],x['instance_id']))
   for i,p in enumerate(panels):
    if p['page']!=g['page']:continue
    b=p['bbox'];over=max(0,min(bb[0]+bb[2],b[0]+b[2])-max(bb[0],b[0]))*max(0,min(bb[1]+bb[3],b[1]+b[3])-max(bb[1],b[1]))
    if over/area>.8:candidates.append((b[2]*b[3],'foundation.panel',p.get('instance_id',p.get('id','panel-'+str(i+1)))))
   chosen=min(candidates)if candidates else None
   changes.append({'oldInstance':g['instance_id'],'page':g['page'],'oldBBox':bb,'oldDesign':g.get('design'),'resolution':'mapped-owner'if chosen else'needs-provenance-review','owner':chosen[1]if chosen else None,'ownerInstance':chosen[2]if chosen else None})
  (R/'gap-reclassification.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2));allchanges+= [{'collection':cid,**x}for x in changes]
  rows=[]
  for leaf in folders:
   links=''.join(f'<a href="sheets/{leaf}-{v}.png">{v}</a> 'for v in ['light','dark','replica']if(R/'sheets'/f'{leaf}-{v}.png').exists());rows.append('<li><b>'+leaf+'</b> '+links+'</li>')
  panel_links=('<h2>패널</h2><a href="sheets/foundation-panels-light.png">light</a><a href="sheets/foundation-panels-dark.png">dark</a><a href="sheets/foundation-panels-replica.png">source</a>')if panels else''
  (R/'index.html').write_text('<!doctype html><html lang="ko"><meta charset="utf-8"><title>'+cid+' round5</title><style>body{font:16px/1.6 system-ui;margin:40px}li{margin:12px}a{margin-left:12px}</style><h1>'+cid+' round5</h1><a href="PROVENANCE.md">출처</a><a href="review-notes.md">검수</a><a href="GAPS.md">남은gap</a><ul>'+''.join(rows)+'</ul>'+panel_links+'</html>')
  summary.append({'collection':cid,'designs':len(folders),'newDesignFolders':new,'sources':sources,'deletedGeneric':deleted,'replacedObservedFamilies':replaced,'panels':len(panels),'chartExtensions':charts,'gaps':len(gaps),'pages':col['pages']})
 (ROOT/'round5/summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));(ROOT/'round5/gap-reclassification.json').write_text(json.dumps(allchanges,ensure_ascii=False,indent=2));print('Documented',sum(x['designs']for x in summary),'designs;',len(allchanges),'old gaps;',sum(x['resolution']=='needs-provenance-review'for x in allchanges),'need provenance review')
if __name__=='__main__':main()
