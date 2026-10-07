"""Link all individually reviewed final team images and the root integration audit."""
import hashlib,json,pathlib,shutil
from collections import Counter
from PIL import Image,ImageChops
root=pathlib.Path(__file__).resolve().parents[1]
journal=json.loads((root/'review/quality/root-review-journal.json').read_text())
manifest=json.loads((root/'public/reference/manifest.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
owners={};source_mismatch=[]
for p in sorted((root/'review/quality').glob('owner-*-completion.json')):
 record=json.loads(p.read_text())
 for file,expected in record['sourceFiles'].items():
  if sha(root/file)!=expected:source_mismatch.append(file)
 for s in record['slides']:
  key=f'{s["deck"]}/{s["slide"]}'
  assert key not in owners,f'Duplicate reviewer ownership: {key}'
  owners[key]={**s,'owner':record['owner'],'evidenceFile':str(p.relative_to(root))}
slides=[];missing=[];changed=[];root_passed=[];root_pending=[];root_changed=[];carried=[]
for deck in manifest:
 meta=json.loads((root/'comparisons/final'/f'{deck["id"]}.json').read_text())
 for s in meta['slides']:
  key=f'{deck["id"]}/{s["id"]}';entry=owners.get(key)
  png=root/'renders/final'/f'{deck["id"]}-{s["id"]}.png'
  ref=pathlib.Path(s['reference']);pair=root/'comparisons/final'/f'{deck["id"]}-{s["id"]}.jpg'
  final={'pngSha256':sha(png),'referenceSha256':sha(ref),'comparisonSha256':sha(pair)}
  assert final['pngSha256']==s['pngSha256'],f'PNG changed after browser capture: {key}'
  reviewed=entry and all(entry.get(f) for f in ['round1IndividuallyViewed','round2IndividuallyViewed'])
  final_confirmed=entry and (entry.get('actualFinalIndividuallyViewed') or entry.get('finalPixelsCarryConfirmed'))
  if not reviewed or not final_confirmed:missing.append(key)
  elif any(final[k]!=entry.get('viewed'+k[0].upper()+k[1:]) for k in ['pngSha256','referenceSha256']):changed.append(key)
  else:
   proof=None
   if not entry.get('actualFinalIndividuallyViewed'):
    evidence=entry.get('latestImprovedEvidence') or entry.get('round2Evidence')
    assert evidence and evidence.get('actualIndividuallyViewed') and evidence.get('actualViewCompletedAt'),f'Missing fresh actual view evidence: {key}'
    reviewed_png=root/evidence['pngPath'];reviewed_ref=root/evidence['referencePath']
    assert sha(reviewed_png)==evidence['pngSha256']==final['pngSha256'],f'Final carry has different browser pixels: {key}'
    assert sha(reviewed_ref)==evidence['referenceSha256']==final['referenceSha256'],f'Final carry has different reference: {key}'
   if final['comparisonSha256']!=entry.get('viewedComparisonSha256'):
    if entry.get('comparisonEvidenceCarriedFromRound2'):
     previous=root/entry['viewedComparisonPath'];previous_png=root/entry['round2ViewedPng']
     assert previous.is_file() and sha(previous)==entry['viewedComparisonSha256'],f'Missing actual comparison evidence: {key}'
     assert sha(previous_png)==final['pngSha256']==entry['round2ViewedPngSha256'],f'Reviewed browser pixels changed: {key}'
     with Image.open(previous) as a,Image.open(pair) as b:
      assert a.size==b.size==(2584,756),f'Comparison layout changed: {key}'
      # The round caption is in the top 30px. JPEG chroma/DCT boundary
      # differences can extend into the first few page rows; those pixels
      # are covered by the exact browser PNG and native-reference hashes.
      assert ImageChops.difference(a.convert('RGB').crop((0,40,2584,750)),b.convert('RGB').crop((0,40,2584,750))).getbbox() is None,f'Compared page pixels changed: {key}'
     evidence=root/'review/quality/carried-comparisons'/previous.name;evidence.parent.mkdir(exist_ok=True);shutil.copyfile(previous,evidence)
     proof={'deck':deck['id'],'slide':s['id'],'actualPreviouslyViewedComparison':str(evidence.relative_to(root)),
      'actualPreviouslyViewedComparisonSha256':entry['viewedComparisonSha256'],'finalComparisonSha256':final['comparisonSha256'],
      'finalBrowserPngByteIdenticalToReviewedPng':True,'nativeReferenceByteIdentical':True,
      'decodedComparisonPageRegionByteIdentical':True,'decodedRegion':[0,40,2584,750],
      'difference':'Only the comparison round-caption/JPEG header boundary changed; full underlying browser PNG and reference hashes match exactly.'}
     carried.append(proof)
    else:changed.append(key)
   if final['comparisonSha256']==entry.get('viewedComparisonSha256') or proof:
    slides.append({**entry,**final,'matchesFinalPixelsAndReference':True,'comparisonCarryProof':proof,
     'finalPngPath':str(png.relative_to(root)),'finalComparisonPath':str(pair.relative_to(root)),
     'finalReferencePath':str(ref.relative_to(root)),
     'finalReviewMethod':'direct-final-individual-view' if entry.get('actualFinalIndividuallyViewed') else 'new-individual-review-linked-by-identical-browser-and-reference-bytes',
     'finalDefinitionSha256':meta['definitionHash'],'finalRendererSha256':meta['rendererHash']})
  main=journal.get(key)
  if main:
   if main['followUpRequired']:root_pending.append(key)
   elif main['pngSha256']!=final['pngSha256'] or main['referenceSha256']!=final['referenceSha256']:root_changed.append(key)
   else:root_passed.append({**main,'finalComparisonSha256':final['comparisonSha256'],
    'finalPngPath':str(png.relative_to(root)),'finalComparisonPath':str(pair.relative_to(root)),
    'finalReferencePath':str(ref.relative_to(root))})
coverage=Counter(s['deck'] for s in root_passed)
root_missing=[d['id'] for d in manifest if coverage[d['id']]<min(3,len(d['slides']))]
report={'qualityRevision':'2026-10-07-v2','freshReviewAfterUserFeedback':True,'expectedSlides':1057,'teamIndividuallyViewedFinalSlides':len(slides),
 'mainAgentIndividuallyViewedFinalPairs':len(root_passed),'mainAgentReviewedDecks':len(coverage),
 'mainAgentIntegrationPolicy':'Three or more separately viewed current-result/reference pairs per deck (both pages for the two-page deck), linked to final PNG and reference hashes; every root-reported correction separately rechecked. Assigned agents individually review every improved page; production output is directly rechecked when pixels changed, otherwise linked by exact hashes.',
 'ownerMissing':missing,'ownerFinalFilesChangedSinceView':changed,'sourceHashMismatch':source_mismatch,
 'rootPendingCorrections':root_pending,'rootFilesChangedSinceView':root_changed,'rootUnreviewedDecks':root_missing}
(root/'review/root-review-coverage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(root/'review/identical-pixels-review-carry.json').write_text(json.dumps({'method':'Actual newly reviewed browser PNG and native reference must be byte-identical; decoded comparison page region must also be identical. Original viewed comparison files are included. Only the round caption changed.','pages':carried},ensure_ascii=False,indent=2)+'\n')
assert not any([missing,changed,source_mismatch,root_pending,root_changed,root_missing]) and len(slides)==1057,report
(root/'review/visual-review.json').write_text(json.dumps({'allIndividuallyViewed':True,
 'viewer':'Six assigned agents performed fresh individual comparisons of every improved page. Final production pixels are either directly viewed or proven byte-identical to the newly viewed browser PNG and reference; main agent performed integration across all 47 decks.',
 'method':'Each actual-browser page beside its native cropped reference. Two owner comparison/correction rounds, third integration and final-change verification; contact sheets are previews only.',
 'qualityRevision':'2026-10-07-v2','freshReviewAfterUserFeedback':True,'decks':47,'slides':slides,'mainAgentFinalIntegration':root_passed,'coverage':report},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
