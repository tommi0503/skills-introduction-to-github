import type { ReactNode } from 'react'
import { Placed } from '../../../ui'
import { theme } from '../theme'

/** Dark green capsule section title. */
export function PillHeading({ x, y, width, children }: { x: number; y: number; width: number; children: ReactNode }) {
  return (
    <Placed
      x={x}
      y={y}
      width={width}
      height={43}
      className="flex items-center justify-center rounded-full font-dohyeon text-[23px] tracking-[-0.03em] leading-none"
      style={{ background: theme.green, color: theme.onGreen }}
    >
      {children}
    </Placed>
  )
}
