def pill_css():
 return '''
${display:flex;align-items:center;justify-content:center;padding:var(--gap-sm) var(--gap);border:var(--stroke) solid var(--ink);border-radius:999px;background:var(--ink);color:var(--page);isolation:isolate;}
$.line{background:var(--page);color:var(--ink)}$.quiet{background:var(--n-1);border-color:var(--n-1);color:var(--ink)}$.on{background:var(--a1);border-color:var(--a1);color:var(--a1-on)}
$ .parts{display:flex;align-items:center;justify-content:center;gap:calc(var(--gap-sm)/2);min-width:0;width:100%;height:100%;}
$ .name{font-size:clamp(var(--type-18),min(10cqw,35cqh),var(--type-26));font-weight:var(--name-weight);line-height:var(--name-line);text-align:center;}
$ .note{font-size:var(--type-20);line-height:var(--body-line);color:inherit;text-align:center;}
$ .mark{min-width:26px;min-height:26px;display:flex;align-items:center;justify-content:center;font-size:var(--type-14);line-height:var(--label-line);}
$ .mark .icon{width:28px;height:28px;}
$:not(.line,.quiet) .parts:has(>.note:not(:empty)){flex-direction:column;gap:calc(var(--gap-sm)/2)}
$:not(.line,.quiet) .parts:has(>.note:not(:empty))>.name{font-size:clamp(var(--type-18),min(11.24cqw,24.54cqh),var(--type-40));}
$:has(.mark):not(:has(.icon)){padding:0;background:none;border:0;}
$:has(.mark):not(:has(.icon)):before{content:'';position:absolute;inset:min(13px,20cqh) 0 0;border:var(--stroke) solid var(--ink);border-radius:999px;background:var(--ink);z-index:-1;}
$.line:has(.mark):not(:has(.icon)):before{background:var(--page)}$.quiet:has(.mark):not(:has(.icon)):before{background:var(--n-1);border-color:var(--n-1)}$.on:has(.mark):not(:has(.icon)):before{background:var(--a1);border-color:var(--a1)}
$:has(.mark):not(:has(.icon)) .parts{padding: min(26px,40cqh) var(--gap-sm) 0;}
$:has(.mark):not(:has(.icon)) .mark{position:absolute;top:0;left:50%;transform:translateX(-50%);height:min(26px,40cqh);min-height:0;min-width:26px;padding:0 calc(var(--gap-sm)/2);border:1px solid var(--ink);border-radius:var(--radius-sm);background:var(--page);color:var(--ink);font-size:clamp(var(--type-10),8cqh,var(--type-12));}
$.line:has(.mark):not(:has(.icon)) .name{font-size:var(--type-18);font-weight:var(--name-weight);}
$ .note:empty{display:none;}
@container(min-aspect-ratio:3/1){$ .parts,$:not(.line,.quiet) .parts:has(>.note:not(:empty)){flex-direction:row;}$ .note{font-size:var(--type-14);}}
@container(max-width:500px){$ .parts{flex-wrap:wrap}}
@container(max-height:100px){$ .note{font-size:var(--type-14)}}
'''
