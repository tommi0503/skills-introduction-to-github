import { cn } from '../../../ui'
import type { Activity } from '../data'
import { SectionHeading } from './SectionHeading'

export function ActivityItem({ item, className }: { item: Activity; className?: string }) {
  return (
    <SectionHeading
      title={item.title}
      body={item.desc}
      className={cn('', className)}
      titleClassName="text-[19px] leading-[26px] font-extrabold"
      bodyClassName="mt-[9px] text-[13.8px] leading-[19.5px] tracking-[-0.3px]"
    />
  )
}
