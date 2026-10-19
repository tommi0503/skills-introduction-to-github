#!/usr/bin/env python3
"""Validate the supplied collection's source contract. Browser geometry is reported separately."""
from pathlib import Path
from html.parser import HTMLParser
import json,re,sys
P=Path(__file__).resolve().parent.parent
C=P/'rhetis-business-01'; errors=[]; checks=[]
def check(value,message):
 checks.append({'check':message,'pass':bool(value)})
 if not value: errors.append(message)
class Fragment(HTMLParser):
 def __init__(self):super().__init__();self.depth=0;self.roots=[];self.nodes=[]
 def handle_starttag(self,t,a):
  a=dict(a);self.nodes.append((t,a))
  if self.depth==0:self.roots.append((t,a))
  if t not in ('br','hr','img','input','meta','link','wbr'):self.depth+=1
 def handle_endtag(self,t):
  if t not in ('br','hr','img','input','meta','link','wbr'):self.depth-=1
kit=json.loads((C/'kit/kit.json').read_text());taxonomy=json.loads((P/'contract/taxonomy.json').read_text());required=json.loads((P/'contract/kit-tokens.json').read_text())['tokens'];steps=json.loads((P/'contract/type-steps.json').read_text());tokens=(C/'kit/css/tokens.css').read_text()
check(kit['schema']=='rhetis.kit/2' and kit['id']==C.name,'kit schema and id')
blocks=re.findall(r'\.slide(?:\.dark)?\s*\{([^}]*)\}',tokens)
for token,kind in required.items():
 check(re.search(re.escape(token)+r'\s*:',blocks[0]),'light token '+token)
 if kind=='color':check(re.search(re.escape(token)+r'\s*:',blocks[1]),'dark color '+token)
allowed=set(taxonomy['foundation']['classes'])|set(taxonomy['parts'])|set('card pill callout tag hl list check num divided item quote big by stat stats delta from to bars h bar lines pt donut donuts meter tablebox table pick legend key steps step track stop alt cycle core node hub spoke funnel stage pyramid level matrix axis-x axis-y cell venn set org root branch leaf flowchart start ask end to-r to-d to-l to-u arch layer chip versus side vs plan plans price person people logos frame agenda entry quiet line'.split())|{f'tone-{i}' for i in range(1,6)}
contracts={v['category'].split('.')[-1]:v for v in taxonomy['contracts']};folders=sorted(p.name for p in (C/'elements').iterdir() if p.is_dir());check(set(folders)==set(contracts),'all 31 contract folders, no extras')
fixtures=0
for kind,folder in [('foundation',C/'foundation')]+[('element',C/'elements'/n) for n in folders]:
 meta=json.loads((folder/f'{kind}.json').read_text());css=(folder/f'{kind}.css').read_text();desc=(folder/'description.md').read_text()
 check(meta['schema']==f'rhetis.design-library-{kind}-source/1','schema '+folder.name)
 check(isinstance(meta['registrations'],dict) and isinstance(meta['tokenDefaults'],dict),'registration maps '+folder.name)
 check(bool(desc.strip()) and not re.search('[가-힣]',desc),'English description '+folder.name)
 if kind=='element':check(meta['contract']==contracts[folder.name]['id'],'contract '+folder.name)
 check(not re.search(r'@(?:import|font-face|keyframes|property)\b|url\s*\(',css,re.I),'no forbidden CSS resources '+folder.name)
 for size in re.findall(r'font-size\s*:\s*([^;}]+)',css):check(bool(re.fullmatch(r'var\(--type-(\d+)\)',size.strip())) and int(re.search(r'\d+',size)[0]) in steps,'type step '+folder.name+': '+size)
 for prop,val in re.findall(r'(font-family|font-weight|letter-spacing|line-height|color|background-color|border-radius)\s*:\s*([^;}]+)',css):
  check(not re.search(r'#[0-9a-fA-F]{3,8}\b|\b(?:white|black|red|blue|teal)\b',val),'tokenized '+folder.name+' '+prop)
  if prop in ('font-family','font-weight','letter-spacing'):check('var(' in val or val in ('inherit','normal'),'shared typography '+folder.name+' '+prop)
 if kind=='element':
  check('@container' in css,'responsive '+folder.name)
  for selector in re.findall(r'(?:^|[{}])\s*([^{}]+)\s*\{',css):
   if selector.startswith('@'):continue
   for part in re.split(r',\s*(?=\.[\w-]+\[data-el)',selector):check(f'data-el="{C.name}-{folder.name}"' in part,'scope '+folder.name+' '+part[:90])
 files=list((folder/'fixtures').glob('*.html'));check(len(files)>=(2 if kind=='element' else 1),'fixture count '+folder.name)
 for f in files:
  fixtures+=1;text=f.read_text();check(bool(re.match(r'<!-- min: \d+x\d+(?: \| \d+x\d+)* -->\n',text)),'minimum grid '+str(f.relative_to(C)))
  parser=Fragment();parser.feed(text);check(len(parser.roots)==1,'one fixture root '+str(f.relative_to(C)))
  if kind=='element':
   top=parser.roots[0][1];check(top.get('data-el')==f'{C.name}-{folder.name}','fixture data-el '+str(f.relative_to(C)));check('grid-column:1 / span 12; grid-row:1 / span 6' in top.get('style',''),'fixture placement '+str(f.relative_to(C)))
  for tag,a in parser.nodes:
   check(set(a.get('class','').split())<=allowed,'allowed classes '+str(f.relative_to(C)))
   check(tag not in ('img','script','iframe','canvas','svg'),'no image substrate '+str(f.relative_to(C)))
check(len(folders)==31,'31 elements total')
def luminance(color):
 values=[int(color[i:i+2],16)/255 for i in (1,3,5)]
 values=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in values]
 return sum(v*w for v,w in zip(values,(.2126,.7152,.0722)))
contrastPairs=[('ink','page'),('ink-2','surface'),('mute','page'),('accent','page'),('accent','accent-soft'),('accent-ink','accent')]+[(f'tone-{i}-ink',f'tone-{i}') for i in range(1,6)]
contrast=[]
for mode,block in zip(('light','dark'),blocks):
 palette=dict(re.findall(r'--([\w-]+):\s*(#[\da-fA-F]{6})',block))
 for foreground,background in contrastPairs:
  a,b=sorted((luminance(palette[foreground]),luminance(palette[background])))
  ratio=(b+.05)/(a+.05);contrast.append({'mode':mode,'foreground':foreground,'background':background,'ratio':round(ratio,3)})
  check(ratio>=4.5,'text contrast '+mode+' '+foreground+' / '+background)
summary={'collection':C.name,'elementCount':len(folders),'fixtureCount':fixtures,'checkCount':len(checks),'errors':errors,'passed':not errors,'checks':checks,'contrast':contrast}
(P/'review/collection-contract.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in summary.items() if k!='checks'},ensure_ascii=False,indent=2));sys.exit(bool(errors))
