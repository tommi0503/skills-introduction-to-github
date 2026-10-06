import type { CSSProperties, ReactNode } from 'react'
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

export const Pill = ({ cx, cy, w, h, bg = t.green, color = '#fff', size = 14, className, children }: { cx: number; cy: number; w: number; h: number; bg?: string; color?: string; size?: number; className?: string; children: ReactNode }) => (
  <Abs x={cx - w / 2} y={cy - h / 2} w={w} h={h} className={cn('flex items-center justify-center whitespace-nowrap rounded-full leading-none', className)} style={{ background: bg, color, fontSize: size }}>{children}</Abs>
)

export const Dashed = ({ x, y, w, vertical = false, h = 0 }: { x: number; y: number; w?: number; vertical?: boolean; h?: number }) => (
  <Abs x={x} y={y} w={vertical ? 0 : w} h={vertical ? h : 0} style={vertical ? { borderLeft: '1px dashed #cfc6b4' } : { borderTop: '1px dashed #cfc6b4' }} />
)

/** Landscape backdrop + white card + org line + yellow tag + title + cream panel. */
export function Page({ tag, title, tagW = 152, panel = true, children }: { tag: string; title: string; tagW?: number; panel?: boolean; children: ReactNode }) {
  return (
    <Slide background="#f3e9a6" className={t.font} style={{ color: t.ink }}>
      <Ph x={0} y={0} w={1280} h={720} label="rapeseed field landscape illustration" />
      <Abs x={30} y={38} w={1220} h={652} className="rounded-[30px] bg-white" />
      <Txt x={1212} cy={74} size={14} align="right" w={400} style={{ color: '#444' }}>{t.org}</Txt>
      <Pill cx={640} cy={108} w={tagW} h={36} bg={t.yellow} color={t.body} size={19}>{tag}</Pill>
      {title && <Txt x={640} cy={174} size={53} align="center" w={1100} className="font-semibold tracking-[-0.02em]" style={{ color: t.title }}>{title}</Txt>}
      {panel && <Abs x={86} y={235} w={1112} h={410} className="rounded-[30px]" style={{ background: t.panel }} />}
      {children}
    </Slide>
  )
}
