from pathlib import Path
import json,hashlib
from render_reassembled import run,server
R=Path('/workspace/work/rebuild');out={}
for n in json.loads((R/'profiles.json').read_text()):
 v=R/n/'review';q=json.loads((v/'validation/reassembled.json').read_text());old={a['page']:a['source_html_sha256']for a in q['pages']};stale=[]
 for f in (v/'reassembled').glob('slide_*.html'):
  if old.get(f.stem[-2:])!=hashlib.sha256(f.read_bytes()).hexdigest():stale.append(f.stem[-2:])
 if stale:out[n]=sorted(stale)
(R/'assembly-stale.json').write_text(json.dumps(out));print(out,flush=True)
for n,ps in out.items():run(n,ps)
server.shutdown()
