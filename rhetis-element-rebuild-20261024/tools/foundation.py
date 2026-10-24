"""Write fresh foundation primitives. Furniture geometry is data from map, never page selectors.
Grid track overrides are generated from map bboxes once, before reconstruction rendering.
"""
from pathlib import Path
import json
ROOT=Path('/workspace/work/rebuild');profiles=json.loads((ROOT/'profiles.json').read_text())
for name,p in profiles.items():
 C=ROOT/name/name;n=name
 head_h={'tide-tab':120,'cutfield':130,'filament':128,'portico':155,'toggle-grid':180,'lamella':130,'rulemark':110}[name]
 head_size={'tide-tab':64,'cutfield':100,'filament':98,'portico':54,'toggle-grid':79,'lamella':44,'rulemark':48}[name]
 defaults={f'--{n}-grid-gap':'var(--gap)',f'--{n}-grid-columns':'repeat(12,minmax(0,1fr))',f'--{n}-grid-rows':'repeat(6,minmax(0,1fr))',f'--{n}-furn-x':'var(--margin-x)',f'--{n}-furn-y':'var(--margin-y)',f'--{n}-furn-w':'calc(1280px - var(--margin-x)*2)',f'--{n}-furn-h':'160px',f'--{n}-furn-font-ratio':'.065',f'--{n}-furn-font-size':'var(--type-14)',f'--{n}-furn-surface':'transparent',f'--{n}-furn-foreground':'inherit',f'--{n}-furn-align':'left',f'--{n}-body-x':'var(--margin-x)',f'--{n}-body-y':'var(--margin-y)',f'--{n}-body-w':'calc(1280px - var(--margin-x)*2)',f'--{n}-body-h':'calc(720px - var(--margin-y)*2)',f'--{n}-surface':'var(--page)',f'--{n}-foreground':'var(--ink)'}
 css=f'''/* Page furniture measured from the fixed {name} replicas; element appearance stays in element.css.
   Furniture boxes and 12x6 track positions are immutable map input, not CSS page/fixture conditions. */
.slide{{box-sizing:border-box;position:relative;width:1280px;height:720px;isolation:isolate;background:var(--page);color:var(--ink);font-family:var(--font-body);font-weight:var(--body-weight);font-size:var(--type-18);line-height:var(--body-line);letter-spacing:var(--body-track)}}
.slide *,.slide *::before,.slide *::after{{box-sizing:border-box}}
.slide>.page{{position:relative;isolation:isolate;width:100%;height:100%;padding:var(--margin-y) var(--margin-x);background:var(--{n}-surface);color:var(--{n}-foreground)}}
.slide>.page.on{{background:var(--{n}-surface);color:var(--{n}-foreground)}}
.slide>.page>.body{{position:absolute;left:var(--{n}-body-x);top:var(--{n}-body-y);z-index:1;display:grid;grid-template-columns:var(--{n}-grid-columns);grid-template-rows:var(--{n}-grid-rows);gap:var(--{n}-grid-gap);width:var(--{n}-body-w);height:var(--{n}-body-h);min-width:0;min-height:0;container-type:size}}
.slide .body>*{{min-width:0;min-height:0}}
.slide .group{{display:flex;gap:var(--gap);min-width:0;min-height:0}}
.slide .group.on{{color:var(--page)}}
.slide .group>*{{flex:1;min-width:0;min-height:0}}
.slide .group.col,.slide .stack{{display:flex;flex-direction:column;gap:var(--gap);min-width:0;min-height:0}}
.slide .stack>*{{flex:1;min-width:0;min-height:0}}
.slide .group.two{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))}}
.slide .group.three{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}}
.slide .split{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:var(--gap-lg);min-width:0;min-height:0}}
.slide .split.wide-left{{grid-template-columns:minmax(0,2fr) minmax(0,1fr)}}
.slide .seat{{display:grid;place-items:center;min-width:0;min-height:0;background:var(--n-2);color:var(--n-7);font:var(--label-weight) var(--type-18)/var(--label-line) var(--font-body)}}
.slide .seat:empty::after{{content:attr(data-ph)}}
.slide .seat.avatar{{aspect-ratio:1;border-radius:50%}}
.slide .seat.logo,.slide .seat.portrait{{aspect-ratio:1}}
.slide .seat.back{{position:absolute;inset:0;z-index:0}}
.slide .icon{{display:inline-block;flex:none;width:28px;height:28px}}
.slide>.page>:is(.head,.top,.rail,.foot,.deco){{position:absolute;left:var(--{n}-furn-x);top:var(--{n}-furn-y);width:var(--{n}-furn-w);height:var(--{n}-furn-h);margin:0;z-index:2;min-width:0;min-height:0}}
.slide>.page>.head{{--{n}-furn-h:{head_h}px;--{n}-furn-font-ratio:{head_size/(1280-2*p["mx"])};}}
.slide>.page>.top{{--{n}-furn-y:var(--gap-sm);--{n}-furn-h:var(--top-h)}}
.slide>.page>.foot{{--{n}-furn-y:calc(720px - var(--margin-y));--{n}-furn-h:var(--foot-h)}}
.slide>.page>.rail{{--{n}-furn-x:calc(1280px - var(--rail-w));--{n}-furn-y:0px;--{n}-furn-w:var(--rail-w);--{n}-furn-h:720px}}
.slide>.page:has(>.head){{--{n}-body-y:calc(var(--margin-y) + {head_h}px + var(--furn-gap));--{n}-body-h:calc(720px - var(--margin-y)*2 - {head_h}px - var(--furn-gap))}}
.slide>.page>.head{{color:var(--{n}-furn-foreground);container-type:size;display:flex;flex-direction:column;justify-content:flex-start;gap:var(--gap-sm)}}
.slide>.page>.head.center{{text-align:center;align-items:center}}
.slide>.page>.head>.deck{{font-size:var(--{n}-furn-font-size);font-weight:var(--body-weight);line-height:var(--label-line);text-align:var(--{n}-furn-align)}}
.slide>.page>.head>.title{{margin:0;max-width:100%;font-family:var(--font-display),var(--font-body);font-size:clamp(var(--type-20),calc(100cqw * var(--{n}-furn-font-ratio)),var(--type-128));font-weight:var(--title-weight);line-height:var(--title-line);letter-spacing:var(--title-track)}}
.slide>.page>.head>.kicker{{margin:0;font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track)}}
.slide>.page>.head>.lead{{margin:0;font-size:var(--{n}-furn-font-size);font-weight:var(--lead-weight);line-height:var(--lead-line);letter-spacing:var(--lead-track)}}
.slide>.page>.head:has(>.lead)>.title{{font-size:clamp(var(--type-20),min(calc(100cqw * var(--{n}-furn-font-ratio)),50cqh),var(--type-128))}}
.slide>.page>.top{{display:flex;align-items:center;justify-content:space-between;background:var(--{n}-furn-surface);color:var(--{n}-furn-foreground);font-size:var(--{n}-furn-font-size);font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track)}}
.slide>.page>.top>.idx{{display:flex;align-items:center;gap:var(--gap-sm)}}
.slide>.page>.top .label{{display:flex;align-items:center;justify-content:center;min-height:var(--top-h);padding:0 var(--gap);border:var(--stroke) solid currentColor;border-radius:999px;font-size:var(--type-12);line-height:var(--label-line)}}
.slide>.page>.top .label.on{{background:var(--ink);color:var(--page)}}
.slide>.page>.rail{{display:flex;flex-direction:column;justify-content:space-between;writing-mode:vertical-rl;text-align:var(--{n}-furn-align);background:var(--{n}-furn-surface);color:var(--{n}-furn-foreground);font-size:var(--{n}-furn-font-size);font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track)}}
.slide>.page>.foot{{display:flex;align-items:center;justify-content:space-between;gap:var(--gap-sm);background:var(--{n}-furn-surface);color:var(--{n}-furn-foreground);font-size:var(--{n}-furn-font-size);font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track)}}
.slide>.page>.deco{{z-index:0;pointer-events:none;overflow:hidden;color:var(--{n}-furn-foreground)}}
.slide>.page>.deco>svg{{display:block;width:100%;height:100%}}
.slide.cover .lockup{{position:absolute;z-index:2;max-width:85%;color:inherit}}
.slide.cover .lockup>.title{{margin:0;font-family:var(--font-display),var(--font-body);font-size:clamp(var(--type-20),calc(100cqw * var(--{n}-furn-font-ratio)),var(--type-128));font-weight:var(--title-weight);line-height:var(--title-line);letter-spacing:var(--title-track)}}
.slide.cover .lockup>.title b{{font-weight:calc(var(--body-weight)*1.75)}}
.slide.cover .lockup>.kicker{{margin:0 0 var(--gap-sm);font-size:var(--type-20);font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track)}}
.slide.cover .lockup>.lead{{margin:var(--gap) 0 0;font-size:var(--type-18);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track)}}
.slide.cover .at-center{{left:50%;top:50%;transform:translate(-50%,-50%);text-align:center}}
.slide.cover .at-left{{left:var(--margin-x);top:50%;transform:translateY(-50%)}}
.slide.cover .at-top-left{{left:var(--{n}-furn-x);top:var(--{n}-furn-y);width:var(--{n}-furn-w);height:var(--{n}-furn-h);container-type:size}}
.slide.cover .at-bottom-left{{left:var(--margin-x);bottom:var(--margin-y)}}
.slide.cover .meta{{position:absolute;z-index:2;right:var(--margin-x);bottom:var(--margin-y);margin:0;font-size:var(--type-14);line-height:var(--body-line);letter-spacing:var(--body-track)}}
'''
 if name=='tide-tab':
  css+='''.slide>.page{background:linear-gradient(var(--a1-1-soft),var(--a2-1-soft))}.slide>.page::after{content:"";position:absolute;z-index:3;left:0;right:0;bottom:0;height:8px;background:linear-gradient(90deg,var(--a1) 50%,var(--a2) 50%)}
.slide>.page>.head>.title{color:var(--a1-7);font-weight:var(--title-weight);line-height:calc(var(--title-line)*1.0714285714)}.slide>.page>.head>.title b{font-weight:inherit;color:var(--a2)}.slide>.page>.head>.kicker{order:2;color:var(--a1-7);font-size:var(--type-10);letter-spacing:calc(var(--label-track-latin)*6)}.slide>.page>.head>.title{order:1}.slide>.page>.head>.lead{order:3;color:var(--n-7);font-size:var(--type-14)}
.slide>.page>.rail{writing-mode:horizontal-tb;justify-content:flex-start;gap:var(--gap-sm)}.slide>.page>.rail>.title{margin:0;font:var(--title-weight) var(--type-64)/calc(var(--title-line)*.8571428571) var(--font-display);letter-spacing:var(--title-track);color:var(--a1-7)}.slide>.page>.rail>.title b{color:var(--a2);font-weight:inherit}.slide>.page>.rail>.label{font-size:var(--type-10);letter-spacing:calc(var(--label-track-latin)*6);color:var(--a1-7)}.slide>.page>.rail>.lead{margin:var(--gap-sm) 0 0;font-size:var(--type-14);color:var(--n-7);line-height:var(--lead-line)}
'''
 elif name=='cutfield':
  css+='''.slide>.page>.top{font-weight:var(--body-weight);white-space:nowrap}.slide>.page>.top>.deck{display:flex;align-items:center;gap:calc(var(--gap-sm)*.75);font-weight:calc(var(--body-weight)*1.75)}.slide>.page>.top .seat.logo{width:28px;height:28px;aspect-ratio:1}.slide>.page>.head>.title{padding-top:var(--gap);font-weight:calc(var(--weight-display)*.875);line-height:calc(var(--title-line)*.75)}.slide>.page>.head>.lead{font-size:var(--type-26)}.slide.cover .lockup>.title{font-weight:calc(var(--weight-display)*.875);line-height:calc(var(--title-line)*.75)}
'''
 elif name=='filament':
  defaults['--filament-furn-rotation']='0deg'
  css=css.replace('.slide>.page>.rail{display:flex;','.slide>.page>.rail{transform:rotate(var(--filament-furn-rotation));display:flex;',1)
  # Mirror the reviewed Filament furniture only; never alter other collection branches.
  css=css.replace('.slide>.page>.head>.kicker{margin:0;font-size:var(--type-14);','.slide>.page>.head>.kicker{margin:0;font-size:var(--filament-furn-font-size);')
  for selector in ['.slide>.page>.rail{display:flex;','.slide>.page>.foot{display:flex;']:
   prefix,separator,tail=css.partition(selector)
   rule,close,suffix=tail.partition('}')
   css=prefix+separator+rule.replace('font-weight:var(--label-weight)','font-weight:var(--body-weight)')+close+suffix
  css+='''.slide>.page>.rail,.slide>.page>.foot{font-style:italic}.slide>.page>.top{font-weight:calc(var(--body-weight)*1.75);font-size:var(--type-16)}.slide>.page>.head>.title{font-weight:var(--weight-display);line-height:calc(var(--title-line)*.875)}.slide>.page>.foot>.deck{margin:0;text-align:var(--filament-furn-align)}.slide.cover .lockup>.title{font-weight:var(--weight-display)}

/* Replica05: the tall left reading rail is bottom-to-top; the small confidentiality rail keeps its own direction. */
.slide>.page>.rail:has(>.title){container-type:size;transform:rotate(180deg);font-style:normal;align-items:center;justify-content:center}
.slide>.page>.rail>.title{margin:0;font-family:var(--font-display),var(--font-body);font-size:clamp(var(--type-20),calc(100cqw * var(--filament-furn-font-ratio)),var(--type-128));font-weight:var(--weight-display);line-height:var(--title-line);letter-spacing:var(--title-track)}
'''
 elif name=='portico':
  css+='''.slide.cover .lockup>.kicker{margin:0;font-size:clamp(var(--type-36),6.29225cqw,var(--type-40));font-weight:calc(var(--body-weight)*1.25);line-height:calc(var(--label-line)*1.0833333333);letter-spacing:calc(var(--label-track)*4.358974359)}.slide.cover .lockup>.title{letter-spacing:calc(var(--label-track-latin)*1.40625);line-height:calc(var(--title-line)*.9821428571)}.slide.cover .lockup>.lead{margin-top:calc(var(--gap-sm)*.875);font-size:var(--type-16);color:inherit}.slide>.page.on{background:var(--portico-surface);color:var(--portico-foreground)}.slide>.page>.head{--portico-furn-x:0px;--portico-furn-y:0px;--portico-furn-w:1192px;flex-direction:row;align-items:center;gap:var(--gap);padding:calc(var(--pad)*1.25) var(--margin-x) 0;background:var(--portico-furn-surface);color:var(--portico-furn-foreground)}.slide>.page>.head>.title{font-weight:calc(var(--weight-display)*1.0625);letter-spacing:calc(var(--label-track-latin)*1.8741111111);line-height:calc(var(--title-line)*.9821428571);white-space:nowrap}.slide>.page>.head>.icon{width:35px;height:35px;color:var(--a1)}.slide>.page>.rail{display:block;padding:0;writing-mode:horizontal-tb;background:var(--portico-furn-surface);color:var(--portico-furn-foreground);font-size:clamp(var(--type-10),calc(var(--type-12)*.9166666667),var(--type-12));font-weight:calc(var(--body-weight)*.75);line-height:calc(var(--body-line)*1.0344827586);letter-spacing:calc(var(--label-track)*0)}.slide>.page>.rail>.sec,.slide>.page>.rail>.deck{position:absolute;left:37.5%;top:20.1388888889%;white-space:nowrap;transform-origin:0 0;transform:rotate(-90deg)}.slide>.page>.rail>.deck{top:94.0277777778%}.slide.cover>.page>.rail{font-size:clamp(var(--type-12),calc(var(--type-14)*.9285714286),var(--type-14));letter-spacing:calc(var(--label-track-latin)*6.153846154)}.slide.cover>.page>.rail>.sec{left:33.3333333333%;top:65.6050955414%}.slide>.page>.foot{padding:0 var(--margin-x);background:var(--a1-9);color:var(--page);border-top:var(--stroke) solid var(--n-5)}
'''
 elif name=='toggle-grid':
  from toggle_foundation import css as toggle_furniture_css, defaults as toggle_furniture_defaults
  css=toggle_furniture_css()
  defaults.update(toggle_furniture_defaults())
 elif name=='lamella':
  css+='''.slide>.page>.head>.title{font-weight:var(--title-weight);line-height:calc(var(--title-line)*1.1339285714)}.slide>.page>.top{color:var(--lamella-furn-foreground);font-size:var(--lamella-furn-font-size);font-weight:var(--body-weight)}.slide>.page>.top>.sec{margin:0;white-space:nowrap;text-align:var(--lamella-furn-align)}.slide>.page>.foot{font-size:var(--type-12)}.slide>.page>.foot>.no{margin-left:auto}.slide.cover .meta{top:var(--margin-y);bottom:auto;text-align:right}
'''
 elif name=='rulemark':
  css+='''.slide>.page>.top{align-items:flex-start;border-bottom:var(--stroke) solid var(--n-5);font-size:var(--type-20);font-weight:var(--title-weight)}.slide>.page>.top>.deck{display:flex;align-items:center;gap:var(--gap-sm);margin-top:var(--gap-sm)}.slide>.page>.top>.idx{gap:calc(var(--gap-sm)*.75)}.slide>.page>.top .label{min-height:36px;min-width:calc(var(--pad)*127/28);padding:0 calc(var(--gap)*.5);letter-spacing:calc(var(--label-track)*0)}.slide>.page>.top .logo{display:inline-block;position:relative;width:30px;height:26px}.slide>.page>.top .logo::before,.slide>.page>.top .logo::after{content:"";position:absolute;width:7px;height:21px;background:var(--ink);border-radius:4px;transform:rotate(28deg);top:3px}.slide>.page>.top .logo::before{left:4px}.slide>.page>.top .logo::after{left:14px}.slide>.page>.top .logo>i{position:absolute;width:7px;height:11px;background:var(--ink);border-radius:4px;transform:rotate(-35deg);left:22px;top:13px}.slide>.page>.head>.title{font-size:var(--type-48);font-weight:var(--title-weight);line-height:calc(var(--title-line)*1.1160714286);letter-spacing:calc(var(--title-track)*2.6666666667)}.slide>.page>.foot{padding:0 var(--margin-x);background:var(--ink);color:var(--page);font-size:var(--type-14)}.slide.cover .lockup{text-align:center}.slide.cover .lockup>.title{font-size:var(--type-88);font-weight:var(--body-weight);line-height:calc(var(--title-line)*1.0714285714)}.slide.cover .lockup>.title b{font-weight:var(--weight-display)}
'''
 if name=='portico':
  css+='''.slide.cover>.page{--portico-surface:var(--a1);--portico-foreground:var(--a1-on)}.slide>.page>.head{--portico-furn-surface:var(--n-3)}.slide>.page>.rail{--portico-furn-x:1192px;--portico-furn-w:88px;--portico-furn-surface:var(--a1);--portico-furn-foreground:var(--a1-on)}.slide>.page:has(>.rail){--portico-body-w:calc(1192px - var(--margin-x)*2)}.slide.cover>.page>.rail{--portico-furn-x:1229px;--portico-furn-w:51px;--portico-furn-h:628px;--portico-furn-surface:var(--n-3);--portico-furn-foreground:var(--ink)}.slide.cover .at-top-left{--portico-furn-x:73px;--portico-furn-y:101px;--portico-furn-w:619.81px;--portico-furn-h:244.86px;--portico-furn-font-ratio:.2065148997}.slide.cover>.page>.foot{--portico-furn-x:0px;--portico-furn-y:627px;--portico-furn-w:1280px;--portico-furn-h:93px}
'''
  css+='''.slide>.page>.head:has(>.lead){flex-direction:column;align-items:flex-start;justify-content:center;gap:var(--gap-sm);padding-top:0}.slide.cover>.page>.foot{justify-content:flex-start;gap:calc(var(--gap-sm)*1.25);padding:0 calc(var(--pad)*2.5);font-weight:var(--body-weight)}.slide.cover>.page>.foot>.idx{padding-left:calc(var(--pad)*35/24);display:flex;align-items:center}.slide.cover>.page>.foot>.idx+.idx{margin-left:calc(var(--gap-sm)*2.5)}.slide.cover>.page>.foot .deck>b,.slide.cover>.page>.foot>.label{font-weight:calc(var(--body-weight)*1.75)}.slide.cover>.page>.foot>.label{margin-left:auto}
'''
 defaults[f'--{n}-furn-depth']='0'
 css=css.replace('.slide>.page>.deco{z-index:0;',f'.slide>.page>.deco{{z-index:var(--{n}-furn-depth);')
 (C/'foundation/foundation.css').write_text(css)
 (C/'foundation/foundation.json').write_text(json.dumps({'schema':'rhetis.design-library-foundation-source/1','kit':name,'registrations':{},'tokenDefaults':defaults},indent=2))
 (C/'foundation/description.md').write_text('The foundation owns the measured page devices and a twelve-column, six-row grid. Source-map geometry is supplied as declared layout data before any component is rendered. No page IDs, fixture names or element selectors occur here. All component faces, labels and member connectors remain in their own element files. Unsupported apparatus is recorded rather than simulated with another component.\n')
print('seven foundations freshly compiled; source geometry fields declared')
