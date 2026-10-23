from pathlib import Path
C=Path('/workspace/output/nightchamfer')
def append(n,s):
 p=C/'elements'/n/'element.css';p.write_text(p.read_text()+'\n'+s.replace('$',f'[data-el="nightchamfer-{n}"]')+'\n')
append('heatmap','''$ .cell>b{background:var(--page);color:var(--ink);border-radius:calc(var(--radius-sm)/3);padding:calc(var(--gap-sm)/4);font-size:var(--type-12)}''')
append('code','''$ .c{color:var(--n-8)}''')
append('timeline','''@container(min-height:380px){$:not(.col):not(.alt)>.stop::before{display:none}$:not(.col):not(.alt)>.stop>.kick{display:inline-flex;align-items:center;justify-content:center;align-self:flex-start;min-width:60px;min-height:44px;background:var(--a1);color:var(--a1-on);border:6px solid var(--a1-2-muted);border-radius:999px;padding:calc(var(--gap-sm)/4) var(--gap-sm)}}''')
p=C/'elements/waffle/element.css';p.write_text(p.read_text().replace('gap:2px','gap:calc(var(--gap-sm)/6)'))
R=Path('/workspace/output/nightchamfer-review')
p=R/'replica/replica.css';p.write_text(p.read_text()+'''\n.cover{background:radial-gradient(ellipse 42% 60% at 0% 100%,#9dbedf 0,#13315b 36%,#0000 82%),radial-gradient(ellipse 30% 40% at 100% 0,#194485,#0000),#000}\n''')
for p in (R/'replica').glob('*.html'):
 s=p.read_text().replace('♧','M')
 s=s.replace('⌂','<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 10 9-7 9 7v11H3Z"/><path d="M9 21v-8h6v8"/></svg>')
 s=s.replace('☎','<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 3h4l2 5-3 2a15 15 0 0 0 6 6l2-3 5 2v4c-1 6-20-4-18-14Z"/></svg>')
 s=s.replace('✉','<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16"/><path d="m2 5 10 8L22 5"/></svg>')
 p.write_text(s)
