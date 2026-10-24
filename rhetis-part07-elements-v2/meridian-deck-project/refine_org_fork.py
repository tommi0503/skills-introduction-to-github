from pathlib import Path
p=Path(__file__).parent/'meridian-deck/elements/hierarchy/element.css'
s='''
/* A branch owns its node and every leaf; parallel leaves must share one fork. */
.org[data-el="meridian-deck-hierarchy"]:has(>.branch>.leaf)>.branch:has(>.leaf:nth-child(3)){anchor-scope:all;isolation:isolate}
.org[data-el="meridian-deck-hierarchy"]:has(>.branch>.leaf)>.branch:has(>.leaf:nth-child(3))>.node{position:relative;anchor-name:--meridian-deck-org-node}
.org[data-el="meridian-deck-hierarchy"]:has(>.branch>.leaf)>.branch:has(>.leaf:nth-child(3))>.node::after{content:"";position:absolute;left:100%;top:calc(var(--gap-sm)*-1);height:calc(50% + var(--gap-sm));width:var(--stroke);background:var(--n-5)}
.org[data-el="meridian-deck-hierarchy"]:has(>.branch>.leaf)>.branch:has(>.leaf:nth-child(3))>.leaf{position:static}
.org[data-el="meridian-deck-hierarchy"]:has(>.branch>.leaf)>.branch:has(>.leaf:nth-child(3))>.leaf::before{content:"";position:absolute;left:anchor(--meridian-deck-org-node right);right:anchor(var(--meridian-deck-org-leaf) center);top:calc(anchor(--meridian-deck-org-node top) - var(--gap-sm));bottom:calc(100% - anchor(var(--meridian-deck-org-leaf) top));width:auto;height:auto;background:none;border-top:var(--stroke) solid var(--n-5);border-right:var(--stroke) solid var(--n-5);z-index:-1}
.org[data-el="meridian-deck-hierarchy"]:has(>.branch>.leaf)>.branch:has(>.leaf:nth-child(3))>.leaf::after{content:"";position:absolute;left:calc(anchor(var(--meridian-deck-org-leaf) center) - 4px);top:calc(anchor(var(--meridian-deck-org-leaf) top) - 8px);width:8px;height:8px;border:0;background:var(--n-5);clip-path:polygon(0 0,50% 65%,100% 0,100% 35%,50% 100%,0 35%);rotate:0deg}
'''
for i in range(1,4): s+=f'.org[data-el="meridian-deck-hierarchy"]:has(>.branch>.leaf)>.branch:has(>.leaf:nth-child(3))>.leaf:nth-child({i} of .leaf){{--meridian-deck-org-leaf:--meridian-deck-org-leaf-{i};anchor-name:--meridian-deck-org-leaf-{i}}}\n'
p.write_text(p.read_text()+s)
