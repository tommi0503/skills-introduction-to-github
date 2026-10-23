"""Final material fixes from the complete light/dark visual review; fixture markup untouched."""
from pathlib import Path
P=Path(__file__).parent/'meridian-deck'
def add(name,css):
 f=P/'elements'/name/'element.css'
 with f.open('a') as h:h.write('\n/* Final material visual review. */\n'+css+'\n')
s='[data-el="meridian-deck-'
f=P/'foundation/foundation.css'
with f.open('a') as h:h.write('\n/* Bare stacked placeholders retain square intrinsic geometry. */\n.slide .stack>.seat{flex:1 1 0;aspect-ratio:1;width:auto;height:0;max-width:100%;align-self:center}\n')
add('chart-donut',s+'chart-donut"].donut>.name{max-width:calc(min(100cqw,100cqh,220px) - 48px);overflow-wrap:anywhere;font-size:var(--type-16)}')
add('chart-stack',''.join(s+f'chart-stack"] .seg:nth-child({i} of .seg):not(:is(.tone-1,.tone-2,.tone-3,.tone-4,.tone-5))'+'{background:var(--'+a+');color:var(--'+a+'-on)}' for i,a in [(1,'a1'),(2,'a2'),(3,'a3'),(4,'a4')])+s+'chart-stack"] .seg.tone-1{background:var(--a1);color:var(--a1-on)}'+s+'chart-stack"] .seg.tone-5{background:var(--n-6);color:var(--n-6-on)}')
# Explicit inline-size containment gives nested list content a real intrinsic height.
add('list',s+'list"]{container-type:inline-size;flex-shrink:0}')
add('pricing',s+'pricing"].plan>.tag{align-self:center;flex:none}'+s+'pricing"].plan>.price,'+s+'pricing"].plan>.name{flex:none}')
# Funnel clipping belongs on paint only; text retains the full padded content box.
add('funnel',s+'funnel"] .stage{clip-path:none;isolation:isolate;background:none;padding-inline:calc(var(--pad)*2)}'+s+'funnel"] .stage::before{content:"";position:absolute;inset:0;z-index:-1;background:var(--a1-2-soft);clip-path:polygon(0 0,100% 0,94% 100%,6% 100%)}'+s+'funnel"] .stage:nth-child(2)::before{background:var(--a1-3-soft)}'+s+'funnel"] .stage:nth-child(3)::before{background:var(--a1-4-soft)}'+s+'funnel"] .stage:nth-child(n+4){background:none}'+s+'funnel"] .stage:nth-child(n+4)::before{background:var(--a1)}'+s+'funnel"] .stage>.name{font-size:var(--type-20)}')
# Calendar square widths derive from both available axes, including every data row.
h=s+'heatmap"]'
css=h+'.calendar{align-items:center}'+h+'.calendar .row,'+h+'.calendar .heads{width:min(100%,calc((100cqh - var(--type-14)*var(--body-line) - var(--gap-sm)*6)*var(--cols,12)/7));padding-left:0;min-height:0}'+h+'.calendar .cell{aspect-ratio:auto;min-height:0}'
add('heatmap',css)
# Waffle square cells are bounded in both axes and reserve room for the actual caption.
w=s+'waffle"]'
css=w+' .units{flex:none;max-height:none;height:min(55cqh,calc(90cqw*var(--meridian-deck-unit-rows,1)/10));width:min(90%,calc(55cqh*10/var(--meridian-deck-unit-rows,1)));grid-template-rows:repeat(var(--meridian-deck-unit-rows,1),minmax(0,1fr))}'+w+' .u{aspect-ratio:auto;min-height:0}'
for i in range(2,11):css+=w+f' .units:has(.u:nth-child({(i-1)*10+1}))'+'{--meridian-deck-unit-rows:'+str(i)+'}'
css+='@container (max-height:250px){'+w+' .units{height:min(35cqh,calc(90cqw*var(--meridian-deck-unit-rows,1)/10));width:min(90%,calc(35cqh*10/var(--meridian-deck-unit-rows,1)))}}'
add('waffle',css)
# Short source page 20 icon cards cannot use the large card's reserved badge row.
c=s+'card"]'
add('card','@container (max-height:170px){'+c+'.card:has(.mark) .parts{position:absolute;inset:var(--gap-sm);width:auto;height:auto;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:calc(var(--gap-sm)/2)}'+c+'.card:has(.mark) .mark{width:40px;height:40px}'+c+'.card:has(.mark) .name{font-size:var(--type-16);min-height:0;padding:0;border:0}'+c+'.card:has(.mark) .note{font-size:var(--type-12);padding:0}}')
# Mood markers and two directed connecting segments use the same actual anchored coordinates.
j=s+'journey"]'
css=j+' .stage::before,'+j+' .stage::after{content:none;transform:none;border:0;border-radius:0;background:none;z-index:2}'+j+' .stage>.name::before{content:"";position:absolute;left:50%;top:calc(10% + (100 - var(--mood))*.35%);width:12px;height:12px;translate:-50% -50%;border:2px solid var(--a1);border-radius:999px;background:var(--page);z-index:3}'
for i in range(1,13):
 css+=j+f' .stage:nth-child({i})>.name::before'+'{anchor-name:--meridian-journey-'+str(i)+'}'
 if i>1:
  for pseudo,first,second,direction in [('before',i-1,i,'top'),('after',i,i-1,'bottom')]:
   css+=j+f' .stage:nth-child({i})::{pseudo}'+'{content:"";position:absolute;pointer-events:none;left:anchor(--meridian-journey-'+str(i-1)+' center);right:anchor(--meridian-journey-'+str(i)+' center);top:calc(anchor(--meridian-journey-'+str(first)+' center) - 1px);bottom:calc(anchor(--meridian-journey-'+str(second)+' center) - 1px);width:auto;height:auto;translate:none;background:linear-gradient(to '+direction+' right,transparent calc(50% - 1px),var(--a1) calc(50% - 1px),var(--a1) calc(50% + 1px),transparent calc(50% + 1px))}'
