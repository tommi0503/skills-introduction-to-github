"""Read-only supplementary contract audit. Writes only integration-contracts/*.json.

README + taxonomy are normative. This is deliberately separate from audit.py's
selector scope/type/6-character-copy checks and from the final visual review.
Use --partial while another owner is adding folders; missing files become pending.
"""
from pathlib import Path
import argparse,collections,datetime,hashlib,json,re,sys
from lxml import html,etree
from audit import blocks as cssblocks
ROOT=Path(__file__).resolve().parents[1];REF=Path('/workspace/work/reference')
TAX=json.loads((REF/'contract/taxonomy.json').read_text());SHARED=json.loads((REF/'contract/kit-tokens.json').read_text())['tokens']
CONTRACT={x['category'].split('.',1)[1]:x for x in TAX['contracts']}
FOUND=set(TAX['foundation']['classes']);WRAPPERS={'group','stack','split'};MEDIA={'icon','seat','avatar','portrait','logo','back'}
PALETTE={'--page','--ink','--good','--warn','--bad'}|{f'--n-{i}' for i in range(1,10)}|{f'--a{i}' for i in range(1,5)}|{f'--a{i}-on' for i in range(1,5)}|{f'--a{i}-{j}{s}' for i in range(1,5) for j in range(1,10) for s in ['','-soft','-muted']}
FONTS={'Pretendard Variable','NanumMyeongjo','Nanum Pen','SUITE','Freesentation','ChosunIlboMyungjo','JoseonGulim','JoseonPalace','Noto Sans','Noto Sans KR','Pretendard','Do Hyeon','Montserrat','Nanum Gothic Coding'}
GOLD={'card':('confetti',['card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone']),'callout':('annual',['callout','callout-icon','callout-stack']),'chart-area':('annual',['area-1','areas-2','areas-stacked-3','area-3pt']),'chart-bar':('confetti',['bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2']),'chart-donut':('amethyst',['donut','donuts-3','donuts-4','donut-0','donut-100']),'chart-line':('amethyst',['lines-12','lines-6','lines-3','lines-flat'])}
# Classes admitted by each structure, expanded rank suffixes, plus explicitly
# admitted foundation composition/media parts. No collection is the allow-list.
ALLOWED={}
for leaf,c in CONTRACT.items():
 names=set(re.findall(r'\.([A-Za-z][\w-]*)',c['structure']))|set(c['roots'])|set(TAX['parts'])
 for value in re.findall(r'class="([^"]+)"',c['structure']):names.update(value.split())
 if leaf in ['flowchart','swimlane']:names.update(['to-r','to-d','to-l','to-u'])
 for f in (REF/'samples').glob('*/elements/'+leaf+'/fixtures/*.html'):
  for value in re.findall(r'class="([^"]+)"',f.read_text()):names.update(value.split())
 if leaf in ['card','pill','metric']:names|=set(TAX['parts'])
 names.discard('tone-N');names.discard('tone-1');names|={f'tone-{n}' for n in range(1,10)} if 'tone-' in c['structure'] else set()
 ALLOWED[leaf]=names|MEDIA|WRAPPERS|{'col','two','three','wide-left'}
ROOT_VARIANTS={'card':{'on','quiet','line'}|{f'tone-{i}' for i in range(1,6)},'pill':{'on','quiet','line'},'list':{'check','num','divided'},'quote':{'big'},'headline':{'big','center','on'},'prose':{'lead','cols','quiet'},'bars':{'h'},'steps':{'col'},'track':{'alt','col'},'matrix':{'swot'},'plan':{'on'},'stacks':{'pct','h'},'areas':{'stacked'},'scatter':{'bubble'},'spark':{'bars','up','down'},'heat':{'calendar'},'waffle':{'figures'},'slope':{'dumbbell'},'code':{'numbered'}}
ROOT_TO=collections.defaultdict(list)
for leaf,c in CONTRACT.items():
 for root in c['roots']:ROOT_TO[root].append(leaf)
