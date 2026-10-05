import { X } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { Chrome } from '../components/Chrome'
import { FloatButton } from '../components/FloatButton'
import { IncludesList } from '../components/IncludesList'
import { PlanOptionCard } from '../components/PlanOptionCard'
import { plans } from '../data'
import { theme } from '../theme'

export function PlansScreen() {
  const { pro, max } = plans
  return (
    <AppScreen background={theme.scrim}>
      <Chrome />
      <div className="absolute inset-x-0 top-[58px] bottom-0 rounded-t-[30px] bg-[#fafaf8]">
        <FloatButton icon={X} iconSize={20} className="absolute top-[18px] left-[15px]" />
        <h1 className="mt-[101px] text-center font-times text-[32px] leading-none tracking-[-0.8px] text-[#141413]">{plans.title}</h1>
        <p className="mt-[22px] text-center text-[16.5px] text-[#262624]">{plans.subtitle}</p>
        <section className="mx-[16px] mt-[25px] rounded-[16px] bg-white">
          <div className="px-[23px] pt-[26px] pb-[20px]">
            <h2 className="font-times text-[22px] leading-none text-[#141413]">{pro.name}</h2>
            <p className="mt-[5px] text-[14.5px] text-[#262624]">{pro.tagline}</p>
            <div className="mt-[14px] flex gap-[13px]">
              {pro.options.map((o) => (
                <PlanOptionCard key={o.key} option={o} />
              ))}
            </div>
            <button type="button" className="mt-[15px] h-[48px] w-full rounded-full bg-[#141413] text-[16px] font-semibold text-white">
              {pro.cta}
            </button>
          </div>
          <div className="border-t border-[#efeeea] px-[23px] pt-[18px] pb-[17px]">
            <IncludesList title={pro.includesTitle} items={pro.includes} footnote={pro.footnote} />
          </div>
        </section>
        <section className="mx-[16px] mt-[40px] rounded-t-[16px] bg-white px-[23px] pt-[24px] pb-[40px]">
          <h2 className="font-times text-[26px] leading-none text-[#141413]">{max.name}</h2>
          <p className="mt-[5px] text-[14.5px] text-[#262624]">{max.tagline}</p>
        </section>
      </div>
    </AppScreen>
  )
}
