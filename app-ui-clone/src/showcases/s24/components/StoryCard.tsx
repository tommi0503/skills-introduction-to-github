import { ImagePlaceholder, cn } from '../../../ui'
import type { StoryCardItem } from '../data'

export function StoryCard({ item, className }: { item: StoryCardItem; className?: string }) {
  return (
    <div className={cn('w-[348px] font-pretendard', className)}>
      <ImagePlaceholder label={item.title} className="w-full rounded-[8px]" style={{ height: item.imageHeight }} />
      <div className="mt-[17px] px-[9px] text-[15.6px] font-bold leading-[18px] tracking-[-0.3px] text-[#33364a]">
        {item.title}
      </div>
      <div className="mt-[4px] px-[9px] text-[13.2px] leading-[16px] tracking-[-0.2px] text-[#7a7d8a]">{item.subtitle}</div>
    </div>
  )
}
