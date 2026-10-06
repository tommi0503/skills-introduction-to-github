import type { CSSProperties, ReactNode } from 'react'
import { Slide } from '../../ui'
import { theme } from './theme'

/** Slide whose children are laid out in reference-image pixels (scaled by theme.k). */
export const Frame = ({ children }: { children: ReactNode }) => (
  <Slide background={theme.bg}>
    <div className="relative origin-top-left" style={{ width: 1280 / theme.k, height: 720 / theme.k, transform: `scale(${theme.k})` }}>{children}</div>
  </Slide>
)
export const T = ({ x, y, w, className = '', style, children }: { x: number; y: number; w?: number; className?: string; style?: CSSProperties; children: ReactNode }) => (
  <div className={`absolute whitespace-nowrap ${className}`} style={{ left: x, top: y, width: w, ...style }}>{children}</div>
)
/** Horizontally condensed serif text (scaleX), anchored left or centred in a box. */
export const Cond = ({ x, y, w, s, size, lh, align = 'left', className = '', children }: { x: number; y: number; w: number; s: number; size: number; lh?: number; align?: 'left' | 'center' | 'right'; className?: string; children: ReactNode }) => (
  <div className="absolute" style={{ left: x, top: y, width: w }}>
    <div className={`${theme.serif} whitespace-nowrap uppercase-none ${className}`} style={{ fontSize: size, lineHeight: `${lh ?? size}px`, textAlign: align, transform: `scaleX(${s})`, transformOrigin: align === 'left' ? 'left top' : align === 'center' ? 'center top' : 'right top', width: w }}>{children}</div>
  </div>
)
export const Header = ({ left, num, right }: { left: string; num: string; right?: string }) => (
  <>
    <T x={5} y={7} className="font-archivo text-[4.5px] font-extrabold tracking-wide">{left}</T>
    <T x={228} y={5} className={`${theme.serif} text-[8px]`}>{num}</T>
    {right && <T x={462} y={7} className="font-archivo text-[4.5px] font-extrabold tracking-wide" style={{ transform: 'translateX(-100%)' }}>{right}</T>}
  </>
)
