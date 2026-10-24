"""New chart geometry only: anchors derive connections directly from contract --v points."""
def chart_css(root,area,name):
 s=''
 def r(t,b):return ','.join(x if '[data-el='in x else root+x for x in t.split(','))+'{'+b+'}\n'
 s+=r('','--chart-head:64px;--chart-foot:36px;--plot-h:calc(100cqh - var(--chart-head) - var(--chart-foot));--plot-color:var(--a1);--plot-ink:var(--a1-8);position:relative;anchor-scope:all;')
 pt='>.series>.pt'if area else'>.pt'
 if area:
  s+=r('>.series','position:absolute;inset:var(--chart-head) 4% var(--chart-foot);display:flex;align-items:flex-end;justify-content:space-between;anchor-scope:all;--plot-color:var(--a1);--plot-ink:var(--a1-8);')
  s+=r('>.series>.name','position:absolute;top:calc(-1 * var(--chart-head) + 8px);left:calc(var(--series-index,0)*25%);max-width:24%;font-size:var(--type-12);font-weight:var(--label-weight);line-height:var(--label-line);color:var(--ink);')
  for k in range(1,5):s+=r('>.series:nth-child('+str(k)+' of .series)',f'--series-index:{k-1};--plot-color:var(--a{k});--plot-ink:var(--a{k}-8);z-index:{5-k};')
  s+=r('>.axis','position:absolute;bottom:0;left:4%;right:4%;height:var(--chart-foot);display:flex;align-items:center;justify-content:space-between;border-top:var(--stroke) solid var(--n-4);')+r('>.axis>span','flex:1;min-width:0;text-align:center;font-size:var(--type-12);line-height:var(--label-line);')
  s+=r(':not(:has(>.axis>span:not(:empty)))>.series','left:3.5px;right:3.5px;')
  s+=r(':not(:has(>.series>.name:not(:empty)))','--chart-head:3.5px;')+r(':not(:has(>.axis>span:not(:empty)))','--chart-foot:0px;')
 else:s+=r('','display:flex;justify-content:space-between;align-items:flex-end;padding:0 8%;')
 s+=r(pt,'position:static;flex:none;width:1px;height:1px;margin-bottom:calc('+('' if area else 'var(--chart-foot) + ')+'var(--v)/var(--max,100)*var(--plot-h));anchor-name:var(--own);box-shadow:0 0 0 3px var(--plot-color);border-radius:50%;')
 for k in range(1,13):s+=r(pt+':nth-child('+str(k)+' of .pt)',f'--own:--{name}-'+('area'if area else'line')+f'-{k};'+(f'--previous:--{name}-'+('area'if area else'line')+f'-{k-1};'if k>1 else''))
 s+=r(pt+'>b','position:absolute;left:anchor(var(--own) center);top:calc(anchor(var(--own) top) - 12px);transform:translate(-50%,-100%);white-space:nowrap;font-size:clamp(var(--type-12),1.5cqw,var(--type-18));font-weight:var(--figure-weight);line-height:var(--figure-line);color:var(--plot-ink);')
 if area:
  s+=r(pt+'::before','content:"";position:absolute;left:anchor(var(--previous) center);right:anchor(var(--own) center);top:calc(anchor(var(--previous) top) - var(--plot-h));bottom:0;background:linear-gradient(to top,transparent,color-mix(in srgb,var(--plot-color) 25%,transparent));background-size:100% var(--plot-h);background-position:bottom;clip-path:polygon(0 var(--plot-h),100% calc(100% - var(--v)/var(--max,100)*var(--plot-h)),100% 100%,0 100%);')
  s+=r(pt+'::after','content:"";position:absolute;left:anchor(var(--previous) center);right:anchor(var(--own) center);top:calc(anchor(var(--previous) top) - var(--plot-h));bottom:0;background:var(--plot-color);clip-path:polygon(0 calc(var(--plot-h) - .7px),100% calc(100% - var(--v)/var(--max,100)*var(--plot-h) - .7px),100% calc(100% - var(--v)/var(--max,100)*var(--plot-h) + .7px),0 calc(var(--plot-h) + .7px));')
  s+=r('.stacked>.series>.pt::before','background:var(--plot-color);opacity:1;')
 else:
  s+=r(pt+'>span','position:absolute;left:anchor(var(--own) center);bottom:0;transform:translateX(-50%);height:var(--chart-foot);display:flex;align-items:center;font-size:var(--type-12);line-height:var(--label-line);white-space:nowrap;color:var(--ink);')
  s+=r(pt+'::before','content:"";position:absolute;left:anchor(var(--previous) center);right:anchor(var(--own) center);top:calc(anchor(var(--previous) top) - .7px);bottom:calc(anchor(var(--own) top) - .7px);background:linear-gradient(to top right,transparent calc(50% - 1px),var(--plot-color) calc(50% - .6px),var(--plot-color) calc(50% + .6px),transparent calc(50% + 1px));')
  s+=r(pt+'::after','content:"";position:absolute;left:anchor(var(--previous) center);right:anchor(var(--own) center);top:calc(anchor(var(--own) top) - .7px);bottom:calc(anchor(var(--previous) top) - .7px);background:linear-gradient(to bottom right,transparent calc(50% - 1px),var(--plot-color) calc(50% - .6px),var(--plot-color) calc(50% + .6px),transparent calc(50% + 1px));')
 s+=r(pt+':first-child::before,'+pt+':first-child::after','content:none;')
 s+='@container (max-width:650px){'+r('>.axis>span:nth-child(even)','visibility:hidden;')+'}\n'
 return s
