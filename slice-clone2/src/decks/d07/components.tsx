import type { ReactNode } from 'react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { Lines } from '../../ui'
import type { Deco } from './data'
import { t } from './theme'

export function KitschSlide({ bg, page, pageRight = false, deco = [], under, children }: { bg: string; page?: string; pageRight?: boolean; deco?: Deco[]; under?: ReactNode; children?: ReactNode }) {
  return (
    <Slide background={bg} className={t.sans} style={{ color: t.ink, ['--ly' as string]: '0.05em' }}>
      {under}
      {deco.map((d, i) => <DecoItem key={i} d={d} />)}
      {page && <Lines x={pageRight ? 1251 : 27} cy={34} align={pageRight ? 'right' : 'left'} w={80} size={21} className={t.latin} color={t.green} lines={[page]} />}
      {children}
    </Slide>
  )
}

export function DecoItem({ d }: { d: Deco }) {
  if (d.k === 'circle') return <Abs x={d.cx - d.r} y={d.cy - d.r} w={d.r * 2} h={d.r * 2} className="rounded-full" style={{ background: d.c }} />
  if (d.k === 'ring') return <Abs x={d.cx - d.r} y={d.cy - d.r} w={d.r * 2} h={d.r * 2} className="rounded-full" style={{ border: `${d.b}px solid ${d.c}` }} />
  return <Abs x={d.x} y={d.y} w={d.w} h={d.h}><ImagePlaceholder label="decorative shape" className="h-full w-full" style={{ borderRadius: d.r }} /></Abs>
}

/** Ellipse in slide coordinates (big background arcs / bubbles). */
export const Ellipse = ({ x, y, w, h, c }: { x: number; y: number; w: number; h: number; c: string }) => (
  <Abs x={x} y={y} w={w} h={h} className="rounded-[50%]" style={{ background: c }} />
)

export const Kicker = ({ x, cy, text, align = "center", color = t.green, size = 23 }: { x: number; cy: number; text: string; align?: 'left' | 'center'; color?: string; size?: number }) => (
  <Lines x={x} cy={cy} align={align} size={size} className="font-montserrat font-bold tracking-[0.15em]" color={color} lines={[text]} />
)

export const Display = ({ x, cy, lines, size, lh, align = 'center', color = t.ink, className }: { x: number; cy: number; lines: readonly string[]; size: number; lh?: number; align?: 'left' | 'center'; color?: string; className?: string }) => (
  <Lines x={x} cy={cy} lh={lh} align={align} size={size} className={cn(t.display, className)} color={color} lines={lines} />
)
