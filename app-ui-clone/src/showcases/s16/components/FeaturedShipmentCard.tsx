import { CalendarDays, MapPin } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { FeaturedShipment } from '../data'
import { theme } from '../theme'
import { ShipmentProgress } from './ShipmentProgress'
import { StatusChip } from './StatusChip'

const factIcons = { pin: MapPin, calendar: CalendarDays }

/** Hero shipment card: product, status, progress tracker and key facts. */
export function FeaturedShipmentCard({ data }: { data: FeaturedShipment }) {
  return (
    <div className="relative mx-[16px] h-[183px] overflow-hidden rounded-[20px] bg-white">
      <div className="absolute top-[16px] left-[16px] flex items-center gap-[7px]">
        <ImagePlaceholder className="h-[46px] w-[46px] rounded-full" label="product" />
        <div>
          <div className="text-[15px] leading-[21px] tracking-[-0.2px]" style={{ color: theme.ink }}>
            {data.title}
          </div>
          <div className="mt-[2px] text-[12px]" style={{ color: theme.muted }}>
            {data.code}
          </div>
        </div>
      </div>
      <StatusChip label={data.status} tone="grey" className="absolute top-[16px] right-[16px] h-[31px] w-[63px]" />
      <div className="absolute top-[77px] left-[15px]">
        <ShipmentProgress steps={data.steps} />
      </div>
      <ImagePlaceholder className="absolute top-[63px] right-0 h-[120px] w-[118px] rounded-tl-[6px]" label="parcel boxes" />
      <div className="absolute top-[122px] left-[16px] flex gap-[36px]">
        {data.facts.map((f) => {
          const Icon = factIcons[f.icon]
          return (
            <div key={f.label}>
              <div className="flex items-center gap-[4px] text-[12px]" style={{ color: theme.muted }}>
                <Icon size={14} strokeWidth={1.6} />
                {f.label}
              </div>
              <div className="mt-[6px] text-[17px] font-medium tracking-[-0.2px]" style={{ color: theme.ink }}>
                {f.value}
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
