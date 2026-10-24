"""Assemble mapped structures; only contract roots and grid placement, no page CSS."""
from pathlib import Path
from lxml import html,etree
import copy,json
P=Path(__file__).parent;K=P/'vectorbox';O=P/'reassembled';O.mkdir(exist_ok=True)
raw={n:html.fromstring((P/'replica'/f'slide_{n:02}.html').read_text()).xpath('//section/*') for n in range(2,14)}
def txt(n,i):
 e=raw[n][i-1];return (e.text or '')+''.join(etree.tostring(c,encoding='unicode',method='html') for c in e if c.tag!='svg')
def icon(s):return f'<span class="icon" data-icon="{s}"></span>'
def card(cls='',mark=None,name=None,note=None,kick=None,fig=None):
 return '<div class="card '+cls+'" data-el="vectorbox-card"><div class="parts">'+(f'<p class="kick">{kick}</p>' if kick else '')+(f'<span class="mark">{icon(mark)}</span>' if mark else '')+(f'<b class="fig">{fig}</b>' if fig else '')+(f'<p class="name">{name}</p>' if name else '')+(f'<p class="note">{note}</p>' if note else '')+'</div></div>'
def box(s,c,r,w,h):
 e=html.fragment_fromstring(s);e.set('style',f'grid-column:{c} / span {w};grid-row:{r} / span {h}');return etree.tostring(e,encoding='unicode',method='html')
def group(items):return '<div class="group">'+''.join(items)+'</div>'
def legend(items,tones=None):return '<div class="legend" data-el="vectorbox-legend">'+''.join(f'<span class="key'+(f' tone-{(tones or [1,2,3,4,5])[j%len(tones or [1,2,3,4,5])]}' if (tones or [1,2,3,4,5])[j%len(tones or [1,2,3,4,5])] else '')+f'">{t}</span>' for j,t in enumerate(items))+'</div>'
B={};D={}
B[2]=box('<div class="agenda" data-el="vectorbox-agenda">'+''.join(f'<div class="entry"><span class="mark">{txt(2,4+2*j)}</span><b class="name">{txt(2,5+2*j)}</b></div>' for j in range(8))+'</div>',2,1,8,5);D[2]=''
B[3]=box(group([card('line',m,txt(3,7+3*j),txt(3,8+3*j)) for j,m in enumerate(['target','users-round','trending-up','rocket'])]),1,1,12,5)
# Unexpressible grouped bars remain absent, not replaced by a semantically different chart.
B[4]='<!-- GAP 04-grouped-chart: category-group and explicit axis markup needed. -->'+box(legend([txt(4,6),txt(4,8)]),3,1,4,1)+box(card('on',fig='85<small>%</small>'),9,1,2,2)+box(card('line tone-1','medal',txt(4,35)),11,1,2,3)+box(card('on tone-2',fig='42<small>%</small>'),9,4,2,2)+box(card('line','trending-up',txt(4,38)),11,4,2,3)
B[5]=box(group([card('quiet',m,txt(5,6+3*j),txt(5,7+3*j)) for j,m in enumerate(['notebook-pen','user-round-search','settings','refresh-cw'])]),1,1,12,5)
B[6]=box('<div class="hub" data-el="vectorbox-hub"><div class="core">'+icon('layers')+'<b class="name">'+raw[6][5].text_content().strip()+'</b></div>'+''.join('<div class="spoke"><span class="mark">'+icon(m)+'</span><b class="name">'+txt(6,8+3*j)+'</b><p class="note">'+txt(6,9+3*j)+'</p></div>' for j,m in enumerate(['settings','clipboard-list','users-round','notebook-pen']))+'</div>',2,1,10,5)
t=copy.deepcopy(raw[7][4][0]);t.set('class','table')
for tr in t.xpath('.//tr'):
 if len(tr)>2:tr[2].set('class','pick')
