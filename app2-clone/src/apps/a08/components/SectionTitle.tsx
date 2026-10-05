import { MoreHorizontal } from 'lucide-react'
import { cn } from '../../../ui'

export function SectionTitle({ title, className }: { title: string; className?: string }) {
  return (
    <div className={cn('flex items-center justify-between pr-[20px] pl-[16px]', className)}>
      <h2 className="text-[20px] leading-[26px] font-bold text-[#1f2328]">{title}</h2>
      <MoreHorizontal size={22} strokeWidth={2.2} className="text-[#555a62]" />
    </div>
  )
}
