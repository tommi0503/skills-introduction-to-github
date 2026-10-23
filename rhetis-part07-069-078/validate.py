"""Independent artifact contract audit. It is not the unavailable Rhetis intake."""
from pathlib import Path
import json,re,sys,hashlib
from lxml import html
ROOT=Path(__file__).resolve().parent;REF=Path('/workspace/work/reference') if Path('/workspace/work/reference').exists() else Path(__file__).resolve().parent/'reference'
exec((ROOT/'scaffold.py').read_text().split("if __name__")[0],globals())
TOKENS=json.loads((REF/'contract/kit-tokens.json').read_text())['tokens']
TAX=json.loads((REF/'contract/taxonomy.json').read_text());STEPS=json.loads((REF/'contract/type-steps.json').read_text())

def normal(text,kid):return re.sub(r'data-el="(?:annual|confetti|amethyst|'+re.escape(kid)+')-', 'data-el="ID-',text).replace('\r\n','\n').strip()

def audit(kid):
 P=ROOT/(kid+'-project');K=P/kid;errors=[];warnings=[]
 dirs={p.name for p in (K/'elements').iterdir() if p.is_dir()};expected={c['category'].split('.')[-1] for c in TAX['contracts']}
 if dirs!=expected:errors.append({'rule':'56-folders','missing':sorted(expected-dirs),'extra':sorted(dirs-expected)})
 for p in K.rglob('*'):
  if p.is_file() and p.suffix not in ['.css','.json','.md','.html']:errors.append({'rule':'file-type','file':str(p.relative_to(K))})
 for c in TAX['contracts']:
  name=c['category'].split('.')[-1];E=K/'elements'/name
  for fname in ['element.css','element.json','description.md']:
   if not (E/fname).is_file():errors.append({'rule':'missing','file':str((E/fname).relative_to(K))})
  if not (E/'element.css').exists():continue
  css=(E/'element.css').read_text()
  if f'data-el="{kid}-{name}"' not in css and f"data-el='{kid}-{name}'" not in css:errors.append({'rule':'scope-root','element':name})
  if re.search(r'@(?:import|font-face|keyframes)|\burl\s*\(',css,re.I):errors.append({'rule':'external-or-at-rule','element':name})
  if re.search(r'#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla|oklch|lab)\(',css):errors.append({'rule':'color-literal','element':name})
  for size in re.findall(r'font-size\s*:\s*([^;}]+)',css):
   if not re.fullmatch(r'var\(--type-(\d+)\)',size.strip()) or int(re.search(r'\d+',size).group()) not in STEPS:errors.append({'rule':'type-step','element':name,'value':size})
  for v in re.findall(r'font-weight\s*:\s*([^;}]+)',css):
   if not re.search(r'var\(--',v):errors.append({'rule':'weight-token','element':name,'value':v})
  for v in re.findall(r'(?<!-)line-height\s*:\s*([^;}]+)',css):
   if not re.search(r'var\(--',v):errors.append({'rule':'line-token','element':name,'value':v})
  fixtures=list((E/'fixtures').glob('*.html'))
  if len(fixtures)<2:errors.append({'rule':'fixture-count','element':name,'count':len(fixtures)})
  if name in GOLD:
   sample,names=GOLD[name]
   for n in names:
    p=E/'fixtures'/(n+'.html');src=REF/'samples'/sample/'elements'/name/'fixtures'/(n+'.html')
    if not p.exists() or normal(p.read_text(),kid)!=normal(src.read_text(),kid):errors.append({'rule':'golden-exact','element':name,'fixture':n})
  for f in fixtures:
   txt=f.read_text()
   if not re.match(r'<!--\s*min:',txt):errors.append({'rule':'fixture-min','file':str(f.relative_to(K))})
   try:
    doc=html.fragments_fromstring(txt);roots=[x for x in doc if not isinstance(x,str) and isinstance(x.tag,str)]
    if len(roots)!=1:errors.append({'rule':'one-fixture-root','file':str(f.relative_to(K))})
    for x in roots:
     for el in [x]+list(x.iterdescendants()):
      de=el.get('data-el')
      if de and not de.startswith(kid+'-'):errors.append({'rule':'fixture-data-el','file':str(f.relative_to(K)),'data':de})
   except Exception as e:errors.append({'rule':'fixture-parse','file':str(f.relative_to(K)),'error':str(e)})
 for f in ['kit/kit.json','kit/css/tokens.css','kit/description.md','foundation/foundation.css','foundation/foundation.json','foundation/description.md']:
  if not (K/f).exists():errors.append({'rule':'missing','file':f})
 tp=K/'kit/css/tokens.css'
 if tp.exists():
  txt=tp.read_text()
  for t in TOKENS:
   if t+':' not in re.sub(r'\s+','',txt):errors.append({'rule':'kit-token','token':t})
  if '.slide.dark' not in txt:errors.append({'rule':'dark-kit'})
 for stage in ['replica','reassembled']:
  for f in (P/stage).glob('slide*.html'):
   txt=f.read_text()
   if stage=='reassembled':
    if '<style' in txt: warnings.append({'rule':'reassembly-embedded-style-review','file':f.name})
    if 'data-el=' not in txt and not re.search(r'class="slide[^"]*\bcover\b',txt):errors.append({'rule':'reassembly-no-elements','file':f.name})
 out={'collection':kid,'errors':errors,'warnings':warnings,'elementCount':len(dirs),'fixtureCount':sum(1 for _ in (K/'elements').glob('*/fixtures/*.html')),'note':'Independent local checks; upstream Rhetis intake is not included in reference pack.'}
 (P/'contract-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(kid,'errors',len(errors),'warnings',len(warnings))
 return out
if __name__=='__main__':
 for kid in sys.argv[1:]:audit(kid)
