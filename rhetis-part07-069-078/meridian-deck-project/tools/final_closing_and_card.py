from pathlib import Path
import json,re
P=Path(__file__).parent;C=P/'meridian-deck'
f=C/'elements/card/element.css';q='.slide.src .body>.group:has(>[data-el="meridian-deck-card"]:nth-child(4):last-child)>[data-el="meridian-deck-card"].card.on:has(.mark)';f.write_text(f.read_text()+'\n'+q+'{padding:calc(var(--gap-lg) + var(--stroke)*2) 0 0}'+q+' .parts{grid-template-columns:100%;justify-content:stretch}'+q+' .name{border-bottom:0}'+q+'::after{content:"";position:absolute;left:0;right:0;top:247px;height:var(--stroke);background:var(--n-4)}\n')
f=C/'foundation/foundation.json';j=json.loads(f.read_text());j['tokenDefaults']['--meridian-deck-closing-ink']='var(--ink)';f.write_text(json.dumps(j,ensure_ascii=False,indent=2))
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'\n.slide.cover .lockup.at-center .title{color:var(--meridian-deck-closing-ink)}\n')
f=P/'assets/source-palette.css';f.write_text(f.read_text()+'\n.slide.src{--meridian-deck-closing-ink:#595959}\n')
f=P/'assets/source-defaults.css';f.write_text(f.read_text()+'\n.slide{--meridian-deck-closing-ink:var(--ink)}\n')
f=P/'replica/slide_28.html';s=f.read_text();count=[0]
def chevron(m):
 count[0]+=1;txt=m[0]
 if count[0]<4:return txt.replace('top:227px"','top:227px;overflow:visible"').replace('0,0 270,0 285,22 270,44 0,44 15,22','0,0 280,0 295,22 280,44 0,44 15,22')
 return txt.replace('width="285"','width="275"').replace('viewBox="0 0 285 44"','viewBox="0 0 275 44"').replace('0,0 270,0 285,22 270,44 0,44 15,22','0,0 260,0 275,22 260,44 0,44 15,22')
s=re.sub(r'<svg class="shape" style="left:\d+px;top:227px"[^>]*>.*?</svg>',chevron,s);f.write_text(s)
print('Preserved source9 vertical geometry/full rules, closing gray and joined replica28')
