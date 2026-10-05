import { ArrowUp, CalendarDays, Clock, Search } from 'lucide-react'
import { cn } from '../../../ui'
import { AreaChart } from '../components/AreaChart'
import { BigAmount } from '../components/BigAmount'
import { InvestPhone } from '../components/InvestPhone'
import { Pill } from '../components/Pill'
import { ScreenHeader } from '../components/ScreenHeader'
import { TransactionRow } from '../components/TransactionRow'
import { chartGrid, chartLayers, portfolio } from '../data'
import { theme } from '../theme'

/** Asset detail: balance, range chips, area chart and latest transaction. */
export function PortfolioScreen() {
  const p = portfolio
  return (
    <InvestPhone background={theme.portfolioScreen}>
      <ScreenHeader title={p.title} />
      <BigAmount value={p.amount} className="absolute inset-x-0 top-[160px]" />
      <div className="absolute inset-x-0 top-[259px] flex items-center justify-center gap-[5px] text-[14px]">
        <ArrowUp size={15} strokeWidth={2.2} style={{ color: theme.positive }} />
        <span className="text-[15px] font-semibold">{p.change}</span>
        <span className="text-[#5d5d62]">{p.changeCaption}</span>
      </div>

      <div className="absolute left-[20px] top-[307px] flex items-center gap-[5px]">
        {p.ranges.map((r) => (
          <Pill key={r} active={r === p.activeRange} className="h-[47px] w-[56px] text-[13.5px]">
            {r}
          </Pill>
        ))}
      </div>
      <div className="absolute left-[283px] top-[307px] flex h-[47px] w-[91px] items-center rounded-full" style={{ background: theme.translucent }}>
        <span className="flex h-[47px] w-[47px] items-center justify-center rounded-full bg-[#1c1c1e] text-white">
          <CalendarDays size={18} strokeWidth={1.8} />
        </span>
        <Clock size={18} strokeWidth={1.8} className="ml-[12px] text-[#3a3a3c]" />
      </div>

      <AreaChart layers={chartLayers} grid={chartGrid} fill={theme.chartFill} width={393} height={560} />
      <span className="absolute left-[253px] top-[391px] flex h-[28px] w-[72px] items-center justify-center rounded-full bg-[#141414] text-[11px] font-semibold text-white">
        {p.tooltip}
      </span>

      <div className="absolute left-[0px] right-[0px] top-[576px] grid grid-cols-6 text-center text-[14px] text-[#48484d]">
        {p.months.map((m) => (
          <span key={m} className={cn(m === p.activeMonth && 'font-bold text-[#5c4f00]')}>
            {m}
          </span>
        ))}
      </div>

      <div className="absolute inset-x-[20px] top-[640px] flex items-center justify-between">
        <span className="text-[31.5px] font-bold tracking-[-0.6px]">{p.sectionTitle}</span>
        <Search size={21} strokeWidth={2} className="mr-[6px]" />
      </div>
      <div className="absolute inset-x-[20px] top-[703px] flex gap-[7px]">
        {p.filters.map((f) => (
          <Pill key={f} active={f === p.activeFilter} className="h-[47px] flex-1 text-[14.5px] font-medium">
            {f}
          </Pill>
        ))}
      </div>
      <div className="absolute inset-x-[20px] top-[773px]">
        <TransactionRow tx={p.transaction} />
      </div>
    </InvestPhone>
  )
}
