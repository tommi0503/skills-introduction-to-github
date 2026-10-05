import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export interface FloatingProps {
  children?: ReactNode
  className?: string
  style?: CSSProperties
}

/** White, softly shadowed surface used for every floating control (circles, pills, chips). */
export function Floating({ children, className, style }: FloatingProps) {
  return (
    <div
      className={cn('flex items-center justify-center rounded-full bg-white', className)}
      style={{ boxShadow: theme.softShadow, ...style }}
    >
      {children}
    </div>
  )
}
