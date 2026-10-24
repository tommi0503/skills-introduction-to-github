"""Contract/file/scope/minimum/golden-fixture checks. Does not replace visual review."""
import argparse,hashlib,json,re
from pathlib import Path
from lxml import html
ROOT=Path(__file__).resolve().parents[1]
GOLDEN={
 'card':('confetti',['card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone']),
 'callout':('annual',['callout','callout-icon','callout-stack']),
 'chart-area':('annual',['area-1','areas-2','areas-stacked-3','area-3pt']),
 'chart-bar':('confetti',['bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2']),
 'chart-donut':('amethyst',['donut','donuts-3','donuts-4','donut-0','donut-100']),
 'chart-line':('amethyst',['lines-12','lines-6','lines-3','lines-flat'])}

def split_selectors(selector):
 depth=0;begin=0;result=[]
 for i,c in enumerate(selector):
  if c in '([':depth+=1
  elif c in ')]':depth-=1
  elif c==','and not depth:result.append(selector[begin:i].strip());begin=i+1
 return result+[selector[begin:].strip()]

def canonical_fixture(path):
 raw=re.sub(r'<!--.*?-->','',path.read_text(),flags=re.S).strip();e=html.fragment_fromstring(raw)
 for node in e.iter():
  if node.get('data-el'):node.set('data-el',node.get('data-el').split('-',1)[-1])
  if 'style'in node.attrib:
   style=re.sub(r'grid-(column|row)\s*:[^;]+;?','',node.get('style','')).strip('; ')
   if style:node.set('style',style)
   else:del node.attrib['style']
  if node.text:node.text=re.sub(r'\s+',' ',node.text).replace('엔터프라이즈','대규모조직').replace('대규모 조직','대규모조직')
  if node.tail:node.tail=re.sub(r'\s+',' ',node.tail)
  if 'icon'in node.get('class','').split()and(node.text or'').strip()=='✹':
   node.text=None;node.set('data-icon','sparkles')
 return e

def main(args):
 taxonomy=json.loads((ROOT/'contract/taxonomy.json').read_text());contracts=taxonomy['contracts'];issues=[];rows=[]
 # Folder names are explicitly preserved in all 56 reference samples.
 reference=ROOT/'reference-contract/samples'
 if not reference.exists():reference=Path('/workspace/work/ref/samples')
 names={p.name:json.loads((p/'element.json').read_text())['contract']for p in(reference/'annual/elements').iterdir()if p.is_dir()}
 for c in json.loads((ROOT/'collections.json').read_text()):
  cid=c['id'];C=ROOT/cid
  if args.collections and cid not in args.collections:continue
  def issue(file,rule,detail):issues.append({'file':str(file.relative_to(ROOT)),'rule':rule,'detail':detail})
  for p in C.rglob('*'):
   if p.is_file()and p.suffix not in ['.css','.json','.md','.html']:issue(p,'file-type',p.suffix)
  for leaf,contract in names.items():
   E=C/'elements'/leaf
   for fname in ['element.css','element.json','description.md']:
    if not(E/fname).exists():issue(E/fname,'missing-file',fname)
   if not(E/'element.css').exists():continue
   data=json.loads((E/'element.json').read_text())
   if data.get('contract')!=contract:issue(E/'element.json','contract-id',data.get('contract'))
   css=re.sub(r'/\*.*?\*/','',(E/'element.css').read_text(),flags=re.S)
   for selector in re.findall(r'([^{}]+)\{',css):
    selector=selector.strip()
    if selector.startswith('@'):
     if not re.match(r'@(container|media|supports)\b',selector):issue(E/'element.css','at-rule',selector[:100])
     continue
    for arm in split_selectors(selector):
     if not re.search(r'\[data-el\s*=\s*[\"\']'+re.escape(cid+'-'+leaf)+r'[\"\']\]',arm):issue(E/'element.css','scope',arm[:180])
     if re.search(r'data-(?:fixture|page)|:has\([^)]*\[style',arm):issue(E/'element.css','fixture-or-page-condition',arm[:180])
   for pattern in [r'font-size\s*:[^;{}]*\b\d+px',r'font-weight\s*:\s*\d',r'(?<![\w-])#[0-9a-fA-F]{3,8}\b',r'rgba?\(',r'\b(?:\d+(?:\.\d+)?)(?:vw|vh)\b',r'url\(']:
    if re.search(pattern,css):issue(E/'element.css','literal-or-external',pattern)
   files=list((E/'fixtures').glob('*.html'))
   if len(files)<2:issue(E/'fixtures','fixture-count',len(files))
   for f in files:
    raw=f.read_text();m=re.match(r'<!--\s*min:\s*(\d+)x(\d+)\s*-->',raw)
    if not m or not(1<=int(m[1])<=12 and 1<=int(m[2])<=6):issue(f,'minimum',raw[:60])
    try:root=html.fragment_fromstring(re.sub(r'<!--.*?-->','',raw,flags=re.S).strip())
    except Exception as e:issue(f,'fixture-root',str(e));continue
    for icon in root.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," icon ")]'):
     if ''.join(icon.itertext()).strip()or len(icon):issue(f,'empty-lucide-slot',html.tostring(icon,encoding='unicode')[:120])
    for node in root.iter():
     if node.get('data-el')and not node.get('data-el').startswith(cid+'-'):issue(f,'foreign-data-el',node.get('data-el'))
   if leaf in GOLDEN:
    sample,required=GOLDEN[leaf]
    for stem in required:
     target=E/'fixtures'/(stem+'.html')
     if not target.exists():issue(target,'golden-fixture-missing',stem);continue
     # Keep the exact semantic DOM, apart from the two recorded conflict repairs.
     old=canonical_fixture(reference/sample/'elements'/leaf/'fixtures'/(stem+'.html'));new=canonical_fixture(target)
     for n in [*old.iter(),*new.iter()]:
      if n.get('data-el'):n.set('data-el',n.get('data-el').split('-')[-1])
     if html.tostring(old)!=html.tostring(new):
      # Attribute order and insignificant whitespace do not change the contract data.
      def signature(e):return(e.tag,tuple(sorted(e.attrib.items())),(e.text or'').strip(),tuple(signature(x)for x in e),(e.tail or'').strip())
      if signature(old)!=signature(new):issue(target,'golden-markup-or-data','Diff requires review; only enterprise text and glyph-to-Lucide repairs are allowed.')
  rows.append({'collection':cid,'elements':len(list((C/'elements').glob('*/element.css'))),'fixtures':len(list(C.glob('**/fixtures/*.html')))})
 report={'collections':rows,'issues':issues};(ROOT/'static-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('collections',nargs='*');main(p.parse_args())
