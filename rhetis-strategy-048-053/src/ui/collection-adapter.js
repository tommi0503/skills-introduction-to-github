/** Compile editable scene data into the Rhetis collection's native contracts.
 * Page geometry is supplied by the scene; surfaces/parts remain library-owned.
 */
export function collectionType(n){
 if(n.kind==='placeholder')return {folder:'image-frame',root:'frame',part:'seat',contract:'frame.picture@1'};
 if(n.kind==='text'&&/^[\d\s,.+−%억만원명개월건배]+$/.test(n.text||'')&&/\d/.test(n.text))return {folder:'metric',root:'stat',part:'parts',textPart:'fig',contract:'metric.figure@1'};
 if(n.kind==='text'&&n.align==='center'&&n.verticalAlign==='middle'&&n.size<=22&&n.w<=260&&n.h<=64)return {folder:'pill',root:'pill',part:'parts',textPart:'name',contract:'pill.parts@1'};
 return {folder:'card',root:'card',part:'parts',textPart:'name',contract:'card.parts@1'};
}
export function collectionNode(n,body,style,cls){
 const t=collectionType(n);return `<div class="${cls} ${t.root} overrides" data-el="strategy-blueprint-${t.folder}" data-contract="${t.contract}" style="${style}"><div class="${t.part} bridge-part">${n.kind==='text'?`<div class="${t.textPart} bridge-text">${body}</div>`:body}</div></div>`;
}
