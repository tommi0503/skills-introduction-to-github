#!/usr/bin/env python3
"""Verify actual Round5 designs, current matrices, panels, pages and root-reviewed SHA.

The design/replica inputs are read-only. Reports record raw source-style contrast
candidates separately from official-palette element usability. No fixed contract,
fixture, GAP, provenance-row or canonical-image count is assumed.
"""
from __future__ import annotations
from pathlib import Path
import argparse, collections, datetime, hashlib, json, re, struct, subprocess, sys
from sheets import ROOT, REF, fingerprint, minimum, sizing, RENDERER_VERSION

PROJECTS=[('vectorbox',12),('seedmark',21),('crossrail',30),('meridian-deck',30),('onboard-docket',19)]
GEOMETRY=['outside','clipped','overlaps','outsideComponent','outsideParts']
KEYS=GEOMETRY+['contrast']
H=lambda b:hashlib.sha256(b).hexdigest()
J=lambda p:json.loads(Path(p).read_text())
UTC=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()

def tree(p):
 files={str(f.relative_to(p)):H(f.read_bytes())for f in sorted(p.rglob('*'))if f.is_file()}
 return{'sha256':H(json.dumps(files,sort_keys=True).encode()),'files':files}
def raw_counts(rows):
 r={k:sum(len(x.get(k,[]))for x in rows)for k in KEYS}
 r['fontFailures']=sum(not f.get('declared',False)or not f.get('loaded',False)for x in rows for f in x.get('fonts',[]));r['requestFailures']=sum(len(x.get('requestFailures',[]))for x in rows)
 return r
def painted_bounds_resolution(P,k,rows,scope,leaf=None):
 """Keep raw metrics; resolve only font-box candidates disproven by current paint."""
 counts=raw_counts(rows);resolved=[];proofs={}
 for row in rows:
  for field in ['outside','outsideComponent']:
   for candidate in row.get(field,[]):
    target=leaf or str(candidate.get('component','')).removeprefix(k+'-')
    if not target or row.get('clipped'):continue
    file=P/'paint-proofs'/(target+('-matrix'if scope=='matrix'else'-assembly')+'.json')
    if not file.is_file():continue
    if target not in proofs:proofs[target]=J(file)
    proof=proofs[target];expected=fingerprint(P,k,target if scope=='matrix'else None)
    if proof.get('schema')!='rhetis.painted-bounds/1'or proof.get('collection')!=k or proof.get('leaf')!=target or proof.get('sourceFingerprint')!=expected:continue
    matches=[x for x in proof.get('cases',[])if (x.get('fixture')==row.get('fixture')and x.get('mode')==row.get('_proofMode')and x.get('size')==row.get('size'))if scope=='matrix']if scope=='matrix'else[x for x in proof.get('cases',[])if x.get('fixture')==str(row.get('page'))+'.html'and x.get('htmlSHA256')==row.get('htmlSHA256')]
    if len(matches)!=1:continue
    case=matches[0];r=case.get('root',{});box=case.get('physicalPaintBounds');rr=[r.get(v,0)for v in ['x','y','width','height']];candidate_root=candidate.get('componentBox')if field=='outsideComponent'else row.get('root')
    if case.get('actualOutside')or not box or not candidate_root or len(candidate_root)!=4 or any(abs(a-b)>.1 for a,b in zip(rr,candidate_root)):continue
    if not(0<=rr[0]<=1280 and 0<=rr[1]<=720 and rr[0]+rr[2]<=1281 and rr[1]+rr[3]<=721 and box[0]>=rr[0]-1 and box[1]>=rr[1]-1 and box[2]<=rr[0]+rr[2]+1 and box[3]<=rr[1]+rr[3]+1):continue
    element=candidate.get('box',[])
    if len(element)!=4 or element[0]<rr[0]-1 or element[1]<rr[1]-1 or element[0]+element[2]>rr[0]+rr[2]+1 or element[1]+element[3]>rr[1]+rr[3]+1:continue
    counts[field]-=1;resolved.append({'field':field,'fixtureOrPage':row.get('fixture',row.get('page')),'mode':row.get('_proofMode','original'),'size':row.get('size'),'candidate':candidate,'paintedBounds':box,'proof':str(file.relative_to(ROOT))})
 return{'effectiveCounts':counts,'resolvedFontMetricCandidates':resolved,'method':'Only current paired whole-canvas physical paint can resolve outside font metrics; raw JSON stays unchanged; clipping/overlap is never resolved.'}
