from pathlib import Path
import json
P=Path(__file__).parent;E=P/'crossrail/elements'
# A shared mathematical formatter uses only built-in decimal-leading-zero counters.
# If all thirds are integral, before shows integers. Otherwise after shows two decimals.
def rail(root,top,bottom,width):
 names=[];fraction=[]
 for rank,expr in [(3,'var(--max)'),(2,'calc(var(--max)*2/3)'),(1,'calc(var(--max)/3)'),(0,'0')]:
  names += [f'crossrail-y{rank} {expr}']
  rounded=f'round({expr}*100,1)'
  fraction += [f'crossrail-yi{rank} round(down,{rounded}/100,1)',f'crossrail-yf{rank} mod({rounded},100)']
 ints=' "\\a" '.join(f'counter(crossrail-y{rank})' for rank in [3,2,1,0])
 dec=' "\\a" '.join(f'counter(crossrail-yi{rank}) "." counter(crossrail-yf{rank},decimal-leading-zero)' for rank in [3,2,1,0])
 selector=root+'::before,'+root+'::after'
 return f'''\n{selector}{{position:absolute;left:calc(var(--gap-sm)/2);top:calc({top} - 100cqh/6);bottom:auto;width:{width};height:calc(100cqh*4/3);background:none;white-space:pre;text-align:right;font-family:var(--font-body);font-size:var(--type-14);font-weight:var(--body-weight);line-height:calc(100cqh/3);letter-spacing:var(--figure-track);font-variant-numeric:tabular-nums;color:var(--ink);pointer-events:none}}
{root}::before{{counter-set:{' '.join(names)};content:{ints};opacity:calc(1 - min(1,abs(mod(var(--max),3))*1000000000))}}
{root}::after{{counter-set:{' '.join(fraction)};content:{dec};opacity:min(1,abs(mod(var(--max),3))*1000000000)}}
@container(max-height:180px){{{selector}{{display:none}}}}
'''
b='.bars[data-el="crossrail-chart-bar"]';p=E/'chart-bar/element.css';s=p.read_text();s+='''\n.bars[data-el="crossrail-chart-bar"]{padding-left:calc(var(--pad)*2);background-color:var(--n-1);background-image:repeating-linear-gradient(to top,var(--n-3) 0 1px,transparent 1px 33.333333%);background-size:calc(100% - var(--pad)*3) calc(100% - var(--pad)*2 - var(--gap-lg)*1.5);background-position:left calc(var(--pad)*2) bottom calc(var(--gap-lg)*1.5);background-repeat:no-repeat}.bars[data-el="crossrail-chart-bar"].h{background-image:repeating-linear-gradient(to right,var(--n-3) 0 1px,transparent 1px 25%);background-size:calc(100% - var(--gap-lg)*5) calc(100% - var(--pad)*2);background-position:left calc(var(--gap-lg)*3) bottom var(--pad)}
'''+rail(b,'calc(var(--pad)*2)','calc(var(--gap-lg)*1.5)','calc(var(--pad)*2 - var(--gap-sm))')+f'\n{b}.h::before,{b}.h::after{{content:none;display:none}}\n';p.write_text(s)
l='.lines[data-el="crossrail-chart-line"]';p=E/'chart-line/element.css';s=p.read_text();s+=f'\n{l}{{padding-left:calc(var(--pad)*2 + var(--gap-sm))}}\n'+rail(l,'var(--gap-lg)','calc(var(--gap-lg) + var(--gap-sm)/4)','calc(var(--pad)*2 - var(--gap-sm))');p.write_text(s)
M=json.loads((P/'map.json').read_text())
for source,target in [('p20-numeric-axis','p20-quarter-bars'),('p22-numeric-axis','p22-weekly-line')]:
 old=next(i for i in M['instances'] if i['id']==source);dest=next(i for i in M['instances'] if i['id']==target)
 for r in old['sourceMeasurements']:r['owner']=target;dest['sourceMeasurements'].append(r)
 dest['design']+=' Four numeric Y ticks are calculated from --max at zero, one third, two thirds and maximum. The original independent-tick GAP claim was incorrect; built-in CSS counters provide the existing data-derived rail.'
 M['instances'].remove(old)
(P/'map.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n')
gaps=[i for i in M['instances'] if i['use']=='unexpressible'];out=['# Crossrail 계약상 미표현 영역','','지원되는 원문과 공개 수치는 조립본에 보존한다. 미지원 두번째 디자인을 임의 source/fixture 조건으로 숨겨 구현하지 않는다. 계산가능한max축의4tick은GAP이아니며CSS일반수학으로그린다.','']
for i in gaps:out+=['## '+i['id'],f'원본{i["page"]:02} / bbox `{i["bbox"]}`',i['design'],i.get('why',''),'필요한 계약 마크업: `'+i.get('requiredMarkup','별도 의미 마크업이 필요하다.')+'`.','']
(P/'GAPS.md').write_text('\n\n'.join(out)+'\n');print('axes restored; map',len(M['instances']),'gaps',len(gaps))
