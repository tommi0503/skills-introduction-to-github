"""Independent structural CSS and fixture audit; no sample design styles are read.
This checker is deliberately separate from the main author's validation script.
"""
from pathlib import Path
import argparse, json, re
from lxml import html
BASE=Path(__file__).resolve().parents[1]
REFERENCE=Path('/workspace/work/reference') if Path('/workspace/work/reference').exists() else BASE/'reference'
COLLECTIONS=['vectorbox','seedmark','crossrail','meridian-deck','onboard-docket']
TAX=json.loads((REFERENCE/'contract/taxonomy.json').read_text())
SHARED=json.loads((REFERENCE/'contract/kit-tokens.json').read_text())['tokens']
PALETTE=set(json.loads((REFERENCE/'contract/palette.json').read_text())['light'])
STEPS=set(json.loads((REFERENCE/'contract/type-steps.json').read_text()))
GOLD={
 'card':('confetti','card-2-quiet card-3-icon3d card-3-line card-3-on card-4 card-5-tone'.split()),
 'callout':('annual','callout callout-icon callout-stack'.split()),
 'chart-area':('annual','area-1 areas-2 areas-stacked-3 area-3pt'.split()),
 'chart-bar':('confetti','bars-12 bars-6 bars-3 bars-h-5 bars-h-8 bars-2'.split()),
 'chart-donut':('amethyst','donut donuts-3 donuts-4 donut-0 donut-100'.split()),
 'chart-line':('amethyst','lines-12 lines-6 lines-3 lines-flat'.split())}
ROOTS=set(sum([c['roots'] for c in TAX['contracts']],[]))
ALLOWED_CLASSES=set(TAX['foundation']['classes'])|set(TAX['parts'])|ROOTS|{'to-r','to-d','to-l','to-u'}
for c in TAX['contracts']:
 ALLOWED_CLASSES.update(re.findall(r'\.([a-z][a-z0-9-]*)',c['structure']))
 for cls in re.findall(r'class="([^"]+)"',c['structure']):ALLOWED_CLASSES.update(cls.split())
ALLOWED_CLASSES.update('tone-'+str(i) for i in range(1,6))
DATAVARS={'--max','--v','--xmax','--ymax','--x','--y','--r','--n','--cols','--from','--to','--target','--low','--high','--a','--b','--at','--mood','--next','--tilt','--x1','--y1','--x2','--y2'}|{'--v'+str(i) for i in range(1,9)}


def strip_comments(s):
 return re.sub(r'/\*.*?\*/','',s,flags=re.S)


def split_top(s,sep=','):
 result=[];start=0;depth=0;quote=None;escape=False
 for i,c in enumerate(s):
  if quote:
   if escape:escape=False
   elif c=='\\':escape=True
   elif c==quote:quote=None
   continue
  if c in ['"',"'"]:quote=c
  elif c in '([':depth+=1
  elif c in ')]':depth-=1
  elif c==sep and depth==0:result.append(s[start:i].strip());start=i+1
 result.append(s[start:].strip());return [x for x in result if x]


def parse_rules(s,offset=0):
 """Return (prelude, block, line) with balanced strings/comments/parentheses."""
 s=strip_comments(s);out=[];pos=0
 while pos<len(s):
  while pos<len(s) and s[pos].isspace():pos+=1
  if pos>=len(s):break
  start=pos;quote=None;escape=False;depth=0
  while pos<len(s):
   c=s[pos]
   if quote:
    if escape:escape=False
    elif c=='\\':escape=True
    elif c==quote:quote=None
   elif c in ['"',"'"]:quote=c
   elif c in '([':depth+=1
   elif c in ')]':depth-=1
   elif depth==0 and c in '{;':break
   pos+=1
  if pos>=len(s):
   if s[start:].strip():out.append(('!PARSE',s[start:],s[:start].count('\n')+1+offset))
   break
  prelude=s[start:pos].strip();line=s[:start].count('\n')+1+offset
  if s[pos]==';':out.append((prelude,'',line));pos+=1;continue
  pos+=1;blockstart=pos;braces=1;quote=None;escape=False
  while pos<len(s) and braces:
   c=s[pos]
   if quote:
    if escape:escape=False
    elif c=='\\':escape=True
    elif c==quote:quote=None
   elif c in ['"',"'"]:quote=c
   elif c=='{':braces+=1
   elif c=='}':braces-=1
   pos+=1
  if braces:out.append(('!PARSE',prelude,line));break
  out.append((prelude,s[blockstart:pos-1],line))
 return out


