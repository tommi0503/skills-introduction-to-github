"""Fresh inferred charts. Connectors use the independently browser-proved anchor construction."""
from write_elements import write,K,REF,kid
import sys,re

GOLD={'chart-bar':('confetti',['bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2']),'chart-line':('amethyst',['lines-12','lines-6','lines-3','lines-flat']),'chart-area':('annual',['area-1','areas-2','areas-stacked-3','area-3pt']),'chart-donut':('amethyst',['donut','donuts-3','donuts-4','donut-0','donut-100'])}
def golden(k):
 kit,names=GOLD[k]
 for name in names:
  s=(REF/'samples'/kit/'elements'/k/'fixtures'/(name+'.html')).read_text().replace(kit+'-'+k,kid+'-'+k)
  if name=='donuts-4':s=re.sub(r'min: \d+x\d+','min: 4x4',s,count=1)
  (K/'elements'/k/'fixtures'/(name+'.html')).write_text(s)

def author(k):
 if k=='chart-bar':
  css='''/* Inferred from replica17 bare value labels and replica06 quiet capsule fills.
Each data member owns its bar; the complete plot owns the common baseline. */
ROOT{container-type:size;container-name:od-bars;position:relative;display:flex;align-items:stretch;gap:var(--gap-sm);padding:0 3%;min-width:0;min-height:0;--od-bars-n:6;color:var(--ink)}
ROOT::after{content:"";position:absolute;left:3%;right:3%;bottom:40px;height:1px;background:var(--n-4)}
ROOT>.bar{position:relative;flex:1;min-width:0;min-height:0}ROOT>.bar::before{content:"";position:absolute;left:22%;right:22%;bottom:40px;height:calc((100cqh - 80px) * var(--v) / var(--max));background:var(--n-4);border-radius:999px 999px 0 0}
ROOT>.bar>b{position:absolute;left:0;right:0;bottom:calc(44px + (100cqh - 80px)*var(--v)/var(--max));text-align:center;font-size:var(--type-16);font-weight:var(--name-weight);line-height:var(--label-line);letter-spacing:var(--label-track);white-space:nowrap}
ROOT>.bar>span{position:absolute;left:0;right:0;bottom:0;height:32px;display:flex;align-items:flex-start;justify-content:center;text-align:center;font-size:var(--type-14);font-weight:var(--body-weight);line-height:var(--label-line);letter-spacing:var(--body-track);overflow-wrap:anywhere}
ROOT>.bar.on::before,ROOT>.bar.tone-1::before{background:var(--a1)}ROOT>.bar.tone-2::before{background:var(--a2)}ROOT>.bar.tone-3::before{background:var(--a3)}ROOT>.bar.tone-4::before{background:var(--a4)}ROOT>.bar.tone-5::before{background:var(--n-5)}
ROOT.h{flex-direction:column;gap:var(--gap-sm);padding:2% 3%}ROOT.h::after{display:none}ROOT.h>.bar{width:100%;min-height:0}ROOT.h>.bar::before{left:34%;right:auto;top:50%;bottom:auto;transform:translateY(-50%);width:calc(57% * var(--v) / var(--max));height:min(18px,calc((100cqh / var(--od-bars-n))*.4));border-radius:999px}
ROOT.h>.bar>span{left:0;right:auto;top:50%;bottom:auto;transform:translateY(-50%);width:30%;height:auto;text-align:left;justify-content:flex-start;align-items:center}ROOT.h>.bar>b{left:auto;right:0;top:50%;bottom:auto;transform:translateY(-50%);width:8%;text-align:right}
@container od-bars (max-width:600px){ROOT>.bar>b,ROOT>.bar>span{font-size:var(--type-12)}}@container od-bars (max-height:220px){ROOT>.bar>b,ROOT>.bar>span{font-size:var(--type-12)}ROOT.h>.bar>span{font-size:var(--type-12)}}
'''
  css+=''.join(f'ROOT:has(>.bar:nth-child({i}):last-child){{--od-bars-n:{i}}}'for i in range(2,13))
  write(k,'bars',css,'Rounded caps extend the source’s capsule vocabulary into data bars. Quiet neutral members keep one accent bar legible, and labels stay outside the marks. Horizontal bars reserve independent name and value lanes.',[('queue-channels','6x3','<div class="bars" DATA style="--max:300">'+''.join('<div class="bar'+(' on'if i==2 else '')+'" style="--v:'+str(v)+'"><b>'+str(v)+'</b><span>'+n+'</span></div>'for i,(n,v) in enumerate([('온라인 접수',184),('전화 상담',132),('운영 이관',247)]))+'</div>'),('approval-weeks','6x3','<div class="bars" DATA style="--max:80">'+''.join('<div class="bar'+(' on'if i==3 else '')+'" style="--v:'+str(v)+'"><b>'+str(v)+'%</b><span>'+n+'</span></div>'for i,(n,v) in enumerate([('첫째 주',41),('둘째 주',53),('셋째 주',49),('넷째 주',67)]))+'</div>')])
  golden(k)
 elif k=='chart-donut':
  css='''/* Inferred from replica06 ring geometry and replica17 open figure hierarchy.
This contract is one share, unlike the source's unsupported three-way split ring. */
.donuts[data-el="onboard-docket-chart-donut"]{container-type:size;container-name:od-donuts;display:grid;grid-template-columns:repeat(12,minmax(0,1fr));grid-auto-rows:minmax(0,1fr);gap:var(--gap-sm);min-width:0;min-height:0}
.donuts[data-el="onboard-docket-chart-donut"]>.donut{grid-column:span 4}.donuts[data-el="onboard-docket-chart-donut"]:has(>.donut:nth-child(4):last-child)>.donut{grid-column:span 3}
.donut[data-el="onboard-docket-chart-donut"]{container-type:size;container-name:od-donut;display:grid;grid-template-columns:minmax(0,1fr);grid-template-rows:auto auto;align-content:center;justify-items:center;row-gap:var(--gap-sm);min-width:0;min-height:0;color:var(--ink)}
.donut[data-el="onboard-docket-chart-donut"]::before{content:"";grid-column:1;grid-row:1;inline-size:min(70cqw,64cqh,224px);aspect-ratio:1;border-radius:50%;background:conic-gradient(var(--a1) calc(var(--v)*1%),var(--n-2) 0);mask:radial-gradient(circle,transparent 59%,var(--ink) 60%)}
.donut[data-el="onboard-docket-chart-donut"]>.fig{grid-column:1;grid-row:1;align-self:center;margin:0;max-width:50%;font-size:clamp(var(--type-18),calc(12cqw),var(--type-40));font-weight:var(--figure-weight);line-height:var(--figure-line);letter-spacing:var(--figure-track);white-space:nowrap;text-align:center}
.donut[data-el="onboard-docket-chart-donut"]>.fig>small{font-size:var(--type-12);font-weight:var(--body-weight)}.donut[data-el="onboard-docket-chart-donut"]>.name{grid-column:1;grid-row:2;margin:0;max-width:94%;font-size:var(--type-14);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);text-align:center;overflow-wrap:anywhere}
@container od-donuts (max-width:500px){.donuts[data-el="onboard-docket-chart-donut"]>.donut,.donuts[data-el="onboard-docket-chart-donut"]:has(>.donut:nth-child(4):last-child)>.donut{grid-column:span 6}}
@container od-donut (max-height:160px){.donut[data-el="onboard-docket-chart-donut"]>.fig{font-size:var(--type-18)}.donut[data-el="onboard-docket-chart-donut"]>.name{font-size:var(--type-12);line-height:var(--label-line)}}
'''
  write(k,'donut',css,'One measured share occupies a clean ring with an open central figure and a separate caption. The ring derives from replica06 while preserving the semantic distinction between one share and the unsupported three-way annotated ring.',[('handoff-share','4x3','<div class="donut" DATA style="--v:73"><b class="fig">73<small>%</small></b><p class="name">담당 조직 배정까지 완료한 이관 요청</p></div>'),('approval-share','4x3','<div class="donut" DATA style="--v:46"><b class="fig">46<small>%</small></b><p class="name">예외 승인 검토를 마친 배포 요청</p></div>')]);golden(k)
 elif k in ['chart-line','chart-area']:
  area=k=='chart-area';root='areas'if area else'lines';member='.series>'if area else'';base=f'ROOT>{member}.pt'
  if area:
   css='''/* Inferred from replica17 open numbers and replica16 hairline rules.
Filled data intervals share the thin-rule language; all segments belong to one series. */
ROOT{container-type:size;container-name:od-areas;position:relative;display:grid;grid-template-columns:minmax(0,1fr);grid-template-rows:minmax(0,1fr);padding:40px 3% 32px;min-width:0;min-height:0;color:var(--ink)}
ROOT>.series{position:static;anchor-scope:all;grid-column:1;grid-row:1;display:grid;grid-template-columns:repeat(var(--od-points),minmax(0,1fr));grid-template-rows:minmax(0,1fr);min-width:0;min-height:0;--od-points:6}
ROOT>.series>.pt::before{z-index:4}ROOT>.series:nth-child(2)>.pt::before{z-index:3}ROOT>.series:nth-child(3)>.pt::before{z-index:2}ROOT>.series:nth-child(4)>.pt::before{z-index:1}
ROOT>.series>.name{position:absolute;top:6px;left:3%;width:23%;margin:0;font-size:var(--type-12);font-weight:var(--name-weight);line-height:var(--label-line);letter-spacing:var(--body-track);color:var(--a1-7)}ROOT>.series:nth-child(2)>.name{left:27%}ROOT>.series:nth-child(3)>.name{left:51%}ROOT>.series:nth-child(4)>.name{left:75%}
ROOT>.axis{position:absolute;left:3%;right:3%;bottom:0;display:flex;align-items:flex-start;justify-content:space-around;height:26px;font-size:var(--type-12);font-weight:var(--body-weight);line-height:var(--label-line);letter-spacing:var(--body-track);color:var(--n-7)}ROOT>.axis>span{flex:1;text-align:center;white-space:nowrap}
'''
  else:
   css='''/* Inferred from replica17 bare figures, replica16 fine rules and replica15 linked sequences.
The whole plot owns every interval, including flat and declining intervals. */
ROOT{container-type:size;container-name:od-lines;position:relative;anchor-scope:all;display:grid;grid-template-columns:repeat(var(--od-points),minmax(0,1fr));grid-template-rows:minmax(0,1fr);padding:28px 3% 36px;min-width:0;min-height:0;--od-points:6;color:var(--ink)}
'''
  css+=base+'''{position:static;grid-column:var(--od-point-i);grid-row:1;justify-self:center;align-self:start;margin-top:calc(100cqh*(1 - var(--v)/var(--max)));width:0;height:0}
'''
  if area:
   css+=base+'''::before{content:"";position:absolute;left:anchor(var(--od-prev) center);right:anchor(var(--od-self) center);top:calc(anchor(var(--od-prev) center) - 100cqh);bottom:32px;background:var(--a1-2-soft);clip-path:polygon(0 100cqh,100% calc(100% - 100cqh*var(--v)/var(--max)),100% 100%,0 100%)}
'''
  else:
   css+=base+'''::before{content:"";position:absolute;left:anchor(var(--od-prev) center);right:anchor(var(--od-self) center);top:calc(anchor(var(--od-prev) center) - 100cqh);bottom:36px;background:var(--a1-7);clip-path:polygon(0 100cqh,100% calc(100% - 100cqh*var(--v)/var(--max)),100% calc(100% - 100cqh*var(--v)/var(--max) + 2px),0 calc(100cqh + 2px))}
'''
   css+=base+'''::after{content:"";position:absolute;left:calc(anchor(var(--od-self) center) - 3px);top:calc(anchor(var(--od-self) center) - 3px);width:6px;height:6px;border-radius:50%;background:var(--page);border:2px solid var(--a1-7)}
'''+base+'''.on::after{background:var(--a1);width:8px;height:8px;left:calc(anchor(var(--od-self) center) - 4px);top:calc(anchor(var(--od-self) center) - 4px)}
'''+base+'''>span{position:absolute;left:anchor(var(--od-self) center);bottom:0;transform:translateX(-50%);height:28px;font-size:var(--type-12);font-weight:var(--body-weight);line-height:var(--label-line);letter-spacing:var(--body-track);white-space:nowrap;color:var(--n-7)}
'''
  css+=base+'''>b{position:absolute;left:anchor(var(--od-self) center);top:calc(anchor(var(--od-self) center) - 8px);transform:translate(-50%,-100%);font-size:var(--type-12);font-weight:var(--name-weight);line-height:var(--label-line);letter-spacing:var(--label-track);white-space:nowrap;color:var(--ink);background:var(--page);padding:0 2px;z-index:8}
'''
  if area:
   for sn in range(2,5):css+=f'ROOT>.series:nth-child({sn})>.name{{color:var(--a{sn}-7)}}ROOT>.series:nth-child({sn})>.pt::before{{background:var(--a{sn}-2-soft)}}\n'
  for i in range(1,13):
   parent='ROOT>.series' if area else'ROOT';offset=1 if area else 0
   css+=f'{parent}:has(>.pt:nth-child({i+offset}):last-child){{--od-points:{i}}}\n'
   css+=f'{base}:nth-child({i+offset}){{--od-point-i:{i};--od-self:--od-p{i};--od-prev:--od-p{i-1};anchor-name:--od-p{i}}}\n'
  css+=base+(':nth-child(2)'if area else':first-child')+'::before{display:none}\n'
  if not area:
   css+='@container od-lines (max-width:600px){ROOT:has(>.pt:nth-child(10))>.pt:not(:nth-child(3n + 1)):not(:last-child)>span{visibility:hidden}ROOT:has(>.pt:nth-child(10))>.pt:not(:nth-child(2n)):not(:last-child)>b{visibility:hidden}}\n'
  else:css+='@container od-areas (max-width:500px){ROOT:has(>.axis>span:nth-child(10))>.axis>span:not(:nth-child(3n + 1)):not(:last-child){visibility:hidden}}\n'
  def fixture(vals):
   if area:return '<div class="areas" DATA style="--max:100"><div class="series"><b class="name">이관 승인률</b>'+''.join('<div class="pt" style="--v:'+str(v)+'"><b>'+str(v)+'</b></div>'for v in vals)+'</div><div class="axis">'+''.join('<span>'+str(i+1)+'주</span>'for i in range(len(vals)))+'</div></div>'
   return '<div class="lines" DATA style="--max:100">'+''.join('<div class="pt'+(' on'if i==len(vals)-1 else'')+'" style="--v:'+str(v)+'"><b>'+str(v)+'%</b><span>'+str(i+1)+'주</span></div>'for i,v in enumerate(vals))+'</div>'
  write(k,root,css,'Open numeric labels sit above equal time steps. Each interval is built from the actual neighbouring point anchors, so rises, declines and flat values remain continuous without extra data. Fine rules and pale fills extend the source’s measured docket language.',[('weekly-approval','4x3',fixture([38,51,51,47,68,79])),('three-milestones','4x3',fixture([27,49,71]))]);golden(k)
 else:raise SystemExit(k)

if __name__=='__main__':author(sys.argv[1])
