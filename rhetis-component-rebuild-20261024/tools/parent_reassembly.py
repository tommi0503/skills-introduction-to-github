"""New semantic reassembly. Frozen replica DOM supplies content only; no source CSS is copied."""
from pathlib import Path
import shutil
import sys,json,html,re
from playwright.sync_api import sync_playwright
sys.path.insert(0,str(Path(__file__).parent))
from size_review import browser,serve_url,assets,stylesheet,BASE,OLD
B=BASE

def esc(t):return html.escape(t)
def el(n,leaf,root,content,cls='',col=1,wide=12,row=1,high=6,data=''):
 return f'<div class="{root} {cls}" data-el="{n}-{leaf}" style="grid-column:{col} / span {wide};grid-row:{row} / span {high}{data}">{content}</div>'
def raw(page,sel,i=0):
 return page.locator(sel).nth(i).evaluate('e=>e.innerHTML.replace(/ style="[^"]*"/g,"").replace(/ class="[^"]*"/g,"")')
def txt(page,sel,i=0):return page.locator(sel).nth(i).inner_text()
def top(page):
 vs=page.locator('.top span').all_text_contents();return '<header class="top"><span class="deck">'+esc(vs[0])+'</span><span class="sec">'+esc(vs[1])+'</span><span class="src">'+esc(vs[2])+'</span></header>'
def head(n,page):
 return '<p class="kick">'+raw(page,'.eyebrow')+'</p><h2>'+raw(page,'.heading')+'</h2>'
