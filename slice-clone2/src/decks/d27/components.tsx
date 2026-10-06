import type { CSSProperties, ReactNode } from 'react'
import { MoveRight } from 'lucide-react'
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

/** Thin outlined card. */
export const Card = ({ x, y, w, h, r = 14, children, style }: { x: number; y: number; w: number; h: number; r?: number; children?: ReactNode; style?: CSSProperties }) => (
  <Abs x={x} y={y} w={w} h={h} className="overflow-hidden" style={{ border: `1px solid ${t.line}`, borderRadius: r, ...style }}>{children}</Abs>
)

/** Script overlay text (e.g. "Autumn Camping"). */
export const Script = ({ x, cy, size, align = 'center', w = 600, color = t.orange, children, opacity = 1 }: { x: number; cy: number; size: number; align?: Align; w?: number; color?: string; children: ReactNode; opacity?: number }) => (
  <Txt x={x} cy={cy} size={size} lh={size} align={align} w={w} className={t.script} style={{ color, opacity }}>{children}</Txt>
)

export const Rule = ({ x, y, w, color = t.soft }: { x: number; y: number; w: number; color?: string }) => <Abs x={x} y={y} w={w} h={1} style={{ background: color }} />

export const Leaf = ({ x, y, s = 90 }: { x: number; y: number; s?: number }) => <Ph x={x} y={y} w={s} h={s} label="autumn leaf illustration" className="rounded-[40%]" />

/** Round arrow bubble. */
export const ArrowDot = ({ cx, cy, r = 32 }: { cx: number; cy: number; r?: number }) => (
  <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="flex items-center justify-center rounded-full" style={{ background: t.cream, border: `1px solid ${t.line}` }}>
    <MoveRight size={26} color={t.ink} strokeWidth={1.2} />
  </Abs>
)

/** Standard page: green top strip, numbered badge, centred title, footer. */
export function Page({ no, title, sub, band = 24, children }: { no?: string; title?: string; sub?: string; band?: number; children: ReactNode }) {
  return (
    <Slide background={t.cream} className={t.font} style={{ color: t.ink }}>
      <Abs x={0} y={0} w={1280} h={band} style={{ background: t.band }} />
      {no && <Abs x={610} y={49} w={60} h={38} className="flex items-center justify-center rounded-full" style={{ background: t.badge, color: '#fff', fontSize: 19 }}>{no}</Abs>}
      {title && <Txt x={640} cy={129} size={42} align="center" w={1100} className="font-medium tracking-[-0.02em]">{title}</Txt>}
      {sub && <Txt x={640} cy={183} size={22} align="center" w={900}>{sub}</Txt>}
      {children}
      <Footer />
    </Slide>
  )
}
export const Footer = () => (
  <>
    <Txt x={52} cy={688} size={12}>{t.footer[0]}</Txt>
    <Txt x={1230} cy={688} size={12} align="right" w={300}>{t.footer[1]}</Txt>
  </>
)

/** Photo-backed slide with the green header strip and a cream ticket card. */
export function TicketSlide({ band, card, children }: { band?: { h: number; left: string; center: string; right: string; size: number; side: number }; card: { x: number; y: number; w: number; h: number }; children: ReactNode }) {
  return (
    <Slide background={t.cream} className={t.font} style={{ color: t.ink }}>
      <Ph x={0} y={0} w={1280} h={720} label="autumn camping landscape photo" tone="#d4d4d4" />
      {band && (
        <>
          <Abs x={0} y={0} w={1280} h={band.h} style={{ background: t.band }} />
          <Txt x={50} cy={band.h / 2} size={band.side}>{band.left}</Txt>
          <Txt x={640} cy={band.h / 2} size={band.size} align="center" w={800} className="font-medium">{band.center}</Txt>
          <Txt x={1230} cy={band.h / 2} size={band.side} align="right" w={300}>{band.right}</Txt>
        </>
      )}
      <Abs x={card.x} y={card.y} w={card.w} h={card.h} style={{ background: t.cream }} />
      {children}
    </Slide>
  )
}
