import {esc,fontCSS} from './renderer.mjs';
import fs from 'node:fs';
const icons=JSON.parse(fs.readFileSync(new URL('./lucide-icons.json',import.meta.url),'utf8'));
const scope=k=>`data-el="blueprint-06-${k}"`;
const name=x=>`<div class="name">${esc(x.name||'')}</div>`;
const note=x=>x.note?`<p class="note">${esc(x.note)}</p>`:'';
const icon=x=>{if(!x)return '';let k=x.replace(/(^|-)(\w)/g,(_,a,b)=>b.toUpperCase());return `<span class="mark">${icons[k]||icons.Circle}</span>`};
const fig=x=>x.fig?`<div class="fig">${esc(x.fig)}</div>`:'';
const list=(items,variant='')=>`<div class="list ${variant}" ${scope('list')}>${items.map(x=>`<div class="item">${name(typeof x==='string'?{name:x}:x)}${note(x)}</div>`).join('')}</div>`;
const where=a=>a?` style="grid-column:${a[0]} / span ${a[1]};grid-row:${a[2]} / span ${a[3]}"`:'';
export function blockHTML(b){
 const it=b.items||[],variant=b.variant||'';let html='',root='',element='';
 switch(b.kind){
 case 'cards':return `<div class="group${b.column?' col':b.columns===2?' two':b.columns===3?' three':''}"${where(b.at)}>${it.map(x=>`<article class="card ${x.variant||variant}" ${scope('card')}><div class="parts">${x.kick?`<p class="kick">${esc(x.kick)}</p>`:''}${x.image?`<div class="mark" style="width:100%;height:${x.imageHeight||120}px;border-radius:${x.round?"50%":"0"};flex-shrink:0"><div class="seat" data-ph="1" style="width:100%;height:100%;border-radius:inherit"></div></div>`:icon(x.icon)}${fig(x)}${name(x)}${note(x)}</div></article>`).join('')}</div>`;
 case 'metrics':root='stats';element='metric';html=it.map(x=>`<div class="stat" ${scope('metric')}><div class="parts">${fig(x)}${name(x)}${note(x)}</div></div>`).join('');break;
 case 'bars':root='bars'+(b.horizontal?' h':'');element='chart-bar';html=it.map((x,i)=>`<div class="bar${i===it.length-1?' on':''}" style="--v:${x.value}"><b>${esc(x.label||x.value)}</b><span>${esc(x.name)}</span></div>`).join('');break;
 case 'lines':root='lines';element='chart-line';html=it.map((x,i)=>`<div class="pt" style="--v:${x.value};--blueprint-06-next:${it[i+1]?.value??x.value}"><b>${esc(x.label||x.value)}</b><span>${esc(x.name)}</span></div>`).join('');break;
 case 'donuts':root='donuts';element='chart-donut';html=it.map(x=>`<div class="donut" ${scope('chart-donut')} style="--v:${Math.min(100,x.value)}"><div class="fig">${esc(x.label||x.value+'%')}</div>${name(x)}</div>`).join('');break;
 case 'table':root='tablebox';element='table';html=`<table class="table">${b.widths?`<colgroup>${b.widths.map(w=>`<col style="width:${w}%">`).join('')}</colgroup>`:''}<thead><tr>${b.headers.map((x,i)=>`<th${i===b.pick?' class="pick"':''}>${esc(x)}</th>`).join('')}</tr></thead><tbody>${b.rows.map(row=>`<tr>${row.map((x,i)=>`<td${i===b.pick?' class="pick"':''}>${esc(x)}</td>`).join('')}</tr>`).join('')}</tbody></table>`;break;
 case 'list':root='list '+variant;element='list';html=it.map(x=>`<div class="item">${name(typeof x==='string'?{name:x}:x)}${note(x)}</div>`).join('');break;
 case 'steps':root='steps'+(b.column?' col':'');element='steps';html=it.map((x,i)=>`<div class="step"><span class="mark">${esc(x.mark||String(i+1).padStart(2,'0'))}</span>${name(x)}${note(x)}</div>`).join('');break;
 case 'timeline':root='track '+variant;element='timeline';html=it.map(x=>`<div class="stop${x.on?' on':''}"><div class="kick">${esc(x.kick||'')}</div>${name(x)}${note(x)}</div>`).join('');break;
 case 'agenda':root='agenda';element='agenda';html=it.map((x,i)=>`<div class="entry${x.on?' on':''}"><span class="mark">${esc(x.mark||String(i+1).padStart(2,'0'))}</span>${name(x)}${note(x)}</div>`).join('');break;
 case 'image':root='frame';element='image-frame';html='<div class="seat" data-ph="1"></div>';break;
 case 'callout':root='callout';element='callout';html=`<p>${esc(b.text)}</p>`;break;
 case 'quote':root='quote '+variant;element='quote';html=`<blockquote>${esc(b.text)}</blockquote><div class="by"><div class="seat avatar" data-ph="1"></div>${name(b)}${note(b)}</div>`;break;
 case 'venn':root='venn';element='venn';html=it.map((x,i)=>`<div class="set${i===1?' on':''}">${name(x)}</div>`).join('');if(b.name)html+=`<div class="core">${esc(b.name)}</div>`;break;
 case 'pyramid':root='pyramid';element='pyramid';html=it.map(x=>`<div class="level">${name(x)}${note(x)}</div>`).join('');break;
 case 'architecture':root='arch';element='architecture';html=it.map(x=>`<div class="layer">${name(x)}${(x.chips||[]).map(s=>`<span class="chip">${esc(s)}</span>`).join('')}</div>`).join('');break;
 case 'hierarchy':root='org';element='hierarchy';html=`<div class="root">${esc(b.name)}</div>`+it.map(x=>`<div class="branch"><div class="node">${esc(x.name)}</div>${(x.children||[]).map(y=>`<div class="leaf">${esc(y)}</div>`).join('')}</div>`).join('');break;
 case 'pills':return `<div class="stack"${where(b.at)}>${it.map(x=>`<div class="pill ${variant}" ${scope('pill')}><div class="parts">${icon(x.icon)}${name(x)}${note(x)}</div></div>`).join('')}</div>`;
 case 'gauge':return `<div class="stack"${where(b.at)}>${it.map(x=>`<div class="meter" ${scope('gauge')} style="--v:${x.value}">${name(x)}<div class="fig">${esc(x.value+'%')}</div></div>`).join('')}</div>`;
 default:throw Error('Unsupported assembly block: '+b.kind);
 }
 let extra=(b.kind==='bars'||b.kind==='lines')?`--max:${b.max||100};--blueprint-06-count:${it.length};`:'';
 let pos=b.at?`grid-column:${b.at[0]} / span ${b.at[1]};grid-row:${b.at[2]} / span ${b.at[3]};`:'';
 return `<div class="${root}" ${scope(element)} style="${pos}${extra}">${html}</div>`;
}
const palettes={
 '042':{'--accent':'#2454cd','--accent-soft':'#e8effc','--tone-1':'#2454cd','--tone-2':'#5480db','--tone-3':'#91b3ec','--tone-4':'#b4cbef'},
 '044':{'--accent':'#161616','--accent-ink':'#ffffff','--accent-soft':'#ededed','--tone-1':'#777777','--tone-2':'#989898','--tone-3':'#b4b4b4','--tone-4':'#d4d4d4'},
 '045':{'--accent':'#385bd7','--accent-soft':'#edf1fc','--tone-1':'#385bd7','--tone-2':'#708be1','--tone-3':'#aab9ee','--tone-4':'#d2daf6'},
 '046':{'--accent':'#505d98','--accent-soft':'#eeeef4','--tone-1':'#39417d','--tone-2':'#7377ac','--tone-3':'#9d9fc4'},
 '047':{'--accent':'#174b72','--accent-soft':'#edf3fa','--tone-1':'#4c9cf8','--tone-2':'#20ba91','--tone-3':'#f2b83d'},
 '048':{'--accent':'#3a5db0','--accent-soft':'#edf1f8','--tone-1':'#3a5db0','--tone-2':'#8097c6','--tone-3':'#a8b4d1'}
};
export function renderAssembly(deck,s){
 let tokens=Object.entries(s.dark?{}:palettes[deck.id]||{}).map(([k,v])=>k+':'+v).join(';');
 const attrs=`data-deck="${deck.id}" data-slide="${s.id}" style="${tokens}"`;
 if(s.cover)return `<section class="slide cover${s.dark?' dark':''}" ${attrs}><div class="page"><div class="deco"></div><div class="lockup at-left"><p class="kicker">${esc(s.kicker||deck.title)}</p><h1 class="title">${esc(s.title)}</h1><p class="lead">${esc(s.lead||'')}</p></div><p class="meta">${esc(s.meta||'MIRI COMPANY · 20XX')}</p></div></section>`;
 return `<section class="slide${s.dark?' dark':''}" ${attrs}><div class="page"><header class="head"><p class="kicker">${esc(s.kicker||deck.title)}</p><h1 class="title">${esc(s.title)}</h1>${s.lead?`<p class="lead">${esc(s.lead)}</p>`:''}</header><div class="body">${s.blocks.map(blockHTML).join('')}</div></div><footer class="foot"><span class="deck">MIRI COMPANY</span><span class="src">BLUEPRINT 06</span><span class="no">${s.id.replace('slide_','')}</span></footer></section>`;
}
export function assemblyDocument(title,body,css){return `<!doctype html><html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=1280"><title>${esc(title)}</title><style>${fontCSS}\n${css}\n*{box-sizing:border-box}html,body{margin:0;padding:0}body{background:#e9ebef}.slide{width:1280px;height:720px;overflow:hidden;break-after:page;print-color-adjust:exact;-webkit-print-color-adjust:exact}.slide:last-child{break-after:auto}.slide .name,.slide .note,.slide .lead,.slide .title,.slide blockquote{white-space:pre-line}.slide svg{max-width:100%;max-height:100%}.slide .mark svg{width:36px;height:36px}.slide .seat[data-ph]{background:#e5e5e5}.slide .seat[data-ph]::after{content:none!important}@page{size:1280px 720px;margin:0}</style></head><body>${body}<script>document.fonts.ready.then(()=>document.body.dataset.ready='true')</script></body></html>`}
