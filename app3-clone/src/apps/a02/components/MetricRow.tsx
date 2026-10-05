import type { Metric } from '../data'
import { SquareButton } from './SquareButton'

/** Icon tile + label on the left, emphasised value on the right. */
export function MetricRow({ metric }: { metric: Metric }) {
  const Icon = metric.icon
  return (
    <div className="flex h-[66px] items-center pr-[15px] pl-[15px]">
      <SquareButton size={36} radius={8} className="text-[#555]">
        <Icon size={16} strokeWidth={1.6} />
      </SquareButton>
      <span className="ml-[13px] flex-1 text-[15px] tracking-[0.1px] text-[#6a6a67]">{metric.label}</span>
      <span className="text-[17.5px] font-semibold tracking-[-0.4px]">{metric.value}</span>
    </div>
  )
}
