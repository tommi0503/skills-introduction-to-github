import { ArrowRight } from 'lucide-react'
import { hero } from '../data'
import { theme } from '../theme'

/** Orange hero panel (gradient art flattened to a solid section colour). */
export function Hero() {
  return (
    <section
      className="relative mx-2 mt-2 flex h-[760px] flex-col items-center rounded-[16px] text-white"
      style={{ background: theme.color.heroOrange }}
    >
      <span className="mt-[188px] flex h-[42px] items-center gap-4 rounded-full border border-white/70 pl-4 pr-[6px] text-[16px] font-medium leading-5 tracking-[-0.1px]">
        {hero.eyebrow}
        <span className="flex size-[26px] items-center justify-center rounded-full bg-white text-[#ff5e1f]">
          <ArrowRight className="size-4" strokeWidth={2.25} />
        </span>
      </span>
      <h1 className="mt-[40px] w-[1080px] text-center text-[56px] font-medium leading-[55.44px] tracking-[-0.95px]">
        {hero.title.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </h1>
      <p className="mt-[39px] text-center text-[19.2px] leading-[23.04px] tracking-[-0.48px]">
        {hero.body.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </p>
      <span className="mt-[56px] flex h-[50px] w-[204px] items-center justify-center rounded-full bg-white text-[16px] font-medium text-[#1f1f1f]">
        {hero.cta}
      </span>
    </section>
  )
}
