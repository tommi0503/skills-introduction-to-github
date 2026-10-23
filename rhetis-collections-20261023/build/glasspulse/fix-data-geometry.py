from pathlib import Path
C=Path('/workspace/output/glasspulse')
p=C/'elements/sparkline/element.css';base='\n'.join(p.read_text().splitlines()[:4]);r='.spark[data-el="glasspulse-sparkline"]';s=base+f'''
{r}{{display:flex;align-items:flex-start;justify-content:space-between;gap:0;padding:var(--gap-sm);color:var(--a1-7);anchor-scope:all;--glasspulse-spark-h:calc(100cqh - var(--gap-sm)*2)}}
{r}.up{{color:var(--good)}}{r}.down{{color:var(--bad)}}
{r}:not(.bars)>span{{position:static;flex:0 0 0;width:0;height:0;min-height:0;background:none;border-radius:0;margin-top:calc(var(--glasspulse-spark-h)*(1 - var(--v)/var(--max)));anchor-name:var(--glasspulse-spark-self);--glasspulse-spark-vh:calc(var(--glasspulse-spark-h)*var(--v)/var(--max))}}
{r}:not(.bars)>span::before{{content:"";position:absolute;left:anchor(var(--glasspulse-spark-prev) center);right:anchor(var(--glasspulse-spark-self) center);top:calc(anchor(var(--glasspulse-spark-prev) center) - var(--glasspulse-spark-h));bottom:var(--gap-sm);background:currentColor;clip-path:polygon(0 calc(var(--glasspulse-spark-h) - var(--stroke)/2),100% calc(100% - var(--glasspulse-spark-vh) - var(--stroke)/2),100% calc(100% - var(--glasspulse-spark-vh) + var(--stroke)/2),0 calc(var(--glasspulse-spark-h) + var(--stroke)/2))}}
{r}:not(.bars)>span:first-child::before{{content:none}}
{r}.bars{{align-items:flex-end;gap:calc(var(--gap-sm)/3)}}{r}.bars>span{{flex:1;height:calc(var(--glasspulse-spark-h)*var(--v)/var(--max));min-height:var(--stroke);background:currentColor;border-radius:calc(var(--gap-sm)/4) calc(var(--gap-sm)/4) 0 0}}
'''
for n in range(1,61):s+=f'{r}>span:nth-child({n}){{--glasspulse-spark-self:--glasspulse-spark-{n};--glasspulse-spark-prev:--glasspulse-spark-{n-1}}}\n'
p.write_text(s)
p=C/'elements/slope/element.css';base='\n'.join(p.read_text().splitlines()[:4]);r='.slope[data-el="glasspulse-slope"]';s=base+f'''
{r}{{display:block;padding:0;--glasspulse-slope-a:calc((1 - var(--a)/var(--max))*100%);--glasspulse-slope-b:calc((1 - var(--b)/var(--max))*100%)}}
{r}:not(.dumbbell){{background:linear-gradient(var(--n-4),var(--n-4)) 35% calc(var(--gap)*3)/var(--stroke) calc(100% - var(--gap)*5) no-repeat,linear-gradient(var(--n-4),var(--n-4)) right calc(var(--pad)*3) top calc(var(--gap)*3)/var(--stroke) calc(100% - var(--gap)*5) no-repeat}}
{r}>.heads{{position:absolute;left:35%;right:calc(var(--pad)*3);top:var(--gap);display:flex;justify-content:space-between;padding:0;font-size:var(--type-20);font-weight:var(--label-weight);line-height:var(--label-line)}}
{r}>.pair{{position:absolute;inset:0;display:block;gap:0;--glasspulse-slope-a:calc((1 - var(--a)/var(--max))*100%);--glasspulse-slope-b:calc((1 - var(--b)/var(--max))*100%)}}
{r}>.pair>.name{{position:absolute;left:var(--pad);top:calc(var(--gap)*3 + (100% - var(--gap)*5)*(1 - var(--a)/var(--max)));width:calc(35% - var(--pad) - var(--gap)*2);transform:translateY(-50%);font-size:var(--type-20);font-weight:var(--name-weight);line-height:var(--name-line)}}
{r}>.pair>.a,{r}>.pair>.b{{position:absolute;font-size:var(--type-24);font-weight:var(--figure-weight);line-height:var(--figure-line);white-space:nowrap;background:var(--page);z-index:2}}
{r}>.pair>.a{{left:35%;top:calc(var(--gap)*3 + (100% - var(--gap)*5)*(1 - var(--a)/var(--max)));transform:translate(-100%,-50%);padding-right:var(--gap-sm);color:var(--n-7)}}
{r}>.pair>.b{{left:calc(100% - var(--pad)*3);top:calc(var(--gap)*3 + (100% - var(--gap)*5)*(1 - var(--b)/var(--max)));transform:translateY(-50%);padding-left:var(--gap-sm);color:var(--a1-7)}}
{r}>.pair>.a::before,{r}>.pair>.b::before{{content:"";position:absolute;top:50%;width:var(--gap-sm);height:var(--gap-sm);border:var(--stroke) solid var(--n-5);border-radius:50%;background:var(--page);transform:translate(-50%,-50%)}}
{r}>.pair>.a::before{{left:100%}}{r}>.pair>.b::before{{left:0;background:var(--a1-7);border-color:var(--a1-7)}}
{r}>.pair::after{{content:"";position:absolute;left:35%;right:calc(var(--pad)*3);top:calc(var(--gap)*3);bottom:calc(var(--gap)*2);width:auto;height:auto;transform:none;background:var(--n-4);clip-path:polygon(0 calc(var(--glasspulse-slope-a) - var(--stroke)/2),100% calc(var(--glasspulse-slope-b) - var(--stroke)/2),100% calc(var(--glasspulse-slope-b) + var(--stroke)/2),0 calc(var(--glasspulse-slope-a) + var(--stroke)/2))}}
{r}>.pair.on::after{{background:var(--a1-7)}}
{r}.dumbbell{{display:flex;flex-direction:column;justify-content:center;gap:calc(var(--gap-sm)/1.5);padding:var(--gap)}}
{r}.dumbbell>.heads{{position:static;flex:none;display:flex;padding-left:27%;font-size:var(--type-20)}}
{r}.dumbbell>.pair{{position:relative;inset:auto;flex:1;min-height:0;width:100%;height:auto;display:block}}
{r}.dumbbell>.pair>.name{{left:0;top:50%;width:23%;transform:translateY(-50%)}}
{r}.dumbbell>.pair>.a,{r}.dumbbell>.pair>.b{{top:50%;font-size:var(--type-18);font-weight:var(--figure-weight);line-height:var(--figure-line);padding:0;background:none}}
{r}.dumbbell>.pair>.a{{left:calc(27% + var(--a)/var(--max)*66%);transform:translate(-50%,-100%);padding-bottom:calc(var(--gap-sm)/3)}}
{r}.dumbbell>.pair>.b{{left:calc(27% + var(--b)/var(--max)*66%);transform:translateX(-50%);padding-top:calc(var(--gap-sm)/3)}}
{r}.dumbbell>.pair>.a::before{{left:50%;top:100%}}{r}.dumbbell>.pair>.b::before{{left:50%;top:0}}
{r}.dumbbell>.pair::after{{left:calc(27% + min(var(--a),var(--b))/var(--max)*66%);right:auto;top:50%;bottom:auto;width:calc(abs(var(--a) - var(--b))/var(--max)*66%);height:var(--stroke);transform:none;clip-path:none;background:var(--n-4)}}
{r}.dumbbell>.pair.on::after{{background:var(--a1-7)}}
''';p.write_text(s)