def paragraph(n,content,cls='',**kw):return el(n,'prose','prose','<p>'+content+'</p>',cls,**kw)
def frame(n,**kw):return el(n,'image-frame','frame','<div class="seat" data-ph="1"></div>',**kw)
def body(x):return '<div class="body">'+x+'</div>'
def afterglow(page,pp):
 n='afterglow';f=top(page);x='';outer='slide';pagecontent=''
 if pp=='01':
  t=raw(page,'.slide>div:nth-of-type(1)');f+='<header class="head"><h1 class="title">'+t+'</h1></header>'
  x+=paragraph(n,raw(page,'.slide>h2'),'lead',col=5,wide=3,row=1,high=3)
  x+=paragraph(n,raw(page,'.slide>p'),'quiet',col=8,wide=5,row=1,high=3)
 elif pp=='02':
  a=page.locator('.slide>div').first
  texts=['Contents','목차'];outer+=' on'
  # The source section head is furniture, not a second agenda design.
  f+='<header class="head"><h1 class="title">'+esc(texts[0])+'</h1><p class="lead">'+esc(texts[1])+'</p></header>'
  entries=page.locator('.slide>div[style*="border-radius:50%"]');s=''
  for e in entries.all():
   ch=e.locator('span').all_text_contents();s+='<div class="entry"><span class="name">'+esc(ch[0])+'</span><span class="note">'+esc(ch[-1])+'</span></div>'
  x+=el(n,'agenda','agenda',s,col=2,wide=10,row=3,high=3)
 elif pp=='03':
  outer+=' on';f+='<header class="head"><h1 class="title"></h1><p class="lead">'+raw(page,'.slide>div:nth-of-type(2)')+'</p></header>'
  x+='<!-- GAP: source176px Service and circular action have no matching permitted contract. -->'
  copy=paragraph(n,raw(page,'.slide>div:nth-of-type(4)>p'),'quiet')
  s=''.join('<div class="item"><span class="name">'+esc(t)+'</span></div>'for t in page.locator('li').all_text_contents())
  x+='<div class="stack" style="grid-column:9 / span 4;grid-row:5 / span 2">'+copy+el(n,'list','list',s,'check')+'</div>'
 elif pp in ['04','05','06','07','08']:
  x+=el(n,'headline','headline',head(n,page),wide=6,high=2)
  if pp in ['04','06']:
   s='<div class="item"><span class="mark"><span class="icon" data-icon="chevron-right"></span></span><span class="name">'+raw(page,'.bullet h3')+'</span><span class="note">'+raw(page,'.bullet p')+'</span></div>'
   x+=el(n,'list','list',s,wide=5,row=3,high=2)
   if pp=='04':x+=frame(n,col=7,wide=6,row=1,high=6)
   else:
    s='<div class="series tone-1"><span class="name"></span>'+''.join('<div class="pt" style="--v:'+str(v)+'"></div>'for v in[54.68,57.97,62.28,69.62,80.25,100])+'</div><div class="axis">'+''.join('<span></span>'for _ in range(6))+'</div>'
    x+=el(n,'chart-area','areas',s,row=2,high=5,data=';--max:100')
    x+='<!-- GAP: 140px figure and non-data arrow ornament omitted; see GAPS.md. -->'
  elif pp=='05':
   s=''
   for i,e in enumerate(page.locator('.service-card').all(),1):s+='<div class="card" data-el="afterglow-card"><div class="parts"><div class="mark"><div class="seat" data-ph="'+str(i)+'"></div></div><div class="kick">'+str(i)+'</div><div class="name">'+e.locator('h3').inner_text()+'</div><div class="note">'+e.locator('p').inner_html()+'</div></div></div>'
   x+='<div class="group" style="grid-column:1 / span 12;grid-row:3 / span 4">'+s+'</div>'
  elif pp=='07':
   x+=frame(n,col=4,wide=6,row=2,high=5)
   for i,e in enumerate(page.locator('.process').all()):
    c=1 if i%2==0 else 10;r=3 if i<2 else 5
    s=el(n,'tag','tag',e.locator('h3').inner_html(),high=1)
    s+=paragraph(n,e.locator('p').inner_html(),'quiet',row=2,high=5)
    x+='<div class="stack" style="grid-column:'+str(c)+' / span 3;grid-row:'+str(r)+' / span 2">'+s+'</div>'
   x+='<!-- GAP: independent upper pair horizontal rules omitted. -->'
  elif pp=='08':
   x+=paragraph(n,raw(page,'.content>p.bodycopy'),col=1,wide=5,row=3,high=3)
   s=''
   for i,e in enumerate(page.locator('.how-card').all()):s+='<div class="step"><div class="mark"><span class="icon" data-icon="'+['lock-keyhole','key-round','shield-check'][i]+'"></span></div><div class="name">'+e.locator('h3').inner_html()+'</div><div class="note">'+e.locator('p').inner_html()+'</div></div>'
   x+=el(n,'steps','steps',s,'col',col=6,wide=7,row=1,high=6)
 elif pp=='09':
  x+=el(n,'headline','headline','<h2>'+raw(page,'.slide>h1')+'</h2>','center',row=1,high=2)
  x+='<!-- GAP: closing centered16px body paragraph lacks a semantic prose.center modifier; see map. -->'
  # Closing contact details are page metadata and stay in the foundation.
  f+='<footer class="foot"><span class="src">'+raw(page,'.slide>div:last-of-type')+'</span></footer>'
 return '<section class="'+outer+'"><div class="page">'+f+body(x)+'</div></section>'

