import type { ReactNode } from 'react'
import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'

export interface FvButtonProps {
  children: ReactNode
  variant?: 'solid' | 'outline'
  icon?: LucideIcon
  className?: string
}

/** Rectangular Fiverr button — black solid or hairline outline. */
export function FvButton({ children, variant = 'outline', icon: Icon, className }: FvButtonProps) {
  return (
    <span
      className={cn(
        'flex items-center justify-center gap-[10px] rounded-[6px] text-[15px] font-medium',
        variant === 'solid' ? 'bg-[#111] text-white' : 'border border-[#9a9b9f] bg-white text-[#222325]',
        className,
      )}
    >
      {Icon && <Icon size={21} strokeWidth={1.7} />}
      {children}
    </span>
  )
}
