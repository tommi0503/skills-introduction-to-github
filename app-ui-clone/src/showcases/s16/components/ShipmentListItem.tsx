import { ImagePlaceholder } from '../../../ui'
import type { ShipmentRow } from '../data'
import { theme } from '../theme'
import { StatusChip } from './StatusChip'

/** One row of the shipments sheet. */
export function ShipmentListItem({ row }: { row: ShipmentRow }) {
  return (
    <div
      className="flex h-[74px] items-center rounded-[18px] pr-[12px] pl-[14px]"
      style={{ background: '#fdfdfd', boxShadow: '0 2px 10px rgba(0,0,0,0.035)' }}
    >
      <ImagePlaceholder className="h-[50px] w-[50px] rounded-full" label={row.title} />
      <div className="ml-[6px] flex-1">
        <div className="text-[15px] leading-[20px] tracking-[-0.2px]" style={{ color: theme.ink }}>
          {row.title}
        </div>
        <div className="mt-[2px] text-[12px]" style={{ color: theme.muted }}>
          {row.code}
        </div>
      </div>
      <StatusChip label={row.status} tone={row.tone} className="h-[28px] px-[11px] text-[10.5px]!" />
    </div>
  )
}
