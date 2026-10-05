import { Star } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { palette as c } from '../theme'

export interface ListingStatsProps {
  rating: string
  badge: string[]
  reviews: string
  reviewsLabel: string
}

function Laurel({ flip }: { flip?: boolean }) {
  return (
    <ImagePlaceholder
      className="rounded-full"
      style={{ width: 13, height: 30, transform: flip ? 'scaleX(-1)' : undefined }}
      label="laurel"
    />
  )
}

export function ListingStats({ rating, badge, reviews, reviewsLabel }: ListingStatsProps) {
  const divider = <span className="h-[34px] w-px" style={{ background: c.line }} />
  return (
    <div className="flex items-center" style={{ color: c.text }}>
      <div className="flex w-[106px] flex-col items-center">
        <span className="text-[16.5px] leading-[20px] font-semibold">{rating}</span>
        <span className="mt-[1px] flex gap-[1px]">
          {Array.from({ length: 5 }, (_, i) => (
            <Star key={i} size={8} fill={c.text} strokeWidth={0} />
          ))}
        </span>
      </div>
      {divider}
      <div className="flex w-[160px] items-center justify-center gap-[8px]">
        <Laurel />
        <span className="text-center text-[15px] leading-[16px] font-semibold">
          {badge.map((b) => (
            <span key={b} className="block">
              {b}
            </span>
          ))}
        </span>
        <Laurel flip />
      </div>
      {divider}
      <div className="flex w-[98px] flex-col items-center">
        <span className="text-[16.5px] leading-[20px] font-semibold">{reviews}</span>
        <span className="text-[10.5px] leading-[13px] font-semibold">{reviewsLabel}</span>
      </div>
    </div>
  )
}
