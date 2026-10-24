"""Diagnostic source-sized elements. Fixed positioning is confined to build/, never reassembled/."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright
from sheets import context, Quiet, JS
from reassemble import palette
from source_markup import source_markup
import json, threading, hashlib, io, sys

R=Path('/workspace/work/rebuild'); OLD=Path('/workspace/work/delivery')
FONT=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',14)

def run(names,leaves=None):
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R)))
 threading.Thread(target=server.serve_forever,daemon=True).start()
 with sync_playwright() as pw:
  browser=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-breakpad'])
  pg=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for name in names:
   m=json.loads((R/name/'review/map.json').read_text()); dest=R/name/'build/source-boxes';dest.mkdir(exist_ok=True);proof=[]
   styles=context(name)+'.slide{'+''.join(k+':'+v+';'for k,v in palette(name).items())+'}'
   for entry in m['instances']:
    if not entry.get('leaf') or entry['use'] in ['unexpressible','background','furniture']:continue
    if leaves and entry['leaf'] not in leaves:continue
    children=[x for x in m['instances'] if x.get('parent')==entry['id']]
    markup=source_markup(name,entry,children)
    soup=BeautifulSoup(markup,'html.parser');root=soup.find();x,y,w,h=entry['bbox']
    root['style']=root.get('style','')+f';position:fixed;left:{x}px;top:{y}px;width:{w}px;height:{h}px;grid-column:1;grid-row:1'
    # The source page supplies its inherited text context, never an element-specific rule.
    foreground='var(--page)'if entry.get('foundation_context')=='on'else'var(--ink)'
    doc='<!doctype html><html lang="ko"><meta charset="utf-8"><link rel="stylesheet" href="../../review/assets/fonts/fonts.css"><style>'+styles+'</style><body><section class="slide"><div class="page"><div class="body" style="color:'+foreground+'">'+str(soup)+'</div></div></section></body></html>'
    path=dest/(entry['id']+'.html');path.write_text(doc);pg.goto(f'http://127.0.0.1:{server.server_port}/{name}/build/source-boxes/{path.name}');pg.evaluate('document.fonts.ready')
    q=pg.evaluate(JS);q.pop('texts');q.update(id=entry['id'],page=entry['page'],leaf=entry['leaf'],source_bbox=entry['bbox'],css_sha256=hashlib.sha256((R/name/name/'elements'/entry['leaf']/'element.css').read_bytes()).hexdigest())
    q['metrics']=pg.locator('.body > :first-child').evaluate('''r=>[...r.querySelectorAll('.name,.note,.fig,h1,h2,p,blockquote,td,th')].map(e=>{let s=getComputedStyle(e),b=e.getBoundingClientRect();return{tag:e.tagName,class:e.className,text:e.textContent.slice(0,120),bbox:[b.x,b.y,b.width,b.height],font:parseFloat(s.fontSize),weight:s.fontWeight,line:s.lineHeight,tracking:s.letterSpacing}})''')
    q['font_errors']=pg.evaluate('()=>[...document.fonts].filter(f=>f.status==="error").map(f=>f.family)');proof.append(q)
    shot=Image.open(io.BytesIO(pg.screenshot())).convert('RGB');box=(round(x),round(y),round(x+w),round(y+h));src=Image.open(OLD/name/'review/replica'/('slide_'+entry['page']+'.png')).convert('RGB').crop(box);render=shot.crop(box)
    panel=Image.new('RGB',(src.width*2+36,src.height+40),'#dfe2e6');draw=ImageDraw.Draw(panel);draw.text((8,8),entry['id']+' replica',font=FONT,fill='#111');draw.text((src.width+28,8),'source-sized element',font=FONT,fill='#111');panel.paste(src,(8,32));panel.paste(render,(src.width+28,32));panel.save(path.with_suffix('.png'),optimize=True)
   target=dest/('validation-'+ '-'.join(sorted(leaves))+'.json'if leaves else'validation.json')
   target.write_text(json.dumps(proof,ensure_ascii=False,indent=2));print(name,len(proof),'source-sized comparisons',flush=True)
  browser.close()
 server.shutdown()

if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument('collections',nargs='*');parser.add_argument('--leaf',action='append');args=parser.parse_args()
 run(args.collections or list(json.loads((R/'profiles.json').read_text())),set(args.leaf)if args.leaf else None)
