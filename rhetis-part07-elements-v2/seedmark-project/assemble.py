"""Fresh contract-only assembly from the measured map; no per-page styling."""
from pathlib import Path
import ast,json,re,math,html as escape
from types import SimpleNamespace
from lxml import html
P=Path(__file__).parent;C=P/'seedmark';M=json.loads((P/'map.json').read_text());RAW={p['page']:p['nodes']for p in M['rawMeasurements']}
# Load pure markup functions only; importing the fixture writer during a render would mutate inputs.
namespace={'P':P,'C':C,'A':M,'RAW':RAW,'F':SimpleNamespace(fresh=lambda t,seed=0:t),'html':html,'re':re,'math':math}
mod=ast.parse((P/'source_instances.py').read_text());exec(compile(ast.Module(body=[n for n in mod.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'source_markup','exec'),namespace)
make=namespace['make'];text=namespace['original_html'];O=P/'reassembled';O.mkdir(exist_ok=True)
links=['../assets/fonts/fonts.css','../seedmark/kit/css/tokens.css','../seedmark/foundation/foundation.css']+[f'../seedmark/elements/{e.name}/element.css'for e in sorted((C/'elements').iterdir())if e.is_dir()]+['../assets/source-palette.css']
# External source palette supplies colors only. The copied historical numeric defaults are deliberately unused.
records=[]
for page in range(1,22):
 ns=RAW[page];parts=[];top='<div class="top"><span>'+text(ns[0])+'</span><span>'+text(ns[1])+'</span></div>'
 if page==1:
  body='<section class="slide cover">'+top+'<div class="page"><div class="lockup at-left"><p class="kicker">'+text(ns[2])+'</p><h1 class="title">'+text(ns[3])+'<br>'+text(ns[4])+'</h1></div><div class="seat back" data-ph=""></div><div class="meta">'+text(ns[6])+'</div></div></section>'
 else:
  mapped=M['instances'];headnodes=[]
  for i in mapped:
   if i['page']==page and i.get('leaf')is None and i['use']=='furniture':
    for sel in i['selectors']:
     k=int(re.search(r'nth-child\((\d+)\)',sel).group(1))-1
     if k in[2,3]and ns[k].get('text','').strip():headnodes.append(k)
  kicker=2 if 2 in headnodes else None;title=3 if 3 in headnodes else None
  header='<header class="head">'+('<p class="kicker">'+text(ns[kicker])+'</p>'if kicker is not None else'')+('<h1 class="title">'+text(ns[title])+'</h1>'if title is not None else'')+'</header>'
  multiline=title is not None and '<br'in text(ns[title])
  y0=320 if multiline else(266 if title is not None else 138);height=638-y0;cw=(1112-11*24)/12;rh=(height-5*24)/6
  placed=[]
  for inst in mapped:
   if inst['page']!=page or not inst.get('leaf')or inst.get('parentId')and inst['id']!='sm-20-caption':continue
   if inst['use']=='unexpressible':parts.append('<!-- '+escape.escape(inst['id']+' unexpressible: '+str(inst.get('why','see GAPS.md')))+' -->');continue
   got=make(inst,True)
   if not got:continue
   markup,_=got;x,y,w,h=inst['bbox'];col=max(1,min(12,1+round((x-84)/(cw+24))));row=max(1,min(6,1+round((y-y0)/(rh+24))));cols=max(1,min(13-col,round((w+24)/(cw+24))));rows=max(1,min(7-row,round((h+24)/(rh+24))))
   if inst['leaf']=='legend':cols=max(2,cols)
   if inst['leaf']=='tag':cols=max(2,cols)
   if inst['leaf']=='concentric':cols=max(6,cols)
   grid=f'grid-column:{col} / span {cols};grid-row:{row} / span {rows}'
   opening=markup.split('>',1)[0]
   if 'style="'in opening:markup=markup.replace('style="','style="'+grid+';',1)
   else:markup=markup.replace('>',' style="'+grid+'">',1)
   parts.append('<!-- '+inst['id']+' -->'+markup);placed.append({'id':inst['id'],'bbox':inst['bbox'],'grid':[col,row,cols,rows]})
  footer='<div class="foot"><span></span><span>'+text(ns[25])+'</span><span></span></div>'if page==19 else''
  body='<section class="slide">'+top+footer+'<div class="page">'+header+'<div class="body">'+''.join(parts)+'</div></div></section>';records.append({'page':page,'bodyBBox':[84,y0,1112,height],'placements':placed})
 doc='<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Seedmark assembled '+str(page).zfill(2)+'</title>'+''.join('<link rel="stylesheet" href="'+s+'">'for s in links)+'<script defer src="../assets/lucide.min.js"></script><script defer src="../assets/render-icons.js"></script></head><body>'+body+'</body></html>'
 (O/f'slide_{page:02}.html').write_text(doc)
(P/'assembly-grid-records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2));print('21 fresh grid-only assembly sources written; no replica or asset changed.')
