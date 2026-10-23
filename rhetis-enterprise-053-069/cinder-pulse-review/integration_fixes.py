from pathlib import Path
import json,re
B=Path(__file__).parent;C=B.parent/'cinder-pulse'
def add(n,s):
 p=C/f'elements/{n}/element.css';p.write_text(p.read_text()+'\n'+s)
# Review: reserve the overlap for core text; set copy stays in the outer lobe.
add('venn','.venn[data-el="cinder-pulse-venn"]:has(>.core)>.set{padding-left:calc(var(--pad)*.6);padding-right:calc(var(--pad)*1.4);}.venn[data-el="cinder-pulse-venn"]:has(>.core)>.set:nth-child(2){padding-left:calc(var(--pad)*1.4);padding-right:calc(var(--pad)*.6);}.venn[data-el="cinder-pulse-venn"]:has(>.core)>.set>:is(.name,.note){max-width:72%;}.venn[data-el="cinder-pulse-venn"]:has(>.core)>.set:first-child>:is(.name,.note){align-self:flex-start;text-align:center;}.venn[data-el="cinder-pulse-venn"]:has(>.core)>.set:nth-child(2)>:is(.name,.note){align-self:flex-end;text-align:center;}.venn[data-el="cinder-pulse-venn"]:has(>.set:nth-child(3)) .name{font-size:var(--type-20);}.venn[data-el="cinder-pulse-venn"]:has(>.set:nth-child(3)) .note{font-size:var(--type-14);}')
add('metric','.stats[data-el="cinder-pulse-metric"]{flex-wrap:wrap;}.stats[data-el="cinder-pulse-metric"]>.stat{flex:1 1 180px;height:auto;min-height:0;}')
add('waffle','.waffle[data-el="cinder-pulse-waffle"]{gap:var(--gap-sm);}.waffle[data-el="cinder-pulse-waffle"]>.units{flex:1;min-height:0;height:auto;}@container (max-height:220px){.waffle[data-el="cinder-pulse-waffle"] .fig{font-size:var(--type-28);}.waffle[data-el="cinder-pulse-waffle"] .name{font-size:var(--type-14);}}')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'\n.slide.cover .lockup.at-center~.deco{left:calc(var(--pad)*-1);right:auto;width:36%;}.slide.cover .lockup.at-center{max-width:58%;}.slide.cover .lockup.at-center~.meta{left:40%;}\n')
# Explicit safe minima from the all-size scan. Required fixture markup remains untouched.
audit=json.loads((B/'size-audit.json').read_text())[0]['fixtures'];changed=[]
for a in audit:
 if not a['failures']:continue
 label=a['label'];name,rest=label.split(' / ',1);stem=rest.split(' min ')[0].strip();p=C/f'elements/{name}/fixtures/{stem}.html'
 if not p.exists():continue
 if name in {'card','callout','chart-area','chart-bar','chart-donut','chart-line'}:continue
 fails=[tuple(map(int,f['size'].split('x'))) for f in a['failures']]
 candidates=[(w*h,w,h) for w in range(2,13) for h in range(1,7) if all(not(x>=w and y>=h) for x,y in fails)]
 _,w,h=min(candidates);s=p.read_text();s=re.sub(r'<!-- min:.*?--> ',f'<!-- min: {w}x{h} --> ',s,count=1);s=re.sub(r'^<!-- min:.*?-->\n',f'<!-- min: {w}x{h} -->\n',s,count=1);p.write_text(s);changed.append([name,stem,w,h])
(B/'minimum-adjustments.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2))
# Remove sample placeholder words only in non-required data fixtures.
for p in (C/'elements').glob('*/fixtures/*.html'):
 if p.parent.parent.name in {'card','callout','chart-area','chart-bar','chart-donut','chart-line'}:continue
 p.write_text(p.read_text().replace('TEXT HERE','신규 채널').replace('TEXT 기획','서비스 기획').replace('GRAPH DATA','운영 혁신').replace('Rhetis 권장','운영 검토'))
# Keep the process diagram labels short as in the original: details belong to the side cards.
p=B/'build_reassembled.py';s=p.read_text();s=s.replace("circ('cycle','고객 성공',process,pl(4,1,6,6))", "circ('cycle','고객 성공',[(a,'') for a,b in process],pl(4,1,6,6))")
s=s.replace("steps([(f'STEP {i+1}.',a,b) for i,(a,b) in enumerate(process[:3])],pl(1,1,3,6),'steps col')", "'<div class=\"group col\" style=\"'+pl(1,1,3,6)+'\">'+''.join(card(a,b,f'STEP {i+1}.') for i,(a,b) in enumerate(process[:3]))+'</div>'")
s=s.replace("steps([(f'STEP {i+4}.',a,b) for i,(a,b) in enumerate(process[3:])],pl(10,1,3,6),'steps col')", "'<div class=\"group col\" style=\"'+pl(10,1,3,6)+'\">'+''.join(card(a,b,f'STEP {i+4}.') for i,(a,b) in enumerate(process[3:]))+'</div>'")
# Partners have three parallel owners, not three rows of a single long list.
start="listing([('기술 파트너'";at=s.find(start)
if at!=-1:
 end=s.find("],pl(1,5,12,2),'divided')",at)
 if end!=-1:
  segment=s[at:end+len("],pl(1,5,12,2),'divided')")]
  data=segment[len('listing('):segment.index('],pl(1,5,12,2)')+1]
  s=s.replace(segment,"'<div class=\"group\" style=\"'+pl(1,5,12,2)+'\">'+''.join(listing([item]) for item in "+data+")+ '</div>'")
p.write_text(s)
print('integration fixes',len(changed),'fixture minima revised')
