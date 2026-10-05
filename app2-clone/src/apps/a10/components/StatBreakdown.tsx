import type { Stat } from '../data'

export interface StatBreakdownProps {
  stats: Stat[]
  /** widths of all but the last column (last one takes the rest) */
  columnWidths: number[]
  className?: string
}

/** Labelled percentage columns over a segmented share bar. */
export function StatBreakdown({ stats, columnWidths, className }: StatBreakdownProps) {
  return (
    <div className={className}>
      <div className="flex">
        {stats.map((s, i) => (
          <div key={s.label} style={{ width: columnWidths[i] }} className={i === stats.length - 1 ? 'flex-1' : ''}>
            <div className="flex items-center text-[13px] leading-[16px] text-black">
              <span className="mr-[4px] h-[13px] w-[2px]" style={{ background: s.color }} />
              {s.label}
            </div>
            <div className="mt-[4px] text-[22px] leading-[26px] font-semibold text-black">{s.value}</div>
            <div className="text-[14px] leading-[17px] text-[#8e8e93]">{s.count}</div>
          </div>
        ))}
      </div>
      <div className="mt-[11px] flex h-[4px] gap-[3px]">
        {stats.map((s) => (
          <span key={s.label} className="rounded-full" style={{ background: s.color, flexGrow: s.share, flexBasis: 0 }} />
        ))}
      </div>
    </div>
  )
}
