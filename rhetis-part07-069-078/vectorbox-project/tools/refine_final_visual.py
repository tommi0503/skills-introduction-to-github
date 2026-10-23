"""Final visual corrections only; leaves fixtures and integrated runtime untouched."""
from pathlib import Path
P=Path(__file__).parent/'vectorbox'
START='/* Final visual review corrections. */'
def add(n,s):
 p=P/'elements'/n/'element.css'
 old=p.read_text().split(START)[0].rstrip()
 p.write_text(old+'\n'+START+'\n'+s.replace('R',f'[data-el="vectorbox-{n}"]')+'\n')

add('chart-line','R .pt b{color:var(--ink)}')
stack='''R .sbar.on{background:none;color:var(--ink)}R .sbar>span{color:var(--ink)}R .seg{position:relative;container-type:inline-size}R.h .seg>b{position:relative;white-space:nowrap}R.h .seg:nth-of-type(2n)>b{z-index:2}@container(max-width:40px){R.h .seg>b{position:absolute;bottom:calc(100% + var(--gap-sm));font-size:var(--type-12);color:var(--ink)}R.h .seg:nth-of-type(2n)>b{bottom:auto;top:calc(100% + var(--gap-sm))}}'''
for i in range(1,5):
 stack+=f'R .seg.tone-{i}'+'{background:var(--a'+str(i)+');color:var(--a'+str(i)+'-on)}'
add('chart-stack',stack)
add('concentric','''R:has(>.ring:nth-child(4))>.ring:nth-child(3){justify-content:flex-start;padding-top:var(--gap-sm);gap:calc(var(--stroke)*4)}R:has(>.ring:nth-child(4))>.ring:nth-child(3) .name{font-size:var(--type-20)}R:has(>.ring:nth-child(4))>.ring:nth-child(3) .fig{font-size:var(--type-28)}''')
cycle=''
for n in range(3,7):
 for i in range(n):
  cycle+=f'R:has(>.node:nth-of-type({n+1}):last-child)>.node:nth-of-type({i+2}):after'+'{transform:rotate('+str(45+360*i/n)+'deg)}'
add('cycle',cycle)
add('funnel','''R .stage{position:relative;isolation:isolate;clip-path:none;border:0;background:none;padding:calc(var(--stroke)*4) clamp(var(--gap-sm),calc(var(--v)*.06%),calc(var(--pad)*1.5));container-type:inline-size}R .stage:first-child{background:none}R .stage:before{content:'';position:absolute;inset:0;z-index:-1;background:var(--n-2);clip-path:polygon(0 0,100% 0,94% 100%,6% 100%)}R .stage:first-child:before{background:var(--a1)}R .stage .name,R .stage .fig{white-space:nowrap}R .stage .fig{font-size:var(--type-28)}@container(max-width:320px){R .stage .name{font-size:var(--type-18)}R .stage .fig{font-size:var(--type-22)}}@container(max-width:230px){R .stage .name{font-size:var(--type-14)}R .stage .fig{font-size:var(--type-16)}}''')
journey='''R{transform:translate(0);anchor-scope:all}R .stage{container-type:normal}R .stage:nth-child(n):after,R .stage>.name:before{content:'';position:fixed;width:auto;height:auto;transform:none;pointer-events:none}R .stage:first-child:after,R .stage:first-child>.name:before{display:none}'''
for i in range(1,10):
 journey+=f'R .stage:nth-child({i}):before'+'{anchor-name:--vectorbox-journey-'+str(i)+'}'
 if i>1:
  x=f'left:anchor(--vectorbox-journey-{i-1} center);right:anchor(--vectorbox-journey-{i} center);'
  for pseudo,top,bot,dr in [(':after',i,i-1,'bottom'),('>.name:before',i-1,i,'top')]:
   journey+=f'R .stage:nth-child({i})'+pseudo+'{'+x+f'top:calc(anchor(--vectorbox-journey-{top} center) - 1px);bottom:calc(anchor(--vectorbox-journey-{bot} center) - 1px);background:linear-gradient(to {dr} right,transparent calc(50% - 1px),var(--a1) calc(50% - 1px) calc(50% + 1px),transparent calc(50% + 1px))'+'}'
