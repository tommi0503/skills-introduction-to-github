import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'

export interface PillButtonProps {
  label: string
  icon: LucideIcon
  className?: string
  iconClassName?: string
}

/** Full-width rounded CTA with a leading icon pinned left and a centred label. */
export function PillButton({ label, icon: Icon, className, iconClassName }: PillButtonProps) {
  return (
    <div className={cn('relative flex h-[56px] items-center justify-center rounded-full', className)}>
      <Icon className={cn('absolute left-[40px]', iconClassName)} size={21} strokeWidth={1.8} />
      <span>{label}</span>
    </div>
  )
}
