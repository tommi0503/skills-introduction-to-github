import type { ReactNode } from 'react'
import { cn } from '../../ui'

export interface PrimaryButtonProps {
  children: ReactNode
  /** Visual state. */
  variant?: 'primary' | 'disabled' | 'soft'
  background?: string
  color?: string
  height?: number
  radius?: number
  fontSize?: number
  className?: string
  style?: React.CSSProperties
}

const VARIANTS = {
  primary: { background: '#4caf50', color: '#fff' },
  disabled: { background: '#e2e2e2', color: '#a8a8a8' },
  soft: { background: '#e7f6ea', color: '#3c9a4c' },
} as const

/** Full-width rounded action button (logical px). */
export function PrimaryButton({
  children,
  variant = 'primary',
  background,
  color,
  height = 52,
  radius = 8,
  fontSize = 16,
  className,
  style,
}: PrimaryButtonProps) {
  const v = VARIANTS[variant]
  return (
    <div
      className={cn('flex items-center justify-center font-semibold', className)}
      style={{
        height,
        borderRadius: radius,
        background: background ?? v.background,
        color: color ?? v.color,
        fontSize,
        letterSpacing: -0.3,
        ...style,
      }}
    >
      {children}
    </div>
  )
}
