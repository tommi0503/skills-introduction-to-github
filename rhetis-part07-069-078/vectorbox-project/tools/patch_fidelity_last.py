from pathlib import Path
import math
p=Path(__file__).with_name('refine_fidelity.py');s=p.read_text()
s=s.replace('R .name{font-weight:var(--label-weight)}@container(max-width:600px)', 'R .name{font-weight:var(--label-weight);position:relative;top:calc(7*var(--stroke))}@container(max-width:600px)')
s=s.replace('R.line .mark:has(>.icon:nth-child(3):last-child)>.icon{position:absolute;width:80px;height:100px;top:55px;left:8px}', 'R.line .mark:has(>.icon:nth-child(3):last-child)>.icon{position:absolute;width:60px;height:90px;top:42px;left:8px}')
s=s.replace('>.icon:nth-child(2){left:88px}', '>.icon:nth-child(2){left:108px}')
s=s.replace('>.icon:last-child{left:38px;top:26px;width:100px;height:130px;background:var(--page)}', '>.icon:last-child{left:48px;top:52px;width:80px;height:100px;background:none}')
s=s.replace('@container(max-width:700px){R:not(.h)', '@container(max-width:500px){R:not(.h)')
s=s.replace('padding:calc(var(--gap) + 5*var(--stroke)) 0 0;margin-left:calc(-1*var(--gap-sm) - 3*var(--stroke))', 'padding:var(--gap-lg) 0 0;margin-left:calc(-1*var(--gap-sm) - 9*var(--stroke))')
s=s.replace('R.big h2>span{display:block;margin-top:var(--gap-sm)}R.big>.note{margin-top:var(--gap-lg);', 'R.big h2>span{display:block;margin-top:calc(var(--gap-sm) - 3*var(--stroke))}R.big>.note{margin-top:calc(var(--gap) + 2*var(--stroke));margin-left:calc(6*var(--stroke));')
s=s.replace('R.quiet{padding:0 0 calc(6*var(--stroke));', 'R.quiet{padding:0 0 calc(var(--gap-sm) + 6*var(--stroke));')
s=s.replace('.slide .head>.title:lang(en){font-family:', '.slide .head>.title:lang(en){margin-top:calc(var(--gap-lg) + var(--gap-sm) + 11*var(--stroke));font-family:')
s=s.replace('.slide .head>.lead{margin-top:var(--gap)}', '.slide .head>.lead{margin-top:calc(var(--gap) - 2*var(--stroke))}')
s=s.replace('overflow:visible}R:has(>.spoke:nth-child(5):last-child)>.core>.icon', 'overflow:hidden}R:has(>.spoke:nth-child(5):last-child)>.core>.icon')
# Smooth 12-petal burst: fixed design geometry, not fixture-value interpolation.
pts=[]
for i in range(48):
 a=-math.pi/2+i*2*math.pi/48;r=[79.5,79.5,70.5,70.5][i%4];pts.append((79.5+r*math.cos(a),79.5+r*math.sin(a)))
parts=[f'M{pts[0][0]:.2f} {pts[0][1]:.2f}']
for i in range(48):
 a,b,c,d=[pts[j%48] for j in [i-1,i,i+1,i+2]]
 u=(b[0]+(c[0]-a[0])/6,b[1]+(c[1]-a[1])/6);v=(c[0]-(d[0]-b[0])/6,c[1]-(d[1]-b[1])/6)
 parts.append(f'C{u[0]:.2f} {u[1]:.2f} {v[0]:.2f} {v[1]:.2f} {c[0]:.2f} {c[1]:.2f}')
path=' '.join(parts)+'Z'
s=s.replace('R.stat.on.tone-2 .fig{{background:var(--a2);color:var(--a2-on)}}', 'R.stat.on.tone-2 .fig{{background:var(--a2);color:var(--a2-on);clip-path:path("'+path+'");}}')
p.write_text(s)
