"""Fail-closed delivery audit; reports incomplete work without labelling it a release."""
from pathlib import Path
from PIL import Image
from sheets import SIZES, minparse
from audit_collection import audit as contract_audit
from audit_required_fixtures import audit as required_audit
import json, hashlib, sys

R=Path('/workspace/work/rebuild'); OLD=Path('/workspace/work/delivery')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(name):
 c=R/name/name;v=R/name/'review';issues=[];elements=[];pngs={}
 rootreviews=json.loads((R/'root-final-review.json').read_text())if(R/'root-final-review.json').exists()else{}
 reviewed=rootreviews.get(name,{})
 ca=contract_audit(name);ra=required_audit(name)
 issues.extend(ca['errors']);issues.extend('unwritten '+x for x in ca['pending'])
 issues.extend('missing mandatory '+x for x in ra['missing']);issues.extend('mandatory structure/data '+x for x in ra['structure_errors'])
 frozen=json.loads((R/'replica-freeze.json').read_text())[name]
 for f,h in frozen.items():
  if digest(OLD/name/'review/replica'/f)!=h:issues.append('FROZEN REPLICA CHANGED '+f)
 for folder in sorted((c/'elements').iterdir()):
  if not folder.is_dir():continue
  leaf=folder.name;local=[];proof=v/'validation'/(leaf+'.json');q={}
  if not proof.exists():local.append('missing size proof')
  else:
   q=json.loads(proof.read_text())
   if leaf=='venn'and q.get('paint_members_revision',0)<2:local.append('venn set boundary proof missing')
   for f,h in q['source_hashes'].items():
    p=c/f
    if not p.exists()or digest(p)!=h:local.append('stale source '+f)
   for f,h in q.get('shared_render_hashes',{}).items():
    if not Path(f).exists()or digest(Path(f))!=h:local.append('stale shared '+f)
   if not q.get('shared_render_hashes'):local.append('missing complete dependency proof')
   if set(q.get('counts',{}))!=set(['outside','clipped','hidden','member_outside','overlaps','contrast','chip_alignment','shape_clipped','painted_outside']):local.append('missing current QA fields')
   if any(q['counts'].values()):local.append('visual QA '+str(q['counts']))
   actual={(x['fixture'],x['mode'],tuple(x['grid']))for x in q['cases']};expected=set()
   for f in folder.joinpath('fixtures').glob('*.html'):
    mins,_=minparse(f.read_text());sizes={s for s in SIZES if any(s[0]>=m[0]and s[1]>=m[1]for m in mins)}|set(mins)
    expected|={(f.stem,mode,s)for mode in ['light','dark']for s in sizes}
   if actual!=expected:local.append('case coverage missing='+str(len(expected-actual))+' extra='+str(len(actual-expected)))
   fonts=q.get('font_checks',[])
   if len(fonts)!=len(list(folder.joinpath('fixtures').glob('*.html')))*2:local.append('missing actual-font checks')
   if any(x['load_errors']for x in fonts):local.append('font loading error')
   if any(x.get('font_probe_version')!=2 for x in fonts):local.append('missing actual descendant font proof')
   for x in fonts:
    if x.get('font_nodes')and not x.get('platform_fonts'):local.append('text rendered without actual font evidence')
    if any(not f['isCustomFont']for f in x.get('platform_fonts',[])):local.append('system font fallback '+x['fixture'])
    if x.get('html_sha256'):
     p=v/'html'/leaf/(x['fixture']+'-'+x['mode']+'.html')
     if not p.exists()or digest(p)!=x['html_sha256']:local.append('stale actual-font HTML')
  for mode in ['light','dark']:
   p=v/'sheets'/(leaf+'-'+mode+'.png')
   if not p.exists():local.append('missing '+mode+' sheet')
   elif reviewed.get('elements',{}).get(leaf,{}).get('sheet_sha256',{}).get(mode)!=digest(p):local.append('missing current primary review '+mode)
  elements.append({'leaf':leaf,'cases':len(q.get('cases',[])),'issues':local})
  issues.extend(leaf+': '+x for x in local)
 m=json.loads((v/'map.json').read_text())
 for leaf in sorted({x['leaf']for x in m['instances']if x.get('leaf')and x['use']!='unexpressible'}):
  if not (v/'sheets'/(leaf+'-replica.png')).exists():issues.append('missing replica comparison '+leaf)
 pages=json.loads((R/name/'build/source-dom.json').read_text())
 assembly=v/'validation/reassembled.json'
 if not assembly.exists():issues.append('missing assembly proof')
 else:
  aq=json.loads(assembly.read_text());actual={a['page']for a in aq['pages']}
  if actual!=set(pages):issues.append('assembly page coverage')
  for a in aq['pages']:
   if a['size']!=[1280,720]or a['png_size']!=[1280,720]:issues.append(a['page']+': page size')
   if a['textOutsidePage']:issues.append(a['page']+': text outside page')
   if any(not f['loaded']for f in a['fontChecks']):issues.append(a['page']+': font error')
   p=v/'reassembled'/('slide_'+a['page']+'.html')
   if digest(p)!=a['source_html_sha256']:issues.append(a['page']+': stale rendered HTML')
   rv=reviewed.get('pages',{}).get(a['page'],{})
   if rv.get('status')!='pass'or rv.get('comparison_sha256')!=digest(v/'compare-reassembled'/('slide_'+a['page']+'.png')):issues.append(a['page']+': missing current primary comparison review')
 ip=R/name/'build/reassembly-inputs.json'
 if not ip.exists():issues.append('missing assembly dependency snapshot')
 else:
  for f,h in json.loads(ip.read_text()).items():
   p=R/name/f
   if not p.exists()or digest(p)!=h:issues.append('stale assembly dependency '+f)
 for p in sorted(v.rglob('*.png')):
  with Image.open(p)as im:im.verify()
  with Image.open(p)as im:pngs[str(p.relative_to(v))]=list(im.size)
 cp=v/'validation/copy-audit.json'
 if not cp.exists():issues.append('missing complete six-character audit')
 elif json.loads(cp.read_text())['matches']:issues.append('replica wording in fixtures')
 raster=v/'validation/raster-paint-audit.json'
 if not raster.exists():issues.append('missing full raster paint audit')
 else:
  rp=json.loads(raster.read_text())
  if not rp.get('all_cases')or rp.get('missing_cells')or rp.get('issues'):issues.append('incomplete or failing raster paint audit')
  if rp.get('checked_shadow_cases')!=sum(x['cases']for x in elements):issues.append('raster coverage differs from final native cases')
  for leaf,deps in rp.get('source_hashes_by_leaf',{}).items():
   for f,h in deps.items():
    if not(c/f).exists()or digest(c/f)!=h:issues.append('stale raster dependency '+f)
 fp=v/'validation/foundation.json'
 if not fp.exists():issues.append('missing foundation proof')
 else:
  fq=json.loads(fp.read_text())
  if len(fq)!=len(list((c/'foundation/fixtures').glob('*.html')))*2:issues.append('foundation coverage')
  for f in fq:
   if f['textOutside']or f['fonts']or f['contrast']:issues.append('foundation QA '+f['fixture']+' '+f['mode'])
 report={'collection':name,'ready':not issues,'frozen_replica_files':len(frozen),'elements':elements,'native_cases':sum(x['cases']for x in elements),'png_dimensions':pngs,'issues':issues}
 (v/'validation/release-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(name,'READY'if not issues else'INCOMPLETE',len(issues),'issues',len(pngs),'PNG',flush=True)
 return report

if __name__=='__main__':
 results=[check(n)for n in (sys.argv[1:]or list(json.loads((R/'profiles.json').read_text()))) ]
 sys.exit(0 if all(x['ready']for x in results)else 1)