def cls(e):return set(e.get('class','').split())
def elems(e):return [c for c in e if isinstance(c.tag,str)]
def direct(e,c):return [x for x in elems(e) if c in cls(x)]
def styles(s):
 # Declaration splitter respects quoted strings and nested function arguments.
 result={};buf='';depth=0;quote=None
 for ch in s+';':
  if quote:
   buf+=ch
   if ch==quote and not buf.endswith('\\'+ch):quote=None
  elif ch in ['"',"'"]:quote=ch;buf+=ch
  elif ch=='(':depth+=1;buf+=ch
  elif ch==')':depth-=1;buf+=ch
  elif ch==';' and depth==0:
   if ':' in buf:
    name,value=buf.split(':',1);result[name.strip()]=value.strip()
   buf=''
  else:buf+=ch
 return result
def sign(e,text=True):
 if not isinstance(e.tag,str):return None
 attrs={k:('COLLECTION-'+v.rsplit('-',1)[-1] if k=='data-el' else v) for k,v in e.attrib.items() if k!='data-el'}
 # data-el is the single admitted attribute normalisation. Min comments are not nodes.
 return [e.tag,sorted(attrs.items()),e.text if text else None,[sign(c,text) for c in elems(e)],e.tail if text else None]
def sign_visible(e):
 # Formatting-only whitespace between nodes is not fixture wording. Preserve each
 # text/tail position so moving words into/out of an inline bold is still a change.
 if not isinstance(e.tag,str):return None
 attrs={k:v for k,v in e.attrib.items() if k!='data-el'}
 clean=lambda value:re.sub(r'\s+','',value or '')
 return [e.tag,sorted(attrs.items()),clean(e.text),[sign_visible(c)for c in elems(e)],clean(e.tail)]
