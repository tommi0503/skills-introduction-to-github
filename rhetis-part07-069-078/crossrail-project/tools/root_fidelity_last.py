from pathlib import Path
from bs4 import BeautifulSoup as B
import re
P=Path(__file__).parent;E=P/'crossrail/elements'
def app(el,s):f=E/el/'element.css';f.write_text(f.read_text()+'\n'+s+'\n')
f=P/'replica/slide_24.html';s=B(f.read_text(),'html.parser')
for d in s.select('div[style]'):
 if d.get_text().startswith('원 그래프'):d['style']=re.sub(r'width:[^;]+','width:539px',d['style'])
f.write_text(str(s))
for f in [P/'reassembled/slide_26.html',E/'roadmap/fixtures/roadmap-split-lane.html']:
 s=B(f.read_text(),'html.parser');lanes=s.select('.lane');bars=lanes[1].select('.bar');bars[-1]['class']=['bar','tone-2'];f.write_text(str(s))
s='[data-el="crossrail-roadmap"]:has(.heads>span:nth-child(5):last-child)'
app('roadmap',s+' .lane:nth-child(1 of .lane)>.bar,'+s+' .lane:last-child>.bar{box-shadow:0 calc(var(--gap-sm)*-1.125) 0 var(--n-3),0 calc(var(--gap-sm)*31/24) 0 var(--n-3)}')
# The arrow is behind the first white circle, while its label remains above.
app('positioning','''[data-el="crossrail-positioning"] .mark:nth-child(1 of .mark)::after{content:"";position:absolute;inset:0;border-radius:50%;background:var(--page);z-index:0}[data-el="crossrail-positioning"] .mark:nth-child(1 of .mark)>.name{position:relative;z-index:1}''')
f=P/'assets/source-palette.css';f.write_text(f.read_text()+'\n.slide [data-el="crossrail-table"]:not(:has(thead)):has(tr:nth-child(6)){--n-7:var(--ink)}\n')
# Scale the four tiers proportionally for all minimum/full library slots; at393px they remain100/80/88/107px.
s='[data-el="crossrail-pyramid"]:not(:has(.note))'
app('pyramid',s+' .level:first-child{flex:100 1 0px;padding-top:0}'+s+' .level:nth-child(2){flex:80 1 0px}'+s+' .level:nth-child(3){flex:88 1 0px}'+s+' .level:nth-child(4){flex:107 1 0px}'+s+' .level:first-child .name{transform:translateY(calc(var(--gap-lg)*.5))}')
f=P/'review-notes.md';s=f.read_text().replace('일반 fixture162개','일반 fixture173개');s+='''\n주 에이전트의 마지막30장 개별 삼중 대조에서 요청한 source 보정도 반영했다. 06 tier 사선을 삼각 외곽선으로 맞추고, 07 note를 원문 세 줄로 고정했으며, 08은 원본의 두 가로 구성선만 둔다. 12의 bullet과 세로선, 13의70px 아이콘·66px capsule·90px 간격, 14의22px 화살촉, 15 사진 뒤 가로선을 복원했다. 24 replica의 네 줄 문구가 재차 감기지 않도록 글상자 폭을 수정했다. 26의 두 번째 긴 막대는 중간 accent 역할이고 첫·마지막 lane에는 연한 타임레일을 둔다. 29 사선 화살표는 버전1 원 뒤에 가리고 표의 설명은 원본 navy 역할을 외부 provider로 공급했다. 신규 source 구조11개도 추가 fixture로 드러내 최종 검수 대상에 포함했다.\n''';f.write_text(s)
