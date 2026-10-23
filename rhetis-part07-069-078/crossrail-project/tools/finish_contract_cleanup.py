from pathlib import Path
import re,json
P=Path(__file__).parent;C=P/'crossrail'; E=C/'elements'
# Palette-independent token expressions retain the measured source geometry.
f=C/'foundation/foundation.css';h=f.read_text().replace('letter-spacing:0','letter-spacing:var(--label-track)').replace('padding-left:1px','padding-left:calc(var(--gap-sm)/12)').replace('line-height:1.25','line-height:var(--crossrail-title-stack-line)').replace('line-height:1.34','line-height:var(--title-line)');f.write_text(h)
repls={'hub':{'border-radius:194px 194px 0 0':'border-radius:calc(var(--gap-lg)*4.85) calc(var(--gap-lg)*4.85) 0 0'},'pill':{'margin-left:146px':'margin-left:calc(var(--gap-lg)*3.65)'},'steps':{'margin-top:calc(var(--gap) - 1px)':'margin-top:calc(var(--gap) - var(--gap-sm)/12)','gap:35px':'gap:calc(var(--gap-lg)*.875)','padding:18px':'padding:calc(var(--gap-sm)*1.5)','padding-top:calc(var(--gap) - .5px)':'padding-top:calc(var(--gap) - var(--gap-sm)/24)'},'image-frame':{'padding:7px':'padding:calc(var(--gap-sm)*7/12)'},'agenda':{'letter-spacing:0':'letter-spacing:var(--label-track)'}}
for el,rs in repls.items():
 f=E/el/'element.css';h=f.read_text()
 for a,b in rs.items():h=h.replace(a,b)
 f.write_text(h)
# Font sizes are discrete type steps; chart geometry variables must never become typography.
f=E/'chart-donut/element.css';h=f.read_text().replace('font-size:var(--crossrail-donut-value-size)','font-size:var(--type-52)').replace('font-size:var(--crossrail-donut-name-size)','font-size:var(--type-18)');h+='\n[data-el="crossrail-chart-donut"].donut:not(:has(.fig small)) .fig{font-size:var(--type-18)}[data-el="crossrail-chart-donut"].donut .name:has(small){font-size:var(--type-26)}@container(max-width:350px){[data-el="crossrail-chart-donut"].donut:has(.fig small) .fig{font-size:var(--type-36)}}@container(max-width:240px){[data-el="crossrail-chart-donut"].donut:has(.fig small) .fig{font-size:var(--type-28)}}\n';f.write_text(h)
# Remove obsolete style controls from both the source annotations and fixture charts.
for folder in [P/'reassembled',E/'chart-donut/fixtures']:
 for f in folder.glob('*.html'):
  h=re.sub(r'--crossrail-donut-(?:value|name)-size:[^;\"]+;?','',f.read_text())
  # An inherited custom-property alias resolves on its declaring ancestor; explicit source endpoints are chart data.
  for v in ['-53px','-65px']:
   h=h.replace('--crossrail-donut-line-x:'+v+';','--crossrail-donut-line-x:'+v+';--crossrail-donut-leg-x:'+v+';')
  f.write_text(h)
f=E/'chart-donut/element.json';j=json.loads(f.read_text());[j.get('tokenDefaults',{}).pop('--crossrail-donut-'+v+'-size',None) for v in ['value','name']];f.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
# Default variables may be consumed by both the official preview and the external source theme.
allvars={}
for f in E.glob('*/element.json'):allvars.update(json.loads(f.read_text()).get('tokenDefaults',{}))
(P/'assets/source-defaults.css').write_text('.slide{'+''.join(k+':'+str(v)+';' for k,v in sorted(allvars.items()))+'}\n')
