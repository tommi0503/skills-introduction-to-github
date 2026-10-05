import { Heart, Star } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Stay } from '../data'
import { palette as c } from '../theme'

export function StayCard({ stay }: { stay: Stay }) {
  return (
    <article className="w-[165px] shrink-0">
      <div className="relative">
        <ImagePlaceholder className="rounded-[16px]" style={{ width: 165, height: 156 }} label={`${stay.title} photo`} />
        {stay.guestFavorite && (
          <span
            className="absolute top-[9px] left-[9px] rounded-full bg-white px-[10px] py-[4px] text-[10.5px] leading-[14px] font-semibold"
            style={{ color: c.text, boxShadow: '0 1px 3px rgba(0,0,0,0.12)' }}
          >
            Guest favorite
          </span>
        )}
        <Heart size={21} strokeWidth={2} color="#fff" fill="rgba(0,0,0,0.45)" className="absolute top-[11px] right-[15px]" />
      </div>
      <div className="mt-[8px] text-[13.3px] leading-[16px] font-medium tracking-[0.2px] whitespace-pre-line" style={{ color: c.text }}>
        {stay.title}
      </div>
      <div className="mt-[4px] flex items-center gap-[8px] text-[11.5px] leading-[14px] tracking-[0.15px]" style={{ color: c.muted }}>
        <span>{stay.price}</span>
        <span className="flex items-center gap-[2px]">
          <Star size={8} fill={c.muted} strokeWidth={0} />
          {stay.rating}
        </span>
      </div>
    </article>
  )
}
