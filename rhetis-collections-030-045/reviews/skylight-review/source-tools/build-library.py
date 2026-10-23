from pathlib import Path
import subprocess,re
C=Path('/workspace/work/deliverables/skylight');R=Path('/workspace/work/deliverables/skylight-review/library')
for mode in ['light','dark']:
 args=['python','/workspace/work/reference/tools/preview.py',str(C),'/workspace/work/reference/contract/type-steps.json','--out',str(R/f'{mode}.html')]
 if mode=='dark':args+=['--dark']
 subprocess.run(args,check=True)
 p=R/f'{mode}.html';s=p.read_text();s=re.sub(r'href="file:[^"]*fonts.css"','href="../fonts/fonts.css"',s);s=s.replace('small{color:#777;margin-left:8px}','article>h2>small{color:#777;margin-left:8px}').replace('.frame{width:640px','body>article>.frame{width:640px').replace('.frame>.slide{width:1280px','body>article>.frame>.slide{width:1280px');p.write_text(s)
