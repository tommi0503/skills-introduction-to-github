from pathlib import Path
import json
import fidelity_tail_patch as m
P=Path(__file__).parent;C=P/'meridian-deck'
for n,t in m.ELEMENT_PATCHES.items():
 f=C/'elements'/n/'element.css';s=f.read_text();marker='/* TAIL RESTORATION */';s=s.split(marker)[0];f.write_text(s+'\n'+marker+'\n'+t)
f=C/'foundation/foundation.css';marker='/* TAIL RESTORATION */';f.write_text(f.read_text().split(marker)[0]+'\n'+marker+'\n'+m.FOUNDATION_PATCH)
f=C/'foundation/foundation.json';j=json.loads(f.read_text());j['tokenDefaults'].update(m.TOKEN_DEFAULTS);f.write_text(json.dumps(j,ensure_ascii=False,indent=2))
f=C/'kit/css/tokens.css';f.write_text(f.read_text()+'\n.slide{'+''.join(k+':'+v+';' for k,v in m.TOKEN_DEFAULTS.items())+'}\n')
for name,t in m.FIXTURES.items():
 f=C/name;f.parent.mkdir(exist_ok=True,parents=True);f.write_text(t)
f=P/'assets/source-palette.css';f.write_text(f.read_text()+'\n.slide{--a1-1-soft:#deefff;--a1-2-soft:#b9defc;--a1-4-muted:#78a6df}\n')
print('Merged tail',len(m.ELEMENT_PATCHES),len(m.FIXTURES))
