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

export function Lines({ lines, x, cy, pitch, size, w, align = 'left', className, style }: { lines: readonly string[]; x: number; cy: number; pitch: number; size: number; w?: number; align?: 'left' | 'center' | 'right'; className?: string; style?: CSSProperties }) {
  return <>{lines.map((l, i) => <T key={i} x={x} cy={cy + i * pitch} size={size} w={w} align={align} className={className} style={style}>{l}</T>)}</>
}

export const HLine = ({ x, y, w, c = t.rule, h = 1 }: { x: number; y: number; w: number; c?: string; h?: number }) => <Abs x={x} y={y} w={w} h={h} style={{ background: c }} />
export const Dotted = ({ x, y, w, c = '#c5c8d2' }: { x: number; y: number; w: number; c?: string }) => <Abs x={x} y={y} w={w} h={0} style={{ borderTop: `1.3px dotted ${c}` }} />

/** Running header: section no., label, year. `dark` = on photo. */
export function RunHead({ no, label, year = '2039', end = 1238, dark }: { no?: string; label: string; year?: string; end?: number; dark?: boolean }) {
  const c = dark ? '#fff' : t.ink
  return (
    <>
      {no && <HLine x={42} y={35} w={40} c={c} />}
      <HLine x={no ? 92 : 42} y={35} w={end - (no ? 92 : 42)} c={dark ? 'rgba(255,255,255,0.6)' : c} />
      {no && <T x={42} cy={49} size={13} style={{ color: c }}>{no}</T>}
      <T x={no ? 92 : 42} cy={49} size={13} style={{ color: c }}>{label}</T>
      {year && end > 1000 && <T x={1138} w={100} cy={49} size={13} align="right" style={{ color: dark && !no ? '#8a93b8' : c }}>{year}</T>}
    </>
  )
}

/** Page title: dark lead + blue tail. */
export const Title = ({ lead, tail, cy = 125, size = 30 }: { lead: string; tail: string; cy?: number; size?: number }) => (
  <T x={41} cy={cy} size={size} className="font-extrabold tracking-[-0.01em]" style={{ color: t.ink }}>{lead}<span style={{ color: t.blue, marginLeft: size * 0.25 }}>{tail}</span></T>
)

export function Page({ children, dark }: { children?: ReactNode; dark?: boolean }) {
  return <Slide background={dark ? t.dark : '#fff'} className={t.font} style={{ color: t.text }}>{children}</Slide>
}

export const PhotoBg = ({ label }: { label: string }) => (
  <Abs x={0} y={0} w={1280} h={720}><ImagePlaceholder label={label} tone={t.dark} className="h-full w-full" /></Abs>
)
