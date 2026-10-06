import type { CSSProperties, ReactNode } from 'react'
import { Camera } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { t } from './theme'

export function T({ x, cy, size, children, w, className, align = 'left', style }: { x: number; cy: number; size: number; children: ReactNode; w?: number; className?: string; align?: 'left' | 'center' | 'right'; style?: CSSProperties }) {
  return (
    <Abs x={x} y={cy - size * 0.75} w={w} h={size * 1.5} className={cn('flex items-center whitespace-pre leading-none', align === 'center' && 'justify-center', align === 'right' && 'justify-end', className)} style={{ fontSize: size, ...style }}>
      {children}
    </Abs>
  )
}

export function Lines({ lines, x, cy, pitch, size, w, align, className, style }: { lines: readonly string[]; x: number; cy: number; pitch: number; size: number; w?: number; align?: 'left' | 'center' | 'right'; className?: string; style?: CSSProperties }) {
  return <>{lines.map((l, i) => <T key={i} x={x} cy={cy + i * pitch} size={size} w={w} align={align} className={className} style={style}>{l}</T>)}</>
}

/** Scalloped-badge stand-in: grey disc with the page number. */
export function Badge({ n, dark }: { n: number | string; dark?: boolean }) {
  return <Abs x={1189} y={39} w={44} h={44} className="flex items-center justify-center rounded-full font-bold tracking-[0.01em] text-white" style={{ background: dark ? '#444' : '#b0b0b0', fontSize: 19 }}>{n}</Abs>
}

/** White page with grey left rail, red marker and numbered title. */
export function Page({ title, page, children, rail = t.side, titleColor = t.ink, dark }: { title: string; page: number; children?: ReactNode; rail?: string; titleColor?: string; dark?: boolean }) {
  return (
    <Slide background="#fff" className={t.font} style={{ color: t.ink, letterSpacing: '0.05em' }}>
      <Abs x={0} y={0} w={t.rail} h={720} style={{ background: rail }} />
      {children}
      <Abs x={75} y={27} w={17} h={50} style={{ background: t.red }} />
      <T x={124} cy={51} size={42} className="font-bold tracking-[0.01em]" style={{ color: titleColor }}>{title}</T>
      <Badge n={page} dark={dark} />
    </Slide>
  )
}

export const Sub = ({ children, cy = 136, x = 207, color = t.sub }: { children: ReactNode; cy?: number; x?: number; color?: string }) => (
  <T x={x} cy={cy} size={25} className="font-bold tracking-[0.01em]" style={{ color }}>{children}</T>
)

/** Grey photo slot with a camera glyph (as in the reference template). */
export function PhotoSlot({ x, y, w, h }: { x: number; y: number; w: number; h: number }) {
  return (
    <Abs x={x} y={y} w={w} h={h} className="flex items-center justify-center">
      <ImagePlaceholder label="photo" tone={t.photo} className="absolute inset-0" />
      <Camera size={44} fill="#555" color={t.photo} strokeWidth={1.6} className="relative" />
    </Abs>
  )
}

export const Dot = ({ cx, cy, r, bg }: { cx: number; cy: number; r: number; bg: string }) => <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full" style={{ background: bg }} />