add('journey',journey)
add('network','''R .link{width:hypot(calc((var(--x2) - var(--x1))*.008*100cqw),calc((var(--y2) - var(--y1))*.008*100cqh));transform:rotate(atan2(calc((var(--y2) - var(--y1))*.008*100cqh),calc((var(--x2) - var(--x1))*.008*100cqw)))}''')
mind='''R{transform:translate(0);isolation:isolate}R .core{anchor-name:--vectorbox-map-core}R .branch:before{position:fixed;content:'';background:none;width:auto;height:auto;border:0;z-index:-1}'''
for i in range(2,8):
 left=i%2==0;row=(i-2)//2
 mind+=f'R>.branch:nth-child({i})'+'{anchor-name:--vectorbox-map-'+str(i)+'}'
 a=f'anchor(--vectorbox-map-{i} center)';c='anchor(--vectorbox-map-core center)'
 x=('left:anchor(--vectorbox-map-'+str(i)+' right);right:anchor(--vectorbox-map-core left);') if left else ('left:anchor(--vectorbox-map-core right);right:anchor(--vectorbox-map-'+str(i)+' left);')
 if row==0:
  edge='right' if left else 'left';s=x+f'top:{a};bottom:{c};border-top:1px solid var(--n-4);border-{edge}:1px solid var(--n-4);border-top-{edge}-radius:var(--gap);'
 elif row==1:s=x+f'top:{c};bottom:auto;height:0;border-top:1px solid var(--n-4);'
 else:
  edge='right' if left else 'left';s=x+f'top:{c};bottom:{a};border-bottom:1px solid var(--n-4);border-{edge}:1px solid var(--n-4);border-bottom-{edge}-radius:var(--gap);'
 mind+=f'R>.branch:nth-child({i}):before'+'{'+s+'}'
