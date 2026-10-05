import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface CircleButtonProps {
  x: number
  y: number
  size?: number
  background?: string
  className?: string
  children: ReactNode
}

/** Round floating button positioned by its centre. */
export function CircleButton({ x, y, size = 44, background = '#fff', className, children }: CircleButtonProps) {
  return (
    <div
      className={cn('absolute flex items-center justify-center rounded-full', className)}
      style={{ left: x - size / 2, top: y - size / 2, width: size, height: size, background }}
    >
      {children}
    </div>
  )
}
