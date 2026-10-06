import type { CSSProperties, ReactNode } from 'react'
import { Abs, Slide, cn } from '../../ui'
import { t } from './theme'

type Align = 'left' | 'center' | 'right'

/** Single text line: `x` is left edge / centre / right edge per `align`, `cy` the vertical centre. */
export function Txt({ x, cy, size, align = 'left', w = 1100, className, style, children, d }: {
  x: number; cy: number; size: number; align?: Align; w?: number; className?: string; style?: CSSProperties; children: ReactNode
  /** Display face: thinned + tightened; the value is the colour behind the text. */
  d?: string | true
}) {
  if (d) {
    const fs = size * t.dScale
    style = { letterSpacing: t.dTrack, WebkitTextStroke: `${fs * t.dThin}px ${d === true ? t.bg : d}`, ...style, fontSize: fs }
    className = cn(t.head, className)
  }
  const left = align === 'left' ? x : align === 'center' ? x - w / 2 : x - w
  const justify = align === 'left' ? 'justify-start' : align === 'center' ? 'justify-center' : 'justify-end'
  return (
    <Abs x={left} y={cy - size * 0.7} w={w} h={size * 1.4} className={cn('flex items-center whitespace-nowrap leading-none', justify, className)} style={{ fontSize: size, ...style }}>
      <span>{children}</span>
    </Abs>
  )
}

/** Inline markup: [[bold+highlight]], ==highlight==, **bold**. */
export function Rich({ text }: { text: string }) {
  return (
    <>
      {text.split(/(\[\[.*?\]\]|==.*?==|\*\*.*?\*\*)/).map((s, i) => {
        if (s.startsWith('[[')) return <Hl key={i} className="font-bold">{s.slice(2, -2)}</Hl>
        if (s.startsWith('==')) return <Hl key={i}>{s.slice(2, -2)}</Hl>
        if (s.startsWith('**')) return <b key={i}>{s.slice(2, -2)}</b>
        return s
      })}
    </>
  )
}

export const Hl = ({ children, className }: { children: ReactNode; className?: string }) => (
  <span className={className} style={{ background: t.hl }}>{children}</span>
)

/** Stack of lines with centres `cy0`, `cy0 + gap`, ... */
export function Lines({ x, cy0, gap, size, lines, align = 'left', w, className, style, d }: {
  x: number; cy0: number; gap: number; size: number; lines: readonly string[]; align?: Align; w?: number; className?: string; style?: CSSProperties; d?: string | true
}) {
  return (
    <>
      {lines.map((l, i) => (
        <Txt key={i} x={x} cy={cy0 + i * gap} size={size} align={align} w={w} className={className} style={style} d={d}><Rich text={l} /></Txt>
      ))}
    </>
  )
}

export const Circle = ({ cx, cy, r, color, style }: { cx: number; cy: number; r: number; color: string; style?: CSSProperties }) => (
  <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full" style={{ background: color, ...style }} />
)

/** Display heading (one or more lines). */
export function Title({ x = 173, cy = 100, lines, size = 46, align = 'left', gap = 58, d = true }: { x?: number; cy?: number; lines: readonly string[]; size?: number; align?: Align; gap?: number; d?: string | true }) {
  return <Lines x={x} cy0={cy} gap={gap} size={size} lines={lines} align={align} d={d} />
}

export function Base({ children }: { children: ReactNode }) {
  return <Slide background={t.bg} style={{ color: t.ink }}>{children}</Slide>
}

/** Content slide: left rail with section numbers and vertical section label. */
export function RailSlide({ active, label, children }: { active: number; label: string; children: ReactNode }) {
  const s = t.side
  return (
    <Base>
      <Abs x={s.lineX - 1} y={0} w={2} h={720} style={{ background: t.ink }} />
      {[0, 1, 2, 3, 4].map((i) => (
        <div key={i}>
          {i === active && <Circle cx={s.numX} cy={s.numY0 + i * s.numGap} r={20} color={t.green} />}
          <Txt x={s.numX} cy={s.numY0 + i * s.numGap} size={20} align="center" w={40} d={i === active ? t.green : true}>{String(i + 1).padStart(2, '0')}</Txt>
        </div>
      ))}
      <Abs x={s.numX - 10} y={380} w={20} h={300} className={cn(t.body, 'flex items-center justify-start whitespace-nowrap leading-none')} style={{ fontSize: 14, writingMode: 'sideways-lr' }}>
        {label}
      </Abs>
      {children}
    </Base>
  )
}
