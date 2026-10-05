import type { CSSProperties, ReactNode } from 'react'
import { cn } from './cn'

export interface ContainerProps {
  /** Max content width in px (centred). */
  width?: number
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** Centred max-width column used by every section. */
export function Container({ width = 1200, className, style, children }: ContainerProps) {
  return (
    <div className={cn('mx-auto w-full', className)} style={{ maxWidth: width, ...style }}>
      {children}
    </div>
  )
}
