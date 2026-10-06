import type { CSSProperties, ReactNode } from 'react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { t } from './theme'

export function T({ x, cy, size, children, w, className, align = 'left', style }: { x: number; cy: number; size: number; children: ReactNode; w?: number; className?: string; align?: 'left' | 'center' | 'right'; style?: CSSProperties }) {
  return (
    <Abs x={x} y={cy - size * 0.75} w={w} h={size * 1.5} className={cn('flex items-center whitespace-pre leading-none', align === 'center' && 'justify-center', align === 'right' && 'justify-end', className)} style={{ fontSize: size, ...style }}>
      {children}
    </Abs>
  )
}

export function Lines({ lines, x, cy, pitch, size, w, align = 'left', justify, className, style }: { lines: readonly string[]; x: number; cy: number; pitch: number; size: number; w?: number; align?: 'left' | 'center' | 'right'; justify?: boolean; className?: string; style?: CSSProperties }) {
  return (
    <>
      {lines.map((l, i) => justify && i < lines.length - 1
        ? <Abs key={i} x={x} y={cy + i * pitch - size * 0.75} w={w} h={size * 1.5} className={cn('whitespace-nowrap', className)} style={{ fontSize: size, lineHeight: `${size * 1.5}px`, textAlign: 'justify', textAlignLast: 'justify', ...style }}>{l}</Abs>
        : <T key={i} x={x} cy={cy + i * pitch} size={size} w={w} align={align} className={className} style={style}>{l}</T>)}
    </>
  )
}

export function Page({ children, bg = '#fff' }: { children?: ReactNode; bg?: string }) {
  return <Slide background={bg} className={t.kr} style={{ color: t.text, letterSpacing: '-0.035em' }}>{children}</Slide>
}

export const HLine = ({ y, x = 0, w = 1280, c = t.rule, h = 1.5 }: { y: number; x?: number; w?: number; c?: string; h?: number }) => <Abs x={x} y={y} w={w} h={h} style={{ background: c }} />

/** Ring marker with stub lines: 'v' vertical above, 'h' horizontal both sides, 'd' diagonals. */
export function Marker({ cx, cy, kind, color = t.red, r = 10, sw = 4 }: { cx: number; cy: number; kind: 'v' | 'h' | 'd'; color?: string; r?: number; sw?: number }) {
  const line = (x1: number, y1: number, x2: number, y2: number) => <line x1={x1} y1={y1} x2={x2} y2={y2} stroke={color} strokeWidth={1.5} />
  return (
    <svg className="absolute" style={{ left: cx - 40, top: cy - 40 }} width={80} height={80}>
      {kind === 'v' && line(40, 10, 40, 40 - r)}
      {kind === 'h' && <>{line(4, 40, 40 - r, 40)}{line(40 + r, 40, 76, 40)}</>}
      {kind === 'd' && <>{line(50, 8, 40 + r * 0.4, 40 - r)}{line(40 + r * 0.4, 40 + r, 50, 72)}</>}
      <circle cx={40} cy={40} r={r - sw / 2} fill="none" stroke={color} strokeWidth={sw} />
    </svg>
  )
}

/** Section header: marker + label + page number. */
export function Header({ kind, label, page, cy = 72, labelX = 99, color, pageColor = t.ink }: { kind: 'v' | 'h' | 'd'; label: string; page: string; cy?: number; labelX?: number; color?: string; pageColor?: string }) {
  return (
    <>
      <Marker cx={79} cy={cy} kind={kind} color={color} />
      <T x={labelX} cy={cy} size={17} className="font-bold" style={{ color: t.ink }}>{label}</T>
      <T x={1180} w={42} cy={58} size={14} align="right" className={t.en} style={{ color: pageColor }}>{page}</T>
    </>
  )
}

/** Heavy Latin display heading (two lines). */
export function Display({ lines, x = 65, cy, pitch = 62, color = '#fff', size = 66 }: { lines: readonly string[]; x?: number; cy: number; pitch?: number; color?: string; size?: number }) {
  return <Lines lines={lines} x={x} cy={cy} pitch={pitch} size={size} className="font-inter font-extrabold" style={{ color, letterSpacing: '0.005em' }} />
}

/** Circle with a hatched (tick-mark) ring around it. */
export function Hatched({ cx, cy, r, ring, color = '#b8b3a2', fill, children }: { cx: number; cy: number; r: number; ring: number; color?: string; fill?: string; children?: ReactNode }) {
  const mask = `radial-gradient(circle, transparent ${r + 3}px, #000 ${r + 4}px, #000 ${ring}px, transparent ${ring + 1}px)`
  return (
    <>
      <Abs x={cx - ring} y={cy - ring} w={ring * 2} h={ring * 2} className="rounded-full" style={{ background: `repeating-conic-gradient(${color} 0 0.7deg, transparent 0.7deg 1.6deg)`, mask, WebkitMask: mask }} />
      {fill && <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full" style={{ background: fill }} />}
      {children}
    </>
  )
}

export function Photo({ x, y, w, h, className, tone, label = 'photo' }: { x: number; y: number; w: number; h: number; className?: string; tone?: string; label?: string }) {
  return <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label={label} tone={tone} className={cn('h-full w-full', className)} /></Abs>
}
