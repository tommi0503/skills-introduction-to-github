import { Star } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Trending } from '../data'
import { cardTones } from '../theme'

/** Restaurant tile used in "Trending near you". */
export function TrendingCard({ item }: { item: Trending }) {
  return (
    <div className="relative h-[190px] w-[175px] overflow-hidden rounded-[22px]" style={{ background: cardTones[item.tone] }}>
      <span className="absolute top-[12px] right-[11px] flex h-[25px] w-[56px] items-center justify-center gap-[4px] rounded-full bg-white text-[11.5px] text-[#444]">
        <Star size={12} fill="#111" color="#111" />
        {item.rating}
      </span>
      <ImagePlaceholder className="absolute top-[40px] left-[9px] h-[112px] w-[160px] rounded-[10px]" label={item.name} />
      <div className="absolute top-[156px] left-[13px] font-condensed text-[14px] font-bold text-[#111]">{item.name}</div>
      <span className="absolute top-[150px] right-[12px] h-[32px] w-[32px] rounded-full bg-black" />
    </div>
  )
}
