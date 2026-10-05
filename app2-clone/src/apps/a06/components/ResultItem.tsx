import { Star } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import type { ResultData } from '../data'
import { theme } from '../theme'
import { DiscountBar } from './DiscountBar'
import { DeliveryInfo } from './DeliveryInfo'
import { TagRows } from './Tag'

/** Search result row: photo card with caption/price/discount, then store details. */
export function ResultItem({ item, className }: { item: ResultData; className?: string }) {
  return (
    <div className={cn('flex gap-[12px] border-b border-[#f0f1f3] pb-[15px] pl-[13px] pt-[15px]', className)}>
      <div className="relative h-[106px] w-[113px] shrink-0 overflow-hidden rounded-[8px]">
        <ImagePlaceholder label="menu photo" tone="#b8bcc2" className="h-full w-full" />
        <div className="absolute left-[7px] right-[6px] top-[6px] text-white">
          <p className="truncate text-[11.5px] leading-[16px] tracking-[-0.3px]">{item.thumb.caption}</p>
          <p className="text-[13px] font-bold leading-[18px]">{item.thumb.price}</p>
        </div>
        <DiscountBar label={item.thumb.discount} className="absolute inset-x-0 bottom-0 h-[18px]" />
      </div>
      <div className="min-w-0 flex-1 pr-[12px] tracking-[-0.3px]">
        <p className="text-[16px] font-bold leading-[20px] text-[#111]">{item.name}</p>
        <p className="mt-[2px] truncate text-[13px] leading-[20px] text-[#8a8d92]">
          {item.desc.map((r, i) => (
            <span key={i} style={r.hit ? { color: theme.blue } : undefined}>
              {r.text}
            </span>
          ))}
        </p>
        <p className="flex h-[22px] items-center gap-[3px] text-[13px]">
          <Star size={15} fill={theme.star} color={theme.star} />
          <b className="font-bold text-[#222]">{item.rating}</b>
          <span className="text-[#8a8d92]">{item.reviews}</span>
          <span className="ml-[3px] text-[#8a8d92]">최소주문</span>
          <span className="text-[#333]">{item.minOrder}</span>
        </p>
        <DeliveryInfo eta={item.eta} etaIcon={item.etaIcon} className="h-[21px] text-[13px]" />
        <TagRows rows={item.tags} className="mt-[4px]" />
        {item.ad && <p className="mt-[5px] text-[9.5px] leading-[10px] text-[#a6a9ad]">광고</p>}
      </div>
    </div>
  )
}
