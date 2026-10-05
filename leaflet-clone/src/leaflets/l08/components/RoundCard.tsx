import type { ReactNode } from 'react'
import { Placed, cn } from '../../../ui'
import { theme } from '../theme'

export interface RoundCardProps {
  x: number
  y: number
  width: number
  height: number
  className?: string
  children?: ReactNode
}

/** Soft white rounded card. */
export function RoundCard({ x, y, width, height, className, children }: RoundCardProps) {
  return (
    <Placed x={x} y={y} width={width} height={height} className={cn('rounded-[18px]', className)} style={{ background: theme.card }}>
      {children}
    </Placed>
  )
}
