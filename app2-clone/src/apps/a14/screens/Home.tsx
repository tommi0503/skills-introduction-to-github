import { ChevronRight, Ellipsis, House, Maximize2, X } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { Flag } from '../components/Flag'
import { NavBar } from '../components/NavBar'
import { SearchPill } from '../components/SearchPill'
import { StatusRow } from '../components/StatusRow'
import { home as d, navDots, navTabs, type Recent } from '../data'
import { nord } from '../theme'

function ConnectionCard() {
  return (
    <div className="absolute top-[137px] left-[16px] h-[333px] w-[356px] overflow-hidden rounded-[16px] border-[2px] border-[#5a6ce8] bg-white">
      <ImagePlaceholder label="map" tone="#edf0f7" className="absolute inset-0" />
      <span className="absolute top-[14px] right-[14px] flex h-[37px] w-[37px] items-center justify-center rounded-full border border-[#d8d8dc] bg-white">
        <Maximize2 size={17} strokeWidth={1.6} />
      </span>
      <span className="absolute top-[162px] left-[173px] h-[8px] w-[8px] rounded-full" style={{ background: nord.dot }} />
      <div className="absolute top-[201px] left-[14px] flex items-center">
        <span className="rounded-full border-[2px] border-[#1d5a46] bg-white p-[2px]">
          <Flag size={42} />
        </span>
        <div className="ml-[12px]">
          <div className="text-[20px] leading-[24px] font-semibold">{d.city}</div>
          <div className="text-[15px] leading-[22px]" style={{ color: nord.secured }}>
            {d.status}
          </div>
        </div>
      </div>
      <div className="absolute top-[268px] left-[14px] flex h-[46px] w-[266px] items-center justify-center rounded-full border border-[#cfcfd4] text-[15px] font-medium">
        {d.pause}
      </div>
      <span className="absolute top-[269px] left-[291px] flex h-[47px] w-[47px] items-center justify-center rounded-full border border-[#cfcfd4]">
        <Ellipsis size={18} strokeWidth={1.6} />
      </span>
    </div>
  )
}

function PromoCard() {
  return (
    <div className="absolute top-[495px] left-[16px] flex h-[73px] w-[356px] items-center rounded-[16px] bg-white pr-[20px] pl-[15px]">
      <span className="flex h-[44px] w-[44px] items-center justify-center rounded-[12px] bg-[#f3f3f5] shadow-[0_1px_3px_rgba(0,0,0,0.12)]">
        <House size={20} strokeWidth={1.6} className="text-[#3aa76d]" />
      </span>
      <div className="ml-[8px] flex-1">
        <div className="text-[15.5px] leading-[20px]">{d.promo.title}</div>
        <div className="mt-[2px] text-[11.5px] text-[#77777b]">{d.promo.body}</div>
      </div>
      <X size={17} strokeWidth={1.4} className="text-[#8a8a8f]" />
    </div>
  )
}

function RecentCard({ r }: { r: Recent }) {
  return (
    <div className="h-[93px] w-[142px] shrink-0 rounded-[14px] bg-white pt-[12px] pl-[15px]">
      <Flag size={24} />
      <div className="mt-[5px] text-[14.5px] leading-[18px]">
        {r.lines.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </div>
      {r.sub && <div className="text-[12.5px] leading-[17px] text-[#8a8a8f]">{r.sub}</div>}
    </div>
  )
}

export function Home() {
  return (
    <AppScreen className="font-inter" background={nord.bgHome} style={{ color: nord.ink }}>
      <StatusRow />
      <SearchPill label={d.search} className="top-[66px] left-[16px] w-[356px]" />
      <ConnectionCard />
      <PromoCard />
      <div className="absolute top-[600px] left-[32px] text-[13.5px] text-[#77777b]">{d.recentsTitle}</div>
      <div className="absolute top-[600px] right-[38px] flex items-center gap-[12px] text-[14px] text-[#333]">
        {d.allLocations}
        <ChevronRight size={15} strokeWidth={1.6} />
      </div>
      <div className="absolute top-[632px] left-[16px] flex gap-[8px]">
        {d.recents.map((r) => (
          <RecentCard key={r.key} r={r} />
        ))}
      </div>
      <NavBar tabs={navTabs} activeKey="globe" dots={navDots} top={761} className="bg-white" />
    </AppScreen>
  )
}
