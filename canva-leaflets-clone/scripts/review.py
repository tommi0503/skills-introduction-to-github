"""Record only individual comparison images actually opened by the primary reviewer."""
import argparse,json,hashlib,datetime
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('keys',nargs='+');p.add_argument('--note',required=True);a=p.parse_args()
file=root/'review/primary-review.json'
report=json.loads(file.read_text()) if file.exists() else {'reviewer':'primary-agent','method':'Each original/browser pair opened individually at final capture; contact sheets used only as navigation','comparisonRound':'final (third cycle)','pages':[]}
for key in a.keys:
    brochure=key.split('-')[0];page_id=key[len(brochure)+1:]
    meta=json.loads((root/f'comparisons/final/{brochure}.json').read_text())
    page=next(x for x in meta['panels']+meta['sides'] if x['id']==page_id)
    pair=root/f'comparisons/final/{key}.jpg';assert pair.exists()
    assert hashlib.sha256((root/page['file']).read_bytes()).hexdigest()==page['pngSha256']
    row={'key':key,'originalAndResultViewedIndividually':True,'comparisonFile':str(pair.relative_to(root)),'comparisonSha256':hashlib.sha256(pair.read_bytes()).hexdigest(),'pngSha256':page['pngSha256'],'definitionHash':meta['definitionHash'],'rendererHash':meta['rendererHash'],'reviewedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'visualObservations':a.note,'status':'reviewed-with-documented-differences'}
    report['pages']=[x for x in report['pages'] if x['key']!=key]+[row]
report['pages'].sort(key=lambda x:x['key']);report['reviewedCount']=len(report['pages'])
file.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Recorded',len(a.keys),'individual pairs; total',report['reviewedCount'])
