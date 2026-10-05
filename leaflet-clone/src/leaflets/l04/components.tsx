import type { ReactNode } from 'react'
import { cn, Placed } from '../../ui'
import { NotchedFrame } from '../shared-0407/components/NotchedFrame'
import { frame } from './theme'

/** Panel-sized notched line frame (used on both inside panels). */
export function PanelFrame({ color }: { color: string }) {
  return (
    <Placed x={frame.x} y={frame.y}>
      <NotchedFrame width={frame.width} height={frame.height} notch={frame.notch} color={color} strokeWidth={2} />
    </Placed>
  )
}

/** Centred serif section heading with wide tracking. */
export function SerifHeading({ y, className, children }: { y: number; className?: string; children: ReactNode }) {
  return (
    <Placed x={0} y={y} width={480} className={cn('text-center font-noto-serif font-black tracking-[0.18em]', className)}>
      {children}
    </Placed>
  )
}
