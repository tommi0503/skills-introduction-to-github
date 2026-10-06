import {B,G,T} from '../primitives'
import type {Element,SvgShape,GraphicOptions} from '../model'
// Editable vector artwork, generated from paths and repeatable motifs rather than reference bitmaps.
const olive='#90977d', peach='#cb8577', off='#fff5ed', ink='#302d2c'
const path=(d:string,fill='none',stroke?:string,strokeWidth=1,extra:Partial<SvgShape>={}):SvgShape=>({d,fill,stroke,strokeWidth,...extra})
const ellipse=(cx:number,cy:number,rx:number,ry:number,fill:string,stroke?:string,strokeWidth=1,rotate=0):SvgShape=>path(`M ${cx-rx} ${cy} a ${rx} ${ry} 0 1 0 ${rx*2} 0 a ${rx} ${ry} 0 1 0 ${-rx*2} 0`,fill,stroke,strokeWidth,{transform:rotate?`rotate(${rotate} ${cx} ${cy})`:undefined})
const svg=(x:number,y:number,w:number,h:number,paths:SvgShape[],vb='0 0 300 450',extra:Partial<Element>={},options:GraphicOptions={})=>G(x,y,w,h,'custom',{viewBox:vb,paths,...options},extra)
const leaf=(x:number,y:number,len:number,angle:number,color:string,width=.38,stroke?:string)=>path(`M ${x} ${y} Q ${x-len*width} ${y-len*.7} ${x} ${y-len} Q ${x+len*width} ${y-len*.7} ${x} ${y} Z`,color,stroke,1,{transform:`rotate(${angle} ${x} ${y})`})
export function hangingPlant(x:number,y:number,w:number,h:number,variant='basket'):Element {
 const paths:SvgShape[]=[]
 const cactus=variant==='cactus'||variant==='diamond'
 const trailing=variant==='trail'||variant==='vine'||variant==='heart'||variant==='striped'
 if(cactus){
  paths.push(path('M150 -8 L35 185 L150 264 L268 185 Z','none',ink,1.2),path('M150 -8 L150 264 M35 185 L265 185 M89 184 L150 264 L209 184','none',ink,1),path('M80 185 L220 185 L198 258 L101 258 Z',peach,ink,1))
  paths.push(path('M127 183 L127 127 C99 132 92 94 100 78 C106 64 119 65 124 80 L125 101 L127 99 L128 57 C130 29 157 29 159 54 L159 115 C162 118 165 111 166 93 C168 76 186 79 187 96 C188 127 172 143 158 142 L159 183Z',olive),path('M138 182 L138 62 M148 174 L148 65 M133 98 L119 104 M153 132 L177 118','none',off,1))
 } else {
  paths.push(path(variant==='trail'?'M150 -12 C183 -5 178 57 150 71 C123 56 117 7 150 -12 Z':'M150 -12 C171 -9 173 36 150 52 C126 36 128 -9 150 -12 Z','none',ink,1.2),path('M150 38 L8 275 L293 275 Z','none',ink,1.2))
  if(variant==='trail') paths.push(path('M28 255 C21 322 68 342 150 342 C229 342 278 314 272 255Z',off,ink,1),...Array.from({length:8},(_,i)=>path(`M${45+i*27} 263 L${63+i*27} 307 L${42+i*27} 329`,i%2?peach:olive,ink,.4)))
  else paths.push(path('M8 275 L293 275 L250 345 L52 345Z',peach,ink,1),path('M8 275 L52 345 M293 275 L250 345 M53 275 L70 345 M150 275 L150 345 M242 275 L225 345','none',ink,.8))
  if(variant==='basket'||variant==='striped')for(let row=0;row<6;row++)paths.push(path(`M${9+row*8} ${275+row*11} L${292-row*8} ${275+row*11}`,'none',off,1.5))
  paths.push(path('M143 278 C128 184 154 155 162 148 M166 280 C202 186 173 160 198 128 M108 280 C61 236 69 216 62 205 M189 275 C256 224 246 201 258 180','none',ink,1.5))
  ;[[142,247,90,-52,off],[144,217,93,40,olive],[146,190,83,-25,olive],[162,246,97,43,off],[177,220,73,-13,olive],[193,177,77,25,olive],[92,269,63,-62,off],[72,233,65,-45,olive],[215,253,68,65,olive],[239,219,64,22,off]].forEach(([a,b,c,d,col])=>paths.push(leaf(Number(a),Number(b),Number(c),Number(d),String(col),.25,ink)))
  if(trailing){paths.push(path('M202 282 C206 315 236 318 223 355 C213 382 221 410 246 443 M110 273 C92 319 117 339 94 370','none',ink,1.5)); for(let i=0;i<5;i++){paths.push(leaf(224+i*2,333+i*22,35,i%2?70:-70,i%2?olive:off,.36,ink));paths.push(leaf(101-i*2,307+i*15,24,i%2?-65:75,olive,.45,ink))}}
 }
 if(variant==='striped')for(const shape of paths)if(shape.fill===olive)shape.fill=ink
 const vh=cactus?282:variant==='heart'||variant==='trail'?345:variant==='striped'?407:variant==='vine'?650:388
 return svg(x,y,w,h,paths,`0 0 300 ${vh}`)
}
export function pottedPlant(x:number,y:number,w:number,h:number,variant='spike'):Element {
 const shapes:SvgShape[]=[]
 if(variant.startsWith('outline')){
  const outline=variant==='outline-dark'?ink:off
  shapes.push(ellipse(150,413,112,17,'none',outline,1),path('M93 270 L222 270 L205 406 L117 406Z','none',outline,1),path('M157 271 C132 156 192 97 177 10 M157 271 C158 128 85 141 50 82 M157 271 C147 160 227 172 255 117','none',outline,1))
  for(let i=0;i<12;i++){shapes.push(leaf(158-i*2,250-i*19,90,i%2?70:-65,'none',.3,peach))}
 } else {
  shapes.push(path(variant==='large'?'M27 273 C40 360 255 360 274 273Z':'M51 311 L248 311 L229 430 L73 430Z',variant==='large'?peach:peach,ink,.8))
  if(variant==='large') shapes.push(path('M53 324 L39 450 M243 322 L264 450 M151 343 L150 450','none',ink,1.5))
  else for(let i=0;i<6;i++)shapes.push(path(`M${73+i*26} 323 l13 23 -14 20 16 25 -13 22`,off,ink,.5))
  shapes.push(path('M149 314 C148 195 152 140 157 14 M150 300 C126 222 89 177 40 162 M151 294 C195 207 223 180 286 128','none',ink,1.8))
  const leaves=variant==='large'?[[147,285,200,-55,ink],[149,260,228,-20,olive],[153,254,225,30,olive],[156,268,191,70,ink],[152,276,158,-78,peach],[150,224,195,8,olive],[151,275,205,51,off]]:[[150,311,227,0,olive],[147,295,219,-31,off],[148,282,177,32,olive],[146,311,164,-57,olive],[152,303,178,64,off],[147,315,246,-17,olive],[151,301,236,23,peach]]
  leaves.forEach(([a,b,c,d,col])=>{shapes.push(leaf(Number(a),Number(b),Number(c),Number(d),String(col),variant==='large'?.12:.21,ink)); shapes.push(path(`M${a} ${b} l0 ${-Number(c)*.9}`,'none',ink,.7,{transform:`rotate(${d} ${a} ${b})`}))})
 }
 return svg(x,y,w,h,shapes)
}
const sweaterPattern=(paths:SvgShape[],area:'sweater'|'pants',color=off)=>{
 if(area==='pants'){for(let r=0;r<7;r++)for(let c=0;c<4;c++){const px=75+c*45+r*3,py=237+r*25;if((py<288&&px<225)||(px>185&&px<233))paths.push(path(`M${px} ${py} l12 -10 10 20 Z`,olive))}}
 else for(let r=0;r<6;r++)for(let c=0;c<5;c++)paths.push(ellipse(54+c*41,90+r*23,11,11,'none',color,2))
}
export function creativePerson(x:number,y:number,w:number,h:number,pose='seated'):Element {
 const q:SvgShape[]=[]
 if(pose==='seated'){
  q.push(path('M40 208 C10 212 18 332 26 350 M20 207 L281 207 L287 362 L30 362 M53 361 L44 445 M267 361 L278 450','none',off,1.5))
  q.push(path('M118 53 C145 59 213 80 225 99 L236 174 L185 177 L121 160 L89 132Z',olive),path('M149 173 C186 159 234 191 237 233 L243 421 L198 434 L171 288 L85 258 L67 344 L32 315 L53 239 C63 214 103 188 149 173Z',ink));sweaterPattern(q,'pants')
  q.push(path('M96 123 L139 159 L190 163 L194 148 L130 131 L119 83Z',off),path('M210 101 C230 115 239 145 246 146 L272 133 L269 121 L250 125 L235 91Z',off))
  q.push(path('M186 104 L230 113 L230 153 L185 143Z',peach,ink,1),ellipse(166,44,18,23,off),path('M146 47 C135 6 177 1 182 36 C170 13 168 44 159 54Z',ink),path('M135 59 L147 76 L166 59',off))
  q.push(path('M201 425 L246 418 L269 439 L269 445 L197 449Z',peach,ink,1),path('M45 311 L79 321 L109 345 L112 357 L57 352 L35 335Z',off,ink,1),path('M201 439 L268 438 M59 344 L107 350','none',ink,1))
 } else if(pose==='female'||pose==='male'){
  const female=pose==='female'
  q.push(ellipse(139,437,130,8,'none',peach,.8))
  q.push(ellipse(female?147:165,49,21,27,'#9b654d'),path(female?'M125 50 C90 28 113 4 131 24 C154 -1 179 13 174 32 L161 34 L159 18 L147 28 L143 48Z':'M140 29 C139 -6 179 8 184 19 L191 40 L148 45Z',ink))
  if(female){
   q.push(path('M118 78 C129 65 179 69 189 94 L211 161 L161 179 L103 155Z','#f3b2b1'));sweaterPattern(q,'sweater')
   q.push(path('M98 163 L190 167 L210 255 L67 254Z','#d0a291'),path('M70 247 L205 250 L203 424 L151 425 L133 286 L111 417 L55 416Z','#bd8469'))
   q.push(path('M185 93 L212 110 L247 92 L271 105 L267 115 L248 112 L213 131 L195 124Z',peach),path('M111 97 L80 170 L120 183 L140 177 L125 165 L104 163 L127 108Z',peach))
   q.push(path('M55 413 L113 418 L129 436 L123 444 L48 441Z',peach,ink,.7),path('M153 420 L204 415 L226 433 L223 443 L151 443Z',peach,ink,.7))
  }else{
   q.push(path('M131 77 C141 71 194 74 204 90 L236 178 L200 207 L105 178 L119 104Z',olive),path('M123 181 L210 178 L220 401 L173 409 L157 255 L137 406 L88 407Z',ink))
   q.push(path('M121 93 L83 135 L32 134 L12 145 L31 153 L91 152 L140 120Z',peach),path('M203 107 L230 161 L207 202 L195 197 L208 158 L190 123Z',peach))
   q.push(path('M217 142 L246 128 L260 205 L229 217Z',off,ink,.7),path('M89 405 L134 406 L153 436 L150 442 L79 440Z',olive,ink,.8),path('M174 404 L219 399 L247 422 L243 433 L172 439Z',olive,ink,.8))
  }
 }else if(pose==='presenter'){
  q.push(ellipse(173,39,22,29,'#9b654d'),path('M148 52 C118 33 148 1 178 4 C209 5 213 35 203 54 L186 52 L187 17 L161 23 L160 48Z',ink))
  q.push(path('M142 71 L197 72 L226 160 L204 175 L138 168 L112 109Z','#f3b2b1'),path('M119 104 L55 115 L16 82 L1 89 L42 143 L126 130Z','#9b654d'),path('M218 113 L231 176 L286 199 L295 191 L243 157 L237 105Z','#9b654d'))
  q.push(path('M140 161 L208 166 L209 387 L169 391 L158 260 L149 382 L97 387 L115 218Z',off))
  for(let r=0;r<7;r++)for(let c=0;c<3;c++)q.push(path(`M${128+c*29} ${187+r*25} q-8 10 -1 19`, 'none','#f3b2b1',5))
  q.push(path('M100 382 L151 379 L154 419 L124 437 L51 439 L57 423 L94 410Z',peach,ink,1),path('M168 388 L209 388 L228 426 L259 433 L257 444 L171 445Z',peach,ink,1))
 }else if(pose==='recline'){
  q.push(path('M-11 341 Q16 273 98 287 L165 318 L166 389 M-11 343 L-4 402 L143 402','none',ink,1.1))
  q.push(path('M82 180 C84 129 110 92 144 111 C176 128 187 174 205 214 L269 351 L242 369 L187 295 L155 272 L162 356 L123 356 L79 254Z',olive,ink,.8))
  for(let r=0;r<6;r++)for(let c=0;c<4;c++){const cx=110+c*25+r*8,cy=137+r*33;if(cx<149+cy*.16&&!(cx<125&&cy>242))q.push(ellipse(cx,cy,10,12,off))}
  q.push(path('M28 147 Q42 110 91 127 L109 244 L3 242 L-3 192Z',olive),ellipse(67,104,16,22,peach),path('M39 104 C25 66 58 59 80 84 L77 98 L69 92 L66 110Z',ink),path('M37 80 C19 60 -8 99 10 116 L49 114Z',ink))
  q.push(path('M8 167 L77 174 L112 162 L117 179 L93 195 L62 203 L7 202Z',peach),path('M96 145 L133 143 L135 205 L96 202Z',ink),path('M106 174 Q123 151 130 171 L124 190 L113 191Z',peach),path('M130 337 L166 340 L187 403 Q196 427 179 433 L147 422 L132 397Z',peach),path('M235 348 L268 338 L292 394 Q307 414 289 426 L258 416 L239 390Z',peach))
  q.push(path('M173 414 l-5 10 M180 413 l-5 12 M185 410 l-3 11 M283 409 l-3 11 M290 409 l-2 10','none',ink,1))
 }else if(pose==='laptop'){
  q.push(path('M18 252 L127 267 L89 374 L24 377 L13 328Z',ink))
  q.push(path('M10 185 C104 193 154 218 205 270 L260 395 L219 416 L171 324 L85 284 L48 320 L108 384 L85 408 L5 342Z','#ae7764'))
  q.push(path('M-35 89 C-2 71 59 60 97 85 L128 188 L42 218 L-40 169Z','#f3b2b1'))
  for(let i=0;i<8;i++)q.push(path(`M${-30+i*19} 98 q38 15 11 41 q-25 25 15 55`,'none',off,2))
  q.push(ellipse(48,38,22,27,off),path('M27 45 C11 6 50 -6 70 16 L68 36 L50 18 L39 42Z',ink))
  q.push(path('M92 113 L134 161 L183 168 L184 181 L122 179 L83 152Z',off),path('M163 178 L187 168 L204 172 L210 185 L183 186Z',off))
  if(pose==='laptop') q.push(path('M185 185 L290 185 L300 74 L289 74 L273 172 L193 172Z',ink),path('M128 195 L299 195 L300 210 L130 210Z',off,ink,1),path('M145 210 L139 440 M288 210 L294 446','none',ink,1))
  else q.push(path('M151 138 L197 126 L215 176 L174 194Z',ink),path('M-15 337 Q75 282 133 332 L142 381 M-10 339 L-7 418 L106 418','none',off,1.5))
  q.push(path('M217 401 L245 392 L283 419 L297 429 L297 441 L229 433Z',off,ink,1),path('M83 385 L112 375 L144 408 L141 427 L102 423 L83 411Z',off,ink,1),path('M219 431 L297 441 M107 425 L139 427','none',peach,8))
 }else if(pose==='thumbs'||pose==='tablet'){
  q.push(ellipse(149,437,122,6,'none',ink,.6),ellipse(142,43,24,29,pose==='thumbs'?'#af7b62':off),path('M113 32 C109 4 160 4 168 27 L170 38 L147 24 L118 43Z',ink))
  q.push(path('M113 83 L174 80 L203 218 L102 217 L78 119Z','#f3b2b1'),path('M101 204 L194 211 L194 319 L159 326 L141 249 L111 321 L72 316Z',pose==='thumbs'?ink:'#aa765f'))
  if(pose==='thumbs')q.push(path('M100 91 L82 151 L36 111 L27 93 L18 87 L7 99 L9 123 L79 195 L124 128Z','#af7b62'),path('M177 91 L202 160 L245 113 L261 91 L275 86 L281 99 L269 123 L205 196 L164 140Z','#af7b62'),path('M95 316 L128 323 L122 396 L99 395Z','#af7b62'),path('M163 319 L193 316 L203 396 L178 398Z','#af7b62'),path('M98 374 L122 375 L123 407 L90 409Z',off),path('M174 374 L201 373 L207 408 L177 408Z',off))
  else {q.push(path('M114 320 L91 388 L122 411 L157 390 L155 379 L127 382 L146 317Z','#aa765f'),path('M177 323 L222 363 L232 401 L198 410 L186 378 L158 363Z','#aa765f'),path('M153 114 L235 147 L214 219 L130 183Z',ink),path('M118 115 L91 169 L145 189 L156 182 L116 167 L141 134Z',off),path('M175 104 L221 139 L210 159 L179 135Z',off)); for(let r=0;r<5;r++)q.push(path(`M110 ${87+r*23} q22 -15 55 7`,'none',olive,1.8))}
  q.push(path('M90 400 L129 401 L162 426 L161 439 L73 438Z',peach,ink,1),path('M179 400 L210 399 L246 424 L239 438 L173 438Z',peach,ink,1))
 }
 if(pose==='female')q.push(path('M77 247 L204 247 M91 168 L76 251 M110 165 L105 252 M130 167 L138 250 M160 169 L174 251 M183 174 L198 250 M123 281 L137 397','none',ink,.8))
 if(pose==='male')q.push(path('M150 85 L162 113 L175 85 M119 173 L210 175 M146 178 L148 291 M135 204 L107 389 M191 204 L203 389','none',off,.8))
 return svg(x,y,w,h,q)
}
export function creativeRoom(variant:'seated'|'discussion'|'presenter'|'sofa'):Element[] {
 if(variant==='seated')return [hangingPlant(750,-24,209,321,'vine'),pottedPlant(774,368,190,438,'outline'),svg(879,362,645,538,[path('M0 116 L597 116 L597 149 L0 149Z',off),path('M74 148 L45 538 M578 148 L607 538','none',ink,1.6),path('M59 20 L106 20 L106 88 L59 88Z',peach,ink,1),path('M106 34 C145 32 144 72 108 72','none',ink,1.2)],'0 0 645 538')]
 if(variant==='discussion')return [svg(987,57,613,782,[path('M198 43 L394 43 L394 402 L198 402Z M216 43 L216 401 M198 237 L394 237 M83 275 L347 275 L347 548 L83 548Z M83 331 L347 331 M168 331 L168 548 M258 331 L258 548 M130 283 L156 283','none',peach,1),path('M44 143 Q78 81 112 143 L105 202 L58 202Z M82 107 L82 207 M35 202 L126 202 L112 275 L49 275Z','none',peach,1),path('M213 126 C211 72 301 74 300 122 C299 158 268 158 244 155 L225 178 L229 153 C220 150 213 142 213 126Z',peach),path('M236 118 L274 118 M236 126 L270 126','none',off,2)],'0 0 613 782')]
 if(variant==='presenter')return [svg(788,107,812,704,[path('M1 0 L299 0 L299 237 L1 237Z',off,ink,1.2),path('M1 0 L299 0 L299 14 L1 14Z M1 222 L299 222 L299 237 L1 237Z',off,ink,1.2),path('M147 237 L147 259 M141 259 Q149 270 156 259','none',ink,1.2),path('M64 73 L103 73 L103 207 L64 207Z M129 115 L166 115 L166 207 L129 207Z M195 151 L235 151 L235 207 L195 207Z',peach),path('M56 37 L210 124 L263 151 M56 37 L73 41 M56 37 L63 52','none',ink,1.3),path('M261 201 L713 201 Q745 200 741 239 L718 498 L222 498 L205 259 Q199 205 239 204 M275 238 L267 468 L670 468 L688 238Z M246 498 L230 591 M690 498 L705 591','none',off,1.5),path('M753 464 L812 464 M772 464 L793 650 M789 462 C802 349 759 281 746 238 M789 399 C744 377 746 364 723 352 M791 356 C837 324 817 299 812 286','none',peach,1)],'0 0 812 704'),pottedPlant(798,538,160,276)]
 return [pottedPlant(713,393,190,434,'outline-dark'),svg(986,454,614,373,[path('M14 105 Q9 72 35 79 L160 107 M160 49 Q158 18 203 10 L578 10 Q618 8 614 59 L581 296 L182 296 L149 162 M183 39 L171 269 L556 269 L586 40 M31 119 L96 300 L577 300 M97 300 L99 371 M541 300 L574 371','none',ink,1.2)],'0 0 614 373')]
}
function engravedLeaf(cx:number,cy:number,len:number,angle:number,color:string):SvgShape[]{
 const result=[leaf(cx,cy,len,angle,'none',.37,color),path(`M${cx} ${cy} L${cx} ${cy-len}`,'none',color,1,{transform:`rotate(${angle} ${cx} ${cy})`})]
 for(let j=1;j<43;j++){const t=j/43;const side=Math.sin(t*Math.PI)*len*.185;result.push(path(`M${cx} ${cy-len*t} l${side} ${-len*.055} M${cx} ${cy-len*t} l${-side} ${-len*.055}`,'none',color,1.15,{transform:`rotate(${angle} ${cx} ${cy})`}))}
 return result
}
function engravedFlower(cx:number,cy:number,r:number,color:string,fill='none'):SvgShape[]{
 const result:SvgShape[]=[]
 for(let ring=0;ring<2;ring++)for(let p=0;p<12;p++){
  const a=p*30+ring*15,rr=r*(ring?.58:1)
  result.push(path(`M${cx} ${cy} C${cx-rr*.34} ${cy-rr*.32} ${cx-rr*.45} ${cy-rr*.72} ${cx-rr*.25} ${cy-rr*.84} L${cx-rr*.18} ${cy-rr*.93} L${cx-rr*.07} ${cy-rr*.88} L${cx+rr*.02} ${cy-rr*.98} L${cx+rr*.14} ${cy-rr*.92} C${cx+rr*.38} ${cy-rr*.85} ${cx+rr*.55} ${cy-rr*.51} ${cx} ${cy}Z`,fill,color,1.15,{transform:`rotate(${a} ${cx} ${cy})`}))
  for(let j=0;j<14;j++)result.push(path(`M${cx+(j-7)*1.6} ${cy-rr*.12} Q${cx-rr*.21+j*rr*.032} ${cy-rr*.55} ${cx-rr*.19+j*rr*.029} ${cy-rr*.88}`,'none',color,.9,{transform:`rotate(${a} ${cx} ${cy})`}))
 }
 result.push(ellipse(cx,cy,r*.2,r*.17,fill,color,1.5)); for(let i=0;i<90;i++){const a=i*2.4;result.push(ellipse(cx+Math.cos(a)*r*.14*(i/90),cy+Math.sin(a)*r*.14*(i/90),1.5,1.5,color))}return result
}
export function blueBotanical(id:string):Element {
 const color='#7697c8',q:SvgShape[]=[]
 if(id==='s014'){
  q.push(path('M25 900 C72 571 292 294 211 -20 M1448 900 C1483 696 1293 444 1460 66','none',color,2.4),...engravedFlower(195,60,255,color),...engravedFlower(1490,925,172,color))
  ;[[45,754,304,57],[155,583,257,-41],[206,424,237,66],[307,213,193,47],[53,651,225,-33],[1378,715,200,-65],[1426,472,240,41],[1397,532,184,-72],[1494,366,233,14],[1388,655,270,-42]].forEach(([a,b,c,d])=>q.push(...engravedLeaf(a,b,c,d,color)))
 }else{
  q.push(path('M845 -40 C925 135 1101 261 1279 425 C1424 575 1533 747 1620 930 M1038 146 L1200 110 M1160 330 L1000 350 M1370 526 L1530 430','none',color,2))
  ;[[920,120,193,-58],[970,36,176,47],[1200,140,219,59],[1122,276,211,-60],[1004,363,182,-92],[1444,235,222,34],[1368,490,182,-58],[1494,720,211,67],[1420,719,181,-41],[1530,818,242,-27]].forEach(([a,b,c,d])=>q.push(...engravedLeaf(a,b,c,d,color)))
  ;[[1281,347,100],[1176,493,84],[1435,491,95],[1456,660,122],[1558,853,78]].forEach(([a,b,c])=>q.push(...engravedFlower(a,b,c,color)))
 }
 return svg(0,0,1600,900,q,'0 0 1600 900')
}
export function flask(x:number,y:number,w:number,h:number,conical=false):Element {
 const teal='#598e86',blue='#a4d4d1',yellow='#eef9e6',q:SvgShape[]=[]
 if(conical){q.push(path('M103 20 L177 20 L177 167 L268 378 Q285 427 253 442 L34 442 Q4 425 23 383 L105 167Z',teal),path('M86 222 L206 222 L262 393 Q273 414 250 424 L49 424 Q25 414 37 387Z',blue),ellipse(140,21,44,18,'#ebacc2'),ellipse(140,21,33,10,yellow),ellipse(149,404,105,16,teal),path('M121 71 L126 171 L61 359 Q55 377 45 373 L42 370 L111 167 L109 73Z',yellow))}
 else{q.push(path('M103 18 L189 18 L184 153 C325 207 319 401 201 438 C79 483 -4 396 12 288 C23 217 50 180 106 156Z',teal),path('M40 249 C68 211 237 208 273 249 C292 339 257 414 172 427 C91 441 35 391 29 335Z',blue),ellipse(150,249,112,25,blue),ellipse(146,20,53,18,'#ebacc2'),ellipse(146,20,43,9,yellow),path('M129 73 L134 162 Q51 223 57 270 L48 309 Q14 207 118 145 L118 73Z',yellow),path('M33 324 C38 380 67 411 104 419 L115 411 C61 376 56 350 53 316Z',yellow))}
 for(let i=0;i<7;i++)q.push(ellipse(73+(i%3)*60,271+Math.floor(i/3)*42,9,9,conical?teal:'#98596d'))
 return svg(x,y,w,h,q)
}
export function microbe(x:number,y:number,w:number,h:number,variant=0):Element {
 const q:SvgShape[]=[path('M240 -20 C315 -28 444 35 600 141 L600 213 C470 126 363 75 281 64 C229 56 211 89 253 111 C383 155 514 229 600 300 L600 368 C480 288 364 231 245 193 C193 177 183 206 217 224 L531 386 C561 402 561 433 530 438 C510 440 485 422 471 415 L184 273 C144 253 126 221 135 196 C142 178 168 161 190 159 C222 147 216 137 188 126 C171 120 159 130 132 126 C96 118 84 87 104 73 C133 53 152 72 175 65 C196 57 171 21 191 1 C204 -11 223 -16 240 -20Z','#a3ceb7')]
 ;[[285,29,51,17,'#a36679',2],[493,130,27,12,'#d9cc73',36],[203,159,33,10,'#d9cc73',15],[373,222,45,16,'#a36679',24],[477,315,34,11,'#d9cc73',25],[262,258,37,12,'#a36679',23]].forEach(([cx,cy,rx,ry,col,ang])=>q.push(ellipse(Number(cx),Number(cy),Number(rx),Number(ry),String(col),undefined,0,Number(ang))))
 const transform=variant?'rotate(180 300 225)':undefined
 if(transform)q.forEach(shape=>shape.transform=shape.transform?transform+' '+shape.transform:transform)
 return svg(x,y,w,h,q,'0 0 600 450')
}
export function neuron(x:number,y:number,w:number,h:number,color=peach):Element {
 const q:SvgShape[]=[]
 const points:string[]=[];for(let i=0;i<18;i++){const a=i*Math.PI/9,rad=i%2?40:118;points.push(`${150+Math.cos(a)*rad},${150+Math.sin(a)*rad}`)}
 q.push(path('M'+points.join(' L')+'Z',color))
 for(let i=0;i<9;i++){const a=i*Math.PI*2/9,cx=150+Math.cos(a)*92,cy=150+Math.sin(a)*92;q.push(path(`M${cx} ${cy} l${Math.cos(a+.7)*35} ${Math.sin(a+.7)*35} M${cx} ${cy} l${Math.cos(a-.65)*34} ${Math.sin(a-.65)*34}`,'none',color,5,{strokeLinecap:'round'}))}
 q.push(ellipse(150,150,16,16,'#f6f6f2'));return svg(x,y,w,h,q,'0 0 300 300')
}
function flower(cx:number,cy:number,r:number,fill:string,center:string,petals=5):SvgShape[]{
 const q:SvgShape[]=[];for(let i=0;i<petals;i++){const angle=i*360/petals;q.push({...ellipse(cx,cy-r*.46,petals>7?r*.115:r*.33,r*.55,fill),transform:`rotate(${angle} ${cx} ${cy})`})}q.push(ellipse(cx,cy,r*.25,r*.25,center));return q
}
function fern(x:number,y:number,len:number,angle:number,color:string):SvgShape[]{
 const q=[path(`M${x} ${y} L${x} ${y-len}`,'none',color,3,{transform:`rotate(${angle} ${x} ${y})`})];for(let i=0;i<12;i++){const cy=y-i*len/12,l=(1-i/14)*len*.21;q.push(leaf(x,cy,l,-55,color,.22),leaf(x,cy,l,55,color,.22));q[q.length-1].transform=`rotate(${angle+55} ${x} ${cy})`;q[q.length-2].transform=`rotate(${angle-55} ${x} ${cy})` }return q
}
export function floralBackdrop():Element[] {
 const q:SvgShape[]=[]
 const gold='#efbe5d',rust='#bf5132',lp='#f1b6bf',sage='#879e88'
 ;[[56,72,150,lp,gold,14],[421,126,152,off,rust,5],[609,161,157,lp,gold,14],[865,176,176,off,rust,5],[1060,-10,169,rust,gold,12],[1320,64,169,sage,gold,5],[1600,83,167,rust,gold,12],[33,369,170,sage,gold,5],[451,310,115,lp,gold,5],[415,490,112,lp,gold,5],[568,380,76,lp,gold,5],[293,560,80,lp,gold,5],[329,720,175,rust,gold,14],[137,905,177,off,rust,5],[648,842,162,rust,gold,14],[874,886,160,sage,gold,5],[1375,833,94,lp,gold,5],[1490,890,100,lp,gold,5]].forEach(([a,b,c,d,e,p])=>q.push(...flower(Number(a),Number(b),Number(c),String(d),String(e),Number(p))))
 q.push(...fern(248,432,473,0,sage),...fern(-30,840,385,25,sage),...fern(1250,958,318,27,sage),path('M1410 110 C1440 342 1647 440 1480 696','none',sage,4))
 ;[[1460,230],[1530,351],[1600,465],[1540,640]].forEach(([a,b])=>q.push(...flower(a,b,56,lp,gold,5)))
 return [B(0,0,1600,900,gold),svg(0,0,1600,900,q,'0 0 1600 900')]
}
export function buildingDots():Element[] {
 const result:Element[]=[]
 for(const [x,y,w,h,variant] of [[0,0,420,415,0],[1110,604,490,296,1]]){
  const points:SvgShape[]=[]
  for(let r=0;r<h/9+4;r++)for(let c=0;c<w/8+4;c++){
   const px=c*8+Math.sin(r*.14)*28*(1-c/(w/8)),py=r*9+Math.sin(c*.2)*12
   const strength=Math.max(.1,1-c/(w/8)*.66)
   points.push(ellipse(variant?w-px:px,variant?h-py:py,1.1*strength,2.5*strength,'#fffdf4',undefined,0,(r+c)*.4))
  }
  result.push(svg(x,y,w,h,points,`0 0 ${w} ${h}`,{opacity:.88,mask:variant?'linear-gradient(135deg,transparent,#000 60%)':'linear-gradient(135deg,#000,transparent 90%)'}))
 }
 return result
}
const manuscript='The story of our time\nA journey through history\nIn every place and every day\nWe share our dreams and hopes\nMemories of the world\nLetters from a distant friend\nThe spirit of an age\nA record for tomorrow\nWith kindness and curiosity'
function letter(x:number,y:number,w:number,h:number,rotate=0,color='#e9dfc4'):Element[]{
 return [B(x,y,w,h,color,{rotate,clipPath:'polygon(1% 0,95% 0,100% 17%,94% 34%,100% 51%,94% 70%,99% 88%,90% 100%,0 98%,4% 70%,0 47%,3% 25%)'}),T(x,y,w,h,manuscript,20,{clipPath:'polygon(1% 0,95% 0,100% 17%,94% 34%,100% 51%,94% 70%,99% 88%,90% 100%,0 98%,4% 70%,0 47%,3% 25%)',padding:12,font:'Caveat Brush',weight:400,color:'#81734f',lineHeight:1.5,rotate,opacity:.65,allowClip:true,clipReason:'Source manuscript is a cropped background ornament'})]
}
function flourish(x:number,y:number,w:number,h:number,color='#7d6c44'):Element {
 const q:SvgShape[]=[]
 q.push(path('M45 290 C-43 258 20 122 93 197 C117 241 47 270 38 218 C25 178 74 172 77 206 M132 429 C211 333 72 217 118 128 C189 -4 293 65 229 164 C192 210 160 147 195 127 C237 103 257 159 221 209 C147 300 183 351 277 376 M122 128 C66 103 14 60 49 20 C79 -13 139 11 131 50 C127 73 106 83 88 64','none',color,2.1))
 for(let i=0;i<7;i++)q.push(leaf(126+i*6,151+i*39,68,i%2?74:-71,'none',.29,color))
 return svg(x,y,w,h,q)
}
export function craftBackdrop(variant:'introduction'|'facts'):Element[] {
 const q:Element[]=[B(0,0,1600,900,'radial-gradient(ellipse at 65% 25%,#c4a076,#b99268 72%,#a48056)'),G(0,0,1600,900,'grain',{color:'#765330',frequency:'.022',seed:31},{opacity:.3}),G(0,0,1600,900,'grain',{color:'#ece3ca',frequency:'.53',seed:31},{opacity:.14})]
 if(variant==='introduction')q.push(...letter(-70,13,226,449,-5,'#ded3ac'),...letter(1427,502,252,465,6,'#ded3ac'))
 else q.push(B(1162,-45,474,248,'#e1d7b8',{clipPath:'polygon(0 0,100% 0,100% 100%,87% 91%,73% 99%,53% 85%,39% 96%,22% 89%,0 94%)'}),B(-37,673,531,257,'#e1d7b8',{clipPath:'polygon(0 0,20% 4%,37% 0,55% 6%,68% 1%,87% 9%,100% 0,100% 100%,0 100%)'}),G(1162,-35,458,244,'botanical',{color:'#443f2f',accent:'#847758',variant:'branch',stroke:1.5}),G(-70,688,540,222,'botanical',{color:'#443f2f',accent:'#847758',variant:'branch',stroke:1.5}))
 return q
}
export function quill(x:number,y:number,w:number,h:number):Element {
 const q:SvgShape[]=[path('M41 435 C101 349 212 165 260 15 C272 20 299 116 253 181 C250 115 217 168 243 210 C216 205 181 218 209 250 C178 242 147 280 161 296 C139 286 120 324 116 344 C85 345 54 411 41 435Z','#e8e5d4','#8a815b',1.4),path('M40 435 C110 344 199 176 259 16','none','#6a6849',2.4)]
 for(let i=0;i<30;i++){const t=i/30,a=252-t*160,b=36+t*312;q.push(path(`M${a} ${b} q${25-t*12} ${32-t*15} ${20+t*5} ${43-t*20} M${a} ${b} q${-25-t*28} 3 ${-33-t*29} -7`,'none','#9f9b7d',.75))}
 return svg(x,y,w,h,q)
}
export function hourglass(x:number,y:number,w:number,h:number):Element {
 const q:SvgShape[]=[ellipse(150,22,120,19,'#f0ebcd','#686552',4),ellipse(150,428,129,20,'#f0ebcd','#686552',4),path('M41 25 L39 425 M258 27 L258 423','none','#777766',12),path('M47 31 C34 120 73 168 139 226 C78 280 52 336 50 414 L248 414 C245 332 215 276 162 226 C228 164 263 114 250 31Z','#efedda','#827e6c',2),path('M67 90 L232 90 C220 165 183 188 151 220 C119 185 75 149 67 90Z','#bab29c'),path('M72 396 C104 349 134 330 150 276 C163 332 195 352 231 396Z','#a59c87'),path('M150 220 L150 304','none','#99927d',3),path('M64 58 C53 128 99 169 124 192 M233 279 Q254 342 239 391','none','#fffef1',8,{opacity:.8}),ellipse(150,23,126,15,'#c9c6b2','#7a7765',3),ellipse(150,425,135,17,'#b0ad97','#6f6c5e',4)]
 for(let i=0;i<17;i++)q.push(path(`M${38+i*14} 14 l8 16 M${27+i*15} 416 l8 16`,'none','#6c685b',.9))
 return svg(x,y,w,h,q)
}
export function pocketWatch(x:number,y:number,w:number,h:number):Element[] {
 const q=[ellipse(150,254,143,155,'#aeaa83','#6e7254',3),ellipse(150,254,129,139,'#eeebd7','#929b6c',3),ellipse(150,254,116,125,'#e4e4c8','#b7bc96',2),path('M151 110 L152 72 C105 34 124 0 156 12 C201 34 166 71 151 74','none','#c1c19a',12),path('M130 92 L173 92 L178 119 L123 119Z','#b1b493','#6e7254',2),path('M150 255 L95 178 M151 254 L231 224','none','#263c35',4),ellipse(150,254,7,7,'#354238')]
 for(let i=0;i<60;i++){const a=i*Math.PI/30;q.push(path(`M${150+Math.sin(a)*107} ${254-Math.cos(a)*116} L${150+Math.sin(a)*(i%5?101:96)} ${254-Math.cos(a)*(i%5?110:104)}`,'none','#757b5e',i%5?1:2))}
 const elements:Element[]=[svg(x,y,w,h,q)]
 const numbers=['XII','I','II','III','IV','V','VI','VII','VIII','IX','X','XI'];numbers.forEach((n,i)=>{const a=i*Math.PI/6;elements.push(T(x+w*(.5+Math.sin(a)*.29)-w*.095,y+h*(.565-Math.cos(a)*.21)-h*.024,w*.19,h*.065,n,22,{font:'Tinos',weight:400,color:'#536447',align:'center',lineHeight:1}))})
 return elements
}
export function vintageBackdrop(id:string):Element[] {
 const q:Element[]=[B(0,0,1600,900,'radial-gradient(ellipse at 44% 41%,#d5c89a,#c8b883 80%,#b8a778)'),G(0,0,1600,900,'grain',{color:'#79653d',frequency:'.017',seed:18},{opacity:.34}),G(0,0,1600,900,'grain',{color:'#f6efdc',frequency:'.71',seed:18},{opacity:.21})]
 if(id==='s005')q.push(...letter(-45,-31,321,452,-6),...letter(1322,-71,334,417,9),...letter(988,804,620,185,-3),flourish(1384,351,243,466),G(0,503,488,397,'grid',{color:'#aa9d73',spacing:37,stroke:.5},{opacity:.48}),G(1120,0,480,333,'contour-lines',{color:'#aa9c6d',spacing:16,stroke:.7},{opacity:.45}))
 if(id==='s006')q.push(flourish(-51,-40,266,382),...letter(1282,-55,361,502,12),...letter(-13,822,977,153,-1),flourish(1305,602,334,351))
 if(id==='s007')q.push(...letter(-54,-55,483,662,-2),...letter(1192,-49,422,676,8),flourish(392,-97,309,642),G(161,4,560,398,'custom',{viewBox:'0 0 600 400',paths:[path('M281 -40 L336 118 L521 134 L391 226 L424 391 L281 287 L125 389 L169 226 L20 133 L222 118Z','none','#ece8d9',4)]}))
 if(id==='s008')q.push(...letter(1175,-88,453,420,5),...letter(-64,560,348,392,-5),flourish(1258,314,359,507),G(1034,0,497,460,'custom',{viewBox:'0 0 500 460',paths:[path('M236 -56 L294 128 L476 132 L332 244 L383 423 L232 303 L64 409 L120 234 L-28 129 L170 127Z','none','#ede6d3',4)]}))
 return q
}
function vintageBloom(cx:number,cy:number,r:number):SvgShape[]{
 const q:SvgShape[]=[],cream='#e4d9b9',blue='#344b50'
 for(let i=0;i<5;i++){
  const rotate=`rotate(${i*72} ${cx} ${cy})`
  q.push(path(`M${cx} ${cy} C${cx-r*.14} ${cy-r*.19} ${cx-r*.58} ${cy-r*.28} ${cx-r*.42} ${cy-r*.73} C${cx-r*.58} ${cy-r*.86} ${cx-r*.31} ${cy-r*1.1} ${cx-r*.15} ${cy-r*.96} C${cx+r*.08} ${cy-r*1.15} ${cx+r*.49} ${cy-r*.87} ${cx+r*.35} ${cy-r*.68} C${cx+r*.53} ${cy-r*.3} ${cx+r*.16} ${cy-r*.18} ${cx} ${cy}Z`,cream,blue,2.8,{transform:rotate}))
  for(let k=0;k<6;k++)q.push(path(`M${cx+k*2} ${cy-r*.2} Q${cx-r*.12+k*4} ${cy-r*.47} ${cx-r*.24+k*9} ${cy-r*.75}`,'none','#ab9471',1.3,{transform:rotate}))
 }
 q.push(ellipse(cx,cy,r*.19,r*.16,blue),ellipse(cx,cy,r*.08,r*.07,'#a98c65'));return q
}
export function botanicalVintageBackdrop():Element[] {
 const q:SvgShape[]=[],cream='#dfd5b8',blue='#344c4d'
 ;[[65,456,67],[32,654,90],[229,657,85],[190,849,97],[1410,70,91],[1545,165,97],[1568,7,83],[99,873,95],[349,839,64]].forEach(([a,b,c])=>q.push(...vintageBloom(a,b,c)))
 ;[[116,597,124,-52],[204,487,135,40],[257,777,136,38],[57,846,142,-26],[385,804,120,63],[1485,292,177,-26],[1367,84,142,-59],[1456,207,149,25],[1568,381,175,29],[1462,840,185,-32],[214,680,131,-23],[168,831,179,25]].forEach(([a,b,c,d])=>{q.push(leaf(a,b,c,d,blue,.24));for(let i=0;i<18;i++)q.push(path(`M${a} ${b-c*i/18} l${Math.sin(i/18*Math.PI)*c*.11} ${-c*.07}`,'none',cream,.9,{transform:`rotate(${d} ${a} ${b})`}))})
 return [B(0,0,1600,900,'radial-gradient(ellipse at 50% 45%,#767b61,#747860 59%,#646d53)'),G(0,0,1600,900,'grain',{color:'#354b2b',frequency:'.018',seed:19},{opacity:.3}),G(0,0,1600,900,'grain',{color:'#b4b39d',frequency:'.55',seed:19},{opacity:.1}),B(0,0,545,900,cream,{clipPath:'polygon(0 0,100% 0,91% 12%,75% 16%,74% 32%,48% 40%,50% 56%,40% 67%,66% 81%,57% 100%,0 100%)'}),...letter(-122,15,501,840,-6,cream),...letter(1325,-10,340,969,0,cream),svg(0,0,1600,900,q,'0 0 1600 900')]
}
export function researchBackdrop(id:string):Element[] {
 const d=id==='s001'?'M1660 880 C1640 958 1556 951 1508 872 L1082 284 C980 143 900 129 888 288 C884 403 1015 609 1100 683 C1180 752 1216 676 1174 607 L1114 510 C1057 423 1075 375 1117 417 L1552 854 C1591 891 1628 834 1600 791':'M67 -45 C175 63 279 299 143 346 C51 385 -91 77 -42 -2 M21 17 C134 183 201 328 127 312 C77 292 -19 96 -13 44'
 const paths=[path(d,'none','#a5afc0',61,{opacity:.18,strokeLinecap:'round'}),path(d,'none','url(#glass)',53,{opacity:.55,strokeLinecap:'round'}),path(d,'none','#fafcff',35,{opacity:.26,strokeLinecap:'round'}),path(d,'none','#ffffff',5,{opacity:.52,strokeLinecap:'round',transform:'translate(-15 -8)'}),path(d,'none','#aeb7c9',3,{opacity:.27,strokeLinecap:'round',transform:'translate(17 4)'})]
 return [B(0,0,1600,900,'linear-gradient(115deg,#d9dee7 0%,#d3d9e3 39%,#f0f2f7 80%,#e8ecf3 100%)'),svg(0,0,1600,900,paths,'0 0 1600 900',{}, {gradients:[{id:'glass',x1:'0%',y1:'0%',x2:'100%',y2:'80%',stops:[{offset:'0%',color:'#fafdff',opacity:.3},{offset:'35%',color:'#ffffff',opacity:.7},{offset:'65%',color:'#bdc6d6',opacity:.65},{offset:'100%',color:'#fbfcff',opacity:.5}]}]})]
}
export function financeHead(x:number,y:number,w:number,h:number):Element {
 const green='#9bd13c',deep='#3d5500',light='#efffc9'
 return svg(x,y,w,h,[path('M419 73 C279 10 130 71 117 210 L58 289 L100 308 L100 357 C94 397 127 418 195 419 L222 569 L390 569 L390 422 C475 338 509 196 419 73Z',deep),path('M399 58 C259 -5 113 60 103 197 L45 275 L86 292 L86 343 C80 383 113 404 181 405 L206 553 L374 553 L374 408 C462 324 495 182 399 58Z',green),path('M264 107 C229 74 188 96 194 121 C166 111 150 141 173 163 C144 177 164 205 185 205 C178 236 212 253 233 234 C241 264 277 253 282 235 C310 248 335 231 330 207 C363 190 349 159 327 159 C341 128 308 101 282 122 C281 105 271 101 264 107Z',light),path('M222 115 Q234 143 209 157 Q187 176 210 202 M264 124 Q246 150 267 176 Q278 206 252 228 M300 140 Q279 157 304 180','none',green,6,{strokeLinecap:'round'}),path('M289 205 L223 328 L273 325 L238 427 L331 296 L281 296 L323 215Z',deep),path('M277 193 L211 316 L261 313 L226 415 L319 284 L269 284 L311 203Z',light),path('M18 18 L162 18 Q183 18 183 41 L183 111 Q183 132 159 132 L86 132 L56 154 L59 132 L23 132 Q0 132 0 111 L0 39 Q0 18 18 18Z',deep),path('M10 8 L153 8 Q174 8 174 31 L174 101 Q174 122 151 122 L77 122 L48 144 L50 122 L14 122 Q-9 122 -9 101 L-9 29 Q-9 8 10 8Z',light,deep,2.8),path('M16 37 L124 37 M16 58 L91 58 M16 78 L91 78','none',deep,6,{strokeLinecap:'round'}),path('M112 57 L145 57 L145 91 L112 91Z',green),path('M380 354 C472 336 499 432 444 477 L435 531 L354 531 L347 477 C291 434 306 369 357 356Z',deep),path('M366 344 C458 326 485 422 430 467 L421 521 L340 521 L333 467 C277 424 292 359 343 346Z',light),path('M360 378 C330 393 328 428 355 448 L360 484 L404 484 L410 446 C437 426 434 393 409 379 C392 369 377 371 360 378Z',green),path('M360 385 Q342 405 360 431 M348 510 L415 510 M345 529 L417 529 M356 548 L405 548','none',deep,8,{strokeLinecap:'round'}),...Array.from({length:7},(_,i)=>{const a=(i*35+145)*Math.PI/180;return path(`M${380+Math.cos(a)*98} ${410+Math.sin(a)*98} l${Math.cos(a)*25} ${Math.sin(a)*25}`,'none',deep,7,{strokeLinecap:'round'})})],'0 0 550 620')
}
export function financeBag(x:number,y:number,w:number,h:number):Element[] {
 const deep='#3d5500',green='#9bd13c',cream='#efffc9'
 const q=[ellipse(304,592,241,39,deep),path('M165 228 C139 331 90 360 91 476 C84 575 182 607 313 595 C465 589 500 527 454 417 C425 359 399 321 382 229Z',deep),path('M152 215 C126 318 77 347 78 463 C71 562 169 594 300 582 C452 576 487 514 441 404 C412 346 386 308 369 216Z',green),path('M128 104 C112 154 148 196 213 208 L330 208 C397 184 421 143 391 106Z',green),ellipse(260,117,129,35,deep),path('M130 105 Q162 127 220 133 Q290 150 389 111 L392 130 Q335 159 257 157 Q177 157 133 130Z',green),ellipse(260,214,96,27,cream,deep,2),ellipse(260,206,95,18,cream),ellipse(296,43,58,23,deep,undefined,0,24),ellipse(285,28,58,23,cream,deep,2,24),ellipse(214,87,50,21,deep,undefined,0,-18),ellipse(204,74,50,21,cream,deep,2,-18),ellipse(118,410,113,113,deep),ellipse(107,397,113,113,cream),ellipse(107,397,96,96,green),path('M104 298 L111 298 L111 393 L191 438 L187 447 L104 403Z',cream),path('M108 401 L184 488 A114 114 0 0 0 216 401Z',deep),path('M113 410 L190 496 L208 478 L151 412Z',green),path('M340 226 L377 204 L377 345 L340 366Z',green),path('M377 204 L399 222 L399 365 L377 345Z',deep),path('M375 184 L412 162 L412 345 L375 366Z',green),path('M412 162 L433 178 L433 364 L412 345Z',deep),path('M410 152 L447 130 L447 345 L410 366Z',cream),path('M447 130 L469 148 L469 364 L447 345Z',deep),path('M442 102 L479 80 L479 345 L442 366Z',green),path('M479 80 L501 98 L501 364 L479 345Z',deep)]
 return [svg(x,y,w,h,q,'0 0 550 637'),T(x+w*.38,y+h*.49,w*.4,h*.43,'$',203,{font:'DM Sans',weight:700,color:cream,align:'center',lineHeight:1})]
}
export function ornateB(x:number,y:number,w:number,h:number):Element {
 return svg(x,y,w,h,[path('M1 0 L121 0 C180 0 192 64 149 88 C204 108 214 161 180 203 C151 239 96 242 61 218 L0 237 L16 220 Q28 211 27 191 L27 25 Q25 7 1 0Z','#ececec'),path('M70 17 L111 17 C147 17 154 66 114 88 L70 87Z','#b3431c'),ellipse(120,167,52,51,'#b3431c'),path('M83 173 C66 140 92 117 116 137 C144 158 118 192 99 175 C109 164 100 148 87 153 C74 160 80 183 92 193 C108 209 147 203 159 175 C170 149 152 123 132 117 C93 98 69 131 68 155 C65 186 76 207 99 215Z','#ececec')],'0 0 200 240')
}
export function fatArrow(x:number,y:number,w:number,h:number,color:string):Element {
 return svg(x,y,w,h,[path('M17 2 Q12 -2 8 2 L2 8 Q-2 12 2 17 L33 47 L17 47 Q9 47 14 55 L37 78 Q43 83 50 83 L74 83 Q83 83 83 74 L83 50 Q83 43 78 37 L55 14 Q47 9 47 17 L47 33Z','none',color,1.6,{strokeLinejoin:'round'})],'0 0 83 83')
}
export function coil(x:number,y:number,w:number,h:number,color:string,variant='oval'):Element {
 const q:SvgShape[]=[]
 if(variant==='circles'){q.push(ellipse(110,120,108,108,'none',color,1.2),ellipse(250,120,108,108,'none',color,1.2))}
 else for(let i=0;i<7;i++)q.push(ellipse(140,50+i*30,135-i*5,48,'none',color,.8))
 return svg(x,y,w,h,q,variant==='circles'?'0 0 360 230':'0 0 300 300')
}
export function pinkStarburst(x:number,y:number,w:number,h:number,variant=0):Element {
 const cx=variant?235:7,cy=variant?193:-35,r=variant?240:265,n=44,pts:string[]=[]
 for(let i=0;i<n*2;i++){const a=i*Math.PI/n,rad=i%2?r*.81:r;pts.push(`${cx+Math.cos(a)*rad},${cy+Math.sin(a)*rad}`)}
 return svg(x,y,w,h,[path(`M${pts.join(' L')} Z`,'url(#pink)')],`0 0 ${w} ${h}`,{}, {gradients:[{id:'pink',type:'radial',cx:variant?'130%':'0%',cy:variant?'50%':'0%',r:'110%',stops:[{offset:'0%',color:'#de8fba',opacity:0},{offset:'66%',color:'#e8a9c7',opacity:.38},{offset:'100%',color:'#de8fba',opacity:.8}]}]})
}
export function pinkFrame():Element[] {
 return [B(449,379,329,327,'linear-gradient(135deg,transparent 0%,#e6bdd333 31%,#e3a4cb 78%,#dc91bc 100%)',{clipPath:'polygon(0 0,67% 0,100% 31%,100% 100%,31% 100%,0 67%)'}),B(550,479,225,223,'transparent',{border:'6.5px solid #df9aca'})]
}
export function rotateElementsAround(elements:Element[],cx:number,cy:number,angle:number):Element[]{
 const rad=angle*Math.PI/180
 return elements.map(e=>{const ex=(e.x+e.w/2)*16,ey=(e.y+e.h/2)*9,dx=ex-cx,dy=ey-cy;return {...e,x:(cx+dx*Math.cos(rad)-dy*Math.sin(rad)-e.w*8)/16,y:(cy+dx*Math.sin(rad)+dy*Math.cos(rad)-e.h*4.5)/9,rotate:(e.rotate??0)+angle}})
}
export function foldedPageCorner():Element {
 return G(1199,684,340,142,'custom',{viewBox:'0 0 340 142',gradients:[{id:'curl',x1:'10%',y1:'0%',x2:'80%',y2:'100%',stops:[{offset:'0%',color:'#d7d7c5'},{offset:'43%',color:'#efefdf'},{offset:'100%',color:'#b5b59c'}]}],paths:[path('M340 0 C295 14 229 25 180 52 C134 81 89 103 0 142 C102 92 138 42 162 15 C222 8 275 9 340 0Z','url(#curl)')]})
}
