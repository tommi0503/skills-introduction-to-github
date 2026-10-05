import { Handbag } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { CuTabBar } from '../components/CuTabBar'
import { HighlightStatusBar } from '../components/HighlightStatusBar'
import { NavBar } from '../components/Primitives'
import { cuTabsSpaced, keeping, keepingInfo, type InfoRow } from '../data'
import { cu } from '../theme'

function InfoRowView({ row }: { row: InfoRow }) {
  const Icon = row.icon
  return (
    <div className="flex text-[14.5px] leading-[21px] text-[#333]">
      <span className="flex w-[87.6px] shrink-0 items-start font-bold">
        <Icon size={14} strokeWidth={1.5} className="mt-[3.5px] mr-[5px] text-[#666]" />
        {row.label}
      </span>
      <span>
        {row.lines.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </span>
    </div>
  )
}

function Barcode() {
  return (
    <div className="flex flex-col items-center">
      <ImagePlaceholder label="barcode" className="h-[59px] w-[199px]" />
      <div className="mt-[2px] flex items-center gap-[3px] text-[14px] leading-[16px] font-medium text-[#222]">
        {keeping.barcode.first}
        <ImagePlaceholder label="hidden barcode digits" className="h-[14px] w-[83px]" />
        {keeping.barcode.last}
      </div>
    </div>
  )
}

export function KeepingScreen() {
  return (
    <div className="relative h-full overflow-hidden font-pretendard" style={{ background: '#f8f8f8' }}>
      <div className="absolute inset-x-0 top-0 h-[115px] bg-white" />
      <HighlightStatusBar />
      <NavBar title={keeping.title} actions={[Handbag]} />

      <div className="absolute rounded-[20px] bg-white" style={{ left: 16.4, right: 17, top: 133, height: 390 }}>
        <div className="mx-auto mt-[22.6px] flex h-[162px] w-[162px] items-center justify-center rounded-[16px] border border-[#e8e8e8]">
          <ImagePlaceholder label="product bottle" className="h-[128px] w-[38px] rounded-[6px]" />
        </div>
        <div className="mt-[14px] flex items-center justify-center gap-[7px]">
          <span className="text-[18.5px] font-bold text-[#222]" style={{ letterSpacing: -0.3 }}>
            {keeping.item}
          </span>
          <span className="flex h-[23.5px] items-center rounded-full bg-[#eeeeee] px-[7px] text-[10.5px] text-[#777]">{keeping.badge}</span>
        </div>
        <p className="mt-[1px] text-center text-[14px] leading-[20px] text-[#333]">
          {keeping.until}
          <span className="ml-[6px] font-semibold" style={{ color: cu.pink }}>
            {keeping.remaining}
          </span>
        </p>
        <p className="text-center text-[14px] leading-[20px] text-[#888]">{keeping.since}</p>
        <div className="mx-[43.6px] mt-[13px] h-px bg-[#efefef]" />
        <div className="mt-[15px]">
          <Barcode />
        </div>
      </div>

      <div className="absolute flex flex-col gap-[10px]" style={{ left: 16.4, top: 562 }}>
        {keepingInfo.map((r) => (
          <InfoRowView key={r.label} row={r} />
        ))}
      </div>

      <CuTabBar tabs={cuTabsSpaced} active="my" />
    </div>
  )
}
