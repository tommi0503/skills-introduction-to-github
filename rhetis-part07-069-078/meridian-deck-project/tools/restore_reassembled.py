from pathlib import Path
import re,html,json
P=Path(__file__).parent;C=P/'meridian-deck';R=P/'reassembled'
def e(t,cls,body,style=''):
 return f'<div class="{cls}" data-el="meridian-deck-{t}"'+(f' style="{style}"' if style else '')+'>'+body+'</div>'
def seat(n=1,cl=''):return f'<div class="seat{(" "+cl) if cl else ""}" data-ph="{n}"></div>'
def frame(n=1,cl=''):return e('image-frame','frame',seat(n,cl))
def pro(t,cl=''):return e('prose','prose'+(' '+cl if cl else ''),''.join('<p>'+x.replace('\n','<br>')+'</p>' for x in t.split('\n\n')))
def hd(t,cl='',kick='',note=''):return e('headline','headline'+(' '+cl if cl else ''),(f'<p class="kick">{kick}</p>' if kick else '')+'<h2>'+t.replace('\n','<br>')+'</h2>'+(f'<p class="note">{note}</p>' if note else ''))
def wrap(cl,items):return '<div class="'+cl+'">'+''.join(items)+'</div>'
def g(items,cl=''):return wrap('group'+(' '+cl if cl else ''),items)
def st(items):return wrap('stack',items)
def pos(s,c=1,r=1,w=12,h=6):
 a=s.find('>');start=s[:a];v=f'grid-column:{c} / span {w};grid-row:{r} / span {h};'
 if 'style="' in start:start=start.replace('style="','style="'+v,1)
 else:start+=' style="'+v+'"'
 return start+s[a:]
def ls(items,notes=None,cl=''):
 return e('list','list'+(' '+cl if cl else ''),''.join('<div class="item"><b class="name">'+t+'</b>'+(f'<p class="note">{notes[i]}</p>' if notes else '')+'</div>' for i,t in enumerate(items)))
def pill(t,cl='on'):return e('pill','pill '+cl,'<div class="parts"><p class="name">'+t+'</p></div>')
def call(t):return e('callout','callout','<p>'+t+'</p>')
def card(name,note='',cl='',kick='',ic=''):
 return e('card','card'+(' '+cl if cl else ''),'<div class="parts">'+(f'<p class="kick">{kick}</p>' if kick else '')+(f'<span class="mark"><span class="icon" data-icon="{ic}"></span></span>' if ic else '')+'<p class="name">'+name+'</p>'+(f'<p class="note">{note}</p>' if note else '')+'</div>')
def write(n,body,title=None,sub=None):
 f=R/f'slide_{n:02d}.html';t=f.read_text()
 # Existing complete local runtime/font providers stay unchanged.
 old=re.search(r'<div class="body">',t)
 if old:
  a=old.end();end=t.rfind('</div><footer');t=t[:a]+body+t[end:]
 if title is not None:t=re.sub(r'(<h1 class="title">).*?(</h1>)',lambda m:m[1]+title+m[2],t,flags=re.S)
 if sub is not None:t=re.sub(r'(<p class="lead">).*?(</p>)',lambda m:m[1]+sub+m[2],t,count=1,flags=re.S)
 f.write_text(t)
# Image-led three-spoke diagram preserves every original icon and both supporting lines.
notes='관련 내용을 텍스트로 간략하게 입력해주세요. 이곳에 관련 내용을 텍스트로<br>간략하게 입력해주세요. 관련 내용을 텍스트로 간략하게 입력해주세요.'
hub='<div class="core">'+seat(1,'avatar')+'</div>'
for i,ic in enumerate(['folder','pencil','graduation-cap']):
 hub+='<div class="spoke"><span class="mark"><span class="icon" data-icon="'+ic+'"></span></span><b class="name">'+('이곳에 제목을 입력하세요' if i==1 else '제목을 입력하세요')+'　<small>│ KEY POINT</small></b><p class="note">'+notes+'</p></div>'
write(10,pos(e('hub','hub',hub)))
# Numbered media rows keep the body as independent prose, never squeeze it into .note.
rows=[]
copy='좌측에 관련 이미지를 넣어주세요. 실제로 경험한 이미지를 넣으면 더 좋습니다. 업무 현장 사진을<br>추가해주세요. 업무 현장 사진을 추가해주세요. 관련 도표를 넣어주셔도 좋습니다.<br>실제로 경험한 업무 내용을 입력해주세요. 관련된 프로젝트 사진을 아래에 넣어주세요.'
for i,(h,en) in enumerate([('고객 니즈','CUSTOMER'),('문제 OR 기회상황','COMPANY'),('비교대상','COMPETITOR')]):rows.append(wrap('split',[hd(f'{i+1:02d}','big center'),wrap('split',[frame(i+1),st([hd('<b>'+h+'</b>　<small>│ '+en+'</small>'),pro(copy)])])]))
write(16,pos(st(rows)))
# Action rows include the complete source paragraph and two separate quiet bullet cells.
copy='좌측에 관련 이미지를 넣어주세요. 실제로 경험한<br>이미지를 넣으면 더 좋습니다. 상단에 현장 사진을<br>추가해주세요. 관련 도표를 넣어주셔도 좋습니다.'
rows=[]
for h in ['문제해결 액션','생산성 증가 액션','의사소통 협상 액션']:rows.append(g([st([hd('<b>'+h+'</b>'),pro(copy)]),ls(['강조하고 싶은 포인트 내용을 입력하세요']*2)]))
write(24,pos(call('이곳에 프로젝트 결과에 대해 강조하고 싶은 내용을 텍스트로 입력해 주세요. 관련 내용을 텍스트로 입력해주세요.'),1,1,12,1)+pos(wrap('split wide-left',[st(rows),frame()]),1,2,12,5))
print('Restored source-level compositions:',[10,16,24])
