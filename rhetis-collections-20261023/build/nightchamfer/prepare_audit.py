from pathlib import Path
import shutil
W=Path('/workspace/work/nightchamfer');P=W/'public';P.mkdir(exist_ok=True);shutil.copytree('/workspace/output/nightchamfer-review/fonts',P/'fonts',dirs_exist_ok=True)
s=Path('/workspace/work/integration/browser_audit.py').read_text().replace("WORK=Path('/workspace/work/integration')","WORK=Path('/workspace/work/nightchamfer')").replace('http://127.0.0.1:8760/','http://127.0.0.1:8765/')
s=s.replace("raw=fixture.read_text();minimum=", "\n   if os.environ.get('NC_SELECT') and fixture.stem not in os.environ['NC_SELECT'].split(','):continue\n   raw=fixture.read_text();minimum=")
s=s.replace('asyncio.run(main())', '''import threading,http.server,functools
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',8765),functools.partial(Quiet,directory='/workspace/work/nightchamfer/public'));threading.Thread(target=server.serve_forever,daemon=True).start()
asyncio.run(main())''')
(W/'browser_audit.py').write_text(s)
