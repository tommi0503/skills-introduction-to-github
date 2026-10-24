from pathlib import Path
from playwright.sync_api import sync_playwright
from lxml import html,etree
import json
P=Path(__file__).parent;M=json.loads((P/'map.json').read_text());rows=[i for i in M['instances'] if i['page']==18 and i.get('leaf')=='list'];glyphs={};assert len(rows)==5
with sync_playwright() as q:
 b=q.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':720});page.goto('http://127.0.0.1:8875/crossrail-project/replica/slide_18.html');page.evaluate('document.fonts.ready')
 for i in rows:
  glyphs[i['id']]=page.evaluate('''s=>{const el=document.querySelector(s),w=document.createTreeWalker(el,NodeFilter.SHOW_TEXT);let t;while(t=w.nextNode()){let j=t.textContent.indexOf('•');if(j>=0){let r=document.createRange();r.setStart(t,j);r.setEnd(t,j+1);let b=r.getBoundingClientRect();return [b.x,b.y,b.width,b.height]}}return null}''',i['sourceMeasurements'][0]['selector'])
 b.close()
gaps=[]
for i in rows:
 old=P/'crossrail'/i['fixture'];d=html.fromstring(old.read_text());text=''.join(d.itertext());newpath='elements/prose/fixtures/'+old.name
 prose=html.Element('div',{'class':'prose','data-el':'crossrail-prose','style':d.get('style')});etree.SubElement(prose,'p').text=text
 (P/'crossrail'/newpath).write_text('<!-- min:3x1 -->\n'+html.tostring(prose,encoding='unicode')+'\n');old.unlink()
 i.update(leaf='prose',use='same-as:3',fixture=newpath,interpretation='One paragraph uses prose. Its standalone dot is a separate gap: list.items@1 requires at least two items.')
 g={'id':i['id']+'-single-marker','page':18,'leaf':'prose','use':'unexpressible','bbox':[round(v,2) for v in glyphs[i['id']]],'sourceMeasurements':[],'sourceTextRange':{'selector':i['sourceMeasurements'][0]['selector'],'text':'•','range':'first bullet character'},'why':'A single paragraph has a dot marker. list.items@1 requires2..8 items; inventing another row changes the content. Prose retains the paragraph but has no standalone marker.','requiredMarkup':'<div class="prose marked"><p>…</p></div> (a contracted single-paragraph marker variant)'};gaps.append(g)
M['instances']+=gaps;(P/'map.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n')
f=P/'reassembled/slide_18.html';d=html.fromstring(f.read_text())
for e in d.xpath('//*[@data-el="crossrail-list"]'):
 n=html.Element('div',{'class':'prose','data-el':'crossrail-prose','style':e.get('style')});etree.SubElement(n,'p').text=''.join(e.itertext());e.getparent().replace(e,n)
f.write_text('<!doctype html>'+html.tostring(d,encoding='unicode')+'\n')
f=P/'crossrail/elements/matrix-nine/fixtures/base-a.html';d=html.fromstring(f.read_text());a=html.Element('div',{'class':'axis-y'})
for t in ['긴급 대응','예정 점검','상시 보관']:etree.SubElement(a,'span').text=t
d.insert(0,a);a=html.Element('div',{'class':'axis-x'})
for t in ['낮은 물량','보통 물량','높은 물량']:etree.SubElement(a,'span').text=t
d.append(a);f.write_text('<!-- min:9x6 -->\n'+html.tostring(d,encoding='unicode')+'\n')
with (P/'GAPS.md').open('a') as f:
 for g in gaps:f.write('\n## '+g['id']+'\n\nSource18, actual single-character DOM range bbox `'+str(g['bbox'])+'`.\n\n'+g['why']+'\n\nRequired markup: `'+g['requiredMarkup']+'`.\n')
with (P/'review-notes.md').open('a') as f:f.write('\n## 後속 taxonomy 계약 교정\n\n추가 감사에서 source18 단일 항목5개의 list 최소2항목 규칙 위반을 확인했다. 행을 지어내지 않고 같은 문장·지도 슬롯을 prose로 옮겼다. 원래 한 글자 bullet은 DOM Range로 측정해 marked-prose gap으로 기록했다. matrix-nine의 첫 기본 fixture에 누락된 axis-x/axis-y와 각3개 라벨도 넣었다. 관련 시트와 조립본을 다시 렌더한다.\n')
print('remapped',len(rows),'map',len(M['instances']),'gaps',sum(i['use']=='unexpressible' for i in M['instances']))
