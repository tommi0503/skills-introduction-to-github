import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export interface OutlineChipProps {
  label: string
  icon?: LucideIcon
  className?: string
}

/** Pale-blue chip with a light blue outline (Generate / Add CTA). */
export function OutlineChip({ label, icon: Icon, className }: OutlineChipProps) {
  return (
    <span
      className={cn('flex items-center justify-center gap-[5px] rounded-[10px] font-medium', className)}
      style={{ background: theme.chipBlue, border: `1.5px solid ${theme.chipBorder}`, color: '#3ea2f2' }}
    >
      {Icon && <Icon size={13} strokeWidth={1.8} />}
      {label}
    </span>
  )
}
