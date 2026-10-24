from pathlib import Path
E=Path(__file__).parent/'meridian-deck/elements'
def add(l,s):
 p=E/l/'element.css';p.write_text(p.read_text()+'\n'+s+'\n')
add('legend','.legend[data-el="meridian-deck-legend"]{padding:0}')
add('list','.list[data-el="meridian-deck-list"]:not(.num):not(.divided){padding:0}@container(max-height:90px){.list[data-el="meridian-deck-list"]:not(.num):not(.divided)>.item{grid-template-columns:var(--gap-sm) minmax(0,1fr);gap:calc(var(--gap-sm)/2)}.list[data-el="meridian-deck-list"]:not(.num):not(.divided)>.item>.name{font-size:var(--type-12)}}')
add('timeline','.track[data-el="meridian-deck-timeline"].alt>.stop:nth-child(odd)>.note{top:78%}')
add('matrix','''.matrix[data-el="meridian-deck-matrix"].swot{isolation:isolate}.matrix[data-el="meridian-deck-matrix"].swot>.cell{isolation:auto}.matrix[data-el="meridian-deck-matrix"].swot>.cell>.kick{isolation:auto;z-index:auto}.matrix[data-el="meridian-deck-matrix"].swot>.cell>.kick::after{content:"";position:absolute;inset:0;rotate:-45deg;background:var(--n-7);clip-path:polygon(75% 75%,100% 75%,100% 100%,75% 100%);z-index:2}.matrix[data-el="meridian-deck-matrix"].swot>.cell:nth-child(2)>.kick::after{rotate:45deg;background:var(--a1)}.matrix[data-el="meridian-deck-matrix"].swot>.cell:nth-child(3)>.kick::after{rotate:-135deg;background:var(--a1)}.matrix[data-el="meridian-deck-matrix"].swot>.cell:nth-child(4)>.kick::after{rotate:135deg}''')
