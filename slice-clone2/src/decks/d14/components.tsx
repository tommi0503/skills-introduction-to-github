import { Fragment, type CSSProperties, type ReactNode } from 'react'
import { Flower } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { t } from './theme'

/** Cream slide with optional section header (number + label + deck name + rule). */
export function Page({ no, label, children }: { no?: string; label?: string; children?: ReactNode }) {
  return (
    <Slide background={t.bg} className={t.sans} style={{ color: t.ink }}>
      {no && (
        <>
          <Abs x={48} y={27}><Flower size={20} fill={t.ink} color={t.ink} strokeWidth={1.5} /></Abs>
          <T x={90} y={30} size={14.5}>{no}</T>
          <T x={118} y={29} size={15}>{label}</T>
          <T x={928} y={29} w={300} size={15} align="right">{t.deckName}</T>
          <Abs x={30} y={65} w={1220} h={1.5} style={{ background: '#222' }} />
        </>
      )}
      {children}
    </Slide>
  )
}

/** Gradient blob background stand-in. */
export const Blob = ({ x, y, w, h, r = 200, tone }: { x: number; y: number; w: number; h: number; r?: number | string; tone?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label="green gradient blob" tone={tone} className="h-full w-full" style={{ borderRadius: r }} /></Abs>
)

export function T({ x, y, w, size, children, className, style, align = 'left' }: { x: number; y: number; w?: number; size: number; children: ReactNode; className?: string; style?: CSSProperties; align?: 'left' | 'center' | 'right' }) {
  return <Abs x={x} y={y} w={w} className={cn('whitespace-nowrap leading-none', className)} style={{ fontSize: size, textAlign: align, ...style }}>{children}</Abs>
}

export function Lines({ x, y, w, size, lh, lines, className, style, align = 'left' }: { x: number; y: number; w?: number; size: number; lh: number; lines: readonly string[]; className?: string; style?: CSSProperties; align?: 'left' | 'center' | 'right' }) {
  return (
    <Abs x={x} y={y} w={w} className={cn('whitespace-nowrap', className)} style={{ fontSize: size, lineHeight: `${lh}px`, textAlign: align, ...style }}>
      {lines.map((l, i) => <div key={i}>{l}</div>)}
    </Abs>
  )
}

/** Big serif heading; multi-line in one element (lines are tight). */
export const Title = ({ x, y, size = 56, lines, lh, align = 'left', w }: { x: number; y: number; size?: number; lines: readonly string[]; lh?: number; align?: 'left' | 'center'; w?: number }) => (
  <Abs x={x} y={y} w={w} className={cn(t.serif, 'whitespace-nowrap font-medium')} style={{ fontSize: size, lineHeight: `${lh ?? size * 1.05}px`, textAlign: align, letterSpacing: '-0.01em' }}>
    {lines.map((l, i) => <Fragment key={i}>{i > 0 && <br />}{l}</Fragment>)}
  </Abs>
)

export const Card = ({ x, y, w, h, r = 18, children, style }: { x: number; y: number; w: number; h: number; r?: number; children?: ReactNode; style?: CSSProperties }) => (
  <Abs x={x} y={y} w={w} h={h} style={{ background: t.card, borderRadius: r, ...style }}>{children}</Abs>
)

export const Pill = ({ cx, cy, w, h, text, size = 20, bg = '#fff', className }: { cx: number; cy: number; w: number; h: number; text: string; size?: number; bg?: string; className?: string }) => (
  <Abs x={cx - w / 2} y={cy - h / 2} w={w} h={h} className={cn('flex items-center justify-center whitespace-nowrap rounded-full', className)} style={{ background: bg, fontSize: size }}>{text}</Abs>
)
