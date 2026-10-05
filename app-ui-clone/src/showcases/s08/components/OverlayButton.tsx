import type { LucideIcon } from 'lucide-react'
import { theme } from '../theme'

/** Frosted round button floating on top of a photo. */
export function OverlayButton({ icon: Icon, size = 37, iconSize = 17 }: { icon: LucideIcon; size?: number; iconSize?: number }) {
  return (
    <span
      className="flex items-center justify-center rounded-full"
      style={{ width: size, height: size, background: 'rgba(248,243,234,0.82)', color: theme.ink }}
    >
      <Icon size={iconSize} strokeWidth={2} />
    </span>
  )
}
