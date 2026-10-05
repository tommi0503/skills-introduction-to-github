import type { Stat } from '../data'
import { SoftCard } from './SoftCard'

/** Big number + caption tile. */
export function StatCard({ stat }: { stat: Stat }) {
  return (
    <SoftCard className="h-[86px] px-[17px] pt-[21px]">
      <div className="text-[24px] leading-[26px] font-bold tracking-[-0.3px]">{stat.value}</div>
      <div className="mt-[4px] text-[11.7px] font-medium text-[#8e8e93]">{stat.label}</div>
    </SoftCard>
  )
}
