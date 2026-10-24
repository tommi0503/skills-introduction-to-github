"""Explicit root review records. Call only after inspecting the named artifacts."""
from pathlib import Path
import json,hashlib,sys,argparse
R=Path('/workspace/work/rebuild');P=R/'root-final-review.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def record(n,kind,items,status,note):
 data=json.loads(P.read_text())if P.exists()else{};obj=data.setdefault(n,{}).setdefault(kind,{})
 for item in items:
  v=R/n/'review';entry={'status':status,'note':note}
  if kind=='pages':
   p=v/'compare-reassembled'/('slide_'+item+'.png');entry.update(comparison_sha256=sha(p),html_sha256=sha(v/'reassembled'/('slide_'+item+'.html')))
  else:
   entry['sheet_sha256']={mode:sha(v/'sheets'/(item+'-'+mode+'.png'))for mode in ['light','dark']};entry['proof_sha256']=sha(v/'validation'/(item+'.json'))
  obj[item]=entry
 P.write_text(json.dumps(data,ensure_ascii=False,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('collection');p.add_argument('kind',choices=['pages','elements']);p.add_argument('items',nargs='+');p.add_argument('--status',default='pass');p.add_argument('--note',required=True);a=p.parse_args();record(a.collection,a.kind,a.items,a.status,a.note)
