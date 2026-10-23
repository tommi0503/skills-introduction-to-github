from pathlib import Path
import re
C=Path('/workspace/output/cyanloop')
for p in C.glob('elements/*/fixtures/*.html'):
 if p.parent.parent.name in ['card','callout','chart-area','chart-bar','chart-donut','chart-line']:continue
 s=p.read_text()
 def lists(m):
  tag,attrs,body=m.group(1),m.group(2),m.group(3)
  if 'data-el=' not in attrs:attrs+=' data-el="cyanloop-list"'
  def item(x):
   itag,attr,text=x.group(1),x.group(2),x.group(3)
   if 'class="item' in attr:return x.group(0)
   return '<'+itag+' class="item"><span class="name">'+text+'</span></'+itag+'>'
  if 'class="item' not in body:body=re.sub(r'<(li|p)([^>]*)>(.*?)</\1>',item,body,flags=re.S)
  return '<'+tag+attrs+'>'+body+'</'+tag+'>'
 s=re.sub(r'<(ul|div)(\s+class="list[^>]*?)>(.*?)</\1>',lists,s,flags=re.S)
 s=re.sub(r'<span class="tag"(?![^>]*data-el)', '<span class="tag" data-el="cyanloop-tag"',s)
 p.write_text(s)
def lst(values):return '<ul class="list" data-el="cyanloop-list">'+''.join('<li class="item"><span class="name">'+v+'</span></li>' for v in values)+'</ul>'
p=C/'elements/versus/fixtures/expanded-versus.html';p.write_text('<!-- min: 8x4 -->\n<div class="versus" data-el="cyanloop-versus" style="grid-column:1 / span 12; grid-row:1 / span 6"><div class="side"><b class="name">개별 업무 중심의 기존 교육 운영</b>'+lst(['부서별로 다른 교육 신청과 일정 관리','참여 인원만 확인하는 월말 보고','학습 이후 현업 적용 여부 파악의 어려움'])+'</div><b class="vs">VS</b><div class="side on"><b class="name">현업 전환을 관리하는 통합 학습 운영</b>'+lst(['조직의 목표에 맞춘 하나의 교육 로드맵','학습 진행과 성과를 함께 보는 실시간 지표','전담 코치와 부서장이 공동으로 관리하는 현업 적용 과제','분기별 개선 사항을 다음 과정에 반영'])+'</div></div>\n')
p=C/'elements/tag/fixtures/expanded-tag-hl.html';p.write_text('<!-- min: 6x2 -->\n<div class="prose" data-el="cyanloop-prose" style="grid-column:1 / span 12; grid-row:1 / span 6"><p><span class="tag" data-el="cyanloop-tag">현업 적용</span> 교육이 끝난 뒤에도 전담 코치가 과제 진행을 지원합니다. 이번 분기에는 <b class="hl" data-el="cyanloop-tag">팀 단위 적용 프로젝트 24건</b>을 완료했습니다.</p></div>\n')
p=C/'elements/legend/fixtures/expanded-legend.html';p.write_text('<!-- min: 4x1 -->\n<div class="legend" data-el="cyanloop-legend" style="grid-column:1 / span 12; grid-row:1 / span 6"><span class="key tone-1">교육 참여</span><span class="key tone-2">학습 완료</span><span class="key tone-3">현업 적용 성과</span></div>\n')
p=C/'elements/pricing/fixtures/expanded-plans-3.html';p.write_text('<!-- min: 8x4 -->\n<div class="plans" data-el="cyanloop-pricing" style="grid-column:1 / span 12; grid-row:1 / span 6"><div class="plan" data-el="cyanloop-pricing"><b class="name">실무 집중 워크숍</b><div class="price"><b class="fig">12만</b><small>원 / 인</small></div>'+lst(['직무별 핵심 과제 실습','수료 후 2주 동안의 과제 피드백'])+'</div><div class="plan on" data-el="cyanloop-pricing"><span class="tag" data-el="cyanloop-tag">조직 맞춤</span><b class="name">현업 전환 통합 학습 프로그램</b><div class="price"><b class="fig">32만</b><small>원 / 인</small></div>'+lst(['사전 진단과 맞춤형 과정 설계','온·오프라인 통합 교육','팀 단위 현업 적용 프로젝트','분기별 성과 분석과 개선 제안'])+'</div></div>\n')
fix={'list':'.list[data-el="cyanloop-list"]{list-style:none;margin:0;padding:0;}', 'versus':'.versus[data-el="cyanloop-versus"] .side>.list{flex:1;width:100%;min-height:0;}', 'pricing':':is(.plan[data-el="cyanloop-pricing"],.plans[data-el="cyanloop-pricing"]) .plan>.list,:is(.plan[data-el="cyanloop-pricing"],.plans[data-el="cyanloop-pricing"]).plan>.list{flex:1;width:100%;min-height:0;}', 'matrix':'.matrix[data-el="cyanloop-matrix"] .cell>.list{flex:1;width:100%;min-height:0;}'}
for n,txt in fix.items():
 p=C/'elements'/n/'element.css';p.write_text(p.read_text()+'\n'+txt+'\n')
