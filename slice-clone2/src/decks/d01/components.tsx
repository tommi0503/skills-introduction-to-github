import type { CSSProperties, ReactNode } from 'react'
import { Sparkle } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { t } from './theme'

/** White slide with the hand-drawn rectangular frame. */
export function FrameSlide({ children }: { children: ReactNode }) {
  const f = t.frame
  return (
    <Slide background="#fff" style={{ color: t.ink }}>
      <Abs x={f.x} y={f.y} w={f.w} h={f.h} style={{ border: `${f.border}px solid ${t.ink}` }} />
      {children}
    </Slide>
  )
}

/** Horizontally centred text line, `cy` = vertical centre. */
export function Center({ cy, size, children, className, x = 0, w = 1280 }: { cy: number; size: number; children: ReactNode; className?: string; x?: number; w?: number }) {
  return (
    <Abs x={x} y={cy - size * 0.7} w={w} h={size * 1.4} className={cn('flex items-center justify-center whitespace-nowrap leading-none', className)} style={{ fontSize: size }}>
      {children}
    </Abs>
  )
}

/** Slide heading — optional bold lead + regular tail. */
export function Heading({ text, cy = 118, size = 58 }: { text: string | readonly [string, string]; cy?: number; size?: number }) {
  const [lead, tail] = typeof text === 'string' ? ['', text] : text
  return (
    <Center cy={cy} size={size} className={t.body}>
      {lead && <span className={t.head} style={{ fontSize: size * 1.05 }}>{lead}</span>}
      {tail}
    </Center>
  )
}

export const Croc = ({ x, y, w, h }: { x: number; y: number; w: number; h: number }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label="crocodile illustration" className="h-full w-full rounded-[32px]" /></Abs>
)

export const Star = ({ x, y, size }: { x: number; y: number; size: number }) => (
  <Abs x={x} y={y}><Sparkle size={size} fill={t.star} color={t.ink} strokeWidth={1.4} /></Abs>
)

/** Rounded hand-drawn speech bubble (border ellipse). */
export function Bubble({ x, y, w, h, lines, style }: { x: number; y: number; w: number; h: number; lines: string[]; style?: CSSProperties }) {
  return (
    <Abs x={x} y={y} w={w} h={h} className={cn('flex flex-col items-center justify-center rounded-[50%] bg-white text-center', t.body)} style={{ border: `3px solid ${t.ink}`, fontSize: 30, lineHeight: 1.15, ...style }}>
      {lines.map((l) => <div key={l}>{l}</div>)}
    </Abs>
  )
}

export function Photo({ x, y, w, h }: { x: number; y: number; w: number; h: number }) {
  return (
    <Abs x={x} y={y} w={w} h={h} style={{ border: `3px solid ${t.ink}` }}>
      <ImagePlaceholder label="photo" className="h-full w-full" />
    </Abs>
  )
}
