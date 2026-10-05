import type { LucideIcon } from 'lucide-react'
import { IconButton } from '../../../ui'

/** Round light-grey header button. */
export function CircleButton({ icon, size, iconSize }: { icon: LucideIcon; size: number; iconSize: number }) {
  return <IconButton icon={icon} size={size} iconSize={iconSize} strokeWidth={2.6} className="bg-[#f4f4f4] text-[#151518]" />
}
