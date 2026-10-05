import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'
import { library } from '../theme'

interface FramedPillProps {
  fill: string
  width?: number
  height?: number
  borderWidth?: number
  /** Corner radius; defaults to a full capsule. */
  radius?: number
  className?: string
  style?: CSSProperties
  children: ReactNode
}

/** Capsule / rounded label with the navy outline used throughout the library leaflets. */
export function FramedPill({ fill, width, height, borderWidth = 2, radius = 999, className, style, children }: FramedPillProps) {
  return (
    <span
      className={cn('box-border inline-flex shrink-0 items-center justify-center whitespace-nowrap', className)}
      style={{ width, height, background: fill, border: `${borderWidth}px solid ${library.ink}`, borderRadius: radius, ...style }}
    >
      {children}
    </span>
  )
}
