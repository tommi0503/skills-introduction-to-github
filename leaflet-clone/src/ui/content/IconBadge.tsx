import type { LucideIcon } from 'lucide-react'
import { cn } from '../core/cn'

export interface IconBadgeProps {
  icon: LucideIcon
  size?: number
  iconSize?: number
  strokeWidth?: number
  /** Shape/colour of the badge (e.g. 'rounded-full bg-blue-500 text-white'). */
  className?: string
}

/** A lucide icon sitting in a coloured shape. */
export function IconBadge({ icon: Icon, size = 36, iconSize = 18, strokeWidth = 2, className }: IconBadgeProps) {
  return (
    <span className={cn('inline-flex shrink-0 items-center justify-center', className)} style={{ width: size, height: size }}>
      <Icon size={iconSize} strokeWidth={strokeWidth} />
    </span>
  )
}
