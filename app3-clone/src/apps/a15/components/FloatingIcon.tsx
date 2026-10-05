import type { LucideIcon } from 'lucide-react'
import { IconButton, cn } from '../../../ui'

/** Translucent white circle over a photo. */
export function FloatingIcon({ icon, className }: { icon: LucideIcon; className?: string }) {
  return <IconButton icon={icon} size={38} iconSize={17} strokeWidth={2} className={cn('absolute bg-white/75 text-[#222]', className)} />
}
