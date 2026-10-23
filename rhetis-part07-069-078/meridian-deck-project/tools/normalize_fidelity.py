from pathlib import Path
import re,json
P=Path(__file__).parent;C=P/"meridian-deck"
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
# Every measured gutter and corner is a reusable named kit length.
f=C/'kit/kit.json';kit=json.loads(f.read_text());vals={}
for path in C.rglob('*.css'):
 if path.name=='tokens.css':continue
 s=path.read_text()
 def spacing(m):
  prop,v=m[1],m[2]
  def length(n):
   val=n[0];key='--meridian-deck-space-'+re.sub('[^a-z0-9]','',val.replace('-','neg').replace('.','p'));vals[key]=val;kit['extensions'][key]='length';return 'var('+key+')'
  # Geometric circles and square corners are part of the shape, not kit rounding.
  if prop=='border-radius' and re.fullmatch(r'(?:0|50%|100%|999px)(?:[ /]+(?:0|50%|100%|999px))*',v):return m[0]
  return prop+':'+re.sub(r'(?<![\w-])-?(?:\d*\.)?\d+(?:px|rem|em|%)',length,v)
 s=re.sub(r'(?<![-\w])((?:margin|padding)(?:-[a-z]+)?|gap|row-gap|column-gap|border-radius):([^;}]+)',spacing,s);path.write_text(s)
f.write_text(json.dumps(kit,ensure_ascii=False,indent=2))
f=C/'kit/css/tokens.css';f.write_text(f.read_text()+'\n.slide{'+''.join(k+':'+v+';' for k,v in vals.items())+'}\n')
print('Registered measured spacing',len(vals))
