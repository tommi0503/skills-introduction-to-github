import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export type PillVariant = 'dark' | 'soft' | 'outline'

export interface PillButtonProps {
  children: ReactNode
  variant?: PillVariant
  height?: number
  className?: string
  style?: CSSProperties
}

const variants: Record<PillVariant, CSSProperties> = {
  dark: { background: theme.ink, color: '#fff' },
  soft: { background: theme.soft, color: theme.ink },
  outline: { background: '#fff', color: theme.ink, boxShadow: 'inset 0 0 0 1px #e3e3e3' },
}

/** Rounded-full action button used across the page. */
export function PillButton({ children, variant = 'dark', height = 40, className, style }: PillButtonProps) {
  return (
    <span
      className={cn('inline-flex items-center justify-center rounded-full text-[14px] font-[450] leading-5', className)}
      style={{ height, ...variants[variant], ...style }}
    >
      {children}
    </span>
  )
}
