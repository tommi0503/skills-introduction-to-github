import { cn } from '../../../ui'
import { sp } from '../theme'

export function Chip({ label, active, className }: { label: string; active?: boolean; className?: string }) {
  return (
    <span
      className={cn('flex h-[32px] shrink-0 items-center rounded-full px-[17px] text-[13px]', className)}
      style={active ? { background: sp.green, color: '#000' } : { background: sp.chip, color: sp.white }}
    >
      {label}
    </span>
  )
}
