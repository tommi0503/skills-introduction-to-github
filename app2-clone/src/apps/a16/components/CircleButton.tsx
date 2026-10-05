import type { LucideIcon } from 'lucide-react'
import { IconButton, cn } from '../../../ui'

export interface CircleButtonProps {
  icon: LucideIcon
  /** Colour classes (background + icon colour). */
  toneClassName?: string
  className?: string
  size?: number
  iconSize?: number
}

/** Round icon button (header actions). */
export function CircleButton({ icon, toneClassName = 'bg-[#f2f2f3] text-[#111]', className, size = 40, iconSize = 19 }: CircleButtonProps) {
  return <IconButton icon={icon} size={size} iconSize={iconSize} strokeWidth={2} className={cn(toneClassName, className)} />
}