def declarations(block):
 for d in split_top(block,';'):
  if ':' in d:
   p,v=d.split(':',1);yield p.strip().lower(),v.strip()


def normal_golden(s,kid):
 s=s.replace('\r\n','\n').replace('\r','\n')
 s=re.sub(r'data-el="(?:annual|confetti|amethyst|'+re.escape(kid)+')-','data-el="COLLECTION-',s)
 return s.strip()


def audit(kid):
 project=BASE/(kid+'-project');kit=project/kid
 findings=[];counts={'elementCss':0,'goldenFixtures':0,'otherFixtures':0}
 def finding(severity,rule,file,detail,line=None):
  obj={'severity':severity,'rule':rule,'file':str(file.relative_to(project)),'detail':detail}
  if line is not None:obj['line']=line
  findings.append(obj)
 metadata={}
 for f in kit.rglob('*.json'):
  try:metadata[f]=json.loads(f.read_text())
  except Exception as e:finding('error','json-parse',f,str(e))
 known=set(SHARED)|PALETTE|DATAVARS|{'--type-'+str(int(n)) for n in STEPS}|{'--radius-lg'}
 for obj in metadata.values():
  for key in ['extensions','tokenDefaults','registrations']:known.update(obj.get(key,{}))
 for f in kit.rglob('*.css'):
  css=f.read_text();localdecl=set(re.findall(r'(--[A-Za-z0-9_-]+)\s*:',strip_comments(css)));known_here=known|localdecl
  is_element=f.name=='element.css';name=f.parent.name
  if is_element:counts['elementCss']+=1
  scope=f'[data-el="{kid}-{name}"]'
  def walk(text,offset=0):
   for prelude,block,line in parse_rules(text,offset):
    if prelude=='!PARSE':finding('error','css-balanced-syntax',f,block[:120],line);continue
    if prelude.startswith('@'):
     ar=re.match(r'@([\w-]+)',prelude)
     if not ar or ar.group(1) not in {'container','media','supports'}:finding('error','at-rule',f,prelude,line)
     else:walk(block,line-1)
     continue
    if 'container' in prelude and not prelude.startswith('@') and re.search(r'\bcontainer\s*\(',prelude):finding('error','missing-at-container',f,prelude,line)
    for sel in split_top(prelude):
     classes=set(re.findall(r'(?<![\w-])\.([a-z][a-z0-9-]*)',sel))
     invented=classes-ALLOWED_CLASSES
     if invented:finding('error','new-class',f,{'selector':sel,'classes':sorted(invented)},line)
     if is_element:
      compact=re.sub(r"\[data-el='([^']+)'\]",r'[data-el="\1"]',sel)
      if scope not in compact:finding('error','selector-scope',f,sel,line)
      elif re.search(re.escape(scope)+r'\s*[+~]',compact):finding('error','sibling-outside-scope',f,sel,line)
      if re.search(r':not\([^)]*'+re.escape(scope),compact):finding('warning','negative-scope-review',f,sel,line)
     if f.name=='foundation.css':
      conflicts=classes & (ROOTS-set(TAX['foundation']['classes']))
      if conflicts:finding('error','foundation-element-root',f,{'selector':sel,'classes':sorted(conflicts)},line)
    for prop,value in declarations(block):
     if prop.startswith('--') and prop not in SHARED and prop in PALETTE:finding('error','palette-redefined',f,prop,line)
     if prop=='font-size' and is_element:
      m=re.fullmatch(r'var\(--type-(\d+)\)(?:\s*!important)?',value)
      if not m or int(m.group(1)) not in STEPS:finding('error','font-size-step',f,value,line)
     if prop in {'font-family','font-weight','line-height','letter-spacing'} and not prop.startswith('--'):
      if not re.search(r'var\(--',value) and value not in {'inherit','normal'}:finding('error','type-property-token',f,{'property':prop,'value':value},line)
     if prop in {'font-family'} and is_element and value in {'inherit','normal'}:finding('warning','inherited-font-review',f,value,line)
     if prop in {'margin','margin-top','margin-bottom','margin-left','margin-right','margin-inline','margin-block','padding','padding-top','padding-bottom','padding-left','padding-right','padding-inline','padding-block','gap','row-gap','column-gap'}:
      remainder=re.sub(r'(?:calc|min|max)\([^;]*?\)','',value)
      remainder=re.sub(r'var\([^)]*\)','',remainder)
      if re.search(r'(?<![\w-])(?:[1-9]\d*(?:\.\d+)?|0\.\d+)(?:px|rem|em|%)',remainder):
       if any(('var('+t+')') in value for t in DATAVARS):finding('warning','geometry-spacing-review',f,{'property':prop,'value':value},line)
       else:finding('error','spacing-token',f,{'property':prop,'value':value},line)
     if prop=='border-radius':
      if not re.search(r'var\(--',value) and not re.fullmatch(r'(?:0|50%|100%|999px|inherit)(?:[ /]+(?:0|50%|100%|999px))*',value):finding('error','radius-token',f,value,line)
     if is_element and re.search(r'var\(--text-(?:title|lead|body|name|label|figure)',value):finding('error','page-role-size',f,value,line)
     if re.search(r'\b(?:rgb|rgba|hsl|hsla|oklch|oklab|lab|lch)\s*\(|#[0-9A-Fa-f]{3,8}\b',value):
      if not (f.name=='tokens.css' and prop in {'--page','--ink'}):finding('error','literal-color',f,{'property':prop,'value':value},line)
     if prop in {'color','background','background-color','fill','stroke','border-color','outline-color'}:
      # Transparent/currentColor are neutral drawing mechanics, not a theme color.
      colors=set(re.findall(r'\b(?:white|black|red|blue|green|yellow|orange|purple|gray|grey|navy|teal|lime|silver|aqua|fuchsia|maroon|olive)\b',re.sub(r'var\([^)]*\)','',value),re.I))
      if colors:finding('error','named-color',f,{'property':prop,'value':value},line)
     for token in re.findall(r'var\(\s*(--[A-Za-z0-9_-]+)',value):
      if token not in known_here:finding('error','unknown-token',f,{'property':prop,'token':token},line)
  walk(css)
  if re.search(r'\burl\s*\(',strip_comments(css),re.I):finding('error','external-resource',f,'url()')
  if is_element and '@container' not in css:finding('warning','missing-container-response',f,'No explicit @container responsive rule')
 for c in TAX['contracts']:
  name=c['category'].split('.')[-1];ep=kit/'elements'/name
  for missing in ['element.css','element.json','description.md']:
   if not (ep/missing).exists():finding('incomplete','missing-file',ep/missing,'Not yet written')
  fixtures=list((ep/'fixtures').glob('*.html'))
  for f in fixtures:
   text=f.read_text();isgold=name in GOLD and f.stem in GOLD[name][1]
   if isgold:
    counts['goldenFixtures']+=1;sample=GOLD[name][0];source=REFERENCE/'samples'/sample/'elements'/name/'fixtures'/f.name
    if normal_golden(text,kid)!=normal_golden(source.read_text(),kid):finding('error','golden-exact',f,'Markup/data differ beyond data-el and line endings')
   else:counts['otherFixtures']+=1
   try:
    fragments=html.fragments_fromstring(text);roots=[x for x in fragments if not isinstance(x,str) and isinstance(x.tag,str)]
    if len(roots)!=1:finding('error','fixture-root-count',f,len(roots))
    for root in roots:
     if not isgold:
      placement=dict(declarations(root.get('style','')))
      if not re.search(r'\bspan\s+12\b',placement.get('grid-column','')) or not re.search(r'\bspan\s+6\b',placement.get('grid-row','')):
       finding('error','fixture-root-grid',f,{'grid-column':placement.get('grid-column'),'grid-row':placement.get('grid-row')})
     for el in root.iter():
      if not isinstance(el.tag,str):continue
      invented=set(el.get('class','').split())-ALLOWED_CLASSES
      if invented:finding('error','fixture-new-class',f,sorted(invented))
      data=el.get('data-el','')
      if data and not data.startswith(kid+'-'):finding('error','fixture-scope-id',f,data)
      if 'icon' in el.get('class','').split() and ''.join(el.itertext()).strip():
       if not (isgold and name=='card' and f.stem=='card-4'):finding('warning','nonempty-icon-review',f,''.join(el.itertext()).strip())
   except Exception as e:finding('error','fixture-html-parse',f,str(e))
 result={'collection':kid,'counts':counts,'findings':findings,'summary':{level:sum(x['severity']==level for x in findings) for level in ['error','warning','incomplete']},'limitations':'Static local audit; browser geometry and upstream Rhetis intake are separate.'}
 return result

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('collections',nargs='*',default=COLLECTIONS);a=p.parse_args()
 for kid in a.collections:
  r=audit(kid);target=BASE/'qa'/(kid+'-audit.json');target.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(kid,r['counts'],r['summary'])
