def mindmap_css():
 s='''
${display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:repeat(var(--seedmark-half),minmax(0,1fr));gap:var(--gap);padding:var(--gap-sm);anchor-scope:all;isolation:isolate;}
$ .core{grid-column:2;grid-row:1/span var(--seedmark-half);align-self:center;anchor-name:--seedmark-core;z-index:2;display:flex;align-items:center;justify-content:center;text-align:center;padding:var(--gap);border-radius:999px;background:var(--ink);color:var(--page);font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);}
$ .branch{position:static;min-width:0;min-height:0;display:flex;flex-direction:column;justify-content:center;gap:calc(var(--gap-sm)/2);padding:var(--gap-sm);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--n-1);}
$ .branch.on{background:var(--a1-2-soft);border-color:var(--ink);}
$ .branch:before{content:'';position:absolute;top:min(anchor(--seedmark-core center),anchor(var(--seedmark-branch) center));bottom:min(anchor(--seedmark-core center),anchor(var(--seedmark-branch) center));min-height:2px;z-index:-1;}
$ .name{font-size:var(--type-20);font-weight:var(--name-weight);line-height:var(--name-line)}$ .leaf{font-size:var(--type-16);line-height:var(--body-line);border-top:var(--stroke) solid var(--n-3);padding-top:calc(var(--gap-sm)/2);}
@container(max-width:650px){$ .name{font-size:var(--type-16)}$ .leaf{font-size:var(--type-12)}}
'''
 for n in range(2,7):
  cond=f'$:has(>.branch:nth-child({n} of .branch)):not(:has(>.branch:nth-child({n+1} of .branch)))';half=(n+1)//2;s+=f'{cond}{{--seedmark-half:{half};}}'
  for i in range(1,n+1):
   row=(i+1)//2;right=i%2==1;below=row>(half+1)/2;sel=cond+f'>.branch:nth-child({i} of .branch)';s+=f'{sel}{{grid-column:{3 if right else 1};grid-row:{row};anchor-name:--seedmark-b{i};--seedmark-branch:--seedmark-b{i};}}'
   props=('left:anchor(--seedmark-core right);right:anchor(--seedmark-b'+str(i)+' left);'if right else'left:anchor(--seedmark-b'+str(i)+' right);right:anchor(--seedmark-core left);')
   props+='border-'+('right'if right else'left')+':var(--stroke) solid var(--n-3);border-'+('top'if below==right else'bottom')+':var(--stroke) solid var(--n-3);'
   corner=('top'if below==right else'bottom')+'-'+('right'if right else'left');props+='border-'+corner+'-radius:50%;'
   s+=sel+':before{'+props+'}'
 return s

def radar_css():
 s='''
${isolation:isolate;}
$:before{content:'';position:absolute;left:50%;top:50%;width:min(64cqw,64cqh);height:min(64cqw,64cqh);transform:translate(-50%,-50%);border:var(--stroke) solid var(--n-3);border-radius:50%;background:radial-gradient(circle,transparent 32%,var(--n-3) 32% 33%,transparent 33% 65%,var(--n-3) 65% 66%,transparent 66%);z-index:-1;}
$ .axis{position:absolute;left:calc(50% + sin(var(--seedmark-angle))*min(42cqw,42cqh));top:calc(50% - cos(var(--seedmark-angle))*min(42cqw,42cqh));transform:translate(-50%,-50%);max-width:24%;text-align:center;}
$ .axis>.name{font-size:var(--type-12);line-height:var(--label-line);font-weight:var(--label-weight);}
$ .series{position:static;}
$ .series:before{content:'';position:absolute;left:50%;top:50%;width:min(64cqw,64cqh);height:min(64cqw,64cqh);transform:translate(-50%,-50%);background:color-mix(in srgb,var(--a1) 25%,transparent);}
$ .series>.name{position:absolute;top:0;font-size:var(--type-12);line-height:var(--label-line);font-weight:var(--label-weight);color:var(--ink);}
$ .series.tone-2:before{background:color-mix(in srgb,var(--a2) 25%,transparent)}$ .series.tone-3:before{background:color-mix(in srgb,var(--a3) 25%,transparent)}$ .series.tone-4:before{background:color-mix(in srgb,var(--a4) 25%,transparent)}$ .series.tone-5:before{background:color-mix(in srgb,var(--n-5) 25%,transparent)}
'''
 for n in range(3,9):
  cond=f'$:has(>.axis:nth-child({n} of .axis)):not(:has(>.axis:nth-child({n+1} of .axis)))'
  for i in range(1,n+1):s+=cond+f'>.axis:nth-child({i} of .axis){{--seedmark-angle:{(i-1)*360/n}deg;}}'
  poly=','.join(f'calc(50% + sin({(i-1)*360/n}deg)*var(--v{i})/var(--max)*50%) calc(50% - cos({(i-1)*360/n}deg)*var(--v{i})/var(--max)*50%)'for i in range(1,n+1));s+=cond+' .series:before{clip-path:polygon('+poly+');}'
 for n in range(1,4):
  cond=f'$:has(>.series:nth-child({n} of .series)):not(:has(>.series:nth-child({n+1} of .series)))'
  for i in range(1,n+1):s+=cond+f'>.series:nth-child({i} of .series)>.name{{left:calc(var(--gap-sm) + ({i}-1)*(100% - var(--gap-sm)*2)/{n});width:calc((100% - var(--gap-sm)*2)/{n} - var(--gap-sm));}}'
 return s

