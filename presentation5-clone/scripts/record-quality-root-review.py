"""Record a batch only after the main agent has viewed each individual pair."""
import argparse, datetime, hashlib, json, pathlib
root=pathlib.Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('deck');p.add_argument('slides',nargs='+')
p.add_argument('--round',default='final');p.add_argument('--note',required=True)
p.add_argument('--pending',action='store_true',help='Viewed individually but a concrete visual correction is still pending')
a=p.parse_args()
path=root/'review/quality/root-review-journal.json'
journal=json.loads(path.read_text()) if path.exists() else {}
meta=json.loads((root/'comparisons'/a.round/f'{a.deck}.json').read_text())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
for id in a.slides:
 s=next(s for s in meta['slides'] if s['id']==id)
 pair=root/'comparisons'/a.round/f'{a.deck}-{id}.jpg'
 png=root/'renders'/a.round/f'{a.deck}-{id}.png'
 ref=pathlib.Path(s['reference'])
 assert pair.is_file() and sha(png)==s['pngSha256']
 journal[f'{a.deck}/{id}']={'deck':a.deck,'slide':id,'viewedRound':a.round,
  'individuallyViewed':True,'viewer':'main-agent','reviewedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),
  'pngSha256':sha(png),'referenceSha256':sha(ref),'comparisonSha256':sha(pair),
  'note':a.note,'followUpRequired':a.pending}
path.write_text(json.dumps(journal,ensure_ascii=False,indent=2)+'\n')
print(f'{len(journal)} independent pairs recorded')
