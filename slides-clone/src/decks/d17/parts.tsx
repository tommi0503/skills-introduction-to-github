import type { ReactNode } from 'react'
import { Abs, ImagePlaceholder, cn } from '../../ui'
import { brand } from './data'

/** Brand lock-up: logo mark (placeholder) + wordmark. */
export function Logo({ x, y, size, color = '#fff' }: { x: number; y: number; size: number; color?: string }) {
  return (
    <Abs x={x} y={y} className="flex items-center font-manrope font-bold tracking-[-0.02em]" style={{ gap: size * 0.25, fontSize: size, color }}>
      <ImagePlaceholder className="rounded-sm" tone={color === '#fff' ? '#5b5b66' : '#d4d4d8'} style={{ width: size * 1.1, height: size * 0.7 }} />
      {brand.name}
    </Abs>
  )
}

export const Crystal = ({ x, y, w, h }: { x: number; y: number; w: number; h: number }) => (
  <ImagePlaceholder className="absolute" tone="#25252c" style={{ left: x, top: y, width: w, height: h }} label="crystal render" />
)

export const Mono = ({ x, y, w, children, className }: { x: number; y: number; w?: number; children: ReactNode; className?: string }) => (
  <Abs x={x} y={y} w={w} className={cn('font-plexmono text-[11px] leading-[14px]', className)}>{children}</Abs>
)

export const Glow = ({ x, y, w, h, c }: { x: number; y: number; w: number; h: number; c: string }) => (
  <ImagePlaceholder className="absolute rounded-full" tone={c} style={{ left: x, top: y, width: w, height: h }} label="gradient glow" />
)
