from pathlib import Path
import re,json
p=Path(__file__).parent;c=p/'crossrail'
f=c/'elements/chart-donut/element.json';d=json.loads(f.read_text());d['tokenDefaults'].update({'--crossrail-donut-start':'0deg','--crossrail-donut-track':'var(--n-3)','--crossrail-donut-fill':'var(--a1-7)','--crossrail-donut-hole':.56,'--crossrail-donut-hole-fill':'var(--page)','--crossrail-donut-diameter':'min(calc(100cqw - var(--gap-sm)*2),calc(100cqh - var(--gap-sm)*2))','--crossrail-donut-cx':'50%','--crossrail-donut-cy':'50%','--crossrail-donut-value-radius':'0px','--crossrail-donut-name-x':'0px','--crossrail-donut-name-y':'32px','--crossrail-donut-name-size':'var(--type-22)','--crossrail-donut-value-size':'var(--type-52)','--crossrail-donut-value-y':'0px','--crossrail-donut-line-x':'0px','--crossrail-donut-line-y':'0px','--crossrail-donut-line-w':'0px','--crossrail-donut-leg-w':'0px','--crossrail-donut-leg-angle':'0deg'});f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
s='[data-el="crossrail-chart-donut"].donut'
css=f'''\n/* Each root remains a one-share donut. Multiple roots may share a chart cell. */
{s}::before{{left:var(--crossrail-donut-cx);top:var(--crossrail-donut-cy);width:var(--crossrail-donut-diameter);height:var(--crossrail-donut-diameter);background:conic-gradient(from var(--crossrail-donut-start),var(--crossrail-donut-fill) calc(var(--v)*1%),var(--crossrail-donut-track) 0)}}
{s}::after{{left:var(--crossrail-donut-cx);top:var(--crossrail-donut-cy);width:calc(var(--crossrail-donut-diameter)*var(--crossrail-donut-hole));height:calc(var(--crossrail-donut-diameter)*var(--crossrail-donut-hole));background:var(--crossrail-donut-hole-fill)}}
{s} .fig{{position:absolute;left:calc(var(--crossrail-donut-cx) + sin(calc(var(--crossrail-donut-start) + var(--v)*1.8deg))*var(--crossrail-donut-value-radius));top:calc(var(--crossrail-donut-cy) - cos(calc(var(--crossrail-donut-start) + var(--v)*1.8deg))*var(--crossrail-donut-value-radius) + var(--crossrail-donut-value-y));transform:translate(-50%,-50%);font-size:var(--crossrail-donut-value-size)}}
{s} .name{{position:absolute;left:calc(var(--crossrail-donut-cx) + var(--crossrail-donut-name-x));top:calc(var(--crossrail-donut-cy) + var(--crossrail-donut-name-y));margin:0;width:max-content;max-width:70%;font-size:var(--crossrail-donut-name-size);line-height:var(--name-line);text-align:left}}
{s} .name::before{{content:"";position:absolute;left:var(--crossrail-donut-line-x);top:var(--crossrail-donut-line-y);width:var(--crossrail-donut-line-w);height:2px;background:var(--n-3)}}
{s} .name::after{{content:"";position:absolute;left:var(--crossrail-donut-line-x);top:var(--crossrail-donut-line-y);width:var(--crossrail-donut-leg-w);height:2px;background:var(--n-3);transform-origin:left center;transform:rotate(var(--crossrail-donut-leg-angle))}}
'''
# Composite roots have numeric figures without a unit. Ordinary percent donuts retain their center typography.
css+=f'''{s}:not(:has(.fig small)) .fig{{font-weight:var(--body-weight);color:var(--page);-webkit-text-stroke:.5px var(--ink);paint-order:stroke fill}}{s} .name:has(small){{transform:translateX(-50%);text-align:center}}{s} .name>small{{display:block;color:var(--n-5);font-size:var(--type-18);margin-top:var(--gap-sm)}}'''
f=c/'elements/chart-donut/element.css';f.write_text(f.read_text()+css+'\n')
# Source chart geometry is chart data. Page placement remains exclusively grid-column/grid-row.
base={'--crossrail-donut-track':'transparent','--crossrail-donut-hole':.6,'--crossrail-donut-hole-fill':'var(--n-1)','--crossrail-donut-diameter':'336px','--crossrail-donut-cx':'55%','--crossrail-donut-cy':'42%','--crossrail-donut-value-radius':'140px','--crossrail-donut-value-size':'var(--type-18)','--crossrail-donut-name-size':'var(--type-18)'}
def donut(v,name,start,fill,dx,dy,lx,ly,lw,leg,angle):
 vals=base|{'--v':v,'--crossrail-donut-start':str(start)+'deg','--crossrail-donut-fill':fill,'--crossrail-donut-name-x':str(dx)+'px','--crossrail-donut-name-y':str(dy)+'px','--crossrail-donut-line-x':str(lx)+'px','--crossrail-donut-line-y':str(ly)+'px','--crossrail-donut-line-w':str(lw)+'px','--crossrail-donut-leg-w':str(leg)+'px','--crossrail-donut-leg-angle':str(angle)+'deg'}
 sty='grid-column:7 / span 6;grid-row:1 / span 6;'+''.join(k+':'+str(v)+';' for k,v in vals.items())
 return '<div class="donut" data-el="crossrail-chart-donut" style="'+sty+'"><p class="fig">'+str(v)+'</p><p class="name">'+name+'</p></div>'