def page_id(v):
 try:return f'{int(v):02d}'
 except(ValueError,TypeError):return str(v)
def fullslide(f):return bool(re.search(r'class=["\'][^"\']*\bslide\b',f.read_text()))
def run(pending=(),root=ROOT,refresh_audits=False):
 root=Path(root).resolve();ref=root/'reference';start=UTC();errors=[];warnings=[];projects=[];canonical=set();native=set();pngs=[];before={};counts=collections.Counter()
 def rel(p):return p.relative_to(root).as_posix()
 def record(p):return{'path':rel(p),'bytes':p.stat().st_size,'sha256':H(p.read_bytes())}
 def need(p,what):
  if not p.is_file():errors.append({'code':'missing-'+what,'path':rel(p)});return False
  return True
 def load(p,what):
  if not need(p,what):return None
  try:return J(p)
  except(Exception)as e:errors.append({'code':'invalid-'+what,'path':rel(p),'detail':str(e)});return None
 def matrix_stats(d,fs,leaf,P,k,global_fp=False):
  expected={(f.name,mode,*size)for f in fs for mode in ['light','dark']for size in sizing(minimum(f))};actual=[];rows=[]
  for mode,rs in d.get('modes',{}).items():
   for x in rs:
    actual.append((x['fixture'],mode,*x['size']));rows.append(dict(x,_proofMode=mode))
    filename=(f'{Path(x["fixture"]).stem}--{mode}--{x["size"][0]}x{x["size"][1]}.png'if global_fp else f'{leaf}--{Path(x["fixture"]).stem}--{mode}--{x["size"][0]}x{x["size"][1]}.png');p=P/('panel-cells'if global_fp else'sheet-cells')/filename
    if need(p,'native-cell'):native.add(rel(p))
  rawstats=raw_counts(rows);paint=painted_bounds_resolution(P,k,rows,'matrix',None if global_fp else leaf);stats=paint['effectiveCounts'];actualset=set(actual);duplicates=[list(v)for v,n in collections.Counter(actual).items()if n>1];current=fingerprint(P,k,None if global_fp else leaf)
  result={'fixtures':len(fs),'expectedCells':len(expected),'actualCells':len(actual),'minimums':{f.name:list(minimum(f))for f in fs},'capturedFingerprint':d.get('sourceFingerprint'),'currentFingerprint':current,'fingerprintCurrent':d.get('sourceFingerprint')==current,'missingCells':[list(x)for x in sorted(expected-actualset)],'extraCells':[list(x)for x in sorted(actualset-expected)],'duplicateCells':duplicates,'counts':stats,'rawCounts':rawstats,'paintBoundsResolution':paint}
  if expected!=actualset or duplicates:errors.append({'code':'matrix-coverage','collection':k,'leaf':leaf,'detail':result})
  if not result['fingerprintCurrent']:errors.append({'code':'stale-matrix','collection':k,'leaf':leaf})
  if any(stats[x]for x in GEOMETRY+['fontFailures','requestFailures']):errors.append({'code':'matrix-geometry-or-font','collection':k,'leaf':leaf,'counts':stats})
  if stats['contrast']:errors.append({'code':'official-palette-contrast','collection':k,'leaf':leaf,'count':stats['contrast']})
  return result
 for k,n in PROJECTS:
  P=root/(k+'-project');K=P/k
  if refresh_audits:
   for tool in ['audit.py','contracts_audit.py']:
    proc=subprocess.run([sys.executable,str(root/'tools'/tool),k],capture_output=True,text=True)
    if proc.returncode:errors.append({'code':'audit-execution','collection':k,'tool':tool,'stderr':proc.stderr[-2000:]})
  before[k]=tree(K);ls=sorted(f.name for f in(K/'elements').iterdir()if f.is_dir());mapping=load(P/'map.json','map')or{'instances':[],'pages':[]};instances=mapping.get('instances',[]);sourcepages=sorted({page_id(i['page'])for i in instances if i.get('page')is not None}|{page_id(i['page'])for i in mapping.get('pages',[])if i.get('page')is not None});current=fingerprint(P,k);static=load(P/'source-contract-audit.json','source-audit');strict=load(root/'integration-contracts'/f'{k}.json','contract-audit')
  c={'collection':k,'sourceDeckPages':n,'elementFolders':len(ls),'designFolders':ls,'fixtureCount':0,'collectionTreeSHA256':before[k]['sha256'],'currentGlobalFingerprint':current,'mappedPageIds':sourcepages,'replicaHTMLPages':len(list((P/'replica').glob('slide_*.html'))),'replicaPNGPages':len(list((P/'replica').glob('slide_*.png'))),'map':{'instances':len(instances),'roles':len(mapping.get('roles',{})),'designPresent':sum(bool(str(i.get('design','')).strip())for i in instances),'unexpressible':sum(i.get('use')=='unexpressible'for i in instances),'ignoredResidue':len(mapping.get('ignoredResidue',[])),'sha256':H((P/'map.json').read_bytes())},'leaves':[]}
  if len(sourcepages)!=n or c['replicaHTMLPages']!=n or c['replicaPNGPages']!=n:errors.append({'code':'page-inventory','collection':k,'detail':c['mappedPageIds']})
  if not c['map']['roles']or c['map']['designPresent']!=len(instances):errors.append({'code':'map-roles-design','collection':k})
  deps=collections.defaultdict(set)
  for leaf in ls:
   for f in(K/'elements'/leaf/'fixtures').glob('*.html'):
    for dep in re.findall(r'data-el=["\']'+re.escape(k)+r'-([^"\']+)',f.read_text()):
     if dep!=leaf:deps[dep].add(leaf)
  for typ,d in [('source',static),('strict',strict)]:
   if not d:continue
   c[typ+'Audit']={'errors':d.get('errors',[]),'warnings':d.get('warnings',[]),'sixCharacterOverlaps':d.get('replicaTextOverlap6',[]),'globalFingerprint':d.get('globalFingerprint')}
   if d.get('errors')or d.get('replicaTextOverlap6'):errors.append({'code':typ+'-audit-failed','collection':k,'errors':d.get('errors',[])})
   if d.get('globalFingerprint')!=current:errors.append({'code':'stale-'+typ+'-audit','collection':k})
  for leaf in ls:
   folder=K/'elements'/leaf;fs=sorted((folder/'fixtures').glob('*.html'));c['fixtureCount']+=len(fs);d=load(P/'sheets'/f'{leaf}-checks.json','sheet-checks');observed=any(i.get('leaf')==leaf and(i.get('use')=='base'or str(i.get('use','')).startswith('variant:'))for i in instances)
   entry={'leaf':leaf,'contractLeaf':leaf.split('--',1)[0],'observed':observed,'dependencyOf':sorted(deps.get(leaf,[]))}
   if not observed and not deps.get(leaf):errors.append({'code':'unobserved-unneeded-filler','collection':k,'leaf':leaf})
   if len(fs)<2:errors.append({'code':'fixture-count','collection':k,'leaf':leaf,'actual':len(fs)})
   if d:
    entry.update(matrix_stats(d,fs,leaf,P,k));entry['rendererVersion']=d.get('rendererVersion')
    if d.get('rendererVersion')!=RENDERER_VERSION:errors.append({'code':'renderer-version','collection':k,'leaf':leaf})
   for mode in ['light','dark']:
    f=P/'sheets'/f'{leaf}-{mode}.png'
    if need(f,'mode-sheet'):canonical.add(rel(f))
   if observed:
    f=P/'sheets'/f'{leaf}-replica.png'
    if need(f,'replica-comparison'):canonical.add(rel(f))
   c['leaves'].append(entry)
  active_replica={str(P/'sheets'/f'{v["leaf"]}-replica.png')for v in c['leaves']if v['observed']}
  obsolete=[rel(f)for f in(P/'sheets').glob('*-replica.png')if str(f)not in active_replica]
  if obsolete:errors.append({'code':'obsolete-replica-comparison','collection':k,'paths':obsolete})
  ffs=sorted((K/'foundation/fixtures').glob('*.html'));c['foundationFixtureCount']=len(ffs);fd=load(P/'foundation-checks.json','foundation-checks')
  if fd:
   rows=fd.get('fixtures',[]);want={(f.name,m)for f in ffs for m in ['light','dark']};actual={(r['fixture'],r['mode'])for r in rows};c['foundation']={'renders':len(rows),'expectedRenders':len(want),'fingerprintCurrent':fd.get('sourceFingerprint')==current,'counts':raw_counts(rows)}
   if len(rows)!=len(want)or actual!=want or not c['foundation']['fingerprintCurrent']:errors.append({'code':'foundation-coverage-or-fingerprint','collection':k,'detail':c['foundation']})
   if any(c['foundation']['counts'][q]for q in GEOMETRY+['fontFailures','requestFailures','contrast']):errors.append({'code':'foundation-render-candidates','collection':k,'counts':c['foundation']['counts']})
  for f in ffs:
   for mode in ['light','dark']:
    q=P/'foundation-sheets'/f'{f.stem}-{mode}.png'
    if need(q,'foundation-png'):canonical.add(rel(q))
  pfs=[f for f in ffs if f.name.startswith('panel')and not fullslide(f)];c['panelFixtureCount']=len(pfs)
  if pfs:
   pd=load(P/'panel-sheets/panel-checks.json','panel-checks')
   if pd:c['panels']=matrix_stats(pd,pfs,'foundation-panels',P,k,True)
   for mode in ['light','dark']:
    q=P/'panel-sheets'/f'foundation-panels-{mode}.png'
    if need(q,'panel-matrix'):canonical.add(rel(q))
  else:c['panels']={'fixtures':0,'actualCells':0,'expectedCells':0,'fingerprintCurrent':True,'scope':'No standalone panel fixture; full-page panel examples are counted in foundation.'}
  assembly=load(P/'reassembly-checks.json','reassembly-checks')
  if assembly:
   rows=assembly.get('pages',[]);actualids={page_id(x.get('page','').removeprefix('slide_'))for x in rows};c['reassembly']={'pages':len(rows),'expectedPages':n,'allFingerprintsCurrent':all(x.get('sourceFingerprint')==current for x in rows),'rawCandidates':raw_counts(rows),'isolatedContextPerPage':assembly.get('isolatedContextPerPage'),'report':record(P/'reassembly-checks.json')}
   if len(rows)!=n or actualids!=set(sourcepages)or not c['reassembly']['allFingerprintsCurrent']:errors.append({'code':'assembly-page-or-fingerprint','collection':k,'detail':c['reassembly']})
   paint=painted_bounds_resolution(P,k,rows,'assembly');c['reassembly']['paintBoundsResolution']=paint
   critical={q:paint['effectiveCounts'][q]for q in GEOMETRY+['fontFailures','requestFailures']if paint['effectiveCounts'][q]}
   if critical:errors.append({'code':'assembly-geometry-or-font','collection':k,'counts':critical})
   if c['reassembly']['rawCandidates']['contrast']:warnings.append({'code':'original-style-contrast','collection':k,'count':c['reassembly']['rawCandidates']['contrast'],'interpretation':'Source palette is external style; inspect original|replica|assembly and review notes. Official-palette element contrast is checked separately.'})
  for pid in sourcepages:
   for ext in ['html','png']:need(P/'reassembled'/f'slide_{pid}.{ext}','assembly')
   q=P/'compare-reassembled'/f'slide_{pid}.png'
   if need(q,'triple'):canonical.add(rel(q))
  c['sheetCells']=sum(x.get('actualCells',0)for x in c['leaves']);c['expectedSheetCells']=sum(x.get('expectedCells',0)for x in c['leaves']);c['staleLeaves']=[x['leaf']for x in c['leaves']if not x.get('fingerprintCurrent')]
  for f in sorted(P.rglob('*.png')):
   b=f.read_bytes();dims=list(struct.unpack('>II',b[16:24]))if b[:8]==b'\x89PNG\r\n\x1a\n'and len(b)>=24 else None;r={'path':rel(f),'dimensions':dims,'bytes':len(b),'sha256':H(b),'role':'canonical-review'if rel(f)in canonical else'current-native-cell'if rel(f)in native else'immutable-replica'if f.parent.name=='replica'else'author-diagnostic-or-inactive'};pngs.append(r)
   if dims is None:errors.append({'code':'invalid-png','path':rel(f)})
   if f.parent.name in ['replica','reassembled','foundation-sheets']and dims!=[1280,720]:errors.append({'code':'page-png-size','path':rel(f),'dimensions':dims})
   if f.parent.name=='compare-reassembled'and dims!=[3840,720]:errors.append({'code':'triple-png-size','path':rel(f),'dimensions':dims})
  projects.append(c)
 # Baseline cardinality is discovered from immutable source records, not assumed.
 baseline=load(root/'replica-preservation.json','replica-baseline')or{};preserved=[];preserve_errors=[];copies={'round5':root,'elements-v2':root.parent/'rhetis-elements-v2','part07':root.parent/'rhetis-part07'};available={k:v for k,v in copies.items()if v.is_dir()};unavailable=sorted(set(copies)-set(available))
 for k,files in baseline.items():
  for label,base in available.items():
   for name,sha in files.items():
    f=base/(k+'-project')/'replica'/name;actual=H(f.read_bytes())if f.exists()else None;r={'collection':k,'copy':label,'file':name,'baselineSHA256':sha,'actualSHA256':actual,'pass':actual==sha};preserved.append(r)
    if actual!=sha:preserve_errors.append(r)
 if preserve_errors:errors.append({'code':'immutable-replica-changed','records':preserve_errors})
 if unavailable:warnings.append({'code':'legacy-replica-copies-unavailable','copies':unavailable,'interpretation':'No preservation claim is made for unavailable legacy copies.'})
 changed=[k for k,_ in PROJECTS if tree(root/(k+'-project')/k)['sha256']!=before[k]['sha256']]
 if changed:errors.append({'code':'source-changed-during-aggregation','collections':changed})
 review=J(root/'root-visual-review.json')if(root/'root-visual-review.json').is_file()else{'images':{}};reviewed=review.get('images',{});current_review={p for p in canonical if p in reviewed and(root/p).is_file()and H((root/p).read_bytes())==reviewed[p].get('sha256')};unseen=sorted(canonical-current_review)
 if unseen:errors.append({'code':'root-canonical-review-incomplete','paths':unseen})
 visual={'reviewer':review.get('reviewer'),'scope':review.get('scope'),'expected':len(canonical),'current':len(current_review),'unseenOrStale':unseen,'historicalOrDiagnosticRecords':len(set(reviewed)-canonical),'canonicalImages':sorted(canonical)}
 (root/'root-visual-review-status.json').write_text(json.dumps(visual,ensure_ascii=False,indent=2)+'\n')
 (root/'integration-png-manifest.json').write_text(json.dumps({'schema':'rhetis.round5-png-manifest/1','scope':'All PNG files under current project directories, with current canonical/native evidence distinguished from author diagnostic or inactive images.','files':pngs},ensure_ascii=False,indent=2)+'\n')
 (root/'integration-replica-preservation.json').write_text(json.dumps({'schema':'rhetis.round5-replica-preservation/1','baseline':record(root/'replica-preservation.json')if(root/'replica-preservation.json').exists()else None,'availableCopies':list(available),'unavailableCopies':unavailable,'fileChecks':len(preserved),'errors':preserve_errors,'files':preserved},ensure_ascii=False,indent=2)+'\n')
 totals={'collections':len(projects),'sourcePages':sum(n for _,n in PROJECTS),'elements':sum(p['elementFolders']for p in projects),'fixtures':sum(p['fixtureCount']for p in projects),'foundationFixtures':sum(p['foundationFixtureCount']for p in projects),'panelFixtures':sum(p['panelFixtureCount']for p in projects),'sheetCells':sum(p['sheetCells']for p in projects),'expectedSheetCells':sum(p['expectedSheetCells']for p in projects),'panelCells':sum(p['panels'].get('actualCells',0)for p in projects),'canonicalReviewPNGs':len(canonical),'currentCanonicalImagesReviewed':len(current_review),'allPNGFiles':len(pngs),'activeNativeCellPNGs':len(native),'sixCharacterOverlapCount':sum(len(p.get('sourceAudit',{}).get('sixCharacterOverlaps',[]))for p in projects),'strictContractErrors':sum(len(p.get('strictAudit',{}).get('errors',[]))for p in projects),'unexpressibleInstances':sum(p['map']['unexpressible']for p in projects),'immutableReplicaHashChecks':len(preserved),'immutableReplicaHashErrors':len(preserve_errors)}
 tools=['integration_verify.py','package.py','audit.py','contracts_audit.py','sheets.py','foundation_sheets.py','panel_sheets.py','reassembly.py','paint_bounds_audit.py','optical_audit.py'];refs=['README.md','contract/taxonomy.json','contract/kit-tokens.json','contract/palette.json','contract/type-steps.json'];result={'schema':'rhetis.round5-integration-verification/1','startedAtUTC':start,'generatedAtUTC':UTC(),'status':'provisional-awaiting-final-renders'if pending else'verified-with-recorded-candidates'if not errors else'not-ready','pendingCollections':list(pending),'sourceInputsChangedDuringAggregate':changed,'toolSHA256':{n:H((root/'tools'/n).read_bytes())for n in tools if(root/'tools'/n).exists()},'referenceSHA256':{n:H((ref/n).read_bytes())for n in refs if(ref/n).exists()},'totals':totals,'projects':projects,'manualVisualReview':visual,'errors':errors,'warnings':warnings,'interpretation':['ROUND5 optional contracts, independent design folders, free own parts, foundation panels/vector, chart extensions and8–256 type tokens supersede the historical fixed-contract brief.','All counts and provenance rows are discovered from current directories and maps; deleted inferred designs and obsolete comparisons cannot count as evidence.','Root SHA review is evidence of the reviewer scope recorded in root-visual-review.json; it does not claim every glyph in every native cell was individually read.','Source palette contrast candidates remain raw recorded observations; official-palette element and foundation usability is separately enforced.','This verifier writes reports only. Archive integrity, public API publication and actual re-download verification are separate and never inferred.']}
 (root/'integration-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');write_markdown(result,root);print(json.dumps({'status':result['status'],'totals':totals,'errors':errors,'warnings':warnings},ensure_ascii=False,indent=2));return result

