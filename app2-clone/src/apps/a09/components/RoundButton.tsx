import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'
import { fv } from '../theme'

export interface RoundButtonProps {
  icon: LucideIcon
  size?: number
  iconSize?: number
  strokeWidth?: number
  /** Surface colour (translucent over photos). */
  surface?: string
  className?: string
}

/** White circular control with a soft halo. */
export function RoundButton({ icon: Icon, size = 44, iconSize = 20, strokeWidth = 2, surface = '#fff', className }: RoundButtonProps) {
  return (
    <span
      className={cn('flex shrink-0 items-center justify-center rounded-full text-[#222]', className)}
      style={{ width: size, height: size, background: surface, boxShadow: fv.halo }}
    >
      <Icon size={iconSize} strokeWidth={strokeWidth} />
    </span>
  )
}
