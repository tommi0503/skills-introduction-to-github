import { ImagePlaceholder, cn } from '../../../ui'
import type { ServiceItem } from '../data'
import { theme } from '../theme'

export interface ServiceCardProps {
  item: ServiceItem
  className?: string
  style?: React.CSSProperties
}

/** Monthly plan card: copy on the left, product photo (placeholder) on the right. */
export function ServiceCard({ item, className, style }: ServiceCardProps) {
  const { photo } = item
  return (
    <div
      className={cn('relative h-[155.5px] w-[340px] overflow-hidden rounded-[4px] font-pretendard', className)}
      style={{ background: item.surface, ...style }}
    >
      <ImagePlaceholder
        label={`${item.name} 사진`}
        className="absolute"
        style={{ left: photo.x, top: photo.y, width: photo.w, height: photo.h, borderRadius: photo.radius }}
      />
      <div className="absolute top-[20px] left-[19px]" style={{ color: theme.ink }}>
        <div className="text-[18.5px] font-bold leading-[22px] tracking-[0px]">{item.name}</div>
        <div className="mt-[8px] text-[15.3px] leading-[22px] tracking-[0px]" style={{ color: '#2e2e2e' }}>
          {item.details.map((line) => (
            <div key={line}>{line}</div>
          ))}
        </div>
      </div>
      <div className="absolute top-[118px] left-[19px] flex items-baseline gap-[2px]" style={{ color: theme.ink }}>
        <span className="text-[16.5px] font-bold tracking-[-0.2px]">{item.price}</span>
        <span className="text-[15.3px] tracking-[0px]" style={{ color: '#333' }}>
          {item.unit}
        </span>
      </div>
    </div>
  )
}