def apply(D):
 D['mindmap']=mindmap_css();D['radar']=radar_css()
 D['matrix']+='''
$.swot .cell{gap:calc(var(--gap-sm)/2);padding:var(--gap-sm);}
$.swot .cell>.kick{font-size:var(--type-24);line-height:var(--name-line);}
$.swot .cell>.name{font-size:var(--type-20);line-height:var(--name-line);}
$.swot .cell>.list{margin:0;padding-left:var(--gap-sm);font-size:var(--type-14);line-height:var(--body-line);text-align:left;}
'''
 D['pricing']=D['pricing'].replace('flex-direction:column;justify-content:center;gap:var(--gap);padding:var(--pad);','flex-direction:column;justify-content:center;gap:var(--gap-sm);padding:var(--gap-sm);')
 D['pricing']+='''
$.plan{display:grid;grid-template-rows:26px 60px 58px minmax(0,1fr);height:min(100%,calc(var(--pad)*13));align-self:center;align-content:stretch;}
$.plan>.tag{grid-row:1;font-size:var(--type-12);line-height:var(--label-line);}
$.plan>.name{grid-row:2;font-size:var(--type-20);line-height:var(--name-line);align-self:start;}
$.plan>.price{grid-row:3;align-self:start;}
$.plan>.list{grid-row:4;align-self:start;margin:0;padding-left:var(--gap-sm);font-size:var(--type-14);line-height:var(--body-line);}
'''
 D['person']+='\n$.person>.list{text-align:left;}\n'
 D['positioning']+='\n@container(max-width:650px){$:has(>.mark:nth-child(6 of .mark)) .mark{width:24px;height:24px;}$:has(>.mark:nth-child(6 of .mark)) .mark.on{width:72px;height:44px;}$:has(>.mark:nth-child(6 of .mark)) .mark.on>.name{font-size:var(--type-12);padding:calc(var(--gap-sm)/3);}}'
 a=D['slope'].index('$ .pair:before{');b=D['slope'].index('$ .pair>.a,')
 D['slope']=D['slope'][:a]+'''
$ .pair:before{content:'';position:absolute;inset:0;background:var(--n-4);clip-path:polygon(0 calc((1 - var(--a)/var(--max))*100%),100% calc((1 - var(--b)/var(--max))*100%),100% calc((1 - var(--b)/var(--max))*100% + 2px),0 calc((1 - var(--a)/var(--max))*100% + 2px));}
$ .pair.on:before{background:var(--a1);}
'''+D['slope'][b:]
 # Dumbbell uses a straight connector whose geometry is independent of the slope strip.
 D['slope']=D['slope'].replace('height:2px;background:var(--n-4);','height:2px;background:var(--n-4);clip-path:none;')
 D['sankey']=D['sankey'].replace('top:50%;transform:translateY(-50%);width:calc(var(--pad)*4);','top:var(--gap-sm);bottom:var(--gap-sm);width:calc(var(--pad)*4);').replace('top:15%;bottom:15%;','top:0;bottom:0;').replace('clip-path:polygon(0 30%,100% 0,100% 100%,0 70%);','border-radius:var(--radius-sm) 0 0 var(--radius-sm);')
 D['venn']+='''
$:not(:has(>.set:nth-child(3))){--seedmark-diameter:min(62cqw,90cqh);}
$:not(:has(>.set:nth-child(3)))>.set{width:var(--seedmark-diameter);height:var(--seedmark-diameter);}
$:not(:has(>.set:nth-child(3)))>.set:first-child{left:calc(50% - var(--seedmark-diameter)*.8);right:auto;}
$:not(:has(>.set:nth-child(3)))>.set:nth-child(2){left:calc(50% - var(--seedmark-diameter)*.2);right:auto;}
$:not(:has(>.set:nth-child(3)))>.set:first-child>.name{transform:translateX(calc(var(--seedmark-diameter)*-.15));}
$:not(:has(>.set:nth-child(3)))>.set:nth-child(2)>.name{transform:translateX(calc(var(--seedmark-diameter)*.15));}
$:not(:has(>.set:nth-child(3))):before{content:'';position:absolute;left:calc(50% - var(--seedmark-diameter)*.8);top:50%;transform:translateY(-50%);width:var(--seedmark-diameter);height:var(--seedmark-diameter);border-radius:50%;background:var(--ink);mask-image:radial-gradient(circle calc(var(--seedmark-diameter)*.5) at 110% 50%,var(--ink) 99%,transparent);z-index:1;}
$ .set.on{background:var(--a1-2-soft);}
$ .core{background:none;color:var(--page);width:min(25cqw,30cqh);height:min(25cqw,30cqh);}
'''
