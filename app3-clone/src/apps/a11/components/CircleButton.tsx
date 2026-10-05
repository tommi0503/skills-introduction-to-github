import type { LucideIcon } from 'lucide-react'
import { IconButton } from '../../../ui'

export function CircleButton({ icon, className }: { icon: LucideIcon; className?: string }) {
  return <IconButton icon={icon} size={42} iconSize={22} strokeWidth={1.9} className={className} />
}
