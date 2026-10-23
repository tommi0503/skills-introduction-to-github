from pathlib import Path
from bs4 import BeautifulSoup
R=Path('/workspace/work/deliverables/dockside/review/replica')
p=R/'replica.css';p.write_text(p.read_text()+'''\n/* Source measurements, reopened fidelity review. */
.title{font-size:60px;letter-spacing:-1.5px}.title b{color:#3299f4}.aside b{font-size:20px}.slide::before{display:none}.slide{background:radial-gradient(ellipse at 110% 95%,#e2f0fb,transparent 45%),radial-gradient(ellipse at 100% 3%,#f2f7ec,transparent 25%),#fafafa}.rail{border-left-width:17px;padding:0;display:block}.rail .seat{position:absolute;left:18px;width:50px;height:50px;border-radius:12px;overflow:visible}.rail:after{display:none}.rail .seat.on{width:72px;height:72px}.rail .seat.on::before{content:"";position:absolute;left:-20px;top:26px;width:16px;height:20px;clip-path:polygon(0 0,100% 50%,0 100%);background:#3299f4}.slide.cover{background:radial-gradient(ellipse at 50% 100%,#c8e4f5,transparent 65%),radial-gradient(ellipse at 100% 100%,#e9e4f8,transparent 45%),radial-gradient(ellipse at 0 100%,#e4efdc,transparent 45%),#fafafa}.cover-nav{left:75px;right:60px;top:38px;height:59px}.dock .seat.focus{width:126px;height:126px;margin-bottom:10px}.dock{left:38px;right:38px;bottom:36px}
''')
base=[20,99,179,257,336,415,493,572,652];activeTop=[9,87,166,245,324,403,482,561,640]
for n in range(1,31):
 p=R/f'slide_{n:02}.html';b=BeautifulSoup(p.read_text(),'html.parser')
 if b.select_one('.rail'):
  a=0 if n<=7 else 1 if n<=11 else 2 if n<=16 else 3 if n<=18 else 4 if n==19 else 5 if n<=23 else 6 if n<=26 else 7 if n<=28 else 8
  for j,q in enumerate(b.select('.rail>.seat')):q['class']=['seat']+(['on'] if j==a else []);q['style']=f'top:{activeTop[j] if j==a else base[j]}px'
 if n==1:
  q=b.select_one('.center');q['style']='left:180px;top:229px;width:920px;height:230px;position:absolute'
  ds=q.find_all('div',recursive=False);ds[0]['style']='font-size:80px;line-height:1.14;color:#3299f4;letter-spacing:-1.5px;font-weight:400';ds[1]['style']='font-size:100px;line-height:1.14;letter-spacing:-1.5px;font-weight:600'
 if n==5:
  boxes=b.select('.box')
  for q,x in zip(boxes,[445,845]):q['style']=f'left:{x}px;top:196px;width:362px;height:414px'
  ps=b.select('.pill:not(.dark)')
  for q,x in zip(ps,[477,877]):
   q['style']=f'position:absolute;left:{x}px;top:169px;width:300px;height:60px;font-size:22px;gap:12px'
   text=q.get_text().replace('✓','').strip();q.clear();q.append(BeautifulSoup('<span class="icon" data-icon="check" style="width:20px;height:20px"></span>','html.parser'));q.append(text)
  q=b.select_one('.bubble');q['style']='position:absolute;left:971px;top:279px;width:173px;height:173px;border-radius:50%;display:grid;place-items:center;background:linear-gradient(#3299f4,#e2f0fb);color:#fff';q.select_one('b')['style']='font-size:40px'
  q=b.select_one('.thin-circle');q['style']='position:absolute;left:903px;top:394px;width:106px;height:106px;border-radius:50%;background:linear-gradient(#ddd,#eee);border:0';q.clear();q.append(BeautifulSoup('<div style="font-size:16px;margin-top:21px">20XX</div><div style="font-size:28px">20%</div>','html.parser'))
  for x,y,w,rot in [(950,470,170,-50),(962,497,157,-50)]:
   b.select_one('.slide').append(BeautifulSoup(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;border-top:2px dashed #ddd;transform:rotate({rot}deg);transform-origin:left"></div>','html.parser'))
 if n==17:
  q=b.select_one('.solid-core');q['style']='position:absolute;left:559px;top:501px;width:278px;height:278px;border:24px solid #fafafa;border-radius:50%;background:#3299f4;color:#fff;display:grid;place-items:center'
  q=b.select_one('.thin-circle');q['style']='position:absolute;left:515px;top:457px;width:366px;height:366px;border:2px dashed #8ac2f4;background:none;border-radius:50%;box-shadow:none'
  b.select_one('.slide').append(BeautifulSoup('<div style="position:absolute;left:446px;top:388px;width:505px;height:505px;border:2px dashed #e2f0fb;border-radius:50%;pointer-events:none"></div>','html.parser'))
 if n==23:
  for q in b.select('.box'):q['style']=q.get('style','')+';padding-top:57px'
  for q in b.select('.box>.small'):q['style']='color:#48a0df;margin-top:0;font-size:16px'
 if n==30:
  for q in b.select('.center p'):q['style']=q.get('style','')+';margin:0'
 if not b.select_one('script[src="../assets/icons-runtime.js"]'):b.body.append(BeautifulSoup('<script src="../assets/icons-runtime.js"></script>','html.parser'))
 p.write_text(str(b))
