"""Read-only browser replay upgrades actual-font evidence without rewriting rendered PNGs."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright
from font_qa import actual_fonts
import json,threading,hashlib,sys
R=Path('/workspace/work/rebuild')
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass

def run(names,force=False):
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R)));threading.Thread(target=server.serve_forever,daemon=True).start();totals=[]
 with sync_playwright()as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-breakpad']);pg=b.new_page(viewport={'width':1280,'height':720});cdp=pg.context.new_cdp_session(pg);cdp.send('DOM.enable');cdp.send('CSS.enable')
  for n in names:
   num=0;fallback=[]
   for f in sorted((R/n/'review/validation').glob('*.json')):
    if not (R/n/n/'elements'/f.stem/'element.css').exists():continue
    original=f.read_bytes();q=json.loads(original)
    if not isinstance(q,dict)or not isinstance(q.get('cases'),list) or'source_hashes'not in q:continue
    if not force and q.get('font_checks')and all(x.get('font_probe_version')==2 for x in q['font_checks']):
     for a in q['font_checks']:
      if a['load_errors']or(a.get('font_nodes')and not a['platform_fonts'])or any(not x['isCustomFont']for x in a['platform_fonts']):fallback.append({'leaf':f.stem,**a})
     continue
    checks=[]
    for fixture,mode in sorted({(x['fixture'],x['mode'])for x in q['cases']}):
     html=R/n/'review/html'/f.stem/(fixture+'-'+mode+'.html')
     if not html.exists():continue
     pg.goto(f'http://127.0.0.1:{server.server_port}/{n}/review/html/{f.stem}/{html.name}');pg.evaluate('document.fonts.ready');a=actual_fonts(pg,cdp);a.update(fixture=fixture,mode=mode,html_sha256=hashlib.sha256(html.read_bytes()).hexdigest());checks.append(a)
     if a['load_errors']or (a['font_nodes']and not a['platform_fonts'])or any(not x['isCustomFont']for x in a['platform_fonts']):fallback.append({'leaf':f.stem,**a})
    if f.read_bytes()!=original:print(n,f.stem,'changed during font replay; skipped',flush=True);continue
    q['font_checks']=checks;f.write_text(json.dumps(q,ensure_ascii=False,indent=2));num+=1
   out={'collection':n,'upgraded_leaves':num,'noncustom_or_missing_or_load_errors':fallback};(R/n/'review/validation/actual-font-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));totals.append(out);print(n,'font evidence upgraded',num,'fallback records',len(fallback),flush=True)
  b.close()
 server.shutdown();return totals
if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument('collections',nargs='*');parser.add_argument('--force',action='store_true');args=parser.parse_args();run(args.collections or list(json.loads((R/'profiles.json').read_text())),args.force)
