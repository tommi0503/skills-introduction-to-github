"""Record hashes only AFTER the named images have actually been viewed by root."""
from pathlib import Path
import sys,json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'root-visual-review.json'
data=json.loads(path.read_text()) if path.exists() else {'reviewer':'root','scope':'Full final sheet overviews; native crops on suspect cases. This does not claim every character in every native cell was separately read. Element authors also reviewed their own all-size cells.','images':{}}
args=sys.argv[1:];prepared=None
if args and args[0]=='--prepared':
 prepared=json.loads(Path(args[1]).read_text());args=args[2:]
for name in args:
 p=ROOT/name
 assert p.exists(),name
 digest=hashlib.sha256(p.read_bytes()).hexdigest()
 if prepared is not None:assert prepared.get(name)==digest,('Canonical image changed after overview preparation; view again',name)
 data['images'][name]={'sha256':digest,'viewedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat()}
path.write_text(json.dumps(data,ensure_ascii=False,indent=2))
print('Recorded',len(args),'actually viewed images;',len(data['images']),'total')
