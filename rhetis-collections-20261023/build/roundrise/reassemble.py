from pathlib import Path
import json,re,importlib.util
R=Path('/workspace/output/roundrise-review');B=Path('/workspace/output/roundrise');S=R/'reassembled';S.mkdir(exist_ok=True)
D=json.loads((R/'replica/slides.json').read_text())
# Styles are exact collection, type-ladder and reference palette output. No page-specific CSS is introduced.
css=''.join((p.read_text() for p in [B/'kit/css/tokens.css',B/'foundation/foundation.css']+sorted(B.glob('elements/*/element.css'))))
steps=json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text());palette=json.loads(Path('/workspace/work/reference/contract/palette.json').read_text());css+='\n.slide{'+''.join(f'--type-{n}:{n}px;' for n in steps)+'}\n'
source_palette={}
for mode,vs in palette.items():
 vs=dict(palette['light'])
 for key,value in list(vs.items()):
  if key.startswith('--a1-') and key!='--a1-on':
   value=re.sub(r'([0-9.]+)\)$','264)',value);vs[key]=value
 vs.update({'--a1-1-soft':'#e6efff','--a1-2-soft':'#c6e5f8' if mode=='dark' else '#d6ebfa','--page':'#ffffff','--ink':'#050608','--a1':'#065de5','--a1-on':'#ffffff','--a1-7':'#065de5','--roundrise-dark-surface':'var(--a1)'})
 source_palette[mode]=vs
 css+=('.slide.dark' if mode=='dark' else '.slide')+'{'+''.join(f'{k}:{v};' for k,v in vs.items())+'}\n'
(R/'source-palette.json').write_text(json.dumps(source_palette,indent=2))
(S/'collection.css').write_text(css)
def el(k,c,body='',style='',tag='div'):
 return f'<{tag} class="{c}" data-el="roundrise-{k}"'+(f' style="{style}"' if style else '')+f'>{body}</{tag}>'
def slot(k,c,body='',col=1,cols=12,row=1,rows=6,style=''):
 return el(k,c,body,f'grid-column:{col} / span {cols}; grid-row:{row} / span {rows}'+('; '+style if style else ''))
def icon(name='users'):
 paths={
 'users':'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/><circle cx="9" cy="7" r="4"/>',
 'target':'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/><path d="M12 12 23 1M17 1h6v6"/>',
 'chart':'<path d="M3 3v18h18M7 17v-5h3v5M12 17V8h3v9M17 17V4h3v13"/>',
 'handshake':'<path d="m11 17 2 2a2 2 0 0 0 3-3l-6-6-3 3a2 2 0 0 1-3-3l4-4h5l4 4M3 5H1v12h3M21 5h2v12h-3M7 17l3 3a2 2 0 0 0 3-3M5 15l3 3"/>',
 'briefcase':'<rect x="3" y="7" width="18" height="14" rx="2"/><path d="M8 7V3h8v4M3 13h18M10 13v3h4v-3"/>',
 'puzzle':'<path d="M4 3h6v3a2 2 0 1 0 4 0V3h7v7h-3a2 2 0 1 0 0 4h3v7h-7v-3a2 2 0 1 0-4 0v3H3v-7h3a2 2 0 1 0 0-4H3V3Z"/>'}
 return '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round">'+paths[name]+'</svg>'
def parts(**kw):return '<div class="parts">'+''.join(f'<div class="{k}">{v}</div>' for k,v in kw.items() if v is not None)+'</div>'
def card(name,fig=None,note=None,kick=None,mark=None,on=False):return el('card','card'+(' on' if on else ''),parts(mark=mark,kick=kick,name=name,fig=fig,note=note))
def head(text,kick='',note='',big=False,center=False,on=False,**grid):return slot('headline','headline'+(' big' if big else '')+(' center' if center else '')+(' on' if on else ''),(f'<p class="kick">{kick}</p>' if kick else '')+f'<h2>{text}</h2>'+(f'<p class="note">{note}</p>' if note else ''),**grid)
def group(items,col=1,cols=12,row=1,rows=6,classes='group'):
 return f'<div class="{classes}" style="grid-column:{col} / span {cols}; grid-row:{row} / span {rows}">'+''.join(items)+'</div>'
def graph(vals,kind,col,cols,row,rows):
 if kind=='bar':return slot('chart-bar','bars',''.join(f'<div class="bar" style="--v:{v}"><b>{v}</b><span>XX년 {j+1}분기</span></div>' for j,v in enumerate(vals)),col,cols,row,rows,style='--max:150')
 return slot('chart-area','areas','<div class="series"><b class="name">분기별 신규 계약 추이</b>'+''.join(f'<div class="pt" style="--v:{v}"><b>{v}</b></div>' for v in vals)+'</div><div class="axis">'+''.join(f'<span>XX년 {j+1}분기</span>' for j in range(len(vals)))+'</div>',col,cols,row,rows,style='--max:150')
