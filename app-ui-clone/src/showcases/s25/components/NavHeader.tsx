import type { ReactNode } from 'react'
import type { LucideIcon } from 'lucide-react'
import { ChevronLeft } from 'lucide-react'
import { cn } from '../../../ui'

export interface CircleIconProps {
  icon: LucideIcon
  size?: number
  iconSize?: number
  strokeWidth?: number
  className?: string
}

/** Soft grey round icon button used across the bond screens. */
export function CircleIcon({ icon: Icon, size = 39, iconSize = 20, strokeWidth = 1.7, className }: CircleIconProps) {
  return (
    <div
      className={cn('flex shrink-0 items-center justify-center rounded-full bg-[#ececec] text-[#222]', className)}
      style={{ width: size, height: size }}
    >
      <Icon size={iconSize} strokeWidth={strokeWidth} />
    </div>
  )
}

export interface NavHeaderProps {
  center?: ReactNode
  right?: ReactNode
  /** Top of the 39pt button row (pt). */
  top?: number
  className?: string
}

/** Back button · centred title · optional trailing action. */
export function NavHeader({ center, right, top = 61, className }: NavHeaderProps) {
  return (
    <div className={cn('absolute inset-x-0 flex items-center justify-between px-[16.5px]', className)} style={{ top }}>
      <CircleIcon icon={ChevronLeft} iconSize={22} />
      <div className="absolute inset-x-0 flex justify-center">{center}</div>
      {right ?? <span className="w-[39px]" />}
    </div>
  )
}
