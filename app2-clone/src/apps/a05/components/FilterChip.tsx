import { ChevronDown } from 'lucide-react'
import { cn } from '../../../ui'
import { Floating } from './Floating'

export interface FilterChipProps {
  label: string
  leading?: 'dot'
  trailing?: 'chevron'
  className?: string
}

export function FilterChip({ label, leading, trailing, className }: FilterChipProps) {
  return (
    <Floating className={cn('h-[26px] gap-[5px] px-[9px] text-[13.5px] font-medium text-[#111]', className)}>
      {leading && <span className="h-[12px] w-[12px] rounded-full border border-[#bbb] bg-[#f4f4f4]" />}
      <span>{label}</span>
      {trailing && <ChevronDown size={15} strokeWidth={2} />}
    </Floating>
  )
}
