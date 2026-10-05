import { Star, Trophy, Languages } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Listing } from '../data'
import { airbnb } from '../theme'

export function ListingSummary({ listing }: { listing: Listing }) {
  return (
    <div className="flex px-[26px] pt-[24px] pb-[23px]">
      <ImagePlaceholder className="rounded-[8px]" style={{ width: 133, height: 103 }} label="listing photo" />
      <div className="ml-[16px] flex flex-1 flex-col pt-[1px]">
        <span className="text-[11.5px]" style={{ color: airbnb.muted }}>
          {listing.kind}
        </span>
        <div className="mt-[8px] text-[15px] leading-[19px]" style={{ color: airbnb.ink }}>
          {listing.title.map((line, i) => (
            <div key={line} className="flex items-center">
              {i === 0 && <Languages size={12} strokeWidth={2} className="mr-[6px]" />}
              {line}
            </div>
          ))}
        </div>
        <div className="mt-[22px] flex items-center text-[11.5px]" style={{ color: airbnb.ink }}>
          <Star size={10} fill="currentColor" strokeWidth={0} className="mr-[2px]" />
          <span>{listing.rating}</span>
          <span className="ml-[3px]" style={{ color: airbnb.muted }}>
            {listing.reviews} ·
          </span>
          <Trophy size={9} fill="currentColor" strokeWidth={1.5} className="mr-[2px] ml-[4px]" />
          <span style={{ color: airbnb.muted }}>{listing.badge}</span>
        </div>
      </div>
    </div>
  )
}