def write_markdown(r,root=ROOT):
 t='# ROUND5 최종 통합 검증\n\n상태: `'+r['status']+'` · '+r['generatedAtUTC']+'\n\n실제 존재하는 디자인 폴더와 현재 지도·fixture·최소 칸에서 동적으로 집계했다. 이전 고정 개수/일반 요소/모범 fixture 의무를 적용하지 않는다.\n\n|컬렉션|디자인|fixture|시트 칸|현재 FP 시트|panel 칸|잔여 GAP 인스턴스|\n|---|---:|---:|---:|---:|---:|---:|\n'
 for c in r['projects']:t+=f'|{c["collection"]}|{c["elementFolders"]}|{c["fixtureCount"]}|{c["sheetCells"]}|{c["elementFolders"]-len(c["staleLeaves"])}/{c["elementFolders"]}|{c["panels"].get("actualCells",0)}|{c["map"]["unexpressible"]}|\n'
 a=r['totals'];t+=f'\n실제 페이지{a["sourcePages"]}장, 시트 허용 칸{a["sheetCells"]}/{a["expectedSheetCells"]}개, 전용 panel 칸{a["panelCells"]}개. 불변 replica 파일 해시{a["immutableReplicaHashChecks"]}건 검사, 차이{a["immutableReplicaHashErrors"]}건이다. 현재 원본6자 문구 겹침{a["sixCharacterOverlapCount"]}건, 확정 계약 오류{a["strictContractErrors"]}건이다.\n\n'
 t+=f'주 에이전트 검수 기록과 현재 SHA가 일치하는 canonical 이미지{a["currentCanonicalImagesReviewed"]}/{a["canonicalReviewPNGs"]}장이다. 범위 원문: {r["manualVisualReview"].get("scope")}\n\n'
 t+=f'집계 오류{len(r["errors"])}건, 기록된 경고{len(r["warnings"])}건. 경고와 원본 style 대비 후보는 기능 통과나 원본과의 픽셀 동일성을 뜻하지 않는다. source 원문·자료 자체의 모순·그리드 차이는 컬렉션별 검수 기록과 GAPS를 따른다. [전체 JSON](integration-verification.json) · [실제 PNG 크기/SHA](integration-png-manifest.json) · [불변 replica 증거](integration-replica-preservation.json)\n\nZIP CRC·오프라인 의존성·압축 후 SHA는 package.py, 게시된 파일의 실제 재다운로드는 별도 게시 검증에서 확인한다.\n'
 (Path(root)/'integration-verification.md').write_text(t)

if __name__=='__main__':
 a=argparse.ArgumentParser(description=__doc__);a.add_argument('--root',type=Path,default=ROOT);a.add_argument('--pending',nargs='*',default=[]);a.add_argument('--refresh-audits',action='store_true');v=a.parse_args();r=run(v.pending,v.root,v.refresh_audits);raise SystemExit(int(bool(r['errors'])and not v.pending))
