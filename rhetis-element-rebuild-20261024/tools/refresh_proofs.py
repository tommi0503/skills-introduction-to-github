"""Refresh only stale completed size proofs, recording every changed native PNG."""
from pathlib import Path
from PIL import Image
import json,hashlib,sys,argparse
from sheets import render
R=Path('/workspace/work/rebuild')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pixel_sha(p):
 with Image.open(p) as im:return hashlib.sha256(str(im.size).encode()+im.convert('RGB').tobytes()).hexdigest()
def stale(n,leaf,q):
 c=R/n/n;bad=[]
 for f,h in q.get('source_hashes',{}).items():
  p=c/f
  if not p.exists()or sha(p)!=h:bad.append(f)
 for f,h in q.get('shared_render_hashes',{}).items():
  p=Path(f)
  if not p.exists()or sha(p)!=h:bad.append(f)
 if not q.get('shared_render_hashes'):bad.append('missing shared dependency checks')
 if set(q.get('counts',{}))!=set(['outside','clipped','hidden','member_outside','overlaps','contrast','chip_alignment','shape_clipped','painted_outside']):bad.append('missing current QA fields')
 if len(q.get('font_checks',[]))!=len(list((c/'elements'/leaf/'fixtures').glob('*.html')))*2:bad.append('missing complete CDP font proof')
 return bad

def run(names,execute=False,leaves=None,shared_only=False):
 report=[]
 for n in names:
  for f in sorted((R/n/'review/validation').glob('*.json')):
   leaf=f.stem
   if not (R/n/n/'elements'/leaf/'element.css').exists():continue
   if leaves and leaf not in leaves:continue
   q=json.loads(f.read_text())
   if not isinstance(q,dict)or not isinstance(q.get('cases'),list) or 'source_hashes'not in q:continue
   bad=stale(n,leaf,q)
   if not bad:continue
   if shared_only and any(not(f.startswith('foundation/')or f.endswith('/assets/fonts/fonts.css')or f in ['missing shared dependency checks','missing current QA fields'])for f in bad):continue
   a={'collection':n,'leaf':leaf,'stale':bad,'before_counts':q.get('counts',{})};report.append(a)
   if not execute:continue
   if any(q.get('counts',{}).values()):a['skipped']='unresolved QA; owning author must fix first';continue
   d=R/n/'build/cells'/leaf;old={p.name:sha(p)for p in d.glob('*.png')};oldpixels={p.name:pixel_sha(p)for p in d.glob('*.png')};oldproof=sha(f)
   fresh=render(n,leaf);new={p.name:sha(p)for p in d.glob('*.png')};newpixels={p.name:pixel_sha(p)for p in d.glob('*.png')};changed=[p for p in newpixels if oldpixels.get(p)!=newpixels[p]]
   a.update(before_proof_sha256=oldproof,after_proof_sha256=sha(f),after_counts=fresh['counts'],changed_cells=changed,removed_cells=sorted(set(old)-set(new)),pixel_identical=oldpixels==newpixels,rewritten_pngs=[p for p in new if old.get(p)!=new[p]])
   (R/n/'build'/('refresh-'+leaf+'.json')).write_text(json.dumps(a,ensure_ascii=False,indent=2));print(n,leaf,'CHANGED',len(changed),'removed',len(a['removed_cells']),flush=True)
 (R/'proof-refresh-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('stale proofs',len(report),flush=True);return report
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('collections',nargs='*');p.add_argument('--execute',action='store_true');p.add_argument('--leaf',action='append');p.add_argument('--shared-only',action='store_true');a=p.parse_args();run(a.collections or list(json.loads((R/'profiles.json').read_text())),a.execute,set(a.leaf)if a.leaf else None,a.shared_only)
