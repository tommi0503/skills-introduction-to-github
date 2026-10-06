import type { CSSProperties, ReactNode } from 'react'
import { Abs } from '../core/Abs'
import { cn } from '../core/cn'

/**
 * Shared text/shape primitives: explicit lines placed by the
 * vertical centre of the first line. A slide can set the CSS var `--ly`
 * (e.g. '0.07em') to compensate fonts whose glyphs sit high in the line box. `x` is the left edge, centre or right edge
 * depending on `align`.
 */
export interface LinesProps {
  x: number
  cy: number
  lines: readonly ReactNode[] | ReactNode
  size: number
  lh?: number
  align?: 'left' | 'center' | 'right'
  w?: number
  className?: string
  color?: string
  style?: CSSProperties
}

export function Lines({ x, cy, lines, size, lh = Math.round(size * 1.4), align = 'left', w = 1400, className, color, style }: LinesProps) {
  const arr = Array.isArray(lines) ? lines : [lines]
  const left = align === 'left' ? x : align === 'center' ? x - w / 2 : x - w
  const justify = align === 'left' ? 'justify-start' : align === 'center' ? 'justify-center' : 'justify-end'
  return (
    <Abs x={left} y={cy - lh / 2} w={w} className={cn('pointer-events-none', className)} style={{ fontSize: size, color, transform: 'translateY(var(--ly, 0em))', ...style }}>
      {arr.map((l, i) => (
        <div key={i} className={cn('flex items-center whitespace-nowrap leading-none', justify)} style={{ height: lh }}>
          {l}
        </div>
      ))}
    </Abs>
  )
}

/** Plain rectangle in slide coordinates. */
export function Box({ x, y, w, h, bg, className, style, children }: { x: number; y: number; w: number; h: number; bg?: string; className?: string; style?: CSSProperties; children?: ReactNode }) {
  return (
    <Abs x={x} y={y} w={w} h={h} className={className} style={{ background: bg, ...style }}>
      {children}
    </Abs>
  )
}

/** Donut / pie chart from conic-gradient segments (percent values, clockwise from 12 o'clock). */
export function Donut({ cx, cy, r, hole = 0, segs, holeBg = '#fff', start = 0 }: { cx: number; cy: number; r: number; hole?: number; segs: readonly { v: number; c: string }[]; holeBg?: string; start?: number }) {
  let acc = 0
  const stops = segs.map((s) => `${s.c} ${acc}% ${(acc += s.v)}%`).join(', ')
  return (
    <>
      <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full" style={{ background: `conic-gradient(from ${start}deg, ${stops})` }} />
      {hole > 0 && <Abs x={cx - hole} y={cy - hole} w={hole * 2} h={hole * 2} className="rounded-full" style={{ background: holeBg }} />}
    </>
  )
}
