import type { LucideIcon } from 'lucide-react'
import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface CircleIconButtonProps {
  icon: LucideIcon
  size: number
  iconSize?: number
  strokeWidth?: number
  className?: string
  /** Optional corner badge (e.g. notification count). */
  badge?: ReactNode
}

/** Circular icon button with an optional badge, styled via className. */
export function CircleIconButton({ icon: Icon, size, iconSize = 22, strokeWidth = 1.7, className, badge }: CircleIconButtonProps) {
  return (
    <div
      className={cn('relative flex shrink-0 items-center justify-center rounded-full', className)}
      style={{ width: size, height: size }}
    >
      <Icon size={iconSize} strokeWidth={strokeWidth} />
      {badge}
    </div>
  )
}

export function CountBadge({ count, color, size = 16, top = -1, right = -1 }: { count: number; color: string; size?: number; top?: number; right?: number }) {
  return (
    <span
      className="absolute flex items-center justify-center rounded-full font-medium text-white"
      style={{ width: size, height: size, top, right, background: color, fontSize: size * 0.6, lineHeight: 1 }}
    >
      {count}
    </span>
  )
}
