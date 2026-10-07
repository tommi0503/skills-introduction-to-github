// Reject silent data loss (for example, spreading object keys into elements).
export function validateDefinitions(decks, graphicNames) {
 const graphics=graphicNames?new Set(graphicNames):null
 const kinds=new Set(['text','box','image','icon','line','bars','donut','table','path','chip','graphic'])
 const deckIds=new Set()
 for(const deck of decks){
  if(!deck||typeof deck.id!=='string'||deckIds.has(deck.id))throw Error('Invalid or duplicate deck ID')
  deckIds.add(deck.id)
  if(!Array.isArray(deck.slides)||!deck.slides.length)throw Error(`Empty deck ${deck.id}`)
  const slideIds=new Set()
  for(const slide of deck.slides){
   if(!slide||typeof slide.id!=='string'||slideIds.has(slide.id))throw Error(`Invalid/duplicate slide ${deck.id}`)
   slideIds.add(slide.id)
   if(!Array.isArray(slide.elements))throw Error(`Missing elements ${deck.id}/${slide.id}`)
   for(const [index,e] of slide.elements.entries()){
    const label=`${deck.id}/${slide.id} element ${index}`
    if(!e||typeof e!=='object'||Array.isArray(e)||!kinds.has(e.kind))throw Error(`Invalid element object: ${label}`)
    for(const field of ['x','y','w','h'])if(typeof e[field]!=='number'||!Number.isFinite(e[field]))throw Error(`Invalid ${field}: ${label}`)
    for(const [field,value] of Object.entries(e))if(typeof value==='number'&&!Number.isFinite(value))throw Error(`Nonfinite ${field}: ${label}`)
    if(e.text!==undefined&&typeof e.text!=='string')throw Error(`Invalid text: ${label}`)
    if(e.kind==='text'&&e.text===undefined&&!e.runs?.length)throw Error(`Missing text content: ${label}`)
    if(e.runs&&!e.runs.every(r=>r&&typeof r.text==='string'))throw Error(`Invalid text runs: ${label}`)
    if(e.kind==='icon'&&typeof e.icon!=='string')throw Error(`Missing icon name: ${label}`)
    if(e.kind==='graphic'&&typeof e.graphic!=='string')throw Error(`Missing vector scene name: ${label}`)
    if(e.kind==='graphic'&&graphics&&!graphics.has(e.graphic))throw Error(`Unregistered vector scene ${e.graphic}: ${label}`)
    if(e.values&&!e.values.every(v=>typeof v==='number'&&Number.isFinite(v)))throw Error(`Invalid chart data: ${label}`)
    if(e.innerRatio!==undefined&&(e.innerRatio<0||e.innerRatio>=1))throw Error(`Invalid donut inner radius: ${label}`)
    if(e.points&&!e.points.every(p=>p&&Number.isFinite(p.x)&&Number.isFinite(p.y)))throw Error(`Invalid path point: ${label}`)
    if(e.rows&&!e.rows.every(row=>Array.isArray(row)&&row.every(cell=>typeof cell==='string')))throw Error(`Invalid table cells: ${label}`)
    if('italic' in e)throw Error(`Unsupported italic field (use fontStyle): ${label}`)
    for(const field of ['tracking','leading','fontFamily','fontSize','fontWeight','gradient'])if(field in e)throw Error(`Unsupported ${field} field (use letterSpacing/lineHeight/font/size/weight or CSS gradient in fill): ${label}`)
   }
  }
 }
}
