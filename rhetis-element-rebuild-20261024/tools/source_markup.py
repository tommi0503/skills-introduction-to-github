"""Contract markup from frozen source-map data; no layout decisions or CSS here."""
from html import escape
import re,json
from bs4 import BeautifulSoup

def txt(v):return escape(str(v or '')).replace('\n','<br>')
def part(c,v,tag='p'):return '<'+tag+' class="'+c+'">'+txt(v)+'</'+tag+'>' if v is not None and str(v).strip() else ''
def source_markup(name,i,children=()):
 leaf=i['leaf'];d=i.get('data')or i.get('reconstruction')or{};cl=' '.join(i.get('contractClasses',[]));use=i['use']
 if use.startswith('variant:'):cl+=' '+use.split(':',1)[1].replace('.','')
 def root(c,inside,tag='div',attrs=''):
  return '<'+tag+' class="'+c+(' '+cl.strip() if cl.strip() else '')+'" data-el="'+name+'-'+leaf+'"'+attrs+'>'+inside+'</'+tag+'>'
 raw=i.get('sourceMarkup')or i.get('reassembly_markup')
 if raw:return raw
 if leaf=='card':
  kick=part('kick',d.get('kick'));note=part('note',d.get('note') or '\n'.join(d.get('noteText',[])))
  for child in children:
   mark=source_markup(name,child)
   if child.get('part')=='kick':kick='<div class="kick">'+mark+'</div>'
   elif child.get('part')=='note':note=note[:-4]+mark+'</p>' if note else '<div class="note">'+mark+'</div>'
  mark=part('mark',d.get('mark'),'span')
  if d.get('markIcon'):mark='<span class="mark"><span class="icon" data-icon="'+escape(d['markIcon'])+'"></span></span>'
  return root('card','<div class="parts">'+kick+mark+part('fig',d.get('fig'),'div')+part('name',d.get('name'),'h3')+note+'</div>')
 if leaf=='headline':
  h=d.get('h2',d.get('heading',''));h=txt(h)
  for b in d.get('emphasis',[]):h=h.replace(txt(b),'<b>'+txt(b)+'</b>')
  return root('headline',part('kick',d.get('kick'))+'<h2>'+h+'</h2>'+part('note',d.get('note')))
 if leaf=='prose':
  ps=d.get('paragraphs',[d.get('paragraph','')]);return root('prose',''.join('<p>'+txt(p)+'</p>' for p in ps))
 if leaf=='callout':
  s=txt(d.get('sentence',''));bold=d.get('bold');s=s.replace(txt(bold),'<b>'+txt(bold)+'</b>') if bold else s
  return root('callout','<p>'+s+'</p>')
 if leaf=='image-frame':return root('frame','<div class="seat" data-ph="'+str(d.get('placeholder',1))+'"></div>')
 if leaf=='tag':return root('tag',txt(d.get('label','')),'span')
 if leaf=='pill':return root('pill','<div class="parts">'+part('mark',d.get('mark'),'span')+part('name',d.get('name'),'span')+part('note',d.get('note'),'span')+'</div>')
 if leaf=='metric':return root('stat','<div class="parts">'+part('fig',d.get('fig'),'div')+part('name',d.get('name'))+part('note',d.get('note'))+'</div>')
 if leaf=='logo-group':return root('logos',''.join('<div class="seat logo" data-ph="'+str(k+1)+'"></div>' for k in range(d.get('members',3))))
 if leaf=='legend':return root('legend',''.join('<span class="key tone-'+str(k+1)+'">'+txt(t)+'</span>' for k,t in enumerate(d.get('keys',[]))))
 if leaf=='list':
  xs=d.get('items') or d.get('sourceText',[]);body=''
  if len(xs)==1 and '\n'in xs[0]:xs=xs[0].split('\n')
  for t in xs:
   if isinstance(t,dict):body+='<div class="item">'+part('name',t.get('name'))+part('note',t.get('note'))+'</div>'
   else:body+='<div class="item">'+part('name',t)+'</div>'
  return root('list',body)
 if leaf=='agenda':
  body=''
  for e in d['entries']:
   a=e.split('\n');body+='<div class="entry">'+part('mark',a[0],'span')+part('name',a[1]if len(a)>1 else a[0])+part('note','\n'.join(a[2:]))+'</div>'
  return root('agenda',body)
 if leaf=='quote':
  q=d.get('quote')or '\n'.join(d.get('quoteText',[]));by=('<div class="seat avatar" data-ph="'+str(d['avatar'])+'"></div>' if d.get('avatar')else '')+part('name',d.get('name'))+part('note',d.get('note'))
  return root('quote','<blockquote>'+txt(q)+'</blockquote><div class="by">'+by+'</div>')
 if leaf=='person':
  members=d.get('members',[]);body=''
  for k,m in enumerate(members):
   source=m.get('sourceText','');bio=m.get('note') or m.get('bio') or '\n'.join(s for s in source.split('\n') if s.strip() and s.strip()!=m['name'] and not s.strip().isdigit())
   photo='portrait'if m.get('portrait')or name=='lamella'else'avatar';ph=m.get('portrait',k+1)
   body+='<div class="person" data-el="'+name+'-person"><div class="seat '+photo+'" data-ph="'+str(ph)+'"></div>'+part('name',m.get('name'))+part('note',bio)+'</div>'
  return root('people',body)
 if leaf=='chart-donut':
  if 'items'in d:
   body=''.join('<div class="donut" data-el="'+name+'-chart-donut" style="--v:'+str(a['value'])+'"><div class="fig">'+str(a['value'])+'<small>%</small></div>'+part('name',a['name'])+'</div>' for a in d['items']);return root('donuts',body)
  return root('donut','<div class="fig"><b>'+txt(d.get('fig'))+'</b><small>'+txt(d.get('small'))+'</small></div>'+part('name',d['name']),attrs=' style="--v:'+str(d['value'])+'"')
 if leaf=='chart-bar':return root('bars',''.join('<div class="bar" style="--v:'+str(v)+'">'+('<b>'+txt(d['shown_values'][k])+'</b>'if d.get('shown_values',[None]*len(d['values']))[k]else '')+'<span>'+txt(d['labels'][k])+'</span></div>' for k,v in enumerate(d['values'])),attrs=' style="--max:'+str(d['max'])+'"')
 if leaf=='chart-area':
  body=''.join('<div class="series tone-'+str(k+1)+'">'+part('name',a.get('name'),'span')+''.join('<div class="pt" style="--v:'+str(v)+'"></div>' for v in a['values'])+'</div>' for k,a in enumerate(d['series']));body+='<div class="axis">'+''.join('<span>'+txt(a)+'</span>'for a in d['labels'])+'</div>';return root('areas',body,attrs=' style="--max:'+str(d['max'])+'"')
 raise ValueError('Missing source markup factory for '+name+'/'+leaf+'/'+i['page'])
