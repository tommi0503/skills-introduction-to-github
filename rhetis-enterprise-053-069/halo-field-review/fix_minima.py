from pathlib import Path
R=Path(__file__).parent;C=R.parent/'halo-field'
def add(el,s):
 p=C/'elements'/el/'element.css';root=('[data-el="halo-field-'+el+'"]')*3;p.write_text(p.read_text()+'\n'+s.replace('$',root))
# rerun curve overrides with enough specificity; layout algorithm is anchor based and inherits each fixture's values.
s=(R/'refine_collection.py').read_text();s=s.replace("root='[data-el=\"halo-field-'+el+'\"]'", "root='[data-el=\"halo-field-'+el+'\"]'*3");(R/'refine_collection.py').write_text(s)
exec(compile(s,str(R/'refine_collection.py'),'exec'),{'__file__':str(R/'refine_collection.py')})
add('architecture','''$>.layer{padding:var(--gap-sm) var(--gap);gap:var(--gap-sm);min-height:0} $ .name{font-size:var(--type-20)} $ .chip{font-size:var(--type-16);padding:calc(var(--gap-sm)/2)}''')
add('chart-donut','''@container(max-width:120px){$ .fig{font-size:var(--type-20)} $ .name{font-size:var(--type-12);max-width:80%} $ small{font-size:var(--type-12)}}''')
add('chart-scatter','''$>.axis-x{bottom:0;left:40%}''')
add('chart-waterfall','''$>.move>span{top:auto;bottom:calc(var(--gap)*-1.4);font-size:var(--type-14)}''')
add('code','''@container(max-height:360px){$ .lines{font-size:var(--type-16);line-height:var(--label-line)} $ .lines>p{min-height:0}}''')
add('delta','''$ :is(.from,.to){white-space:nowrap} @container(max-width:400px){$ :is(.from,.to){font-size:var(--type-32)}}''')
add('funnel','''$>.stage{padding:calc(var(--gap-sm)/2) var(--gap);gap:calc(var(--gap-sm)/2);min-height:0} $ .name{font-size:var(--type-20)} $ .fig{font-size:var(--type-28)} @container(max-height:350px){$ .name{font-size:var(--type-18)} $ .fig{font-size:var(--type-22)}}''')
add('heatmap','''$.calendar .cell{aspect-ratio:auto;height:100%} $.calendar>.row{max-height:none}''')
add('list','''@container(max-height:360px){$ {gap:var(--gap-sm)} $ .name{font-size:var(--type-18)} $ .note{font-size:var(--type-14)} $.divided>.item+.item{padding-top:var(--gap-sm)}}''')
add('matrix','''$.swot>.cell{padding:var(--gap-sm);gap:calc(var(--gap-sm)/2)} $.swot .list{height:auto;flex:1;gap:calc(var(--gap-sm)/2)} $.swot .list .name{font-size:var(--type-16)} $.swot .list .note{font-size:var(--type-12)} $.swot .kick{font-size:var(--type-18)}''')
add('mindmap','''$>.branch:nth-child(odd):before{left:auto;right:100%}''')
add('radar','''$>.axis{inset:auto;left:calc(50% + cos(calc(var(--halo-field-i)*360deg/var(--n) - 90deg))*38%);top:calc(50% + sin(calc(var(--halo-field-i)*360deg/var(--n) - 90deg))*38%);width:0;height:0;transform:none} $>.axis>.name{left:0;top:0;transform:translate(-50%,-50%);font-size:var(--type-16);white-space:nowrap}''')
for k in range(3,9):
 pts=','.join(f'calc(50% + cos({i*360/k-90}deg)*var(--v{i+1})/var(--max)*50%) calc(50% + sin({i*360/k-90}deg)*var(--v{i+1})/var(--max)*50%)' for i in range(k))
 add('radar',f'$:has(>.axis:nth-child({k} of .axis)):not(:has(>.axis:nth-child({k+1} of .axis)))>.series{{clip-path:polygon({pts})}}')
add('sankey','''@container(max-height:360px){$>.branch{padding:calc(var(--gap-sm)/2) var(--gap-sm)} $ .name{font-size:var(--type-18)} $ .fig{font-size:var(--type-24)}}''')
add('slope','''$ .pair b{font-size:var(--type-20)} $>.pair{min-height:0}''')
add('tag','''$.hl{display:inline;padding:0;font-size:inherit;line-height:inherit;border-radius:0}''')
add('timeline','''$.col>.stop{padding:calc(var(--gap-sm)/2) var(--pad);flex:1;min-height:0} $.col .kick{font-size:var(--type-14);padding:calc(var(--gap-sm)/4) var(--gap-sm);margin-bottom:calc(var(--gap-sm)/2)} $.col .name{font-size:var(--type-20)} $.col .note{font-size:var(--type-14)}''')
add('treemap','''$ .tile{min-width:0;padding:calc(var(--gap-sm)/2)} $ .tile .name{font-size:var(--type-18);overflow-wrap:anywhere}''')
add('waffle','''$>.units{max-height:65%;max-width:440px;width:75%;gap:3px} $>.fig{font-size:var(--type-36)} $>.name{font-size:var(--type-20)} @container(max-height:350px){$>.units{max-width:200px;width:60%} $>.fig{font-size:var(--type-28)} $>.name{font-size:var(--type-18)} $ small{font-size:var(--type-14)}} @container(max-height:80px){$>.units{position:absolute;width:30%;left:0;top:0;bottom:0;max-height:100%;max-width:none;align-items:center} $ .u{max-height:16px} $>.fig{position:absolute;left:33%;top:0;font-size:var(--type-14)} $>.name{position:absolute;left:48%;top:0;font-size:var(--type-12)} $ small{font-size:var(--type-10)}}''')
add('card','''$.tone-1{background:var(--a1-1-soft)} $.tone-2{background:var(--a1-2-soft)} $.tone-3{background:var(--n-1)} $.tone-4{background:var(--n-2)} $.tone-5{background:var(--a1-3-soft)}''')
