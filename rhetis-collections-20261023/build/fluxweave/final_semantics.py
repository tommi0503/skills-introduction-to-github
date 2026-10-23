from pathlib import Path
O=Path('/workspace/output/fluxweave')
def ap(f,s):p=O/'elements'/f/'element.css';p.write_text(p.read_text()+s.replace('ROOT',f'[data-el="fluxweave-{f}"]'))
ap('balance','''
ROOT{isolation:isolate;}
ROOT::before{content:"";position:absolute;left:10%;right:10%;top:75%;height:3px;background:var(--ink);transform:rotate(calc(var(--tilt)*.05deg));z-index:-1;}
ROOT>.pan{position:relative;transform:translateY(calc(var(--tilt)*-.3px));}
ROOT>.pan:nth-child(2){transform:translateY(calc(var(--tilt)*.3px));}
ROOT>.pan::after{content:"";position:absolute;width:2px;height:40px;left:50%;top:100%;background:var(--n-4);}
ROOT>.fulcrum::before{content:"";position:absolute;width:64px;height:100px;left:calc(50% - 32px);bottom:var(--gap-lg);background:var(--n-4);clip-path:polygon(50% 0,100% 100%,0 100%);}
''')
ap('decision-tree','''
ROOT .q{position:relative;}
ROOT .q::after{content:"";position:absolute;left:50%;top:100%;height:var(--gap-lg);border-left:var(--stroke) solid var(--n-4);}
ROOT .opt{position:relative;}
ROOT .opt::before{content:"";position:absolute;left:50%;bottom:100%;height:var(--gap);border-left:var(--stroke) solid var(--n-4);}
''')
ap('bullet','''
ROOT::before,ROOT>.bullet::before{background:linear-gradient(to right,var(--n-2) 0 calc(var(--low,45)*1%),var(--n-3) calc(var(--low,45)*1%) calc(var(--high,75)*1%),var(--n-4) calc(var(--high,75)*1%) 100%);}
ROOT .note::after{content:none;}
ROOT .fig::after{content:"";position:absolute;left:calc(min(var(--target),100)*1%);bottom:-4px;width:2px;height:22px;background:var(--ink);z-index:3;}
''')
ap('radar','''
ROOT>.series{clip-path:none!important;background:none;border:0;}
ROOT>.series::before{content:"";position:absolute;inset:0;background:color-mix(in srgb,var(--a1) 30%,var(--page));}
ROOT>.series.tone-2::before{background:color-mix(in srgb,var(--a2) 30%,var(--page));}
ROOT>.series.tone-3::before{background:color-mix(in srgb,var(--a3) 30%,var(--page));}
ROOT>.series>.name{position:absolute;top:calc(-1*var(--gap-lg));left:0;font-size:var(--type-14);white-space:nowrap;color:var(--ink);}
ROOT>.series:nth-child(2 of .series)>.name{left:50%;}
ROOT>.series:nth-child(3 of .series)>.name{left:100%;}
ROOT::before{background:repeating-conic-gradient(var(--n-3) 0deg .3deg,color-mix(in srgb,var(--page) 0%,var(--page) 1%) .3deg calc(360deg/var(--n)));}
''')
for n in range(3,9):
 pts=[]
 for i in range(n):
  a=-90+i*360/n;pts.append(f'calc(50% + cos({a}deg)*var(--v{i+1})/var(--max)*50%) calc(50% + sin({a}deg)*var(--v{i+1})/var(--max)*50%)')
 ap('radar',f'ROOT[style*="--n:{n}"]>.series::before,ROOT[style*="--n: {n}"]>.series::before{{clip-path:polygon('+','.join(pts)+');}')
print('semantic detail checks complete')
