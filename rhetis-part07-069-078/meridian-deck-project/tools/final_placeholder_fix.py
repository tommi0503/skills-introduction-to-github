from pathlib import Path
P=Path(__file__).parent;C=P/'meridian-deck'
rules={
'image-frame':'.slide.src .body>.group.three:has(>.stack>[data-el="meridian-deck-image-frame"])>.stack>[data-el="meridian-deck-image-frame"]>.seat::before{content:none}',
'person':'.slide.src .body>[data-el="meridian-deck-person"].people:has(>.person:nth-child(4):last-child)>[data-el="meridian-deck-person"].person>.seat.portrait::before{content:none}'
}
for n,r in rules.items():
 f=C/'elements'/n/'element.css';s=f.read_text()
 if r not in s:f.write_text(s+'\n/* Source placeholders stay unlabelled; ordinary library seats retain data-ph. */\n'+r+'\n')
print('Suppressed source-only image-frame and four-person placeholder indices')
