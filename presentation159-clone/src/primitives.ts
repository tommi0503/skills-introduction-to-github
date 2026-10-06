import type {Element,Slide,Deck,GraphicOptions} from './model'
// Coordinates and typography are specified in the supplied 1600 × 900 images.
// Only this adapter converts them into the uniform 1280 × 720 render canvas.
export const T=(x:number,y:number,w:number,h:number,text:string,size:number,extra:Partial<Element>={}):Element=>({kind:'text',x:x/16,y:y/9,w:w/16,h:h/9,text,size:size*.8,font:'Pretendard',lineHeight:1.2,...extra,letterSpacing:(extra.letterSpacing??0)*.8})
export const B=(x:number,y:number,w:number,h:number,fill:string,extra:Partial<Element>={}):Element=>({kind:'box',x:x/16,y:y/9,w:w/16,h:h/9,fill,...extra})
export const I=(x:number,y:number,w:number,h:number,label='Image placeholder',extra:Partial<Element>={}):Element=>({kind:'image',x:x/16,y:y/9,w:w/16,h:h/9,text:label,...extra})
export const G=(x:number,y:number,w:number,h:number,name:string,options:GraphicOptions={},extra:Partial<Element>={}):Element=>({kind:'graphic',x:x/16,y:y/9,w:w/16,h:h/9,graphic:name,graphicOptions:options,...extra})
export const L=(x:number,y:number,w:number,color='#bbb',width=1,extra:Partial<Element>={}):Element=>({kind:'line',x:x/16,y:y/9,w:extra.vertical?0:w/16,h:extra.vertical?w/9:0,color,strokeWidth:width*.8,...extra})
export const IC=(x:number,y:number,w:number,h:number,name:string,color='#222',extra:Partial<Element>={}):Element=>({kind:'icon',x:x/16,y:y/9,w:w/16,h:h/9,icon:name,color,...extra})
export const C=(x:number,y:number,w:number,h:number,text:string,size:number,fill:string,extra:Partial<Element>={}):Element=>({kind:'chip',x:x/16,y:y/9,w:w/16,h:h/9,text,size:size*.8,fill,font:'Pretendard',weight:500,radius:8,align:'center',lineHeight:1,...extra,letterSpacing:(extra.letterSpacing??0)*.8})
export const P=(points:number[][],color:string,width=1,fill?:string,extra:Partial<Element>={}):Element=>({kind:'path',x:0,y:0,w:100,h:100,points:points.map(([x,y])=>({x:x/16,y:y/9})),color,strokeWidth:width*.8,fill,closed:!!fill,...extra})
export const S=(id:string,title:string,background:string,elements:Element[]):Slide=>({id,title,background,elements})
export const D=(id:string,title:string,slides:Slide[]):Deck=>({id,title,slides,columns:2,referenceSize:{width:1600,height:900},referenceRegions:slides.map(()=>({x:0,y:0,w:100,h:100})),references:slides.map(s=>`/reference/${id}/${s.id}.jpg`)})
// Paragraph alignment is a data decision. Keep headings, chips and lists intact.
export const justifyParagraphs=(deck:Deck,slideIds:string[],matches:(element:Element)=>boolean):Deck=>({
  ...deck,slides:deck.slides.map(slide=>slideIds.includes(slide.id)?{
    ...slide,elements:slide.elements.map(element=>element.kind==='text'&&matches(element)?{
      ...element,align:'justify',nowrap:false,text:element.text?.replace(/\s+/g,' ').trim(),
    }:element),
  }:slide),
})
