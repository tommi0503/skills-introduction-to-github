import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../core/cn'

export interface PlacedProps {
  x: number
  y: number
  width?: number
  height?: number
  zIndex?: number
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** Absolute positioning helper (panel or sheet coordinates). */
export function Placed({ x, y, width, height, zIndex, className, style, children }: PlacedProps) {
  return (
    <div className={cn('absolute', className)} style={{ left: x, top: y, width, height, zIndex, ...style }}>
      {children}
    </div>
  )
}
