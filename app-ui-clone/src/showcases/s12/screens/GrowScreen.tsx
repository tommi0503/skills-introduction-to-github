import { ImagePlaceholder } from '../../../ui'
import { AppStatusBar, NavHeader } from '../components/AppHeader'
import { HeroCard } from '../components/HeroCard'
import { NetworkPicker } from '../components/NetworkPicker'
import { Pill } from '../components/Pill'
import { PlanCards } from '../components/PlanCards'
import { growHero, networks, picker } from '../data'
import { headline, theme } from '../theme'

/** Phone 2 — centred hero with mascots and the network picker. */
export function GrowScreen() {
  return (
    <>
      <AppStatusBar />
      <NavHeader />
      <HeroCard top={109.6} height={547}>
        <ImagePlaceholder label="blue mascot" className="absolute bottom-0 left-0 h-[370px] w-[161px]" />
        <ImagePlaceholder label="orange mascot" className="absolute right-0 bottom-0 h-[365px] w-[163px]" />
        <div className="absolute top-[38px] flex w-full justify-center">
          <Pill tone="glass" width={133}>
            {growHero.badge}
          </Pill>
        </div>
        <h1 className={`absolute top-[81px] left-1/2 w-[268px] -translate-x-1/2 text-center text-white ${headline}`}>
          {growHero.title}
        </h1>
      </HeroCard>
      <div className="absolute top-[670.5px] left-[13.6px] h-[300px] w-[362px] rounded-[19px]" style={{ background: theme.surface }}>
        <h2 className="absolute top-[20px] left-[23px] text-[24px] leading-[27px] font-medium tracking-[-0.035em] text-[#1a1a1a]">
          {picker.title}
        </h2>
        <div className="absolute top-[62px] left-[23.4px]">
          <NetworkPicker items={networks} active={picker.active} />
        </div>
        <div className="absolute top-[130px] left-[23.4px]">
          <PlanCards plans={picker.discounts.map((discount) => ({ discount }))} />
        </div>
      </div>
    </>
  )
}
