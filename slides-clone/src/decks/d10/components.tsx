import type { CSSProperties, ReactNode } from 'react'
import { ImagePlaceholder, Slide } from '../../ui'
import { theme } from './theme'

export const Frame = ({ k, children }: { k: number; children: ReactNode }) => (
  <Slide background={theme.bg}>
    <div className="relative origin-top-left" style={{ width: 1280 / k, height: 720 / k, transform: `scale(${k})` }}>{children}</div>
  </Slide>
)
export const T = ({ x, y, w, className = '', style, children }: { x: number; y: number; w?: number; className?: string; style?: CSSProperties; children?: ReactNode }) => (
  <div className={`absolute font-archivo text-white ${className}`} style={{ left: x, top: y, width: w, ...style }}>{children}</div>
)
const wide: CSSProperties = { fontStretch: '125%', fontWeight: 800 }
/** Big extended headline; `lime` words (split by |) render in lime. */
export const Headline = ({ x, y, lines, size = 36, lh = 37 }: { x: number; y: number; lines: string[]; size?: number; lh?: number }) => (
  <T x={x} y={y} className="whitespace-nowrap uppercase" style={{ ...wide, fontSize: size, lineHeight: `${lh}px` }}>
    {lines.map((l) => <div key={l}>{l.split(/(\*[^*]+\*)/).map((p, i) => p.startsWith('*') ? <span key={i} style={{ color: theme.lime }}>{p.slice(1, -1)}</span> : p)}</div>)}
  </T>
)
export const Small = ({ x, y, lines, size = 6.5, lh, right }: { x: number; y: number; lines: string[]; size?: number; lh?: number; right?: boolean }) => (
  <T x={x} y={y} className="whitespace-nowrap font-bold uppercase" style={{ fontSize: size, lineHeight: `${lh ?? size * 1.2}px`, textAlign: right ? 'right' : 'left', transform: right ? 'translateX(-100%)' : undefined, fontStretch: '110%' }}>
    {lines.map((l) => <div key={l}>{l}</div>)}
  </T>
)
export const Year = ({ x, y }: { x: number; y: number }) => <T x={x} y={y} className="text-[9px] font-bold leading-[8px]" style={{ color: theme.lime }}>20<br />23</T>
export const Device = ({ x, y, w, h }: { x: number; y: number; w: number; h: number }) => (
  <ImagePlaceholder tone="#2b2b2b" className="absolute" style={{ left: x, top: y, width: w, height: h, borderRadius: 28 }} />
)