parts=[donut(20,'북미',0,'var(--a1-3)',208,-164,-53,23,87,44,114),donut(25,'남미',72,'var(--a1-4)',171,165,-65,27,109,57,-114),donut(15,'유럽',162,'var(--a1-5)',-181,165,-25,27,93,0,0),donut(10,'아시아',216,'var(--a1-6)',-253,112,0,28,91,0,0),donut(30,'아프리카',252,'var(--a1-7)',-269,-146,0,24,107,0,0)]
# The hole caption is an independent one-share root with zero share and transparent track.
v=base|{'--v':0,'--crossrail-donut-fill':'transparent','--crossrail-donut-value-radius':'0px','--crossrail-donut-value-y':'24px','--crossrail-donut-name-x':'0px','--crossrail-donut-name-y':'-26px','--crossrail-donut-name-size':'var(--type-26)'}
parts.append('<div class="donut" data-el="crossrail-chart-donut" style="grid-column:7 / span 6;grid-row:1 / span 6;'+''.join(k+':'+str(x)+';' for k,x in v.items())+'"><p class="fig"></p><p class="name">글로벌 매출<small>Global</small></p></div>')
f=p/'reassembled/slide_24.html';h=f.read_text();h=re.sub(r'<div class="donut " data-el="crossrail-chart-donut".*?</div>',lambda m:''.join(parts),h)
h=h.replace('원 그래프와 유사하지만 중앙 공간 활용도가 높아 정보 전달과 디자인을 동시에 잡을 수 있는 레이아웃입니다. 그래프 옆이나 하단에는 데이터가 시사하는 핵심 내용을 요약해 적어주세요.','원 그래프와 유사하지만 중앙 공간 활용도가 높아 정보 전달과 디자인을 동시에 잡을 수 있는 레이아웃입니다. 그래프 옆이나 하단에는 데이터가 시사하는 핵심 내용을 요약해 적어주세요. 그래프에서 도출된 결론을 텍스트로 보완하면 읽는 이에게 더욱 강력한 설득력을 줍니다.')
f.write_text(h)
# Refresh the external tokenDefaults provider without changing the source collection data.
f=p/'assets/source-defaults.css';h=f.read_text();h+='\n.slide{'+''.join(k+':'+str(v)+';' for k,v in d['tokenDefaults'].items())+'}\n';f.write_text(h)
print('source 24 composite 5-share chart restored')
