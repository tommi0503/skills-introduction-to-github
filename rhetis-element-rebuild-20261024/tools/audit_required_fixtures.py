"""Check required fixture structure and data independently of element CSS.
The latest user instruction forbids source-copy even in required examples; record
any text substitution separately while enforcing their exact DOM/data structure.
"""
from pathlib import Path
from bs4 import BeautifulSoup,Comment,NavigableString
import json,re
R=Path('/workspace/work/rebuild');REF=Path('/workspace/work/reference')
REQUIRED={'card':('confetti',['card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone']),'callout':('annual',['callout','callout-icon','callout-stack']),'chart-area':('annual',['area-1','areas-2','areas-stacked-3','area-3pt']),'chart-bar':('confetti',['bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2']),'chart-donut':('amethyst',['donut','donuts-3','donuts-4','donut-0','donut-100']),'chart-line':('amethyst',['lines-12','lines-6','lines-3','lines-flat'])}
def normalized(raw,structure=False,legacy_star=False):
 s=BeautifulSoup(raw,'html.parser')
 for c in s.find_all(string=lambda x:isinstance(x,Comment)):c.extract()
 first=s.find()
 if first and first.has_attr('style'):
  declarations=[x for x in first['style'].split(';')if x.strip()and not x.strip().startswith(('grid-column:','grid-row:'))]
  first['style']=';'.join(declarations+['grid-column:1 / span 12','grid-row:1 / span 6'])
 # The supplied card-4 example contains literal star icon text, contrary to its
 # own empty-Lucide requirement. Normalize only that documented source defect.
 for icon in s.select('.icon'):
  if icon.get_text().strip()in ['*','✹'] and not icon.has_attr('data-icon'):
   icon.clear();icon['data-icon']='sparkles'
  elif legacy_star and icon.get('data-icon')in ['asterisk','sparkles']:
   icon['data-icon']='sparkles'
 for e in s.find_all():
  if e.has_attr('data-el'):e['data-el']='COLLECTION-'+e['data-el'].split('-',1)[-1] if e['data-el'].startswith(('annual-','amethyst-','confetti-'))else'COLLECTION-'+next((l for l in REQUIRED if e['data-el'].endswith('-'+l)),e['data-el'].rsplit('-',1)[-1])
  if e.has_attr('style'):e['style']=';'.join(re.sub(r'\s+','',x)for x in e['style'].split(';')if x.strip())
 if structure:
  for t in list(s.find_all(string=True)):
   if t.strip():t.replace_with('TEXT')
 return re.sub(r'>\s+<','><',str(s)).strip()
def audit(n):
 out={'collection':n,'missing':[],'structure_errors':[],'text_substitutions':[],'checked':[]}
 for leaf,(sample,fixtures)in REQUIRED.items():
  for fn in fixtures:
   p=R/n/n/'elements'/leaf/'fixtures'/(fn+'.html');source=REF/'samples'/sample/'elements'/leaf/'fixtures'/(fn+'.html')
   if not p.exists():out['missing'].append(str(p.relative_to(R/n/n)));continue
   a,b=source.read_text(),p.read_text();out['checked'].append(leaf+'/'+fn)
   legacy=leaf=='card'and fn=='card-4'
   if normalized(a,True,legacy)!=normalized(b,True,legacy):out['structure_errors'].append(leaf+'/'+fn)
   elif normalized(a,False,legacy)!=normalized(b,False,legacy):out['text_substitutions'].append(leaf+'/'+fn)
 (R/n/'build/required-fixture-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(n,'checked',len(out['checked']),'missing',len(out['missing']),'DOM/data_errors',out['structure_errors'],'copy-substitutions',out['text_substitutions'])
 return out
if __name__=='__main__':
 import sys
 for n in(sys.argv[1:]or list(json.loads((R/'profiles.json').read_text()))):audit(n)
