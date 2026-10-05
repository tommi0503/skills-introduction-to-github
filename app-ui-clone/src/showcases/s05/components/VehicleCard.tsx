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
    <div className="relative h-[492px] w-[362px] rounded-[22px]" style={{ background: theme.card, boxShadow: cardShadow }}>
      <span
        className="absolute left-[15px] top-[23px] flex h-[21px] items-center gap-[6px] rounded-full px-[9px] text-[11px]"
        style={{ background: '#e2f7e8', color: theme.greenDeep }}
      >
        <span className="h-[5px] w-[5px] rounded-full" style={{ background: theme.greenDeep }} />
        {status}
      </span>
      <span
        className="absolute right-[15px] top-[21px] flex h-[25px] items-center rounded-full px-[13px] text-[11px] whitespace-pre text-white"
        style={{ background: '#f49d33' }}
      >
        {nextService}
      </span>

      <ImagePlaceholder label="vehicle top view" className="absolute left-[106px] top-[67px] h-[300px] w-[150px] rounded-[40px]" />

      <div className="absolute left-[23px] top-[421px] grid grid-cols-[117px_117px_117px]">
        {metrics.map((m) => (
          <div key={m.key}>
            <p className="text-[13.5px] tracking-[-0.3px] text-[#7d7d7d]">{m.label}</p>
            <p className="mt-[6px] text-[17.5px] tracking-[-0.3px]" style={{ color: m.color }}>
              {m.value}
            </p>
          </div>
        ))}
      </div>
    </div>
  )
}
