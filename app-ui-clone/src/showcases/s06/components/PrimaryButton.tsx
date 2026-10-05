import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export interface PrimaryButtonProps {
  label: string
  icon: LucideIcon
  className?: string
}

/** Full-width glowing blue CTA. */
export function PrimaryButton({ label, icon: Icon, className }: PrimaryButtonProps) {
  return (
    <div
      className={cn('flex h-[58px] items-center justify-center gap-[12px] rounded-[16px] text-[16px] font-medium text-white', className)}
      style={{
        background: theme.blue,
        boxShadow: 'inset 0 0 7px 2px rgba(255,255,255,0.32), 0 2px 8px rgba(62,142,254,0.3)',
      }}
    >
      <Icon size={19} strokeWidth={1.8} />
      {label}
    </div>
  )
}
