import type { CSSProperties, ReactNode } from 'react'
import { Slide } from '../../ui'
import { theme } from './theme'

export const Frame = ({ bg, children }: { bg: string; children: ReactNode }) => (
  <Slide background={bg}>
    <div className="relative origin-top-left" style={{ width: 1280 / theme.k, height: 720 / theme.k, transform: `scale(${theme.k})` }}>{children}</div>
  </Slide>
)
export const T = ({ x, y, w, h, className = '', style, children }: { x: number; y: number; w?: number; h?: number; className?: string; style?: CSSProperties; children?: ReactNode }) => (
  <div className={`absolute font-inter ${className}`} style={{ left: x, top: y, width: w, height: h, ...style }}>{children}</div>
)
export const Tag = ({ x, y, children, color = theme.blue, bg = theme.tag }: { x: number; y: number; children: ReactNode; color?: string; bg?: string }) => (
  <T x={x} y={y} className="whitespace-nowrap rounded-[2px] px-[4px] py-[1.5px] text-[5.5px] font-medium" style={{ color, background: bg }}>{children}</T>
)
export const Chevron = ({ x, y, w, first, children }: { x: number; y: number; w: number; first: boolean; children: ReactNode }) => (
  <T x={x} y={y} w={w} h={36} className="flex items-center justify-center px-5 text-center text-[7px] font-semibold leading-[8px] text-white"
    style={{ background: first ? '#3b82f6' : theme.blue, clipPath: first ? 'polygon(0 0,90% 0,100% 50%,90% 100%,0 100%)' : 'polygon(0 0,90% 0,100% 50%,90% 100%,0 100%,10% 50%)' }}>{children}</T>
)
