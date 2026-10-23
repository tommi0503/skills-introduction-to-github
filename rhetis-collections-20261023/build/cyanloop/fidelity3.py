from pathlib import Path
C=Path('/workspace/output/cyanloop');W=Path('/workspace/work/cyanloop')
p=W/'reassembly.py';s=p.read_text().replace("' at-bottom-left' if n==13", "' at-bottom-left' if n in (11,13)");s=s.replace('--a1-7:#f5f5f5;--a1-on:#f5f5f5;', '--a1:#00a9ee;--a2:#0753d6;--a3:#2bd4c8;--a1-7:#f5f5f5;--a1-on:#f5f5f5;--a2-on:#f5f5f5;--n-9:#111;');s=s.replace("('Professional','badge-check')", "('Professional','file-badge')");s=s.replace('--a1-on:#f5f5f5;--a1-7:#001134;', '--n-9:#111;--a1-on:#f5f5f5;--a1-7:#001134;');p.write_text(s)
p=C/'elements/hub/element.css';s=p.read_text();s+='''
.hub[data-el="cyanloop-hub"].on .spoke{padding:var(--gap-sm);}
.hub[data-el="cyanloop-hub"].on .spoke .note{font-size:var(--type-16);}
.hub[data-el="cyanloop-hub"].on .core{padding-top:calc(var(--gap-lg)*2);}
.hub[data-el="cyanloop-hub"].line::before{top:20.2%;}
.hub[data-el="cyanloop-hub"].line::after{top:41.1%;}
.hub[data-el="cyanloop-hub"].line .core{top:51%;}
.hub[data-el="cyanloop-hub"].line .spoke>.name,.hub[data-el="cyanloop-hub"].line .spoke>.note{color:var(--n-9);}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(2)>.mark{top:20.9%;}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(3)>.mark{top:45.8%;}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(4)>.mark{top:65%;}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(5)>.mark{top:27.9%;}
.hub[data-el="cyanloop-hub"].line .spoke:nth-child(6)>.mark{top:63.9%;}
'''
# Text source offsets remain invariant as a fraction of the 598-high root.
for i,yn,yt in [(2,161,195),(3,291,329),(4,416,452),(5,161,195),(6,416,452)]:
 s+=f'.hub[data-el="cyanloop-hub"].line .spoke:nth-child({i})>.name{{top:{yn/598*100:.4f}%;}}\n.hub[data-el="cyanloop-hub"].line .spoke:nth-child({i})>.note{{top:{yt/598*100:.4f}%;}}\n'
p.write_text(s)
p=C/'elements/prose/element.css';p.write_text(p.read_text()+'\n.prose[data-el="cyanloop-prose"]{color:var(--n-9);}.prose[data-el="cyanloop-prose"].lead.quiet{color:var(--n-9);}\n')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'\n.slide .icon svg{stroke-width:calc(var(--stroke) * 1.5);}\n')
# Smaller photo halo: the visible outside ring follows the photo edge on the left.
p=C/'elements/image-frame/element.css';p.write_text(p.read_text()+'''\n.frame[data-el="cyanloop-image-frame"].on::before{width:96cqw;height:96cqh;border-width:18px;}\n''')
