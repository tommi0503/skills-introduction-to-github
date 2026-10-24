"""Bookkeeping for the primary agent's actual image views; never auto-approves images.

--prepare prints the next paths for view_image. --approve is a separate manual
action after the images have been inspected, and binds that review to PNG bytes.
"""
import argparse,hashlib,json,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LOG=ROOT/'primary-visual-review.json';PENDING=ROOT/'pending-visual.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main(args):
 rows=json.loads(LOG.read_text())if LOG.exists()else[]
 if args.approve:
  pending=json.loads(PENDING.read_text())if PENDING.exists()else[]
  for item in pending:
   if sha(ROOT/item['path'])!=item['sha256']:raise ValueError('PNG changed after image view: '+item['path'])
   rows=[r for r in rows if r['path']!=item['path']]
   rows.append({**item,'reviewer':'primary','status':'pass','method':'Direct full-sheet/page image view, with automated per-state text/paint/font/contrast checks used alongside visual inspection.','note':args.note or'배치·형태·위계·연결선·크기/테마 변화 확인.','reviewedUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())})
  LOG.write_text(json.dumps(rows,ensure_ascii=False,indent=2));PENDING.write_text('[]');print('Recorded',len(pending),'actual views; total',len(rows))
 if args.prepare:
  paths=[]
  for item in json.loads((ROOT/'collections.json').read_text()):
   R=ROOT/(item['id']+'-review')
   if args.group in ['sheets','all']:paths+=sorted((R/'sheets').glob('*.png'))
   if args.group in ['pages','all']:paths+=sorted((R/'compare-reassembled').glob('*.png'))
  current={x['path']:x['sha256']for x in rows if x.get('status')=='pass'}
  remaining=[p for p in paths if current.get(str(p.relative_to(ROOT)))!=sha(p)and not any(p.name.startswith(x+'-')for x in args.exclude)]
  pending=[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)}for p in remaining[:args.count]];PENDING.write_text(json.dumps(pending,ensure_ascii=False,indent=2));print(json.dumps({'remaining':len(remaining),'next':pending},ensure_ascii=False))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--prepare',action='store_true');p.add_argument('--approve',action='store_true');p.add_argument('--count',type=int,default=3);p.add_argument('--group',choices=['sheets','pages','all'],default='sheets');p.add_argument('--note');p.add_argument('--exclude',nargs='*',default=[]);main(p.parse_args())
