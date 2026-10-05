import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export interface PillButtonProps {
  variant?: 'solid' | 'ghost'
  className?: string
  style?: CSSProperties
  children: ReactNode
}

/** Fully rounded Cosmos button: black solid, or outlined ghost. */
export function PillButton({ variant = 'solid', className, style, children }: PillButtonProps) {
  const solid = variant === 'solid'
  return (
    <span
      className={cn('inline-flex items-center justify-center rounded-full font-medium', className)}
      style={{
        background: solid ? theme.color.ink : 'transparent',
        color: solid ? '#fff' : theme.color.ink,
        border: solid ? undefined : `1px solid ${theme.color.searchBorder}`,
        ...style,
      }}
    >
      {children}
    </span>
  )
}
