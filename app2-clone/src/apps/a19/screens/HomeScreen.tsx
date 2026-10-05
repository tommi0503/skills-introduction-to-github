import { Bell, ChevronDown, ChevronRight, Gift, Info, Loader } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { FiStatusBar } from '../components/FiStatusBar'
import { DeviceStatusRow } from '../components/DeviceStatusRow'
import { PetMarker } from '../components/PetMarker'
import { CircleIcon } from '../components/CircleIcon'
import { FiTabBar } from '../components/FiTabBar'
import { Illustration, MiniBars, SectionHeader, SummaryCard } from '../components/HomeCards'
import { home, homeStatus, pet, tabs } from '../data'
import { fi } from '../theme'

export function HomeScreen() {
  return (
    <AppScreen background={`linear-gradient(#fff 0, #fff 120px, ${fi.surface} 380px)`}>
      <FiStatusBar />
      {/* header */}
      <div className="absolute left-[20px] top-[56px] flex items-center">
        <span className="text-[29px] font-semibold tracking-[-0.6px] text-black">{pet.name}</span>
        <ChevronDown size={16} strokeWidth={2.4} className="ml-[3px] mt-[4px]" />
      </div>
      <div className="absolute left-[20px] top-[97px] text-[11.5px] font-medium tracking-[0.7px]" style={{ color: fi.grey }}>
        {pet.breed}
      </div>
      <Gift size={21} strokeWidth={2} className="absolute left-[299px] top-[66px]" fill="#000" stroke="#000" />
      <Bell size={21} strokeWidth={2} className="absolute left-[340px] top-[65px]" fill="#000" />

      {/* map card */}
      <div className="absolute left-[16px] top-[134px] h-[229px] w-[357px] overflow-hidden rounded-[14px]">
        <ImagePlaceholder className="h-full w-full" label="map" />
        <DeviceStatusRow status={homeStatus} className="absolute left-[16px] top-[18px]" />
        <CircleIcon icon={Loader} size={29} iconSize={19} strokeWidth={2.2} className="absolute left-[311px] top-[19px]" />
        <PetMarker className="absolute left-[153px] top-[76px]" size={53} />
        <div className="absolute left-[68px] top-[167px] flex h-[42px] items-center rounded-full bg-white/80 pl-[15px] pr-[13px] text-[15px] font-medium text-black">
          {home.place} <span className="ml-[4px]">›</span>
        </div>
      </div>

      {/* today */}
      <SectionHeader
        className="absolute left-[24px] right-[18px] top-[389px]"
        title={home.todayLabel}
        right={<span className="text-[14.5px]" style={{ color: fi.grey }}>{home.todayDate}</span>}
      />
      <SummaryCard title={home.rest.title} className="absolute left-[16px] top-[427px] h-[134px] w-[170px]">
        <div className="mt-[14px] pl-[16px] text-[13px] leading-[17px]" style={{ color: fi.grey }}>
          {home.rest.lines.map((l) => (
            <div key={l}>{l}</div>
          ))}
        </div>
        <Illustration className="absolute bottom-0 left-[19px] h-[33px] w-[132px] rounded-t-[30px]" label="clouds and moon" />
      </SummaryCard>
      <SummaryCard title={home.activity.title} className="absolute left-[203px] top-[427px] h-[134px] w-[170px]">
        <div className="mt-[13px] pl-[16px] text-[11.5px] font-medium tracking-[0.3px]" style={{ color: fi.grey }}>
          {home.activity.caption}
        </div>
        <div className="pl-[15px] text-[24px] font-medium leading-[30px]" style={{ color: fi.green }}>
          {home.activity.value}
        </div>
        <MiniBars bars={home.activityBars} className="absolute bottom-0 left-[45px]" />
      </SummaryCard>

      {/* last time outside */}
      <SectionHeader
        className="absolute left-[24px] right-[32px] top-[591px]"
        title={
          <span className="flex items-center gap-[5px]">
            {home.outsideTitle}
            <Info size={17} strokeWidth={2.5} fill="#000" stroke="#fff" />
          </span>
        }
        right={
          <span className="flex items-center text-[14px] font-semibold text-black">
            {home.outsideLink}
            <ChevronRight size={16} strokeWidth={2.6} className="ml-[2px]" />
          </span>
        }
      />
      <div className="absolute left-[16px] top-[629px] h-[160px] w-[357px] rounded-[12px] bg-white">
        <div className="absolute left-[17px] top-[49px] text-[15px] leading-[23px] tracking-[0.1px]" style={{ color: fi.grey }}>
          {home.outsideText.map((l) => (
            <div key={l}>{l}</div>
          ))}
        </div>
        <Illustration className="absolute left-[252px] top-[30px] h-[80px] w-[94px] rounded-[6px]" label="trees" />
      </div>

      <FiTabBar items={tabs} active="live" className="top-[760px] shadow-[0_-1px_0_rgba(0,0,0,0.04)]" />
    </AppScreen>
  )
}
