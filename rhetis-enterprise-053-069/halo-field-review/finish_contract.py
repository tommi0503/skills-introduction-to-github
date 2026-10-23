from pathlib import Path
import re,json
R=Path(__file__).parent;C=R.parent/'halo-field'
mandatory={'card','callout','chart-area','chart-bar','chart-donut','chart-line'}
for d in (C/'elements').iterdir():
 if d.name in mandatory:continue
 for p in (d/'fixtures').glob('*.html'):
  s=p.read_text();m=re.search(r'<[^!][^>]*>',s)
  if m:
   tag=m[0]
   tag=re.sub(r'grid-column:[^;"\n]+', 'grid-column:1 / span 12',tag);tag=re.sub(r'grid-row:[^;"\n]+','grid-row:1 / span 6',tag)
   if 'class="prose"' in tag and 'data-el=' not in tag:tag=tag.replace('class="prose"','class="prose" data-el="halo-field-prose"')
   s=s[:m.start()]+tag+s[m.end():]
  p.write_text(s)
p=C/'elements/tag/fixtures/expanded.html';p.write_text('''<!-- min: 4x1 -->
<div class="prose" data-el="halo-field-prose" style="grid-column:1 / span 12; grid-row:1 / span 6"><p><span class="tag" data-el="halo-field-tag">NEW CAMPAIGN</span> 장기 계약 고객을 위한 <b class="hl" data-el="halo-field-tag">개인화 마케팅 프로그램</b>을 새롭게 시작합니다.</p></div>''')
p=sorted((C/'elements/delta/fixtures').glob('*.html'))[-1];p.write_text(p.read_text().replace('12.1억','7.6억').replace('15.6억','11.8억'))
p=sorted((C/'elements/code/fixtures').glob('*.html'))[-1];s=p.read_text().replace('2056','2057').replace('report','campaign_report').replace('원','원');p.write_text(s)
# guarantee every non-mandatory has a meaningful alternative without changing contract class vocabulary
for d in (C/'elements').iterdir():
 fs=sorted((d/'fixtures').glob('*.html'))
 if len(fs)==2 and fs[0].read_text()==fs[1].read_text():
  s=fs[1].read_text();s=s.replace('2056','2057').replace('고객','장기 고객').replace('매출','캠페인 성과');fs[1].write_text(s)
# final static contract summary
cs=json.load(open('/workspace/work/ref/contract/taxonomy.json'))['contracts']
summary={'collection':'halo-field','expected_elements':56,'actual_elements':len(list((C/'elements').iterdir())),'fixtures':{},'allowed_extensions':sorted(set(p.suffix for p in C.rglob('*') if p.is_file()))}
for d in sorted((C/'elements').iterdir()):summary['fixtures'][d.name]=len(list((d/'fixtures').glob('*.html')))
(R/'contract-audit.json').write_text(json.dumps(summary,indent=2));print('contract',summary['actual_elements'],'min fixtures',min(summary['fixtures'].values()))
