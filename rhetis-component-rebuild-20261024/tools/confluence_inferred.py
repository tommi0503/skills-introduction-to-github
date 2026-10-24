"""Confluence-only inferred material grammar: source03 inset captions, source04 white medallion rims.
These are generated from scratch with each component, never read from another collection CSS.
"""
def signature(leaf):
 roots={'network':'network','cycle':'cycle','matrix':'matrix','matrix-nine':'grid9','pyramid':'pyramid','venn':'venn','radar':'radar','flowchart':'flowchart','swimlane':'swimlane','balance':'balance','concentric':'orbit','metric':'stat','delta':'delta','chart-area':'areas','chart-line':'lines','chart-bar':'bars','chart-stack':'stacks','chart-waterfall':'waterfall','chart-donut':'donut','funnel':'funnel','image-frame':'frame','logo-group':'logos','person':'person','table':'tablebox','quote':'quote','code':'code','roadmap':'roadmap','timeline':'track'}
 if leaf not in roots:return ''
 root='.'+roots[leaf]+'[data-el="confluence-'+leaf+'"]'
 def r(t,b):return ','.join(root+x for x in t.split(','))+'{'+b+'}\n'
 s='\n/* Inferred from replica03 inset caption bands and replica04 white medallion rims. */\n'
 if leaf=='network':s+=r('>.node','border:4px solid var(--page);background:var(--a1-2-soft);color:var(--ink);box-shadow:0 0 0 1px var(--a1);')+r('>.node.on','background:var(--a1-7);color:var(--page);')+r('>.link.strong','background:var(--a2);')
 elif leaf=='cycle':s+=r('>.core','border:clamp(4px,1cqw,12px) solid var(--page);background:var(--a1-7);color:var(--page);')+r('>.node>.name','align-self:stretch;background:var(--a2-7);color:var(--page);border-radius:var(--radius-sm);padding:calc(var(--gap-sm)*.4);')
 elif leaf in ['matrix','matrix-nine']:s+=r('>.cell>.name','align-self:stretch;background:var(--a1-7);color:var(--page);border-radius:var(--radius-sm);padding:calc(var(--gap-sm)*.4) var(--gap-sm);')+r('>.cell.on>.name','background:var(--a2-7);')
 elif leaf=='pyramid':s+=r('>.level','position:relative;background:var(--a1-7);color:var(--ink);')+r('>.level::before','content:"";position:absolute;inset:2px;background:var(--page);clip-path:polygon(10% 0,90% 0,100% 100%,0 100%);')+r('>.level>.name,>.level>.note','position:relative;z-index:1;')+r('>.level>.name','color:var(--a2-7);')
 elif leaf=='venn':s+=r('>.set','border:6px solid var(--page);box-shadow:0 0 0 1px var(--a1);')+r('>.set.on','background:var(--a1-7);color:var(--page);')
 elif leaf=='radar':s+=r('::before','border:6px solid var(--page);box-shadow:0 0 0 1px var(--n-3);background-color:var(--page);')
 elif leaf in ['flowchart','swimlane']:s+=r('>.node.start,>.node.end','border:6px solid var(--page);box-shadow:0 0 0 1px var(--a1);background:var(--a1-7);color:var(--page);')
 elif leaf=='balance':s+=r('>.pan>.name','background:var(--a1-7);color:var(--page);border-radius:var(--radius-sm);padding:calc(var(--gap-sm)*.4);')
 elif leaf=='concentric':s+=r('>.ring','border:6px solid var(--page);box-shadow:0 0 0 1px var(--a1);')+r('>.ring.on','background:var(--a1-7);color:var(--page);')
 elif leaf=='metric':s+=r(' .fig','color:var(--ink);')+r(' .name','color:var(--a1-7);')
 elif leaf=='delta':s+=r('>.from','color:var(--a1-7);')+r('>.to','color:var(--a2-7);')+r('::after','height:0;top:50%;background:none;border-top:var(--stroke) solid var(--a1);')+r('::before','content:"";position:absolute;left:52%;top:calc(50% - 4px);width:8px;height:8px;border-top:var(--stroke) solid var(--a1);border-right:var(--stroke) solid var(--a1);transform:rotate(45deg);')
 elif leaf in ['chart-area','chart-line','chart-bar','chart-stack','chart-waterfall']:s+=r('','background-color:var(--page);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);')
 if leaf=='matrix-nine':s+='@container (max-height:420px){'+r('>.cell>.note','display:none;')+'}\n'
 if leaf=='chart-area':s+=r('>.series>.name:not(:empty)','background:var(--a1-7);color:var(--page);border-radius:var(--radius-sm);padding:calc(var(--gap-sm)*.4);')
 elif leaf=='chart-line':s+=r('>.pt','box-shadow:0 0 0 3px var(--plot-color),0 0 0 5px var(--page);')
 elif leaf=='chart-bar':s+=r('>.bar::before','background:var(--n-3);')+r('>.bar.on::before','background:var(--a1);')
 elif leaf=='chart-donut':s+=r('::after','content:"";position:absolute;left:50%;top:36%;transform:translate(-50%,-50%);width:calc(var(--diameter) + 12px);height:calc(var(--diameter) + 12px);border:6px solid var(--page);border-radius:50%;pointer-events:none;')
 elif leaf=='funnel':s+=r('>.stage','position:relative;background:var(--a1-7);color:var(--ink);')+r('>.stage::before','content:"";position:absolute;inset:2px;background:var(--page);clip-path:polygon(5% 0,95% 0,100% 100%,0 100%);')+r('>.stage>.name,>.stage>.fig','position:relative;z-index:1;')+r('>.stage>.name','color:var(--a1-7);')
 elif leaf=='image-frame':s+=r('','background:var(--page);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);padding:var(--gap-sm);')
 elif leaf=='logo-group':s+=r(':not(.square)>.seat','border-radius:50%;border:4px solid var(--page);box-shadow:0 0 0 1px var(--n-3);')
 elif leaf=='person':s+=r('>.name','align-self:stretch;background:var(--a1-7);color:var(--page);border-radius:var(--radius-sm);padding:calc(var(--gap-sm)*.4);')
 elif leaf=='table':s+=r(' th','background:var(--a1-7);color:var(--page);')
 elif leaf=='quote':s+=r('>blockquote','font-weight:var(--title-weight);')+r('>.by>.name','color:var(--a1-7);')
 elif leaf=='code':s+=r('>.name','background:var(--a1-7);color:var(--page);border-radius:var(--radius-sm);padding:var(--gap-sm);')
 elif leaf=='roadmap':s+=r('>.lane','background:var(--page);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);')
 elif leaf=='timeline':s+=r('>.stop>.kick','background:var(--a1-7);color:var(--page);border-radius:var(--radius-sm);padding:calc(var(--gap-sm)*.4);')+r('>.stop.on>.kick','background:var(--a2-7);color:var(--page);')
 return s
