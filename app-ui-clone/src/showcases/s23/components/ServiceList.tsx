import { cn } from '../../../ui'
import type { ServiceItem } from '../data'
import { ServiceCard } from './ServiceCard'

export interface ServiceListProps {
  items: ServiceItem[]
  gap?: number
  className?: string
}

export function ServiceList({ items, gap = 14.5, className }: ServiceListProps) {
  return (
    <div className={cn('flex flex-col px-[25px]', className)} style={{ gap }}>
      {items.map((item) => (
        <ServiceCard key={item.id} item={item} />
      ))}
    </div>
  )
}
