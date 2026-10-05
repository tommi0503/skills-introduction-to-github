import type { CSSProperties, ReactNode } from 'react'
import { Placed, cn } from '../../../ui'

export interface RoundedBoxProps {
  x: number
  y: number
  width: number
  height: number
  background: string
  radius?: number
  borderColor?: string
  borderWidth?: number
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** Absolutely placed rounded card / band, optionally outlined. */
export function RoundedBox({
  x,
  y,
  width,
  height,
  background,
  radius = 12,
  borderColor,
  borderWidth = 2,
  className,
  style,
  children,
}: RoundedBoxProps) {
  return (
    <Placed
      x={x}
      y={y}
      width={width}
      height={height}
      className={cn('box-border', className)}
      style={{
        background,
        borderRadius: radius,
        border: borderColor ? `${borderWidth}px solid ${borderColor}` : undefined,
        ...style,
      }}
    >
      {children}
    </Placed>
  )
}
