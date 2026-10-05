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
        boxShadow: '0 0 6px 2px rgba(62,142,254,0.45), inset 0 0 8px rgba(255,255,255,0.25)',
      }}
    >
      <Icon size={19} strokeWidth={1.8} />
      {label}
    </div>
  )
}
