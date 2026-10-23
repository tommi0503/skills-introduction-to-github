from pathlib import Path
from bs4 import BeautifulSoup as B
import re
P=Path(__file__).parent;E=P/'crossrail/elements'
def app(el,s):f=E/el/'element.css';f.write_text(f.read_text()+'\n'+s+'\n')
f=P/'replica/slide_04.html';s=B(f.read_text(),'html.parser')
for d in s.select('div[style]'):
 if 'font-size:64px' in d['style']:d['style']=d['style'].replace('top:131px','top:125px')
f.write_text(str(s))
f=P/'assets/source-palette.css';f.write_text(f.read_text()+'\n.slide:has(.rail.on):not(:has(.head.at-bottom-left)) [data-el="crossrail-agenda"]{--n-7:#555555}\n')
# Tier corners continue along the source triangular envelope.
s='[data-el="crossrail-pyramid"]:not(:has(.note))'
app('pyramid',s+' .level:nth-child(2){width:48.25%;clip-path:polygon(22% 0,78% 0,100% 100%,0 100%)}'+s+' .level:nth-child(3){width:72.5%;clip-path:polygon(16% 0,84% 0,100% 100%,0 100%)}'+s+' .level:nth-child(4){clip-path:polygon(13% 0,87% 0,100% 100%,0 100%)}')
# Source07 deliberate three-line note, as read from the original.
f=P/'reassembled/slide_07.html';soup=B(f.read_text(),'html.parser');notes=soup.select('[data-el="crossrail-card"] .note');note=notes[2] if '위아래' in notes[2].get_text() else next(x for x in notes if '위아래' in x.get_text());note.clear();note.extend(B('위아래 순서가 있는 목록형과 달리<br>원형 배치는 모든 요소를 동등한 비중으로<br>다룹니다.','html.parser').contents);f.write_text(str(soup))
s='[data-el="crossrail-card"].quiet:not(:has(.mark,.kick,.fig))'
app('card',s+' .note{padding-inline:0;letter-spacing:calc(var(--body-track)*1.125)}')
# Three text blocks have two construction rules, not three row borders.
s='[data-el="crossrail-list"].divided:has(>.item:nth-child(3):last-child)'
app('list',s+'{gap:calc(var(--gap-sm)*13/6)}'+s+'>.item{position:relative;box-sizing:border-box;flex:none;border:0;padding:0;height:calc(var(--gap-lg)*2.9)}'+s+'>.item:last-child{height:auto}'+s+'>.item:not(:last-child)::after{content:"";position:absolute;left:calc(var(--margin-x)*-1);top:100%;height:1px;width:calc(100% + var(--margin-x) + var(--gap-lg)*1.3);background:var(--n-3)}'+s+'>.item:nth-child(2)::after{width:calc(100% + var(--margin-x) + var(--gap-lg)*3.15)}')
# The A-D divider sits halfway inside the 36 px inter-column gutter.
s='[data-el="crossrail-card"].line:has(.fig):not(:has(.mark,.kick)):not(:has(.fig>b))'
app('card',s+':not(:last-child)::after{right:calc(var(--gap-sm)*-1.5)}'+s+' .note>span{color:var(--ink)}')
for f in [P/'reassembled/slide_12.html',E/'card/fixtures/card-letter-columns.html']:
 soup=B(f.read_text(),'html.parser')
 for p in soup.select('.note'):
  h=p.decode_contents();h=re.sub(r'(•[^<]+)',r'<span>\1</span>',h);p.clear();p.extend(B(h,'html.parser').contents)
 f.write_text(str(soup))
