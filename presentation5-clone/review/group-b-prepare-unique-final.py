import json,hashlib,shutil
from pathlib import Path
root=Path(__file__).resolve().parents[1];out=Path('/tmp/envato-b-final-unique');out.mkdir(exist_ok=True);rows={}
for meta in sorted((root/'comparisons/final').glob('p*.json')):
 d=json.loads(meta.read_text())
 if d['id']not in {'p050','p051','p064','p069','p073','p080','p081','p091','p092','p101','p104','p107'}:continue
 for s in d['slides']:
  key=d['id']+'/'+s['id'];png=Path(s['file']);ref=Path(s['reference']);pair=root/f"comparisons/final/{d['id']}-{s['id']}.jpg";sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest();ph,rh,ch=sha(png),sha(ref),sha(pair);assert ph==s['pngSha256'];name=f"{d['id']}-{s['id']}-{ph[:16]}-{rh[:8]}-{ch[:16]}.jpg";dest=out/name;shutil.copyfile(pair,dest);rows[key]={'path':str(dest),'pngSha256':ph,'referenceSha256':rh,'comparisonSha256':ch}
(root/'review/group-b-final-unique-view-paths.json').write_text(json.dumps(rows,indent=2));print(len(rows),'unique comparisons copied')
O=json.loads((root/'review/owner-b-completion.json').read_text());diff=[]
for s in O['pages']:
 k=s['deck']+'/'+s['slideId']
 if s.get('actualFinalIndividuallyViewed')and s.get('viewedPngSha256')!=rows[k]['pngSha256']:diff.append(k)
print('already-marked PNG changes',diff)
