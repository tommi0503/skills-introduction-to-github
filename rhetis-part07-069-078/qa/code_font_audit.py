"""Verify that code text uses an actually loaded monospaced allowed font."""
import json,sys,importlib.util
from playwright.sync_api import sync_playwright
from audit_css import BASE,REFERENCE,COLLECTIONS
s=importlib.util.spec_from_file_location('pv',REFERENCE/'tools/preview.py');pv=importlib.util.module_from_spec(s);s.loader.exec_module(pv)
if __name__=='__main__':
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page();q.goto('http://127.0.0.1:8765/qa/probe.html')
  for k in (sys.argv[1:] or COLLECTIONS):
   m=pv.sheet(BASE/(k+'-project')/k,json.loads((REFERENCE/'contract/type-steps.json').read_text()),json.loads((REFERENCE/'contract/palette.json').read_text()),fonts_href='/assets/fonts/fonts.css');q.set_content(m,wait_until='networkidle');q.evaluate('document.fonts.ready')
   out=q.evaluate('''()=>{const canvas=document.createElement('canvas'),ctx=canvas.getContext('2d');return [...document.querySelectorAll('.code .lines p')].map(e=>{let s=getComputedStyle(e);ctx.font=`${s.fontWeight} ${s.fontSize} ${s.fontFamily}`;let narrow=ctx.measureText('iiii').width,wide=ctx.measureText('WWWW').width;return {family:s.fontFamily,fontStatus:document.fonts.check(ctx.font),monospaced:Math.abs(narrow-wide)<.2,widths:[narrow,wide]}}).filter((x,i,a)=>a.findIndex(y=>y.family===x.family&&y.monospaced===x.monospaced)===i)}''')
   (BASE/'qa'/(k+'-code-font-audit.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(k,out)
  b.close()
