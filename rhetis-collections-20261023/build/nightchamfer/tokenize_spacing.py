from pathlib import Path
import re
C=Path('/workspace/output/nightchamfer')
v={1:'var(--stroke)',3:'calc(var(--gap-sm)/4)',4:'calc(var(--gap-sm)/3)',5:'calc(var(--gap-sm)/2 - var(--stroke))',6:'calc(var(--gap-sm)/2)',7:'calc(var(--gap-sm)/2 + var(--stroke))',8:'calc(var(--gap-sm)*2/3)',9:'calc(var(--gap-sm)*3/4)',10:'calc(var(--gap-sm) - var(--stroke)*2)',12:'var(--gap-sm)',14:'calc(var(--gap)/2 + var(--stroke)*2)',16:'calc(var(--gap)*2/3)',18:'calc(var(--gap-sm)*1.5)',20:'calc(var(--gap) - var(--stroke)*4)',21:'calc(var(--gap) - var(--gap-sm)/4)',22:'calc(var(--gap) - var(--stroke)*2)',23:'calc(var(--gap) - var(--stroke))',24:'var(--gap)',25:'calc(var(--gap) + var(--stroke))',26:'calc(var(--gap) + var(--stroke)*2)',27:'calc(var(--pad) - var(--stroke))',28:'var(--pad)',30:'calc(var(--gap) + var(--gap-sm)/2)',32:'calc(var(--gap) + var(--gap-sm)*2/3)',34:'calc(var(--pad) + var(--gap-sm)/2)',36:'calc(var(--gap) + var(--gap-sm))',40:'var(--gap-lg)',44:'calc(var(--gap-lg) + var(--gap-sm)/3)',45:'calc(var(--gap-lg) + var(--gap-sm)/2 - var(--stroke))',50:'calc(var(--gap-lg) + var(--gap-sm) - var(--stroke)*2)',54:'calc(var(--gap-lg) + var(--gap-sm) + var(--stroke)*2)',55:'calc(var(--gap-lg) + var(--gap-sm) + var(--gap-sm)/4)',100:'calc(var(--gap-lg)*2 + var(--gap) - var(--gap-sm)/3)',244:'calc(var(--gap-lg)*6 + var(--gap-sm)/3)'}
for p in [C/'foundation/foundation.css',*C.glob('elements/*/element.css')]:
 t=p.read_text()
 def fix(m):
  k,va=m.groups()
  if 'var('in va or (p.parent.name=='chart-stack'and va.strip()=='1px'):return m.group()
  va=re.sub(r'(?<![\w.-])(\d+)px',lambda m:v[int(m[1])]if int(m[1])in v else m[0],va)
  return k+':'+va
 t=re.sub(r'((?:padding|margin)(?:-[a-z]+)?|(?:row-|column-)?gap)\s*:\s*([^;{}]+)',fix,t)
 # Values containing shared tokens plus one measured offset also use the shared spacing basis.
 t=t.replace('padding:30px var(--pad)','padding:calc(var(--gap) + var(--gap-sm)/2) var(--pad)')
 p.write_text(t)
