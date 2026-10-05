import type { LucideIcon } from 'lucide-react'
import { theme } from '../theme'

export interface RangeSelectorProps {
  ranges: string[]
  active: string
  top: number
  trailing: LucideIcon[]
  /** Ranges rendered faded because they slide under the trailing icons. */
  fadedFrom?: number
}

/** Chart time-range chips with trailing tool icons. */
export function RangeSelector({ ranges, active, top, trailing, fadedFrom }: RangeSelectorProps) {
  return (
    <div className="absolute flex items-center" style={{ left: 15, right: 15, top, height: 30 }}>
      <div className="flex flex-1 items-center gap-[19px] overflow-hidden">
        {ranges.map((r, i) => {
          const on = r === active
          return (
            <span
              key={r}
              className="flex h-[30px] items-center justify-center rounded-[5px] text-[12.5px] font-medium"
              style={{
                minWidth: on ? 31 : undefined,
                padding: on ? '0 9px' : undefined,
                marginRight: on ? -6 : undefined,
                background: on ? theme.greenSoft : undefined,
                boxShadow: on ? `inset 0 0 0 1px ${theme.greenBorder}` : undefined,
                color: on ? theme.green : '#8e8e93',
                opacity: fadedFrom !== undefined && i >= fadedFrom ? 0.35 : 1,
              }}
            >
              {r}
            </span>
          )
        })}
      </div>
      <div className="flex items-center gap-[12px] text-[#444]">
        {trailing.map((Icon, i) => (
          <Icon key={i} size={18} strokeWidth={2} />
        ))}
      </div>
    </div>
  )
}
