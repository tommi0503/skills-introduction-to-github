from pathlib import Path
P=Path(__file__).parent;E=P/'meridian-deck/elements'
f=E/'matrix/element.css';s=f.read_text();start=s.index('.matrix[data-el="meridian-deck-matrix"].swot>.cell>.kick{clip-path:none');s=s[:start]+'''\n.matrix[data-el="meridian-deck-matrix"].swot>.cell>.kick{clip-path:none;width:35%;height:auto;aspect-ratio:1;border-radius:0;background:none;color:var(--page);font-size:clamp(var(--type-40),7cqw,var(--type-88));isolation:isolate}.matrix[data-el="meridian-deck-matrix"].swot>.cell>.kick::before{content:"";position:absolute;inset:0;border-radius:50% 50% 0 50%;rotate:-45deg;background:var(--n-7);z-index:-1}.matrix[data-el="meridian-deck-matrix"].swot>.cell:nth-child(2)>.kick,.matrix[data-el="meridian-deck-matrix"].swot>.cell:nth-child(3)>.kick{background:none;color:var(--a1-on)}.matrix[data-el="meridian-deck-matrix"].swot>.cell:nth-child(2)>.kick::before{rotate:45deg;background:var(--a1)}.matrix[data-el="meridian-deck-matrix"].swot>.cell:nth-child(3)>.kick::before{rotate:-135deg;background:var(--a1)}.matrix[data-el="meridian-deck-matrix"].swot>.cell:nth-child(4)>.kick{background:none;color:var(--page)}.matrix[data-el="meridian-deck-matrix"].swot>.cell:nth-child(4)>.kick::before{rotate:135deg}.matrix[data-el="meridian-deck-matrix"].swot>.cell>.name{color:var(--a1-7);font-size:clamp(var(--type-12),2.2cqw,var(--type-26))}\n''';f.write_text(s)
f=P/'assemble.py';s=f.read_text().replace("+'<div class=\"page\">'+back+header", "+'<div class=\"page\">'+extra+back+header");s=s.replace("+'\"><div class=\"page\">'+back+header", "+'\"><div class=\"page\">'+extra+back+header");s=s.replace("+'<div class=\"page\">'", "+'<div class=\"page\">'")
# Use the exact literal at construction, not a page-dependent stylesheet.
s=s.replace("+'\"><div class=\"page\">'+back+header", "+'\"><div class=\"page\">'+extra+back+header")
s=s.replace("+'<div class=\"page\">'+back", "+'<div class=\"page\">'+extra+back")
s=s.replace("+'\"><div class=\"page\">'+back", "+'\"><div class=\"page\">'+extra+back")
s=s.replace("+'\"><div class=\"page\">'+back", "+'\"><div class=\"page\">'+extra+back")
# Simple source spelling covers the concatenated quote in Python.
s=s.replace("<div class=\"page\">'+back+header", "<div class=\"page\">'+extra+back+header")
f.write_text(s)
