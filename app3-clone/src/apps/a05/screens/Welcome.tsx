import { ChevronDown, Search, UserRoundSearch } from 'lucide-react'
import { AppScreen, ImagePlaceholder, StatusBar } from '../../../ui'
import { BlockButton } from '../components/BlockButton'
import { OrDivider } from '../components/OrDivider'
import { welcome } from '../data'
import { ue } from '../theme'

export function Welcome() {
  return (
    <AppScreen className="font-inter" background="#fff">
      <StatusBar />
      <ImagePlaceholder className="absolute top-[52px] left-0 h-[253px] w-full" label="food illustration" />
      <div className="absolute inset-x-[17px] top-[323px]">
        <h1 className="text-[20.5px] leading-[28px] font-semibold tracking-[-0.2px]">{welcome.title}</h1>
        <div className="mt-[18px] flex h-[47px] gap-[8px]">
          <div className="flex w-[103px] items-center justify-center gap-[20px] rounded-[8px]" style={{ background: ue.field }}>
            <ImagePlaceholder className="h-[19px] w-[29px] rounded-[2px]" label="US flag" />
            <ChevronDown size={14} strokeWidth={3} fill="currentColor" />
          </div>
          <div className="flex flex-1 items-center rounded-[8px] pr-[14px] pl-[16px] text-[15px]" style={{ background: ue.field }}>
            <span className="font-medium">{welcome.phonePrefix}</span>
            <span className="ml-[5px] flex-1" style={{ color: ue.muted }}>
              {welcome.phonePlaceholder}
            </span>
            <UserRoundSearch size={21} strokeWidth={1.7} />
          </div>
        </div>
        <BlockButton className="mt-[17px] h-[47px]">{welcome.cta}</BlockButton>
        <OrDivider label={welcome.or} className="mt-[18px]" />
        <div className="mt-[11px] flex flex-col gap-[9px]">
          {welcome.options.map((o) => {
            const Icon = o.icon
            const leading = o.brand ? (
              <ImagePlaceholder className="h-[18px] w-[18px] rounded-full" tone="#d1d5db" label={`${o.key} logo`} />
            ) : (
              Icon && <Icon size={19} strokeWidth={1.8} />
            )
            return (
              <BlockButton key={o.key} variant="secondary" className="h-[47px]" leading={leading}>
                {o.label}
              </BlockButton>
            )
          })}
        </div>
        <div className="mt-[22px] text-center text-[15px] font-medium">{welcome.more}</div>
        <OrDivider label={welcome.or} className="mt-[33px]" />
        <div className="mt-[22px] flex items-center justify-center gap-[9px] text-[15px] font-medium">
          <Search size={18} strokeWidth={2} />
          {welcome.find}
        </div>
      </div>
    </AppScreen>
  )
}
