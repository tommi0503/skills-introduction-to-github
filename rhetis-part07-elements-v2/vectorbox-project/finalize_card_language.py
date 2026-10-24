from pathlib import Path
import json
P=Path(__file__).parent;p=P/'write_elements_v2.py';s=p.read_text()
s=s.replace('align-items:center;justify-content:center;width:100%}R .note','align-items:flex-start;justify-content:center;width:100%}R .note')
s=s.replace('height:min(59.7cqw,35.7cqh);margin-bottom:var(--gap-sm)', 'height:min(59.7cqw,35.7cqh);margin-bottom:var(--gap)')
s=s.replace('R.quiet .name{font-size:clamp(var(--type-16),10cqw,var(--type-26));min-height:1lh;', 'R.quiet .name{font-size:clamp(var(--type-16),10cqw,var(--type-26));min-height:2lh;')
s=s.replace('R.quiet .note{min-height:2lh}', 'R.quiet .note{min-height:4lh}')
s=s.replace('font-weight:var(--body-weight);min-height:0;margin:0}R.line:has(.kick)', 'font-weight:var(--body-weight);min-height:0;margin:0;color:var(--ink)}R.line:has(.kick)')
needle="styles['agenda']=";a=s.index(needle);extra="""styles['card']=(styles['card'][0],styles['card'][1]+'''R.tone-2 .mark{color:var(--a2)}R.tone-3 .mark{color:var(--a3)}R.tone-4 .mark{color:var(--a4)}R.line.tone-1 .mark{border-color:var(--a1-4-soft)}R.line.tone-1 .mark:before{background:TONECORNERS}R.on.tone-2 .parts>.fig:only-child{background:var(--a2);color:var(--a2-on)}R.on.tone-3 .parts>.fig:only-child{background:var(--a3);color:var(--a3-on)}R.on.tone-4 .parts>.fig:only-child{background:var(--a4);color:var(--a4-on)}'''.replace('TONECORNERS',','.join(f'linear-gradient(var(--a1),var(--a1)) {x} {y}/7px 7px no-repeat' for x,y in [('0','0'),('100%','0'),('0','100%'),('100%','100%')])))
""";s=s[:a]+extra+s[a:]
s=s.replace(" for leaf,(origin,body) in styles.items():emit(leaf,origin,body)\n print('Fresh CSS authored:',len(styles))", " import sys\n selected=sys.argv[1:] or list(styles)\n for leaf in selected:\n  origin,body=styles[leaf];emit(leaf,origin,body)\n print('Fresh CSS authored:',','.join(selected))")
p.write_text(s)
f=P/'vectorbox/elements/card/fixtures/replica-04-on.html';(f.parent/'replica-04-tone-2.html').write_text(f.read_text().replace('card on','card on tone-2').replace('78<small>','64<small>'))
f=P/'vectorbox/elements/card/fixtures/replica-04-line.html';f.write_text(f.read_text().replace('card line','card line tone-1'))
p=P/'map.json';d=json.loads(p.read_text())
for i in d['instances']:
 if i['id']=='04-burst-2':i.update(use='variant:.tone-2',variant='.tone-2',fixture='elements/card/fixtures/replica-04-tone-2.html')
 if i['id']=='04-caption-1':i.update(use='variant:.tone-1',variant='.tone-1')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
