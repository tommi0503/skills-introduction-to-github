import { Search } from 'lucide-react'
import { cn } from '../../../ui'

export interface FilterChipsProps {
  items: string[]
  active: number
  /** Width of each chip (logical px) — measured from the reference. */
  widths: number[]
  className?: string
  style?: React.CSSProperties
}

/** Horizontally scrolling category pills, faded at the right edge, followed by a round search button. */
export function FilterChips({ items, active, widths, className, style }: FilterChipsProps) {
  return (
    <div className={cn('flex items-center', className ?? 'relative')} style={{ height: 34, ...style }}>
      <div className="relative flex overflow-hidden" style={{ gap: 6.5, width: 302 }}>
        {items.map((label, i) => (
          <div
            key={label}
            className="flex shrink-0 items-center justify-center rounded-full"
            style={{
              width: widths[i],
              height: 34,
              fontSize: 15,
              letterSpacing: -0.3,
              background: i === active ? '#2c3138' : '#fff',
              color: i === active ? '#fff' : '#6f6f6f',
              fontWeight: i === active ? 700 : 400,
              border: i === active ? undefined : '1px solid #e3e3e3',
            }}
          >
            {label}
          </div>
        ))}
        <div
          className="pointer-events-none absolute inset-y-0 right-0"
          style={{ width: 26, background: 'linear-gradient(90deg, rgba(255,255,255,0), #fff 85%)' }}
        />
      </div>
      <div
        className="absolute flex items-center justify-center rounded-full"
        style={{ left: 316.7, width: 34, height: 34, border: '1px solid #e3e3e3' }}
      >
        <Search size={18} strokeWidth={2.2} color="#1d1d1d" />
      </div>
    </div>
  )
}
