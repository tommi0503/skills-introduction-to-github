export type Region={x:number;y:number;w:number;h:number}
export type Element=Region & {id?:string;kind:'text'|'box'|'image'|'icon'|'path'|'donut';text?:string;size?:number;weight?:number;font?:string;fontStyle?:string;color?:string;fill?:string;radius?:number|string;border?:string;lineHeight?:number;letterSpacing?:number;align?:'left'|'center'|'right';chip?:boolean;inkFit?:boolean;icon?:string;strokeWidth?:number;points?:number[][];d?:string;closed?:boolean;opacity?:number;replacement?:boolean;confidence?:number;textStroke?:string;values?:number[];colors?:string[];hole?:number;rotate?:number}
export type ImageRegion=Region & {radius?:number|string;dropText?:boolean;label?:string;layer?:'background'|'foreground'}
export type SidePatch={background?:string;clearShapes?:boolean;images?:ImageRegion[];removeText?:Region[];removeShapes?:Region[];elements?:Element[];underTextElements?:Element[];defaultFont?:string;defaultWeight?:number;textEdits?:Record<string,Partial<Element>>;textStyles?:Array<Region & Partial<Element>>;notes?:string[]}
export type Side={id:string;size:[number,number];reference:string;elements:Element[];notes:string[]}
export type Panel={id:string;title:string;sideId:string;index:number;crop:Region;size:[number,number];reference:string;elements:Element[]}
export type Brochure={id:string;title:string;sides:Side[];panels:Panel[]}
