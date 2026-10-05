import { cn } from '../../../ui'
import type { Plan } from '../data'
import { theme } from '../theme'

export function PlanRow({ plan, className }: { plan: Plan; className?: string }) {
  return (
    <div className={cn('flex h-[63px] items-center pr-[20px] pl-[11px]', className)} style={{ background: theme.planRow }}>
      <span
        className="h-[30px] w-[30px] shrink-0 rounded-full"
        style={
          plan.selected
            ? { background: theme.accent, boxShadow: 'inset 0 0 0 3px #6b6b70' }
            : { background: '#6e6e74' }
        }
      />
      <div className="ml-[14px] flex flex-1 flex-col">
        <div className="flex items-center gap-[8px]">
          <span className="text-[18px] leading-[22px] font-semibold text-white">{plan.name}</span>
          {plan.badge && (
            <span className="rounded-[3px] px-[5px] text-[9.5px] leading-[16px] font-semibold text-white" style={{ background: theme.badge }}>
              {plan.badge}
            </span>
          )}
        </div>
        <span className="text-[12px] leading-[18px] font-medium text-[#c9c9cc]">{plan.detail}</span>
      </div>
      <div className="flex flex-col items-end">
        <span className="text-[15px] leading-[20px] font-bold text-white">{plan.price}</span>
        <span className="text-[11px] leading-[15px] font-medium text-[#bdbdc0]">{plan.unit}</span>
      </div>
    </div>
  )
}
