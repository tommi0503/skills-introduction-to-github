import { BadgePercent, Heart } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Restaurant } from '../data'
import { theme } from '../theme'
import { Rating } from './Rating'

export function RestaurantCard({ restaurant }: { restaurant: Restaurant }) {
  return (
    <div className="w-[280px] shrink-0 rounded-[10px] border border-[#eeeeee] bg-[#fbfbfb] p-[4px]">
      <div className="relative h-[146px]">
        <ImagePlaceholder label={`${restaurant.name} dish photo`} className="h-full w-full rounded-[7px]" />
        <span
          className="absolute left-[10px] top-[11px] flex h-[31px] items-center gap-[5px] rounded-full pl-[10px] pr-[13px] text-[14px] font-medium text-white"
          style={{ background: theme.accent }}
        >
          <BadgePercent size={15} fill="#fff" color={theme.accent} strokeWidth={2} />
          {restaurant.promo}
        </span>
        <Heart className="absolute right-[9px] top-[14px] text-white" size={24} strokeWidth={2} />
      </div>
      <div className="flex items-center justify-between px-[8px] pt-[13px]">
        <span className="text-[16.5px] text-[#1c1c1c]">{restaurant.name}</span>
        <Rating value={restaurant.rating} count={restaurant.reviews} className="text-[14px]" />
      </div>
      <div className="flex items-center gap-[6px] px-[8px] pt-[2px] pb-[12px] text-[14px] text-[#9a9a9a]">
        <span>{restaurant.price}</span>
        <span className="text-[10px]">•</span>
        <span>{restaurant.kind}</span>
      </div>
    </div>
  )
}
