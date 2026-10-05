import { ChevronDown } from 'lucide-react'
import { FloatingTiles } from '../components/FloatingTiles'
import { PillButton } from '../components/PillButton'
import { hero, heroTiles } from '../data'
import { theme } from '../theme'

/** Full-viewport hero: drifting tiles around the wordmark, headline and CTAs. */
export function Hero() {
  return (
    <section className="absolute left-0 top-0 h-[900px] w-[1440px]" style={{ background: theme.color.canvas }}>
      <FloatingTiles tiles={heroTiles} />
      <div className="absolute left-0 top-[357px] flex flex-col items-center" style={{ width: theme.contentWidth }}>
        <span className="text-[23px] font-semibold leading-[24px] tracking-[-0.2px]" style={{ color: theme.color.ink }}>
          {hero.wordmark}
        </span>
        <h1
          className="mt-[16px] text-center"
          style={{ fontSize: 74, lineHeight: '74px', letterSpacing: '-3.7px', fontWeight: 350, color: theme.color.ink }}
        >
          {hero.title.map((line) => (
            <span key={line} className="block">
              {line}
            </span>
          ))}
        </h1>
        <div className="mt-[30px] flex gap-[8px]">
          <PillButton className="h-[56px] w-[104px] text-[16px]">{hero.primary}</PillButton>
          <PillButton variant="ghost" className="h-[56px] w-[134px] text-[16px]">
            {hero.secondary}
          </PillButton>
        </div>
      </div>
      <ChevronDown size={24} strokeWidth={1.5} className="absolute left-[703px] top-[852px]" color={theme.color.hint} />
    </section>
  )
}
