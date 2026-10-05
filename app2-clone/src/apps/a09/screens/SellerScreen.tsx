import { Check, ChevronLeft, Diamond, Heart, MapPin, MessageSquareText, Star, Timer } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { seller } from '../data'
import { FvStatusBar } from '../components/FvStatusBar'
import { OnlineAvatar } from '../components/OnlineAvatar'
import { FvButton } from '../components/Buttons'
import { UnderlineTabs } from '../components/UnderlineTabs'
import { ReadMore } from '../components/ReadMore'

export function SellerScreen() {
  return (
    <AppScreen className="font-figtree">
      <FvStatusBar />
      <ChevronLeft size={28} strokeWidth={2} className="absolute top-[66px] left-[8px] text-[#222]" />
      <div className="absolute top-[73px] left-[145px] rounded-full border border-[#efefef] p-[2px]">
        <OnlineAvatar size={94} dot={9} />
      </div>
      <div className="absolute inset-x-0 top-[180px] flex flex-col items-center">
        <h1 className="text-[18.5px] leading-[26px] font-semibold text-[#222325]">{seller.name}</h1>
        <span className="text-[14px] leading-[18px] text-[#95979d]">{seller.handle}</span>
        <span className="mt-[10px] rounded-[3px] bg-[#e4e3fd] px-[8px] text-[12.5px] leading-[19px] font-medium text-[#2b2b8a]">
          {seller.badge}
        </span>
        <div className="mt-[10px] flex items-center gap-[4px] text-[15px] font-semibold text-[#222325]">
          <Star size={12} fill="currentColor" strokeWidth={0} />
          {seller.rating}
          <span className="text-[13px] font-normal text-[#95979d]">{seller.reviews}</span>
          <span className="ml-[10px] flex items-center gap-[2px] rounded-[3px] bg-[#fdead2] px-[6px] text-[12px] leading-[19px] font-medium text-[#b9692a]">
            {seller.level}
            <span className="ml-[4px] flex gap-[1px]">
              {[0, 1, 2].map((i) => (
                <Diamond key={i} size={10} fill="currentColor" strokeWidth={0} />
              ))}
            </span>
          </span>
        </div>
      </div>
      <div className="absolute top-[300px] left-[13px] flex gap-[11px]">
        <FvButton icon={Heart} className="h-[40px] w-[175px]">
          {seller.save}
        </FvButton>
        <FvButton icon={MessageSquareText} variant="solid" className="h-[40px] w-[175px]">
          {seller.contact}
        </FvButton>
      </div>
      <div className="absolute inset-x-0 top-[374px] border-b border-[#ececec]">
        <UnderlineTabs
          items={seller.tabs}
          active={0}
          className="h-[44px] gap-[30px] pl-[14px]"
          itemClassName="text-[16px]"
          barClassName="-inset-x-[14px] h-[2px]"
        />
      </div>

      <div className="absolute inset-x-0 top-[434px] px-[14px] text-[#404145]">
        <h3 className="text-[14.5px] font-semibold text-[#222325]">{seller.vettedTitle}</h3>
        <p className="mt-[2px] pr-[50px] text-[13.5px] leading-[17px] text-[#95979d]">{seller.vettedText}</p>
        <h2 className="mt-[24px] text-[18px] font-medium text-[#222325]">{seller.vettedForTitle}</h2>
        <div className="mt-[8px] flex flex-wrap gap-x-[14px] gap-y-[8px] pr-[60px] text-[14px]">
          {seller.vettedFor.map((v) => (
            <span key={v} className="flex items-center gap-[5px]">
              <Check size={15} strokeWidth={2.2} className="text-[#222]" />
              {v}
            </span>
          ))}
        </div>
        <div className="mt-[22px] flex items-center gap-[8px] text-[14.5px] font-medium text-[#222325]">
          <Timer size={18} strokeWidth={1.6} className="text-[#95979d]" />
          {seller.hourly}
        </div>
        <h2 className="mt-[34px] text-[18px] font-medium text-[#222325]">{seller.infoTitle}</h2>
        <ReadMore text={seller.bio} more={seller.more} className="mt-[33px] text-[14.5px] leading-[18px]" />
        <div className="mt-[18px] flex gap-[16px] border-t border-[#ececec] pt-[10px]">
          <MapPin size={20} strokeWidth={1.4} className="mt-[8px] text-[#b5b6ba]" />
          <div>
            <div className="text-[13px] text-[#95979d]">{seller.from.label}</div>
            <div className="text-[14.5px] font-medium text-[#222325]">{seller.from.value}</div>
          </div>
        </div>
      </div>
    </AppScreen>
  )
}
