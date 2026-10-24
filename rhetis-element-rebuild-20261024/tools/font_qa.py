"""Actual rendered fonts for representative direct text and generated labels."""
import json
COLLECT=r'''()=>{let root=document.querySelector('.body')?.firstElementChild||document.querySelector('.slide'),seen=new Set(),i=0,out=[];if(!root)return out;for(let e of [root,...root.querySelectorAll('*')]){let st=getComputedStyle(e),r=e.getBoundingClientRect();if(st.display==='none'||st.visibility==='hidden'||r.width<.1||r.height<.1)continue;let text=[...e.childNodes].filter(n=>n.nodeType===3).map(n=>n.textContent).join('').trim(),sources=[];if(text)sources.push({pseudo:null,text,style:st});for(let pseudo of ['::before','::after']){let ps=getComputedStyle(e,pseudo);if(ps.content&& !['none','normal','""'].includes(ps.content))sources.push({pseudo,text:ps.content,style:ps})}for(let src of sources){let key=src.style.fontFamily+'|'+src.style.fontWeight+'|'+(/[가-힣]/.test(src.text)?'ko':/[a-z]/i.test(src.text)?'latin':'other')+'|'+src.pseudo+'|'+[...new Set([...src.text].filter(c=>c.codePointAt(0)>127&&!/[가-힣\s]/.test(c)))].sort().join('');if(seen.has(key))continue;seen.add(key);let id=e.getAttribute('data-rhetis-font-probe');if(!id){id='f'+i++;e.setAttribute('data-rhetis-font-probe',id)}out.push({id,pseudo:src.pseudo,text:src.text.slice(0,100),requested:src.style.fontFamily,weight:src.style.fontWeight})}}return out}'''
def actual_fonts(page,cdp):
 representatives=page.evaluate(COLLECT);doc=cdp.send('DOM.getDocument')['root']['nodeId'];details=[];allfonts={}
 for a in representatives:
  node=cdp.send('DOM.querySelector',{'nodeId':doc,'selector':'[data-rhetis-font-probe="'+a['id']+'"]'})['nodeId']
  if not node:continue
  if a['pseudo']:
   descr=cdp.send('DOM.describeNode',{'nodeId':node,'depth':1})['node'];typ=a['pseudo'][2:];p=next((p for p in descr.get('pseudoElements',[])if p.get('pseudoType')==typ),None)
   if p:
    node=p.get('nodeId',0)
    if not node:node=cdp.send('DOM.pushNodesByBackendIdsToFrontend',{'backendNodeIds':[p['backendNodeId']]})['nodeIds'][0]
  fonts=cdp.send('CSS.getPlatformFontsForNode',{'nodeId':node})['fonts']if node else[];a['fonts']=fonts;details.append(a)
  for font in fonts:
   k=(font['familyName'],font.get('postScriptName'),font['isCustomFont']);allfonts.setdefault(k,dict(font,glyphCount=0));allfonts[k]['glyphCount']+=font['glyphCount']
 page.evaluate('()=>document.querySelectorAll("[data-rhetis-font-probe]").forEach(e=>e.removeAttribute("data-rhetis-font-probe"))')
 return {'platform_fonts':list(allfonts.values()),'font_nodes':details,'font_probe_version':2,'load_errors':page.evaluate('()=>[...document.fonts].filter(f=>f.status==="error").map(f=>f.family)')}
