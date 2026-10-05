import type { ButtonHTMLAttributes, ReactNode } from 'react'
import type { LucideIcon } from 'lucide-react'
import { cn } from '../core/cn'

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  leadingIcon?: LucideIcon
  trailingIcon?: LucideIcon
  iconSize?: number
  iconStrokeWidth?: number
  className?: string
  children?: ReactNode
}

/** Text button with optional lucide icons; visual style injected via className. */
export function Button({
  leadingIcon: Lead,
  trailingIcon: Trail,
  iconSize = 18,
  iconStrokeWidth = 2,
  className,
  children,
  ...rest
}: ButtonProps) {
  return (
    <button type="button" className={cn('inline-flex items-center justify-center', className)} {...rest}>
      {Lead && <Lead size={iconSize} strokeWidth={iconStrokeWidth} />}
      {children}
      {Trail && <Trail size={iconSize} strokeWidth={iconStrokeWidth} />}
    </button>
  )
}
