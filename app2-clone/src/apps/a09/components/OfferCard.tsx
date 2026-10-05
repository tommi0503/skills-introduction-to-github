import { ImagePlaceholder } from '../../../ui'
import { FvButton } from './Buttons'
import { fv } from '../theme'

export interface Offer {
  seller: string
  title: string
  price: string
  delivery: string
  expires: string
}

export function OfferCard({ offer }: { offer: Offer }) {
  return (
    <div className="w-[333px] shrink-0 rounded-[8px] bg-white px-[9px] pt-[10px] pb-[10px]">
      <div className="flex gap-[11px] border-b border-[#f0f0f0] pb-[15px]">
        <ImagePlaceholder label="gig thumbnail" className="h-[59px] w-[79px] rounded-[2px]" />
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-[9px]">
            <span className="relative">
              <ImagePlaceholder label="avatar" className="h-[24px] w-[24px] rounded-full" />
              <span className="absolute right-0 bottom-0 h-[6px] w-[6px] rounded-full border border-white" style={{ background: fv.online }} />
            </span>
            <span className="text-[15.5px] font-medium text-[#222325]">{offer.seller}</span>
          </div>
          <p className="mt-[7px] pr-[10px] text-[14px] leading-[17px] text-[#404145]">{offer.title}</p>
        </div>
      </div>
      <p className="mt-[7px] text-[14px] leading-[20px] text-[#62646a]">
        {offer.price} • {offer.delivery}
      </p>
      <p className="mt-[4px] text-[14px] leading-[20px] text-[#62646a]">{offer.expires}</p>
      <div className="mt-[5px] flex gap-[10px]">
        <FvButton className="h-[40px] flex-1">Open in Chat</FvButton>
        <FvButton variant="solid" className="h-[40px] flex-1">
          Review
        </FvButton>
      </div>
    </div>
  )
}
