from pathlib import Path
P=Path(__file__).parent
f=P/'meridian-deck/elements/card/element.css'
r='[data-el="meridian-deck-card"].card.quiet:not(.tone-2):has(.kick):not(:has(.note:not(:empty))):not(:has(.mark)) .kick{color:var(--page)}'
s=f.read_text()
if r not in s:f.write_text(s+'\n/* Final audit: source strategy labels on the dark neutral discs. */\n'+r+'\n')
print('Two strategy kick labels now use page on dark neutral')
