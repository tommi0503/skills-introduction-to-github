import type { ReactNode } from 'react'
import { ChevronRight } from 'lucide-react'
import { cn } from '../../../ui'

export interface ListRowProps {
  leading: ReactNode
  children: ReactNode
  height?: number
  chevron?: boolean
  className?: string
}

export function ListRow({ leading, children, height = 57, chevron = true, className }: ListRowProps) {
  return (
    <div className={cn('flex items-center pr-[16px] pl-[15px]', className)} style={{ height }}>
      <div className="w-[43px] shrink-0">{leading}</div>
      <div className="min-w-0 flex-1">{children}</div>
      {chevron && <ChevronRight size={17} strokeWidth={2} className="shrink-0 text-[#b4b8be]" />}
    </div>
  )
}
