from pathlib import Path
import re,json
P=Path(__file__).parent;C=P/'meridian-deck'
f=C/'foundation/foundation.css';t=f.read_text();a=t.find('.slide .body>.stack:has');t=t[:a] if a>=0 else t
# Foundation owns only its containers. Each element file owns its text and paint.
t+='''
.slide .body>.stack>.split{display:grid;grid-template-columns:70px minmax(0,1fr);column-gap:calc(var(--gap-lg) - var(--stroke)*5);height:167px;min-height:167px;align-items:start;border-bottom:var(--stroke) solid var(--n-7)}.slide .body>.stack>.split:last-child{border-bottom:0}.slide .body>.stack:has(>.split){gap:0;padding-left:calc(var(--top-h) + var(--stroke)*2);padding-right:calc(var(--top-h) + var(--stroke)*2)}.slide .body>.stack>.split>.split{display:grid;grid-template-columns:297px minmax(0,1fr);column-gap:calc(var(--top-h) + var(--gap-sm) - var(--stroke)*2);height:137px;align-items:start}.slide .body>.stack>.split>.split>.stack{gap:var(--gap-sm);padding-top:var(--gap-sm)}
.slide .split.wide-left{grid-template-columns:698px 429px;gap:calc(var(--gap) + var(--stroke)*3);translate:0 -12px}.slide .split.wide-left>.stack{gap:0}.slide .split.wide-left>.stack>.group{height:151px;min-height:151px;display:grid;grid-template-columns:330px 326px;gap:calc(var(--gap-sm) + var(--stroke)*2);padding-left:calc(var(--pad) + var(--stroke)*4);border-bottom:var(--stroke) solid var(--n-6)}.slide .split.wide-left>.stack>.group:last-child{border-bottom:0}.slide .split.wide-left>.stack>.group>.stack{gap:var(--gap-sm)}
'''
f.write_text(t)
def add(n,s):
 f=C/'elements'/n/'element.css';f.write_text(f.read_text()+'\n/* Scoped media composition behavior. */\n'+s+'\n')
h='[data-el="meridian-deck-headline"]';p='[data-el="meridian-deck-prose"]';fr='[data-el="meridian-deck-image-frame"]';li='[data-el="meridian-deck-list"]'
add('headline','.slide .body>.stack>.split>'+h+'.big{height:137px;border:0;padding:0;text-align:center;justify-content:center}.slide .body>.stack>.split>'+h+'.big h2{font-size:var(--type-44);color:var(--a1-7);font-weight:700;line-height:1.55}.slide .body>.stack>.split>.split>.stack>'+h+'{flex:0 0 auto;padding:0;border:0;justify-content:start}.slide .body>.stack>.split>.split>.stack>'+h+' h2{font-size:var(--type-18);line-height:1.55;font-weight:400}'+h+' h2 small{font-size:var(--type-12);font-weight:400;color:var(--n-7)}.slide .split.wide-left '+h+'{flex:none;height:30px;border:0;padding:0;justify-content:start}.slide .split.wide-left '+h+' h2{font-size:var(--type-20);line-height:1.55}')
add('image-frame','.slide .body>.stack>.split>.split>'+fr+'{height:137px;align-self:start;border:0;padding:0;background:var(--n-2)}.slide .body>.stack>.split>.split>'+fr+'::before{content:none}.slide .body>.stack>.split>.split>'+fr+'>.seat{width:100%;height:100%;max-width:100%;max-height:100%;aspect-ratio:auto}.slide .split.wide-left>'+fr+'{height:392px;align-self:start;border:0;padding:0;background:var(--n-2);translate:0 15px}.slide .split.wide-left>'+fr+'::before{content:none}.slide .split.wide-left>'+fr+'>.seat{width:100%;height:100%;aspect-ratio:auto;max-width:none;max-height:none}')
add('prose','.slide .body>.stack>.split>.split>.stack>'+p+'{padding:0;justify-content:start;height:auto;container-type:inline-size;overflow:visible}.slide .body>.stack>.split>.split>.stack>'+p+' p{font-size:var(--type-14);line-height:1.65;white-space:nowrap;color:var(--n-7)}.slide .split.wide-left '+p+'{padding:0;justify-content:start;container-type:inline-size}.slide .split.wide-left '+p+' p{font-size:var(--type-14);line-height:1.6;color:var(--n-7);white-space:nowrap}')
add('list','.slide .split.wide-left '+li+'{padding:var(--gap-sm) 0;justify-content:start;gap:calc(var(--gap-sm) - var(--stroke)*2)}.slide .split.wide-left '+li+' .item{height:41px;background:var(--n-1);display:flex;align-items:center;padding-left:var(--pad)}.slide .split.wide-left '+li+' .item::before{top:19px;left:26px;background:var(--n-7);width:5px;height:5px}.slide .split.wide-left '+li+' .name{font-size:var(--type-14);font-weight:400;padding-left:var(--gap-sm);color:var(--n-7);line-height:1.55}')
# Register source typography as reusable non-colour kit values.
f=C/'kit/kit.json';kit=json.loads(f.read_text());vals={}
for css in C.rglob('*.css'):
 if css.name=='tokens.css':continue
 text=css.read_text()
 def repl(m):
  prop,v=m[1],m[2]
  if 'var(' in v or v in ['normal','inherit']:return m[0]
  typ={'font-weight':'weight','line-height':'line','letter-spacing':'tracking'}[prop];key='--meridian-deck-'+prop+'-'+re.sub('[^a-z0-9]','',v.replace('-','neg').replace('.','p'))
  vals[key]=v;kit['extensions'][key]=typ
  return prop+':var('+key+')'
 text=re.sub(r'(font-weight|line-height|letter-spacing):([^;}]+)',repl,text);css.write_text(text)
f.write_text(json.dumps(kit,ensure_ascii=False,indent=2))
f=C/'kit/css/tokens.css';f.write_text(f.read_text()+'\n.slide{'+''.join(k+':'+v+';' for k,v in vals.items())+'}\n')
print('Scoped composition CSS, registered typography',len(vals))
