from pathlib import Path
P=Path(__file__).parent;E=P/'crossrail/elements'
for leaf in ['radar','swimlane']:
 p=E/leaf/'element.css';s=p.read_text();import re;s=re.sub(r':not\(:has\(~\.(axis|lane)\)\)',lambda m:':nth-last-child(1 of .'+m[1]+')',s)
 if leaf=='radar':
  s=s.replace('position:absolute;left:50%;top:54%;width:min(68cqw,68cqh);height:min(68cqw,68cqh);transform:translate(-50%,-50%);color:var(--a1-7)','position:static;color:var(--a1-7)')
  s=s.replace('position:absolute;inset:0;background:color-mix(in srgb,currentColor 25%,transparent)','position:absolute;left:50%;top:54%;width:min(68cqw,68cqh);height:min(68cqw,68cqh);transform:translate(-50%,-50%);background:color-mix(in srgb,currentColor 25%,transparent)')
  s=s.replace('position:fixed;left:calc(4cqw','position:absolute;left:calc(4cqw')
 p.write_text(s)
p=E/'sankey/element.css';s=p.read_text().replace('padding:var(--gap-sm) 24% var(--gap-sm) 48%;','padding:0;').replace('flex:var(--v) 1 0;min-height:0;','flex:var(--v) 1 0;min-height:0;margin-left:48%;margin-right:24%;').replace('padding:calc(var(--gap-sm)/2);text-align:center','padding:0;text-align:center')
s=s.replace('clip-path:polygon(0 calc(100cqh + 50cqh - anchor(var(--crossrail-branch-anchor) top) - 30cqh*var(--v)/100),100% 100cqh,100% 100%,0 calc(100cqh + 50cqh - anchor(var(--crossrail-branch-anchor) top) + 30cqh*var(--v)/100))','clip-path:polygon(0 calc(100% - 50cqh - 30cqh*var(--v)/100),100% 100cqh,100% calc(100cqh + (100cqh - var(--gap-sm)*(var(--crossrail-flow-count) - 1))*var(--v)/100),0 calc(100% - 50cqh + 30cqh*var(--v)/100))')
for n in range(2,7):s+=f' .sankey[data-el="crossrail-sankey"]:has(>.branch:nth-child({n} of .branch):last-child){{--crossrail-flow-count:{n}}}'
p.write_text(s)
# Sparkline uses precisely the same general polyline construction, with its own compact geometry.
p=E/'sparkline/element.css';s='''/* source/header and measured Crossrail structural language; standalone element scope. */
.sparkline[data-el="crossrail-sparkline"]{box-sizing:border-box;container-type:size;position:relative;display:grid;grid-template-columns:repeat(calc(var(--crossrail-spark-count) - 1),minmax(0,1fr));grid-template-rows:1fr;anchor-scope:all;min-width:0;min-height:0;color:var(--a1-7)}
.sparkline[data-el="crossrail-sparkline"]>span{position:static;grid-column:var(--crossrail-spark-index);grid-row:1;width:0;height:0;align-self:start;justify-self:start;margin-top:calc(100cqh*(1 - var(--v)/var(--max)))}
.sparkline[data-el="crossrail-sparkline"]>span:last-child{grid-column:calc(var(--crossrail-spark-count) - 1);justify-self:end}
.sparkline[data-el="crossrail-sparkline"]>span::before{content:"";position:absolute;left:anchor(var(--crossrail-spark-prev) center);right:anchor(var(--crossrail-spark-self) center);top:calc(anchor(var(--crossrail-spark-prev) center) - 100cqh);bottom:0;background:currentColor;clip-path:polygon(0 100cqh,100% calc(100% - 100cqh*var(--v)/var(--max)),100% calc(100% - 100cqh*var(--v)/var(--max) + 2px),0 calc(100cqh + 2px))}
.sparkline[data-el="crossrail-sparkline"]>span:first-child::before{display:none}
.sparkline[data-el="crossrail-sparkline"].bars{display:flex;align-items:flex-end;gap:calc(var(--gap-sm)/3)}
.sparkline[data-el="crossrail-sparkline"].bars>span{flex:1;position:relative;width:auto;height:calc(var(--v)/var(--max)*100%);background:currentColor;margin:0}
.sparkline[data-el="crossrail-sparkline"].bars>span::before{display:none}
.sparkline[data-el="crossrail-sparkline"].up{color:var(--good)}
.sparkline[data-el="crossrail-sparkline"].down{color:var(--bad)}
'''
for n in range(5,25):s+=f'.sparkline[data-el="crossrail-sparkline"]:has(>span:nth-child({n}):last-child){{--crossrail-spark-count:{n}}}\n'
for i in range(1,25):s+=f'.sparkline[data-el="crossrail-sparkline"]>span:nth-child({i}){{--crossrail-spark-index:{i};anchor-name:--crossrail-spark-{i};--crossrail-spark-self:--crossrail-spark-{i};--crossrail-spark-prev:--crossrail-spark-{max(1,i-1)}}}\n'
p.write_text(s);(E/'sparkline/description.md').write_text('A genuinely continuous compact polyline follows every supplied value, including flat runs. Its bar form replaces the line with discrete columns, while positive and negative trends use semantic state roles.\n')
import json
for leaf,key,val in [('sparkline','--crossrail-spark-count','12'),('sankey','--crossrail-flow-count','3')]:
 p=E/leaf/'element.json';j=json.loads(p.read_text());j['tokenDefaults'][key]=val;p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
