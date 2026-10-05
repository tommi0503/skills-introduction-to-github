import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'

export interface CircleIconProps {
  icon: LucideIcon
  size?: number
  iconSize?: number
  strokeWidth?: number
  className?: string
  fill?: string
}

/** White floating round button hosting a lucide icon. */
export function CircleIcon({ icon: Icon, size = 40, iconSize = 20, strokeWidth = 2.2, className, fill = 'none' }: CircleIconProps) {
  return (
    <span
      className={cn('flex shrink-0 items-center justify-center rounded-full bg-white text-black', className)}
      style={{ width: size, height: size }}
    >
      <Icon size={iconSize} strokeWidth={strokeWidth} fill={fill} />
    </span>
  )
}