add('mindmap',mind)
add('pyramid','''R .level{position:relative;isolation:isolate;clip-path:none;border:0;background:none;gap:calc(var(--stroke)*4);padding:calc(var(--stroke)*4) var(--gap-sm)}R .level:first-child{clip-path:none;background:none;padding-top:var(--gap-lg)}R .level:before{content:'';position:absolute;inset:0;z-index:-1;background:var(--n-2);clip-path:polygon(12% 0,88% 0,100% 100%,0 100%)}R .level:first-child:before{background:var(--a1);clip-path:polygon(50% 0,100% 100%,0 100%)}R .level .note{max-width:85%;font-size:var(--type-16);text-align:center}R .level:first-child .note{max-width:70%}R .level:first-child .name{font-size:var(--type-22);text-align:center;max-width:90%}@container(max-height:360px){R .level .note{font-size:var(--type-12)}R .level .name,R .level:first-child .name{font-size:var(--type-16)}R .level:first-child{padding-top:var(--gap-sm)}}''')
add('tag','''R.tag,R.hl{container-type:normal;white-space:nowrap;flex:none}''')
add('pricing','''R .plan>.tag,R.plan>.tag{min-width:calc(var(--gap-lg)*2);min-height:var(--gap-lg);white-space:nowrap;justify-content:center;text-align:center;flex:none}''')
add('radar','''R>.series:nth-of-type(n){background:none;border:0;clip-path:none;transform:none;left:calc(50% - min(28cqw,32cqh));top:calc(50% - min(28cqw,32cqh));width:min(56cqw,64cqh);height:min(56cqw,64cqh)}R:before{inset:auto;left:calc(50% - min(28cqw,32cqh));top:calc(50% - min(28cqw,32cqh));width:min(56cqw,64cqh);height:min(56cqw,64cqh)}R:after{inset:auto;left:calc(50% - min(14cqw,16cqh));top:calc(50% - min(14cqw,16cqh));width:min(28cqw,32cqh);height:min(28cqw,32cqh)}R>.series>.name{color:var(--ink)}''')
add('roadmap','''R .bar{width:calc((var(--to) - var(--from))/var(--cols)*100%)}''')
add('sankey','''R{display:flex;flex-direction:column;gap:var(--gap-sm);padding:var(--gap) var(--gap) var(--gap) calc(50% + var(--gap));isolation:isolate}R .source{position:absolute;left:var(--gap);top:var(--gap);bottom:var(--gap);width:28%;height:auto}R>.branch{flex:var(--v);min-height:0;display:grid;grid-template-columns:1fr auto;align-items:center;gap:var(--gap-sm);padding:calc(var(--stroke)*4) var(--gap-sm);color:var(--ink)}R>.branch.on{color:var(--a1-on)}R .branch:before{width:calc(44cqw + .88*var(--gap))}R>.branch:has(>.branch){display:flex;flex-direction:column;gap:calc(var(--stroke)*4);padding-left:18cqw;align-items:stretch;justify-content:stretch}R>.branch:has(>.branch)>.name{position:absolute;left:var(--gap-sm);top:var(--gap-sm);max-width:16cqw}R>.branch:has(>.branch)>.fig{position:absolute;left:var(--gap-sm);top:var(--gap-lg);max-width:16cqw}R>.branch>.branch{flex:var(--v);min-height:0;position:relative;display:grid;grid-template-columns:1fr auto;align-items:center;gap:calc(var(--stroke)*4);padding:calc(var(--stroke)*2);margin:0;background:var(--page);color:var(--ink);border:1px solid var(--n-4)}R>.branch>.branch .name{font-size:var(--type-18)}R>.branch>.branch .fig{font-size:var(--type-20)}R>.branch>.branch:before{width:calc(18cqw - var(--gap-sm));background:var(--a1-3-soft)}@container(max-height:340px){R .branch .name{font-size:var(--type-14)}R .branch .fig{font-size:var(--type-16)}R>.branch{padding:calc(var(--stroke)*2) var(--gap-sm)}}''')
slope='''R .pair:before{width:calc(abs(var(--b) - var(--a))/var(--max)*100%)}R:not(.dumbbell) .pair{position:absolute;inset:var(--gap-lg);height:auto;margin:0;container-type:size}R:not(.dumbbell) .pair:before{left:25%;top:calc((1 - var(--a)/var(--max))*100%);width:hypot(60cqw,calc((var(--a) - var(--b))/var(--max)*100cqh));transform:rotate(atan2(calc((var(--a) - var(--b))/var(--max)*100cqh),60cqw));transform-origin:left center}R:not(.dumbbell) .pair>.name{right:auto;left:0;width:18%;top:calc((1 - var(--a)/var(--max))*100%);color:var(--ink)}R:not(.dumbbell) .pair>.a{left:25%;top:calc((1 - var(--a)/var(--max))*100%);color:var(--ink)}R:not(.dumbbell) .pair>.b{left:85%;top:calc((1 - var(--b)/var(--max))*100%)}R:not(.dumbbell) .heads{left:25%;right:15%}R.dumbbell .pair>.a,R.dumbbell .pair>.b{width:auto;height:auto;min-width:0;border:0;background:none;color:var(--ink);line-height:var(--label-line)}R.dumbbell .pair>.a{transform:translate(-50%,calc(-100% - var(--gap-sm)))}R.dumbbell .pair>.b{transform:translate(-50%,var(--gap-sm))}R.dumbbell .pair>.a:before,R.dumbbell .pair>.b:before{content:'';position:absolute;left:50%;width:8px;height:8px;border-radius:999px;transform:translate(-50%,-50%);border:1px solid var(--n-5);background:var(--page)}R.dumbbell .pair>.a:before{top:calc(100% + var(--gap-sm))}R.dumbbell .pair>.b:before{top:calc(-1*var(--gap-sm));border-color:var(--a1);background:var(--a1)}@container(max-height:340px){R.dumbbell .pair>.a{font-size:var(--type-12);transform:translate(-50%,calc(-100% - 4*var(--stroke)))}R.dumbbell .pair>.b{font-size:var(--type-12);transform:translate(-50%,calc(4*var(--stroke)))}R.dumbbell .pair>.a:before{top:calc(100% + 4*var(--stroke))}R.dumbbell .pair>.b:before{top:calc(-4*var(--stroke))}}'''
add('slope',slope)
spark='''R:not(.bars){display:block;transform:translate(0);anchor-scope:all;border:0;color:var(--a1)}R.up{color:var(--good)}R.down{color:var(--bad)}R:not(.bars)>span{position:absolute;width:0;height:0;border:0;background:none;bottom:calc(var(--gap-sm) + var(--v)/var(--max)*(100% - 2*var(--gap-sm)))}R:not(.bars)>span:before,R:not(.bars)>span:after{content:'';position:fixed;pointer-events:none}R:not(.bars)>span:first-child:before,R:not(.bars)>span:first-child:after{display:none}R:where(.parts>*){width:160px;height:48px;flex:none}'''
for n in range(3,25):
 for i in range(1,n+1):
  q=f'R:not(.bars):has(>span:nth-child({n}):last-child)>span:nth-child({i})'
  spark+=q+'{left:'+f'{5+90*(i-1)/(n-1):.5f}'+'%;anchor-name:--vectorbox-spark-'+str(i)+'}'
  if i>1:
   x=f'left:anchor(--vectorbox-spark-{i-1} center);right:anchor(--vectorbox-spark-{i} center);'
   for pseudo,top,bot,dr in [('before',i,i-1,'bottom'),('after',i-1,i,'top')]:
    spark+=q+':'+pseudo+'{'+x+f'top:calc(anchor(--vectorbox-spark-{top} center) - 1px);bottom:calc(anchor(--vectorbox-spark-{bot} center) - 1px);background:linear-gradient(to {dr} right,transparent calc(50% - 1px),currentColor calc(50% - 1px) calc(50% + 1px),transparent calc(50% + 1px))'+'}'
