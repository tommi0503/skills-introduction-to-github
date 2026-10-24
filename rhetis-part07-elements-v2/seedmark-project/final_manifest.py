from pathlib import Path
from PIL import Image
import json,hashlib,importlib.util,datetime
P=Path(__file__).parent;K=P/'seedmark'
hashf=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def tree(folder,suffix=None):return {str(p.relative_to(P)):hashf(p)for p in sorted(folder.rglob('*'))if p.is_file()and(suffix is None or p.suffix in suffix)}
spec=importlib.util.spec_from_file_location('sheets',P.parent/'tools/sheets.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
cols=['outside','clipped','overlaps','contrast','outsideComponent','outsideParts'];aggregate={c:0 for c in cols};leafs={};badfonts=[]
for f in sorted((P/'sheets').glob('*-checks.json')):
 d=json.loads(f.read_text());expected=m.fingerprint(P,'seedmark',d['leaf']); assert expected==d['sourceFingerprint'],d['leaf'];assert d['rendererVersion']=='v2-grid-paint-font-parts-1'
 sums={c:0 for c in cols};n=0
 for mode,cs in d['modes'].items():
  for c in cs:
   n+=1
   for key in cols:sums[key]+=len(c.get(key,[]))
   for ft in c.get('fonts',[]):
    if not ft.get('declared')or not ft.get('loaded'):badfonts.append([d['leaf'],mode,c['fixture'],ft])
 for key in cols:aggregate[key]+=sums[key]
 leafs[d['leaf']]={'fingerprint':expected,'cells':n,'candidateCounts':sums,'checkSHA256':hashf(f)}
assert len(leafs)==56 and not any(aggregate.values())and not badfonts
pngs={}
for folder in ['replica','reassembled','compare-reassembled','sheets','sheet-cells','visual-review']:
 ps={}
 for f in sorted((P/folder).glob('*.png')):
  with Image.open(f)as im:ps[f.name]=list(im.size)
 pngs[folder]=ps
assert len(pngs['replica'])==21 and len(pngs['reassembled'])==21
assert all(v==[1280,720]for v in pngs['replica'].values())and all(v==[1280,720]for v in pngs['reassembled'].values())
assert len(pngs['compare-reassembled'])==21 and all(v==[3840,720]for v in pngs['compare-reassembled'].values())
rep=tree(P/'replica');old=Path('/workspace/work/rhetis-part07/seedmark-project/replica');comparison={f:{'sha256':sha,'unchangedFromFrozenOriginal':(old/Path(f).relative_to('replica')).exists()and hashf(old/Path(f).relative_to('replica'))==sha}for f,sha in rep.items()};assert all(d['unchangedFromFrozenOriginal']for d in comparison.values());(P/'replica-integrity.json').write_text(json.dumps(comparison,indent=2))
assembly=json.loads((P/'reassembly-checks.json').read_text());assert all(page['sourceFingerprint']==m.fingerprint(P,'seedmark')for page in assembly['pages']);aps={p['page']:{c:len(p.get(c,[]))for c in cols}for p in assembly['pages']}
assert len(aps)==21 and all(p['root']==[0,0,1280,720]for p in assembly['pages'])
audit=json.loads((P/'source-contract-audit.json').read_text());mp=json.loads((P/'map.json').read_text());files=tree(K);treehash=hashlib.sha256(json.dumps(files,sort_keys=True).encode()).hexdigest()
result={'collection':'seedmark','generatedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'collectionTreeSHA256':treehash,'collectionFiles':files,'allowedTypesOnly':all(Path(f).suffix in ['.css','.json','.md','.html']for f in files),'staticAudit':audit,'supplementaryContractAudit':json.loads((P.parent/'integration-contracts/seedmark.json').read_text()),'leafCount':len(leafs),'fixtures':sum(1 for f in(K/'elements').glob('*/fixtures/*.html')),'foundationFixtures':len(list((K/'foundation/fixtures').glob('*.html'))),'mapInstances':len(mp['instances']),'rawTopLevelMeasurements':sum(len(page['nodes'])for page in mp['rawMeasurements']),'inlineMeasurements':len(mp['inlineMeasurements']),'rendererVersion':m.RENDERER_VERSION,'leafChecks':leafs,'renderedCellCount':sum(x['cells']for x in leafs.values()),'libraryCandidateCounts':aggregate,'fontFailures':badfonts,'reassemblyRawCandidateCounts':aps,'assemblyInterpretation':{'contrastDOMFalsePositives':['slide_06 four white names on painted black capsule','slide_16 white core text on black pseudo circle','slide_20 white amount/note on black capsule'],'fixedMapQuantizationOverlaps':['slide_13 period/legend mapped to same grid row','slide_14 axis labels/notes quantized to same row'],'claim':'Element sheet functional pass is separate from original-page fidelity; seven structural GAPS remain.'},'pngDimensions':pngs,'replicaIntegritySHA256':hashf(P/'replica-integrity.json')}
(P/'validation-final.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(treehash,'cells',result['renderedCellCount'],'fixtures',result['fixtures'],'PNG counts',{k:len(v)for k,v in pngs.items()})
