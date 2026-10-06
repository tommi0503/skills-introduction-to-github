import type { CSSProperties, ReactNode } from 'react'
import { X } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { t } from './theme'

type Align = 'left' | 'center' | 'right'
/** Text block: `x` = left / centre / right edge per `align`, `cy` = centre of the first line, `lh` = line pitch. */
export function Txt({ x, cy, size, lh, align = 'left', w = 1000, className, style, children }: {
  x: number; cy: number; size: number; lh?: number; align?: Align; w?: number; className?: string; style?: CSSProperties; children: ReactNode
}) {
  const l = lh ?? size * 1.3
  const left = align === 'left' ? x : align === 'center' ? x - w / 2 : x - w
  return (
    <Abs x={left} y={cy - l / 2} w={w} className={cn('whitespace-pre-line', className)} style={{ fontSize: size, lineHeight: `${l}px`, textAlign: align, ...style }}>
      {children}
    </Abs>
  )
}

export const Ph = ({ x, y, w, h, label = 'photo', tone, className }: { x: number; y: number; w: number; h: number; label?: string; tone?: string; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label={label} tone={tone} className={cn('h-full w-full', className)} /></Abs>
)

export function GSlide({ bg = t.bg, children }: { bg?: string; children: ReactNode }) {
  return <Slide background={bg} className={t.font} style={{ color: t.ink }}>{children}</Slide>
}

/** Row of four small dots. */
export const Dots = ({ x, y, color = t.green, gap = 33 }: { x: number; y: number; color?: string; gap?: number }) => (
  <>{[0, 1, 2, 3].map((i) => <Abs key={i} x={x + i * gap - 4} y={y - 4} w={8} h={8} className="rounded-full" style={{ background: color }} />)}</>
)

export const Square = ({ x, y, s = 44, color = t.green }: { x: number; y: number; s?: number; color?: string }) => (
  <>
    <Abs x={x + 6} y={y + 6} w={s} h={s} style={{ background: 'rgba(0,0,0,0.06)' }} />
    <Abs x={x} y={y} w={s} h={s} style={{ border: `4px solid ${color}` }} />
  </>
)
export const Ring = ({ cx, cy, r = 24, color = t.green }: { cx: number; cy: number; r?: number; color?: string }) => (
  <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full" style={{ border: `4px solid ${color}` }} />
)
export const Cross = ({ cx, cy, s = 30, color = t.green }: { cx: number; cy: number; s?: number; color?: string }) => (
  <Abs x={cx - s / 2} y={cy - s / 2}><X size={s} color={color} strokeWidth={3.2} /></Abs>
)
export const Hatch = ({ x, y, w, h, tone }: { x: number; y: number; w: number; h: number; tone?: string }) => (
  <Ph x={x} y={y} w={w} h={h} label="diagonal hatch pattern" tone={tone} />
)

/** Section header: Korean title + English sub, full-width rule and optional description. */
export function Header({ title, en, x = 135, y = t.headerY, rule = true, desc }: { title: string; en: string; x?: number; y?: number; rule?: boolean; desc?: string }) {
  return (
    <>
      <Abs x={x} y={y - 22} h={44} className="flex items-baseline gap-3 whitespace-nowrap leading-none">
        <span className="font-bold" style={{ fontSize: 32, color: t.greenText }}>{title}</span>
        <span className="font-light" style={{ fontSize: 19, color: t.light }}>{en}</span>
      </Abs>
      {rule && <Abs x={0} y={y + 28} w={1280} h={3} style={{ background: t.green }} />}
      {desc && <Txt x={x} cy={y + 55} size={19} className="font-light" style={{ color: t.grey }}>{desc}</Txt>}
    </>
  )
}

export const IconDisc = ({ cx, cy, r, children }: { cx: number; cy: number; r: number; children: ReactNode }) => (
  <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="flex items-center justify-center rounded-full" style={{ background: t.green }}>{children}</Abs>
)

export type Cell = { text: string; colSpan?: number; rowSpan?: number; head?: boolean; strong?: boolean; color?: string }
/** Simple bordered grid table with absolute column widths and row heights. */
export function Grid({ x, y, cols, rowH, rows, size = 16, headBg = t.green, border = '#d6d6d6', style }: {
  x: number; y: number; cols: number[]; rowH: number | number[]; rows: Cell[][]; size?: number; headBg?: string; border?: string; style?: CSSProperties
}) {
  return (
    <Abs x={x} y={y} style={style}>
      <table className="border-collapse" style={{ tableLayout: 'fixed', width: cols.reduce((a, b) => a + b, 0), fontSize: size }}>
        <colgroup>{cols.map((c, i) => <col key={i} style={{ width: c }} />)}</colgroup>
        <tbody>
          {rows.map((r, ri) => (
            <tr key={ri} style={{ height: Array.isArray(rowH) ? rowH[ri] : rowH }}>
              {r.map((c, ci) => (
                <td key={ci} colSpan={c.colSpan} rowSpan={c.rowSpan} className={cn('p-0 text-center leading-none whitespace-nowrap', c.strong && 'font-semibold')}
                  style={{ border: `1px solid ${border}`, background: c.head ? headBg : '#fff', color: c.head ? '#fff' : c.color ?? t.ink }}>
                  {c.text}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </Abs>
  )
}
