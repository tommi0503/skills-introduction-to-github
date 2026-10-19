import {collectionNode} from './collection-adapter.js';
import {lucidePaths} from './icons.js';
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const px=n=>`${n||0}px`;
const paths={circle:'<circle cx="12" cy="12" r="9"/>',check:'<path d="m5 12 4 4L19 6"/>',arrow:'<path d="M4 12h16m-6-6 6 6-6 6"/>',user:'<circle cx="12" cy="7" r="4"/><path d="M4 22v-3a8 8 0 0 1 16 0v3"/>',users:'<circle cx="9" cy="8" r="3"/><path d="M2 21v-3a7 7 0 0 1 14 0v3m0-16a3 3 0 0 1 0 6m3 4a5 5 0 0 1 3 5"/>',chart:'<path d="M3 3v18h18M7 17v-5m5 5V7m5 10V4"/>',target:'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',building:'<path d="M4 22V3h16v19M8 7h2m4 0h2M8 11h2m4 0h2M8 15h2m4 0h2M10 22v-4h4v4"/>',cloud:'<path d="M6 18a4 4 0 0 1-1-8 7 7 0 0 1 13-2 5 5 0 0 1 0 10Z"/>',briefcase:'<rect x="3" y="7" width="18" height="14" rx="2"/><path d="M8 7V3h8v4M3 13h18m-10 0v3h2v-3"/>',search:'<circle cx="10" cy="10" r="7"/><path d="m15 15 7 7"/>',lightbulb:'<path d="M8 17c0-3-3-3-3-8a7 7 0 0 1 14 0c0 5-3 5-3 8M8 18h8m-7 3h6"/>',globe:'<circle cx="12" cy="12" r="10"/><ellipse cx="12" cy="12" rx="4" ry="10"/><path d="M2 12h20M4 6h16M4 18h16"/>',settings:'<circle cx="12" cy="12" r="4"/><path d="M12 1v4m0 14v4M1 12h4m14 0h4M4 4l3 3m10 10 3 3M4 20l3-3M17 7l3-3"/>',file:'<path d="M5 2h9l5 5v15H5ZM14 2v6h5M8 12h8m-8 4h8"/>',mail:'<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 5 10 8L22 5"/>',phone:'<path d="M4 2h4l2 6-3 2a17 17 0 0 0 7 7l2-3 6 2v4a2 2 0 0 1-2 2C9 22 2 15 2 4a2 2 0 0 1 2-2Z"/>'};
function renderNode(n,mode='direct'){
 let s=`left:${px(n.kind==='line'?n.x+Math.min(n.w,0):n.x)};top:${px(n.kind==='line'?n.y+Math.min(n.h,0):n.y)};width:${px(n.kind==='line'?Math.max(Math.abs(n.w),1):n.w)};height:${px(n.kind==='line'?Math.max(Math.abs(n.h),1):n.h)};`;
 if(n.transform)s+=`transform:${n.transform};transform-origin:${n.transformOrigin||'center'};`;
 s+=`--scene-justify:${({center:'center',right:'flex-end'}[n.align]||'flex-start')};`;
 s+=`--scene-border:${n.border?(n.borderWidth||1)+'px solid '+n.border:'0'};`;
 if(n.kind==='text'||n.kind==='group'||n.kind==='line'||n.kind==='path'||n.kind==='icon')s+='background:transparent;';
 if(n.shadow)s+=`box-shadow:${n.shadow};--scene-shadow:${n.shadow};`;
 if(n.opacity!==undefined)s+=`opacity:${n.opacity};`;
 let body='',cls='node '+n.kind+(n.verticalAlign==='middle'?' centered':'');
 if(n.kind==='text'){s+=`font-size:${px(n.size||20)};color:${n.color||'#222'};font-weight:${n.weight||400};line-height:${n.lineHeight||1.3};letter-spacing:${px(n.letterSpacing||0)};text-align:${n.align||'left'};font-family:${n.font||'Pretendard'},'Noto Sans CJK KR',sans-serif;`;if(n.verticalAlign==='middle')s+='display:flex;align-items:center;justify-content:'+({center:'center',right:'flex-end'}[n.align]||'flex-start')+';';body=esc(n.text).replace(/\n/g,'<br>');}
 else if(n.kind==='rect'||n.kind==='ellipse'||n.kind==='placeholder'){s+=`background:${n.fill||'transparent'};border-radius:${n.kind==='ellipse'?'50%':px(n.radius||0)};`;if(n.border)s+=`border:${n.borderWidth||1}px solid ${n.border};`;}
 else if(n.kind==='line'){body=`<svg viewBox="0 0 ${Math.max(Math.abs(n.w),1)} ${Math.max(Math.abs(n.h),1)}" overflow="visible"><line x1="${n.w<0?-n.w:0}" y1="${n.h<0?-n.h:0}" x2="${n.w<0?0:n.w}" y2="${n.h<0?0:n.h}" stroke="${n.color}" stroke-width="${n.width||1}" ${n.dash?'stroke-dasharray="'+n.dash+'"':''}/></svg>`;}
 else if(n.kind==='path')body=`<svg viewBox="${n.viewBox||'0 0 '+n.w+' '+n.h}" overflow="visible"><path d="${n.d}" fill="${n.fill}" stroke="${n.stroke}" stroke-width="${n.strokeWidth||1}"/></svg>`;
 if(n.kind==='path'&&n.fill?.startsWith('linear-gradient(')){const stops=[...n.fill.matchAll(/(#[a-fA-F0-9]{3,8}|rgba?\([^)]*\))/g)].map(m=>m[1]);const gid='gradient-'+Math.random().toString(36).slice(2);const vertical=/180deg|to bottom/.test(n.fill);const defs=`<defs><linearGradient id="${gid}" x1="0%" y1="0%" x2="${vertical?'0':'100'}%" y2="${vertical?'100':'0'}%">${stops.map((c,i)=>`<stop offset="${i/(stops.length-1)*100}%" stop-color="${c}"/>`).join('')}</linearGradient></defs>`;body=body.replace(/fill="linear-gradient\([^"]*\)"/,`fill="url(#${gid})"`).replace('<path',defs+'<path');}
 else if(n.kind==='icon')body=`<svg viewBox="0 0 24 24" fill="none" stroke="${n.color}" stroke-width="${n.strokeWidth||1.5}" stroke-linecap="round" stroke-linejoin="round">${(n.name==='building'?paths.building:lucidePaths[n.name])||paths[n.name]||paths.circle}</svg>`;
 else if(n.kind==='group')body=n.children.map(c=>renderNode(c,mode)).join('');
 if(mode==='assembled')return collectionNode(n,body,s,cls);
 return `<div class="${cls}" style="${s}">${body}</div>`;
}
export function renderSlide(slide,mode='direct'){return `<section class="slide scene-slide ${mode==='assembled'?'assembled':''}" data-slide="${slide.id}" style="background:${slide.bg||'#fff'}">${slide.nodes.map(n=>renderNode(n,mode)).join('')}</section>`;}
