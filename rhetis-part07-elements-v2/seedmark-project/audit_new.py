from pathlib import Path
import json,re
import tinycss2
P=Path(__file__).parent;C=P/'seedmark';out=[]
def walk(rules,leaf,file):
 for r in rules:
  if r.type=='at-rule'and r.content is not None:walk(tinycss2.parse_rule_list(r.content,skip_whitespace=True,skip_comments=True),leaf,file)
  if r.type!='qualified-rule':continue
  sel=tinycss2.serialize(r.prelude);groups=[];buf=[];depth=0
  for token in r.prelude:
   if token.type=='literal'and token.value==',':groups.append(tinycss2.serialize(buf));buf=[]
   else:buf.append(token)
  groups.append(tinycss2.serialize(buf))
  for s in groups:
   if f'data-el="seedmark-{leaf}"'not in s:out.append({'file':str(file),'rule':'scope','selector':s})
   if '+'in s or '~'in s:out.append({'file':str(file),'rule':'sibling-condition','selector':s})
   if '[style*='in s:out.append({'file':str(file),'rule':'style-value-condition','selector':s})
  for d in tinycss2.parse_declaration_list(r.content,skip_whitespace=True,skip_comments=True):
   if d.type=='error':out.append({'file':str(file),'rule':'parse','message':d.message});continue
   if d.type!='declaration':continue
   v=tinycss2.serialize(d.value).strip()
   if d.name=='font-size'and not(v.startswith('var(--type-')or v.startswith('clamp(')):out.append({'file':str(file),'rule':'font-size','value':v})
   if d.name=='font-family'and not v.startswith('var('):out.append({'file':str(file),'rule':'font-family','value':v})
   if re.search(r'#[0-9a-fA-F]{3,8}\b|\b(?:rgb|hsl|oklch)\(',v):out.append({'file':str(file),'rule':'color-literal','value':v})
for f in(C/'elements').glob('*/element.css'):walk(tinycss2.parse_stylesheet(f.read_text(),skip_whitespace=True,skip_comments=True),f.parent.name,f.relative_to(P))
(P/'new-static-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print('Static findings',len(out));print(out[:20])
