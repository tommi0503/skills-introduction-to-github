"""Strict six-character source-text exclusion for new fixtures; read-only audit."""
from pathlib import Path
from lxml import html
import re,json,sys,unicodedata,argparse
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('collections',nargs='*')
parser.add_argument('--out',help='Write the same audit as JSON')
args=parser.parse_args()
def norm(s):return re.sub(r'\s+','',unicodedata.normalize('NFKC',s)).casefold()
source=json.loads((ROOT/'reference-texts.json').read_text());grams={}
for row in source:
 s=norm(row['text'])
 for i in range(len(s)-5):grams.setdefault(s[i:i+6],{'collection':row['collection'],'page':row['page']})
issues=[];count=0
for name in args.collections or [x['id']for x in json.loads((ROOT/'collections.json').read_text())]:
 C=ROOT/name
 if not (C/'elements').is_dir():parser.error('Unknown collection: '+name)
 for f in sorted(C.glob('**/fixtures/*.html')):
  count+=1;t=html.fromstring(f.read_text());runs=[]
  semantic={'name','note','fig','kick','key','tag','label','cond','pain','by'}
  for e in t.iter():
   if not isinstance(e.tag,str):continue
   classes=set(e.get('class','').split())
   if e.tag.lower() in {'p','h1','h2','h3','blockquote','td','th','b','small','span'} or classes&semantic:
    # A phrase may cross inline emphasis, but never crosses separate bars, cells or labels.
    runs.append(norm(''.join(e.itertext())))
  hits=sorted({run[i:i+6]for run in runs for i in range(len(run)-5)if run[i:i+6]in grams})
  brands=[b for run in runs for b in re.findall(r'miri|miricom|미리컴|미리디|김미리',run)]
  if hits or brands:issues.append({'file':str(f.relative_to(ROOT)),'matches':hits,'brands':brands})
report=json.dumps({'checked':count,'issues':issues},ensure_ascii=False,indent=2)
if args.out:Path(args.out).write_text(report)
print(report);sys.exit(bool(issues)or not count)
