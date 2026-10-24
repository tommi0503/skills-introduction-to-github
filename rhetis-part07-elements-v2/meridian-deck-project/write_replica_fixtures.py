from pathlib import Path
import json,re,html
P=Path(__file__).parent;C=P/'meridian-deck';raw=json.loads((P/'map-measurements.json').read_text());S={p['page']:{x['index']:x for x in p['parts']} for p in raw['pages']}
normalize=lambda x:re.sub(r'\s+','',x).casefold();banned={normalize(x['text'])[i:i+6] for p in raw['pages'] for x in p['parts'] for i in range(max(0,len(normalize(x['text']))-5))}
exec((P/'fresh_copy.py').read_text())
def txt(n,i):
 from lxml import html as L
 e=L.fromstring(S[n][i]['html'])
 def lines(t):return '<br>'.join(fresh(x) for x in (t or '').split('\n'))
 def inner(e):
  out=lines(e.text)
  for c in e:
   val=inner(c)
   out+=('<b>'+val+'</b>' if c.tag in ['b','strong'] else '<u>'+val+'</u>' if c.tag=='u' else '<br>' if c.tag=='br' else '<small>'+val+'</small>' if c.tag=='span' and re.search(r'font-size:\s*(?:1[0-4]|[6-9])px',c.get('style','')) else val)+lines(c.tail)
  return out
 return inner(e)
def headtxt(n,i):
 value=txt(n,i)
 return '<b>'+value+'</b>' if S[n][i].get('paint',{}).get('color')=='rgb(0, 99, 237)' and '<b>' not in value else value
def root(leaf,cls,body,style=''):return f'<div class="{cls}" data-el="meridian-deck-{leaf}"'+(f' style="{style}"' if style else '')+'>'+body+'</div>'
def place(v,c=1,r=1,w=12,h=6):return v.replace('>',f' style="grid-column:{c} / span {w};grid-row:{r} / span {h}">',1)
def group(xs,cls='group'):return '<div class="'+cls+'">'+''.join(xs)+'</div>'
def paragraphs(ts):return ''.join('<p>'+s+'</p>' for s in ts)
def save(leaf,n,body,mini='6x3',suffix=''):
 body=place(body);(C/'elements'/leaf/'fixtures'/f'replica-{n:02d}{suffix}.html').write_text(f'<!-- min: {mini} -->\n'+body+'\n')
def card(name,note='',kick='',fig='',mark='',cl=''):
 p=''.join(('<div class="note">'+x+'</div>') if c=='note' and ('<div' in x or '<p' in x) else f'<p class="{c}">{x}</p>' for c,x in [('kick',kick),('fig',fig),('name',name),('note',note)] if x)
 if mark:p='<span class="mark">'+mark+'</span>'+p
 return root('card','card '+cl,'<div class="parts">'+p+'</div>')
def pill(name,cl=''):return root('pill','pill '+cl,'<div class="parts"><b class="name">'+name+'</b></div>')
def prose(ts,cl=''):return root('prose','prose '+cl,paragraphs(ts))
def headline(title,cl='',kick='',note=''):return root('headline','headline '+cl,('<b class="kick">'+kick+'</b>' if kick else '')+'<h2>'+title+'</h2>'+('<p class="note">'+note+'</p>' if note else ''))
def lst(items,cl=''):return root('list','list '+cl,''.join('<div class="item"><b class="name">'+name+'</b>'+('<div class="note">'+note+'</div>' if '<div' in note else '<p class="note">'+note+'</p>')+'</div>' for name,note in items))
def bullets(n,i):return [(fresh(x.strip()),'') for x in S[n][i]['text'].split('•') if x.strip()]
def icon(name):return '<span class="icon" data-icon="'+name+'"></span>'
def photo(i=1,cl=''):return f'<div class="seat {cl}" data-ph="{i}"></div>'
# Cards: all source members remain present; each independent named design receives its own specimen.
save('card',5,group([card(txt(5,i),txt(5,i+1),cl='on') for i in [10,14,18]]),'9x3')
save('card',9,group([card(txt(9,i+3),txt(9,i+5),mark=icon(ic),cl='on') for i,ic in zip([8,14,20,26],['handshake','files','lightbulb','presentation'])]),'12x4')
save('card',11,group([card(txt(11,i+4),lst(bullets(11,i+5)),kick=txt(11,i+3),cl='line on') for i in [8,14]],'stack'),'5x6')
save('card',13,group([card(txt(13,11),mark=icon('message-circle'),cl='on'),card(txt(13,14),mark=icon('monitor-up'),cl='on')]),'8x2')
save('card',13,group([card('',lst(bullets(13,i+3)),kick=txt(13,i+2),cl='line') for i in [16,20,24]]),'12x2','-line')
save('card',16,group([card(txt(16,i+2),txt(16,i+3),kick=txt(16,i),mark=photo(j+1),cl='line' if j<2 else '') for j,i in enumerate([8,13,18])],'stack'),'12x6')
save('card',19,group([card(txt(19,i+1),txt(19,i+2)) for i in [10,13,16,19]],'group two'),'8x5')
save('card',20,group([card(txt(20,i+2),mark=icon(ic),cl='on') for i,ic in zip([9,16,23],['network','grid-3x3','calendar-days'])],'stack'),'3x5')
save('card',24,group([card(txt(24,i),'<p>'+txt(24,i+1)+'</p>'+lst([(txt(24,i+3),''),(txt(24,i+5),'')]),cl='line' if j<2 else '') for j,i in enumerate([11,18,25])],'stack'),'8x6')
save('card',27,group([card(txt(27,i+1),txt(27,i+3),cl='line') for i in [12,20,28]]),'12x3')
# Headlines use the exact count of source text blocks, with new language.
head_specs={3:([9],'big center',[8]),5:([20],'',[]),6:([10,17,24],'',[]),7:([10],'big on',[]),13:([8],'center',[]),14:([8],'big',[]),15:([8,9,10],'',[]),17:([8],'center',[]),19:([8,9],'',[]),20:([8],'center',[]),22:([8],'center',[]),26:([8],'center',[]),29:([8],'center',[])}
for n,(ids,cl,kicks) in head_specs.items():save('headline',n,group([headline(headtxt(n,i),cl,txt(n,kicks[j]) if kicks else '') for j,i in enumerate(ids)]),'6x2' if len(ids)==1 else '12x2')
pro_specs={3:([10],'lead'),4:([12,13,14,15,16,17,18,19],''),5:([21],''),6:([9,12,19,26],''),7:([11,12],''),11:([26],'quiet'),14:([9],''),25:([16,17],'quiet'),26:([11,17,23,29],'quiet'),29:([9],'quiet')}
for n,(ids,cl) in pro_specs.items():
 if n==4:body=group([prose(['<b>'+txt(n,i)+'</b>',txt(n,i+1)]) for i in [12,14,16,18]],'stack')
 elif n==6:body=group([prose([txt(n,i)]) for i in ids],'stack')
 elif n==26:body=group([prose([txt(n,i)],cl) for i in ids])
 else:body=prose([txt(n,i) for i in ids],cl)
 save('prose',n,body,'8x6' if n==4 else '6x3')
