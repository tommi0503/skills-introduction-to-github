import { Check } from 'lucide-react'
import { getStarted, type Plan } from '../data'
import { theme } from '../theme'
import { Divider } from '../components/Divider'
import { PillButton } from '../components/PillButton'

function PlanCard({ plan }: { plan: Plan }) {
  return (
    <div className="relative h-[416px] rounded-[16px] p-[40px]" style={{ background: theme.card }}>
      <h3 className="text-[24px] font-[450] leading-8 tracking-[-0.24px]">{plan.title}</h3>
      <p className="mt-[12px] text-[16px] leading-6">{plan.body}</p>
      <Divider color="#e4e3e1" style={{ marginTop: 24 }} />
      <ul className="mt-[24px] flex flex-col gap-[12px]">
        {plan.features.map((f) => (
          <li key={f} className="flex items-center gap-[12px] text-[14px] leading-5">
            <Check size={14} strokeWidth={1.6} className="text-black/30" />
            {f}
          </li>
        ))}
      </ul>
      <PillButton variant={plan.variant === 'solid' ? 'dark' : 'outline'} className="absolute bottom-[40px] left-[40px] right-[40px]">
        {plan.cta}
      </PillButton>
    </div>
  )
}

export function GetStarted() {
  return (
    <section className="mx-auto mt-[96px] border-t pt-[96px]" style={{ width: 1280, borderColor: theme.rule, color: theme.ink }}>
      <h2 className="text-center text-[30px] font-[450] leading-9 tracking-[-0.3px]">{getStarted.title}</h2>
      <div className="mx-auto mt-[40px] grid grid-cols-2 gap-[24px]" style={{ width: theme.content }}>
        {getStarted.plans.map((p) => (
          <PlanCard key={p.title} plan={p} />
        ))}
      </div>
    </section>
  )
}
