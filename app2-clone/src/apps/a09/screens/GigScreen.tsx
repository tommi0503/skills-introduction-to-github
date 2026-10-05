import { ChevronLeft, ChevronUp, Heart, MoreHorizontal } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { gig } from '../data'
import { fv } from '../theme'
import { FvStatusBar } from '../components/FvStatusBar'
import { RoundButton } from '../components/RoundButton'
import { OnlineAvatar } from '../components/OnlineAvatar'
import { ReadMore } from '../components/ReadMore'
import { UnderlineTabs } from '../components/UnderlineTabs'

export function GigScreen() {
  return (
    <AppScreen className="font-figtree">
      <ImagePlaceholder label="gig photo" className="absolute inset-x-0 top-0 h-[327px]" />
      <FvStatusBar color="#fff" />
      <RoundButton icon={ChevronLeft} surface="rgba(255,255,255,0.85)" size={40} iconSize={24} strokeWidth={1.8} className="absolute top-[58px] left-[8px]" />
      <div className="absolute top-[58px] right-[15px] flex gap-[9px]">
        <RoundButton icon={Heart} surface="rgba(255,255,255,0.85)" size={40} iconSize={21} strokeWidth={1.8} />
        <RoundButton icon={MoreHorizontal} surface="rgba(255,255,255,0.85)" size={40} iconSize={20} />
      </div>
      <span className="absolute top-[296px] left-[328px] rounded-full bg-[#2d2d2d]/85 px-[9px] py-[3px] text-[12.5px] text-white">
        {gig.imageCounter}
      </span>

      <div className="absolute inset-x-0 top-[327px] flex h-[70px] items-center border-b border-[#ececec] bg-[#fafafa] pr-[18px] pl-[17px]">
        <OnlineAvatar size={38} dot={5} />
        <span className="ml-[14px] text-[15px] font-medium text-[#222325]">{gig.seller}</span>
        <ChevronUp size={20} strokeWidth={1.8} className="ml-auto text-[#b5b6ba]" />
      </div>

      <div className="absolute inset-x-0 top-[411px] px-[22px]">
        <h1 className="text-[26px] leading-[32px] font-semibold tracking-[-0.2px] text-[#222325]">{gig.title}</h1>
        <ReadMore text={gig.description} more={gig.more} className="mt-[17px] text-[14.5px] leading-[19px] tracking-[0.2px] text-[#404145]" />
      </div>
      <div className="absolute inset-x-0 top-[577px] h-px bg-[#f0f0f0]" />
      <div className="absolute inset-x-[15px] top-[580px] border-b-2 border-[#ececec]">
        <UnderlineTabs
          items={gig.packages}
          active={gig.activePackage}
          equal
          className="h-[50px]"
          itemClassName="text-[18px]"
          barDrop={2}
        />
      </div>
      <div className="absolute inset-x-0 top-[644px] pr-[18px] pl-[20px] text-[#404145]">
        <h3 className="text-[15px] font-semibold text-[#222325]">{gig.packageName}</h3>
        <p className="mt-[14px] text-[15px] leading-[19px]">{gig.packageText}</p>
        {gig.facts.map((f) => (
          <div key={f.label} className="flex h-[46.5px] items-center justify-between text-[14px] first:mt-0">
            <span>{f.label}</span>
            {f.value && <span className="text-[15px] font-semibold text-[#222325]">{f.value}</span>}
          </div>
        ))}
      </div>
      <div
        className="absolute top-[766px] left-[276px] flex h-[46px] w-[97px] items-center gap-[11px] rounded-full bg-white pl-[6px] text-[16px] font-semibold text-[#222325]"
        style={{ boxShadow: fv.halo }}
      >
        <OnlineAvatar size={34} dot={4} />
        {gig.chat}
      </div>
    </AppScreen>
  )
}
