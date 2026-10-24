"""Emit all56 complete new element files; never append a CSS patch layer."""
import re
import remaining_new as R
N=R.N;D=N.CSS
D['code']=D['code'].replace('padding:var(--pad);','padding:var(--gap-sm);')
D['timeline']=D['timeline'].replace('$ .stop{position:relative;', '$ .stop{container-type:size;position:relative;')
D['timeline']+='\n$ .name:has(>[data-el]){height:33.33cqh;min-height:0;display:block;container-type:size;}\n$ .name>[data-el]{width:100%;height:100%;}\n'
D['flowchart']=D['flowchart'].replace('$ .node>*{max-width:100%;max-height:100%;}', '$ .node>*{max-width:100%;max-height:100%;}\n$ .node>[data-el]{width:100%;height:100%;}')
D['radar']+='\n'+'\n'.join(f'$:has(>.series:nth-child({n} of .series)):not(:has(>.series:nth-child({n+1} of .series))){{--seedmark-series-count:{n};}}'for n in range(1,4))
for i in range(1,4):D['radar']+=f'$ .series:nth-child({i} of .series)>.name{{left:calc(({i}-1)*100%/var(--seedmark-series-count));max-width:calc(100%/var(--seedmark-series-count) - var(--gap-sm));}}\n'
from line_geometry import line_css,spark_css
D['chart-line']=line_css();D['sparkline']=spark_css()
# All direct-member count selectors use the filtered member index, not the index including headings/cores.
for leaf,part in [('timeline','stop'),('cycle','node'),('hub','spoke'),('pyramid','level'),('hierarchy','branch'),('logo-group','seat'),('heatmap','row'),('sankey','branch'),('journey','stage'),('mindmap','branch')]:
 D[leaf]=re.sub(r'(>\.'+part+r':nth-child\()(\d+)(\):last-child)',lambda m:m.group(1)+m.group(2)+' of .'+part+m.group(3),D[leaf])
for k,v in list(D.items()):
 v=v.replace(')-',') - ').replace(')+',') + ')
 v=v.replace('1-var(', '1 - var(').replace('1-max(', '1 - max(').replace('100%-','100% - ')
 v=v.replace('}.col ', '}$.col ').replace('}.dumbbell ', '}$.dumbbell ')
 D[k]=v
