import { Pill } from './Pill'

export interface Plan {
  amount?: string
  discount: string
}

/** Row of three white package cards (only the top shows above the fold). */
export function PlanCards({ plans }: { plans: Plan[] }) {
  return (
    <div className="flex gap-[3px]">
      {plans.map((p, i) => (
        <div key={i} className="relative h-[110px] w-[106px] rounded-[14px] bg-white">
          <Pill tone="grey" width={50} height={19} className="absolute top-[11px] left-[9px] text-[7.5px] text-[#b0b0b0]">
            {p.discount}
          </Pill>
          {p.amount && (
            <span className="absolute top-[58px] left-[9px] text-[34px] leading-[40px] tracking-[-0.03em] text-black">{p.amount}</span>
          )}
        </div>
      ))}
    </div>
  )
}
