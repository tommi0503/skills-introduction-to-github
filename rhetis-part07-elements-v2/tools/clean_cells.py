#!/usr/bin/env python3
"""Preserve only obsolete native-cell cache files in /tmp, after all280 reports are current.

Never modifies CSS, HTML, fixtures, metadata, replicas or canonical sheet PNGs.
Dry-run is the default; --apply moves files after validating all sources and cells.
"""
from pathlib import Path
import argparse,collections,datetime,hashlib,json,shutil,sys
from sheets import ROOT,fingerprint
PROJECTS=['vectorbox','seedmark','crossrail','meridian-deck','onboard-docket']
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def run(apply=False,destination=Path('/tmp/v2-obsolete-cells')):
 errors=[];plans=[];source_snap={};counts={};expected_by_collection={};canonical_by_collection={};map_snap={}
 for k in PROJECTS:
  P=ROOT/(k+'-project');mapping=json.loads((P/'map.json').read_text());map_snap[k]=H(P/'map.json');expected=set();reports=sorted((P/'sheets').glob('*-checks.json'));reports=[f for f in reports if f.stem.removesuffix('-checks')in {p.name for p in(P/k/'elements').iterdir()if p.is_dir()}]
  if len(reports)!=56:errors.append([k,'expected56 leaf reports',len(reports)])
  for f in reports:
   d=json.loads(f.read_text());leaf=d['leaf'];current=fingerprint(P,k,leaf);source_snap[k+'/'+leaf]=current
   if d.get('sourceFingerprint')!=current:errors.append([k,leaf,'stale sheet; no cache files may move'])
   for mode,rows in d['modes'].items():
    for r in rows:expected.add(f'{leaf}--{Path(r["fixture"]).stem}--{mode}--{r["size"][0]}x{r["size"][1]}.png')
  actual={f.name:f for f in(P/'sheet-cells').glob('*.png')}
  for n in sorted(expected-actual.keys()):errors.append([k,'missing current cell',n])
  expected_by_collection[k]=expected
  obsolete=sorted(actual.keys()-expected);counts[k]={'expected':len(expected),'actualBefore':len(actual),'obsolete':len(obsolete)}
  for n in obsolete:
   f=actual[n];plans.append({'collection':k,'source':f.relative_to(ROOT).as_posix(),'destination':str(destination/k/'sheet-cells'/n),'bytes':f.stat().st_size,'sha256':H(f)})
  leaves={f.name for f in(P/k/'elements').iterdir()if f.is_dir()}
  observed={i['leaf']for i in mapping['instances']if i.get('leaf')in leaves and(i.get('use')=='base'or str(i.get('use','')).startswith('variant:'))}
  canonical={f'{leaf}-{mode}.png'for leaf in leaves for mode in ['light','dark']}|{leaf+'-replica.png'for leaf in observed};canonical_by_collection[k]=canonical
  sheet_files={f.name:f for f in(P/'sheets').glob('*.png')}
  for name in sorted(canonical-sheet_files.keys()):errors.append([k,'missing canonical sheet',name])
  debug=sorted(sheet_files.keys()-canonical);counts[k]['noncanonicalSheetPNGs']=len(debug)
  for name in debug:
   f=sheet_files[name];plans.append({'collection':k,'source':f.relative_to(ROOT).as_posix(),'destination':str(destination/k/'sheets'/name),'bytes':f.stat().st_size,'sha256':H(f)})
 if errors:
  print(json.dumps({'status':'blocked-without-mutation','errors':errors,'collections':counts},ensure_ascii=False,indent=2));return 1
 if apply:
  for k in PROJECTS:
   P=ROOT/(k+'-project')
   assert H(P/'map.json')==map_snap[k],('map changed before cache move',k)
   for f in(P/'sheets').glob('*-checks.json'):
    d=json.loads(f.read_text())
    if 'leaf'in d and k+'/'+d['leaf']in source_snap:assert fingerprint(P,k,d['leaf'])==source_snap[k+'/'+d['leaf']],('source changed before cache move',k,d['leaf'])
  for row in plans:
   f=ROOT/row['source'];dest=Path(row['destination']);dest.parent.mkdir(parents=True,exist_ok=True)
   assert H(f)==row['sha256'],('input changed',f)
   if dest.exists():
    assert H(dest)==row['sha256'],('different preserved file already exists',dest)
    f.unlink()
   else:shutil.move(str(f),str(dest))
   assert H(dest)==row['sha256']and not f.exists()
  for k in PROJECTS:
   actual={f.name for f in(ROOT/(k+'-project')/'sheet-cells').glob('*.png')}
   assert actual==expected_by_collection[k],('current cell set differs after preservation',k)
   counts[k]['actualAfter']=len(actual)
   assert {f.name for f in(ROOT/(k+'-project')/'sheets').glob('*.png')}==canonical_by_collection[k],('canonical sheet set differs',k)
 result={'generatedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'applied'if apply else'dry-run','scope':'Only obsolete PNGs directly under each project sheet-cells/ and noncanonical debug PNGs under sheets/. Current filename keys come from all56 current-FP leaf checks per collection. Inputs and canonical sheets remain unchanged.','collections':counts,'movedFiles':plans,'movedBytes':sum(x['bytes']for x in plans),'errors':[]}
 target=ROOT/'integration-cache-cleanup.json'if apply else Path('/tmp/v2-obsolete-cells-plan.json');target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:result[k]for k in ['mode','collections','movedBytes','errors']},ensure_ascii=False,indent=2));return 0
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--apply',action='store_true');p.add_argument('--destination',type=Path,default=Path('/tmp/v2-obsolete-cells'));a=p.parse_args();sys.exit(run(a.apply,a.destination))
