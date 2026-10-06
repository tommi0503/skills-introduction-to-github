import type { ReactNode } from 'react'
import { Abs, ImagePlaceholder, cn } from '../../ui'

export const vero = { bg: '#1b1b1b', panel: '#2b2b2b', blue: '#3d82d6', muted: '#8d8d8d', mark: '#b7897c' }

export function VeroLogo({ x, y, size = 24 }: { x: number; y: number; size?: number }) {
  return (
    <Abs x={x} y={y} className="flex items-center font-manrope font-medium text-white" style={{ gap: size * 0.3, fontSize: size }}>
      <ImagePlaceholder className="rounded-sm" tone="#6b5a55" style={{ width: size * 0.9, height: size * 0.9 }} label="vero mark" />
      vero
    </Abs>
  )
}

export function VeroHeader({ section, page }: { section: string; page?: string }) {
  return (
    <>
      <VeroLogo x={48} y={50} size={22} />
      <Abs x={289} y={58} className="text-[12px] text-white/50">{section}</Abs>
      {page && <Abs x={0} y={58} w={1232} className="text-right text-[12px] text-white/50">{page}</Abs>}
    </>
  )
}

export const Heading = ({ x, y, w, size = 52, lh = 67, children, className }: { x: number; y: number; w?: number; size?: number; lh?: number; children: ReactNode; className?: string }) => (
  <Abs x={x} y={y} w={w} className={cn('font-manrope font-bold uppercase text-white', className)} style={{ fontSize: size, lineHeight: `${lh}px` }}>{children}</Abs>
)

export const Photo = ({ x, y, w, h, className }: { x: number; y: number; w: number; h: number; className?: string }) => (
  <ImagePlaceholder className={cn('absolute', className)} tone="#3a3a3f" label="photo" style={{ left: x, top: y, width: w, height: h }} />
)
