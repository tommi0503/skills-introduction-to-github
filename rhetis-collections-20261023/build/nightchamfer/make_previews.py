from pathlib import Path
import subprocess
R=Path('/workspace/output/nightchamfer-review')
for mode in ['light','dark']:
 args=['python','/workspace/work/reference/tools/preview.py','/workspace/output/nightchamfer','/workspace/work/reference/contract/type-steps.json','--out',str(R/'library'/f'{mode}.html')]
 if mode=='dark':args.append('--dark')
 subprocess.run(args,check=True)
 p=R/'library'/f'{mode}.html';s=p.read_text().replace('file:///workspace/work/reference/fonts/fonts.css','../fonts/fonts.css');i=s.index('</style>');j=s.index('</style>',i+8);x=s[i:j].replace('.frame{','article>.frame{').replace('.frame>.slide{','article>.frame>.slide{').replace('h2{','article>h2{').replace('small{','article>h2>small{');p.write_text(s[:i]+x+s[j:])