add('sparkline',spark)
add('image-frame','''R.frame{width:100%;height:100%;border-radius:var(--radius);background:var(--page)}''')
add('versus','''R .side>.list{container-type:normal;flex:none;height:auto;min-height:max-content}''')
add('venn','''R:has(>.set:nth-child(3)){display:block}R:has(>.set:nth-child(3))>.set{position:absolute;margin:0;height:min(52cqw,66cqh);width:min(52cqw,66cqh);max-width:none;transform:translate(-50%,-50%)}R:has(>.set:nth-child(3))>.set:nth-child(1){left:42%;top:35%;justify-content:flex-start;padding-top:var(--gap-lg)}R:has(>.set:nth-child(3))>.set:nth-child(2){left:58%;top:35%;justify-content:flex-start;padding-top:var(--gap-lg)}R:has(>.set:nth-child(3))>.set:nth-child(3){left:50%;top:63%;justify-content:flex-end;padding-bottom:var(--gap-lg)}R:has(>.set:nth-child(3))>.core{left:40%;right:40%;top:48%;background:var(--page);z-index:3}''')
add('waffle','''R.figures{grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;min-height:0;padding:calc(var(--stroke)*4);gap:0 var(--gap-sm)}R.figures .units{width:100%;height:min(70%,72px);aspect-ratio:auto;grid-template-columns:repeat(10,minmax(0,1fr));grid-template-rows:minmax(0,1fr);align-self:center}R.figures .u{width:min(100%,24px);height:100%;justify-self:center;aspect-ratio:1/3}R.figures .name small{display:block;font-size:var(--type-12)}@container(max-height:160px){R.figures .fig{font-size:var(--type-20)}R.figures .name{font-size:var(--type-14)}R.figures .units{height:min(80%,36px)}}''')
add('balance','''R .pan:first-child{transform:translateY(calc(-1*var(--tilt)*.04cqw))}R .pan:nth-child(2){transform:translateY(calc(var(--tilt)*.04cqw))}''')
add('bullet','''R.bullet:after,R .bullet:after{top:calc(44% - 8px);height:32px}''')
add('person','''@container(max-height:340px){R .person,R.person{gap:calc(var(--stroke)*4);padding:calc(var(--stroke)*4)}R .seat{width:80px;height:80px;max-height:38%}R .seat.portrait{width:64px;height:80px}R .name{font-size:var(--type-20)}R .note{font-size:var(--type-16)}}''')
add('quote','''R .by{flex:none}R .by:not(:has(>.seat)){grid-template-columns:max-content 1fr}@container(max-height:340px){R{gap:var(--gap-sm);padding:var(--gap-sm)}R blockquote{font-size:var(--type-24)}R blockquote:before{font-size:var(--type-36)}R .by{grid-template-columns:48px 1fr}R .seat{width:48px;height:48px}R .by .name{font-size:var(--type-18)}R .by .note{font-size:var(--type-14)}}''')
add('callout','''R:where(.stack>*){padding:var(--gap-sm)}''')
def extend(n,s):
 p=P/'elements'/n/'element.css';p.write_text(p.read_text()+s.replace('R',f'[data-el="vectorbox-{n}"]')+'\n')
