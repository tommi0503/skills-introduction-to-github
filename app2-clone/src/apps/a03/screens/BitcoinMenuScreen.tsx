import { Settings, SquareArrowOutUpRight } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { ActionMenu } from '../components/ActionMenu'
import { AssetHeader } from '../components/AssetHeader'
import { FloatingNav } from '../components/FloatingNav'
import { LineChart } from '../components/LineChart'
import { RangeSelector } from '../components/RangeSelector'
import { bitcoin } from '../data'
import { bitcoinMenuSeries, bitcoinSeries } from '../series'
import { theme } from '../theme'

/** Left part of the line (under the menu) reuses the detail series, shifted to this quote's level. */
const series: [number, number][] = [
  ...bitcoinSeries.filter(([x]) => x < 205).map(([x, y]): [number, number] => [x, y - 20]),
  ...bitcoinMenuSeries,
]

export function BitcoinMenuScreen() {
  const b = bitcoin
  return (
    <AppScreen className="font-inter">
      <AssetHeader ticker={b.ticker} name={b.name} quote={b.quotes.menu} starred />
      <LineChart points={series} baselineY={470} color={theme.green} />
      <RangeSelector ranges={b.ranges} active="24H" top={536} trailing={[Settings, SquareArrowOutUpRight]} fadedFrom={7} />
      <div className="absolute flex items-center justify-between" style={{ left: 15, right: 15, top: 623 }}>
        <span className="text-[19px] font-semibold">{b.position.title}</span>
        <span className="text-[14px] text-[#8a8a8f]">{b.position.action}</span>
      </div>
      {b.position.rows.map((r, i) => (
        <div key={r.key} className="absolute flex justify-between text-[14.5px]" style={{ left: 15, right: 15, top: 664 + i * 33 }}>
          <span className="text-[#8a8a8f]">{r.label}</span>
          <span style={{ color: r.negative ? theme.red : '#111' }}>{r.value}</span>
        </div>
      ))}
      <ActionMenu groups={b.menu.groups} buy={b.menu.buy} sell={b.menu.sell} top={420} />
      <FloatingNav active="portfolio" />
    </AppScreen>
  )
}
