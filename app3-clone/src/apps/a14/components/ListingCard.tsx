import { Heart, Star } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Listing } from '../data'
import { explorePalette as c } from '../theme'

export function ListingCard({ listing }: { listing: Listing }) {
  return (
    <article className="px-[25px]">
      <div className="relative">
        <ImagePlaceholder className="rounded-[12px]" style={{ width: 340, height: 323 }} label={`${listing.place} photo`} />
        <Heart size={23} strokeWidth={1.8} color="#fff" fill="rgba(0,0,0,0.18)" className="absolute top-[18px] right-[18px]" />
        {listing.dots > 0 && (
          <div className="absolute bottom-[12px] left-1/2 flex -translate-x-1/2 items-center gap-[4px]">
            {Array.from({ length: listing.dots }, (_, i) => (
              <span
                key={i}
                className="rounded-full bg-white"
                style={{ width: i === listing.dots - 1 ? 4 : 6, height: i === listing.dots - 1 ? 4 : 6, opacity: i === 0 ? 1 : 0.65 }}
              />
            ))}
          </div>
        )}
      </div>
      <div className="mt-[12px] flex items-start justify-between leading-[22px]" style={{ color: c.text }}>
        <span className="text-[14.5px] font-semibold">{listing.place}</span>
        <span className="flex items-center gap-[4px] text-[14px]">
          <Star size={12} fill={c.text} strokeWidth={0} />
          {listing.rating}
        </span>
      </div>
      {listing.lines.map((l) => (
        <div key={l} className="text-[14.5px] leading-[22px]" style={{ color: c.muted }}>
          {l}
        </div>
      ))}
      <div className="mt-[6px] text-[14.5px] leading-[22px]" style={{ color: c.text }}>
        <span className="font-semibold">{listing.price}</span> {listing.unit}
      </div>
    </article>
  )
}
