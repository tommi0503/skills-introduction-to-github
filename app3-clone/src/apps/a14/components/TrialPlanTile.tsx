import type { TrialPlan } from '../data'
import { trialPalette as c } from '../theme'
import { RadioMark } from './RadioMark'

export function TrialPlanTile({ plan, selected }: { plan: TrialPlan; selected: boolean }) {
  return (
    <div
      className="relative h-[138px] flex-1 rounded-[18px] bg-white px-[16px] pt-[19px]"
      style={{
        border: selected ? '1px solid #f0f0f0' : `1.5px solid ${c.border}`,
        boxShadow: selected ? '0 6px 18px rgba(0,0,0,0.13)' : undefined,
      }}
    >
      {plan.badge && (
        <span
          className="absolute -top-[13px] left-[33px] rounded-[10px] px-[12px] py-[4px] text-[11px] leading-[16px] font-bold"
          style={{ background: c.green, color: c.greenText }}
        >
          {plan.badge}
        </span>
      )}
      <div className="flex items-center justify-between">
        <span className="text-[15.5px] font-semibold tracking-[-0.3px]" style={{ color: c.text }}>
          {plan.name}
        </span>
        <span className="-mr-[2px]">
          <RadioMark checked={selected} size={24} color={c.green} idle="#e3e3e3" halo />
        </span>
      </div>
      <div className="mt-[4px] text-[18px] leading-[24px] font-semibold" style={{ color: c.price }}>
        {plan.price}
        <span className="text-[11px] font-medium">{plan.unit}</span>
      </div>
      {plan.strike && (
        <div className="text-[11.5px] leading-[16px]" style={{ color: c.price }}>
          <span className="line-through">{plan.strike}</span>
          {plan.unit}
        </div>
      )}
      <div className="absolute top-[100px] left-[16px] text-[9.5px] tracking-[-0.2px]" style={{ color: c.muted }}>
        {plan.billed}
      </div>
    </div>
  )
}
