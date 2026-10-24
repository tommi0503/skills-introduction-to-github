from pathlib import Path
import collections,hashlib,importlib.util,json,datetime
from PIL import Image
P=Path(__file__).parent;K='meridian-deck'
spec=importlib.util.spec_from_file_location('sheettool',P.parent/'tools/sheets.py');tool=importlib.util.module_from_spec(spec);spec.loader.exec_module(tool)
keys=['outside','clipped','overlaps','outsideComponent','outsideParts','contrast']
sheets=[];totals=collections.Counter();fontfail=[];expected=set()
for f in sorted((P/'sheets').glob('*-checks.json')):
 j=json.loads(f.read_text());assert j['sourceFingerprint']==tool.fingerprint(P,K,j['leaf']),f
 assert j['rendererVersion']=='v2-grid-paint-font-parts-1'
 cells=0
 for mode,rows in j['modes'].items():
  for r in rows:
   cells+=1
   for key in keys:totals[key]+=len(r.get(key,[]))
   fontfail.extend(x for x in r['fonts'] if not x['declared'] or not x['loaded'])
   w,h=r['size'];expected.add(f"{j['leaf']}--{Path(r['fixture']).stem}--{mode}--{w}x{h}.png")
 sheets.append({'leaf':j['leaf'],'cells':cells,'sourceFingerprint':j['sourceFingerprint'],'generatedAtUTC':j['generatedAtUTC']})
assert len(sheets)==56 and not any(totals.values()) and not fontfail
assert {f.name for f in (P/'sheet-cells').glob('*.png')}==expected
assembly=json.loads((P/'reassembly-checks.json').read_text());assert len(assembly['pages'])==30
assembly_totals=collections.Counter();assembly_fonts=[]
for r in assembly['pages']:
 assert r['sourceFingerprint']==tool.fingerprint(P,K),r['page']
 assert r['htmlSHA256']==hashlib.sha256((P/'reassembled'/(r['page']+'.html')).read_bytes()).hexdigest()
 assert not r['requestFailures']
 for key in keys:assembly_totals[key]+=len(r.get(key,[]))
 assembly_fonts.extend(x for x in r['fonts'] if not x['declared'] or not x['loaded'])
assert not any(assembly_totals[k] for k in keys if k!='contrast') and not assembly_fonts
images={}
for name in ['sheets','sheet-cells','visual-review','reassembled','compare-reassembled']:
 sizes=collections.Counter();files=sorted((P/name).glob('*.png'))
 for f in files:
  with Image.open(f) as im:sizes[f'{im.width}x{im.height}']+=1;im.verify()
 images[name]={'count':len(files),'dimensions':dict(sorted(sizes.items()))}
assert images['reassembled']=={'count':30,'dimensions':{'1280x720':30}}
assert images['compare-reassembled']=={'count':30,'dimensions':{'3840x720':30}}
audit=json.loads((P/'source-contract-audit.json').read_text());assert not audit['errors'] and not audit['warnings'] and not audit['replicaTextOverlap6']
files=sorted(f for f in (P/K).rglob('*') if f.is_file());manifest={str(f.relative_to(P/K)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files};collection_hash=hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest()
result={'collection':K,'generatedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'source frozen; library quality checks pass; assembly differences disclosed','pixelIdentical':False,'elementFolders':56,'fixtureCount':len(list((P/K/'elements').glob('*/fixtures/*.html'))),'goldenFixtureCount':28,'unexpressibleOwners':audit['unexpressible'],'mapInstances':audit['mapInstances'],'sourceParts':944,'library':{'rendererVersion':tool.RENDERER_VERSION,'rendererSHA256':tool.RENDERER_HASH,'cells':sum(x['cells'] for x in sheets),'issues':dict(totals),'fontFailures':len(fontfail),'staleFingerprints':[],'leaves':sheets},'assembly':{'pages':30,'issues':dict(assembly_totals),'fontFailures':len(assembly_fonts),'requestFailures':0,'sourcePaletteContrastByPage':{r['page']:len(r['contrast']) for r in assembly['pages'] if r['contrast']},'contrastInterpretation':'External original-palette candidates retained independently of the official light/dark library checks. See review-notes.md.'},'png':images,'collectionSHA256':collection_hash,'collectionFileSHA256':manifest,'audit':{'errors':audit['errors'],'warnings':audit['warnings'],'replicaTextOverlap6':audit['replicaTextOverlap6']}}
(P/'final-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(collection_hash);print('verified',len(files),'collection files,',result['fixtureCount'],'fixtures,',result['library']['cells'],'native library cells')
