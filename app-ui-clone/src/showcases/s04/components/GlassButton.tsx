import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'

export interface GlassButtonProps {
  icon: LucideIcon
  size?: number
  iconSize?: number
  className?: string
}

/** Translucent round button floating over a photo/dark header. */
export function GlassButton({ icon: Icon, size = 48, iconSize = 20, className }: GlassButtonProps) {
  return (
    <div
      className={cn('flex items-center justify-center rounded-full text-white backdrop-blur-sm', className)}
      style={{ width: size, height: size }}
    >
      <Icon size={iconSize} strokeWidth={2} />
    </div>
  )
}