save('prose',3,prose([txt(3,11)],'quiet'),'6x2','-quiet')
# Capsule count and wording lengths follow the page, without page furniture.
for n,ids,classes,stack in [(6,[14,16,21,23,28,30],['on']*6,True),(11,[21],['on'],False),(17,[10,12,14],['on','quiet',''],True),(24,[9],['on'],False),(28,[28,30,42,44],['','','on','on'],False)]:
 xs=[pill(txt(n,i),cl) for i,cl in zip(ids,classes)];save('pill',n,group(xs,'stack' if stack else 'group'),'4x4' if stack else '6x2')
save('pill',25,pill(txt(25,9),'on'),'3x1','-caption')
save('list',8,lst([(txt(8,i),txt(8,i+1)) for i in [15,20,25]],'num divided'),'6x5')
for n,ids in [(11,[13,19]),(13,[19,23,27]),(17,[21,34,47]),(28,[18,26,34,40])]:save('list',n,group([lst(bullets(n,i)) for i in ids],'group' if len(ids)>2 else 'stack'),'8x3')
save('list',25,lst([(txt(25,i),lst(bullets(25,i+1))) for i in [20,24,28,32]],'divided'),'5x6')
# Source 17 panels share the same independent trend leaf; all nine point members remain.
line_values=[[20,35,61],[25,65,80],[30,36,69]]
def line(v):return root('chart-line','lines',''.join(f'<div class="pt" style="--v:{x}"><b>{x}</b><span>{j+2}Q</span></div>' for j,x in enumerate(v)),'--max:100')
save('chart-line',17,group([line(v) for v in line_values]),'9x3')
# Add the plot as an independent child of each project panel.
cs=[]
for i,v in zip([15,28,41],line_values):
 panel=card(txt(17,i+4),lst(bullets(17,i+6)),kick=txt(17,i+3),cl='line on');panel=panel[:-12]+line(v)+panel[-12:];cs.append(panel)
save('card',17,group(cs),'12x5')
# Source-specific named suffixes keep independent units independent in the map.
f=P/'map.json';m=json.loads(f.read_text())
for p in m['pages']:
 for u in p['instances']:
  if u.get('page')==13 and u.get('leaf')=='card' and u.get('variant')=='line':u['fixture']='elements/card/fixtures/replica-13-line.html'
  if u.get('page')==25 and u.get('leaf')=='pill' and 'caption' in u.get('name','').lower():u['fixture']='elements/pill/fixtures/replica-25-caption.html'
  if u.get('page')==3 and u.get('leaf')=='prose' and u.get('variant')=='quiet':u['fixture']='elements/prose/fixtures/replica-03-quiet.html'
byid={u['id']:u for p in m['pages'] for u in p['instances']+p['furniture']};m['instances']=[byid.get(u['id'],u) for u in m['instances']];f.write_text(json.dumps(m,ensure_ascii=False,indent=2))
print('Source specimens for first mapped bases written')
