import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme, type } from '../theme'

export type PillVariant = 'dark' | 'soft' | 'light' | 'outline'

const variants: Record<PillVariant, CSSProperties> = {
  dark: { background: theme.ink, color: theme.white },
  soft: { background: theme.softButton, color: theme.ink },
  light: { background: theme.white, color: theme.ink },
  outline: { background: 'transparent', color: theme.white, boxShadow: 'inset 0 0 0 1px rgba(255,255,255,0.12)' },
}

export interface PillProps {
  variant?: PillVariant
  height?: number
  paddingX?: number
  className?: string
  style?: CSSProperties
  children: ReactNode
}

/** Rounded-full button used across the page. */
export function Pill({ variant = 'dark', height = 44, paddingX = 16, className, style, children }: PillProps) {
  return (
    <span
      className={cn('inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-full', className)}
      style={{ ...type.nav, ...variants[variant], height, paddingInline: paddingX, ...style }}
    >
      {children}
    </span>
  )
}
