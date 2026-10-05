import { AppStatusBar } from '../components/AppHeader'
import { FaqCard } from '../components/FaqCard'
import { HeroCard } from '../components/HeroCard'
import { Pill } from '../components/Pill'
import { faq } from '../data'
import { headline } from '../theme'

const CARD_HEIGHTS = [530, 200]

/** Phone 4 — FAQ panel with expandable question cards. */
export function FaqScreen() {
  return (
    <>
      <AppStatusBar />
      <HeroCard top={62.8} height={900} radius={22}>
        <div className="absolute top-[36px] flex w-full justify-center">
          <Pill tone="glass" width={156} height={26}>
            {faq.badge}
          </Pill>
        </div>
        <h1 className={`absolute top-[80px] w-full text-center text-white ${headline}`}>
          Common questions about
          <br />
          buying Blastup likes
        </h1>
        <div className="absolute top-[188px] left-[13.7px] flex flex-col gap-[13px]">
          {faq.items.map((item, i) => (
            <FaqCard key={item.question} item={item} height={CARD_HEIGHTS[i]} />
          ))}
        </div>
      </HeroCard>
    </>
  )
}
