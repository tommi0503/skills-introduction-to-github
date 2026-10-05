import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'

export interface IconCircleProps {
  icon: LucideIcon
  size?: number
  iconSize?: number
  strokeWidth?: number
  className?: string
  iconClassName?: string
}

/** Round button with a centred lucide icon; look comes from className. */
export function IconCircle({ icon: Icon, size = 40, iconSize = 20, strokeWidth = 1.8, className, iconClassName }: IconCircleProps) {
  return (
    <span className={cn('flex shrink-0 items-center justify-center rounded-full', className)} style={{ width: size, height: size }}>
      <Icon size={iconSize} strokeWidth={strokeWidth} className={iconClassName} />
    </span>
  )
}
