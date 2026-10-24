from pathlib import Path
import json
P=Path(__file__).parent;m=json.loads((P/'map.json').read_text())
for ident,why,markup in [('p05-furniture-source-2','The source has a right accent field behind three panels whose top edge begins beside the title. The normal head/body and one sidebar base cannot reserve this independent header-overlap composition without a new layout contract.','<div class="page side-heading"><header class="head">…</header><div class="body">…</div><div class="field"></div></div>'),('p30-furniture-source-2','The closing page combines a 45.4% left cover lockup with a five-row contact table in an independently aligned right field. A cover has no body grid, and the supplied normal-page sidebar has one base geometry.','<section class="slide contact-cover"><div class="page"><div class="lockup at-bottom-left">…</div><div class="body">contact table</div></div></section>')]:
 o=next(x for x in m['instances'] if x['id']==ident);o['use']='unexpressible';o['why']=why;o['requiredMarkup']=markup
orig=next(x for x in m['instances'] if x['id']=='p19-training-impact')
arrow=[r for r in orig['sourceMeasurements'] if not r['text'] and r['bbox'][2]<80 and r['bbox'][1]<330]
if arrow:
 o={'id':'p19-header-direction-arrow','page':19,'leaf':'versus','use':'unexpressible','bbox':[610,269,54,47],'fixture':None,'sourceMeasurements':arrow,'why':'The source connector joins two independent header bands. versus provides a central VS mark, not a directional header connector.','requiredMarkup':'<div class="comparison"><div class="head from">…</div><div class="connector" aria-hidden="true"></div><div class="head to">…</div><div class="sides">…</div></div>'}
 for r in arrow:r['owner']=o['id'];orig['sourceMeasurements'].remove(r)
 m['instances'].append(o)
# Move the two band surfaces to the independent contracted heading owners.
for i in [1,2]:
 dest=next(x for x in m['instances'] if x['id']==f'p19-comparison-head-{i}');x0=95+573*(i-1)
 surfaces=[r for r in orig['sourceMeasurements'] if not r['text'] and abs(r['bbox'][0]-x0)<2 and abs(r['bbox'][1]-260)<2]
 for r in surfaces:r['owner']=dest['id'];dest['sourceMeasurements'].append(r);orig['sourceMeasurements'].remove(r)
for o in m['instances']:
 if o['use']!='unexpressible' or 'requiredMarkup' in o:continue
 ident=o['id'];leaf=o['leaf']
 if 'pie' in ident:o['requiredMarkup']='<div class="pie" style="--max:100"><div class="seg" style="--v:N"><b class="fig">N%</b><span class="name">segment</span></div>…<div class="core">…</div><div class="leader">…</div></div>'
 elif 'numeric-axis' in ident:o['requiredMarkup']='<div class="chart"><div class="axis-y"><span style="--at:N">N</span>…</div><div class="plot">existing data parts</div></div>'
 elif 'highlighted-row' in ident:o['requiredMarkup']='<table class="table"><tbody><tr class="pick-row"><th scope="row">…</th><td>…</td>…</tr></tbody></table>'
 elif 'heading-band' in ident:o['requiredMarkup']='<div class="headline quiet"><h2>…</h2></div> (new quiet ruled-strip variant)'
 elif 'reverse' in ident:o['requiredMarkup']='<div class="steps reverse"><div class="step"><b class="mark">…</b><b class="name">…</b><p class="note">…</p></div>…</div>'
 elif 'hub' in ident or 'pentagon' in ident:o['requiredMarkup']='<div class="hub icon-orbit"><div class="core">…</div><div class="spoke"><span class="icon" data-icon="…"></span></div>…</div> (icon-only spokes and explicit orbit geometry)'
 elif 'calendar' in ident:o['requiredMarkup']='<div class="calendar"><div class="weekdays">…</div><div class="dates"><div class="date" style="--day:N">N</div>…<div class="range" style="--from:N;--to:N">event</div></div></div>'
 elif 'pill' in ident:o['requiredMarkup']='<div class="pill two-line"><div class="parts"><b class="fig">date</b><p class="name">event</p></div></div>'
 elif 'annotated' in ident:o['requiredMarkup']='<div class="bars annotated"><div class="axis-y">…</div><div class="plot"><div class="bar" style="--v:N">…</div>…</div><div class="captions"><div class="caption"><b class="fig">N</b><b class="name">…</b><p class="note">…</p></div>…</div></div>'
 elif 'underlay' in ident:o['requiredMarkup']='<div class="roadmap"><div class="lane"><b class="name">…</b><div class="range" style="--from:N;--to:N"></div><div class="bar" style="--from:N;--to:N">…</div></div>…</div>'
 elif 'background' in ident:o['requiredMarkup']='<div class="lines mixed"><div class="bands"><div class="band" style="--at:N;--v:N"></div>…</div><div class="pt" style="--v:N">…</div>…</div>'
 elif 'arrow' in ident:o['requiredMarkup']='<div class="posmap"><div class="trajectory" style="--from-x:N;--from-y:N;--to-x:N;--to-y:N"></div>existing marks</div>'
 else:o['requiredMarkup']='An explicit named contract part is required for this visual role; no supplied part has this meaning. See why and sourceMeasurements for the exact omitted shape.'
(P/'map.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
lines=['# Crossrail v2 contract gaps','','These are explicit limits, not claims of successful source reproduction. Proposed markup below is documentation only; unsupported classes were not added to collection CSS or assembly HTML. Normal table data remain visible even when row paint is unsupported.','']
for o in m['instances']:
 if o['use']!='unexpressible':continue
 lines+=['## '+o['id'],f'Page {o["page"]}; source bbox `{o["bbox"]}`; closest leaf `{o["leaf"]}`.',o['why'],'Required additional contract:', '```html',o['requiredMarkup'],'```','']
lines+=['## Grid quantization','The body is a 12×6 integral grid, x95/y263, 1090×393. Source rectangles may be smaller than one cell or begin between its lines. `assembly-placement.json` records the chosen spans; no per-page numeric geometry variables or element CSS keyed to those spans are used. Source03/04 use back seats, source09/13/17/21 use the accent-page foundation, source15 uses a horizontal rail, and source25 uses the at-left cover furniture.','', '## Intentional limits of partial assembly','Unsupported pie, calendar, icon-only orbit and reverse-stage regions are empty in the assembly and identified here. They were not replaced by unrelated bars, labels or multiple overlapping one-share donuts. This review therefore distinguishes a complete 56-element collection from full-fidelity expressibility of all 30 source pages.','']
(P/'GAPS.md').write_text('\n'.join(lines)+'\n');print('map',len(m['instances']),'gaps',sum(o['use']=='unexpressible' for o in m['instances']))
