import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'

export interface IconDiscProps {
  icon: LucideIcon
  size: number
  iconSize?: number
  strokeWidth?: number
  /** Fill the glyph (solid phone / pin look). */
  filled?: boolean
  className?: string
}

/** Filled blue circle with a white lucide glyph (phone / pin / link / clock). */
export function IconDisc({ icon: Icon, size, iconSize = Math.round(size * 0.55), strokeWidth = 2.4, filled, className }: IconDiscProps) {
  return (
    <span
      className={cn('inline-flex shrink-0 items-center justify-center rounded-full bg-[#4677ae] text-white', className)}
      style={{ width: size, height: size }}
    >
      <Icon size={iconSize} strokeWidth={strokeWidth} fill={filled ? 'currentColor' : 'none'} />
    </span>
  )
}
