from pathlib import Path
import json,re
P=Path(__file__).parent;C=P/'meridian-deck'
f=C/'foundation/foundation.css';s=f.read_text()+'''\n.slide .top{position:absolute;left:var(--margin-x);top:var(--margin-y);margin:0;font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line);color:var(--a1-7)}.slide .page::after{background:var(--a1)}.slide .deco{container-type:size;isolation:isolate}.slide .deco>.icon{position:absolute;left:3%;top:-55%;display:flex;align-items:center;justify-content:center;width:min(11cqw,62cqh);height:min(11cqw,62cqh);border-radius:999px;background:var(--a1);color:var(--a1-on)}.slide .deco>.icon:nth-child(2){left:30%;top:28%;width:min(6.2cqw,36cqh);height:min(6.2cqw,36cqh)}.slide .deco>.icon:nth-child(3){left:auto;right:8%;top:7%;width:min(6.6cqw,39cqh);height:min(6.6cqw,39cqh)}.slide .deco>.icon>svg{width:54%;height:54%}.slide .page>.seat.back.avatar{left:53.4%;top:0;width:46.6%;height:84.4%;background:none;border-radius:0;isolation:isolate;z-index:0}.slide .page>.seat.back.avatar::before{content:"";position:absolute;left:28%;top:-13%;width:97%;aspect-ratio:1;border-radius:999px;background:var(--n-2)}.slide .page>.seat.back.avatar::after{content:"";position:absolute;left:0;bottom:0;width:56.4%;aspect-ratio:1;border-radius:999px;background:var(--n-2)}.slide.on .page>.seat.back{left:0;top:0;width:100%;height:100%;border-radius:0;background:var(--n-2);isolation:isolate}.slide.on .page>.seat.back::before{content:"";position:absolute;inset:0;background:var(--a1);clip-path:polygon(0 0,50.55% 0,71.02% 100%,0 100%)}\n''';f.write_text(s)
f=C/'kit/css/tokens.css';s=f.read_text().replace('--title-weight:650','--title-weight:700').replace('--weight-display:650','--weight-display:700');f.write_text(s)
# Palette provider is the only source-colour input and contains no geometry or page-specific selectors.
colors={'--page':'#ffffff','--ink':'#222222','--a1':'#0063ed','--a1-on':'#ffffff','--a1-7':'#0063ed','--a1-1-soft':'#deefff','--a1-2-soft':'#b9defc','--a1-3-soft':'#8bc3f5','--a1-1-muted':'#e5edfa','--a1-2-muted':'#cfe1fa','--a1-4-muted':'#78a6df','--n-1':'#f7f7f7','--n-2':'#e8e8e8','--n-3':'#dddddd','--n-4':'#cccccc','--n-5':'#aaaaaa','--n-6':'#999999','--n-7':'#5b5b5b','--n-8':'#222222','--n-9':'#111111'}
(P/'assets/source-palette.css').write_text('.slide{'+''.join(k+':'+v+';' for k,v in colors.items())+'}\n')
(P/'assets/source-defaults.css').write_text('/* No page-specific source geometry defaults are used. */\n')
# Graph marks remain round, while compact trees use the shared rectangular corner token.
f=C/'elements/hierarchy/element.css';s=f.read_text()+'''\n.org[data-el="meridian-deck-hierarchy"]:has(>.branch>.leaf)>.branch>.node,.org[data-el="meridian-deck-hierarchy"]:has(>.branch>.leaf)>.branch>.leaf{height:min(100%,17cqw);align-self:center}\n''';f.write_text(s)
f=C/'elements/headline/element.css';s=f.read_text()+'''\n@container(max-height:90px){.headline[data-el="meridian-deck-headline"]>h2{font-size:clamp(var(--type-14),4cqw,var(--type-32))}}\n''';f.write_text(s)
# Whole-canvas SVG viewboxes do not describe the chart's visible unit.
f=P/'map.json';m=json.loads(f.read_text())
for i in m['instances']:
 if i['id']=='p14-10':i['bbox']=[145,339.8,973,304.9];i['bounds']=dict(zip(['x','y','w','h'],i['bbox']));i['measurementNote']='The full-canvas SVG viewport is excluded; visible axes, path, numbers and 15 labels define this unit.'
b={i['id']:i for i in m['instances']}
for pg in m['pages']:
 for k in ['instances','furniture']:pg[k]=[b.get(i['id'],i) for i in pg[k]]
f.write_text(json.dumps(m,ensure_ascii=False,indent=2))
f=P/'GAPS.md';s=f.read_text().replace("{'x': 0, 'y': 0, 'w': 1280, 'h': 720}","{'x': 145, 'y': 339.8, 'w': 973, 'h': 304.9}");f.write_text(s)
