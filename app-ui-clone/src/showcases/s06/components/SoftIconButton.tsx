import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export interface SoftIconButtonProps {
  icon: LucideIcon
  size?: number
  iconSize?: number
  color?: string
  className?: string
}

/** Rounded-square tinted button hosting a single icon. */
export function SoftIconButton({ icon: Icon, size = 47, iconSize = 20, color = '#555', className }: SoftIconButtonProps) {
  return (
    <span
      className={cn('flex items-center justify-center rounded-[12px]', className)}
      style={{ width: size, height: size, background: theme.softBlue }}
    >
      <Icon size={iconSize} strokeWidth={1.7} color={color} />
    </span>
  )
}
