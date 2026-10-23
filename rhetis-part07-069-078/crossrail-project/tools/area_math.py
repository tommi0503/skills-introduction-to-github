from pathlib import Path
P=Path(__file__).parent/'crossrail/elements/chart-area';r='[data-el="crossrail-chart-area"]';s='\n/* Data-driven continuous area geometry through earlier CSS anchors. */\n'
s+=r+' .series{container-type:size;transform:translateX(0);anchor-scope:all}'+r+' .series>.pt{position:absolute;display:block;min-width:0;width:0;height:0;bottom:calc(var(--v)/var(--max)*100%);background:none;border:0}'+r+' .series>.pt::before{content:"";position:fixed;bottom:0;pointer-events:none;background:var(--a1-3-soft);z-index:-1}'+r+' .series>.pt::after{content:"";position:absolute;left:-3px;top:-3px;width:6px;height:6px;background:var(--a1-7);border-radius:50%}'+r+' .series>.pt:first-of-type::before{display:none}'+r+' .series>.pt b{bottom:var(--gap-sm);font-size:var(--type-14);z-index:2}'+r+' .series:nth-of-type(1){z-index:4}'+r+' .series:nth-of-type(2){z-index:3}'+r+' .series:nth-of-type(3){z-index:2}'+r+' .series:nth-of-type(4){z-index:1}'
for a in range(1,5):
 for i in range(1,13):s+=f'{r}>.series:nth-of-type({a})>.pt:nth-child({i} of .pt){{anchor-name:--crossrail-a{a}p{i};}}'
 for n in range(3,13):
  for i in range(1,n+1):
   q=f'{r}>.series:nth-of-type({a}):has(>.pt:nth-child({n} of .pt):last-child)>.pt:nth-child({i} of .pt)'
   s+=q+f'{{left:{(i-1)/(n-1)*100:.8g}%;}}'
   if i>1:s+=q+f'::before{{left:anchor(--crossrail-a{a}p{i-1} center);right:anchor(--crossrail-a{a}p{i} center);top:calc(anchor(--crossrail-a{a}p{i-1} top) - 100cqh);clip-path:polygon(0 100cqh,100% calc(100% - 100cqh * var(--v)/var(--max)),100% 100%,0 100%);background:var(--a{a}-3-soft);}}'
(P/'element.css').write_text((P/'element.css').read_text()+s+'\n')
print('Generic anchor-area geometry added')
