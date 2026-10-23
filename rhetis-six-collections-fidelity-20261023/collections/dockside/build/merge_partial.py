from pathlib import Path
import json,fitz
R=Path('/workspace/work/deliverables/dockside');V=R/'review';L=V/'library'
old=json.loads((R/'build/audit-library-complete.json').read_text());new=json.loads((V/'audit-library.json').read_text());folders=set(x['folder'] for x in new)
for mode in ['light','dark']:
 baseline=[x for x in old if x['mode']==mode and x['fixture'].endswith('· 12×6')]
 previous=fitz.open(L/f'library-{mode}.pdf');replacement=fitz.open(L/f'partial-{mode}.pdf');merged=fitz.open();j=0
 for i,x in enumerate(baseline):
  if x['folder'] in folders:merged.insert_pdf(replacement,from_page=j,to_page=j);j+=1
  else:merged.insert_pdf(previous,from_page=i,to_page=i)
 assert j==len(replacement)
 tmp=L/f'merged-{mode}.pdf';merged.save(tmp,deflate=True);previous.close();replacement.close();merged.close();tmp.replace(L/f'library-{mode}.pdf');(L/f'partial-{mode}.pdf').unlink()
lookup={(x['mode'],x['folder'],x['fixture']):x for x in new}
report=[lookup.get((x['mode'],x['folder'],x['fixture']),x) for x in old]
(V/'audit-library.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print('Merged',len(report),'probes;',len(new),'updated probes')