D['steps']=D['steps'].replace('$ .step{position:relative;', '$ .step{container-type:size;position:relative;').replace('width:60px;height:60px;', 'width:min(60px,80cqw);height:min(60px,80cqw);').replace('width:48px;height:48px;', 'width:min(48px,80cqw);height:min(48px,80cqw);')
D['person']=D['person'].replace('gap:calc(var(--gap-sm)/2);text-align:center;padding:var(--gap-sm);','gap:calc(var(--gap-sm)/3);text-align:center;padding:var(--gap-sm) 0;')
D['person']=D['person'].replace('width:min(95cqw,52cqh);height:min(95cqw,52cqh);','width:min(100cqw,100cqh - var(--pad)*4.10625);height:min(100cqw,100cqh - var(--pad)*4.10625);')
D['person']=D['person'].replace('height:min(118cqw,52cqh);','height:min(125cqw,100cqh - var(--pad)*4.10625);')
D['person']=D['person'].replace('$ .person>.list{width:100%;min-height:0;}', '$ .person>.list{width:100%;min-height:0;height:62px;flex:none;}')
D['person']=D['person'].replace('$.person>.list{width:100%;min-height:0;}', '$.person>.list{width:100%;min-height:0;height:62px;flex:none;}')
D['list']=D['list'].replace('gap:var(--gap-sm);padding:var(--gap-sm);counter-reset:item;', 'gap:calc(var(--gap-sm)/2);padding:calc(var(--gap-sm)/2);counter-reset:item;')
D['list']+='\n$ .item>.note:empty{display:none;}\n'
D['card']+='\n$.quiet:has(>.parts>.mark):not(:has(>.parts>.kick)) .parts{padding:var(--gap-sm);grid-template-columns:1fr;grid-template-rows:auto auto;align-content:center;justify-items:center;gap:calc(var(--gap-sm)/3);text-align:center;}\n$.quiet .parts:has(>.mark):not(:has(>.kick))>.mark{width:min(54px,45cqw,45cqh);height:min(54px,45cqw,45cqh);background:none;color:var(--ink);}\n$.quiet .parts:has(>.mark):not(:has(>.kick))>.mark .icon{width:100%;height:100%;}\n$.quiet .parts:has(>.mark):not(:has(>.kick))>.name{font-size:var(--type-12);font-weight:var(--label-weight);line-height:var(--label-line);border-radius:var(--radius-sm);background:var(--ink);color:var(--page);padding:calc(var(--gap-sm)/4) calc(var(--gap-sm)/2);}\n'
from pill_new import pill_css
D['pill']=pill_css()
D['headline']+='\n$.big .note{font-size:var(--type-28);line-height:var(--lead-line);}'
D['prose']=D['prose'].replace('$.lead p{font-size:var(--type-28);', '$.lead p{font-size:clamp(var(--type-18),min(24cqw,65cqh),var(--type-28));')
D['prose']=D['prose'].replace('$.lead p{font-size:var(--type-24)}', '$.lead p{font-size:clamp(var(--type-18),min(24cqw,65cqh),var(--type-28));}').replace('$.lead p{font-size:var(--type-20)}', '$.lead p{font-size:clamp(var(--type-18),min(24cqw,65cqh),var(--type-28));}')
D['card']=D['card'].replace('min-aspect-ratio:2.5/1','min-aspect-ratio:2/1').replace('max-height:180px','max-height:140px').replace('width:min(54px,18cqw,18cqh);height:min(54px,18cqw,18cqh);','width:min(54px,45cqw,45cqh);height:min(54px,45cqw,45cqh);')
D['card']+='\n$ .parts>.note:empty{display:none;}\n@container(min-aspect-ratio:2/1){$ .parts>.note{font-size:var(--type-16);}}\n$.quiet:has(>.parts>.kick):not(:has(>.parts>.mark,>.parts>.fig,>.parts>.list)):before{background:var(--page);border:0;border-bottom:var(--stroke) solid var(--n-3);border-radius:0;}\n$.quiet .parts:has(>.kick):not(:has(>.mark,>.fig,>.list)){padding:0;display:grid;grid-template-columns:38% minmax(0,1fr);grid-template-rows:24px auto;gap:calc(var(--gap-sm)/2) var(--gap-sm);align-content:center;}\n$.quiet .parts:has(>.kick):not(:has(>.mark,>.fig,>.list))>.kick{grid-column:1;grid-row:1;}\n$.quiet .parts:has(>.kick):not(:has(>.mark,>.fig,>.list))>.name{grid-column:1;grid-row:2;font-size:var(--type-28);}\n$.quiet .parts:has(>.kick):not(:has(>.mark,>.fig,>.list))>.note{grid-column:2;grid-row:1/span 2;font-size:var(--type-16);align-self:center;}\n'
D['card']=D['card'].replace('padding:var(--gap-sm);grid-template-columns:1fr;grid-template-rows:auto auto;', 'padding:var(--gap-sm) calc(var(--gap-sm)/2) 0;grid-template-columns:1fr;grid-template-rows:auto auto;')
D['chart-donut']=D['chart-donut'].replace('border:1px solid var(--ink);border-radius:var(--radius-sm);padding:calc(var(--gap-sm)/4) calc(var(--gap-sm)/2);background:var(--page);color:var(--ink);', 'border:0;padding:0;color:var(--ink);')
D['chart-donut']+='\n$.donuts{isolation:isolate;}\n$.donuts:before{content:"";position:absolute;left:10%;right:10%;top:50%;height:var(--stroke);background:var(--n-3);z-index:-3;}\n'
D['flowchart']+='\n$ .node:has(>[data-el]){border:0;background:none;padding:0;}\n'
D['chart-area']+='\n$ .pt:after{content:"";position:absolute;left:anchor(var(--seedmark-prev) center);right:anchor(var(--seedmark-self) center);top:calc(anchor(var(--seedmark-prev) top) - (100cqh - var(--pad) - var(--gap-lg) - var(--gap-sm)));bottom:0;background:var(--ink);clip-path:polygon(0 calc(100cqh - var(--pad) - var(--gap-lg) - var(--gap-sm)),100% calc(100% - (100cqh - var(--pad) - var(--gap-lg) - var(--gap-sm))*var(--v)/var(--max)),100% calc(100% - (100cqh - var(--pad) - var(--gap-lg) - var(--gap-sm))*var(--v)/var(--max) + 2px),0 calc(100cqh - var(--pad) - var(--gap-lg) - var(--gap-sm) + 2px));}\n$ .pt:first-of-type:after{display:none;}\n$ .pt>b:after{content:"";position:absolute;left:50%;bottom:-3px;width:6px;height:6px;transform:translateX(-50%);background:var(--ink);border-radius:50%;}\n'
from timeline_new import timeline_css
D['timeline']=timeline_css()
D['headline']+="\n$.big h2{font-size:clamp(var(--type-36),min(14.22cqw,29cqh),var(--type-64));}"
D['card']+="\n$ .parts:has(>.bars){grid-template-rows:auto auto minmax(0,1fr);align-content:stretch;}\n$ .parts:has(>.bars)>.name{grid-row:1;font-size:var(--type-24);}\n$ .parts:has(>.bars)>.kick{grid-row:2;}\n$ .parts>.bars{grid-row:3;width:100%;height:100%;min-height:0;}"
from corrections_new import apply
apply(D)
from topology_new import apply as topology
topology(D)
from final_geometry_new import apply as geometry
geometry(D)
from sequence_new import apply as sequence
sequence(D)
from finish_source_new import apply as source_finish
source_finish(D)
from final_contract_new import apply as contract_finish
contract_finish(D)
from actual_copy_response_new import apply as actual_copy
actual_copy(D)
from contract_review_new import apply as review_contract
review_contract(D)
assert not any(re.search(r"var\(--[\w-]+\s+-",v)for v in D.values())
N.emit()
import describe
print('Wrote',len(D),'whole new CSS files.')
