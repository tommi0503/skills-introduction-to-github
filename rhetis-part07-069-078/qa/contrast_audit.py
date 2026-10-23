"""Final source snapshot contrast check, same solid-background method as integration renderer."""
import json,sys,importlib.util,hashlib
from playwright.sync_api import sync_playwright
from audit_css import BASE,REFERENCE,COLLECTIONS
s=importlib.util.spec_from_file_location('pv',REFERENCE/'tools/preview.py');pv=importlib.util.module_from_spec(s);s.loader.exec_module(pv)
if __name__=='__main__':
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page();q.goto('http://127.0.0.1:8765/qa/probe.html')
  for k in (sys.argv[1:] or COLLECTIONS):
   modes={}
   for dark in [False,True]:
    m=pv.sheet(BASE/(k+'-project')/k,json.loads((REFERENCE/'contract/type-steps.json').read_text()),json.loads((REFERENCE/'contract/palette.json').read_text()),dark=dark,fonts_href=f'/{k}-project/assets/fonts/fonts.css');q.set_content(m,wait_until='networkidle');q.evaluate('document.fonts.ready');contrast=(BASE/'qa/contrast_engine.js').read_text();r=q.evaluate(contrast);r['sourceSha256']=hashlib.sha256(m.encode()).hexdigest();modes['dark' if dark else 'light']=r
   (BASE/'qa'/(k+'-contrast-audit.json')).write_text(json.dumps(modes,ensure_ascii=False,indent=2)+'\n');print(k,{mode:len(v['candidates']) for mode,v in modes.items()},flush=True)
  b.close()
