"""Supply neutral HTML frame, calibrated defaults/fonts and the Lucide runtime Rhetis normally supplies.
No collection geometry CSS is added or changed.
"""
from pathlib import Path
import json,re,shutil,sys
ROOT=Path(__file__).resolve().parent
FONT_KEEP={'Pretendard Variable','Noto Sans KR','Montserrat','Nanum Gothic Coding','Pretendard','Nanum Pen'}
NPM=Path('/opt/codex/runtimes/codex-primary-runtime/dependencies/node/node_modules/lucide')
for kid in sys.argv[1:]:
 P=ROOT/(kid+'-project');assets=P/'assets';assets.mkdir(exist_ok=True)
 shutil.copy2(NPM/'dist/umd/lucide.min.js',assets/'lucide.min.js')
 if (NPM/'LICENSE').exists():shutil.copy2(NPM/'LICENSE',assets/'lucide-LICENSE.md')
 (assets/'render-icons.js').write_text("(()=>{const draw=()=>lucide.createIcons({nameAttr:'data-icon',attrs:{width:'100%',height:'100%','stroke-width':1.5}});if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',draw);else draw();})();\n")
 defaults={}
 for f in sorted((P/kid).glob('**/*.json')):
  defaults.update(json.loads(f.read_text()).get('tokenDefaults',{}))
 (assets/'source-defaults.css').write_text('.slide{'+''.join(k+':'+str(v)+';' for k,v in sorted(defaults.items()))+'}\n')
 fonts=assets/'fonts';reference=Path('/workspace/work/reference/fonts') if Path('/workspace/work/reference/fonts').exists() else ROOT/'reference/fonts';css=(reference/'fonts.css').read_text();blocks=re.findall(r'@font-face\s*\{[^}]+\}',css)
 source_text='\n'.join(f.read_text() for d in [P/kid,P/'replica'] for f in d.rglob('*') if f.is_file() and f.suffix in ['.css','.json','.html'])
 selected=[]
 for block in blocks:
  family=re.search(r"font-family:\s*'([^']+)'",block).group(1)
  files=re.findall(r"url\('([^']+)'\)",block)
  if family in FONT_KEEP or any(q+family+q in source_text for q in [chr(39),chr(34)]) or any(Path(u).name in source_text for u in files):selected.append(block)
 (fonts/'fonts.css').write_text('\n'.join(selected)+'\n')
 keep={fonts/u for x in selected for u in re.findall(r"url\('([^']+)'\)",x)}
 for dest in keep:
  dest.parent.mkdir(parents=True,exist_ok=True)
  if not dest.exists():shutil.copy2(reference/dest.relative_to(fonts),dest)
 for f in (fonts/'artifacts').rglob('*'):
  if f.is_file() and f not in keep:f.unlink()
 for f in (P/'reassembled').glob('slide*.html'):
  text=f.read_text().replace('../../assets/fonts/fonts.css','../assets/fonts/fonts.css')
  if 'source-defaults.css' not in text:
   link='<link rel="stylesheet" href="../assets/source-defaults.css">'
   if '</head>' in text:text=text.replace('</head>',link+'</head>',1)
   else:text=re.sub(r'<body\b',link+'</head><body',text,count=1)
  if 'render-icons.js' not in text:text=text.replace('</body>','<script src="../assets/lucide.min.js"></script><script src="../assets/render-icons.js"></script></body>')
  text=re.sub(r'<body>', '<body style="margin:0">',text)
  f.write_text(text)
 print(kid,'runtime provider installed',len(defaults),'defaults')