B[7]=box('<div class="tablebox" data-el="vectorbox-table">'+etree.tostring(t,encoding='unicode',method='html')+'</div>',1,1,12,5)
B[8]=box(group([card('',m,txt(8,7+4*j),txt(8,8+4*j)) for j,m in enumerate(['lightbulb','receipt-text','chart-pie','badge-check'])]),1,1,12,5)
B[9]=box('<div class="steps" data-el="vectorbox-steps">'+''.join('<div class="step"><span class="mark">'+icon(m)+'</span><p class="name">'+txt(9,8+5*j if j<5 else 32)+'</p><p class="note">'+txt(9,9+5*j if j<5 else 33)+'</p></div>' for j,m in enumerate(['notebook-pen','search','layout-dashboard','monitor-cog','clipboard-check','rocket']))+'</div>',1,1,12,5)
# The six-sector source ring is kept as an explicit gap. One-share donuts are not overlaid.
budget=card('',name=txt(10,20),note=txt(10,21));e=html.fragment_fromstring(budget);e[0].append(html.fragment_fromstring('<span class="mark">'+icon('coins')+'</span>'));budget=etree.tostring(e,encoding='unicode',method='html')
B[10]='<!-- GAP 10-budget-ring: labeled segment list needed. -->'+box(card('',mark='coins'),3,2,2,2)+box(legend([txt(10,8+2*j) for j in range(6)],[1,3,4,None,5,2]),6,1,3,5)+box(budget,9,1,4,5)
B[11]=box('<div class="callout" data-el="vectorbox-callout">'+icon('message-square-text')+'<p>'+txt(11,8)+'</p></div>',2,1,10,4)+box(card('',mark='mic'),10,2,1,2);D[11]=''
e=html.fragment_fromstring(card('line',mark='contact-round',name=txt(12,8),note=txt(12,7),kick=txt(12,5)));e[0].append(e[0].find('p[@class="name"]'))
items=[('phone',10,11),('globe',14,15),('mail',18,19),('map-pinned',22,23),('printer',25,26)]
B[12]=box(etree.tostring(e,encoding='unicode',method='html'),1,1,3,5)+box('<div class="list divided" data-el="vectorbox-list">'+''.join('<div class="item"><span class="mark">'+icon(m)+'</span><p class="name">'+txt(12,a)+'</p><p class="note">'+txt(12,b)+'</p></div>' for m,a,b in items)+'</div>',5,1,8,5)

for n in range(2,14):
 head='<header class="head"><p class="kicker">'+txt(n,2)+'</p>'+(('<h1 class="title">'+txt(n,3)+'</h1>') if n!=13 else '')+('<p class="lead">'+txt(n,5)+'</p>' if n==3 else '')+'</header>'
 idx='' if n in [2,11,12,13] else '<div class="idx">'+''.join('<span class="no'+(' on' if j==n-3 else '')+'"></span>' for j in range(8))+'</div>'
 classes='page';body='<section class="slide"><div class="'+classes+'">'+head+'<div class="body">'+B.get(n,'')+'</div></div>'+idx+D.get(n,'')+'</section>'
 if n==13:
  body='<section class="slide cover"><div class="page"><div class="lockup at-top-left"><p class="kicker">'+txt(13,2)+'</p><h1 class="title"><b>'+txt(13,3)+'</b>'+txt(13,4)+'</h1><p class="lead">'+txt(13,5)+'</p></div><p class="meta">'+txt(13,11)+'</p><div class="deco"></div></div></section>'
 leaves=sorted(set(html.fromstring(body).xpath('//@data-el')));links=['../assets/fonts.css','../assets/type-steps.css','../vectorbox/kit/css/tokens.css','../assets/source-palette.css','../vectorbox/foundation/foundation.css']+['../vectorbox/elements/'+s.removeprefix('vectorbox-')+'/element.css' for s in leaves]
 out='<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Vectorbox v2 · '+f'{n:02}'+'</title>'+''.join('<link rel="stylesheet" href="'+s+'">' for s in links)+'</head><body>'+body+'<script src="../assets/lucide.min.js"></script><script src="../assets/render-icons.js"></script></body></html>'
 (O/f'slide_{n:02}.html').write_text(out)
print('Reassembled12 mapped pages; gaps02/04/10/11 kept explicit.')
