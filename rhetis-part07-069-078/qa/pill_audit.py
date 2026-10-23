"""Verify capsule intrinsic dimensions from real source, rather than only text overflow."""
import json,sys,importlib.util,re
from playwright.sync_api import sync_playwright
from audit_css import BASE,REFERENCE,COLLECTIONS,parse_rules
s=importlib.util.spec_from_file_location('pv',REFERENCE/'tools/preview.py');pv=importlib.util.module_from_spec(s);s.loader.exec_module(pv)
if __name__=='__main__':
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page(viewport={'width':1360,'height':900});q.goto('http://127.0.0.1:8765/qa/probe.html')
  for k in (sys.argv[1:] or COLLECTIONS):
   root=BASE/(k+'-project')/k;m=pv.sheet(root,json.loads((REFERENCE/'contract/type-steps.json').read_text()),json.loads((REFERENCE/'contract/palette.json').read_text()),fonts_href='/assets/fonts/fonts.css');q.set_content(m,wait_until='networkidle');q.evaluate('document.fonts.ready')
   result=[]
   for a in q.locator('article').all():
    title=a.locator(':scope > h2').inner_text()
    if not title.startswith('pill /'):continue
    mins=[tuple(map(int,x)) for x in re.findall(r'(\d+)x(\d+)',title.split('min',1)[-1])];sizes=list(dict.fromkeys(mins+[(12,6)]))
    for c,r in sizes:
     a.evaluate('''(a,s)=>{let f=a.querySelector('.frame');f.style.width='1280px';f.style.height='720px';f.querySelector('.slide').style.transform='none';for(const e of a.querySelector('.body').children){e.style.gridColumn='1 / span '+s[0];e.style.gridRow='1 / span '+s[1]}}''',[c,r])
     bad=a.evaluate('''a=>{const out=[];for(const e of a.querySelectorAll('.pill')){let r=e.getBoundingClientRect(),n=e.querySelector('.name'),t=n?.getBoundingClientRect();if(r.width<10||r.height<10||(t&&(t.left<r.left-2||t.right>r.right+2||t.top<r.top-2||t.bottom>r.bottom+2)))out.push({text:n?.textContent,box:[r.width,r.height],nameBox:t?[t.left-r.left,t.top-r.top,t.width,t.height]:null});}return out}''');result.append({'fixture':title,'size':[c,r],'problems':bad})
   covers=[a for a,b,l in parse_rules((root/'foundation/foundation.css').read_text()) if '.slide .cover' in a]
   report={'collection':k,'pillChecks':result,'problemCases':sum(bool(x['problems']) for x in result),'invalidCoverSelectors':covers};(BASE/'qa'/(k+'-pill-cover-audit.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(k,report['problemCases'],'pillcases',len(covers),'badcover')
  b.close()
