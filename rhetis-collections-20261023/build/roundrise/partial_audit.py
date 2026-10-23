from pathlib import Path
p=Path('/workspace/work/integration/browser_audit.py');s=p.read_text();s=s.replace("for fixture in sorted(root.glob('elements/*/fixtures/*.html')):","for fixture in sorted(root.glob('elements/*/fixtures/*.html')):\n   if fixture.parts[-3] not in ['agenda','hub','steps']:continue")
s=s.replace("(name+'-browser-audit.json')","(name+'-partial-audit.json')")
exec(compile(s,str(p),'exec'))