add('journey',css)
# Slope positions and connector direction are computed from the declared a/b values.
l=s+'slope"]'
css=l+':not(.dumbbell) .pair .a,'+l+':not(.dumbbell) .pair .b{position:absolute;translate:-50% -50%;z-index:2;background:var(--page);border-radius:var(--radius-sm);padding:calc(var(--gap-sm)/4)}'+l+':not(.dumbbell) .pair .a{left:42%;top:calc(80% - var(--a)/var(--max,100)*60%)}'+l+':not(.dumbbell) .pair .b{left:88%;top:calc(80% - var(--b)/var(--max,100)*60%)}'
for pseudo,aa,bb,direction in [('before','a','b','bottom'),('after','b','a','top')]:
 css+=l+':not(.dumbbell) .pair::'+pseudo+'{content:"";position:absolute;left:42%;right:12%;top:calc(80% - var(--'+aa+')/var(--max,100)*60% - 1px);bottom:calc(20% + var(--'+bb+')/var(--max,100)*60% - 1px);border:0;background:linear-gradient(to '+direction+' right,transparent calc(50% - 1px),var(--a1) calc(50% - 1px),var(--a1) calc(50% + 1px),transparent calc(50% + 1px))}'
css+=l+'.dumbbell .pair::after{left:calc(35% + min(var(--a),var(--b))/var(--max,100)*55%);right:calc(65% - max(var(--a),var(--b))/var(--max,100)*55%);border-color:var(--a1)}'+l+'.dumbbell .pair .a{translate:-50% -60%}'+l+'.dumbbell .pair .b{translate:-50% 60%}'
add('slope',css)
print('Applied final material CSS batch; all fixture markup and root repairs preserved.')
# Corrections verified with actual browser anchor boxes (stage siblings share one containing block).
add('chart-stack',s+'chart-stack"] .seg.tone-5{background:var(--n-7);color:var(--page)}')
f=P/'elements/chart-stack/element.css';f.write_text(f.read_text().replace('color:var(--n-6-on)','color:var(--page)'))
add('funnel',s+'funnel"] .stage:nth-child(n){background:none}')
add('card','@container (max-height:170px){'+c+'.card:has(.mark) .mark{align-self:center}}')
css=j+' .stage{position:static}'+j+' .stage:first-child::after{content:none}'+j+' .stage>.name::before{left:calc((100% - var(--gap-sm))*(var(--meridian-deck-stage-index) - .5)/var(--meridian-deck-stage-count,3) + var(--gap-sm)/2)}'
for i in range(1,13):
 css+=j+f':has(>.stage:nth-child({i}))'+'{--meridian-deck-stage-count:'+str(i)+'}'+j+f' .stage:nth-child({i})'+'{--meridian-deck-stage-index:'+str(i)+'}'
