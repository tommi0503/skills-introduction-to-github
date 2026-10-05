import type { CSSProperties, ElementType, ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

interface TypeProps {
  as?: ElementType
  className?: string
  style?: CSSProperties
  children: ReactNode
}

/** Serif display face (Harvey Serif stand-in). */
export function Serif({ as: Tag = 'h2', className, style, children }: TypeProps) {
  return (
    <Tag className={cn('font-normal', className)} style={{ fontFamily: theme.font.serif, ...style }}>
      {children}
    </Tag>
  )
}
