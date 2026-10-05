import type { Plan } from '../data'
import { theme } from '../theme'

export function PlanCard({ plan }: { plan: Plan }) {
  return (
    <div
      className="relative flex h-[76px] items-center justify-between rounded-[14px] pr-[26px] pl-[25px]"
      style={{ background: theme.planBg, border: plan.selected ? '1.5px solid #e2e2e2' : '1.5px solid #1c1c1c' }}
    >
      {plan.badge && (
        <span
          className="absolute top-[-11px] right-[17px] rounded-[4px] px-[6px] text-[12.5px] leading-[19px] font-semibold text-white"
          style={{ background: theme.discount }}
        >
          {plan.badge}
        </span>
      )}
      <div className="flex flex-col">
        <span className="text-[15px] leading-[20px] font-semibold text-white">{plan.name}</span>
        <span className="text-[13px] leading-[18px] text-[#bdbdbd]">{plan.price}</span>
      </div>
      <span className="text-[13.5px] text-white">{plan.perWeek}</span>
    </div>
  )
}
