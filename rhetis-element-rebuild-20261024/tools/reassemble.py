"""Assemble source map once, before visual inspection. All appearance CSS is collection-owned.
The only authored per-page information is source geometry, palette data and contract content.
"""
from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
import json,math,re,hashlib,sys
from source_markup import source_markup
from sheets import context
from guard_grid import tracks as guarded_tracks
R=Path('/workspace/work/rebuild');OLD=Path('/workspace/work/delivery')

def tracks(entries,axis,extent,count):
 weights={0.:1e12,float(extent):1e12}
 for a in entries:
  b=a['bbox'];weight=math.sqrt(max(1,b[2]*b[3]));
  for x in [b[axis],b[axis]+b[axis+2]]:weights[float(x)]=weights.get(float(x),0)+weight
 nodes=[(v,w)for v,w in sorted(weights.items())]
 # Coalesce arithmetic-equivalent endpoints before allocating positive tracks.
 merged=[]
 for value,weight in nodes:
  if merged and value-merged[-1][0]<=1e-6:
   prev,pw=merged[-1];merged[-1]=((prev*pw+value*weight)/(pw+weight),pw+weight)
  else:merged.append((value,weight))
 nodes=merged
 while len(nodes)>count+1:
  costs=[(nodes[k+1][0]-nodes[k][0])**2*nodes[k][1]*nodes[k+1][1]/(nodes[k][1]+nodes[k+1][1]) for k in range(len(nodes)-1)];k=min(range(len(costs)),key=costs.__getitem__);a,wa=nodes[k];b,wb=nodes[k+1];nodes[k:k+2]=[((a*wa+b*wb)/(wa+wb),wa+wb)]
 points=[v for v,w in nodes];points[0]=0;points[-1]=extent
 while len(points)<count+1:
  k=max(range(len(points)-1),key=lambda k:points[k+1]-points[k]);points.insert(k+1,(points[k]+points[k+1])/2)
 return points

def palette(name):
 p=json.loads((R/'profiles.json').read_text())[name];page=p['page'];ink=p['ink'];a=p['accents'];v={'--page':page,'--ink':ink}
 neutral={'--n-1':'#fafafa','--n-2':'#e5e5e5','--n-3':'#d3d3d3','--n-4':'#b9b9b9','--n-5':'#929292','--n-6':'#767676','--n-7':'#5f5f5f','--n-8':'#373737','--n-9':'#202020'};v.update(neutral)
 for k,c in enumerate(a,1):
  v['--a'+str(k)]=c;v['--a'+str(k)+'-on']=page if name in['cutfield','filament','portico','lamella','rulemark'] else ink
  for s in range(1,10):
   for ending in ['', '-soft','-muted']:
    mix=100-abs(5-s)*17 if s>=5 else s*15
    base=ink if s>5 else page
    v[f'--a{k}-{s}{ending}']=f'color-mix(in srgb,{c} {mix}%,{base})'
 if name=='tide-tab':v.update({'--n-1':'#ffffff','--n-3':'#dce5f3','--n-7':'#65749c','--a1-1-soft':'#effafd','--a2-1-soft':'#eff2fc','--a1-3-soft':'#a8c4d6'})
 if name=='cutfield':v.update({'--n-1':'#ffffff','--n-3':'#dddddd','--a1-9':'#0a3033','--a1-on':'#0a3033','--a2-on':'#0a3033'})
 if name=='filament':v.update({'--a1-8':'#a43527','--n-2':'#deded9'})
 if name=='portico':v.update({'--n-1':'#ffffff','--n-2':'#f1f0e7','--n-3':'#dcd3b9','--n-4':'#d8d2bb','--n-5':'#c3c3b1','--n-7':'#978d61','--a1-7':'#244859','--a1-9':'#152e39'})
 if name=='toggle-grid':v.update({'--n-2':'#d1d1cf','--n-3':'#bababa','--n-5':'#777777','--a1-on':'#141414'})
 if name=='lamella':v.update({'--n-1':'#ffffff','--n-5':'#b8b8b8','--a1-2-soft':'#cdd1ec','--a1-3-soft':'#a1aad5','--a1-7':'#5c6dbe','--a2-7':'#6953b9'})
 if name=='rulemark':v.update({'--page':'#f6f6f6','--n-1':'#e7e7e7','--n-4':'#9a9a9a','--n-5':'#777777','--a1-7':'#000000'})
 return v

