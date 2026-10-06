import type { CSSProperties, ReactNode } from 'react'
import { Check, Quote as QuoteIcon } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { t, type Pt } from './theme'

const clip = (pts: Pt[]) => `polygon(${pts.map(([x, y]) => `${x}px ${y}px`).join(',')})`

/** Full-slide polygon fill. */
export const Poly = ({ pts, c = t.blue }: { pts: Pt[]; c?: string }) => <Abs x={0} y={0} w={1280} h={720} style={{ background: c, clipPath: clip(pts) }} />

/** Photo placeholder clipped to a polygon. */
export const PhotoPoly = ({ pts, tone, label = 'photo' }: { pts: Pt[]; tone?: string; label?: string }) => (
  <Abs x={0} y={0} w={1280} h={720} style={{ clipPath: clip(pts) }}><ImagePlaceholder label={label} tone={tone ?? t.photo} className="h-full w-full" /></Abs>
)

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
  return <Slide background={bg} className={t.font} style={{ color: t.ink }}>{children}</Slide>
}

/** Small grey English kicker + big bold Korean title. */
export function Title({ kicker, title, x = 122, cy = 157 }: { kicker: string; title: string; x?: number; cy?: number }) {
  return (
    <>
      <T x={x + 3} cy={cy - 59} size={14.5} style={{ color: '#b0b0b0' }}>{kicker}</T>
      <T x={x} cy={cy} size={61} className="font-extrabold tracking-[-0.02em]">{title}</T>
    </>
  )
}

export const PageNo = ({ n, color = t.ink }: { n: string; color?: string }) => <T x={1180} w={66} cy={685} size={15} align="right" style={{ color }}>{n}</T>

/** Small square number tag. */
export function NumBox({ x, y, n, w = 42, h = 42, size = 19, blue }: { x: number; y: number; n: string; w?: number; h?: number; size?: number; blue?: boolean }) {
  return (
    <Abs x={x} y={y} w={w} h={h} className="flex items-center justify-center bg-white font-bold" style={{ border: `1.5px solid ${blue ? t.blue : '#c9cfd6'}`, color: blue ? t.blue : t.ink, fontSize: size }}>{n}</Abs>
  )
}

/** Bordered box with grey header band. */
export function HeadCard({ x, y, w, h, head, children }: { x: number; y: number; w: number; h: number; head: number; children?: ReactNode }) {
  return (
    <Abs x={x} y={y} w={w} h={h} className="bg-white" style={{ border: `1.5px solid ${t.line}` }}>
      <div style={{ height: head, background: t.pale }} />
      {children}
    </Abs>
  )
}

export const Tick = ({ x, cy, size = 28, color = t.ink }: { x: number; cy: number; size?: number; color?: string }) => (
  <Abs x={x} y={cy - size / 2} w={size} h={size} className="flex items-center justify-center" style={{ border: '1.5px solid #d0d0d0' }}>
    <Check size={size * 1.05} color={color} strokeWidth={2} style={{ marginTop: -size * 0.25, marginLeft: size * 0.1 }} />
  </Abs>
)

/** Bullet list: each item is an array of lines. */
export function Bullets({ items, x, cy, pitch, gap, size, w, justify }: { items: readonly (readonly string[])[]; x: number; cy: number; pitch: number; gap: number; size: number; w?: number; justify?: boolean }) {
  let y = cy
  return (
    <>
      {items.map((lines, i) => {
        const y0 = y
        y += lines.length * pitch + gap
        return (
          <div key={i}>
            <Abs x={x - 14} y={y0 - 3} w={6} h={6} className="rounded-full" style={{ background: t.ink }} />
            <Lines lines={lines} x={x} w={w} cy={y0} pitch={pitch} size={size} justify={justify} />
          </div>
        )
      })}
    </>
  )
}

/** Slanted grey label band (trapezoid). */
export function LabelBand({ pts, text, x, cy, align = 'left', w }: { pts: Pt[]; text: string; x: number; cy: number; align?: 'left' | 'right' | 'center'; w?: number }) {
  return (
    <>
      <Poly pts={pts} c={t.label} />
      <T x={x} w={w} cy={cy} size={25} align={align} className="text-white">{text}</T>
    </>
  )
}

/** Big filled quote mark (lucide glyph; opening and closing use the same mark). */
export const Quote = ({ x, y, color = t.blue, size = 46 }: { x: number; y: number; close?: boolean; color?: string; size?: number }) => (
  <Abs x={x} y={y}><QuoteIcon size={size} fill={color} color={color} strokeWidth={1} /></Abs>
)
