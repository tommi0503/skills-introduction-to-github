"""Measured source17 bare metrics and source02 numbered agenda, authored anew."""
from write_elements import write
import sys

def author(k):
 if k=='metric':
  css='''/* Replica17:19px left names,43px bold figures with30px units,12px left notes;90px vertical rules.
The enclosing gray panel is unexpressible, so these figures draw no surface. */
.stats[data-el="onboard-docket-metric"]{container-type:size;container-name:od-stats;display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:var(--onboard-docket-metric-gap);min-width:0;min-height:0;color:var(--n-8);--od-stat-count:3}
.stats[data-el="onboard-docket-metric"]:has(>.stat:nth-child(4):last-child){--od-stat-count:4}
.stats[data-el="onboard-docket-metric"]:has(>.stat:nth-child(2):last-child){--od-stat-count:2}
.stat[data-el="onboard-docket-metric"]{container-type:size;container-name:od-stat;display:flex;align-items:center;justify-content:center;min-width:0;min-height:0;color:var(--n-8)}
.stats[data-el="onboard-docket-metric"]>.stat{position:relative;flex:1 1 0;min-width:0;min-height:0;height:min(100%,137px);padding-inline:0}
.stats[data-el="onboard-docket-metric"]>.stat:not(:last-child)::after{content:"";position:absolute;right:calc(var(--onboard-docket-metric-gap)*-.35);top:17%;height:66%;width:1px;background:var(--n-5)}
.stat[data-el="onboard-docket-metric"]>.parts{width:100%;display:flex;flex-direction:column;justify-content:center;align-items:stretch;gap:0;text-align:left;min-width:0}
.stat[data-el="onboard-docket-metric"]>.parts>.name{order:0;margin:0;font-size:clamp(var(--type-14),calc(7.3cqw),var(--type-20));font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);overflow-wrap:anywhere}
.stat[data-el="onboard-docket-metric"]>.parts>.fig{order:1;margin:0;font-size:clamp(var(--type-28),calc(18.3cqw),var(--type-44));font-weight:var(--onboard-docket-value-weight);line-height:var(--body-line);text-align:right;padding-right:4.7%;letter-spacing:var(--figure-track);overflow-wrap:anywhere}
.stat[data-el="onboard-docket-metric"]>.parts>.fig>small{font-size:var(--type-30);font-weight:var(--body-weight)}
.stat[data-el="onboard-docket-metric"]>.parts>.note{order:2;margin:0;font-size:var(--type-12);font-weight:var(--name-weight);line-height:var(--body-line);letter-spacing:var(--body-track);color:var(--ink);overflow-wrap:anywhere}
@container od-stats (max-width:560px){.stats[data-el="onboard-docket-metric"]>.stat{flex-basis:100%;height:calc((100% - (var(--od-stat-count) - 1)*var(--onboard-docket-metric-gap)) / var(--od-stat-count));padding:0}.stats[data-el="onboard-docket-metric"]>.stat:not(:last-child)::after{left:15%;right:15%;top:auto;bottom:0;height:1px;width:70%}}
@container od-stat (max-height:100px){.stat[data-el="onboard-docket-metric"]>.parts{flex-direction:row;align-items:center;justify-content:center;flex-wrap:wrap;column-gap:var(--gap-sm)}.stat[data-el="onboard-docket-metric"]>.parts>.name{font-size:var(--type-14)}.stat[data-el="onboard-docket-metric"]>.parts>.fig{font-size:var(--type-24);line-height:var(--figure-line);padding:0}.stat[data-el="onboard-docket-metric"]>.parts>.fig>small{font-size:var(--type-18)}.stat[data-el="onboard-docket-metric"]>.parts>.note{display:none}}
'''
  def row(n,long=False):
   names=['월간 이관 건수','승인 대기 건수','첫 응답 준수율','후속 점검 완료율'];figs=['287','34','92.6','96.1'];units=['건','건','%','%']
   return '<div class="stats" DATA>'+''.join('<div class="stat" data-el="onboard-docket-metric"><div class="parts"><p class="name">'+names[i]+(' 및 예외 처리 현황' if long and i==0 else '')+'</p><p class="fig">'+figs[i]+' <small>'+units[i]+'</small></p><p class="note">'+['승인 기록에서 집계한 접수 물량','담당자 배정 후 이관을 기다리는 항목','영업일 기준 응답 시간을 대조한 결과','조치 종료 뒤 품질 담당자가 대조한 수치'][i]+'</p></div></div>'for i in range(n))+'</div>'
  write(k,'stat',css,'Bare figures preserve the name–number–note hierarchy of replica17. A short vertical rule separates members; a compact column substitutes horizontal rules while retaining every name and figure. The original gray panel is deliberately recorded as an unsupported container.',[('replica-17','6x3',row(3)),('four-long','6x6',row(4,True))])
 elif k=='agenda':
  css='''/* Replica02:451×64 capsules,56px leading number circles and22px names.
Eight entries run down four rows before the second column; rows have16px gaps. */
ROOT{container-type:size;container-name:od-agenda;display:grid;grid-auto-flow:column;grid-template-columns:repeat(2,minmax(0,1fr));grid-template-rows:repeat(var(--od-agenda-rows),minmax(0,1fr));align-content:center;align-self:center;block-size:min(100%,calc(var(--od-agenda-rows)*64px + (var(--od-agenda-rows) - 1)*var(--gap-sm)*8/7));inline-size:min(100%,937px);justify-self:center;padding-inline:0;column-gap:3.735%;row-gap:calc(var(--gap-sm)*8/7);min-width:0;min-height:0;--od-agenda-rows:4;}
ROOT:has(>.entry:nth-child(4):last-child){--od-agenda-rows:2}ROOT:has(>.entry:nth-child(5):last-child),ROOT:has(>.entry:nth-child(6):last-child){--od-agenda-rows:3}
ROOT>.entry{position:relative;display:flex;align-items:center;gap:calc(var(--pad)*.9);border-radius:999px;background:var(--n-1);padding:calc(var(--gap-sm)/4);min-width:0;min-height:0}
ROOT>.entry>.mark{flex:none;display:flex;align-items:center;justify-content:center;inline-size:min(5.977cqw,56px);aspect-ratio:1;border-radius:50%;background:var(--a1);color:var(--a1-on);font-size:clamp(var(--type-12),calc(2.134cqw),var(--type-20));font-weight:var(--onboard-docket-value-weight);line-height:var(--label-line);letter-spacing:var(--label-track)}
ROOT>.entry>.name{margin:0;padding-right:var(--gap-sm);font-size:clamp(var(--type-14),calc(2.348cqw),var(--type-22));font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);color:var(--ink);overflow-wrap:anywhere}
ROOT>.entry>.note{margin:0;font-size:var(--type-12);line-height:var(--body-line);font-weight:var(--body-weight);letter-spacing:var(--body-track);color:var(--n-7)}
@container od-agenda (max-width:750px){ROOT>.entry{gap:var(--gap-sm)}ROOT>.entry>.mark{inline-size:min(7cqw,48px)}ROOT>.entry>.name{font-size:var(--type-16)}ROOT>.entry>.note{display:none}}
@container od-agenda (max-height:230px){ROOT>.entry{gap:calc(var(--gap-sm)/2)}ROOT>.entry>.mark{inline-size:min(20cqh,48px);font-size:var(--type-12)}ROOT>.entry>.name{font-size:var(--type-14);line-height:var(--label-line)}ROOT>.entry>.note{display:none}}
'''
  css+='ROOT:has(>.entry:nth-child(2):last-child){--od-agenda-rows:1}ROOT:has(>.entry:nth-child(3):last-child){--od-agenda-rows:2}ROOT>.entry.on{background:var(--a1-1-soft)}ROOT>.entry.on>.name{color:var(--a1-7)}'
  def row(n,long=False):
   labels=['접수 채널과 책임 범위','지연 원인 검토 결과','승인 기록 관리 원칙','이관 전 점검 항목','현장 담당자 협의','배포 일정과 예외 승인','품질 지표 대조 방법','후속 개선 과제']
   return '<div class="agenda" DATA>'+''.join('<div class="entry'+(' on'if long and i==0 else'')+'"><span class="mark">'+str(i+1).zfill(2)+'</span><p class="name">'+labels[i]+(' 및 담당 조직 배정' if long and i==0 else '')+'</p></div>'for i in range(n))+'</div>'
  write(k,'agenda',css,'Pale pill-shaped entries carry a leading filled number circle. The eight-item arrangement of replica02 fills four rows down each column, with its original circle-to-row ratio and open inter-column space. Narrower boxes step down typography without losing entries.',[('replica-02','8x4',row(8)),('six-long','6x4',row(6,True))])
 else:raise SystemExit(k)

if __name__=='__main__':author(sys.argv[1])
