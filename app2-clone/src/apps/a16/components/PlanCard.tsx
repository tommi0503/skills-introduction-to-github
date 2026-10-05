import { Check } from 'lucide-react'
import { cn } from '../../../ui'
import type { Plan } from '../data'

/** Selectable subscription option with optional floating badge. */
export function PlanCard({ plan, className }: { plan: Plan; className?: string }) {
  return (
    <div
      className={cn(
        'relative flex h-[87px] items-center justify-between rounded-[10px] bg-white px-[15px]',
        plan.selected ? 'border-[1.5px] border-[#6a6ad8]' : 'border-[1.5px] border-[#e6e6e8]',
        className,
      )}
    >
      {plan.badge && (
        <span className="absolute -top-[13px] right-[10px] rounded-full bg-[#5b5bd6] px-[11px] py-[5px] text-[10.5px] leading-none font-bold tracking-[0.3px] text-white">
          {plan.badge}
        </span>
      )}
      <div>
        <div className="flex items-center gap-[9px]">
          {plan.selected ? (
            <span className="flex size-[17px] items-center justify-center rounded-full bg-[#5b5bd6] text-white">
              <Check size={11} strokeWidth={3.5} />
            </span>
          ) : (
            <span className="size-[17px] rounded-full border-[1.5px] border-[#dcdcdf]" />
          )}
          <span className="text-[18px] font-medium text-[#111]">{plan.name}</span>
        </div>
        <p className="mt-[5px] text-[13.5px] text-[#444]">{plan.detail}</p>
      </div>
      <span className="text-[15px] font-semibold text-[#111]">{plan.price}</span>
    </div>
  )
}
