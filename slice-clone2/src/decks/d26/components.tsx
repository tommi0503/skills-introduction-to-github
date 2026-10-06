import type { CSSProperties, ReactNode } from 'react'
import { Crown } from 'lucide-react'
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

export const Ph = ({ x, y, w, h, label = 'illustration', className }: { x: number; y: number; w: number; h: number; label?: string; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label={label} className={cn('h-full w-full', className)} /></Abs>
)

/** White box with the green outline (curled-corner frame simplified). */
export const Frame = ({ x, y, w, h, children, border = '#a9cc7c', r = 14, style }: { x: number; y: number; w: number; h: number; children?: ReactNode; border?: string; r?: number; style?: CSSProperties }) => (
  <Abs x={x} y={y} w={w} h={h} className="bg-white" style={{ border: `3px solid ${border}`, borderRadius: r, ...style }}>{children}</Abs>
)

export const Pill = ({ cx, cy, w, h, bg = t.green, color = '#fff', size = 12, children, className }: { cx: number; cy: number; w: number; h: number; bg?: string; color?: string; size?: number; children: ReactNode; className?: string }) => (
  <Abs x={cx - w / 2} y={cy - h / 2} w={w} h={h} className={cn('flex items-center justify-center whitespace-nowrap rounded-full font-bold leading-none', className)} style={{ background: bg, color, fontSize: size }}>{children}</Abs>
)

/** Cream slide with the top green band (org name) and bottom rule. */
export function CreamSlide({ children }: { children: ReactNode }) {
  return (
    <Slide background={t.cream} className={t.font} style={{ color: t.text }}>
      <Abs x={26} y={26} w={1226} h={47} style={{ background: t.band }} />
      <Txt x={1222} cy={49} size={11} align="right" w={400} style={{ color: '#fff' }}>{t.org}</Txt>
      <Abs x={26} y={685} w={1226} h={4} style={{ background: t.line }} />
      {children}
    </Slide>
  )
}
export function FieldSlide({ children }: { children: ReactNode }) {
  return <Slide background={t.field} className={t.font} style={{ color: t.text }}>{children}</Slide>
}

export type Line = readonly [string, 'b' | 'g' | 'w']
const lineColor = { b: t.brown, g: t.greenText, w: '#fff' }
/** "PART N" kicker + stacked heavy title lines. */
export function SideTitle({ part, lines, cy = 180, size = 52, lh = 57, light = false }: { part: string; lines: readonly Line[]; cy?: number; size?: number; lh?: number; light?: boolean }) {
  return (
    <>
      <Txt x={90} cy={cy - 49} size={16} className="font-montserrat font-medium" style={{ color: light ? '#fff' : t.greenText }}>{part}</Txt>
      {lines.map(([s, c], i) => <Txt key={s} x={88} cy={cy + i * lh} size={size} className={t.head} style={{ color: lineColor[c] }}>{s}</Txt>)}
    </>
  )
}

/** Crown-marked chart caption. */
export const Caption = ({ x, cy, children }: { x: number; cy: number; children: ReactNode }) => (
  <Abs x={x} y={cy - 14} h={28} className="flex items-center gap-[8px] whitespace-nowrap font-bold leading-none" style={{ fontSize: 20, color: t.text }}>
    <Crown size={16} fill="#e8d23c" color="#e8d23c" />{children}
  </Abs>
)
