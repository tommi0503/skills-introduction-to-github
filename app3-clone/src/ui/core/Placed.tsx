import type { CSSProperties, ReactNode } from 'react'
import { cn } from './cn'

export interface PlacedProps {
  x: number
  y: number
  width?: number
  height?: number
  rotate?: number
  zIndex?: number
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** Absolutely positions its children inside a Stage (or any relative parent). */
export function Placed({ x, y, width, height, rotate, zIndex, className, style, children }: PlacedProps) {
  return (
    <div
      className={cn('absolute', className)}
      style={{
        left: x,
        top: y,
        width,
        height,
        zIndex,
        transform: rotate ? `rotate(${rotate}deg)` : undefined,
        ...style,
      }}
    >
      {children}
    </div>
  )
}
