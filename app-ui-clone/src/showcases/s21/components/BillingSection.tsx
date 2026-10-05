import { ChevronRight } from 'lucide-react'
import type { BillingDay, BillingMonth, CardCharge } from '../data'

function MonthBar({ month, total, tone }: Pick<BillingMonth, 'month' | 'total' | 'tone'>) {
  return (
    <div
      className="flex items-center justify-between"
      style={{ height: 43.5, margin: '0 16.5px', padding: '0 12px', background: '#f6f7f9', borderRadius: 6 }}
    >
      <span style={{ fontSize: 14.5, color: '#8b8b8d', letterSpacing: -0.3 }}>{month}</span>
      <span
        style={{
          fontSize: 15,
          fontWeight: tone === 'accent' ? 500 : 400,
          color: tone === 'accent' ? '#43a356' : '#8b8b8d',
          letterSpacing: -0.3,
        }}
      >
        {total}
      </span>
    </div>
  )
}

function Badge({ text }: { text: string }) {
  return (
    <span
      className="inline-flex items-center justify-center"
      style={{
        marginLeft: 6,
        height: 18,
        padding: '0 3px',
        border: '1px solid #43a356',
        borderRadius: 3,
        color: '#43a356',
        fontSize: 10,
        fontWeight: 600,
      }}
    >
      {text}
    </span>
  )
}

function ChargeRow({ charge }: { charge: CardCharge }) {
  return (
    <div className="flex items-center justify-between" style={{ height: 39 }}>
      <span className="flex items-center" style={{ fontSize: 15.5, color: '#1b1b1d', letterSpacing: -0.4 }}>
        {charge.card}
        {charge.badge && <Badge text={charge.badge} />}
      </span>
      <span className="flex items-center" style={{ fontSize: 16, color: '#1b1b1d', letterSpacing: -0.3, marginRight: -5 }}>
        {charge.amount}
        <ChevronRight size={14} strokeWidth={1.8} style={{ marginLeft: 0 }} />
      </span>
    </div>
  )
}

function DayGroup({ day, gap }: { day: BillingDay; gap: number }) {
  return (
    <div style={{ padding: '0 21px 0 20.5px' }}>
      <div
        className="flex items-center justify-between"
        style={{ height: 38, fontSize: 16.5, fontWeight: 700, color: '#111', letterSpacing: -0.4, marginTop: gap }}
      >
        <span>{day.date}</span>
        <span>{day.total}</span>
      </div>
      {day.charges.map((c) => (
        <ChargeRow key={c.card} charge={c} />
      ))}
    </div>
  )
}

/** A month header bar followed by the per-day charges. */
export function BillingSection({ month, dayGap = 9 }: { month: BillingMonth; dayGap?: number }) {
  return (
    <div>
      <MonthBar month={month.month} total={month.total} tone={month.tone} />
      {month.days.map((d) => (
        <DayGroup key={d.date} day={d} gap={dayGap} />
      ))}
    </div>
  )
}
