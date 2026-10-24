from pathlib import Path
E=Path(__file__).parent/'meridian-deck/elements'
def add(l,s):
 f=E/l/'element.css';f.write_text(f.read_text()+'\n'+s+'\n')
add('hub','.hub[data-el="meridian-deck-hub"]:has(>.spoke:nth-child(4 of .spoke):last-child)>.spoke>.note{width:208%;left:-208%;font-size:clamp(var(--type-10),1.15cqw,var(--type-14))}.hub[data-el="meridian-deck-hub"]:has(>.spoke:nth-child(4 of .spoke):last-child)>.spoke:nth-child(even of .spoke)>.note{left:100%}')
add('image-frame','.frame[data-el="meridian-deck-image-frame"]::after{left:calc(min(9cqw,15cqh)*.5);top:calc(min(9cqw,15cqh)*.5);translate:-50% -50%}')