def recolor_svg(html,name):
 """Text-free furniture only; convert every paint to palette roles, preserve geometry."""
 assert '<text' not in html.lower(),'No SVG text workaround'
 p=palette(name);colors={}
 for k,v in p.items():
  if re.fullmatch('#[a-fA-F0-9]{6}',v):colors.setdefault(v.lower(),k)
 def role(c):
  c=c.lower()
  if c in ['none','transparent','currentcolor']:return c
  if c in ['white','#fff']:c='#ffffff'
  if c in ['black','#000']:c='#000000'
  if c in colors:return 'var('+colors[c]+')'
  if c.startswith('url('):return c
  if c.startswith('var('):
   if re.fullmatch(r'var\(--(?:a[1-9]\d*(?:-[1-9](?:-soft|-muted)?|-on)?|n-[1-9]|page|ink|good|warn|bad)\)',c):return c
   fallback=re.search(r'#[a-fA-F0-9]{6}',c)
   return role(fallback[0])if fallback else 'currentColor'
  if c.startswith('#'):
   c=c if len(c)==7 else '#'+''.join(x*2 for x in c[1:]);rgb=tuple(int(c[k:k+2],16)for k in(1,3,5));opts=[]
   for h,k in colors.items():rr=tuple(int(h[j:j+2],16)for j in(1,3,5));opts.append((sum((a-b)**2 for a,b in zip(rgb,rr)),k))
   return 'var('+min(opts)[1]+')'
  if c.startswith('rgb'):
   nums=re.findall(r'[\d.]+',c)
   if len(nums)>=3:return role('#'+''.join(f'{round(float(x)):02x}'for x in nums[:3]))
  return 'currentColor'
 soup=BeautifulSoup(html,'xml');svg=soup.find('svg')
 if not svg:
  soup=BeautifulSoup('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">'+html+'</svg>','xml');svg=soup.svg
 for e in soup.find_all():
  e.attrs.pop('class',None)
  for k in ['fill','stroke','stop-color']:
   if e.has_attr(k):e[k]=role(e[k])
  if e.has_attr('style'):
   s=e['style'];s=re.sub(r'(fill|stroke|stop-color)\s*:\s*([^;]+)',lambda m:m[1]+':'+role(m[2]),s);s=re.sub(r'(position|inset|width|height)\s*:[^;]+;?','',s);e['style']=s
 return str(svg)

def graphic(i,name):
 if i.get('source_svg'):return recolor_svg(i['source_svg'],name)
 b=i['bbox'];w,h=b[2:];kind=i.get('graphic');ink='var(--ink)';page='var(--page)'
 if kind=='hairline':return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 '+str(w)+' '+str(h)+'"><rect width="100%" height="100%" fill="var('+i.get('role','--n-4')+')"/></svg>'
 if kind=='split-rule':return '' # canonical page::after owns it
 if kind=='circle-chevron-down' or kind=='circle-chevron-right':
  pts='35,43 50,59 65,43'if kind.endswith('down')else'43,35 59,50 43,65';face=i.get('role','--ink');fore='--ink'if face=='--page'else'--page';return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="50" fill="var({face})"/><polyline points="{pts}" fill="none" stroke="var({fore})" stroke-width="4"/></svg>'
 if kind=='corner-arrow':return recolor_svg('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">'+i['source_svg_part']+'</svg>',name)
 if kind=='dotted-circles':
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 772 772">'+''.join('<circle cx="386" cy="386" r="'+str(d/2)+'" fill="none" stroke="var(--n-5)" stroke-width="1" stroke-dasharray="3 5"/>'for d in i['diameters'])+'</svg>'
 return ''

