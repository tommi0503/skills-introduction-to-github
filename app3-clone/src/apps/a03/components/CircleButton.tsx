import type { LucideIcon } from 'lucide-react'
import { IconButton, cn } from '../../../ui'

/** White circular header button. */
export function CircleButton({ icon, className }: { icon: LucideIcon; className?: string }) {
  return <IconButton icon={icon} size={50} iconSize={20} strokeWidth={1.8} className={cn('bg-white text-[#161616]', className)} />
}
