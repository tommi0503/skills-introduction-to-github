import { Plus } from 'lucide-react'
import { cn } from '../../../ui'

export interface ChipRowProps {
  labels: string[]
  active?: string
  className?: string
}

/** Horizontally scrolling text chips (home categories). */
export function ChipRow({ labels, active, className }: ChipRowProps) {
  return (
    <div className={cn('flex gap-[8px]', className)}>
      {labels.map((label) => (
        <span
          key={label}
          className={cn(
            'flex h-[50px] shrink-0 items-center rounded-full px-[24px] text-[13.5px] font-medium',
            label === active ? 'bg-black text-white' : 'bg-white text-black',
          )}
        >
          {label}
        </span>
      ))}
    </div>
  )
}

/** Filter chips with a trailing black "+" disc (explore screen). */
export function AddFilterRow({ labels, className }: { labels: string[]; className?: string }) {
  return (
    <div className={cn('flex gap-[16px]', className)}>
      {labels.map((label) => (
        <span key={label} className="flex h-[44px] shrink-0 items-center gap-[9px] rounded-full bg-white pr-[3px] pl-[11px]">
          <span className="text-[13px] font-medium text-[#222]">{label}</span>
          <span className="flex size-[37px] items-center justify-center rounded-full bg-black text-white">
            <Plus size={20} strokeWidth={2.4} />
          </span>
        </span>
      ))}
    </div>
  )
}
