import type { ReactNode } from 'react'
import type { LucideIcon } from 'lucide-react'
import { cn } from '../core/cn'

export interface PillProps {
  icon?: LucideIcon
  iconSize?: number
  /** Visual style (bg, border, radius, font) is injected. */
  className?: string
  children?: ReactNode
}

/** Rounded label / badge / button-like capsule. */
export function Pill({ icon: Icon, iconSize = 14, className, children }: PillProps) {
  return (
    <span className={cn('inline-flex items-center justify-center gap-1.5 whitespace-nowrap rounded-full', className)}>
      {Icon && <Icon size={iconSize} strokeWidth={2} />}
      {children}
    </span>
  )
}
