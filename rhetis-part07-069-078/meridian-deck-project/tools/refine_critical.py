from pathlib import Path
P=Path(__file__).parent;C=P/'meridian-deck';E=C/'elements'
f=C/'foundation/foundation.css';f.write_text(f.read_text().replace('.slide .cover','.slide.cover'))
def add(e,s):
 p=E/e/'element.css';p.write_text(p.read_text()+'\n/* Critical integration: flex-basis and root cover matching. */\n'+s.replace('@',f'[data-el="meridian-deck-{e}"]'))
add('pill','@.pill{container-type:inline-size}.group>@.pill{flex:1 1 0;min-width:0}@.pill .name{font-size:var(--type-18);line-height:var(--name-line)}')
p=E/'pill/element.css';p.write_text(p.read_text()+'\n@container (max-width:520px){[data-el="meridian-deck-pill"] .name{font-size:var(--type-14)}}')
add('image-frame','@ .seat{width:min(100cqw,100cqh);height:min(100cqw,100cqh);aspect-ratio:1;flex:none}')
p=E/'prose/element.css';p.write_text(p.read_text()+'\n@container (max-height:160px){[data-el="meridian-deck-prose"]{padding:var(--gap-sm)}[data-el="meridian-deck-prose"] p{font-size:var(--type-14);line-height:var(--body-line)}}')
p=E/'headline/element.css';p.write_text(p.read_text()+'\n@container (max-height:200px){[data-el="meridian-deck-headline"]{padding:var(--gap-sm)}[data-el="meridian-deck-headline"] h2{font-size:var(--type-24)}[data-el="meridian-deck-headline"] .note{font-size:var(--type-14)}}\n@container (max-width:700px){[data-el="meridian-deck-headline"].big h2{font-size:var(--type-36)}}')
r=P/'build_reassembled.py';s=r.read_text();s=s.replace("stack([pill('제목을 입력하세요',note,True),pill('이곳에 제목을 입력하세요',note,False),pill('제목을 입력하세요',note,True)])", "ls(['제목을 입력하세요','이곳에 제목을 입력하세요','제목을 입력하세요'],[note]*3,'divided')")
r.write_text(s)
print('Critical cover/flex/short-slot fixes applied')
p=E/'card/element.css';p.write_text(p.read_text()+'\n@container (max-height:250px){[data-el="meridian-deck-card"].card:has(.mark)::before{top:0;bottom:0}[data-el="meridian-deck-card"].card:has(.mark) .mark{width:48px;height:48px}[data-el="meridian-deck-card"].card:has(.mark) .name{font-size:var(--type-18);padding:calc(var(--gap-sm)/2) 0}[data-el="meridian-deck-card"].card:has(.mark) .note{font-size:var(--type-12);padding-top:0}}')
