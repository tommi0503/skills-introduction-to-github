from pathlib import Path
import subprocess
C=Path('/workspace/work/deliverables/undertow');R=Path('/workspace/work/deliverables/undertow-review');REF=Path('/workspace/work/reference')
for mode in ['light','dark']:
 args=['python',str(REF/'tools/preview.py'),str(C),str(REF/'contract/type-steps.json'),'--out',str(R/'library'/f'{mode}.html')]
 if mode=='dark':args.append('--dark')
 subprocess.run(args,check=True)
 p=R/'library'/f'{mode}.html';s=p.read_text().replace('file:///workspace/work/reference/fonts/fonts.css','../fonts/fonts.css').replace('}.frame{','}body>article>.frame{').replace('.frame>.slide{','body>article>.frame>.slide{').replace('small{color:#777','article>h2>small{color:#777');p.write_text(s)
