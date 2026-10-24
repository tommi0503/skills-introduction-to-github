from pathlib import Path
from lxml import html
import json
P=Path(__file__).parent;E=P/'crossrail/elements'
p=E/'funnel/element.css';s=p.read_text();s+='''\n.funnel[data-el="crossrail-funnel"]>.stage{gap:0}.funnel[data-el="crossrail-funnel"]>.stage>.name,.funnel[data-el="crossrail-funnel"]>.stage>.fig{box-sizing:border-box;display:flex;align-items:center;justify-content:center;min-height:16.6cqh;line-height:var(--name-line);border:1px solid var(--n-4)}.funnel[data-el="crossrail-funnel"]>.stage>.name{border-right:0;border-radius:999px 0 0 999px;padding:calc(var(--gap-sm)/2) calc(var(--gap-sm)/2) calc(var(--gap-sm)/2) calc(var(--gap)*1.75)}.funnel[data-el="crossrail-funnel"]>.stage>.fig{border-left:0;border-radius:0 999px 999px 0;padding:calc(var(--gap-sm)/2) calc(var(--gap)*1.75) calc(var(--gap-sm)/2) calc(var(--gap-sm)/2)}.funnel[data-el="crossrail-funnel"]>.stage:last-child>.name,.funnel[data-el="crossrail-funnel"]>.stage:last-child>.fig{background:var(--a1-7);border-color:var(--a1-7);color:var(--page)}
''';p.write_text(s)
# Alignment is a semantic markup correction: on sets fill; center remains an independent explicit variant.
for p in list((E/'headline/fixtures').glob('replica-19-*.html'))+[P/'reassembled/slide_19.html']:
 d=html.fromstring(p.read_text());ss=d.xpath('//*[@data-el="crossrail-headline" and contains(concat(" ",normalize-space(@class)," ")," on ")]')
 if d.get('data-el')=='crossrail-headline' and 'on' in d.get('class','').split():ss=[d]
 for a in ss:a.set('class',' '.join(c for c in a.get('class').split() if c!='center'))
 p.write_text(('<!-- min:6x1 -->\n' if 'fixtures' in str(p) else '<!doctype html>')+html.tostring(d,encoding='unicode')+'\n')
p=E/'tag/element.css';p.write_text('''/* Fresh Crossrail design. Source measurements: ../../../../source-measurements.json; map ownership: ../../../../map.json. */
.tag[data-el="crossrail-tag"],.hl[data-el="crossrail-tag"]{box-sizing:border-box;container-type:size;position:relative;min-width:0;min-height:0;display:flex;align-items:center;justify-content:center;color:var(--ink);font-family:var(--font-body);font-size:var(--type-18);font-weight:var(--label-weight);line-height:var(--label-line)}.tag[data-el="crossrail-tag"]>span{display:inline-flex;align-items:center;justify-content:center;min-width:42px;min-height:42px;max-width:100%;box-sizing:border-box;padding:calc(var(--gap-sm)/2) var(--gap-sm);border:0;border-radius:999px;background:var(--a1-7);color:var(--page);font-size:var(--type-20);font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track);text-align:center;overflow-wrap:anywhere}.hl[data-el="crossrail-tag"]{display:inline-flex;align-items:center;justify-content:center;color:var(--ink);font-size:var(--type-18);font-weight:var(--name-weight);line-height:var(--body-line);background:none}.hl[data-el="crossrail-tag"]>span{background:linear-gradient(transparent 60%,var(--a1-2-soft) 0)}
''')
p=E/'legend/element.css';s=p.read_text().replace('flex:none;border-radius:50%;background:var(--a1-7)','flex:none;border-radius:0;background:var(--a1-7)');p.write_text(s)
p=E/'list/element.css';s=p.read_text();s+='''\n.list[data-el="crossrail-list"].divided .item{grid-template-columns:minmax(0,1fr)}.list[data-el="crossrail-list"].divided .item::before{display:none}.list[data-el="crossrail-list"].divided .name,.list[data-el="crossrail-list"].divided .note{grid-column:1}.list[data-el="crossrail-list"].divided .name{font-weight:var(--name-weight)}.list[data-el="crossrail-list"].divided .item:has(>.mark){grid-template-columns:var(--type-20) minmax(0,1fr)}.list[data-el="crossrail-list"].divided .item:has(>.mark)>.name,.list[data-el="crossrail-list"].divided .item:has(>.mark)>.note{grid-column:2}
''';p.write_text(s)
p=E/'pyramid/element.css';s=p.read_text().replace('align-items:center;gap:2px;--crossrail-levels','align-items:center;gap:calc(var(--gap-sm)*.75);--crossrail-levels');p.write_text(s)
M=json.loads((P/'map.json').read_text())
for i in M['instances']:
 if i['leaf']=='tag' and i.get('fixture'):i['design']='42×42px minimum filled navy-role circular badge with a centred white20px single character; a longer label expands naturally inside the same rounded surface. '+i['design']
 if i['id'] in ['p19-comparison-head-1','p19-comparison-head-2']:i['design']='Filled horizontal emphasis band with left-aligned title. Explicit center was removed after checking actual source computed style; malformed source text-align declaration resolves to start. '+i['design']
(P/'map.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n')
(E/'card/description.md').write_text('A broad panel aligns a prominent figure or circular mark against a title, with a fine rule and supporting note. Quiet columns reserve an upper pause for their kicker. Line cards expose open accent rules and a secondary note without an enclosing box.\n')
(E/'tag/description.md').write_text('A filled circular badge has a42px minimum and a centred single-character label. Longer labels expand naturally into the same rounded capsule. Inline highlights retain a quiet underline surface.\n')
print('six mapped parts corrected; headline change is markup only')
