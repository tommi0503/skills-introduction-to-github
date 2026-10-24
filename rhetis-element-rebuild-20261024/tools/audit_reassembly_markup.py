from pathlib import Path
from bs4 import BeautifulSoup
from audit_collection import TAX,classes_for
import json,re,sys
R=Path('/workspace/work/rebuild')
def audit(n):
 c=R/n/n;v=R/n/'review';errors=[];files=list((v/'reassembled').glob('slide_*.html'));seen={}
 for f in files:
  s=BeautifulSoup(f.read_text(),'html.parser');body=s.select_one('.slide>.page>.body')
  if not body:continue
  for e in body.select('[data-el]'):
   leaf=e['data-el'].removeprefix(n+'-');p=c/'elements'/leaf/'element.json'
   if not p.exists():errors.append(f.name+': unknown data-el '+e['data-el']);continue
   contract=next(a for a in TAX['contracts']if a['id']==json.loads(p.read_text())['contract']);allowed=classes_for(contract)
   for x in [e]+[z for z in e.find_all()if not z.has_attr('data-el') and z.find_parent(attrs={'data-el':True})is e]:
    extras=set(x.get('class',[]))-allowed
    if extras:errors.append(f.name+': '+leaf+' unknown classes '+','.join(sorted(extras)))
   seen[leaf]=seen.get(leaf,0)+1
  for e in body.select('[style]'):
   for d in e['style'].split(';'):
    if ':'not in d:continue
    k,value=d.split(':',1);k=k.strip()
    if k not in ['grid-column','grid-row']and not k.startswith('--'):errors.append(f.name+': forbidden inline appearance '+k)
  if body.find(['img','canvas','svg','style']):errors.append(f.name+': authored graphic/style inside body')
 report={'collection':n,'pages':len(files),'contract_instances':seen,'errors':sorted(set(errors))};(v/'validation/reassembly-markup-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(n,len(files),'markup errors',len(report['errors']),report['errors'][:4]);return report
if __name__=='__main__':
 reports=[audit(n)for n in sys.argv[1:]or list(json.loads((R/'profiles.json').read_text()))];sys.exit(1 if any(r['errors'] for r in reports) else 0)
