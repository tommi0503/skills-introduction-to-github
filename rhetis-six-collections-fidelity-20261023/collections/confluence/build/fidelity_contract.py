from pathlib import Path
import re,json,shutil
D=Path('/workspace/work/deliverables/confluence');C=D/'collection/confluence';R=D/'review'
p=C/'foundation/foundation.css';s=p.read_text();s+='\n/* Fidelity typography adjustments */\n.rail .lead{font-size:var(--type-12)}.rail .kicker{font-size:var(--type-10)}\n';p.write_text(s)
p=C/'elements/hub/element.css';s=p.read_text();s+='''\n@container(min-width:1000px){.hub[data-el="confluence-hub"] .core .kick{font-size:var(--type-10)}.hub[data-el="confluence-hub"] .mark .icon[data-icon="arrow-big-up"] svg,.hub[data-el="confluence-hub"] .mark .icon[data-icon="arrow-big-down"] svg{position:absolute;left:-19px;top:0;width:76px;height:76px}.hub[data-el="confluence-hub"] .mark .icon[data-icon="arrow-big-up"],.hub[data-el="confluence-hub"] .mark .icon[data-icon="arrow-big-down"]{overflow:hidden}.hub[data-el="confluence-hub"] .mark .icon[data-icon="mail"]{top:10px!important;height:76px!important}.hub[data-el="confluence-hub"] .mark .icon[data-icon="file-text"]{left:0!important;width:76px!important;height:76px!important}}\n'''
# Avoid baseline-only SVG overflow; fonts still use an allowed size token.
s=s.replace('font-size:0;line-height:0','font-size:var(--type-8);line-height:0')
p.write_text(s)
# Move typography, radii and spacing to declared typed shared kit extensions.
ext={};defs={}
def token(prop,val):
 typ='weight' if prop=='font-weight' else 'number' if prop=='line-height' else 'tracking' if prop=='letter-spacing' else 'length'
 suffix=re.sub(r'[^a-z0-9]+','-',val.lower()).strip('-') or 'zero'
 key='--confluence-'+prop+'-'+suffix
 if val=='0' and typ=='length':val='0px'
 ext[key]=typ;defs[key]=val
 return 'var('+key+')'
for p in [C/'foundation/foundation.css',C/'elements/card/element.css',C/'elements/agenda/element.css',C/'elements/hub/element.css']:
 s=p.read_text()
 for n,m in [(9,8),(13,14),(15,14)]:s=s.replace(f'var(--type-{n})',f'var(--type-{m})')
 # Only post-fidelity rules had new literals; earlier original library is already tokenized.
 if '/* fidelity-v2 */' in s:head,tail=s.split('/* fidelity-v2 */',1);mark='/* fidelity-v2 */'
 elif '/* fidelity-complete */' in s:head,tail=s.split('/* fidelity-complete */',1);mark='/* fidelity-complete */'
 else:head,tail,mark=s,'',''
 def repl(m):
  prop,val=m.group(1),m.group(2).strip()
  if 'var(' in val or val in ['inherit','normal','auto'] or prop=='letter-spacing' and val=='normal':return m.group(0)
  # Space shorthand made of literal lengths/zero gets one shared token.
  if re.fullmatch(r'[-.0-9]+(?:px|em|%)?(?:\s+[-.0-9]+(?:px|em|%)?)*',val):return prop+':'+token(prop,val)
  return m.group(0)
 tail=re.sub(r'(font-weight|line-height|letter-spacing|border-radius|padding(?:-top|-right|-bottom|-left)?|margin(?:-top|-right|-bottom|-left)?|gap|row-gap|column-gap):([^;}]+)',repl,tail)
 p.write_text(head+mark+tail)
# Existing named fidelity extensions also have explicit typed entries.
more={'--confluence-column-gap':'length','--confluence-row-gap':'length','--confluence-agenda-gap':'length','--confluence-agenda-column':'length','--confluence-card-inset':'length','--confluence-caption-line':'number','--confluence-cover-line':'number','--confluence-caption-track':'tracking','--confluence-rail-copy':'length','--confluence-hero-track':'tracking','--confluence-goal-track':'tracking','--confluence-cover-copy-track':'tracking'}
ext.update(more)
p=C/'kit/kit.json';j=json.loads(p.read_text());j['extensions'].update(ext);p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
p=C/'kit/css/tokens.css';s=p.read_text().split('/* fidelity typed extensions */')[0];s+='\n/* fidelity typed extensions */\n.slide{'+''.join(k+':'+v+';' for k,v in defs.items())+'}\n';p.write_text(s)
for p in C.rglob('*.css'):
 out=R/'assets/collection'/p.relative_to(C);out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out)
