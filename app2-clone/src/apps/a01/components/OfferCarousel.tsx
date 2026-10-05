import { CircleDot } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { OfferCard } from '../data'
import { theme } from '../theme'

function Offer({ offer }: { offer: OfferCard }) {
  return (
    <div className="flex h-[133px] w-[301px] shrink-0 overflow-hidden rounded-[10px] bg-white shadow-[0_1px_8px_rgba(0,0,0,0.06)]">
      <ImagePlaceholder className="h-full w-[92px]" label={`${offer.store} logo`} />
      {offer.store && (
        <div className="flex flex-col pt-[17px] pl-[16px] pr-[12px]">
          <span className="text-[13.5px] leading-[17px] font-semibold text-[#222]">{offer.store}</span>
          <span className="text-[13.5px] leading-[19px] font-semibold" style={{ color: theme.purple }}>
            {offer.cashBack}
          </span>
          <span className="mt-[1px] text-[11px] leading-[16px] text-[#55555c]">{offer.description}</span>
          <span className="mt-[6px] flex h-[24px] w-[81px] items-center justify-center gap-[5px] rounded-[6px] border border-dashed border-[#9a9aa0] text-[11px] font-semibold tracking-[1px] text-[#55555c]">
            <CircleDot size={12} strokeWidth={2.4} />
            {offer.code}
          </span>
        </div>
      )}
    </div>
  )
}

export function OfferCarousel({ offers, top }: { offers: OfferCard[]; top: number }) {
  return (
    <div className="absolute flex gap-[20px]" style={{ left: 21, top }}>
      {offers.map((o) => (
        <Offer key={o.key} offer={o} />
      ))}
    </div>
  )
}
