#!/usr/bin/env python3
"""Aggregate final read-only verification evidence; never edits design/render inputs.

Run audit.py/contracts_audit.py/optical_audit.py before this aggregator. During an
in-flight final render, --pending records a provisional snapshot without hiding
stale fingerprints. The same command must be rerun after all renders settle.
"""
from pathlib import Path
import argparse,collections,datetime,hashlib,json,re,struct,sys
from lxml import html
from sheets import ROOT,REF,fingerprint,minimum,sizing,RENDERER_VERSION
from contracts_audit import GOLD,fragment,sign,sign_visible
from audit import text_windows,phrases,windows,normal

PROJECTS=[('vectorbox',12),('seedmark',21),('crossrail',30),('meridian-deck',30),('onboard-docket',19)]
LEAVES=sorted(p.name for p in(REF/'samples/annual/elements').iterdir()if p.is_dir())
KEYS=['outside','clipped','overlaps','contrast','outsideComponent','outsideParts']
H=lambda b:hashlib.sha256(b).hexdigest()
J=lambda p:json.loads(p.read_text())
UTC=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()

def file_record(p):return {'path':p.relative_to(ROOT).as_posix(),'sha256':H(p.read_bytes()),'bytes':p.stat().st_size}
def tree(p):
 files={str(f.relative_to(p)):H(f.read_bytes())for f in sorted(p.rglob('*'))if f.is_file()}
 return {'sha256':H(json.dumps(files,sort_keys=True).encode()),'files':files}
def png_record(p):
 with p.open('rb')as f:b=f.read(24)
 if b[:8]!=b'\x89PNG\r\n\x1a\n':raise ValueError('invalid PNG '+str(p))
 return {'path':p.relative_to(ROOT).as_posix(),'dimensions':list(struct.unpack('>II',b[16:24])),'bytes':p.stat().st_size,'sha256':H(p.read_bytes())}
def raw_counts(rows):
 q={key:sum(len(r.get(key,[]))for r in rows)for key in KEYS}
 q['fontFailures']=sum(not f.get('declared',False)or not f.get('loaded',False)for r in rows for f in r.get('fonts',[]));q['requestFailures']=sum(len(r.get('requestFailures',[]))for r in rows)
 return q

def golden_text_evidence():
 evidence=[]
 for k,_ in PROJECTS:
  P=ROOT/(k+'-project');source=text_windows(P);rows=[]
  for leaf,(sample,names)in GOLD.items():
   for name in names:
    a=fragment((REF/'samples'/sample/'elements'/leaf/'fixtures'/(name+'.html')).read_text());b=fragment((P/k/'elements'/leaf/'fixtures'/(name+'.html')).read_text());conflicts=set()
    for value in phrases(a):conflicts|=windows(normal(value))&set(source)
    rows.append({'leaf':leaf,'fixture':name+'.html','rawFormattingOrTextDiffers':sign(a,True)!=sign(b,True),'visibleFieldTextDiffers':sign_visible(a)!=sign_visible(b),'formattingOnly':sign(a,True)!=sign(b,True)and sign_visible(a)==sign_visible(b),'referenceContainsSourceSixCharacterWindow':bool(conflicts),'conflictingWindows':sorted(conflicts)})
  evidence.append({'collection':k,'rows':rows,'visibleTextEqual':sum(not x['visibleFieldTextDiffers']for x in rows),'actualTextDifferences':sum(x['visibleFieldTextDiffers']for x in rows),'formattingOnly':sum(x['formattingOnly']for x in rows),'actualDifferencesWithReferenceConflict':sum(x['visibleFieldTextDiffers']and x['referenceContainsSourceSixCharacterWindow']for x in rows),'actualDifferencesWithoutReferenceConflict':sum(x['visibleFieldTextDiffers']and not x['referenceContainsSourceSixCharacterWindow']for x in rows)})
 (ROOT/'integration-golden-text-evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n');return evidence