def build(name):
 D=R/name/'build';V=R/name/'review';m=json.loads((V/'map.json').read_text());out=V/'reassembled';out.mkdir(exist_ok=True);source=json.loads((D/'source-dom.json').read_text());layouts={};pal=palette(name)
 used=set()
 for inst in m['instances']:
  if not inst.get('leaf')or inst['use']=='unexpressible':continue
  used.add(inst['leaf'])
  markup=source_markup(name,inst,[child for child in m['instances']if child.get('parent')==inst['id']])
  used.update(re.findall(r'data-el=[\'\"]'+re.escape(name)+r'-([\w-]+)[\'\"]',markup))
 styles=context(name,used)+'.slide{'+''.join(k+':'+v+';'for k,v in pal.items())+'}'
 collection=R/name/name
 foundation=json.loads((collection/"foundation/foundation.json").read_text())
 inputs=[collection/'kit/kit.json',collection/'kit/css/tokens.css',collection/'foundation/foundation.css',collection/'foundation/foundation.json']
 for leaf in sorted(used):inputs.extend([collection/'elements'/leaf/'element.css',collection/'elements'/leaf/'element.json'])
 inputs+=[V/'map.json',R/'profiles.json',V/'assets/fonts/fonts.css',V/'assets/lucide.js']
 (D/'reassembly-used-elements.json').write_text(json.dumps(sorted(used),indent=2))
 import os
 (D/'reassembly-inputs.json').write_text(json.dumps({os.path.relpath(p,R/name):hashlib.sha256(p.read_bytes()).hexdigest()for p in inputs if p.exists()},indent=2))
 for page in source:
  entries=[a for a in m['instances']if a['page']==page];leaves=[a for a in entries if a.get('leaf') and not a.get('parent')];furn=[a for a in entries if a['use']=='furniture'];cover=any(a.get('cover')and a.get('foundation_slot')=='lockup'for a in furn)
  if leaves and not cover:
   x=min(a['bbox'][0]for a in leaves);y=min(a['bbox'][1]for a in leaves);r=max(a['bbox'][0]+a['bbox'][2]for a in leaves);bot=max(a['bbox'][1]+a['bbox'][3]for a in leaves);x=max(0,x);y=max(0,y);r=min(1280,r);bot=min(720,bot);box=[x,y,r-x,bot-y]
   relative=[dict(a,bbox=[a['bbox'][0]-x,a['bbox'][1]-y,*a['bbox'][2:]])for a in leaves];xs=tracks(relative,0,box[2],12);ys=tracks(relative,1,box[3],6)
  else:box=[0,0,1280,720];xs=[k*1280/12 for k in range(13)];ys=[k*120 for k in range(7)]
  # Detect source-disjoint boxes that nearest-track rounding would overlap.
  # This uses only source boxes, never element CSS or rendered appearance.
  row_index=None
  if leaves and not cover:
   def old_row(b):
    a=min(range(7),key=lambda k:abs(ys[k]-(b[1]-box[1])));z=max(a+1,min(range(7),key=lambda k:abs(ys[k]-(b[1]+b[3]-box[1]))));return min(a,5),min(z,6)
   collision=False
   for ai,a in enumerate(leaves):
    for b in leaves[ai+1:]:
     u,v=a['bbox'],b['bbox'];ar,br=old_row(u),old_row(v)
     same_x=min(u[0]+u[2],v[0]+v[2])-max(u[0],v[0])>1
     separated_y=u[1]+u[3]<=v[1]+1 or v[1]+v[3]<=u[1]+1
     if same_x and separated_y and min(ar[1],br[1])>max(ar[0],br[0]):collision=True
   if collision:ys,row_index=guarded_tracks(relative,1,box[3],6)
  geometry={f'--{name}-body-'+k:str(round(v,4))+'px' for k,v in zip(['x','y','w','h'],box)}
  geometry[f'--{name}-grid-columns']=' '.join(str(round(xs[k+1]-xs[k],6))+'fr'for k in range(12));geometry[f'--{name}-grid-rows']=' '.join(str(round(ys[k+1]-ys[k],6))+'fr'for k in range(6));geometry[f'--{name}-grid-gap']='0px'
  back=next(a for a in entries if a['use']=='background'and not a.get('region'));geometry[f'--{name}-surface']='var('+back['role']+')';geometry[f'--{name}-foreground']='var('+back.get('foreground_role','--ink')+')'
  children=[];placed=[]
  for a in leaves:
   b=a['bbox'];ix=lambda v: min(range(13),key=lambda k:abs(xs[k]-v));iy=lambda v:row_index[min(row_index,key=lambda k:abs(k-v))]if row_index is not None else min(range(7),key=lambda k:abs(ys[k]-v));c1=ix(b[0]-box[0]);c2=max(c1+1,ix(b[0]+b[2]-box[0]));r1=iy(b[1]-box[1]);r2=max(r1+1,iy(b[1]+b[3]-box[1]));c1=min(c1,11);c2=min(c2,12);r1=min(r1,5);r2=min(r2,6)
   raw=source_markup(name,a,[x for x in entries if x.get('parent')==a['id']]);s=BeautifulSoup(raw,'html.parser');root=s.find();assert root and root.get('data-el')==name+'-'+a['leaf'],a['id'];prev=root.get('style','');root['style']=prev+(';'if prev else '')+f'grid-column:{c1+1} / span {c2-c1};grid-row:{r1+1} / span {r2-r1}'
   if a.get('foundation_context')=='on':
    layout=root['style'];root['style']=';'.join(q for q in layout.split(';')if not q.strip().startswith(('grid-column','grid-row')));children.append('<div class="group on" style="'+f'grid-column:{c1+1} / span {c2-c1};grid-row:{r1+1} / span {r2-r1}'+'">'+str(root)+'</div>')
   else:children.append(str(root))
   actual=[box[0]+xs[c1],box[1]+ys[r1],xs[c2]-xs[c1],ys[r2]-ys[r1]];placed.append({'id':a['id'],'bbox':b,'grid':[c1+1,c2-c1,r1+1,r2-r1],'render_slot':actual,'difference':[round(v-b[k],3)for k,v in enumerate(actual)]})
  apparatus=[]
  for a in furn:
   slot=a['foundation_slot'];b=a['bbox'];content=a.get('reassembly_markup','')
   if slot=='deco':content=graphic(a,name)
   if not content:continue
   st={f'--{name}-furn-'+k:str(round(v,5))+'px' for k,v in zip(['x','y','w','h'],b)}
   if a.get('text_align'):st[f'--{name}-furn-align']=a['text_align']
   if a.get('rotation_degrees')is not None:st[f'--{name}-furn-rotation']=str(a['rotation_degrees'])+'deg'
   for token,value in a.get('foundation_tokens',{}).items():
    assert token.startswith('--'+name+'-'),(a.get('id'),token)
    assert token in foundation['tokenDefaults'],(a.get('id'),'undeclared foundation token',token)
    st[token]=str(value)
   if a.get('foreground_device'):st[f'--{name}-furn-depth']='3'
   if a.get('surface_role'):st[f'--{name}-furn-surface']='var('+a['surface_role']+')' if a['surface_role']!='transparent'else'transparent'
   if a.get('foreground_role'):st[f'--{name}-furn-foreground']='var('+a['foreground_role']+')'
   if a.get('source_font_size'):
    steps=json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text());step=min(steps,key=lambda x:abs(x-a['source_font_size']));st[f'--{name}-furn-font-size']='var(--type-'+str(step)+')'
   if a.get('title_font')and b[2]>0:st[f'--{name}-furn-font-ratio']=str(a['title_font']/b[2])
   tag='header'if slot=='head'else'footer'if slot=='foot'else'div';cl=slot+(' at-top-left'if slot=='lockup'else'');apparatus.append('<'+tag+' class="'+cl+'" style="'+escape(';'.join(k+':'+v for k,v in st.items()),quote=True)+'">'+content+'</'+tag+'>')
  for a in entries:
   if a['use']=='background'and a.get('region'):
    aa=dict(a,foundation_slot='deco',graphic='hairline');b=aa['bbox'];st=';'.join(f'--{name}-furn-'+k+':'+str(v)+'px'for k,v in zip(['x','y','w','h'],b));apparatus.insert(0,'<div class="deco" style="'+st+'">'+graphic(aa,name)+'</div>')
  pagecontext=next((a.get('context')for a in entries if a['use']=='background'),'base');pgclass='page'+(' on'if pagecontext=='on'else'');pgstyle=escape(';'.join(k+':'+v for k,v in geometry.items()),quote=True)
  html='<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=1280"><title>'+name+' '+page+'</title><link rel="stylesheet" href="../assets/fonts/fonts.css"><style>'+styles+'</style></head><body><section class="slide'+(' cover'if cover else'')+'"><div class="'+pgclass+'" style="'+pgstyle+'">'+''.join(apparatus)+(''if cover else'<div class="body">'+''.join(children)+'</div>')+'</div></section><script src="../assets/lucide.js"></script></body></html>'
  (out/('slide_'+page+'.html')).write_text(html);layouts[page]={'body_box':box,'columns':xs,'rows':ys,'instances':placed,'source_map_sha256':hashlib.sha256((V/'map.json').read_bytes()).hexdigest()}
 (D/'layout-before-render.json').write_text(json.dumps(layouts,ensure_ascii=False,indent=2));print(name,len(layouts),'assembled contract pages; geometry frozen before rendering')
if __name__=='__main__':
 for n in (sys.argv[1:]or['tide-tab','cutfield','filament','portico','toggle-grid','lamella','rulemark']):build(n)
