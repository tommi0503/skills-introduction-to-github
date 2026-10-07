import type {ComponentType} from 'react'

export interface GraphicProps {colors?:string[];variant?:string}
export type GraphicScenes = Record<string,ComponentType<GraphicProps>>
