import type { LucideIcon } from 'lucide-react'
import { IconButton, cn } from '../../../ui'
import { floatShadow } from '../theme'

/** White round floating header button. */
export function FloatButton({ icon, className, iconSize = 19 }: { icon: LucideIcon; className?: string; iconSize?: number }) {
  return (
    <IconButton
      icon={icon}
      size={43}
      iconSize={iconSize}
      strokeWidth={1.6}
      className={cn('bg-[#fefefc] text-[#3d3d3a]', floatShadow, className)}
    />
  )
}
