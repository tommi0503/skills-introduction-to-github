import type { LucideIcon } from 'lucide-react'
import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface RoundButtonProps {
  icon?: LucideIcon
  size?: number
  iconSize?: number
  strokeWidth?: number
  className?: string
  children?: ReactNode
}

/** Soft grey circular button. */
export function RoundButton({ icon: Icon, size = 52, iconSize = 21, strokeWidth = 2, className, children }: RoundButtonProps) {
  return (
    <span className={cn('flex shrink-0 items-center justify-center rounded-full bg-[#f2f2f4] text-[#111]', className)} style={{ width: size, height: size }}>
      {Icon && <Icon size={iconSize} strokeWidth={strokeWidth} />}
      {children}
    </span>
  )
}
