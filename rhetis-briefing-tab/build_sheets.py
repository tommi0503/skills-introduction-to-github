from pathlib import Path
import subprocess,sys,json,re,html
from importlib.util import spec_from_file_location,module_from_spec
ROOT=Path(__file__).resolve().parent
R=ROOT/'briefing-tab-review';C=ROOT/'briefing-tab';REF=ROOT/'reference'
for mode in ['light','dark']:
 cmd=[sys.executable,str(REF/'tools/preview.py'),str(C),str(REF/'contract/type-steps.json'),'--out',str(R/f'library/{mode}.html'),'--fonts',str(R/'fonts/fonts.css')]
 if mode=='dark':cmd+=['--dark']
 subprocess.run(cmd,check=True)
 p=R/f'library/{mode}.html';s=p.read_text();s=re.sub('href="file:[^"]+fonts.css"','href="../fonts/fonts.css"',s);s=s.replace('.frame{','article>.frame{').replace('.frame>.slide{','article>.frame>.slide{');p.write_text(s)
 # One full-resolution sheet per element folder, with every fixture at its complete size.
 style=s.split('<style>',1)[1].split('</style>',1)[0]
 cssframe='body{margin:0;padding:24px;background:#dedee2;font:16px sans-serif}article{margin:0 0 24px}article>h2{margin:0 0 8px;font:16px sans-serif}article>.frame{width:1280px;height:720px}article>.frame>.slide{width:1280px;height:720px;position:relative}[data-icon]:empty::after{content:"";display:block;width:100%;height:100%;box-sizing:border-box;border:1.5px dashed currentColor;border-radius:50%}'
 articles=re.findall(r'<article>.*?</article>',s,re.S)
 for folder in ['foundation']+[p.name for p in sorted((C/'elements').iterdir()) if p.is_dir()]:
  out=R/f'library/{folder}';out.mkdir(exist_ok=True)
  subset=[a for a in articles if f'<h2>{folder} / ' in a]
  doc='<!doctype html><html lang="ko"><meta charset="utf-8"><title>'+html.escape(folder)+' '+mode+'</title><link rel="stylesheet" href="../../fonts/fonts.css"><style>'+style+'</style><style>'+cssframe+'</style><body>'+''.join(subset)+'</body></html>'
  (out/f'{mode}.html').write_text(doc)
 print(mode,len(articles),'fixtures')
