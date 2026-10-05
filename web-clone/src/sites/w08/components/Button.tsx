import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme, type } from '../theme'

export type ButtonVariant = 'solid' | 'outline' | 'ghost'

const variants: Record<ButtonVariant, CSSProperties> = {
  solid: { background: theme.ink, color: theme.page },
  outline: { background: theme.white, color: theme.ink, boxShadow: `inset 0 0 0 1px ${theme.ink}` },
  ghost: { background: 'transparent', color: theme.ink },
}

export interface ButtonProps {
  variant?: ButtonVariant
  width?: number
  height?: number
  radius?: number
  className?: string
  style?: CSSProperties
  children: ReactNode
}

export function Button({ variant = 'solid', width, height = 48, radius = 12, className, style, children }: ButtonProps) {
  return (
    <span
      className={cn('inline-flex items-center justify-center whitespace-nowrap', className)}
      style={{ ...type.nav, ...variants[variant], width, height, borderRadius: radius, paddingInline: width ? 0 : 16, ...style }}
    >
      {children}
    </span>
  )
}
