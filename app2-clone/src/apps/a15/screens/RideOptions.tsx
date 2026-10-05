import { ArrowRight, CalendarDays, ChevronLeft, ChevronRight, Info, Leaf, Plus, UserRound } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { BottomSheet } from '../components/BottomSheet'
import { RoutePath } from '../components/RoutePath'
import { StatusRow } from '../components/StatusRow'
import { rides as d } from '../data'
import { fonts, lyft } from '../theme'

function LocationsHeader() {
  return (
    <div className="absolute top-[66px] left-[8px] w-[372px] overflow-hidden rounded-[8px] shadow-[0_2px_8px_rgba(0,0,0,0.15)]">
      <div className="relative flex h-[44px] items-center justify-center gap-[10px] bg-white">
        <ChevronLeft size={22} strokeWidth={1.8} className="absolute left-[16px]" />
        <ImagePlaceholder label="origin" tone="#cfcfd2" className="h-[16px] w-[82px]" />
        <ArrowRight size={16} strokeWidth={1.6} className="text-[#77727a]" />
        <ImagePlaceholder label="destination" tone="#cfcfd2" className="h-[13px] w-[90px]" />
      </div>
      <div className="flex h-[26px] items-center justify-center text-[13.5px] text-white" style={{ background: lyft.tapBar }}>
        {d.tapToEdit}
      </div>
    </div>
  )
}

function OptionCard() {
  const o = d.option
  return (
    <div className="absolute top-[562px] left-[16px] h-[125px] w-[357px] rounded-[16px] border-[2px] bg-white" style={{ borderColor: lyft.border }}>
      <ImagePlaceholder label="Standard car" className="absolute top-[28px] left-[14px] h-[63px] w-[150px] rounded-[6px]" />
      <div className="absolute top-[9px] right-[14px] flex flex-col items-end">
        <div className="flex items-center gap-[3px] text-[16px] leading-[24px] font-semibold">
          {o.name}
          <UserRound size={13} strokeWidth={0} fill="#5f5a60" className="ml-[3px]" />
          <span className="text-[13px] font-normal text-[#5f5a60]">{o.seats}</span>
        </div>
        <div className="mt-[4px] text-[16px] leading-[22px] font-bold" style={{ color: lyft.green }}>
          {o.price}
        </div>
        <div className="mt-[1px] flex items-center gap-[8px]">
          <span className="flex h-[25px] items-center gap-[4px] rounded-[3px] px-[5px] text-[14px]" style={{ background: lyft.greenSoft, color: lyft.green }}>
            <Leaf size={13} strokeWidth={0} fill="#3f8a5d" />
            {o.discount}
          </span>
          <s className="text-[14px] text-[#77727a]">{o.was}</s>
        </div>
        <div className="mt-[7px] text-[14px]">{o.eta}</div>
      </div>
    </div>
  )
}

function CheckoutPanel() {
  return (
    <div className="absolute top-[697px] left-[16px] h-[127px] w-[357px] rounded-[26px] bg-white shadow-[0_0_10px_rgba(0,0,0,0.12)]">
      <div className="absolute top-[18px] left-[17px] flex items-center text-[14px]">
        <ImagePlaceholder label="Lyft Cash" tone="#c9dccf" className="h-[13px] w-[20px] rounded-[2px]" />
        <span className="ml-[6px]">{d.cash.replace(' + Promo', '')}</span>
        <Plus size={13} strokeWidth={1.8} className="mx-[3px]" />
        <span>Promo</span>
        <ChevronRight size={16} strokeWidth={1.6} className="ml-[12px]" />
      </div>
      <div className="absolute top-[16px] right-[16px] flex items-center gap-[10px] text-[14px]">
        <CalendarDays size={20} strokeWidth={1.4} />
        {d.schedule}
      </div>
      <button
        className="absolute top-[55px] left-[16px] h-[55px] w-[325px] rounded-full text-[18px] font-semibold text-white"
        style={{ background: lyft.purple }}
      >
        {d.cta}
      </button>
    </div>
  )
}

export function RideOptions() {
  const end = d.route[d.route.length - 1]
  return (
    <AppScreen className={fonts.body} style={{ color: lyft.ink }}>
      <ImagePlaceholder label="map of Chicago" className="absolute inset-x-0 top-0 h-[500px]" />
      <RoutePath points={d.route} color={lyft.purple} width={3.5} />
      <span className="absolute top-[145px] left-[165px] h-[12px] w-[12px] rounded-full border-[3px] bg-white" style={{ borderColor: lyft.purple }} />
      <span
        className="absolute h-[16px] w-[16px] rounded-full border-[4px] bg-white"
        style={{ left: end[0] - 8, top: end[1] - 8, borderColor: lyft.magenta }}
      />
      <div className="absolute top-[411px] left-[229px] flex h-[29px] items-center rounded-[14px] bg-white px-[8px] text-[14px] font-medium shadow-[0_1px_4px_rgba(0,0,0,0.15)]">
        {d.arrive}
      </div>
      <StatusRow />
      <LocationsHeader />
      <BottomSheet top={481} grabber>
        <div className="absolute top-[36px] inset-x-0 flex items-center justify-center gap-[7px] text-[13.5px] font-semibold">
          <Leaf size={15} strokeWidth={0} fill="#2f7a4c" />
          {d.saving}
          <Info size={15} strokeWidth={1.6} className="ml-[2px]" />
        </div>
      </BottomSheet>
      <OptionCard />
      <CheckoutPanel />
    </AppScreen>
  )
}
