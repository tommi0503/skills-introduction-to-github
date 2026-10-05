import { ChevronRight, Menu, PictureInPicture2, Settings, SquareArrowOutUpRight, Sun, X } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { ChangeLine } from '../components/ChangeLine'
import { FloatingNav } from '../components/FloatingNav'
import { FloatingPill } from '../components/FloatingPill'
import { LineChart } from '../components/LineChart'
import { RangeSelector } from '../components/RangeSelector'
import { TopBar } from '../components/TopBar'
import { portfolio } from '../data'
import { portfolioSeries } from '../series'
import { theme } from '../theme'

export function PortfolioScreen() {
  const p = portfolio
  return (
    <AppScreen className="font-inter">
      <FloatingPill left={15} top={59} height={42} width={130} className="justify-start gap-[10px] pl-[18px] text-[15px] font-medium">
        <Menu size={18} strokeWidth={2} />
        {p.account}
      </FloatingPill>
      <FloatingPill right={17} top={59} height={44} width={44} className="justify-center">
        <Sun size={17} strokeWidth={2.2} />
      </FloatingPill>
      <TopBar />
      <div className="absolute text-[29px] font-semibold tracking-[-0.4px]" style={{ left: 15, top: 129 }}>
        {p.value}
      </div>
      <div className="absolute inset-x-[10px] flex border-b border-[#e9e9eb] text-[15px]" style={{ top: 189, height: 31 }}>
        {p.tabs.map((t, i) => (
          <span
            key={t}
            className="relative px-[5px] pr-[15px]"
            style={{ color: i === 0 ? theme.ink : '#77777c', fontWeight: i === 0 ? 500 : 400 }}
          >
            {t}
            {i === 0 && <span className="absolute -bottom-px left-0 right-[10px] h-[2px] bg-[#333]" />}
          </span>
        ))}
      </div>
      <ChangeLine value={p.change} top={247} info />
      <LineChart points={portfolioSeries} baselineY={437} color={theme.green} endDot strokeWidth={1.4} />
      <RangeSelector ranges={p.ranges} active="1D" top={514} trailing={[Settings, PictureInPicture2, SquareArrowOutUpRight]} />
      <div className="absolute inset-x-[15px] border-y border-[#e6e6e8]" style={{ top: 567, height: 51 }}>
        <div className="flex h-full items-center justify-between text-[14.5px]">
          <span>{p.marginLabel}</span>
          <span className="flex items-center gap-[8px] font-semibold">
            {p.marginValue}
            <ChevronRight size={18} strokeWidth={2} />
          </span>
        </div>
      </div>
      <div className="absolute overflow-hidden rounded-[10px]" style={{ left: 15, right: 18, top: 642, height: 105 }}>
        <ImagePlaceholder tone="#151a33" className="absolute inset-0" label="promo gradient" />
        <div className="absolute inset-0 px-[12px] pt-[11px] text-white">
          <div className="text-[14.5px] font-semibold">{p.promo.title}</div>
          <p className="mt-[3px] text-[12px] leading-[14.5px] text-[#c9cad3]">{p.promo.body}</p>
          <div className="mt-[11px] flex items-center gap-[5px] text-[14.5px] font-semibold">
            {p.promo.cta}
            <ChevronRight size={15} strokeWidth={2.2} />
          </div>
        </div>
        <X size={12} strokeWidth={2} className="absolute top-[16px] right-[13px] text-[#9a9aa6]" />
      </div>
      <div className="absolute flex gap-[9.5px]" style={{ left: 129, top: 756 }}>
        {Array.from({ length: p.pages }, (_, i) => (
          <span key={i} className="h-[7.5px] w-[7.5px] rounded-full" style={{ background: i === 0 ? '#333' : '#d4d4d8' }} />
        ))}
      </div>
      <div className="absolute flex items-center justify-between text-[#c7c7cc]" style={{ left: 15, right: 15, top: 815 }}>
        <span className="text-[19px] font-semibold">{p.behindTitle}</span>
        <span className="text-[13px]">{p.behindAction}</span>
      </div>
      <FloatingNav active="portfolio" />
    </AppScreen>
  )
}
