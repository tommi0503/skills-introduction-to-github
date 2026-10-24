"""Refresh evidence metadata only; never change collection, replica or assembly source."""
from pathlib import Path
from lxml import html
from PIL import Image
from collections import Counter
import json
P=Path(__file__).parent;K=P/'crossrail';M=json.loads((P/'map.json').read_text());total=Counter();valid=set();bad=[]
for f in sorted((P/'sheets').glob('*-checks.json')):
 d=json.loads(f.read_text())
 for mode,cells in d['modes'].items():
  for c in cells:
   valid.add(f"{d['leaf']}--{Path(c['fixture']).stem}--{mode}--{c['size'][0]}x{c['size'][1]}.png")
   for key in ['outside','clipped','overlaps','outsideComponent','outsideParts','contrast']:total[key]+=len(c.get(key,[]))
   total['fontFailed']+=sum(not x['loaded'] for x in c['fonts'])
   if any(c.get(key) for key in ['outside','clipped','overlaps','outsideComponent','outsideParts','contrast']):bad.append([d['leaf'],mode,c['fixture'],c['size']])
old=[f for f in (P/'sheet-cells').glob('*.png') if f.name not in valid]
for f in old:f.unlink()
s=json.loads((P/'final-cell-summary.json').read_text());s.update(cells=len(valid),currentNativeCrops=len(valid),totals=dict(total),failures=bad);s['obsoleteGeneratedCropsRemoved']+=len(old);(P/'final-cell-summary.json').write_text(json.dumps(s,indent=2)+'\n')
f=P/'source-fixture-manifest.json';s=json.loads(f.read_text());s['written']=sorted(str(f.relative_to(K)) for f in (K/'elements').glob('*/fixtures/replica-*.html'));s['count']=len(s['written']);f.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
IDENT=json.loads((P/'original-assembly-identities.json').read_text())
placements=[]
for n in range(1,31):
 d=html.fromstring((P/'reassembled'/f'slide_{n:02}.html').read_text());entries=[]
 for root_index,e in enumerate(d.xpath('//div[@class="body"]/*[@data-el]')):
  ids=[IDENT[str(n)][root_index]]
  entries.append({'dataEl':e.get('data-el'),'classes':e.get('class'),'gridStyle':e.get('style'),'mapIds':ids})
 placements.append({'page':n,'placements':entries,'gaps':[i['id'] for i in M['instances'] if i['page']==n and i['use']=='unexpressible']})
(P/'assembly-placement.json').write_text(json.dumps(placements,ensure_ascii=False,indent=2)+'\n')
Image.MAX_IMAGE_PIXELS=None;png={}
for folder,expected in [('replica',(1280,720)),('reassembled',(1280,720)),('compare-reassembled',(3840,720)),('sheets',None),('sheet-cells',None)]:
 sizes=Counter()
 for f in (P/folder).glob('*.png'):
  with Image.open(f) as im:sz=im.size;im.verify()
  if expected:assert sz==expected,(f,sz)
  sizes[str(sz)]+=1
 png[folder]={'count':sum(sizes.values()),'dimensions':dict(sizes),'allPNGDecoded':True}
(P/'png-validation.json').write_text(json.dumps(png,indent=2)+'\n')
v=json.loads((P/'visual-review.json').read_text());v['focusedNativeFinal']=[x for x in v['focusedNativeFinal'] if not x.startswith('list/replica-18')];v['focusedNativeFinal']+=['prose/replica-18-left-strengths-2/3x1/light','prose/replica-18-right-strengths-4/3x1/dark','matrix-nine/base-a/9x6/light'];v['taxonomyCorrection']='Single paragraph fixtures use prose; original standalone bullet glyphs are explicit marked-prose gaps. The nine-grid basic fixture has both required axes.';(P/'visual-review.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
print('cells',len(valid),'total',dict(total),'removed',len(old),'map',len(M['instances']),'gaps',sum(i['use']=='unexpressible' for i in M['instances']))
