"""Measure replica-to-assembly geometry and retain three-way visual evidence.
These diagnostics do not certify pixel identity; every structural difference requires review.
"""
from pathlib import Path
from difflib import SequenceMatcher
import json,sys,re,csv
from PIL import Image
from playwright.sync_api import sync_playwright
from render import ROOT,DECKS,url,ready,browser,source_fingerprint
JS=r'''()=>{const fontFiles={};for(const sheet of document.styleSheets){try{for(const rule of sheet.cssRules){if(rule.type===5){const family=rule.style.fontFamily.replace(/[\"']/g,'');const files=[...rule.style.src.matchAll(/([^/()\"']+\.woff2?)/g)].map(x=>x[1]);fontFiles[family]=[...new Set([...(fontFiles[family]||[]),...files])].sort();}}}catch{}}const all=[];for(const e of document.querySelectorAll('body *')){if(['SCRIPT','STYLE','SVG','PATH'].includes(e.tagName)||!e.textContent.trim()||![...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim()))continue;const s=getComputedStyle(e),r=e.getBoundingClientRect();if(!r.width||!r.height||s.display==='none'||r.width>1250&&r.height>650)continue;const text=e.innerText||e.textContent;if(text.trim().length>700)continue;const range=document.createRange();range.selectNodeContents(e);const t=range.getBoundingClientRect();all.push({text:text.trim(),tag:e.tagName,cls:typeof e.className==='string'?e.className:'svg',box:[r.x,r.y,r.width,r.height].map(v=>+v.toFixed(2)),textBox:[t.x,t.y,t.width,t.height].map(v=>+v.toFixed(2)),font:s.fontFamily,fontSources:fontFiles[s.fontFamily.split(',')[0].replace(/[\"']/g,'').trim()]||[],size:s.fontSize,weight:s.fontWeight,lineHeight:s.lineHeight,color:s.color,lines:range.getClientRects().length});}return all}'''
def norm(s):return re.sub(r'\s+','',s)
def run(kid,page):
 P=ROOT/(kid+'-project');out=P/'fidelity';out.mkdir(exist_ok=True);reports=[];initial={stage:source_fingerprint(P,kid,stage) for stage in ['replica','reassembled']}
 for f in sorted((P/'replica').glob('slide*.html')):
  pair=[];whole=[]
  for stage in ['replica','reassembled']:
   page.set_viewport_size({'width':1280,'height':720});page.goto(url(P/stage/f.name),wait_until='networkidle');ready(page);pair.append(page.evaluate(JS));whole.append(page.locator('.slide').inner_text())
  a,b=pair;used=set();matches=[];missing=[]
  for x in a:
   key=norm(x['text']);choices=[(i,y) for i,y in enumerate(b) if i not in used and norm(y['text'])==key]
   if not choices:
    missing.append({**x,'presentAcrossElements':key in norm(whole[1])});continue
   i,y=min(choices,key=lambda iy:sum(abs(v-w) for v,w in zip(x['textBox'][:2],iy[1]['textBox'][:2])))
   used.add(i);delta=[round(w-v,2) for v,w in zip(x['textBox'],y['textBox'])];matches.append({'text':x['text'],'replica':x,'reassembled':y,'deltaXYWH':delta,'fontEqual':bool(x.get('fontSources')) and all(x[z]==y[z] for z in ['fontSources','size','weight','lineHeight'])})
  report={'page':f.name,'matched':matches,'missingExactText':missing,'missingContentCandidates':[x for x in missing if not x['presentAcrossElements']],'additionalExactText':[x for i,x in enumerate(b) if i not in used],'note':'Missing exact text includes changed line breaks or rewritten wording. Geometry is measured in real browser pixels; zero clipping does not imply fidelity.'};reports.append(report)
  sources=[]
  compare=Image.open(P/'compare-replica'/f.with_suffix('.png').name).convert('RGB');sources=[compare.crop((0,0,1280,720)),Image.open(P/'replica'/f.with_suffix('.png').name).convert('RGB'),Image.open(P/'reassembled'/f.with_suffix('.png').name).convert('RGB')]
  triple=Image.new('RGB',(3840,720));[triple.paste(im,(i*1280,0)) for i,im in enumerate(sources)];triple.save(out/(f.stem+'-triple.png'))
  Image.blend(sources[1],sources[2],.5).save(out/(f.stem+'-overlay.png'))
 assert initial=={stage:source_fingerprint(P,kid,stage) for stage in initial},'source changed during fidelity capture'
 (out/'manifest.json').write_text(json.dumps(initial,indent=2))
 (out/'geometry.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2))
 with (out/'geometry.csv').open('w') as fp:
  w=csv.writer(fp);w.writerow(['page','text','dx','dy','dw','dh','fontEqual'])
  for r in reports:
   for m in r['matched']:w.writerow([r['page'],m['text'],*m['deltaXYWH'],m['fontEqual']])
 print(kid,'fidelity evidence',len(reports),'pages',flush=True)
if __name__=='__main__':
 with sync_playwright() as p:
  b=browser(p);page=b.new_page()
  for k in (sys.argv[1:] or DECKS):run(k,page)
  b.close()