def confluence(page,pp):
 n='confluence';f='';x='';outer='slide'
 if pp=='01':
  outer+=' cover';box=page.locator('.slide>div:last-of-type')
  hs=box.locator('h1').inner_text().split('\n')
  f='<div class="seat portrait" data-ph="1"></div><div class="seat logo" data-ph="2"></div><div class="lockup at-top-left"><p class="kicker">'+box.locator('p').nth(0).inner_html()+'</p><p class="lead">'+box.locator('h2').inner_html()+'</p><h1 class="title"><b>산학<b>협력</b></b><br>제안서</h1><span class="label">'+box.locator('p').nth(1).inner_html()+'</span><span class="src">'+box.locator('p').nth(2).inner_html()+'</span></div>'
  return '<section class="'+outer+'"><div class="page">'+f+'</div></section>'
 if pp=='02':
  f='<header class="head center"><div class="seat portrait" data-ph="1"></div><h1 class="title">목차<b>보기</b></h1><p class="kicker">TABLE OF INDEX</p></header>'
  s=''
  for i,e in enumerate(page.locator('.card').all(),1):s+='<div class="entry"><span class="mark">'+f'{i:02}'+'</span><span class="name">'+e.locator('h2').inner_html()+'</span><span class="note">'+e.locator('p').inner_html()+'</span></div>'
  x=el(n,'agenda','agenda',s)
 elif pp=='03':
  f='<aside class="rail"><div class="seat portrait" data-ph="1"></div><h1 class="title">프로젝트<br><b>개요</b></h1><p class="kicker">PROJECT OUTLINE</p><p class="lead">'+raw(page,'.slide>div:nth-of-type(2) p',1)+'</p></aside>'
  s=''
  for e in page.locator('.card').all()[1:]:
   ps=e.locator('p').all();vals=[v.inner_html()for v in ps]
   notes=''.join('<p><b>'+vals[i]+'</b>'+vals[i+1]+'</p>'for i in range(2,len(vals)-1,2)if re.sub('<[^>]*>','',vals[i]+vals[i+1]).strip())
   s+='<div class="card" data-el="confluence-card"><div class="parts"><div class="kick">'+e.locator('div').nth(0).inner_html()+'</div><div class="name">'+vals[0]+'</div><div class="fig">'+vals[1]+'</div><div class="note">'+notes+'</div></div></div>'
  x='<!-- GAP: blue label/value band at top has no matching contract. -->'+'<div class="group" style="grid-column:1 / span 12;grid-row:2 / span 5">'+s+'</div>'
 elif pp=='04':
  # Only semantic parts are retained; every connector is drawn by hub CSS.
  e=page.locator('.slide>div[style*="width:367px"]');core='<div class="core"><div class="mark"><div class="seat" data-ph="1"></div></div><div class="name">프로젝트<br><b>목표</b></div><div class="kick">PROJECT GOAL</div><div class="note">'+e.locator('p').nth(1).inner_html()+'</div></div>'
  s=''
  for i,e in enumerate(page.locator('.goal').all()):
   name=re.sub(r'<span[^>]*>','<b>',e.locator('h2').inner_html()).replace('</span>','</b>');name=re.sub(r' class="[^"]*"','',name)
   s+='<div class="spoke"><div class="mark"><span class="icon" data-icon="'+['chart-no-axes-combined','messages-square','mail-open','arrow-down-up'][i]+'"></span></div><div class="name">'+name+'</div><div class="note">'+e.locator('p').inner_html()+'</div></div>'
  x=el(n,'hub','hub',core+s)
 return '<section class="'+outer+'"><div class="page">'+f+body(x)+'</div></section>'

with sync_playwright() as pw:
 b=browser(pw)
 for n,count,fn in [('afterglow',9,afterglow),('confluence',4,confluence)]:
  assets(n);shutil.copy('/workspace/work/tools/icons-runtime.js',B/n/'review/assets/icons-runtime.js');out=B/n/'review/reassembled';out.mkdir(exist_ok=True);c=B/n/'collection'/n
  # This host only loads the supplied source palette, type steps and collection styles. It contains no page layout rules.
  (out/'library.css').write_text(stylesheet(c,host=True))
  for num in range(1,count+1):
   pp=f'{num:02}';p=b.new_page(viewport={'width':1280,'height':720});p.goto(serve_url(OLD/n/'review/replica'/('slide_'+pp+'.html')));p.evaluate('document.fonts.ready');content=fn(p,pp);p.close()
   doc='<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>'+n+' '+pp+' / rebuilt contracts</title><link rel="stylesheet" href="../assets/fonts/fonts.css"><link rel="stylesheet" href="library.css"></head><body style="margin:0">'+content+'<script src="../assets/icons-runtime.js"></script></body></html>'
   (out/('slide_'+pp+'.html')).write_text(doc)
  print(n,count,'new semantic pages')
 b.close()
