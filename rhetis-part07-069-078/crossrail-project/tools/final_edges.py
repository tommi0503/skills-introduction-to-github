from pathlib import Path
from bs4 import BeautifulSoup as B
P=Path(__file__).parent;E=P/'crossrail/elements'
def app(el,s):f=E/el/'element.css';f.write_text(f.read_text()+'\n'+s+'\n')
f=P/'reassembled/slide_06.html';s=B(f.read_text(),'html.parser');s.select_one('.body>.group')['style']='grid-column:1 / span 2;grid-row:1 / span 6';f.write_text(str(s))
app('chart-line','''[data-el="crossrail-chart-line"]:has(>.pt:nth-child(7):last-child){background:transparent}[data-el="crossrail-chart-line"]:has(>.pt:nth-child(7):last-child)::before{content:"";position:absolute;left:calc(var(--gap-sm)*4/3);right:0;top:0;bottom:0;background:var(--n-1);z-index:-2}''')
app('chart-bar','''[data-el="crossrail-chart-bar"]:not(.h):has(>.bar:nth-child(4):last-child){background:transparent;isolation:isolate}[data-el="crossrail-chart-bar"]:not(.h):has(>.bar:nth-child(4):last-child)::after{content:"";position:absolute;left:calc(var(--gap-sm)*-4/3);right:0;top:0;bottom:0;background:var(--n-1);z-index:-2}''')
app('table','''[data-el="crossrail-table"]:has(thead th:nth-child(5):last-child):has(tbody tr:nth-child(2):last-child) .table{table-layout:fixed}''')
s=':where(.group.col:has(>[data-el="crossrail-card"]:nth-child(3):last-child))>[data-el="crossrail-card"].quiet.line:not(:has(.mark,.kick,.fig))'
app('card',s+':nth-child(1){transform:translateY(calc(var(--gap-lg)*-.95))}'+s+':nth-child(2){transform:translateY(calc(var(--gap-lg)*-.475))}'+s+' .note{line-height:var(--lead-line)}')
f=P/'crossrail/foundation/foundation.css';f.write_text(f.read_text()+'''\n.slide.cover .lockup.at-top-left{gap:calc(var(--gap-sm)*5/6)}.slide.cover .lockup.at-top-left .title{letter-spacing:var(--title-track)}.slide.cover .meta{bottom:calc(var(--margin-y) + var(--gap-sm)/3)}.slide.cover .lockup.at-left .title{font-size:var(--type-48)}.slide.cover .lockup.at-left .lead{margin-top:calc(var(--gap-lg)*1.45)}\n''')
# Repair a malformed semicolon from the earlier systematic font conversion.
for f in (P/'replica').glob('*.html'):
 h=f.read_text().replace('text-align:centerfont-family:','text-align:center;font-family:').replace('text-align:rightletter-spacing:','text-align:right;letter-spacing:')
 if f.stem in ['slide_03','slide_20','slide_22','slide_24']:
  s=B(h,'html.parser')
  for d in s.select('div[style]'):
   st=d['style'];tx=d.get_text()
   if 'font-size:18px' in st and ('#8c8c8c' in st or '#747' in st):d['style']=st.replace('line-height:1.22','line-height:1.4')
  h=str(s)
 f.write_text(h)
# Replica24 uses the same legible source text and four actual source lines.
f=P/'replica/slide_24.html';s=B(f.read_text(),'html.parser')
for d in s.select('div[style]'):
 if d.get_text().startswith(('원 그래프','원 그래프를')):
  d.clear();d.extend(B('원 그래프와 유사하지만 중앙 공간 활용도가 높아 정보 전달과 디자인을 동<br>시에 잡을 수 있는 레이아웃입니다. 그래프 옆이나 하단에는 데이터가 시사<br>하는 핵심 내용을 요약해 적어주세요. 그래프에서 도출된 결론을 텍스트로<br>보완하면 읽는 이에게 더욱 강력한 설득력을 줍니다.','html.parser').contents);d['style']=d['style'].replace('width:500px','width:539px')
f.write_text(str(s))
