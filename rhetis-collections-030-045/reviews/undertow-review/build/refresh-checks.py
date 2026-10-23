from pathlib import Path
from PIL import Image
import json,hashlib,shutil
C=Path('/workspace/work/deliverables/undertow');R=Path('/workspace/work/deliverables/undertow-review')
p=R/'automatic-checks.json';d=json.loads(p.read_text())
lib=json.loads((R/'library/checks.json').read_text());decks=sum([json.loads((R/f'{n}/checks.json').read_text()) for n in ['replica','reassembled']],[])
d['all_loaded_fonts']=all(x['font'] for x in decks) and all(x['full']['font'] for x in lib)
d['deck_sizes_1280x720']=all(x['size']==[1280,720] for x in decks)
d['deck_text_scroll_candidates']=sum(len(x['overflow']) for x in decks)
d['library_min_mid_full_scroll_candidates']=[{'mode':x['mode'],'title':x['title'],'sizes':[s for s in x['sizes'] if s['overflow']]} for x in lib if any(s['overflow'] for s in x['sizes'])]
d['intentional_shape_label_scroll_candidates']=[{'mode':x['mode'],'title':x['title'],'errors':x['full']['errors']} for x in lib if x['full']['errors']]
pngs=sorted(R.rglob('*.png'));d['png_count']=len(pngs);d['png_dimensions']={str(p.relative_to(R)):list(Image.open(p).size) for p in pngs}
d['collection_source_sha256']={str(p.relative_to(C)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(C.rglob('*')) if p.is_file()}
align=json.loads((R/'library/alignment-checks.json').read_text());d['capsule_alignment']=[{'mode':x['mode'],'count':len(x['items']),'candidates':[i for i in x['items'] if abs(i['dx'])>3 or abs(i['dy'])>3]} for x in align]
d['collection_file_extensions']=sorted({p.suffix for p in C.rglob('*') if p.is_file()})
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
for n in ['refresh-checks.py','alignment.js']:
 shutil.copy(Path('/workspace/work/agents/031')/n,R/'build'/n)
print(json.dumps({k:d[k] for k in ['png_count','all_loaded_fonts','deck_sizes_1280x720','deck_text_scroll_candidates','library_min_mid_full_scroll_candidates','capsule_alignment','collection_file_extensions']},ensure_ascii=False))
print('full intentional',[(x['mode'],x['title']) for x in d['intentional_shape_label_scroll_candidates']])
