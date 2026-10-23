from pathlib import Path
from bs4 import BeautifulSoup
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside';V=R/'review'
# The reopened review applies measured geometry to the independent replica too.
# Freeze all drawing rules into its own stylesheet, so replica has no collection dependency.
paths=[C/'kit/css/tokens.css',C/'foundation/foundation.css']+sorted(C.glob('elements/*/element.css'))
s='/* Independent source replica: frozen measured geometry, reopened review. */\nhtml,body{margin:0;width:1280px;height:720px;overflow:hidden}\n'+'\n'.join(p.read_text() for p in paths)+'\n'+(V/'assets/environment.css').read_text().replace("url('font.woff2')","url('../assets/font.woff2')")
(V/'replica/replica.css').write_text(s)
for p in sorted((V/'reassembled').glob('*.html')):
 b=BeautifulSoup(p.read_text(),'html.parser')
 for q in b.select('link[rel="stylesheet"]'):q.decompose()
 b.head.append(BeautifulSoup('<link href="replica.css" rel="stylesheet">','html.parser'));b.title.string='Dockside source replica '+p.stem
 (V/'replica'/p.name).write_text(str(b))
