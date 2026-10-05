import { cn } from '../../../ui'
import type { PlanOption } from '../data'

/** Billing period option tile with radio + price. */
export function PlanOptionCard({ option }: { option: PlanOption }) {
  return (
    <div
      className={cn(
        'relative h-[108px] flex-1 rounded-[12px] border px-[15px] pt-[14px]',
        option.selected ? 'border-[#b7c8e6] bg-[#e9eef8]' : 'border-[#efeeea] bg-white',
      )}
    >
      {option.selected ? (
        <span className="block size-[20px] rounded-full border-[6px] border-[#2f63c8] bg-white" />
      ) : (
        <span className="block size-[20px] rounded-full border-[1.5px] border-[#d9d8d3]" />
      )}
      {option.badge && (
        <span className="absolute top-[14px] right-[16px] rounded-[5px] bg-[#dfe7f6] px-[4px] py-[2px] text-[13px] text-[#3b64a8]">
          {option.badge}
        </span>
      )}
      <p className="mt-[15px] text-[16px] font-semibold text-[#141413]">{option.price}</p>
      <p className="mt-[1px] text-[13px] text-[#3d3d3a]">{option.billing}</p>
    </div>
  )
}
