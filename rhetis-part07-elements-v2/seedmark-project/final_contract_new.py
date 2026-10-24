def apply(D):
 # Thin labels according to meaningful labelled members, not the raw index of paired bars.
 D['chart-bar']=D['chart-bar'].replace('$ .bar:nth-child(even):not(:last-child)>span{visibility:hidden;}','')
 D['chart-bar']+='\n@container(max-width:450px){$ .bar:nth-child(even of .bar:has(>span:not(:empty))):not(:last-child)>span{visibility:hidden;}$.h .bar>span{visibility:visible;}}'
 D['chart-donut']=D['chart-donut'].replace('$.donut>.name{max-width:', '$.donut>.name{width:min(72cqw,64cqh);max-width:')
 D['card']+='''
$ .parts:has(>.list){height:100%;align-self:center;display:grid;grid-template-columns:minmax(0,1fr);grid-template-rows:20px 56px minmax(0,1fr) min(80px,26cqh);align-content:stretch;gap:var(--gap-sm);}
$ .parts:has(>.list)>.kick{grid-column:1;grid-row:1;}
$ .parts:has(>.list)>.name{grid-column:1;grid-row:2;border-bottom:var(--stroke) solid var(--n-3);}
$ .parts:has(>.list)>.note{grid-column:1;grid-row:3;align-self:start;}
$ .parts>.list{grid-column:1;grid-row:4;width:100%;height:100%;align-self:end;}
'''
