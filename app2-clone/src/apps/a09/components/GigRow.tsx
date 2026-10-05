import { Heart, Star } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Gig } from '../data'

export function GigRow({ gig }: { gig: Gig }) {
  return (
    <div className="flex h-[111px] w-[367px] overflow-hidden rounded-[8px] bg-white">
      <div className="relative h-full w-[145px] shrink-0">
        <ImagePlaceholder label="gig image" className="h-full w-full" />
        {gig.badge && (
          <span className="absolute top-[14px] left-[10px] rounded-[4px] bg-[#1d2b54] px-[7px] py-[2px] text-[10px] font-semibold tracking-[0.3px] text-white">
            {gig.badge.split(' ')[0]} <span className="text-[#5ed79d]">{gig.badge.split(' ')[1]}</span>
          </span>
        )}
      </div>
      <div className="relative flex min-w-0 flex-1 flex-col pt-[9px] pr-[10px] pl-[9px]">
        <div className="flex items-center gap-[4px] text-[15px] font-semibold text-[#222325]">
          <Star size={13} fill="currentColor" strokeWidth={0} />
          {gig.rating}
          <span className="text-[13px] font-normal text-[#95979d]">{gig.reviews}</span>
        </div>
        <Heart size={21} strokeWidth={1.4} className="absolute top-[8px] right-[9px] text-[#b5b6ba]" />
        <p className="mt-[5px] pr-[14px] text-[14px] leading-[17px] text-[#404145]">{gig.title}</p>
        <div className="mt-auto mb-[8px] self-end text-[12px] text-[#74767e]">
          From <span className="text-[16px] font-semibold text-[#222325]">{gig.price}</span>
        </div>
      </div>
    </div>
  )
}
