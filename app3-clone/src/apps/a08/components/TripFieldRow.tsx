import type { TripField } from '../data'
import { airbnb } from '../theme'

export function TripFieldRow({ field }: { field: TripField }) {
  return (
    <div className="flex items-start justify-between" style={{ color: airbnb.ink }}>
      <div>
        <div className="text-[16px] leading-[20px] font-semibold">{field.label}</div>
        <div className="mt-[10px] text-[16px] leading-[20px]">{field.value}</div>
      </div>
      <span className="text-[16px] leading-[20px] font-semibold underline underline-offset-2">{field.action}</span>
    </div>
  )
}
