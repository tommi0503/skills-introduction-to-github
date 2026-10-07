export type Region={x:number;y:number;w:number;h:number}
export type Element=Region & {id?:string;kind:'text'|'box'|'image'|'icon'|'path'|'donut';text?:string;size?:number;weight?:number;font?:string;fontStyle?:string;color?:string;fill?:string;radius?:number|string;border?:string;lineHeight?:number;letterSpacing?:number;align?:'left'|'center'|'right'|'justify';chip?:boolean;icon?:string;strokeWidth?:number;points?:number[][];d?:string;closed?:boolean;opacity?:number;replacement?:boolean;textStroke?:string;values?:number[];colors?:string[];hole?:number;rotate?:number;label?:string;clipPath?:string;shadow?:string;clipReason?:string;foldClip?:boolean}
export type SideDraft={id:string;elements:Element[];notes?:string[]}
export type BrochureDraft={id:string;sides:SideDraft[]}
export type Side={id:string;size:[number,number];reference:string;elements:Element[];notes:string[]}
export type Panel={id:string;title:string;sideId:string;index:number;crop:Region;size:[number,number];reference:string;elements:Element[];notes:string[]}
export type Brochure={id:string;title:string;designId:string;sides:Side[];panels:Panel[]}
