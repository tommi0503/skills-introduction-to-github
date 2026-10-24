def timeline_css():
 return '''
${display:grid;grid-template-columns:repeat(var(--seedmark-count),minmax(0,1fr));gap:var(--gap-sm);padding:var(--gap-sm) 0 var(--gap);isolation:isolate;}
$:before{content:'';position:absolute;left:0;right:0;bottom:calc(var(--gap-sm)/2);height:var(--stroke);background:var(--n-3);z-index:-1;}
$ .stop{position:relative;container-type:size;min-width:0;min-height:0;display:grid;grid-template-rows:33% 20% minmax(0,1fr);gap:var(--gap-sm);border-left:var(--stroke) solid var(--n-3);padding-left:calc(var(--gap-sm)*.833333);padding-right:calc(var(--gap-sm)/6);}
$ .stop:before{content:'';position:absolute;left:0;bottom:calc(var(--gap-sm)*-1.5);width:var(--stroke);height:var(--gap-sm);background:var(--ink);}
$ .kick{grid-row:2;display:flex;align-items:center;justify-content:center;font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line);}
$ .name{grid-row:1;display:flex;align-items:center;justify-content:center;font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);}
$ .name>[data-el]{width:100%;height:100%;}
$ .note{grid-row:3;font-size:var(--type-18);line-height:var(--body-line);}
$ .stop.on .kick{background:var(--ink);color:var(--page);border-radius:var(--radius-sm);padding:calc(var(--gap-sm)/2);}
$.col{grid-template-columns:1fr;grid-auto-rows:minmax(0,1fr);}
$.col:before{top:var(--gap);bottom:var(--gap);left:calc(var(--gap-sm)/2);width:var(--stroke);height:auto;}
$.col .stop{border-left:0;grid-template-columns:25% minmax(0,1fr);grid-template-rows:auto auto;padding-left:var(--gap);}
$.col .stop:before{left:calc(var(--gap-sm)/-2);top:50%;bottom:auto;width:7px;height:7px;border-radius:50%;}
$.col .kick{grid-column:1;grid-row:1/span 2;align-items:center;}
$.col .name{grid-column:2;grid-row:1;justify-content:flex-start;}
$.col .note{grid-column:2;grid-row:2;}
$.alt .stop:nth-child(even){grid-template-rows:minmax(0,1fr) 20% 33%;}
$.alt .stop:nth-child(even) .note{grid-row:1;align-self:end;}$.alt .stop:nth-child(even) .name{grid-row:3;}
@container(max-width:700px){$ .name{font-size:var(--type-18)}$ .note{font-size:var(--type-14)}$ .kick{font-size:var(--type-12)}}
'''+''.join(f'$:has(>.stop:nth-child({n} of .stop):last-child){{--seedmark-count:{n};}}'for n in range(2,13))
