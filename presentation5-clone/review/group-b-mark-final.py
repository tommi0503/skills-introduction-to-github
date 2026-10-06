import json,sys,hashlib,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];p=ROOT/'review/owner-b-completion.json';d=json.loads(p.read_text());cache={}
for key in sys.argv[1:]:
 deck,sid=key.split('/')
 if deck not in cache:cache[deck]=json.loads((ROOT/f'comparisons/final/{deck}.json').read_text())
 meta=next(s for s in cache[deck]['slides'] if s['id']==sid);page=next(r for r in d['pages'] if r['deck']==deck and r['slideId']==sid)
 hashfile=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
 assert hashfile(meta['file'])==meta['pngSha256']
 page.update(actualFinalIndividuallyViewed=True,viewedPngSha256=hashfile(meta['file']),viewedReferenceSha256=hashfile(meta['reference']),viewedComparisonSha256=hashfile(ROOT/f'comparisons/final/{deck}-{sid}.jpg'),reviewedAt=datetime.datetime.now(datetime.timezone.utc).isoformat(),currentSourceFinalIndividualScreenshotViewedAfterLastCorrection=True,rootFinalIntegratedComparisonRequired=False,finalComparison=f'comparisons/final/{deck}-{sid}.jpg',viewedDefinitionHash=cache[deck]['definitionHash'],viewedRendererHash=cache[deck]['rendererHash'])
 unique=json.loads((ROOT/'review/group-b-final-unique-view-paths.json').read_text()).get(key) if (ROOT/'review/group-b-final-unique-view-paths.json').exists() else None
 if unique and unique['pngSha256']==page['viewedPngSha256']:page['actualFinalUniqueHashPath']=unique['path']
 page['finalNotes']='최종 production 비교 이미지를 해당 페이지 단독으로 열어 이전 보정 반영 확인. 사진/복잡한 이미지 회색 placeholder, 판독 불가 문단 및 원본 폰트 근사 차이는 기존 페이지별 기록 참조.'
d['sourceFiles']=d['sourceSha256']
d['slides']=[{'deck':r['deck'],'slide':r['slideId'],'round1IndividuallyViewed':r['round1IndividualComparisonViewed'],'round2IndividuallyViewed':r['round2IndividualComparisonViewed'],'actualFinalIndividuallyViewed':r.get('actualFinalIndividuallyViewed',False),**{k:r.get(k) for k in ['viewedPngSha256','viewedReferenceSha256','viewedComparisonSha256','reviewedAt']}} for r in d['pages']]
d['actualFinalIndividuallyViewedCount']=sum(r.get('actualFinalIndividuallyViewed',False) for r in d['pages']);p.write_text(json.dumps(d,ensure_ascii=False,indent=2));print(d['actualFinalIndividuallyViewedCount'],'/234 actual final pages viewed')