for i,d in enumerate(D,1):
 k=d['kind'];t=d['title'].replace('<em>','<b>').replace('</em>','</b>');n=d.get('note','').replace('<em>','<b>').replace('</em>','</b>');it=d['items'];body='';heading=True
 if k in ['cover','end','statement','qa','message']:
  heading=False
  if k=='cover':
   body=head(t,d['kick'],n,True,col=1,cols=10,row=1,rows=4)+group([el('image-frame','frame','<div class="seat" data-ph="'+str(z)+'"></div>') for z in range(1,4)],row=5,rows=2)
  elif k=='end':body=head(t,note=n,big=True,on=True,col=1,cols=7,row=2,rows=4)+slot('image-frame','frame','<div class="seat avatar" data-ph=""></div>',8,5,1,6)
  else:body=head(t,'<b><svg class="icon" viewBox="0 0 43 24" fill="currentColor"><circle cx="4" cy="18" r="4"/><path d="M8 22 20 2h8L17 22zM22 22 34 2h8L30 22z"/></svg>Miricompany</b>' if k=='statement' else d['kick'],n,True,True,on=k=='qa',col=1,cols=12,row=1,rows=6)
 elif k=='index':
  body=slot('agenda','agenda',''.join(f'<div class="entry"><span class="mark">{j+1:02}</span><b class="name">{a}</b><span class="note">{b}</span></div>' for j,(a,b) in sorted(enumerate(it), key=lambda q:(q[0]%4,q[0]//4))))
 elif k in ['cards','metrics','team']:
  cards=[]
  for j,item in enumerate(it):
   if k=='metrics':
    a,f,b=item;badge=el('pill','pill on',parts(name=b));cards.append(card(a,f,'해당 수치에 대한 출처 및<br>참고 정보를 입력해 주세요.'+badge))
   elif k=='team':
    a,f,b=item;cards.append(card(a,f,b,mark=f'<div class="seat" data-ph="{j+1}"></div>'))
   else:
    a,b=item
    if d.get('blue'):cards.append(el('card','card quiet'+(' on' if j==2 else ''),parts(mark=str(j+1),name=a,note=b)))
    else:cards.append(card(a,note=b,kick=f'{j+1:02}',mark=f'<div class="seat" data-ph="{j+1}"></div>'))
  body=group(cards,classes='group three' if k=='cards' and d.get('blue') else 'group')
 elif k in ['bar','area','position','sequence']:
  heading=False;body=head(t,d['kick'],n,big=k=='area',on=bool(d.get('blue')),col=1,cols=4 if k in ['bar','area'] else 5,row=1,rows=6)
  if k in ['bar','area']:
   chartnode=re.sub(r'grid-column:[^;]+; grid-row:[^;]+;? ?','',graph(it,k,5,8,2,5))
   body+=slot('card','card','<div class="parts"><h3 class="name">'+d['charttitle'].replace('<em>','<b>').replace('</em>','</b>')+'</h3>'+chartnode+(el('legend','legend','<span class="key tone-1">매출액</span>') if k=='bar' else el('legend','legend','<span class="key tone-1">분기별 신규 계약 추이</span>'))+'</div>',5,8,1,6)
  elif k=='position':body+=slot('positioning','posmap','<div class="axis-x"><span></span><span>가격 경쟁력 →</span></div><div class="axis-y"><span></span><span>서비스 품질 →</span></div>'+''.join(f'<div class="mark {"on" if j==3 else ""}" style="--x:{x};--y:{y}"><span class="name">'+('<svg class="icon" viewBox="0 0 43 24" fill="currentColor"><circle cx="4" cy="18" r="4"/><path d="M8 22 20 2h8L17 22zM22 22 34 2h8L30 22z"/></svg>' if j==3 else '')+f'{a}</span></div>' for j,(a,x,y) in enumerate([('A사',19,74),('B사',28,26),('C사',72,34),('Miricompany',79,87)])),6,7,1,6)
  else:body+=slot('steps','steps col',''.join(f'<div class="step"><span class="mark">{j+1:02}</span><b class="name">{a}</b></div>' for j,(a,b) in enumerate(it)),6,7,1,6)
 elif k=='donut':
  heading=False;body=slot('chart-donut','donut','<b class="fig">94%</b><span class="name">재계약률</span>',1,6,1,6,style='--v:94')+head(t,d['kick'],n,col=7,cols=6,row=1,rows=6)
 elif k=='response':
  for j,(a,b) in enumerate(it):
   r=1+j*(6//len(it));rs=6//len(it)
   body+=group([el('card','card line',parts(mark=icon('users' if j==0 else 'chart') if not d.get('blue') else f'{j+1:02}',kick='Challenge' if j==0 and not d.get('blue') else None,name=a,note=('이곳에 관련된 내용을 입력해 주세요.' if not d.get('blue') else None))),el('card','card line on',parts(mark=icon('handshake' if j==0 else 'target') if not d.get('blue') else '',kick='Response' if j==0 and not d.get('blue') else None,name=b,note=('이곳에 관련된 내용을 입력해 주세요.' if not d.get('blue') else None)))],row=r,rows=rs,classes='group two')
 elif k=='market':
  ar=graph(it,'area',1,7,1,6).replace('--max:150','--max:100').replace('분기별 신규 계약 추이','시장 성장 추이 (연도별)')
  ar=re.sub(r'grid-column:[^;]+; grid-row:[^;]+;? ?','',ar)
  ar=re.sub(r'XX년 [1-4]분기','20XX',ar)
  body=slot('card','card','<div class="parts">'+ar+el('metric','stat',parts(name='당사 타겟 시장 규모',fig='4,200<small>억</small>',note='시장은 연평균 +18% 성장 중이며,<br>우리의 기회는 계속 확대되고 있습니다.'))+'</div>')
 elif k=='rows':body=slot('list','list num divided',''.join(f'<div class="item"><b class="name">{a}</b><span class="note">{b}</span></div>' for a,b in it))
 elif k in ['steps','project']:
  cards=[]
  for j,(a,b) in enumerate(it):
   cards.append(el('card','card',parts(mark='<div class="seat" data-ph=""></div>',kick=el('pill','pill on',parts(name=f'STEP {j+1:02}')) if k=='steps' else None,name=a,note=None if k=='steps' else '이곳에 해당 내용에 대한<br>자세한 설명을 입력해 주세요.')))
  body=group(cards,classes='group three',rows=6 if k=='steps' else 4)
  if k=='project':body+=slot('timeline','track',''.join('<div class="stop"><p class="kick">'+b+'</p><b class="name"></b><p class="note"></p></div>' for a,b in it),row=5,rows=2)
 elif k=='goals':body=''.join(slot('card','card line',parts(mark=icon(['handshake','chart','briefcase','puzzle'][j]),name=a,fig=b.replace('<em>','<b>').replace('</em>','</b>')),col=1+(j%2)*6,cols=6,row=1+(j//2)*3,rows=3) for j,(a,b) in enumerate(it))
 elif k=='hub':body=slot('hub','hub','<div class="core"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2"><circle cx="11" cy="13" r="9"/><circle cx="11" cy="13" r="6"/><circle cx="11" cy="13" r="3"/><path d="m11 13 9-9m-3-3v6h6"/></svg><span>2080 하반기<br>목표</span></div>'+''.join(f'<div class="spoke"><b class="name">{a}</b><p class="note">{b}</p></div>' for a,b in it))
 elif k=='values':body=group([el('card','card line'+(' on' if j==1 else ''),parts(kick=f'{j+1:02}',name=a,note=b)) for j,(a,b) in enumerate(it)])
 header=(f'<header class="head center"><p class="kicker">{d["kick"]}</p><h1 class="title">{t}</h1>'+ (f'<p class="lead">{n}</p>' if k in ['steps','values'] and n else '')+'</header>') if heading else ''
 body=re.sub(r'<div class="mark"><div class="seat" data-ph="(\d*)"></div></div>',r'<div class="mark seat" data-ph=""></div>',body)
 decor=''.join('<div class="deco"></div>' for _ in range({2: 3, 3: 2, 4: 3, 5: 2, 6: 2, 7: 3, 8: 3, 9: 2, 10: 2, 11: 2, 12: 2, 13: 2, 14: 2, 15: 3, 16: 2, 17: 2, 18: 2, 19: 2, 20: 2, 21: 2, 23: 3}.get(i,0)))
 html='<!doctype html><html lang="ko"><meta charset="utf-8"><title>Roundrise '+str(i)+'</title><link rel="stylesheet" href="../replica/assets/fonts/fonts.css"><link rel="stylesheet" href="collection.css"><body style="margin:0"><section class="slide'+(' dark' if d.get('blue') else '')+'"'+(' style="--page:#e4e6e8;--a1-1-soft:#e4e6e8;--a1-2-soft:#e4e6e8"' if k=='message' else '')+'><div class="page">'+decor+'<div class="top"><span class="deck"><svg class="icon" viewBox="0 0 43 24" fill="currentColor"><circle cx="4" cy="18" r="4"/><path d="M8 22 20 2h8L17 22zM22 22 34 2h8L30 22z"/></svg>Miricompany</span><span class="sec">Town hall meeting</span></div>'+header+'<div class="body">'+body+'</div></div></section></body></html>'
 if k=='cover':
  html='<!doctype html><html lang="ko"><meta charset="utf-8"><title>Roundrise cover</title><link rel="stylesheet" href="../replica/assets/fonts/fonts.css"><link rel="stylesheet" href="collection.css"><body style="margin:0"><section class="slide cover"><div class="page"><div class="top"><span class="deck"><svg class="icon" viewBox="0 0 43 24" fill="currentColor"><circle cx="4" cy="18" r="4"/><path d="M8 22 20 2h8L17 22zM22 22 34 2h8L30 22z"/></svg>Miricompany</span></div><div class="lockup at-top-left"><p class="kicker">'+d['kick']+'</p><h1 class="title">'+t+'</h1><p class="lead">'+n+'</p></div><div class="deco"></div></div></section></body></html>'
 (S/f'slide_{i:02}.html').write_text(html)
print('24 pages assembled solely from collection CSS and contract markup')
