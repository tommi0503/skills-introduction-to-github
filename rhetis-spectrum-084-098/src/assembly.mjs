// Compile authored primitives into the collection's documented HTML contracts.
// A panel owns its in-bounds text; page overrides retain reference-specific placement.
const area=n=>n.w*n.h;
const inside=(n,p)=>n.x>=p.x-.1&&n.y>=p.y-.1&&n.x+n.w<=p.x+p.w+.1&&n.y+n.h<=p.y+p.h+.1;
const figure=n=>/^\s*[+−\-]?\d[\d,.%억만원명배xX×: /년월일H분기]*\s*$/.test(n.text||'');
export function compileAssembly(slide){
 const owner=new Map(),panels=slide.elements.map((n,i)=>({n,i})).filter(({n})=>n.type==='rect'&&n.w>60&&n.h>36&&!n.rotate);
 slide.elements.forEach((n,i)=>{if(n.type!=='text'||n.rotate)return;const p=panels.filter(p=>p.i<i&&inside(n,p.n)).sort((a,b)=>b.i-a.i)[0];if(!p||p.n.opacity!==undefined)return;const covered=slide.elements.some((b,j)=>j>p.i&&j<i&&['rect','placeholder','pill','svg','icon','line'].includes(b.type)&&b.x<n.x+n.w&&b.x+b.w>n.x&&b.y<n.y+n.h&&b.y+b.h>n.y);if(!covered)owner.set(i,p.i)});
 return slide.elements.map((n,i)=>({index:i,contract:n.type==='pill'?'pill.parts@1':n.type==='placeholder'?'frame.picture@1':n.type==='text'?'metric.figure@1':'card.parts@1',element:n.type==='pill'?'pill':n.type==='placeholder'?'image-frame':n.type==='text'?'metric':'card',part:n.type==='text'?(figure(n)?'fig':'name'):null,owner:owner.get(i)??null,node:n}));
}
export function renderAssembly(slide,renderNode,esc){
 const graph=compileAssembly(slide);const children=new Map();
 for(const g of graph)if(g.owner!==null){if(!children.has(g.owner))children.set(g.owner,[]);children.get(g.owner).push(g)}
 return graph.filter(g=>g.owner===null).map(g=>{
  let out=renderNode(g.node,g.index,'assembly');
  if(g.node.type==='rect'&&children.has(g.index)){
   const part=children.get(g.index).map(c=>{const inset=g.node.stroke&&g.node.stroke!=='none'?(g.node.sw??1):0;const n={...c.node,x:c.node.x-g.node.x-inset,y:c.node.y-g.node.y-inset};let raw=renderNode(n,c.index,'replica');return raw.replace('class="node text"',`class="${c.part}" data-assembly-part="text"`).replace(' data-kind="text"',' data-kind="text"');}).join('');
   out=out.replace('<div class="parts"></div>',`<div class="parts">${part}</div>`);
  }
  return out;
 }).join('');
}
