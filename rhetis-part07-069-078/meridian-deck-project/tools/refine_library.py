from pathlib import Path
P=Path(__file__).parent;C=P/'meridian-deck';E=C/'elements'
def append(e,s):
 p=E/e/'element.css';p.write_text(p.read_text()+'\n/* Meridian review pass 2: intrinsic geometry and compact content. */\n'+s.replace('@',f'[data-el="meridian-deck-{e}"]'))
append('radar','@{width:100%;height:100%;aspect-ratio:auto;max-height:none;margin:0}@ .series>.name{clip-path:none}@ .axis .name{font-size:var(--type-16);white-space:nowrap}')
append('concentric','@{width:100%;height:100%;aspect-ratio:auto;max-height:none;margin:0}')
append('card','@ .parts{display:grid;grid-template-rows:auto minmax(0,1fr) auto minmax(0,1fr);align-items:start;justify-items:center;width:100%;height:90%;gap:var(--gap-sm)}@ .kick{grid-row:1;align-self:end}@ .mark,@ .fig{grid-row:2;align-self:end}@ .name{grid-row:3;min-height:calc(var(--type-24)*var(--name-line)*2);font-size:var(--type-24)}@ .note{grid-row:4;align-self:start}@ .mark{width:96px;height:96px}')
p=E/'card/element.css';s=p.read_text();s+='\n@container (max-width:300px){[data-el="meridian-deck-card"] .mark{width:72px;height:72px}[data-el="meridian-deck-card"] .name{font-size:var(--type-20);min-height:calc(var(--type-20)*var(--name-line)*2)}}\n@container (max-height:200px){[data-el="meridian-deck-card"] .mark{width:48px;height:48px}[data-el="meridian-deck-card"] .name{font-size:var(--type-16);min-height:calc(var(--type-16)*var(--name-line)*2)}}';p.write_text(s)
append('person','@.people{height:100%}@.person{height:100%;overflow:visible}@ .seat{flex:0 1 auto;max-height:52%}')
append('hub','@ .core>.icon{width:48px;height:48px}')
append('timeline','@ .kick{flex:none}')
p=E/'timeline/element.css';p.write_text(p.read_text()+'\n@container (max-height:280px){[data-el="meridian-deck-timeline"] .kick{width:64px;height:64px;font-size:var(--type-18)}[data-el="meridian-deck-timeline"] .stop{padding:calc(var(--gap-sm)/2);gap:calc(var(--gap-sm)/2)}[data-el="meridian-deck-timeline"] .name{font-size:var(--type-16)}[data-el="meridian-deck-timeline"] .note{font-size:var(--type-12)}}')
for e,mem in [('hierarchy','branch'),('sankey','branch')]:
 s=''
 for n in range(2,7):
  if e=='hierarchy':s+=f'@:has(>.{mem}:nth-child({n} of .{mem}):last-child)'+'{'+f'grid-template-columns:repeat({n},minmax(0,1fr));'+'}'
  else:s+=f'@:has(>.{mem}:nth-child({n} of .{mem}):last-child)'+'{'+f'grid-template-rows:repeat({n},minmax(0,1fr));'+'}'
 append(e,s)
f=C/'foundation/foundation.css';s=f.read_text();s+='\nbody:has(>.slide){margin:0;width:1280px;height:720px}\n';f.write_text(s)
r=P/'build_reassembled.py';s=r.read_text().replace("'../../assets/fonts/fonts.css'","'../assets/fonts/fonts.css'");r.write_text(s)
print('Pass2 geometry/spacing fixes applied')
