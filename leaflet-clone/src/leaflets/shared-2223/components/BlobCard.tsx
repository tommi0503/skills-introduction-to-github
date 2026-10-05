import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'

export interface BlobCardProps {
  x: number
  y: number
  width: number
  height: number
  /** CSS border-radius giving the soft, slightly irregular card silhouette. */
  radius?: string
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** White card with big, uneven rounded corners. */
export function BlobCard({
  x,
  y,
  width,
  height,
  radius = '64px 70px 58px 52px / 56px 90px 44px 50px',
  className,
  style,
  children,
}: BlobCardProps) {
  return (
    <div className={cn('absolute bg-white', className)} style={{ left: x, top: y, width, height, borderRadius: radius, ...style }}>
      {children}
    </div>
  )
}