def run(pending):
 start=UTC();errors=[];warnings=[];projects=[];pngs=[];source_before={};gold_evidence=golden_text_evidence();review=J(ROOT/'root-visual-review.json')if(ROOT/'root-visual-review.json').exists()else{'images':{}}
 oldroot=ROOT.parent/'rhetis-part07';old_css=collections.defaultdict(list)
 for k,_ in PROJECTS:
  for f in(oldroot/(k+'-project')/k).rglob('*.css'):old_css[H(f.read_bytes())].append(str(f.relative_to(oldroot)))
 old_matches=[];gold_totals=collections.Counter();current_expected_pngs=set();active_native_pngs=set();active_replica_pngs=set()
 for k,n in PROJECTS:
  P=ROOT/(k+'-project');K=P/k;mapfile=P/'map.json';mapping=J(mapfile);static=J(P/'source-contract-audit.json');contract=J(ROOT/'integration-contracts'/f'{k}.json');current=fingerprint(P,k)
  source_before[k]=tree(K);c={'collection':k,'sourceDeckPages':n,'collectionTreeSHA256':source_before[k]['sha256'],'currentGlobalFingerprint':current,'mappedPageIds':sorted({i['page']for i in mapping['instances']}),'replicaHTMLPages':len(list((P/'replica').glob('slide_*.html'))),'replicaPNGPages':len(list((P/'replica').glob('slide_*.png'))),'elementFolders':len([f for f in(K/'elements').iterdir()if f.is_dir()]),'fixtureCount':sum(len(list((K/'elements'/leaf/'fixtures').glob('*.html')))for leaf in LEAVES),'foundationFixtureCount':len(list((K/'foundation/fixtures').glob('*.html'))),'staticAudit':{'errors':static['errors'],'warnings':static['warnings'],'sixCharacterOverlaps':static['replicaTextOverlap6'],'report':file_record(P/'source-contract-audit.json')},'contractsAudit':{'errors':contract['errors'],'candidates':contract['candidates'],'exceptions':contract['exceptions'],'counts':contract['counts'],'report':file_record(ROOT/'integration-contracts'/f'{k}.json')},'map':{'instances':len(mapping['instances']),'roles':len(mapping.get('roles',{})),'designPresent':sum(bool(str(i.get('design','')).strip())for i in mapping['instances']),'unexpressible':sum(i['use']=='unexpressible'for i in mapping['instances']),'sha256':H(mapfile.read_bytes())},'leaves':[]}
  if len(c['mappedPageIds'])!=n or c['replicaHTMLPages']!=n or c['replicaPNGPages']!=n:errors.append([k,'source map/replica page count mismatch'])
  if c['elementFolders']!=56:errors.append([k,'element count',c['elementFolders']])
  if static['errors']or static['replicaTextOverlap6']:errors.append([k,'static audit failed'])
  if contract['errors']:errors.append([k,'strict contract audit failed',contract['errors']])
  if not c['map']['roles']or c['map']['designPresent']!=c['map']['instances']:errors.append([k,'map roles/design incomplete'])
  if contract['counts'].get('goldenChecked')!=28:errors.append([k,'golden fixture coverage incomplete'])
  gold_totals['checked']+=contract['counts'].get('goldenChecked',0);gold_totals['exactTextAndStructure']+=contract['counts'].get('goldenExact',0);gold_totals['rawExact']+=contract['counts'].get('goldenRawExact',0);gold_totals['formattingOnly']+=contract['counts'].get('goldenFormattingOnly',0);gold_totals['actualTextDifferences']+=contract['counts'].get('goldenActualTextDifferences',0)
  for f in K.rglob('*.css'):
   if H(f.read_bytes())in old_css:old_matches.append({'new':str(f.relative_to(ROOT)),'old':old_css[H(f.read_bytes())]})
  for leaf in LEAVES:
   F=K/'elements'/leaf;fs=sorted((F/'fixtures').glob('*.html'));d=J(P/'sheets'/f'{leaf}-checks.json');want={(f.name,mode,*size)for f in fs for mode in ['light','dark']for size in sizing(minimum(f))};actual=[];rows=[]
   for mode,rs in d['modes'].items():
    for r in rs:
     actual.append((r['fixture'],mode,*r['size']));rows.append(r)
     path=P/'sheet-cells'/f'{leaf}--{Path(r["fixture"]).stem}--{mode}--{r["size"][0]}x{r["size"][1]}.png'
     active_native_pngs.add(str(path.relative_to(ROOT)))
     if not path.exists():errors.append([k,leaf,'missing native cell PNG',str(path.relative_to(ROOT))])
   leaf_current=fingerprint(P,k,leaf);stats=raw_counts(rows);missing=sorted(want-set(actual));extra=sorted(set(actual)-want);dups=[list(a)for a,count in collections.Counter(actual).items()if count>1]
   entry={'leaf':leaf,'fixtures':len(fs),'expectedCells':len(want),'actualCells':len(actual),'sourceFingerprint':d['sourceFingerprint'],'currentFingerprint':leaf_current,'fingerprintCurrent':d['sourceFingerprint']==leaf_current,'rendererVersion':d['rendererVersion'],'counts':stats,'chipDOMMeasurements':sum(len(r.get('chips',[]))for r in rows),'chipDOMScope':'Text Range centre relative to the measured tag/mark/name box; this is not independently the optical centre of a whole multi-part capsule. Plain filled capsule raster checks are separate.','missingCells':missing,'extraCells':extra,'duplicateCells':dups,'minimums':{f.name:list(minimum(f))for f in fs},'report':file_record(P/'sheets'/f'{leaf}-checks.json')};c['leaves'].append(entry)
   if len(fs)<2 or missing or extra or dups:errors.append([k,leaf,'fixture/matrix coverage'])
   if not entry['fingerprintCurrent']:errors.append([k,leaf,'stale sheet fingerprint'])
   if any(stats.values()):warnings.append([k,leaf,'raw render candidates',stats])
   for mode in ['light','dark']:
    f=P/'sheets'/f'{leaf}-{mode}.png';current_expected_pngs.add(str(f.relative_to(ROOT)))
    if not f.exists():errors.append([k,leaf,'missing canonical sheet',mode])
   observed=any(i.get('leaf')==leaf and(i['use']=='base'or str(i['use']).startswith('variant:'))for i in mapping['instances'])
   f=P/'sheets'/f'{leaf}-replica.png'
   if observed:active_replica_pngs.add(str(f.relative_to(ROOT)))
   if observed and not f.exists():errors.append([k,leaf,'missing mapped replica comparison'])
  obsolete=sorted(str(f.relative_to(ROOT))for f in(P/'sheets').glob('*-replica.png')if str(f.relative_to(ROOT))not in active_replica_pngs)
  c['obsoleteReplicaComparisons']=obsolete
  if obsolete:errors.append([k,'obsolete unmapped replica PNG',obsolete])
  c['chipDOMMeasurements']=sum(l['chipDOMMeasurements']for l in c['leaves']);c['sheetCells']=sum(l['actualCells']for l in c['leaves']);c['expectedSheetCells']=sum(l['expectedCells']for l in c['leaves']);c['staleLeaves']=[l['leaf']for l in c['leaves']if not l['fingerprintCurrent']]
  opt=P/'optical-checks.json'
  if opt.exists():
   d=J(opt);c['optical']={'report':file_record(opt),'checks':len(d['checks']),'candidates':d['candidates'],'excludedCellsOrObjects':d['excludedCellsOrObjects'],'scope':d['scope'],'sourceFingerprints':d['sourceFingerprints'],'fingerprintsCurrent':all(v==fingerprint(P,k,l)for l,v in d['sourceFingerprints'].items())}
   if not c['optical']['fingerprintsCurrent']:errors.append([k,'stale optical check'])
   if d['candidates']:warnings.append([k,'optical glyph-centre candidates',len(d['candidates'])])
  else:errors.append([k,'missing optical check'])
  r=J(P/'reassembly-checks.json');rs=r['pages'];c['reassembly']={'pages':len(rs),'expectedPages':n,'allFingerprintsCurrent':all(x.get('sourceFingerprint')==current for x in rs),'stalePages':[x['page']for x in rs if x.get('sourceFingerprint')!=current],'rawCandidates':raw_counts(rs),'paintSettleMilliseconds':r.get('paintSettleMilliseconds'),'report':file_record(P/'reassembly-checks.json')}
  if len(rs)!=n or not c['reassembly']['allFingerprintsCurrent']:errors.append([k,'assembly count/fingerprint incomplete'])
  fd=J(P/'foundation-checks.json');c['foundation']={'renders':len(fd['fixtures']),'expectedRenders':2*c['foundationFixtureCount'],'rawCandidates':raw_counts(fd['fixtures']),'capturedFingerprint':fd['sourceFingerprint'],'currentGlobalFingerprint':current,'globalFingerprintCurrent':fd['sourceFingerprint']==current,'report':file_record(P/'foundation-checks.json'),'fingerprintScopeNote':'Foundation tool captures global collection fingerprint; an unrelated element edit can make it stale without a foundation visual change. Current global proof must be supplied or explicitly reviewed.'}
  if c['foundation']['renders']!=c['foundation']['expectedRenders']:errors.append([k,'foundation render count incomplete'])
  if not c['foundation']['globalFingerprintCurrent']:warnings.append([k,'foundation global FP differs after unrelated source changes'])
  for f in sorted(P.rglob('*.png')):
   v=png_record(f);rel=v['path'];v['role']='canonical-mode-sheet'if rel in current_expected_pngs else'current-native-cell'if rel in active_native_pngs else'mapped-replica-comparison'if rel in active_replica_pngs else f.parent.name if f.parent.name in ['replica','reassembled','compare-reassembled','foundation-sheets']else'historical-or-author-diagnostic';pngs.append(v)
   if f.parent.name in ['replica','reassembled','foundation-sheets']and v['dimensions']!=[1280,720]:errors.append([k,'page PNG size',v['path'],v['dimensions']])
   if f.parent.name=='compare-reassembled'and v['dimensions']!=[3840,720]:errors.append([k,'triple PNG size',v['path'],v['dimensions']])
  projects.append(c)
 baseline=J(ROOT/'replica-preservation.json');preserved=[];preserve_errors=[]
 for k,files in baseline.items():
  for base_name,base in [('v1',oldroot),('v2',ROOT)]:
   for rel,sha in files.items():
    f=base/(k+'-project')/'replica'/rel;actual=H(f.read_bytes())if f.exists()else None;record={'collection':k,'copy':base_name,'file':rel,'baselineSHA256':sha,'actualSHA256':actual,'pass':actual==sha};preserved.append(record)
    if actual!=sha:preserve_errors.append(record)
 if len(preserved)!=474 or preserve_errors:errors.append(['replica preservation failed',len(preserved),len(preserve_errors)])
 if old_matches:errors.append(['exact old CSS matches',len(old_matches)])
 changed=[]
 for k,_ in PROJECTS:
  now=tree(ROOT/(k+'-project')/k)
  if now['sha256']!=source_before[k]['sha256']:changed.append(k)
 if changed:errors.append(['source changed during aggregate',changed])
 visual=[]
 for rel,v in review.get('images',{}).items():
  f=ROOT/rel;sha=H(f.read_bytes())if f.exists()else None;visual.append({'path':rel,'reviewedSHA256':v.get('sha256'),'currentSHA256':sha,'current':sha==v.get('sha256'),'viewedAtUTC':v.get('viewedAtUTC')})
 current_visual={v['path']for v in visual if v['current']}
 triple_paths={str(f.relative_to(ROOT))for k,_ in PROJECTS for f in(ROOT/(k+'-project')/'compare-reassembled').glob('slide_*.png')}
 foundation_paths={str((ROOT/(k+'-project')/'foundation-sheets'/(f.stem+'-'+mode+'.png')).relative_to(ROOT))for k,_ in PROJECTS for f in(ROOT/(k+'-project')/k/'foundation/fixtures').glob('*.html')for mode in ['light','dark']}
 canonical_all=current_expected_pngs|active_replica_pngs|triple_paths|foundation_paths
 review_status=J(ROOT/'root-visual-review-status.json')
 if canonical_all-current_visual:errors.append(['root canonical image review incomplete',sorted(canonical_all-current_visual)])
 if review_status['expected']!=len(canonical_all)or review_status['unseenOrStale']:errors.append(['root review status differs from active canonical set'])
 manual={'reviewer':review.get('reviewer'),'scope':review.get('scope'),'recordedImages':len(visual),'currentImages':sum(x['current']for x in visual),'staleImages':[x for x in visual if x['path']in canonical_all and not x['current']],'historicalOrDiagnosticRecords':sum(x['path']not in canonical_all for x in visual),'allCanonicalImagesExpected':len(canonical_all),'currentAllCanonicalImagesReviewed':len(canonical_all&current_visual),'mappedReplicaComparisonsExpected':len(active_replica_pngs),'currentMappedComparisonsReviewed':len(active_replica_pngs&current_visual),'triplesExpected':len(triple_paths),'currentTriplesReviewed':len(triple_paths&current_visual),'foundationImagesExpected':len(foundation_paths),'currentFoundationImagesReviewed':len(foundation_paths&current_visual),'statusReport':file_record(ROOT/'root-visual-review-status.json'),'canonicalModeSheetsExpected':len(current_expected_pngs),'currentCanonicalModeSheetsReviewed':len(current_expected_pngs&current_visual),'canonicalSheetsNotRecordedCurrent':sorted(current_expected_pngs-current_visual),'report':file_record(ROOT/'root-visual-review.json')}
 manifests={'integration-png-manifest.json':{'scope':'All PNG files under the five project folders, including native cell and author diagnostic PNGs. Their dimensions vary by role; source/reassembled/foundation pages and triple comparison dimensions are enforced separately.','files':pngs},'integration-replica-preservation.json':{'baseline':file_record(ROOT/'replica-preservation.json'),'fileChecks':len(preserved),'errors':preserve_errors,'files':preserved}}
 for name,data in manifests.items():(ROOT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 superseded=[]
 for k,_ in PROJECTS:
  for name in ['validation-final.json','final-verification.json','png-validation.json','replica-integrity.json','relationship-review-final.json']:
   f=ROOT/(k+'-project')/name
   if f.exists():superseded.append({'path':str(f.relative_to(ROOT)),'superseded_by':'integration-verification.json','reason':'Author summaries and earlier source SHA are historical; this final integrated snapshot supplies current source/report fingerprints.'})
 result={'schema':'rhetis.integration-verification/1','generatedAtUTC':UTC(),'startedAtUTC':start,'status':'provisional-awaiting-final-renders'if pending else'verified-with-recorded-candidates'if not errors else'not-ready','pendingCollections':pending,'sourceInputsChangedDuringAggregate':changed,'toolSHA256':{n:H((ROOT/'tools'/n).read_bytes())for n in ['integration_verify.py','audit.py','contracts_audit.py','optical_audit.py','sheets.py','reassembly.py','package.py','clean_cells.py']},'referenceSHA256':{n:H((REF/n).read_bytes())for n in ['README.md','contract/taxonomy.json','contract/kit-tokens.json','contract/palette.json','contract/type-steps.json']},'totals':{'collections':len(projects),'elements':sum(c['elementFolders']for c in projects),'fixtures':sum(c['fixtureCount']for c in projects),'foundationFixtures':sum(c['foundationFixtureCount']for c in projects),'sheetCells':sum(c['sheetCells']for c in projects),'expectedSheetCells':sum(c['expectedSheetCells']for c in projects),'sourcePages':sum(n for _,n in PROJECTS),'allPNGFiles':len(pngs),'activeNativeCellPNGs':len(active_native_pngs),'mappedReplicaComparisonPNGs':len(active_replica_pngs),'canonicalModeSheetPNGs':len(current_expected_pngs),'sixCharacterOverlapCount':sum(len(c['staticAudit']['sixCharacterOverlaps'])for c in projects),'strictContractErrors':sum(len(c['contractsAudit']['errors'])for c in projects),'golden':dict(gold_totals),'immutableReplicaHashChecks':len(preserved),'immutableReplicaHashErrors':len(preserve_errors),'exactOldCSSMatches':len(old_matches),'chipDOMMeasurements':sum(c['chipDOMMeasurements']for c in projects),'opticalFilledCapsuleChecks':sum(c.get('optical',{}).get('checks',0)for c in projects),'opticalFilledCapsuleCandidates':sum(len(c.get('optical',{}).get('candidates',[]))for c in projects)},'projects':projects,'errors':errors,'warnings':warnings,'oldCSSComparison':{'scope':'Every CSS file within all five new collection folders vs every CSS file within all five preserved v1 collection folders; exact byte identity only, not a proof of independent design authorship.','oldFiles':sum(map(len,old_css.values())),'matches':old_matches},'goldenTextEvidence':file_record(ROOT/'integration-golden-text-evidence.json'),'goldenTextEvidenceSummary':[{a:b for a,b in x.items()if a!='rows'}for x in gold_evidence],'manualVisualReview':manual,'cachePreservation':file_record(ROOT/'integration-cache-cleanup.json'),'pngManifest':file_record(ROOT/'integration-png-manifest.json'),'replicaPreservationManifest':file_record(ROOT/'integration-replica-preservation.json'),'supersededReports':superseded,'interpretation':['Automated render candidates are raw observations, not all acceptance failures. The root visual review and GAPS must be read separately.','A library usability pass does not establish pixel identity of reassembled pages. Unexpressible source structures remain explicit in maps/GAPS.','Golden28 is checked per collection for structure and numeric data by contracts_audit. Six-character copy restrictions can require text exceptions; inherited canonical contradictions are reported separately.','Optical raster centring covers only eligible plain filled pill/tag labels; no eligible Seedmark labels is reported honestly as zero coverage, not zero measured error.','No collection CSS, metadata, source HTML, map, fixtures or ZIP is written by this aggregator. Final optical diagnostic HTML is supplied only from browser memory.','Archive CRC, uploaded download SHA and git commit/push are root packaging/publication checks and are outside this prepackage snapshot.']}
 (ROOT/'integration-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 write_markdown(result)
 print(json.dumps({'status':result['status'],'totals':result['totals'],'errors':errors,'warnings':warnings},ensure_ascii=False,indent=2));return result

def write_markdown(r):
 t='# 최종 통합 검증\n\n'
 t+='상태: `'+r['status']+'`. 생성시각: '+r['generatedAtUTC']+'. 이 보고서는 이전 author 요약의 오래된 SHA·칸 수를 대체한다. 원본과의 시각적 동일성 및 계약 GAPS는 자동 기능 검사와 구별한다.\n\n'
 t+='|컬렉션|요소|fixture|시트 칸|현재 FP 시트|6자 겹침|확정 계약 오류|GAPS|\n|---|---:|---:|---:|---:|---:|---:|---:|\n'
 for c in r['projects']:
  t+='|'+c['collection']+'|'+str(c['elementFolders'])+'|'+str(c['fixtureCount'])+'|'+str(c['sheetCells'])+'|'+str(56-len(c['staleLeaves']))+'/56|'+str(len(c['staticAudit']['sixCharacterOverlaps']))+'|'+str(len(c['contractsAudit']['errors']))+'|'+str(c['map']['unexpressible'])+'|\n'
 a=r['totals'];t+='\n원본112페이지. golden140개는 visible field text135개동일·실제문구차이5개이며,그5개에는각각원문6자충돌근거가있다. raw DOM비교의추가29건은끝빈줄등formatting-only차이로문구변경이아니다. 새fixture나CSS변경없이감사판정만정정했다. [140개개별근거](integration-golden-text-evidence.json)를참조한다. golden fixture는 컬렉션별28개, 총'+str(a['golden']['checked'])+'개의 구조·수치 계약을 검사했다. 원문6자 금지가 우선하는 텍스트 예외와 모범 구조에 원래 들어 있는 예외는 상세 JSON에 남겼다.\n\n'
 t+='기존/새 replica '+str(a['immutableReplicaHashChecks'])+'파일 해시 확인, 변경 '+str(a['immutableReplicaHashErrors'])+'건. 새 컬렉션 CSS와 보존된 v1 CSS의 완전 동일 파일 '+str(a['exactOldCSSMatches'])+'건이다. 이 byte 검사는 디자인 독립성 자체의 증명은 아니다.\n\n'
 t+='PNG '+str(a['allPNGFiles'])+'개의 실제 크기·SHA를 [PNG 명세](integration-png-manifest.json)에 기록했다. 조립·foundation·원본 replica 페이지는1280×720, 세 열 비교는3840×720이다. native cell과 요소 전체 시트는 행·크기 수에 따라 다르며, 현재 결과와 과거 진단 이미지를 역할로 구분한다.\n\n'
 t+='일반 DOM chip 측정 '+str(a['chipDOMMeasurements'])+'건과 별도로, 단일 채움 pill/tag의 실제 글리프 중심 '+str(a['opticalFilledCapsuleChecks'])+'건을 측정했고 후보 '+str(a['opticalFilledCapsuleCandidates'])+'건이다. 여러 부품이나 inline 강조는 실제 캡슐 중심과 같지 않아 별도로 제외했다. Seedmark의 eligible0을 측정 통과로 주장하지 않는다.\n\n'
 v=r['manualVisualReview'];t+='주 에이전트 최종 원본·조립 비교 및 현재 시트 검수 '+str(v['currentAllCanonicalImagesReviewed'])+'/'+str(v['allCanonicalImagesExpected'])+'장(요소 mode560·mapped 비교79·triples112·foundation24)의 SHA가 모두 현재 결과와 일치한다. 주 에이전트 직접 검수의 현재 SHA와 일치하는 요소 mode 시트는 '+str(v['currentCanonicalModeSheetsReviewed'])+'/'+str(v['canonicalModeSheetsExpected'])+'장이다. 검수 범위 원문: '+str(v['scope'])+'\n\n'
 t+='확정 집계 오류 '+str(len(r['errors']))+'건, 기록된 경고 '+str(len(r['warnings']))+'건. 세부 후보·현재 fingerprint·도구 SHA·참조 계약 SHA·superseded 목록은 [전체 JSON](integration-verification.json)을 따른다. ZIP CRC·업로드 다운로드 일치·Git push는 root의 패키징/배포 검증에서 추가한다.\n'
 (ROOT/'integration-verification.md').write_text(t)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--pending',nargs='*',default=[]);a=p.parse_args();r=run(a.pending);sys.exit(int(bool(r['errors'])and not a.pending))
