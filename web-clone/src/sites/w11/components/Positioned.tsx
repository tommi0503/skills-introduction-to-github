import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'
import type { Box } from '../data'

export interface PositionedProps {
  box: Partial<Box> & { x?: number; y?: number }
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** Absolutely positioned wrapper using reference coordinates (relative to the parent section). */
export function Positioned({ box, className, style, children }: PositionedProps) {
  return (
    <div
      className={cn('absolute', className)}
      style={{ left: box.x, top: box.y, width: box.w, height: box.h, ...style }}
    >
      {children}
    </div>
  )
}
