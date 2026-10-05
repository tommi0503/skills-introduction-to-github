import { BadgePercent, Crown } from 'lucide-react'
import type { Offer } from '../data'

const icons = { badge: BadgePercent, crown: Crown }

/** Ticket-shaped coupon card with notches cut into both sides. */
export function OfferCard({ offer }: { offer: Offer }) {
  const Icon = icons[offer.icon]
  return (
    <div className="relative h-[94px] w-[238px] shrink-0 rounded-[14px] border border-[#ececec] bg-white px-[16px] pt-[16px]">
      {(['-left-[8px]', '-right-[8px]'] as const).map((side) => (
        <span
          key={side}
          className={`absolute ${side} top-[42px] h-[16px] w-[16px] rounded-full border border-[#ececec] bg-white`}
          style={{ clipPath: side.startsWith('-left') ? 'inset(0 0 0 50%)' : 'inset(0 50% 0 0)' }}
        />
      ))}
      <div className="flex items-center gap-[9px]">
        <Icon size={19} strokeWidth={0} fill="#b8484b" className="[&_path:not(:first-child)]:stroke-white [&_path:not(:first-child)]:[stroke-width:2.2px]" />
        <span className="text-[17px] font-medium text-[#1c1c1c]">{offer.title}</span>
      </div>
      <p className="mt-[3px] pr-[8px] text-[12.8px] leading-[15.5px] text-[#8c8c8c]">{offer.description}</p>
    </div>
  )
}
