"""Expand a root placeholder to each literal admitted root, retaining at-rule nesting."""
def split_top(s):
 out=[];start=0;depth=0;quote=None
 for i,c in enumerate(s):
  if quote:
   if c==quote and(i==0 or s[i-1]!='\\'):quote=None
  elif c in ['"',"'"]:quote=c
  elif c in '([':depth+=1
  elif c in ')]':depth-=1
  elif c==','and depth==0:out.append(s[start:i].strip());start=i+1
 out.append(s[start:].strip());return[x for x in out if x]
def compile_css(s,roots,leaf):
 out=[];pos=0
 while pos<len(s):
  l=s.find('{',pos)
  if l<0:break
  head=s[pos:l].strip();i=l+1;level=1;quote=None
  while i<len(s)and level:
   c=s[i]
   if quote:
    if c==quote and s[i-1]!='\\':quote=None
   elif c in ['"',"'"]:quote=c
   elif c=='{':level+=1
   elif c=='}':level-=1
   i+=1
  if level:raise ValueError(('unclosed block',leaf,head))
  body=s[l+1:i-1]
  if head.startswith('@'):out.append(head+'{'+compile_css(body,roots,leaf)+'}')
  else:
   arms=[]
   for arm in split_top(head):
    explicit=next((r for r in roots if arm.startswith('$.'+r)and(len(arm)==len(r)+2 or arm[len(r)+2]in '.:#>[ ')),None)
    if explicit:arms.append('.'+explicit+'[data-el="seedmark-'+leaf+'"]'+arm[len(explicit)+2:])
    else:
     if not arm.startswith('$'):raise ValueError(('unscoped author selector',leaf,arm))
     arms.extend('.'+r+'[data-el="seedmark-'+leaf+'"]'+arm[1:]for r in roots)
   out.append(','.join(arms)+'{'+body+'}')
  pos=i
 return'\n'.join(out)
