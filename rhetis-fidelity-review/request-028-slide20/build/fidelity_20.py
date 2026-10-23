"""Measured HTML reconstruction. No source bitmap is embedded."""
from pathlib import Path
import math,html
from ruled_backgrounds import trace
B=Path(__file__).resolve().parents[1];R=B/'review'
C='#5c6dbe';M='#9ea9d8';S='#ccd2f0';P='#efefef'
svg=['<svg class="decoration" viewBox="0 0 1280 720"><defs><linearGradient id="down"><stop stop-color="'+C+'"/><stop offset="1" stop-color="'+P+'"/></linearGradient></defs>']
# Ruled circular fans. The second is the first fan turned through 180 degrees.
for idx,(x,y,r,flip) in enumerate([(0,299,179,False),(179,470,179,True),(0,482,179,False),(0,660,179,False),(179,648,179,True),(358,633,179,False)]):
 svg.append(f'<defs><linearGradient id="fade{idx}" gradientUnits="userSpaceOnUse" x1="0" y1="{y}" x2="0" y2="{y+r}"><stop stop-color="{P if flip else C}"/><stop offset="1" stop-color="{C if flip else P}"/></linearGradient></defs>')
 for j in range(0,180,4):
  hh=math.sqrt(max(0,r*r-j*j))
  if flip:a,b=y,y+math.sqrt(max(0,r*r-(r-j)*(r-j)));xx=x+j
  else:a,b=y+r-hh,y+r;xx=x+j
  svg.append(f'<path d="M{xx:.2f} {a:.2f}V{b:.2f}" fill="none" stroke="url(#fade{idx})" stroke-width="2.25"/>')
svg.append('</svg>')
def text(t,x,y,w,h,fs,weight=400,c='#000'):
 return f'<span class="ink" data-x="{x}" data-y="{y}" data-w="{w}" data-h="{h}" style="font-size:{fs}px;font-weight:{weight};color:{c}">{html.escape(t)}</span>'
t=[]
# Coordinates are visible ink boundaries, not CSS line boxes.
for args in [('Seeking a $5M seed',51,51,402,48,46.08),('to accelerate R&D',50,111,367,33,46.08),('and global expansion.',51,167,438,43,46.08),('Request',1183,44,47,12,12,400,C),('This capital injection will be pivotal in',49,238,240,13,14),('finalizing our regulatory approvals',49.5,261,221.5,13,14),('and scaling our engineering team.',49.5,284,220,13,14)]:t.append(text(*args))
for args in [('40%',444,348,55,20,28,500,C),('R&D',455,381,33,13,18,400,C),('30%',633,392,53,20,28,500,'#fff'),('Ops',644,424,32,17,18,400,'#fff'),('30%',499,512,52,19,28,500),('Sales',503,544,44,13,18)]:t.append(text(*args))
for args in [('$5,000,000 Seed Round Investment',808.5,217,305.5,17.5,18,600,'#fff'),('40% R&D: Product Acceleration',808.5,288,215.5,14,14,500,C),("Fast-tracking the 'Multi-Modality Engine' to unify Cardiac and",809,320,303,10,11,400,C),('Pulmonary diagnostics in a seamless single-scan workflow.',809,336,303,10,11,400,C),('30% Sales: Commercial Expansion',808.5,416,236,14,14,500),('Scaling the direct sales organization to capture Tier-1 IDNs and',809,449,314,10,11),('drive nationwide market penetration.',809,465,177,10,11),('30% Ops: Regulatory & Growth',808.5,544,210,14,14,500,'#fff'),('Funding primary market regulatory milestones and aggressive',809,578,309,10,11,400,'#fff'),('talent acquisition for the Go-to-Market leadership team.',809,594,268,10,11,400,'#fff'),('20',1216,665,14,9,12)]:t.append(text(*args))
css=f'''@import url('../assets/fonts.css');*{{box-sizing:border-box}}html,body{{margin:0;width:1280px;height:720px}}.slide{{position:relative;width:1280px;height:720px;overflow:hidden;background:{P};font-family:'Pretendard Variable';}}.decoration{{position:absolute;inset:0;width:100%;height:100%}}.pie{{position:absolute;left:358px;top:237px;width:400px;height:400px;border-radius:50%;background:conic-gradient({C} 0 40%,{M} 40% 70%,{S} 70% 100%)}}.investment{{position:absolute;left:776px;top:211px;width:375px;height:30px;border-radius:0 34px 0 34px;background:{C}}}.rule{{position:absolute;left:794.5px;top:241px;height:479px;border-left:1px solid #555}}.panel{{position:absolute;left:795px;width:356px;height:108px}}.ink{{position:absolute;white-space:pre;line-height:1;}}'''
script='''document.fonts.ready.then(()=>{let ctx=document.createElement('canvas').getContext('2d');for(let e of document.querySelectorAll('.ink')){let s=getComputedStyle(e),f=parseFloat(s.fontSize),w=+e.dataset.w,h=+e.dataset.h;ctx.font=`${s.fontWeight} ${f}px 'Pretendard Variable'`;let m=ctx.measureText(e.textContent);f*=h/(m.actualBoundingBoxAscent+m.actualBoundingBoxDescent);e.style.fontSize=f+'px';ctx.font=`${s.fontWeight} ${f}px 'Pretendard Variable'`;m=ctx.measureText(e.textContent);let track=(w-m.actualBoundingBoxLeft-m.actualBoundingBoxRight)/Math.max(1,e.textContent.length-1);e.style.letterSpacing=track+'px';let baseline=(f-m.fontBoundingBoxAscent-m.fontBoundingBoxDescent)/2+m.fontBoundingBoxAscent;e.style.left=(+e.dataset.x+m.actualBoundingBoxLeft)+'px';e.style.top=(+e.dataset.y+m.actualBoundingBoxAscent-baseline)+'px'}document.body.dataset.ready='1'});'''
doc='<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Lamella — Request faithful replica</title><style>'+css+'</style></head><body><section class="slide">'+trace(20)[0]+'<div class="pie"></div><div class="rule"></div><div class="investment"></div>'+''.join(f'<div class="panel" style="top:{y}px;background:{c}"></div>' for y,c in [(262,S),(390,M),(518,C)])+''.join(t)+'</section><script>'+script+'</script></body></html>'
(R/'replica/slide_20.html').write_text(doc)
print('page20 rebuilt from measured primitives and complete source copy')
