"""Round5 contract families, independent designs, scopes, fixtures and dependencies."""
import argparse,json,re
from pathlib import Path
from lxml import html
ROOT=Path(__file__).resolve().parents[1]
def split_selectors(s):
 depth=0;start=0;out=[]
 for i,c in enumerate(s):
  if c in '([':depth+=1
  elif c in ')]':depth-=1
  elif c==','and depth==0:out.append(s[start:i]);start=i+1
 return out+[s[start:]]
def main(args):
 families=json.loads((ROOT/'contract/leaves.json').read_text());taxonomy={x['id']:x for x in json.loads((ROOT/'contract/taxonomy.json').read_text())['contracts']};issues=[];rows=[]
 def issue(f,rule,detail):issues.append({'file':str(f.relative_to(ROOT)),'rule':rule,'detail':detail})
 for item in json.loads((ROOT/'collections.json').read_text()):
  cid=item['id'];C=ROOT/cid
  if args.collections and cid not in args.collections:continue
  folders=sorted(p for p in(C/'elements').iterdir()if p.is_dir());known={cid+'-'+p.name for p in folders}
  for p in C.rglob('*'):
   if p.is_file()and p.suffix not in ['.css','.json','.md','.html']:issue(p,'file-type',p.suffix)
  for E in folders:
   family=E.name.split('--',1)[0];key=cid+'-'+E.name
   if family not in families or not re.fullmatch(r'[a-z0-9-]+(?:--[a-z0-9]+(?:-[a-z0-9]+)*)?',E.name):issue(E,'design-folder',E.name);continue
   for name in ['element.css','element.json','description.md']:
    if not(E/name).exists():issue(E/name,'missing-file',name)
   if not(E/'element.json').exists():continue
   data=json.loads((E/'element.json').read_text());contract=families[family]
   if data.get('contract')!=contract:issue(E/'element.json','contract-family',data.get('contract'))
   css=re.sub(r'/\*.*?\*/','',(E/'element.css').read_text(),flags=re.S)
   if 'container-type:size'not in re.sub(r'\s+','',css):issue(E/'element.css','root-container','size container missing')
   for selector in re.findall(r'([^{}]+)\{',css):
    selector=selector.strip()
    if selector.startswith('@'):
     if not re.match(r'@(container|media|supports)\b',selector):issue(E/'element.css','at-rule',selector[:100])
     continue
    for arm in split_selectors(selector):
     if not re.search(r'\[data-el\s*=\s*[\"\']'+re.escape(key)+r'[\"\']\]',arm):issue(E/'element.css','scope',arm[:180])
     if re.search(r'data-(?:fixture|page)|:has\([^)]*\[style',arm):issue(E/'element.css','fixture-or-page-condition',arm[:180])
   for pattern in [r'font-size\s*:[^;{}]*\b\d+px',r'(?<![\w-])#[0-9a-fA-F]{3,8}\b',r'rgba?\(',r'\b(?:\d+(?:\.\d+)?)(?:vw|vh)\b',r'url\(']:
    if re.search(pattern,css):issue(E/'element.css','literal-or-external',pattern)
   for n in re.findall(r'--type-(\d+)',css):
    if int(n)not in json.loads((ROOT/'contract/type-steps.json').read_text()):issue(E/'element.css','type-token',n)
   files=sorted((E/'fixtures').glob('*.html'))
   if len(files)<2:issue(E,'fixture-count',len(files))
   for f in files:
    raw=f.read_text();m=re.match(r'<!--\s*min:\s*(\d+)x(\d+)\s*-->',raw)
    if not m or not(1<=int(m[1])<=12 and 1<=int(m[2])<=6):issue(f,'minimum',raw[:60])
    try:root=html.fragment_fromstring(re.sub(r'<!--.*?-->','',raw,flags=re.S).strip())
    except Exception as exc:issue(f,'fixture-root',str(exc));continue
    wrapped=root.get('class','')in ['group','group two','group three','group col','stack','split','split wide-left']and bool(root.xpath('.//*[@data-el="'+key+'"]'))
    if root.get('data-el')!=key and not wrapped:issue(f,'fixture-key',root.get('data-el'))
    if not wrapped and not set(root.get('class','').split())&set(taxonomy[contract]['roots']):issue(f,'contract-root',root.get('class'))
    for node in root.iter():
     if node.get('data-el')and node.get('data-el')not in known:issue(f,'missing-dependency',node.get('data-el'))
     if 'icon'in node.get('class','').split()and node.get('data-icon')and(len(node)or ''.join(node.itertext()).strip()):issue(f,'empty-lucide-slot',node.get('data-icon'))
   # Shared state ids are optional under Round5. Source-derived fixtures do not
   # impersonate registry states, and the original sample is not a design source.
  rows.append({'collection':cid,'elements':len(folders),'fixtures':sum(len(list((E/'fixtures').glob('*.html')))for E in folders)})
 report={'round':5,'collections':rows,'issues':issues};(ROOT/'static-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2));return bool(issues)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('collections',nargs='*');raise SystemExit(main(p.parse_args()))
