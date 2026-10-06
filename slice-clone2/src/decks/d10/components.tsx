import type { ReactNode } from 'react'
import { FileText, Handshake, Lightbulb, MapPin } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide } from '../../ui'
import { Box, Lines } from '../../ui'
import type { R } from './data'
import { t } from './theme'

export const ICONS = { bulb: Lightbulb, doc: FileText, hand: Handshake, pin: MapPin }

/** Grey slide, organic decorations (placeholders) and the big white rounded panel. */
export function BlobSlide({ panel, deco, children }: { panel: R; deco: R[]; children: ReactNode }) {
  const [x, y, w, h] = panel
  return (
    <Slide background={t.bg} className={t.sans} style={{ color: t.ink, ['--ly' as string]: '0.05em' }}>
      {deco.map(([dx, dy, dw, dh], i) => (
        <Abs key={i} x={dx} y={dy} w={dw} h={dh}><ImagePlaceholder label="organic pastel shape" className="h-full w-full" style={{ borderRadius: '45%' }} /></Abs>
      ))}
      <Box x={x} y={y} w={w} h={h} bg={t.panel} style={{ borderRadius: '130px 110px 120px 100px / 110px 120px 100px 120px' }} />
      {children}
    </Slide>
  )
}

/** Lavender number badge (flower → circle). */
export const Badge = ({ cx, cy, n, r = 30 }: { cx: number; cy: number; n: string; r?: number }) => (
  <>
    <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full" style={{ background: t.lavender }} />
    <Lines x={cx} cy={cy} align="center" w={r * 2} size={15} className="font-bold" color="#fff" lines={[n]} />
  </>
)

/** Badge + title + dotted rule. */
export function Header({ badge, title, x = 446, rule = [131, 1142] }: { badge: string; title: string; x?: number; rule?: readonly [number, number] }) {
  return (
    <>
      <Badge cx={x - 54} cy={140} n={badge} />
      <Lines x={x} cy={142} size={50} className={t.head} color={t.ink} lines={[title]} />
      <Dots x={rule[0]} y={199} w={rule[1] - rule[0]} />
    </>
  )
}

export const Dots = ({ x, y, w, color = t.mintDot }: { x: number; y: number; w: number; color?: string }) => (
  <Box x={x} y={y} w={w} h={0} style={{ borderTop: `3px dotted ${color}` }} />
)
export const VDots = ({ x, y, h }: { x: number; y: number; h: number }) => (
  <Box x={x} y={y} w={0} h={h} style={{ borderLeft: `3px dotted ${t.mintDot}` }} />
)

export const Photo = ({ x, y, w, h, r }: { x: number; y: number; w: number; h: number; r?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label="photo" className="h-full w-full" style={{ borderRadius: r }} /></Abs>
)

export const Small = ({ x, cy, lines, align = 'center', w = 500, size = 14, lh = 23 }: { x: number; cy: number; lines: readonly string[]; align?: 'left' | 'center'; w?: number; size?: number; lh?: number }) => (
  <Lines x={x} cy={cy} lh={lh} align={align} w={w} size={size} className="tracking-[-0.04em]" color={t.muted} lines={lines} />
)

/** Left column with badge, 2-line title and description (slides 8 & 9). */
export function SideIntro({ badge, title, desc }: { badge: string; title: readonly string[]; desc: readonly string[] }): ReactNode {
  return (
    <>
      <Badge cx={259} cy={203} n={badge} r={33} />
      <Lines x={259} cy={302} lh={71} align="center" w={380} size={54} className={t.head} color={t.ink} lines={title} />
      <Small x={259} cy={458} lh={27.5} size={15} w={380} lines={desc} />
      <VDots x={428} y={99} h={522} />
    </>
  )
}
