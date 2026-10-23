from pathlib import Path
O=Path('/workspace/output/fluxweave')
def ap(f,s):p=O/'elements'/f/'element.css';p.write_text(p.read_text()+s.replace('ROOT',f'[data-el="fluxweave-{f}"]'))
ap('timeline','''
ROOT.alt{align-items:stretch;isolation:isolate;}
ROOT.alt::before{content:"";position:absolute;left:0;right:0;top:50%;height:2px;background:var(--a1-3-soft);z-index:-1;}
ROOT.alt>.stop{height:48%;flex:1;justify-content:center;border:0;padding:var(--gap-sm);}
ROOT.alt>.stop:nth-child(odd){align-self:flex-start;border-bottom:2px solid var(--a1-3-soft);}
ROOT.alt>.stop:nth-child(even){align-self:flex-end;border-top:2px solid var(--a1-3-soft);}
ROOT.alt>.stop::after{content:"";position:absolute;width:10px;height:10px;border-radius:50%;background:var(--a1);left:50%;bottom:-6px;}
ROOT.alt>.stop:nth-child(even)::after{bottom:auto;top:-6px;}
ROOT.alt>.stop>.name{min-height:0;font-size:var(--type-18);}
ROOT.alt>.stop>.note{font-size:var(--type-14);}
''')
for f in ['bullet','gauge']:
 p=O/'elements'/f/'element.css';p.write_text(p.read_text().replace('width:calc(var(--v)*1%)','width:calc(min(var(--v),100)*1%)'))
ap('chart-stack','''
ROOT>.sbar{justify-content:flex-start;}
ROOT .seg:nth-child(2 of .seg){background:var(--a2-3-soft);}
ROOT .seg:nth-child(3 of .seg){background:var(--a3-3-soft);}
ROOT .seg:nth-child(4 of .seg){background:var(--a4-3-soft);}
ROOT .seg:nth-child(5 of .seg){background:var(--n-3);}
ROOT>.sbar.on>.seg:first-child{background:var(--a1);}
''')
ap('concentric','''
ROOT>.ring{left:50%;transform:translateX(-50%);max-height:none;}
ROOT>.ring:nth-child(1){width:min(92%,100cqh);height:min(92cqw,100cqh);max-height:none;}
ROOT>.ring:nth-child(2){width:min(65%,72cqh);height:min(65cqw,72cqh);max-height:none;}
ROOT>.ring:nth-child(3){width:min(40%,44cqh);height:min(40cqw,44cqh);max-height:none;}
ROOT>.ring:nth-child(4){width:min(23%,25cqh);height:min(23cqw,25cqh);max-height:none;}
''')
ap('venn','''
ROOT:has(>.set:nth-child(3))>.set:nth-child(1){left:50%;transform:translateX(-50%);}
ROOT:has(>.set:nth-child(3))>.set:nth-child(2){left:calc(50% - min(65%,65cqh));}
ROOT:has(>.set:nth-child(3))>.set:nth-child(3){left:50%;right:auto;}
''')
# Static layout anchors make the spoke connections follow their semantic nodes.
for f,m in [('hub','spoke'),('mindmap','branch')]:
 r=f'[data-el="fluxweave-{f}"]';p=O/'elements'/f/'element.css';s=f'\n{r}{{isolation:isolate;}}{r}>.core{{anchor-name:--fluxweave-{f}-core;position:relative;z-index:1;}}{r}>.{m}{{position:static;}}'
 clear='color-mix(in srgb,var(--page) 0%,var(--page) 1%)'
 for i in range(2,8):
  a=f'--fluxweave-{f}-{i}';co=f'--fluxweave-{f}-core';s+=f'{r}>.{m}:nth-child({i}){{anchor-name:{a};}}'
  leftside=i in [2,6,7];upper=i in [2,3];middle=i in [4,7]
  le=a if leftside else co;ri=co if leftside else a
  if middle:
   decl=f'left:anchor({le} center);right:anchor({ri} center);top:calc(anchor({co} center) - 1px);height:2px;background:var(--a1-3-soft);'
  else:
   top=a if upper else co;bot=co if upper else a;direction='top right' if (leftside and upper) or (not leftside and not upper) else 'bottom right'
   decl=f'left:anchor({le} center);right:anchor({ri} center);top:anchor({top} center);bottom:anchor({bot} center);width:auto;height:auto;background:linear-gradient(to {direction},{clear} calc(50% - 1px),var(--a1-3-soft) 50%,{clear} calc(50% + 1px));'
  s+=f'{r}>.{m}:nth-child({i})::before{{content:"";position:absolute;z-index:-1;{decl}}}'
 p.write_text(p.read_text()+s)
ap('cycle','''
ROOT{isolation:isolate;}
ROOT::before{content:"";position:absolute;inset:15%;border:2px solid var(--a1-3-soft);border-radius:50%;z-index:-1;}
ROOT>.node::before{display:none;}
ROOT>.node::after{content:"";position:absolute;right:calc(-1*var(--gap-sm));top:50%;width:10px;height:10px;border-top:2px solid var(--a1);border-right:2px solid var(--a1);transform:rotate(45deg);}
ROOT>.node:nth-child(3)::after,ROOT>.node:nth-child(4)::after{right:50%;top:auto;bottom:calc(-1*var(--gap-sm));transform:rotate(135deg);}
ROOT>.node:nth-child(5)::after,ROOT>.node:nth-child(6)::after{right:auto;left:calc(-1*var(--gap-sm));transform:rotate(225deg);}
ROOT>.node:nth-child(7)::after{right:50%;top:calc(-1*var(--gap-sm));transform:rotate(315deg);}
''')
print('alternate timeline, connectors and diagram semantics finished')
