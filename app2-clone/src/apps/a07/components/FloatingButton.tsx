import type { LucideIcon } from 'lucide-react'
import { IconButton, cn } from '../../../ui'
import { theme } from '../theme'

export interface FloatingButtonProps {
  icon: LucideIcon
  size?: number
  iconSize?: number
  strokeWidth?: number
  className?: string
}

/** White circular button with the soft halo used across the bot app. */
export function FloatingButton({ icon, size = 44, iconSize = 20, strokeWidth = 2, className }: FloatingButtonProps) {
  return (
    <div className={cn('shrink-0 rounded-full', className)} style={{ boxShadow: theme.floatShadow }}>
      <IconButton icon={icon} size={size} iconSize={iconSize} strokeWidth={strokeWidth} className="bg-white text-[#111]" />
    </div>
  )
}