add('journey',css)
# Gradient strips run perpendicular to their gradient direction; flip to match the value endpoints.
f=P/'elements/slope/element.css';t=f.read_text();marker='/* Final material visual review. */';a,b=t.split(marker,1);b=b.replace('to bottom right','to TEMP right').replace('to top right','to bottom right').replace('to TEMP right','to top right');f.write_text(a+marker+b)
for name in ['radar','chart-area']:
 root=s+name+'"]'
 css=''
 for i,a in [(1,'a1'),(2,'a2'),(3,'a3'),(4,'a4')]:
  sel=root+f' .series:nth-child({i} of .series):not(:is(.tone-1,.tone-2,.tone-3,.tone-4,.tone-5))'
  if name=='radar':css+=sel+'{background:color-mix(in srgb,var(--'+a+') 30%,transparent);border-color:var(--'+a+')}'
  else:css+=sel+'{color:var(--'+a+')}'+sel+'>.name,'+sel+'>.pt>b{color:var(--'+a+'-7)}'
 for i,a in [(1,'a1'),(2,'a2'),(3,'a3'),(4,'a4'),(5,'n-7')]:
  sel=root+f' .series.tone-{i}'
  if name=='radar':css+=sel+'{background:color-mix(in srgb,var(--'+a+') 30%,transparent);border-color:var(--'+a+')}'
  else:css+=sel+'{color:var(--'+a+')}'+sel+'>.name,'+sel+'>.pt>b{color:var(--'+(a+'-7' if i<5 else 'n-7')+')}'
 add(name,css)
# Journey's contract already supplies --next. Direct endpoint math avoids a pseudo anchor's
# forward-reference restriction; both directed strips meet the actual mood markers.
f=P/'elements/journey/element.css';f.write_text(f.read_text().split('/* Final material visual review. */')[0])
css=j+' .stage{position:static}'+j+' .stage::before,'+j+' .stage::after{content:none;transform:none;translate:none;border:0;border-radius:0;background:none;z-index:2}'+j+' .stage>.name::before{content:"";position:absolute;left:calc((100% - var(--gap-sm))*(var(--meridian-deck-stage-index) - .5)/var(--meridian-deck-stage-count,3) + var(--gap-sm)/2);top:calc(10% + (100 - var(--mood))*.35%);width:12px;height:12px;translate:-50% -50%;border:2px solid var(--a1);border-radius:999px;background:var(--page);z-index:3}'
for i in range(1,13):css+=j+f':has(>.stage:nth-child({i}))'+'{--meridian-deck-stage-count:'+str(i)+'}'+j+f' .stage:nth-child({i})'+'{--meridian-deck-stage-index:'+str(i)+'}'
for pseudo,first,second,direction in [('before','var(--next,var(--mood))','var(--mood)','bottom'),('after','var(--mood)','var(--next,var(--mood))','top')]:
 css+=j+' .stage:nth-child(n):not(:last-child)::'+pseudo+'{content:"";position:absolute;pointer-events:none;left:calc((100% - var(--gap-sm))*(var(--meridian-deck-stage-index) - .5)/var(--meridian-deck-stage-count,3) + var(--gap-sm)/2);right:calc(100% - (100% - var(--gap-sm))*(var(--meridian-deck-stage-index) + .5)/var(--meridian-deck-stage-count,3) - var(--gap-sm)/2);top:calc(10% + (100 - '+first+')*.35% - 1px);bottom:calc(90% - (100 - '+second+')*.35% - 1px);width:auto;height:auto;transform:none;translate:none;background:linear-gradient(to '+direction+' right,transparent calc(50% - 1px),var(--a1) calc(50% - 1px),var(--a1) calc(50% + 1px),transparent calc(50% + 1px))}'
add('journey',css)