def fragment(s):return html.fragment_fromstring(s,create_parent='audit-fragment')
def audit(k,partial=False):
 P=ROOT/(k+'-project');K=P/k;errors=[];candidates=[];exceptions=[];pending=[];counts=collections.Counter();snapshot={}
 def add(code,f,detail,node=None,level='error'):
  row={'code':code,'file':str(f.relative_to(ROOT)),'detail':detail}
  if node is not None:row['node']=etree.ElementTree(node).getpath(node)
  {'error':errors,'candidate':candidates,'exception':exceptions,'pending':pending}[level].append(row)
 def read(f):
  data=f.read_bytes();digest=hashlib.sha256(data).hexdigest()
  if str(f) in snapshot and snapshot[str(f)]!=digest:add('concurrent-source-change',f,'file changed between reads; rerun before final integration',level='candidate')
  snapshot.setdefault(str(f),digest);return data.decode()
 def missing(f,detail):add('missing-file',f,detail,level='pending' if partial else 'error')
 def require(n,children,f,label):
  for child in children:
   if not direct(n,child):add('required-child',f,f'{label} requires direct .{child}',n,level='candidate' if child in ['note','mark','kick'] else 'error')
 def number(n,var,f,low=None,high=None):
  v=styles(n.get('style','')).get(var)
  if v is None:add('chart-data',f,f'missing {var}',n);return None
  try:v=float(v)
  except ValueError:add('chart-data',f,f'{var} must be a numeric datum: {v}',n);return None
  if (low is not None and v<low) or (high is not None and v>high):add('chart-range',f,f'{var}={v} outside {low}..{high}',n)
  return v
 def structure(n,leaf,f):
  cs=cls(n);c=CONTRACT[leaf];roots=set(c['roots'])
  if not cs&roots:add('root-class',f,f'data-el {leaf} requires one of {sorted(roots)}',n);return
  root=next(x for x in c['roots'] if x in cs)
  extra=cs-{root}-ROOT_VARIANTS.get(root,set())
  if extra:add('root-variant',f,f'.{root} has unnamed variants {sorted(extra)}',n)
  def count(part,a,b):
   v=len(direct(n,part))
   if not a<=v<=b:add('member-count',f,f'{leaf} .{part}: {v}, requires {a}..{b}',n)
  member={'list':('item',2,8),'chart-bar':('bar',2,12),'chart-line':('pt',3,12),'steps':('step',2,6),'timeline':('stop',3,8),'cycle':('node',3,6),'hub':('spoke',3,6),'funnel':('stage',3,6),'pyramid':('level',3,5),'venn':('set',2,3),'hierarchy':('branch',2,4),'architecture':('layer',2,5),'chart-stack':('sbar',2,12),'chart-waterfall':('move',3,10),'chart-scatter':('dot',3,24),'slope':('pair',2,8),'roadmap':('lane',2,6),'swimlane':('lane',2,5),'concentric':('ring',2,4),'journey':('stage',3,7),'mindmap':('branch',2,6),'positioning':('mark',2,12),'network':('node',3,12),'balance':('pan',2,2),'matrix':('cell',4,4),'matrix-nine':('cell',9,9),'treemap':('branch',1,5),'sankey':('branch',2,6),'legend':('key',1,99)}
  if leaf in member:count(*member[leaf])
  if leaf=='prose':
   v=len([x for x in elems(n) if x.tag=='p'])
   if not 1<=v<=4:add('paragraph-count',f,f'prose requires 1..4 direct p, got {v}',n)
  required={'card':['parts'],'pill':['parts'],'quote':['by'],'headline':[],'delta':['from','to'],'table':['table'],'cycle':['core'],'hub':['core'],'hierarchy':['root'],'versus':['vs'],'radar':[],'waffle':['units','fig','name'],'balance':['fulcrum'],'mindmap':['core'],'decision-tree':['q','opts'],'code':['lines']}
  require(n,required.get(leaf,[]),f,leaf)
  if leaf=='headline' and not any(x.tag=='h2' for x in elems(n)):add('heading-tag',f,'headline requires direct h2',n)
  if leaf=='quote' and not any(x.tag=='blockquote' for x in elems(n)):add('quote-tag',f,'quote requires direct blockquote',n)
  if leaf=='callout' and not any(x.tag=='p' for x in elems(n)):add('sentence-tag',f,'callout requires direct p',n)
  if leaf=='image-frame' and not any('seat' in cls(x) and x.get('data-ph') is not None for x in elems(n)):add('image-seat',f,'frame requires direct .seat[data-ph]',n)
  if leaf=='table':
   for tb in direct(n,'table'):
    if tb.tag!='table' or not tb.xpath('./thead') or not tb.xpath('./tbody'):add('table-sections',f,'table requires explicit thead and tbody',tb)
  if leaf in ['matrix','matrix-nine','positioning'] and not (leaf=='matrix' and 'swot' in cs):
   for axis in ['axis-x','axis-y']:
    for a in direct(n,axis):
     expected=3 if leaf=='matrix-nine' else 2
     if len(elems(a))!=expected:add('axis-label-count',f,f'{axis} requires {expected} labels',a)
    if not direct(n,axis):add('axis-missing',f,f'missing {axis}',n)
  if leaf=='matrix' and 'swot' in cs:
   for cell in direct(n,'cell'):require(cell,['kick','name','list'],f,'SWOT cell')
  rows={'list':('item',['name','note']),'steps':('step',['mark','name','note']),'timeline':('stop',['kick','name','note']),'hub':('spoke',['mark','name','note']),'funnel':('stage',['name','fig']),'pyramid':('level',['name','note']),'agenda':('entry',['mark','name','note'])}
  if leaf in rows:
   part,req=rows[leaf]
   for r in direct(n,part):require(r,req,f,leaf+' '+part)
  for multi,single,a,b in [('stats','stat',1,6),('donuts','donut',1,4),('plans','plan',1,4),('people','person',1,6),('bullets','bullet',1,6)]:
   if multi in cs:
    v=len(direct(n,single))
    if not a<=v<=b:add('member-count',f,f'{multi}: {v} .{single}; requires {a}..{b}',n)
  if 'plan' in cs:
   require(n,['name','price','list'],f,'plan')
   for listing in direct(n,'list'):
    if 'check' not in cls(listing):add('pricing-check-list',f,'plan benefits require .list.check',listing)
  if 'stat' in cs:require(n,['parts'],f,'stat')
  if 'donut' in cs:require(n,['fig','name'],f,'donut');number(n,'--v',f,0,100)
  if 'meter' in cs:require(n,['name','fig'],f,'meter');number(n,'--v',f,0,100)
  if leaf in ['chart-bar','chart-line','chart-area','chart-stack','chart-waterfall','sparkline','radar','slope'] and not (leaf=='chart-stack' and 'pct' in cs):number(n,'--max',f,0)
  if leaf=='chart-area':
   count('series',1,4);counts_pt=[]
   for se in direct(n,'series'):
    pts=direct(se,'pt');counts_pt.append(len(pts))
    if not 3<=len(pts)<=12:add('point-count',f,f'area series points {len(pts)} requires3..12',se)
    for pt in pts:number(pt,'--v',f)
   axis=direct(n,'axis')
   if len(axis)!=1 or any(len(elems(axis[0]))!=v for v in counts_pt):add('area-axis-count',f,'one axis with one label per series point required',n)
  if leaf=='chart-stack':
   for bar in direct(n,'sbar'):
    segs=direct(bar,'seg')
    if not 2<=len(segs)<=5:add('segment-count',f,f'stack segments {len(segs)} requires2..5',bar)
    vals=[number(x,'--v',f,0) for x in segs]
    if 'pct' in cs and None not in vals and abs(sum(vals)-100)>.001:add('percent-total',f,f'percent stack sum {sum(vals)} !=100',bar)
  if leaf in ['chart-bar','chart-line','funnel']:
   part={'chart-bar':'bar','chart-line':'pt','funnel':'stage'}[leaf]
   for e in direct(n,part):number(e,'--v',f,0,100 if leaf=='funnel' else None)
  if leaf=='sparkline':
   spans=[x for x in elems(n) if x.tag=='span']
   if not 5<=len(spans)<=24:add('spark-count',f,f'spark span count {len(spans)} requires5..24',n)
   for e in spans:number(e,'--v',f)
  if leaf=='chart-waterfall':
   for e in direct(n,'move'):number(e,'--from',f);number(e,'--to',f)
  if leaf=='radar':
   ax=direct(n,'axis');se=direct(n,'series');v=number(n,'--n',f,3,8)
   if len(ax)!=v or not 1<=len(se)<=3:add('radar-members',f,f'axes={len(ax)} n={v} series={len(se)}',n)
  if 'bullet' in cs:
   number(n,'--v',f,0,100);number(n,'--target',f,0,100)
   for optional in ['--low','--high']:
    if optional in styles(n.get('style','')):number(n,optional,f,0,100)
  if leaf=='journey':
   for stage in direct(n,'stage'):
    number(stage,'--mood',f,0,100)
    if '--next' in styles(stage.get('style','')):number(stage,'--next',f,0,100)
  if leaf=='radar':
   for series in direct(n,'series'):
    for axis in range(1,int(v or 0)+1):number(series,'--v'+str(axis),f,0)
  if leaf=='network':count('link',2,20)
 def htmlcheck(f,fixture=False,foundation=False,golden=False):
  text=read(f)
  try:d=fragment(text)
  except Exception as e:add('html-parse',f,str(e));return
  reference_styles=set();gold_icons={}
  if fixture and not foundation:
   for rf in (REF/'samples').glob('*/elements/'+f.parent.parent.name+'/fixtures/'+f.name):
    rd=fragment(rf.read_text())
    if elems(rd):reference_styles.add(elems(rd)[0].get('style',''))
    if golden:
     gold_icons={etree.ElementTree(x).getpath(x):x.text_content() for x in rd.iter() if isinstance(x.tag,str) and 'icon' in cls(x) and 'seat' not in cls(x)}
  if fixture:
   if len(elems(d))!=1:add('fixture-body-child',f,f'expected one root, got {len(elems(d))}')
   elif not foundation and (not re.search(r'grid-column\s*:\s*1\s*/\s*span\s+12',elems(d)[0].get('style','')) or not re.search(r'grid-row\s*:\s*1\s*/\s*span\s+6',elems(d)[0].get('style',''))):add('fixture-grid',f,'top-level root differs from README12x6 origin placement',elems(d)[0],level='exception' if elems(d)[0].get('style','') in reference_styles else 'error')
   if not re.match(r'\s*<!--\s*min\s*:',text):add('fixture-min',f,'first line must declare min')
  for e in d.iter():
   if not isinstance(e.tag,str) or e.tag in ['audit-fragment','html','head','body','meta','title','link','script']:continue
   if e.tag in ['style','svg','img','canvas','iframe']:add('forbidden-markup',f,f'unadmitted {e.tag}',e)
   cs=cls(e);own=e.get('data-el');owner=next((a.get('data-el') for a in [e]+list(e.iterancestors()) if a.get('data-el')),None)
   leaf=owner[len(k)+1:] if owner and owner.startswith(k+'-') else None
   if own:
    if not own.startswith(k+'-') or leaf not in CONTRACT:add('data-el',f,f'unknown/wrong collection root {own}',e);continue
    structure(e,leaf,f);counts['elementInstances']+=1
   if owner and leaf in CONTRACT:
    illegal=cs-ALLOWED[leaf]
    if illegal:add('contract-class',f,f'{leaf} disallows {sorted(illegal)}',e)
   elif cs-FOUND:add('foundation-class',f,f'outside element root disallows {sorted(cs-FOUND)}',e)
   if not own:
    for root in cs&set(ROOT_TO):
     if leaf and leaf not in ROOT_TO[root] and not (leaf=='code' and root=='lines'):add('nested-data-el',f,f'nested .{root} needs own data-el',e)
     elif leaf is None and root not in FOUND:add('missing-data-el',f,f'.{root} needs own data-el',e)
   if 'seat' in cs and e.get('data-ph') is None:add('seat-number',f,'seat needs data-ph',e)
   if 'icon' in cs and 'seat' not in cs:
    if e.text_content().strip() or elems(e):add('nonempty-icon',f,'icon must be empty Lucide host',e,level='exception' if golden and gold_icons.get(etree.ElementTree(e).getpath(e))==e.text_content() else 'error')
    elif e.get('data-icon') and not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',e.get('data-icon')):add('icon-name',f,'Lucide name must be kebab-case',e)
    elif not e.get('data-icon'):add('icon-name-missing',f,'empty icon lacks data-icon',e,level='candidate')
   st=styles(e.get('style',''))
   for prop,value in st.items():
    allowed=prop in ['grid-column','grid-row'] or prop in {'--max','--v','--from','--to','--xmax','--ymax','--x','--y','--r','--cols','--target','--low','--high','--a','--b','--at','--mood','--next','--tilt','--n','--x1','--y1','--x2','--y2'} or bool(re.fullmatch(r'--v[1-8]',prop))
    if not allowed:add('inline-design-style',f,f'{prop}:{value}',e,level='exception' if golden else 'error')
   if e.getparent() is not None and 'body' in cls(e.getparent()):
    if not all(x in st for x in ['grid-column','grid-row']):add('body-grid-placement',f,'direct body child needs grid-column and grid-row',e)
   if {'deco','foot'}<=cs:add('foundation-device-meaning',f,'.deco.foot is not a named foundation variation',e,level='candidate')
  
  counts['htmlFiles']+=1
 def csscheck(f,kit=False):
  s=read(f)
  leaf=f.parent.name if f.parent.name in CONTRACT else None
  try:rules=list(cssblocks(s))
  except AssertionError as exc:add('css-parse',f,str(exc));return
  for selector,body in rules:
   if leaf:
    names=set(re.findall(r'\.([A-Za-z][\w-]*)',selector))
    illegal=names-ALLOWED[leaf]-set(ROOT_TO)
    if illegal:add('css-contract-class',f,f'{leaf} selector has unadmitted classes {sorted(illegal)}: {selector}')
   for prop,val in styles(body).items():
    refs=set(re.findall(r'var\(\s*(--[\w-]+)',val))
    # Colours may be literal only in kit preview --page/--ink declarations.
    literal=bool(re.search(r'#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla|oklch|oklab|lab|lch|color)\s*\(',val))
    if literal and not (kit and prop in ['--page','--ink']):add('palette-literal',f,f'{selector}: {prop}:{val}')
    colorprop=prop in ['color','background','background-color','border-color','outline-color','fill','stroke','stop-color','text-decoration-color','box-shadow','text-shadow','border','border-top','border-bottom','border-left','border-right']
    if colorprop:
     for ref in refs:
      if ref not in PALETTE and ('color' in prop or prop in ['fill','stroke','stop-color']):add('palette-alias-reference',f,f'{prop} uses nonpalette {ref}',level='candidate')
     bare=re.sub(r'var\([^)]*\)|(?:linear|radial|conic)-gradient|\b(?:none|transparent|currentColor|inherit|solid|dashed|dotted|double|inset|outset|calc|min|max|anchor)\b','',val,flags=re.I)
     if re.search(r'\b(?:white|black|red|blue|green|gray|grey|orange|purple|yellow|pink|navy|teal|lime|silver|maroon|aqua|fuchsia)\b',bare,re.I):add('palette-color-name',f,f'{prop}:{val}')
    if prop.startswith('--') and prop not in PALETTE and refs&PALETTE:add('palette-alias-definition',f,f'{prop}:{val}')
    if kit and prop.startswith('--') and prop in PALETTE-{'--page','--ink'}:add('kit-palette-definition',f,f'kit defines supplied palette {prop}')
  counts['cssFiles']+=1
 actual={f.name for f in (K/'elements').glob('*') if f.is_dir()}
 if actual!=set(CONTRACT):add('element-folders',K/'elements',f'missing={sorted(set(CONTRACT)-actual)}, extra={sorted(actual-set(CONTRACT))}',level='pending' if partial else 'error')
 for f in K.rglob('*'):
  if f.is_file() and f.suffix not in ['.css','.json','.md','.html']:add('file-kind',f,'collection allows .css .json .md .html only')
 kitfile=K/'kit/kit.json';kit={}
 if kitfile.exists():
  kit=json.loads(read(kitfile))
  if kit.get('schema')!='rhetis.kit/2' or kit.get('id')!=k:add('kit-schema',kitfile,'schema/id mismatch')
  if kit.get('tokens')!='css/tokens.css' or kit.get('description')!='description.md':add('kit-paths',kitfile,'tokens/description must point to canonical kit source files')
  if not kit.get('label'):add('kit-label',kitfile,'label required')
  ex=kit.get('extensions',{})
  for token,typ in ex.items():
   if not token.startswith('--'+k+'-') or typ=='color' or token in SHARED:add('kit-extension',kitfile,f'invalid extension {token}:{typ}')
   elif typ not in ['font','weight','tracking','length','number']:add('kit-extension-type',kitfile,f'unrecognised extension type {token}:{typ}; README does not enumerate extension-specific types',level='candidate')
  tokens=K/'kit'/kit.get('tokens','css/tokens.css')
  if tokens.exists():
   mode={}
   for sel,body in cssblocks(read(tokens)):
    mode[sel]=styles(body)
   base=mode.get('.slide',{});dark=mode.get('.slide.dark',{})
   for token in SHARED:
    if token not in base:add('kit-shared-token',tokens,f'missing base {token}')
   for token in dark:
    if token not in ['--page','--ink']:add('kit-dark-token',tokens,f'noncolour {token} is redefined outside base .slide')
   for token in ['--page','--ink']:
    if token not in dark:add('kit-dark-color',tokens,f'missing dark {token}')
   for token in base:
    if token not in SHARED and token not in ex:add('kit-undeclared-token',tokens,f'{token} absent from extensions')
   for token in ex:
    if token not in base:add('kit-extension-value',tokens,f'{token} no base value')
   for token,typ in {**SHARED,**ex}.items():
    if typ=='font' and token in base and base[token].strip('"\'') not in FONTS:add('font-family',tokens,f'{token}:{base[token]} not admitted')
  else:missing(tokens,'kit tokens')
 else:missing(kitfile,'kit metadata')
 for folder in [K/'foundation']+[K/'elements'/x for x in sorted(CONTRACT)]:
  foundation=folder.name=='foundation';kind='foundation' if foundation else 'element';mf=folder/(kind+'.json')
  for required in [mf,folder/(kind+'.css'),folder/'description.md']:
   if not required.exists():missing(required,'required collection source')
  if mf.exists():
   m=json.loads(read(mf));expected='rhetis.design-library-'+kind+'-source/1'
   if m.get('schema')!=expected:add('metadata-schema',mf,f'expected {expected}')
   extra=set(m)-{'schema','kit' if foundation else 'contract','registrations','tokenDefaults'}
   if extra:add('metadata-fields',mf,f'unknown metadata fields {sorted(extra)}')
   if foundation and m.get('kit')!=k:add('foundation-kit',mf,'kit mismatch')
   if not foundation and m.get('contract')!=CONTRACT[folder.name]['id']:add('element-contract',mf,f'expected {CONTRACT[folder.name]["id"]}')
   for field in ['registrations','tokenDefaults']:
    if not isinstance(m.get(field),dict):add('metadata-dictionary',mf,f'{field} must be object')
   for token,value in (m.get('tokenDefaults',{}) if isinstance(m.get('tokenDefaults'),dict) else {}).items():
    if not token.startswith('--'+k+'-'):add('token-default-namespace',mf,token)
    if set(re.findall(r'var\(\s*(--[\w-]+)',str(value)))&PALETTE:add('token-default-color-alias',mf,f'{token}:{value}')
    if re.search(r'#[0-9a-fA-F]{3,8}\b|\b(?:rgb|hsl|oklch)\s*\(',str(value)):add('token-default-color',mf,f'{token}:{value}')
   for token,value in (m.get('registrations',{}) if isinstance(m.get('registrations'),dict) else {}).items():
    if '@property '+token not in value:add('registration-rule',mf,f'{token} missing full matching @property rule')
  fixtures=sorted((folder/'fixtures').glob('*.html'))
  if foundation and fixtures and not any('data-ph=' in f.read_text() for f in fixtures):add('foundation-seat',folder,'foundation fixtures together need at least one numbered seat')
  if not foundation and len(fixtures)<2:add('fixture-count',folder,f'{len(fixtures)} <2',level='pending' if partial else 'error')
  for f in fixtures:htmlcheck(f,fixture=True,foundation=foundation,golden=not foundation and folder.name in GOLD and f.stem in GOLD[folder.name][1])
 assemblies=sorted((P/'reassembled').glob('*.html'))
 mapfile=P/'map.json'
 if mapfile.exists():
  mapped=json.loads(read(mapfile))
  expected=len(mapped.get('pages') or {str(i['page']) for i in mapped.get('instances',[]) if i.get('page') is not None})
  if len(assemblies)!=expected:add('assembly-page-count',P/'reassembled',f'{len(assemblies)} assembled pages, map declares {expected}',level='pending' if partial else 'error')
 for f in assemblies:htmlcheck(f)
 counts['assemblyPages']=len(assemblies)
 for f in sorted(K.rglob('*.css')):csscheck(f,kit=f.parent.name=='css' and f.name=='tokens.css')
 for leaf,(sample,names) in GOLD.items():
  for name in names:
   src=REF/'samples'/sample/'elements'/leaf/'fixtures'/(name+'.html');dest=K/'elements'/leaf/'fixtures'/(name+'.html')
   if not dest.exists():missing(dest,'required golden fixture');continue
   a=fragment(src.read_text());b=fragment(read(dest))
   if sign(a,False)!=sign(b,False):add('golden-structure-data',dest,'structure/attributes/style differ after only data-el/min normalisation')
   elif sign_visible(a)!=sign_visible(b):
    add('golden-text-exception',dest,'Visible field text differs; structure and numeric data are checked separately. The precise source-six-character evidence is recorded in integration-golden-text-evidence.json, not inferred from any raw whitespace difference.',level='exception');counts['goldenActualTextDifferences']+=1
   else:
    counts['goldenExact']+=1
    if sign(a,True)!=sign(b,True):counts['goldenFormattingOnly']+=1
    else:counts['goldenRawExact']+=1
   def data_figures(doc):
    rows=[]
    for node in doc.iter():
     if not isinstance(node.tag,str):continue
     parent=node.getparent();pclasses=cls(parent) if parent is not None else set()
     if 'fig' in cls(node) or node.tag=='b' and pclasses&{'bar','pt','seg','move'}:
      rows.append(re.findall(r'-?\d+(?:[,.]\d+)*',node.text_content()))
    return rows
   if data_figures(a)!=data_figures(b):add('golden-figure-data',dest,'numeric figure or chart-point text differs from reference')
   counts['goldenChecked']+=1
 for path,digest in snapshot.items():
  if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=digest:add('concurrent-source-change',Path(path),'file changed during read-only audit; rerun before final integration',level='candidate')
 # Collapse exact duplicate findings from repeated reads, retaining real node locations.
 def unique(xs):return list({json.dumps(x,sort_keys=True):x for x in xs}.values())
 return {'collection':k,'partial':partial,'taxonomyVersion':TAX['version'],'generatedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'referenceSHA256':{n:hashlib.sha256((REF/n).read_bytes()).hexdigest() for n in ['README.md','contract/taxonomy.json','contract/kit-tokens.json']},'counts':dict(counts),'errors':unique(errors),'candidates':unique(candidates),'exceptions':unique(exceptions),'pending':unique(pending),'sourceFileSHA256':{str(Path(n).relative_to(ROOT)):v for n,v in sorted(snapshot.items())},'limits':['Visual semantics, unnamed foundation variant meaning, geometry, contrast and source-copy overlap are not acceptance claims of this script.','Existing audit.py remains responsible for CSS scope, typography token rules and six-character copy checks.','Palette alias references in compound calculations are candidates for review; literal colours and alias definitions are definite findings.','Golden text changes are reported separately; style chart data, numeric figures and complete DOM structure are compared without general normalisation.', 'Missing mark/note/kick is a manual candidate because the reference non-golden examples omit those displayed parts; mandatory root/body/card structure remains strict.', 'A matching non-golden reference root grid is recorded as a sample-vs-README exception. Non-golden inline design and missing nested data-el remain findings even when inherited from a sample.']}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('collections',nargs='*',default=['vectorbox','seedmark','crossrail','meridian-deck','onboard-docket']);ap.add_argument('--partial',action='store_true');a=ap.parse_args();out=ROOT/'integration-contracts';out.mkdir(exist_ok=True);summary=[]
 for k in a.collections:
  r=audit(k,a.partial);(out/(k+'.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');s={x:len(r[x]) for x in ['errors','candidates','exceptions','pending']};summary.append({'collection':k,**s});print(k,s,flush=True)
 (out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
 return int(any(x['errors'] for x in summary))
if __name__=='__main__':sys.exit(main())
