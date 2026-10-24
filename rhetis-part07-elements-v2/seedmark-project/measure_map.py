from pathlib import Path
import asyncio,json,re
from playwright.async_api import async_playwright
P=Path(__file__).parent
# Each module owns its surface, text, icon and local divider. Connections are assigned to the full topology owner.
S={
1:[('foundation',[0,1,2,3,4,5,6],'base',None)],
2:[('headline',[2,3,4],'variant:big',None),('agenda',list(range(5,41)),'base',None)],
3:[('prose',[5],'base',None),('tag',[6],'base',None),('prose',[7],'variant:quiet',None),('steps',list(range(8,19)),'variant:col',None)],
4:[('venn',list(range(5,17)),'unexpressible','The source has outline-only circles, an elongated centre set and icon/name/note parts. venn.sets has no line variant and no mark/note slots; the single base is the filled three-set overlap on page16.')],
5:[('card',list(range(k,k+7)),'variant:line'if k==11 else'base',None)for k in[4,11,18]],
6:[('flowchart',list(range(5,26)),'base',None)],
7:[('headline',[3],'base',None),('concentric',list(range(4,10)),'base',None)]+[('metric',list(range(k,k+4)),'base',None)for k in[10,14,18]]+[('foundation',[22],'base',None)],
8:[('chart-donut',list(range(5,12)),'base',None),('card',list(range(12,16)),'variant:quiet',None),('card',list(range(16,20)),'variant:quiet',None)],
9:[('flowchart',[5,6,7,8,9]+list(range(16,37))+[38],'base',None),('pill',list(range(10,16)),'unexpressible','Three cylindrical stores require a database/store shape with top ellipse, side wall and attached label. pill.parts is a one-line capsule; changing it into a cylinder would be a second design without a contract variant.'),('callout',[37],'base',None)],
10:[('card',list(range(k,k+6)),'variant:line'if k==23 else'base',None)for k in[5,11,17,23]],
11:[('steps',list(range(5,30)),'base',None)]+[('card',list(range(k,k+5)),'variant:quiet',None)for k in[30,35,40]],
12:[('card',list(range(5,9)),'variant:quiet',None),('card',list(range(9,13)),'variant:quiet',None),('headline',[13],'variant:center',None),('flowchart',list(range(14,23)),'base',None)],
13:[('metric',list(range(k,k+4)),'base',None)for k in[5,9,13]]+[('headline',[17],'base',None),('chart-bar',[18],'base',None),('prose',[19],'variant:quiet',None),('prose',[20],'variant:lead',None)],
14:[('headline',[k],'base',None)for k in[5,6,7]]+[('chart-area',[8],'base',None),('chart-line',[9],'base',None),('chart-bar',[10,11],'base',None)]+[('prose',[k],'base',None)for k in[12,13,14]]+[('chart-line',[15],'unexpressible','A labelled BEP guide at a chosen x value is an annotation; chart.line has only data points and no annotation/target part.'),('tag',[16],'base',None)],
15:[('headline',[3],'base',None),('positioning',list(range(4,17)),'base',None),('list',list(range(17,30)),'variant:divided',None)],
16:[('card',list(range(k,k+4)),'variant:quiet',None)for k in[5,9,13]]+[('venn',list(range(17,22)),'base',None)]+[('tag',[k],'base',None)for k in[22,23,24]],
17:[('timeline',list(range(5,20))+[23,24,25,26],'base',None),('timeline',[20,21,22],'unexpressible','Three duration bands span one/two/two stops. timeline.stop owns a single date, and sibling/empty-date inference is forbidden. A band with from/to period data is required.')],
18:[('prose',[5],'variant:lead',None),('prose',[6],'base',None),('tag',[7],'base',None),('tag',[8],'base',None),('network',list(range(9,32)),'unexpressible','The topology is expressible as network positions/links, but its nodes require independently sized 249x69,94x138,94x47 and267x70 footprints. network.node has position data only and no footprint field. No page geometry token is introduced.')],
19:[('person',list(range(k,k+4)),'base',None)for k in[5,9,13,17,21]]+[('foundation',[25],'base',None)],
20:[('pill',[5,6],'variant:on',None),('pill',[7,8,9],'variant:line',None),('card',[10,12,13,20],'base',None),('card',[11,14,15,21,22,23],'base',None),('chart-stack',[16,17,18,19],'unexpressible','A single four-part allocation bar is not chart.stack: its contract requires 2–12 sbar members. Adding an empty second row would falsify the data.')],
21:[('metric',[5,6,7,17],'base',None),('metric',[8,9,10],'base',None),('metric',[11,12,13,18],'base',None),('metric',[14,15,16],'base',None),('chart-donut',list(range(19,28)),'unexpressible','A four-share pie is not a one-share donut or a row of donuts. The contract has no pie/sector/start-angle form, and overlaying four whole donuts would misrepresent their semantics.')]
}
async def main():
 raw=[];instances=[]
 async with async_playwright()as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);g=await b.new_page(viewport={'width':1280,'height':720})
  for i in range(1,22):
   await g.goto(f'http://127.0.0.1:8792/replica/slide_{i:02}.html');await g.evaluate('document.fonts.ready')
   nodes=await g.evaluate('''()=>[...document.querySelector('main').children].map((e,index)=>{const B=q=>{let r=q.getBoundingClientRect();return[r.x,r.y,r.width,r.height].map(v=>+v.toFixed(3))},s=getComputedStyle(e);return{index,selector:`main > :nth-child(${index+1})`,bbox:B(e),text:e.innerText||e.textContent,fontSize:s.fontSize,lineHeight:s.lineHeight,fontWeight:s.fontWeight,letterSpacing:s.letterSpacing,classes:e.className,html:e.outerHTML,primitives:[...e.querySelectorAll('svg>*')].map(q=>({tag:q.tagName,bbox:B(q),text:q.textContent,source:q.outerHTML}))}})''')
   raw.append({'page':i,'size':[1280,720],'fontLoaded':await g.evaluate('document.fonts.check(\'18px Noto\')'),'nodes':nodes})
   owned=set()
   specs=S[i]
   if i!=1:
    furniture=[j for j in range(min(5,len(nodes)))if j not in {n for _,ids,_,_ in specs for n in ids}]
    if furniture:specs=[('foundation',furniture,'base',None)]+specs
   for q,(leaf,ids,use,why)in enumerate(specs):
    ids=[n for n in ids if n<len(nodes)];owned.update(ids)
    x=min(nodes[n]['bbox'][0]for n in ids);y=min(nodes[n]['bbox'][1]for n in ids);r=max(nodes[n]['bbox'][0]+nodes[n]['bbox'][2]for n in ids);bb=max(nodes[n]['bbox'][1]+nodes[n]['bbox'][3]for n in ids)
    inst={'id':f'sm-{i:02}-{q:02}','page':i,'leaf':leaf,'use':use,'bbox':[round(x,3),round(y,3),round(r-x,3),round(bb-y,3)],'fixture':f'elements/{leaf}/fixtures/replica-{i:02}-{q:02}.html'if leaf!='foundation'and use!='unexpressible'else None,'selectors':[nodes[n]['selector']for n in ids],'sourceMeasurements':[{k:v for k,v in nodes[n].items()if k!='html'}for n in ids]}
    if why:inst['why']=why
    instances.append(inst)
   for n in set(range(len(nodes)))-owned:
    node=nodes[n];instances.append({'id':f'sm-{i:02}-extra-{n}','page':i,'leaf':'foundation'if not node['text'].strip()else'prose','use':'base','bbox':node['bbox'],'selectors':[node['selector']],'sourceMeasurements':[node],'fixture':None})
  await b.close()
 out={'schema':'rhetis.source-map/2','collection':'seedmark','coordinateSpace':{'width':1280,'height':720,'units':'CSS px'},'readme':'Read fully 2026-10-24; latest user restrictions take precedence.','instances':instances,'coverage':{'pages':21,'topLevelNodes':sum(len(p['nodes'])for p in raw),'allTopLevelNodesAssigned':True},'rawMeasurements':raw}
 (P/'map.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));gaps=[x for x in instances if x['use']=='unexpressible'];(P/'GAPS.md').write_text('# Unexpressible source components\n\n'+'\n\n'.join(f'## {x["id"]}: page {x["page"]}, {x["leaf"]}\n\nBBox `{x["bbox"]}`. {x["why"]}'for x in gaps)+'\n')
 print('map:',len(instances),'instances',sum(len(p['nodes'])for p in raw),'source nodes,',len(gaps),'gaps')
asyncio.run(main())
