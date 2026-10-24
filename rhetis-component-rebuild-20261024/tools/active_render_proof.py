"""Conservative reuse of a completed render after unrelated element or furniture edits.
Every fixture byte and every matching CSS rule (including container branches) must agree.
"""
import re,json,hashlib
ACTIVE_JS=r'''([a,b])=>{function active(css){let sh=new CSSStyleSheet();sh.replaceSync(css);function walk(rs){let out=[];for(let r of rs){if(r.selectorText){let sel=r.selectorText.replace(/::[\w-]+(?:\([^)]*\))?/g,'');let match=false;try{match=!!document.querySelector(sel)}catch(e){match=true}if(match)out.push(r.cssText)}else if(r.cssRules){let inner=walk(r.cssRules);if(inner.length)out.push(r.cssText.slice(0,r.cssText.indexOf('{'))+'{'+inner.join('\n')+'}')}else out.push(r.cssText)}return out}return walk(sh.cssRules).join('\n')}let x=active(a),y=active(b);return{equal:x===y,oldLength:x.length,newLength:y.length}}'''
def equivalent(browser,c,r,leaf,fixtures,data,current_css,pixel):
 if not data.get('cases')or(pixel and any(x.get('pixelContrast')is None for x in data['cases'])):return None
 by={p.stem:hashlib.sha256(p.read_bytes()).hexdigest()for p in fixtures}
 if any(x.get('fixtureSHA256')!=by.get(x['fixture'])for x in data['cases']):return None
 if {x['fixture']for x in data['cases']}!=set(by):return None
 audit=r/'sheets'/(leaf+'-audit.json');completed=audit.stat().st_mtime_ns
 for mode in ['light','dark']:
  for p in [r/'probes'/(leaf+'-'+mode+'.html'),r/'sheets'/(leaf+'-'+mode+'.png')]:
   if not p.exists()or p.stat().st_mtime_ns>completed:return None
 p=browser.new_page(viewport={'width':1280,'height':720});p.set_content('<style>html,body{margin:0;width:1280px;height:720px;overflow:hidden}'+current_css+'</style><section class="slide"><div class="page"><div class="body"></div></div></section>');rows=[]
 try:
  for mode in ['light','dark']:
   old=(r/'probes'/(leaf+'-'+mode+'.html')).read_text();match=re.search(r'<style>(.*?)</style>',old,re.S)
   if not match:return None
   p.evaluate('(mode)=>document.querySelector(".slide").className="slide"+(mode==="dark"?" dark":"")',mode)
   for f in fixtures:
    content=re.sub(r'\A<!--.*?-->\s*','',f.read_text(),flags=re.S);p.evaluate('(s)=>document.querySelector(".body").innerHTML=s',content)
    a=p.evaluate(ACTIVE_JS,[match[1],'html,body{margin:0;width:1280px;height:720px;overflow:hidden}'+current_css]);rows.append({'fixture':f.stem,'mode':mode,**a})
    if not a['equal']:return None
 finally:p.close()
 return {'method':'Same fixture SHA-256 and identical ordered matching CSS declarations, including all container branches; nonmatching cover/page/other element rules are ignored. Completed probe and PNG timestamps precede the audit. Rendered pixels and per-case contrast evidence are reused without alteration.','oldSourceSHA256':data['sourceSHA256'],'fixtures':rows}
