from pathlib import Path
import json,re
from lxml import html
P=Path(__file__).parent;E=P/'meridian-deck/elements'
# Real profile content replaces the generic text bank in semantic name fields.
f=E/'person/fixtures/replica-04.html';t=html.fragment_fromstring(f.read_text().split('-->',1)[1],create_parent='div');e=t.xpath('.//*[@class="name"]')[0];e.clear();e.set('class','name');e.text='한빛솔루션 대표이사';br=html.Element('br');e.append(br);br.tail='한지훈';f.write_text('<!-- min: 4x6 -->\n'+html.tostring(t[0],encoding='unicode')+'\n')
f=E/'person/fixtures/replica-29.html';t=html.fragment_fromstring(f.read_text().split('-->',1)[1],create_parent='div')
for e,dept,name in zip(t.xpath('.//*[@class="name"]'),['정비팀','검수팀','회계팀','자재팀'],['오세훈 차장','윤서진 대리','김도현 과장','송하은 주임']):
 e.clear();e.set('class','name');b=html.Element('b');b.text=dept;e.append(b);br=html.Element('br');e.append(br);br.tail=name
f.write_text('<!-- min: 12x6 -->\n'+html.tostring(t[0],encoding='unicode')+'\n')
# The reference is a comparison table, not independent pill/card owners.
for l in ['card','pill']:
 f=E/l/'fixtures/replica-17.html'
 if f.exists():f.unlink()
# Keep an honest one-line caption minimum after regenerating its copy.
f=E/'pill/fixtures/replica-24.html';f.write_text(f.read_text().replace('<!-- min: 6x2 -->','<!-- min: 12x1 -->'))
# Source trends have optional empty value parts, not invented numeric labels.
for f in [E/'chart-line/fixtures/replica-17.html']:
 s=f.read_text();vs=[[20,35,61],[25,65,80],[30,36,69]];idx=[0]
 def patch(m):
  v=vs[idx[0]%3];idx[0]+=1;return m[0].replace('--max:100','--max:'+str(max(v)*1.25),1)
 s=re.sub(r'<div class="lines"[^>]*>',patch,s);s=re.sub(r'(<div class="pt"[^>]*>)<b>\d+</b>',r'\1<b></b>',s);f.write_text(s)
print('Original line counts and semantic profiles preserved with fresh complete copy')
