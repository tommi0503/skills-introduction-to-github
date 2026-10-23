from pathlib import Path
import re,json
p=Path(__file__).parent;c=p/'crossrail'
s='[data-el="crossrail-card"].quiet:has(.parts>.kick):not(:has(.mark,.fig))'
f=c/'elements/card/element.css';f.write_text(f.read_text()+f'\n{s}{{margin:0}}\n')
f=c/'foundation/foundation.css';f.write_text(f.read_text()+'''\n.slide:not(.cover):has(.head>.title>br) .page{top:98px;bottom:98px;grid-template-rows:minmax(0,1fr)}.slide:not(.cover):has(.head>.title>br) .head{position:absolute;left:0;right:0;top:0;padding-top:0}.slide:not(.cover):has(.head>.title>br) .head>.title{margin-top:-1px;line-height:var(--crossrail-title-stack-line)}.slide:not(.cover):has(.head>.title>br) .no{top:0}.slide:not(.cover):has(.head>.title>br) .body{grid-row:1}.slide:not(.cover):has(.head>.title>br) .page::after{bottom:calc(var(--gap) + var(--gap-sm)*5/6)*-1}\n'''.replace('bottom:calc(var(--gap) + var(--gap-sm)*5/6)*-1','bottom:calc((var(--gap) + var(--gap-sm)*5/6)*-1)'))
# Every original line of the readable vision notes is retained explicitly.
lines=[['해당 페이지는 회사의 핵심 가치','와 비전을 적는 페이지입니다.','회사가 추구하는 핵심적인 가치','세 가지만 뽑아보세요. 이 가치를','추구하는 이유는 무엇인지, 이것','들을 통해 이루고 싶은 비전이나','목표는 무엇인지 설명해 주세요.'],['회사가 추구하는 비전을 이루기','위해 어떤 노력과 사업을 하는지','적어보세요. 회사의 사업과 핵심','가치가 어떤 연관성을 가지고 있','는지 설명해 주세요. 비전으로 설','득하고 싶은 부분은 무엇인지 적','어보세요.'],['회사의 비전은 누구나 이해하기','쉽도록 명확하고 간결하게 작성해','야 합니다. 회사가 장기적으로 달','성하려는 목표는 무엇인지 생각해','보세요. 직원과 고객에게 영감을','줄 수 있는 내용을 적으면 좋습니','다.']]
f=p/'reassembled/slide_05.html';s=f.read_text();i=iter(lines);s=re.sub(r'<p class="note">.*?</p>',lambda m:'<p class="note">'+'<br>'.join(next(i))+'</p>',s);f.write_text(s)
f=p/'replica/slide_05.html';s=f.read_text();i=iter(lines)
def note(m):
 st,t=m.groups()
 if 'top:423px;' in st:return '<div style="'+st+'">'+'<br>'.join(next(i))+'</div>'
 return m[0]
s=re.sub(r'<div style="([^"]*)">(.*?)</div>',note,s);s=s.replace('font-size:64px;', 'font-size:64px;').replace('top:130px','top:122px');f.write_text(s)
f=c/'elements/prose/element.css';f.write_text(f.read_text()+'\n[data-el="crossrail-prose"]:has(>p:first-child>b:only-child){max-width:500px}\n')
f=c/'elements/chart-donut/element.json';d=json.loads(f.read_text());d['tokenDefaults']['--crossrail-donut-halo']='0px';f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
f=c/'elements/chart-donut/element.css';f.write_text(f.read_text()+'\n[data-el="crossrail-chart-donut"].donut::before{box-shadow:0 0 0 var(--crossrail-donut-halo) var(--n-1)}\n')
for f in [p/'reassembled/slide_24.html',c/'elements/chart-donut/fixtures/composite-five.html']:
 s=f.read_text().replace('--crossrail-donut-diameter:336px;','--crossrail-donut-diameter:336px;--crossrail-donut-halo:12px;');f.write_text(s)
f=p/'assets/source-defaults.css';f.write_text(f.read_text()+'\n.slide{--crossrail-donut-halo:0px}\n')
print('vision lines and pie halo/source geometry corrected')
