from pathlib import Path
P=Path(__file__).parent;C=P/'meridian-deck'
f=C/'elements/table/element.css';f.write_text(f.read_text()+'\n.slide.src [data-el="meridian-deck-table"]:has(th:first-child:empty) tbody tr:nth-child(-n+3) td:first-child{background:var(--a1-1-muted)}\n')
f=C/'elements/card/element.css';f.write_text(f.read_text()+'\n.slide.src [data-el="meridian-deck-card"].card.line:has(.kick) .kick{background:var(--a1-2-muted)}\n')
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'\n.slide.src .body>.deco.on{background:var(--a1-2-muted)}\n')
f=P/'assets/source-palette.css';f.write_text(f.read_text()+'\n.slide.src{--a1-1-muted:#e5edfa;--a1-2-muted:#cfe1fa}\n')
f=C/'elements/delta/element.css';q='.slide.src .body>.stack>.group>[data-el="meridian-deck-delta"]:has(>.from:empty)';f.write_text(f.read_text()+'\n'+q+'{background:none;clip-path:none}'+q+'::before{background:linear-gradient(to right,transparent,var(--a1-4-muted))}\n')
f=P/'replica/slide_20.html';s=f.read_text();s=s.replace('<polygon points="0,20 71,20 71,0 107,37 71,75 71,55 0,55" fill="#87b1f6"/>','<defs><linearGradient id="arrowfade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#87b1f6" stop-opacity="0"/><stop offset="1" stop-color="#87b1f6"/></linearGradient></defs><polygon points="0,20 71,20 71,0 107,37 71,75 71,55 0,55" fill="url(#arrowfade)"/>');f.write_text(s)
print('Source-only pale tints and full-length arrow fades restored')
