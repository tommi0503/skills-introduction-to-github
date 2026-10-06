import type { CSSProperties, ReactNode } from 'react'
import { Abs, ImagePlaceholder, cn } from '../../ui'
import { t } from './theme'

type Align = 'left' | 'center' | 'right'
export interface TxtProps { x: number; cy: number; size: number; align?: Align; w?: number; className?: string; style?: CSSProperties; children: ReactNode }

/** `==accent==` and `**bold**` inline markup. */
export function Rich({ text }: { text: string }) {
  return (
    <>
      {text.split(/(==.*?==|\*\*.*?\*\*)/).map((s, i) =>
        s.startsWith('==') ? <span key={i} style={{ color: t.green }}>{s.slice(2, -2)}</span>
          : s.startsWith('**') ? <b key={i} className="font-bold">{s.slice(2, -2)}</b> : s)}
    </>
  )
}

/** Single text line: `x` is left edge / centre / right edge per `align`, `cy` the vertical centre. */
export function Txt({ x, cy, size, align = 'left', w = 1100, className, style, children }: TxtProps) {
  const left = align === 'left' ? x : align === 'center' ? x - w / 2 : x - w
  const justify = align === 'left' ? 'justify-start' : align === 'center' ? 'justify-center' : 'justify-end'
  return (
    <Abs x={left} y={cy - size * 0.7} w={w} h={size * 1.4} className={cn('flex items-center whitespace-nowrap leading-none', justify, t.body)} style={{ fontSize: size, ...style }}>
      <span className={className}>{typeof children === 'string' ? <Rich text={children} /> : children}</span>
    </Abs>
  )
}

export function Lines({ lines, cy0, gap, ...rest }: Omit<TxtProps, 'cy' | 'children'> & { lines: readonly string[]; cy0: number; gap: number }) {
  return <>{lines.map((l, i) => <Txt key={i} {...rest} cy={cy0 + i * gap}>{l}</Txt>)}</>
}

export const Ph = ({ x, y, w, h, label, tone, className }: { x: number; y: number; w: number; h: number; label: string; tone?: string; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label={label} tone={tone} className={cn('h-full w-full', className)} /></Abs>
)
export const Box = ({ x, y, w, h, fill, r = 0, style }: { x: number; y: number; w: number; h: number; fill: string; r?: number; style?: CSSProperties }) => (
  <Abs x={x} y={y} w={w} h={h} style={{ background: fill, borderRadius: r, ...style }} />
)

/** Two-tone display title (light first word, green second) with optional KR subtitle. */
export function Display({ x, cy, size, words, gap, sub, subCy, inline }: { x: number; cy: number; size: number; words: readonly [string, string]; gap?: number; sub?: string; subCy?: number; inline?: boolean }) {
  return (
    <>
      {inline
        ? <Txt x={x} cy={cy} size={size} className={t.display}><span style={{ color: t.light }}>{words[0]}</span> <span style={{ color: t.green }}>{words[1]}</span></Txt>
        : words.map((w, i) => <Txt key={w} x={x} cy={cy + i * (gap ?? size)} size={size} className={t.display} style={{ color: i ? t.green : t.light }}>{w}</Txt>)}
      {sub && <Txt x={x + 4} cy={subCy!} size={28} className="font-semibold">{sub}</Txt>}
    </>
  )
}

/** Green rounded pill with white text. */
export function Pill({ x, y, w, h, size, children, fill = t.green, color = '#fff' }: { x: number; y: number; w: number; h: number; size: number; children: ReactNode; fill?: string; color?: string }) {
  return <Abs x={x} y={y} w={w} h={h} className={cn(t.body, 'flex items-center justify-center whitespace-nowrap rounded-full font-medium leading-none')} style={{ background: fill, color, fontSize: size }}>{children}</Abs>
}

/** Text block with a green vertical bar on its left. */
export function Barred({ x, cy0, lines, size = 20, gap = 31, bar = 6, head, color = t.ink }: { x: number; cy0: number; lines: readonly string[]; size?: number; gap?: number; bar?: number; head?: string; color?: string }) {
  const n = lines.length + (head ? 1 : 0)
  const top = cy0 - gap / 2
  return (
    <>
      <Box x={x} y={top} w={bar} h={n * gap + (head ? 10 : 0)} fill={t.green} />
      {head && <Txt x={x + 22} cy={cy0} size={size} className="font-semibold" style={{ color: t.green }}>{head}</Txt>}
      <Lines x={x + 22} cy0={cy0 + (head ? gap + 12 : 0)} gap={gap} size={size} lines={lines} style={{ color }} />
    </>
  )
}
