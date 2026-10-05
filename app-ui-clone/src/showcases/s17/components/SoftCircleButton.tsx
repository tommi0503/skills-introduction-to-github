import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'

/** Pale round button with a single glyph. */
export function SoftCircleButton({ icon: Icon, size = 54, iconSize = 22, className }: { icon: LucideIcon; size?: number; iconSize?: number; className?: string }) {
  return (
    <span className={cn('flex items-center justify-center rounded-full bg-[#f0f0f0] text-[#2f3347]', className)} style={{ width: size, height: size }}>
      <Icon size={iconSize} strokeWidth={2} />
    </span>
  )
}
