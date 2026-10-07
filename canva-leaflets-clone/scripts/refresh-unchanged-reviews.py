"""Carry visual review forward only when both final PNG and viewed pair are byte-identical."""
import json,hashlib,datetime
from pathlib import Path
root=Path(__file__).resolve().parents[1];file=root/'review/primary-review.json';d=json.loads(file.read_text());updated=[];changed=[]
for row in d['pages']:
    b=row['key'].split('-')[0];meta=json.loads((root/f'comparisons/final/{b}.json').read_text());p=next(x for x in meta['panels']+meta['sides'] if row['key']==b+'-'+x['id'])
    pair=root/row['comparisonFile'];pair_hash=hashlib.sha256(pair.read_bytes()).hexdigest()
    if p['pngSha256']!=row['pngSha256'] or pair_hash!=row['comparisonSha256']:changed.append(row['key']);continue
    if meta['rendererHash']!=row['rendererHash'] or meta['definitionHash']!=row['definitionHash']:
        row['identicalRecaptureVerification']={'verifiedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PNGAndIndividualComparisonByteIdentical':True,'previousRendererHash':row['rendererHash'],'previousDefinitionHash':row['definitionHash']}
        row['rendererHash']=meta['rendererHash'];row['definitionHash']=meta['definitionHash'];updated.append(row['key'])
file.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'unchangedReviewsHashRefreshed':updated,'changedMustReopen':changed},ensure_ascii=False))
