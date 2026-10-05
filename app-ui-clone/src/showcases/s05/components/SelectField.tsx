import { ChevronDown } from 'lucide-react'
import { cn } from '../../../ui'
import { cardShadow, theme } from '../theme'

export function SelectField({ value, className }: { value: string; className?: string }) {
  return (
    <div
      className={cn('flex h-[48px] items-center justify-between rounded-[16px] pr-[10px] pl-[21px]', className)}
      style={{ background: theme.card, boxShadow: cardShadow }}
    >
      <span className="text-[14.5px] font-medium tracking-[-0.1px] text-[#1a1a1a]">{value}</span>
      <span className="flex h-[32px] w-[32px] items-center justify-center rounded-full bg-white">
        <ChevronDown size={15} strokeWidth={1.8} color="#222" />
      </span>
    </div>
  )
}
