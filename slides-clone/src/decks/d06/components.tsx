import { Zap } from 'lucide-react'
import type { CSSProperties, ReactNode } from 'react'
import { Slide } from '../../ui'
import { site } from './data'
import { theme } from './theme'

export const Frame = ({ k, bg, children }: { k: number; bg: string; children: ReactNode }) => (
  <Slide background={bg}>
    <div className="relative origin-top-left" style={{ width: 1280 / k, height: 720 / k, transform: `scale(${k})` }}>{children}</div>
  </Slide>
)
export const T = ({ x, y, w, className = '', style, children }: { x: number; y: number; w?: number; className?: string; style?: CSSProperties; children: ReactNode }) => (
  <div className={`absolute font-inter ${className}`} style={{ left: x, top: y, width: w, ...style }}>{children}</div>
)
export const Logo = ({ x, y, color }: { x: number; y: number; color: string }) => (
  <T x={x} y={y} className="flex items-center gap-[2px] text-[6.5px] font-semibold" style={{ color }}>
    <Zap size={7} fill={theme.lime} color={theme.lime} />stroom
  </T>
)
export const Nav = ({ y, color, xs, page }: { y: number; color: string; xs: [number, number]; page?: { x: number; t: string } }) => (
  <>
    <T x={xs[0]} y={y} className="text-[4px]" style={{ color }}>{site}</T>
    {page && <T x={page.x} y={y} className="text-[4px]" style={{ color }}>{page.t}</T>}
  </>
)