extend('waffle','''@container(max-height:60px){R.figures{grid-template-columns:1fr 64px 1fr;grid-template-rows:minmax(0,1fr);padding:0;gap:0 var(--gap-sm)}R.figures .units{grid-row:1;grid-column:1;max-height:100%;height:18px;align-self:center}R.figures .fig{grid-column:2;grid-row:1;align-self:center;font-size:var(--type-16)}R.figures .name{grid-column:3;grid-row:1;align-self:center;font-size:var(--type-12);line-height:var(--figure-line)}R.figures .name small{font-size:var(--type-10);line-height:var(--figure-line)}}''')
extend('slope','''R:not(.dumbbell) .pair:nth-child(n)>.a,R:not(.dumbbell) .pair:nth-child(n)>.b{width:auto;height:auto;border:0;background:none;display:block;color:var(--ink);font-size:var(--type-16);line-height:var(--label-line)}R:not(.dumbbell) .pair:nth-child(2n)>.a,R:not(.dumbbell) .pair:nth-child(2n)>.b{transform:translate(-50%,calc(-100% - 4*var(--stroke)))}R:not(.dumbbell) .pair:nth-child(2n+1)>.a,R:not(.dumbbell) .pair:nth-child(2n+1)>.b{transform:translate(-50%,calc(4*var(--stroke)))}R:not(.dumbbell) .pair:nth-child(2n)>.name{transform:translateY(calc(-100% - 4*var(--stroke)))}R:not(.dumbbell) .pair:nth-child(2n+1)>.name{transform:translateY(calc(4*var(--stroke)))}R:not(.dumbbell) .pair>.a:before,R:not(.dumbbell) .pair>.b:before{content:'';position:absolute;left:50%;width:8px;height:8px;border-radius:999px;transform:translate(-50%,-50%);background:var(--page);border:1px solid var(--n-5)}R:not(.dumbbell) .pair>.b:before{background:var(--a1);border-color:var(--a1)}R:not(.dumbbell) .pair:nth-child(2n)>.a:before,R:not(.dumbbell) .pair:nth-child(2n)>.b:before{top:calc(100% + 4*var(--stroke))}R:not(.dumbbell) .pair:nth-child(2n+1)>.a:before,R:not(.dumbbell) .pair:nth-child(2n+1)>.b:before{top:calc(-4*var(--stroke))}''')
extend('sankey','''R>.branch:has(>.branch){padding-left:24cqw}R>.branch:has(>.branch)>.name,R>.branch:has(>.branch)>.fig{max-width:calc(24cqw - 2*var(--gap-sm))}R>.branch>.branch:before{width:calc(24cqw - var(--gap-sm))}@container(max-width:400px){R>.branch:has(>.branch)>.fig{font-size:var(--type-20)}}''')
for i in range(1,5):
 extend('radar',f'R>.series.tone-{i}:nth-of-type(n):before'+'{background:color-mix(in srgb,var(--a'+str(i)+') 28%,transparent);border-color:var(--a'+str(i)+')}')
 extend('chart-area',f'R>.series.tone-{i}:nth-of-type(n):has(>.pt:nth-child(n of .pt):last-child)>.pt:nth-child(n of .pt):before'+'{background:var(--a'+str(i)+'-3-soft)}')
# Bare fixture seats have no data-el; foundation owns their shape.
f=P/'foundation'/'foundation.css'
s=f.read_text().split(START)[0].rstrip()
f.write_text(s+'\n'+START+'\n.slide .stack:has(>[data-el="vectorbox-callout"]){container-type:size}.slide .stack:has(>[data-el="vectorbox-callout"])>.seat{flex:none;align-self:center;width:min(128px,30cqh);height:min(128px,30cqh);aspect-ratio:1}\n')
print('Final visual CSS corrections written; no fixture or runtime files changed.')
