from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright
from PIL import Image
from html import escape
import json,threading,hashlib,sys
from sheets import context
from reassemble import palette,graphic
from font_qa import actual_fonts
R=Path('/workspace/work/rebuild');B=R/'toggle-grid/build';D=B/'toggle-apparatus';D.mkdir(exist_ok=True);P=json.loads((B/'foundation-toggle-proposal.json').read_text());src=json.loads((B/'source-toggle-furniture.json').read_text());pal=palette('toggle-grid');proof=[]
styles=context('toggle-grid')+'.slide{'+''.join(k+':'+v+';'for k,v in pal.items())+'}'
for page in [f'{i:02}'for i in range(1,13)]:
 entries=[i for i in P['instances']if i['page']==page];cover=any(i.get('cover')for i in entries);back=next(i for i in entries if i['use']=='background'and not i.get('region'));app=[]
 for i in entries:
  if i['use']!='furniture':continue
  slot=i['foundation_slot'];content=graphic(i,'toggle-grid')if slot=='deco'else i.get('reassembly_markup','')
  if not content:continue
  st={f'--toggle-grid-furn-{k}':str(v)+'px'for k,v in zip(['x','y','w','h'],i['bbox'])}
  if i.get('title_font'):st['--toggle-grid-furn-font-ratio']=str(i['title_font']/i['bbox'][2])
  if i.get('foreground_role'):st['--toggle-grid-furn-foreground']='var('+i['foreground_role']+')'
  if i.get('surface_role'):st['--toggle-grid-furn-surface']='transparent'if i['surface_role']=='transparent'else'var('+i['surface_role']+')'
  if i.get('source_font_size'):
   steps=json.loads((R.parent/'reference/contract/type-steps.json').read_text());v=min(steps,key=lambda s:abs(s-i['source_font_size']));st['--toggle-grid-furn-font-size']='var(--type-'+str(v)+')'
  st.update(i.get('foundation_tokens',{}));tag='header'if slot=='head'else'footer'if slot=='foot'else'div';cl=slot+(' at-top-left'if slot=='lockup'else'');app.append('<'+tag+' class="'+cl+'" style="'+escape(';'.join(k+':'+v for k,v in st.items()),quote=True)+'">'+content+'</'+tag+'>')
 html='<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../../review/assets/fonts/fonts.css"><style>'+styles+'</style></head><body><section class="slide'+(' cover'if cover else'')+'"><div class="page" style="--toggle-grid-surface:var('+back['role']+');--toggle-grid-foreground:var('+back.get('foreground_role','--ink')+')">'+''.join(app)+'</div></section></body></html>';(D/f'slide_{page}.html').write_text(html)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R)));threading.Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright()as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-breakpad','--disable-crash-reporter']);pg=browser.new_page(viewport={'width':1280,'height':720});cdp=pg.context.new_cdp_session(pg);cdp.send('DOM.enable');cdp.send('CSS.enable')
 for page in [f'{i:02}'for i in range(1,13)]:
  f=D/f'slide_{page}.html';pg.goto(f'http://127.0.0.1:{server.server_port}/toggle-grid/build/toggle-apparatus/{f.name}');pg.evaluate('document.fonts.ready');qa=pg.evaluate('''()=>{let out=[],w=document.createTreeWalker(document.querySelector('.slide'),NodeFilter.SHOW_TEXT);while(w.nextNode()){let n=w.currentNode,e=n.parentElement;if(!n.textContent.trim())continue;let r=document.createRange();r.selectNodeContents(n);for(let b of r.getClientRects())if(b.width&&(b.left<-.5||b.top<-.5||b.right>1280.5||b.bottom>720.5))out.push({text:n.textContent,box:[b.x,b.y,b.width,b.height]})}let styles={};for(let s of ['.lockup>.title','.head>.title','.head>.kicker','.head>.lead','.rail>.title','.rail>.lead','.foot>.no','.foot>.deck','.foot>.src','.top']){let e=document.querySelector(s);if(!e)continue;let c=getComputedStyle(e),b=e.getBoundingClientRect();styles[s]={font:c.fontFamily,size:parseFloat(c.fontSize),weight:c.fontWeight,line:c.lineHeight,tracking:c.letterSpacing,stretch:c.fontStretch,bbox:[b.x,b.y,b.width,b.height]}}return{page:[document.querySelector('.slide').offsetWidth,document.querySelector('.slide').offsetHeight],textOutside:out,styles}}''');qa.update(source_page=page,font_proof=actual_fonts(pg,cdp),html_sha256=hashlib.sha256(f.read_bytes()).hexdigest());pg.screenshot(path=str(f.with_suffix('.png')));proof.append(qa)
  original=Image.open(R.parent/'delivery/toggle-grid/review/replica'/f'slide_{page}.png').convert('RGB');ours=Image.open(f.with_suffix('.png')).convert('RGB');im=Image.new('RGB',(2560,720));im.paste(original,(0,0));im.paste(ours,(1280,0));im.save(D/f'compare_{page}.png')
 browser.close()
server.shutdown();report={'collection':'toggle-grid','scope':'source page furniture only; body components intentionally omitted from temporary comparison','source_pages':12,'source_hashes':{str(f.relative_to(R/'toggle-grid')):hashlib.sha256(f.read_bytes()).hexdigest()for f in [R/'toggle-grid/toggle-grid/foundation/foundation.css',R/'toggle-grid/toggle-grid/foundation/foundation.json',R/'toggle-grid/toggle-grid/kit/kit.json',R/'toggle-grid/review/assets/fonts/fonts.css']},'native_font_probe':src['native_width_probe'],'pages':proof};(R/'toggle-grid/review/validation/foundation-toggle-source.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('source12',[(i['source_page'],len(i['textOutside']),i['font_proof']['load_errors'])for i in proof])
