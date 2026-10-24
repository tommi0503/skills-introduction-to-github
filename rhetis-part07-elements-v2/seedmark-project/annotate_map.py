from pathlib import Path
import json
P=Path(__file__).parent;a=json.loads((P/'map.json').read_text())
for page in [13,14,20]:
 inst=next(x for x in a['instances']if x['page']==page and x['leaf']=='chart-bar') if page!=20 else None
 raw=next(p for p in a['rawMeasurements']if p['page']==page)
 legends=[]
 for n in raw['nodes']:
  for k,q in enumerate(n['primitives']):
   if q['tag']=='text'and q['text'] in ['타사','MIRI COMPANY']:legends.append((n,k,q))
 if not legends:continue
 x=min(q['bbox'][0]for _,_,q in legends)-14;y=min(q['bbox'][1]for _,_,q in legends);r=max(q['bbox'][0]+q['bbox'][2]for _,_,q in legends);b=max(q['bbox'][1]+q['bbox'][3]for _,_,q in legends)
 a['instances'].append({'id':f'sm-{page:02}-legend','page':page,'leaf':'legend','use':'base','bbox':[x,y,r-x,b-y],'fixture':f'elements/legend/fixtures/replica-{page:02}-legend.html','selectors':[f'{n["selector"]} svg > :nth-child({k+1})'for n,k,q in legends],'sourceMeasurements':[q for _,_,q in legends],'ownershipNote':'These legend texts and adjacent swatches are excluded from chart-bar ownership; the chart owns only plotted bars and axes.'})
 for it in a['instances']:
  if it['page']==page and it['leaf'] in ['chart-bar','card']:it['excludeLegend']=True
(P/'map.json').write_text(json.dumps(a,ensure_ascii=False,indent=2))
proposals={
'venn':'<div class="venn line"><div class="set"><span class="mark"></span><p class="name"></p><p class="note"></p></div></div> — add explicit .line variant and mark/note set parts.',
'pill':'<div class="stores"><div class="store"><p class="name"></p></div></div> — new database-store contract, not a pill variant inferred from an icon name.',
'chart-line':'<div class="lines"><div class="annotation" style="--at:3"><span>BEP</span></div></div> — explicit chart annotation slot and data index.',
'timeline':'<div class="track"><div class="bands"><div class="bar" style="--from:0;--to:1"><span></span></div></div><div class="stop">…</div></div> — explicit owned duration bands.',
'network':'<div class="network"><div class="node" style="--x:20;--y:10;--w:40;--h:20"><p class="name"></p></div></div> — explicit node footprints in graph coordinates; this is a requested contract addition, not an implemented geometry extension.',
'chart-stack':'<div class="stacks pct h"><div class="sbar"><span></span><div class="seg" style="--v:40"><b>40%</b></div>…</div></div> — extend the sbar count lower bound from 2 to 1.',
'chart-donut':'<div class="pie"><div class="share" style="--v:40"><p class="fig"></p><p class="name"></p></div>…</div> — new multi-share pie root with automatic cumulative angles.'}
gaps=[i for i in a['instances']if i['use']=='unexpressible'];(P/'GAPS.md').write_text('# Unexpressible source components\n\n'+'\n\n'.join(f'## {i["id"]}: page {i["page"]}, {i["leaf"]}\n\nMeasured bbox `{i["bbox"]}`. {i["why"]}\n\nRequired contract markup:\n\n```html\n{proposals[i["leaf"]]}\n```'for i in gaps)+'\n')
print(len(a['instances']),'instances; 7 gaps with proposed markup')
