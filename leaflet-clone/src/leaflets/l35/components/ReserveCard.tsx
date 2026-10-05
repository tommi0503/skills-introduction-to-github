import { larana } from '../../shared-3435/theme'
import type { ReserveMethod } from '../data'

/** Outlined method card: caption, value and a blue icon in the bottom-right corner. */
export function ReserveCard({ method }: { method: ReserveMethod }) {
  const Icon = method.icon
  return (
    <div className="relative h-[131px] rounded-[9px] pl-[21px] pt-[15px]" style={{ border: `2px solid ${larana.cardLine}` }}>
      <p className="m-0 text-[12.5px] font-bold leading-[18px]" style={{ color: larana.label }}>
        {method.label}
      </p>
      <p className="m-0 mt-[4px] text-[15px] font-medium leading-[22px]" style={{ color: larana.inkSoft }}>
        {method.value}
      </p>
      <Icon size={36} strokeWidth={2} color={larana.blue} className="absolute right-[14px] bottom-[14px]" />
    </div>
  )
}
