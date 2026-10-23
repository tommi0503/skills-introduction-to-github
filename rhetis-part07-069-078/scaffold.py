"""Contract-only scaffold. Copies fixture markup/data, NEVER sample CSS or descriptions.
Usage: python scaffold.py /absolute/project/collection collection-id
"""
from pathlib import Path
import sys,json,re
REF=Path('/workspace/work/reference') if Path('/workspace/work/reference').exists() else Path(__file__).resolve().parent/'reference'
GOLD={
'card':('confetti','card-2-quiet card-3-icon3d card-3-line card-3-on card-4 card-5-tone'.split()),
'callout':('annual','callout callout-icon callout-stack'.split()),
'chart-area':('annual','area-1 areas-2 areas-stacked-3 area-3pt'.split()),
'chart-bar':('confetti','bars-12 bars-6 bars-3 bars-h-5 bars-h-8 bars-2'.split()),
'chart-donut':('amethyst','donut donuts-3 donuts-4 donut-0 donut-100'.split()),
'chart-line':('amethyst','lines-12 lines-6 lines-3 lines-flat'.split())}
def scaffold(dst,kid):
 dst=Path(dst); provenance={}
 for c in json.loads((REF/'contract/taxonomy.json').read_text())['contracts']:
  name=c['category'].split('.')[-1];out=dst/'elements'/name;fix=out/'fixtures';fix.mkdir(parents=True,exist_ok=True)
  (out/'element.json').write_text(json.dumps({'schema':'rhetis.design-library-element-source/1','contract':c['id'],'registrations':{},'tokenDefaults':{}},indent=2)+'\n')
  if name in GOLD:
   sample,names=GOLD[name];sources=[REF/'samples'/sample/'elements'/name/'fixtures'/(n+'.html') for n in names]
  else:
   sources=sorted((REF/'samples/annual/elements'/name/'fixtures').glob('*.html'))
   if len(sources)<2:
    extra=sorted((REF/'samples/confetti/elements'/name/'fixtures').glob('*.html'))
    for p in extra:
     if p.name not in [x.name for x in sources]:sources.append(p)
     if len(sources)>=2:break
  assert len(sources)>=2,name
  provenance[name]=[]
  for p in sources:
   text=p.read_text();text=re.sub(r'data-el="(?:annual|confetti|amethyst)-','data-el="'+kid+'-',text)
   (fix/p.name).write_text(text)
   provenance[name].append(str(p.relative_to(REF)))
 (dst/'foundation/fixtures').mkdir(parents=True,exist_ok=True)
 (dst/'foundation/foundation.json').write_text(json.dumps({'schema':'rhetis.design-library-foundation-source/1','kit':kid,'registrations':{},'tokenDefaults':{}},indent=2)+'\n')
 (dst/'kit/css').mkdir(parents=True,exist_ok=True)
 (dst/'kit/kit.json').write_text(json.dumps({'schema':'rhetis.kit/2','id':kid,'label':kid.replace('-',' ').title(),'tokens':'css/tokens.css','description':'description.md','extensions':{}},indent=2)+'\n')
 (dst.parent/'fixture-provenance.json').write_text(json.dumps(provenance,indent=2,ensure_ascii=False)+'\n')
 print(kid,len(provenance),'elements',sum(len(x) for x in provenance.values()),'fixtures')
if __name__=='__main__':scaffold(*sys.argv[1:])
