"""Independent local contract audit; official Rhetis intake is not included in this pack."""
from pathlib import Path
from html.parser import HTMLParser
import json,re
P=Path(__file__).resolve().parents[1];C=P/'strategy-blueprint';errors=[]
def ensure(ok,message):
 if not ok:errors.append(message)
class RootCounter(HTMLParser):
 def __init__(self):super().__init__();self.depth=0;self.roots=0
 def handle_starttag(self,t,a):
  if self.depth==0:self.roots+=1
  if t not in ['br','hr','img','input','meta','link']:self.depth+=1
 def handle_endtag(self,t):self.depth-=1
contracts=json.loads((P/'contract/taxonomy.json').read_text())['contracts'];ids={x['id'] for x in contracts};actual=[]
kit=json.loads((C/'kit/kit.json').read_text());ensure(kit['schema']=='rhetis.kit/2' and kit['id']==C.name,'kit schema/id');token_schema=json.loads((P/'contract/kit-tokens.json').read_text())['tokens'];tokens=(C/'kit/css/tokens.css').read_text();blocks=re.findall(r'\.slide(?:\.dark)?\s*\{([^}]+)',tokens)
for key,kind in token_schema.items():
 ensure(key+':' in blocks[0],f'missing light token {key}')
 if kind=='color':ensure(key+':' in blocks[1],f'missing dark token {key}')
for folder in sorted((C/'elements').iterdir()):
 meta=json.loads((folder/'element.json').read_text());actual.append(meta['contract']);ensure(meta['schema']=='rhetis.design-library-element-source/1',str(folder)+' schema')
 css=(folder/'element.css').read_text();ensure(not re.search(r'@(?:import|font-face|keyframes|property)|url\(',css),'forbidden CSS '+folder.name);ensure(not re.search(r'#[a-fA-F0-9]{3,8}\b|rgba?\(',css),'literal color '+folder.name);ensure(not re.search(r'font-size\s*:\s*(?!var\(--type-)[^;}]+',css),'font size '+folder.name)
 # Parse recursive container rules and verify every comma-separated selector carries data-el.
 def rules(s):
  pos=0
  while pos<len(s):
   begin=s.find('{',pos)
   if begin<0:break
   head=s[pos:begin].strip();d=1;end=begin+1
   while end<len(s) and d:
    d+=(s[end]=='{')-(s[end]=='}');end+=1
   body=s[begin+1:end-1]
   if head.startswith('@'):rules(body)
   else:ensure('data-el="strategy-blueprint-'+folder.name+'"' in head,folder.name+' unscoped '+head[:70])
   pos=end
 rules(re.sub(r'/\*.*?\*/','',css,flags=re.S))
 fixtures=list((folder/'fixtures').glob('*.html'));ensure(len(fixtures)>=2,folder.name+' needs2fixtures')
 for f in fixtures:
  s=f.read_text();ensure(bool(re.match(r'<!-- min: [0-9]+x[0-9]+',s)),str(f)+' min comment');ensure('grid-column:1 / span 12; grid-row:1 / span 6' in s,str(f)+' placement');parser=RootCounter();parser.feed(s);ensure(parser.roots==1 and parser.depth==0,str(f)+' single balanced root');ensure('data-el="strategy-blueprint-'+folder.name+'"' in s,str(f)+' root data-el')
ensure(set(actual)==ids and len(actual)==31,'31 exact contract IDs');f=json.loads((C/'foundation/foundation.json').read_text());ensure(f['schema']=='rhetis.design-library-foundation-source/1' and f['kit']==C.name,'foundation schema')
report={'collection':C.name,'elements':len(actual),'fixtures':len(list(C.glob('elements/*/fixtures/*.html'))),'foundation_fixtures':len(list(C.glob('foundation/fixtures/*.html'))),'shared_tokens':len(token_schema),'errors':errors,'official_intake':'not available in supplied reference pack; local checks only'}
(P/'artifacts/contract-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
