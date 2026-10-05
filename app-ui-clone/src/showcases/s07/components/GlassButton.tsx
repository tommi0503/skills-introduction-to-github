import type { LucideIcon } from 'lucide-react'
import { theme } from '../theme'

/** Dark translucent rounded-square button floating over the camera feed. */
export function GlassButton({ icon: Icon, size = 36, iconSize = 18 }: { icon: LucideIcon; size?: number; iconSize?: number }) {
  return (
    <div className="flex items-center justify-center rounded-[9px] text-white" style={{ width: size, height: size, background: theme.glass }}>
      <Icon size={iconSize} strokeWidth={2.4} />
    </div>
  )
}
