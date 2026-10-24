from pathlib import Path
from lxml import html
import json,copy
P=Path(__file__).parent;E=P/'crossrail/elements';M=json.loads((P/'map.json').read_text());I=json.loads((P/'original-assembly-identities.json').read_text())
f=E/'card/element.css';s=f.read_text().replace('.line{background:transparent;color:inherit;border:1px solid var(--n-3)}','.line{background:transparent;color:inherit;border:0}').replace('.line .note{left:0;right:0;top:69cqh;color:inherit}', '.line .note{left:0;right:0;top:69cqh;color:var(--n-7)}');assert s!=f.read_text();f.write_text(s)
f=P/'assets/source-palette.css';f.write_text(f.read_text()+'\n.slide.on .card.line{--n-7:#ffffff}\n')
i=next(i for i in M['instances'] if i['id']=='p14-forward-three');i.update(use='unexpressible',fixture=None,why='This source uses three independently spaced chevrons with three different ordinal fills. The single horizontal steps base from source10 is a continuous same-fill connected rail. Neither the allowed .col variant nor an optional mark/name/note changes that design; treating them as same-as10 was incorrect.',requiredMarkup='<div class="steps separated"><div class="step tone-1">…</div><div class="step tone-2">…</div><div class="step tone-3">…</div></div> (a separately contracted spaced-chevron design)',design='1090×170px at(95,260): three separate right-facing chevrons with visible gaps, navy/slate/pale ordinal fills, 01/02/03 labels, names and secondary notes below. This is a second steps design unsupported by the source10 continuous-rail base.')
f=E/'steps/fixtures/replica-14.html';f.unlink(missing_ok=True)
f=P/'reassembled/slide_14.html';d=html.fromstring(f.read_text());body=d.xpath('//div[@class="body"]')[0]
for e in list(body):
 if e.get('data-el')=='crossrail-steps':body.remove(e)
f.write_text('<!doctype html>'+html.tostring(d,encoding='unicode')+'\n');I['14']=[q for q in I['14'] if q!='p14-forward-three']
for i in list(M['instances']):
 if i['page']!=17 or not i.get('fixture'):continue
 boxes=[q for q in i['sourceMeasurements'] if not q.get('text') and 'border:' in q.get('style','')]
 if not boxes:continue
 gid=i['id']+'-boundary';g={'id':gid,'page':17,'leaf':'card','use':'unexpressible','bbox':i['bbox'],'fixture':None,'sourceMeasurements':boxes,'design':f'{i["bbox"][2]}×{i["bbox"][3]}px independent enclosing rectangle at({i["bbox"][0]},{i["bbox"][1]}), one-pixel pale border'+(' and slate fill' if 'background:' in boxes[0]['style'] else '')+'. It is additional furniture around the supported card name/note.','why':'The source11/12 line-card design has an open accent rule, not a complete enclosing box. Adding this second outline design by an undocumented part/source condition would violate the one-design-per-variant rule. Text remains supported in the line card; only the extra enclosing rectangle is omitted.','requiredMarkup':'<div class="outlined-panel"><div class="card line" data-el="crossrail-card">…</div></div> (a contracted enclosing panel distinct from the open line card)'}
 for q in boxes:q['owner']=gid
 i['sourceMeasurements']=[q for q in i['sourceMeasurements'] if q not in boxes];M['instances'].append(g)
(P/'map.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n');(P/'original-assembly-identities.json').write_text(json.dumps(I,ensure_ascii=False,indent=2)+'\n')
gaps=[i for i in M['instances'] if i['use']=='unexpressible'];out=['# Crossrail 계약상 미표현 영역','','원문과 공개 수치는 지원되는 본문/차트에 보존한다. 미지원 두번째 디자인은 임의의 fixture/source 조건으로 숨겨 구현하지 않는다.','']
for i in gaps:out+=['## '+i['id'],f'원본{i["page"]:02} / bbox `{i["bbox"]}`',i['design'],i.get('why',''),'필요한 계약 마크업: `'+i.get('requiredMarkup','별도 의미 마크업이 필요하다.')+'`.','']
(P/'GAPS.md').write_text('\n\n'.join(out)+'\n');print('map',len(M['instances']),'gaps',len(gaps))
