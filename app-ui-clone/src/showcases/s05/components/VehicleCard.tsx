import { ImagePlaceholder } from '../../../ui'
import type { Metric } from '../data'
import { cardShadow, theme } from '../theme'

export interface VehicleCardProps {
  status: string
  nextService: string
  metrics: Metric[]
}

export function VehicleCard({ status, nextService, metrics }: VehicleCardProps) {
  return (
    <div className="relative h-[495px] w-[373px] rounded-[22px]" style={{ background: theme.card, boxShadow: cardShadow }}>
      <span
        className="absolute left-[15px] top-[23px] flex h-[21px] items-center gap-[6px] rounded-full px-[9px] text-[11px]"
        style={{ background: '#e2f7e8', color: theme.greenDeep }}
      >
        <span className="h-[5px] w-[5px] rounded-full" style={{ background: theme.greenDeep }} />
        {status}
      </span>
      <span
        className="absolute right-[15px] top-[21px] flex h-[25px] items-center rounded-full px-[13px] text-[11px] whitespace-pre text-white"
        style={{ background: theme.orange }}
      >
        {nextService}
      </span>

      <ImagePlaceholder label="vehicle top view" className="absolute left-[112px] top-[67px] h-[290px] w-[148px] rounded-[40px]" />

      <div className="absolute inset-x-[30px] top-[425px] grid grid-cols-3">
        {metrics.map((m) => (
          <div key={m.key}>
            <p className="text-[13px] tracking-[-0.3px] text-[#8a8a8a]">{m.label}</p>
            <p className="mt-[8px] text-[17px] tracking-[-0.3px]" style={{ color: m.color }}>
              {m.value}
            </p>
          </div>
        ))}
      </div>
    </div>
  )
}
