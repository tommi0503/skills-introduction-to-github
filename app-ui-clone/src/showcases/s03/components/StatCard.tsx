import type { Stat } from '../data'
import { SoftCard } from './SoftCard'

/** Big number + caption tile. */
export function StatCard({ stat }: { stat: Stat }) {
  return (
    <SoftCard className="h-[86px] px-[17px] pt-[23px]">
      <div className="text-[21px] leading-[24px] font-bold tracking-[-0.3px]">{stat.value}</div>
      <div className="mt-[7px] text-[11px] font-medium text-[#9c9ca1]">{stat.label}</div>
    </SoftCard>
  )
}
