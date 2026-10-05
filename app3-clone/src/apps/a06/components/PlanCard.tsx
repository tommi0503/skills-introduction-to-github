import { SquareArrowOutUpRight } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Plan } from '../data'
import { sp } from '../theme'

export function PlanTag({ label, color }: { label: string; color: string }) {
  return (
    <span
      className="inline-flex h-[33px] items-center px-[9px] text-[12px] font-bold text-black"
      style={{ background: color, borderRadius: '8px 0 8px 0' }}
    >
      {label}
    </span>
  )
}

export function PlanCard({ plan, brand }: { plan: Plan; brand: string }) {
  return (
    <div className="overflow-hidden rounded-[8px]" style={{ background: sp.card }}>
      <PlanTag label={plan.tag} color={plan.tagColor} />
      <div className="px-[16px] pt-[22px] pb-[17px]">
        <div className="flex items-center gap-[6px]">
          <ImagePlaceholder tone="#ffffff" className="h-[22px] w-[22px] rounded-full" label="Spotify logo" />
          <span className="text-[12px] font-semibold text-white">{brand}</span>
        </div>
        <div className="mt-[18px] text-[23px] leading-[28px] font-bold" style={{ color: sp.pinkText }}>
          {plan.name}
        </div>
        <div className="mt-[9px] text-[15px] leading-[19px] font-bold text-white">{plan.price}</div>
        <div className="mt-[1px] text-[12px]" style={{ color: sp.dim }}>
          {plan.after}
        </div>
        <div className="mt-[16px] h-px bg-white/10" />
        <ul className="mt-[17px] flex flex-col gap-0 pl-[22px] text-[14.5px] leading-[22px] text-white">
          {plan.features.map((f) => (
            <li key={f} className="list-disc pr-[16px]">
              {f}
            </li>
          ))}
        </ul>
        <button
          type="button"
          className="mx-auto mt-[17px] flex h-[47px] w-[320px] items-center justify-center gap-[10px] rounded-full text-[14.5px] font-bold text-black"
          style={{ background: plan.tagColor }}
        >
          {plan.cta}
          <SquareArrowOutUpRight size={18} strokeWidth={2} />
        </button>
        <p className="mt-[16px] px-[8px] text-center text-[10px] leading-[15.5px]" style={{ color: sp.muted }}>
          {plan.legal} <span className="underline">{plan.legalLink}</span>
          {plan.legalTail}
        </p>
      </div>
    </div>
  )
}
