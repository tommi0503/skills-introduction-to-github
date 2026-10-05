import { ChevronLeft, ChevronRight } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { BottomSheet } from '../components/BottomSheet'
import { StatusRow } from '../components/StatusRow'
import { upsell as d } from '../data'
import { fonts, lyft } from '../theme'

function PickupPin() {
  return (
    <div className="absolute top-[253px] left-[178px] flex flex-col items-center">
      <span className="h-[30px] w-[30px] rounded-full border-[9px] bg-white" style={{ borderColor: lyft.purple }} />
      <span className="h-[12px] w-[3px]" style={{ background: lyft.purple }} />
      <ChevronLeft size={12} strokeWidth={2} className="absolute top-[30px] -left-[13px] text-[#4a444b]" />
      <ChevronRight size={12} strokeWidth={2} className="absolute top-[30px] -right-[13px] text-[#4a444b]" />
      <span className="h-[100px] w-[3px] bg-[#b88fd0]" />
    </div>
  )
}

export function Upsell() {
  return (
    <AppScreen className={fonts.body} style={{ color: lyft.ink }}>
      <ImagePlaceholder label="map" tone="#b8b4b7" className="absolute inset-x-0 top-0 h-[420px]" />
      <PickupPin />
      <StatusRow />
      <span className="absolute top-[67px] left-[7px] flex h-[39px] w-[39px] items-center justify-center rounded-[8px] bg-[#dcdadb]">
        <ChevronLeft size={22} strokeWidth={1.6} />
      </span>
      <BottomSheet top={399}>
        <ImagePlaceholder label="Lyft Black car" className="absolute top-[13px] left-[63px] h-[116px] w-[262px] rounded-[10px]" />
        <h2 className="absolute inset-x-0 top-[146px] text-center text-[21px] font-bold">{d.title}</h2>
        <div className="absolute inset-x-0 top-[183px] text-center text-[16.5px] leading-[23.5px] text-[#2e282f]">
          {d.body.map((l) => (
            <div key={l}>{l}</div>
          ))}
        </div>
        <button
          className="absolute top-[295px] left-[46px] h-[47px] w-[294px] rounded-full text-[16.5px] font-semibold text-white"
          style={{ background: lyft.purple }}
        >
          {d.primary}
        </button>
        <div className="absolute top-[351px] left-[46px] h-[47px] w-[294px] overflow-hidden rounded-full bg-[#f0eeef]">
          <div className="absolute inset-y-0 left-0 bg-[#9b9597]" style={{ width: `${d.progress * 100}%` }} />
          <div className="relative flex h-full items-center justify-center text-[16.5px] font-semibold">{d.secondary}</div>
        </div>
      </BottomSheet>
    </AppScreen>
  )
}
