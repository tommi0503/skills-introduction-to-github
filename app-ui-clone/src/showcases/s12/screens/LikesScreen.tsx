import { ImagePlaceholder } from '../../../ui'
import { AppStatusBar, NavHeader } from '../components/AppHeader'
import { HeroCard } from '../components/HeroCard'
import { Pill } from '../components/Pill'
import { PlanCards } from '../components/PlanCards'
import { hero, pricingTeaser } from '../data'
import { headline, theme } from '../theme'

/** Phone 1 — "Supercharge your growth" landing with likes packages. */
export function LikesScreen() {
  return (
    <>
      <AppStatusBar />
      <NavHeader />
      <HeroCard top={109.6} height={547}>
        <ImagePlaceholder label="mascot body" className="absolute top-0 right-0 h-full w-[130px]" />
        <ImagePlaceholder label="mascot arm" className="absolute top-[89px] left-0 h-[159px] w-[232px]" />
        <Pill tone="glass" width={132} className="absolute top-[24px] left-[22px]">
          {hero.badge}
        </Pill>
        <div className="absolute top-[366px] left-[22px] w-[300px] text-white">
          <h1 className={headline}>{hero.title}</h1>
          <p className="mt-[3px] text-[12.5px] leading-[18px] tracking-[-0.02em] text-white/75">{hero.body}</p>
        </div>
      </HeroCard>
      <div className="absolute top-[670.5px] left-[13.6px] h-[300px] w-[362px] rounded-[19px]" style={{ background: theme.surface }}>
        <h2 className="absolute top-[20px] left-[22px] w-[290px] text-[24px] leading-[27px] font-medium tracking-[-0.035em] text-[#1a1a1a]">
          {pricingTeaser.title}
        </h2>
        <div className="absolute top-[86px] left-[23.4px]">
          <PlanCards plans={pricingTeaser.plans} />
        </div>
      </div>
    </>
  )
}
