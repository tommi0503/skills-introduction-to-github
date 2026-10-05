import { ChevronRight, Info, Settings, SquareArrowOutUpRight, Zap } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { AssetHeader } from '../components/AssetHeader'
import { FloatingNav } from '../components/FloatingNav'
import { LineChart } from '../components/LineChart'
import { RangeSelector } from '../components/RangeSelector'
import { bitcoin } from '../data'
import { bitcoinSeries } from '../series'
import { theme } from '../theme'

export function BitcoinScreen() {
  const b = bitcoin
  return (
    <AppScreen className="font-inter">
      <AssetHeader ticker={b.ticker} name={b.name} quote={b.quotes.detail} />
      <LineChart points={bitcoinSeries} baselineY={451} color={theme.green} />
      <RangeSelector ranges={b.ranges} active="24H" top={536} trailing={[Settings, SquareArrowOutUpRight]} fadedFrom={7} />
      <div className="absolute flex items-center gap-[6px] text-[19px] font-semibold" style={{ left: 15, top: 623 }}>
        {b.about}
        <Info size={13} strokeWidth={1.6} color="#9a9aa0" />
      </div>
      <div className="absolute overflow-hidden rounded-[10px]" style={{ left: 15, right: 18, top: 665, height: 200 }}>
        <ImagePlaceholder tone="#c4c6cc" className="absolute inset-0" label="bitcoin coin artwork" />
      </div>
      <div className="absolute flex flex-col justify-center rounded-full bg-white/75 pl-[15px] backdrop-blur" style={{ left: 22, top: 688, width: 131, height: 65 }}>
        <span className="text-[12px] text-[#77777d]">{b.buyingPowerLabel}</span>
        <span className="mt-[3px] text-[15px] font-semibold">{b.buyingPower}</span>
      </div>
      <span className="absolute flex h-[48px] w-[48px] items-center justify-center rounded-full bg-[#1c1c1e] text-white" style={{ left: 224, top: 705 }}>
        <Zap size={17} strokeWidth={2} fill="#fff" />
      </span>
      <span className="absolute flex items-center justify-center rounded-full bg-[#1c1c1e] text-[15px] font-semibold text-white" style={{ left: 285, top: 705, width: 81, height: 48 }}>
        {b.trade}
      </span>
      <div className="absolute flex items-center gap-[4px] text-[13px] font-medium text-white/80" style={{ left: 40, top: 826 }}>
        {b.explore}
        <ChevronRight size={13} strokeWidth={2.2} />
      </div>
      <FloatingNav active="portfolio" />
    </AppScreen>
  )
}
