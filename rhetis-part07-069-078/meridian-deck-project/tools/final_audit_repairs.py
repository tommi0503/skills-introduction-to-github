from pathlib import Path
import re
P=Path(__file__).parent;C=P/'meridian-deck'
# Source media remains a flat placeholder; src is an existing foundation class.
for path in list((P/'reassembled').glob('slide_*.html'))+list((C/'foundation/fixtures').glob('source-composition-*.html')):
 s=path.read_text();s=re.sub(r'<section class="slide([^\"]*)"',lambda m:'<section class="slide'+m[1]+' src"' if 'src' not in m[1].split() else m[0],s)
 if path.stem.endswith(('02','03')):s=re.sub(r'(<footer class="foot">).*?(</footer>)',r'\1PRESENTATION\2',s)
 if path.stem.endswith('04'):
  s=s.replace('class="person" data-el="meridian-deck-person" style="grid-column:9 / span 4','class="person" data-el="meridian-deck-person" style="grid-column:8 / span 5')
 path.write_text(s)
def append(n,t):
 f=C/'elements'/n/'element.css';f.write_text(f.read_text()+'\n/* Final immutable audit repairs. */\n'+t+'\n')
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'\n.slide.src .seat[data-ph]::before{content:none}\n')
# Isolate measured CEO portrait from the normal compact profile, retaining source pixel coordinates.
f=C/'elements/person/element.css';s=f.read_text();old='.slide .body>[data-el="meridian-deck-person"].person';new='.slide.src .body>[data-el="meridian-deck-person"].person:has(>.seat.portrait):not(:has(>.list))';s=s.replace(old,new).replace('left:-25px','left:72px').replace('left:143px','left:240px');f.write_text(s)
append('image-frame','.slide.src .split.wide-left>[data-el="meridian-deck-image-frame"].frame{width:100%;max-width:100%}')
h='[data-el="meridian-deck-hub"]:has(>.spoke:nth-child(4 of .spoke):last-child):not(:has(>.core>.seat))'
append('hub','@container (max-height:300px){'+h+'>.spoke{padding:4px;gap:4px}'+h+'>.spoke>.mark{display:block;width:auto;height:22px;flex:none;font-size:var(--type-20);line-height:1.1;color:var(--a1-on)}'+h+'>.spoke>.name{font-size:var(--type-16);line-height:1.2;width:100%}}')
# Compact pyramid labels must fit the widening triangle rather than lose glyph strokes.
p='[data-el="meridian-deck-pyramid"]'
append('pyramid','@container (max-width:650px){'+p+' .level{min-height:0;padding:4px 8px;gap:4px}'+p+' .level>.name{font-size:var(--type-16);line-height:1.2}'+p+' .level>.note{font-size:var(--type-12);line-height:1.2}'+p+' .level:first-child{width:40%;height:45%;flex:0 0 45%;padding-top:8px;padding-bottom:8px;justify-content:flex-end}'+p+' .level:first-child>.name{max-width:70%}'+p+' .level:first-child>.note{max-width:60%}}')
append('agenda','.slide.src [data-el="meridian-deck-agenda"] .entry{padding-top:var(--gap)}')
ca='[data-el="meridian-deck-card"]';sig='.slide.src .body>.group:has(>'+ca+':nth-child(4):last-child)>'+ca+'.card.on:has(.mark)'
append('card',sig+'{padding:0}'+sig+' .parts{padding-left:0;padding-right:0}'+sig+' .mark>.icon{width:72px;height:72px}'+sig+' .name{width:100%;max-width:none;align-self:stretch}'+'.slide.src .group>'+ca+'.card.on:not(:has(.mark,.fig,.kick)):not(.tone-1):not(:last-child)::before{left:calc(100% + 22px);top:125px;width:24px;height:5px}.slide.src .group>'+ca+'.card.on:not(:has(.mark,.fig,.kick)):not(.tone-1):not(:last-child)::after{left:calc(100% + 31.5px);top:116px;width:5px;height:22px}')
m='[data-el="meridian-deck-matrix"].swot:has(>.cell>[data-el="meridian-deck-list"])'
append('matrix','.slide.src '+m+'>.cell:nth-child(1){z-index:4}.slide.src '+m+'>.cell:nth-child(2){z-index:3}.slide.src '+m+'>.cell:nth-child(3){z-index:1}.slide.src '+m+'>.cell:nth-child(4){z-index:2}')
b='[data-el="meridian-deck-chart-bar"]:has(>.bar>span:empty)'
append('chart-bar','.slide.src '+b+'{border-bottom:0}.slide.src '+b+'::after{content:"";position:absolute;left:14px;right:10px;bottom:54px;height:var(--stroke);background:var(--n-4)}')
# Layer correction belongs to the independent replica as well.
f=P/'replica/slide_12.html';s=f.read_text();s=s.replace('transform:rotate(-45deg);border-bottom-right-radius:0','transform:rotate(-45deg);z-index:3;border-bottom-right-radius:0').replace('transform:rotate(135deg);border-bottom-right-radius:0','transform:rotate(135deg);z-index:3;border-bottom-right-radius:0');s=re.sub(r'(left:(?:457|641)px;top:(?:260|445)px;width:184px;font-size:80px;)',r'\1z-index:4;',s);f.write_text(s)
print('Final audit and source-pixel repairs complete')
