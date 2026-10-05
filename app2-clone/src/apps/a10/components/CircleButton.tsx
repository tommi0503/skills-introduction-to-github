import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'

export interface CircleButtonProps {
  icon: LucideIcon
  size?: number
  iconSize?: number
  strokeWidth?: number
  className?: string
  /** shadowed white disc vs bare icon */
  plain?: boolean
}

export function CircleButton({ icon: Icon, size = 46, iconSize = 22, strokeWidth = 2, className, plain }: CircleButtonProps) {
  return (
    <div
      className={cn(
        'flex shrink-0 items-center justify-center rounded-full',
        !plain && 'bg-white shadow-[0_2px_14px_rgba(0,0,0,0.09)]',
        className,
      )}
      style={{ width: size, height: size }}
    >
      <Icon size={iconSize} strokeWidth={strokeWidth} />
    </div>
  )
}
