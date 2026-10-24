from pathlib import Path
import re
P=Path(__file__).parent;E=P/'meridian-deck/elements'
f=E/'card/element.css';s=f.read_text().replace('.card[data-el="meridian-deck-card"].line>.parts:has(>.kick)>.name:not(:empty)+.note','.card[data-el="meridian-deck-card"].line:not(:has(>.parts>.mark))>.parts:has(>.kick)>.name:not(:empty)+.note');f.write_text(s)
f=E/'list/element.css';s=f.read_text()+'''\n.list[data-el="meridian-deck-list"].divided:not(.num)>.item{grid-template-rows:minmax(0,1fr);align-content:stretch}.list[data-el="meridian-deck-list"]>.item>.note:empty{display:none}.list[data-el="meridian-deck-list"]>.item:has(>.note:empty){row-gap:0}@container(max-height:180px){.list[data-el="meridian-deck-list"]>.item>.name{font-size:var(--type-14)}.list[data-el="meridian-deck-list"]>.item{padding:0}}\n''';f.write_text(s)
f=E/'tag/element.css';s=f.read_text().replace('display:inline-flex;vertical-align:middle','display:inline;vertical-align:middle').replace(';container-type:normal','');f.write_text(s)
f=E/'cycle/element.css';s=f.read_text()+'''\n.cycle[data-el="meridian-deck-cycle"]>.core{font-size:clamp(var(--type-12),min(2.8cqw,6cqh),var(--type-30))}.cycle[data-el="meridian-deck-cycle"]>.node{padding:calc(var(--gap-sm)/2)}.cycle[data-el="meridian-deck-cycle"]>.node>.name{font-size:clamp(var(--type-12),min(2cqw,5cqh),var(--type-24))}.cycle[data-el="meridian-deck-cycle"]>.node>.note{font-size:clamp(var(--type-10),min(1.4cqw,4cqh),var(--type-16))}\n''';f.write_text(s)
f=E/'venn/element.css';s=f.read_text()+'''\n.venn[data-el="meridian-deck-venn"]>.set+.set{margin-left:calc(min(55cqw,85cqh)*-.26)}.venn[data-el="meridian-deck-venn"]:has(>.set:nth-child(3 of .set))>.set+.set{margin-left:calc(min(42cqw,80cqh)*-.26)}\n''';f.write_text(s)
f=E/'pill/element.css';s=f.read_text()+'''\n.pill[data-el="meridian-deck-pill"]>.parts{white-space:nowrap}.pill[data-el="meridian-deck-pill"]>.parts>.name,.pill[data-el="meridian-deck-pill"]>.parts>.note{white-space:nowrap}\n''';f.write_text(s)
f=E/'pill/fixtures/replica-24.html';f.write_text(f.read_text().replace('<!-- min: 6x2 -->','<!-- min: 12x1 -->'))
# Preserve unlabelled source trend points and the measured SVG y scale after fresh-copy generation.
for f in [E/'chart-line/fixtures/replica-17.html',E/'card/fixtures/replica-17.html']:
 s=f.read_text();vs=[[20,35,61],[25,65,80],[30,36,69]];i=[0]
 def patch(m):
  v=vs[i[0]%3];i[0]+=1;return m[0].replace('--max:100','--max:'+str(max(v)*1.25),1)
 s=re.sub(r'<div class="lines"[^>]*>',patch,s);s=re.sub(r'(<div class="pt"[^>]*>)<b>\d+</b>',r'\1<b></b>',s);f.write_text(s)
print('Corrected actual component bounds, circular safe text and one-line capsule minima')
