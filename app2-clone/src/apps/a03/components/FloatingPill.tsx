import type { ReactNode } from 'react'
import { cn } from '../../../ui'

/** White elevated circle/pill used in the floating headers. */
export function FloatingPill({ left, right, top = 59, height = 42, width, className, children }: {
  left?: number
  right?: number
  top?: number
  height?: number
  width?: number
  className?: string
  children: ReactNode
}) {
  return (
    <div
      className={cn('absolute flex items-center rounded-full bg-white shadow-[0_2px_14px_rgba(0,0,0,0.07)]', className)}
      style={{ left, right, top, height, width }}
    >
      {children}
    </div>
  )
}
