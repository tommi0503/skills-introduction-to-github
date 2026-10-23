from pathlib import Path
from math import sin,cos,pi
C=Path('/workspace/output/cyanloop')
p=C/'elements/cycle/element.css';s=p.read_text();r='.cycle[data-el="cyanloop-cycle"]';s+='\n'+r+'{display:block;padding:0;}'+r+'::before{content:"";position:absolute;left:50%;top:50%;width:min(64cqw,64cqh);height:min(64cqw,64cqh);transform:translate(-50%,-50%);border:2px solid var(--n-3);border-radius:50%;}'+r+' .core{position:absolute;left:50%;top:50%;width:min(28cqw,28cqh);height:min(28cqw,28cqh);transform:translate(-50%,-50%);border-radius:50%;}'+r+' .node{position:absolute;width:min(28cqw,28cqh);height:min(28cqw,28cqh);transform:translate(-50%,-50%);padding:var(--gap-sm);border-radius:50%;}'+r+' .node::before{display:none;}'+r+' .node::after{content:"";position:absolute;left:50%;top:calc(100% + var(--gap-sm));width:12px;height:12px;background:var(--a1);clip-path:polygon(0 0,100% 50%,0 100%);}\n'
for n in range(3,7):
 for i in range(n):
  a=-pi/2+i*2*pi/n
  s+=r+f':has(>.node:nth-child({n+1}):last-child) .node:nth-child({i+2}){{left:calc(50% + {cos(a):.6f} * min(32cqw,32cqh));top:calc(50% + {sin(a):.6f} * min(32cqw,32cqh));}}\n'
  s+=r+f':has(>.node:nth-child({n+1}):last-child) .node:nth-child({i+2})::after{{transform:rotate({a*180/pi+90:.4f}deg);}}\n'
s+='@container(max-height:350px){'+r+' .node .note{display:none;}'+r+' .node .name{font-size:var(--type-14);}'+r+' .core{font-size:var(--type-20);padding:calc(var(--gap-sm) / 2);}}\n';p.write_text(s)
p=C/'elements/radar/element.css';s=p.read_text();r='.radar[data-el="cyanloop-radar"]';s+='\n'+r+' .series{clip-path:none;background:none;border:0;isolation:isolate;}'+r+' .series::before{content:"";position:absolute;inset:0;background:var(--a1-2-soft);z-index:-1;}'+r+' .series.tone-2::before{background:var(--a2-2-soft);}'+r+' .series.tone-3::before{background:var(--a3-2-soft);}'+r+' .series .name{top:calc(0px - var(--gap-lg));left:0;white-space:nowrap;color:var(--ink);font-size:var(--type-14);}'+r+' .series+.series .name{left:40%;}'+r+' .series+.series+.series .name{left:75%;}\n'
for n in range(3,9):
 sel=r+f'[style*="--n:{n}"]'
 points=[]
 for i in range(n):
  a=i*2*pi/n
  points.append(f'calc(50% + {sin(a):.6f} * var(--v{i+1}) / var(--max) * 50%) calc(50% - {cos(a):.6f} * var(--v{i+1}) / var(--max) * 50%)')
  angle=i*360/n-90;s+=sel+f' .axis:nth-child({i+1}){{transform:rotate({angle:.4f}deg);}}'+sel+f' .axis:nth-child({i+1}) .name{{transform:rotate({-angle:.4f}deg);}}\n'
 s+=sel+' .series::before{clip-path:polygon('+','.join(points)+');}\n'
p.write_text(s)
p=C/'elements/network/element.css';s=p.read_text();r='.network[data-el="cyanloop-network"]';s+='\n'+r+'{padding:0;}'+r+' .link{width:hypot(calc((var(--x2) - var(--x1)) * .8cqw),calc((var(--y2) - var(--y1)) * .8cqh));transform:rotate(atan2(calc((var(--y2) - var(--y1)) * .8cqh),calc((var(--x2) - var(--x1)) * .8cqw)));}\n';p.write_text(s)
