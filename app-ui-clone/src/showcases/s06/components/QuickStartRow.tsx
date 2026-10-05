import { ChevronRight } from 'lucide-react'
import { cn } from '../../../ui'
import type { QuickStartItem } from '../data'
import { theme } from '../theme'

export interface QuickStartRowProps {
  item: QuickStartItem
  selected?: boolean
}

export function QuickStartRow({ item, selected }: QuickStartRowProps) {
  const Icon = item.icon
  return (
    <div
      className={cn('flex h-[73px] items-center rounded-[14px] pr-[17px] pl-[17px]')}
      style={{
        background: theme.card,
        border: selected ? '1.5px solid #a9d3fb' : '1px solid #eeeeea',
        boxShadow: '0 2px 6px rgba(0,0,0,0.03)',
      }}
    >
      <span className="flex h-[42px] w-[42px] items-center justify-center rounded-[11px] bg-[#f7f7f3]">
        <Icon size={17} strokeWidth={1.6} color={theme.blue} />
      </span>
      <div className="ml-[11px] flex-1 pt-[3px]">
        <p className="text-[14.5px] font-semibold tracking-[-0.2px] text-[#111]">{item.title}</p>
        <p className="mt-[3px] text-[11px] tracking-[-0.1px] text-[#ababab]">{item.subtitle}</p>
      </div>
      <span className="flex h-[28px] w-[28px] items-center justify-center rounded-[7px] text-white" style={{ background: theme.blue }}>
        <ChevronRight size={14} strokeWidth={2.2} />
      </span>
    </div>
  )
}
