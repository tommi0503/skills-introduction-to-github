from pathlib import Path
from bs4 import BeautifulSoup as B
import json
P=Path(__file__).parent;E=P/'crossrail/elements'
def app(el,s):f=E/el/'element.css';f.write_text(f.read_text()+'\n'+s+'\n')
s='[data-el="crossrail-table"]:not(:has(thead)):has(tr>td:nth-child(4))'
app('table',s+' .table{display:block;transform:translateY(var(--gap))}'+s+' tbody{display:block}'+s+' tr{display:grid;grid-template-columns:calc(var(--gap-lg)*3.05) calc(var(--gap-lg)*7.45) calc(var(--gap-lg)*3.05) minmax(0,1fr)}'+s+' td{display:flex;align-items:center;width:auto!important;height:calc(var(--gap-lg)*1.45)}'+s+' .table::before{top:calc(var(--gap-lg)*-.5);bottom:calc(var(--gap-lg)*-.5)}'+ '@container(max-width:600px){'+s+' tr{grid-template-columns:20% 30% 20% 30%}}')
# Annotation baselines follow the same six-row grid at every allowed chart size.
s='[data-el="crossrail-chart-bar"].quiet:not(.h):has(>.bar:nth-child(2):last-child)>.bar'
app('chart-bar',s+' b{top:calc((100% - var(--gap-sm)*5)/3 + var(--gap-sm)*1.5 + (var(--gap-lg)*1.65 - var(--type-26)*var(--body-line))/2)}')
# A full composed fixture exercises the annotation overlay at its declared full-slide minimum.
f=P/'reassembled/slide_23.html';soup=B(f.read_text(),'html.parser');root=soup.select_one('.body');(E/'chart-bar/fixtures/bars-annotated.html').write_text('<!-- min:12x6 max:12x6 -->\n'+str(root)+'\n')
# Fix source-specific labels and chart units while preserving their palette roles.
s='[data-el="crossrail-card"].quiet.on:has(.parts>.fig):not(:has(.mark,.kick)):first-child'
app('card',s+' .fig{color:var(--n-5)}')
