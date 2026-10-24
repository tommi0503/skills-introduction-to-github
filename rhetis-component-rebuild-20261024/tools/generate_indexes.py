from pathlib import Path
import json,collections
B=Path('/workspace/work/rebuild-20261024');names=['nocturne','inflexion','diecut','afterglow','dockside','confluence'];leaves=sorted(p.name for p in Path('/workspace/work/reference/samples/annual/elements').iterdir()if p.is_dir());maps={n:json.loads((B/n/'review/map.json').read_text())for n in names}
out=['# 요소별 replica 출처','','B = 해당 요소의 단일 base, V = 의미가 일치하는 명명된 계약 변형, 신규 = 원본에 직접 대응이 없어 덱의 측정된 언어로 설계. 반복 인스턴스의 좌표와 수치는 각 map.json에 있다.','','| leaf | nocturne | inflexion | diecut | afterglow | dockside | confluence |','|---|---|---|---|---|---|---|']
for leaf in leaves:
 vals=[]
 for n in names:
  xs=[x for x in maps[n]['instances']if x.get('leaf')==leaf and(x['use']=='base'or x['use'].startswith('variant:'))];ys=[]
  for x in xs:
   a='B '+x['page']if x['use']=='base'else'V '+x['page']+' '+x['use'][8:]
   if a not in ys:ys.append(a)
  vals.append('; '.join(ys)or'신규')
 out.append('| `'+leaf+'` | '+' | '.join(vals)+' |')
(B/'element-origins.md').write_text('\n'.join(out)+'\n');summary={};g=['# Unexpressible index','','장면의 지원되지 않는 관계만 아래에 적었다. 제안 마크업·이유는 각 컬렉션 GAPS.md에 있다. 정수 grid의 근사 차이는 review-notes.md에 분리했다.','']
for n in names:
 d=maps[n];base=collections.Counter(x.get('leaf')for x in d['instances']if x['use']=='base');gaps=[x for x in d['instances']if x['use']=='unexpressible'];summary[n]={'instances':len(d['instances']),'sourceBases':len(base),'duplicateBases':{k:v for k,v in base.items()if v!=1},'gaps':len(gaps)};g+=['## '+n+' ('+str(len(gaps))+')','']
 for x in gaps:g.append('- '+x['page']+' · '+x['design'])
 g.append('')
(B/'gap-index.md').write_text('\n'.join(g));(B/'map-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));print('origin56 rows; gaps',sum(x['gaps']for x in summary.values()))
