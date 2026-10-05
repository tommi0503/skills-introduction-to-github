import { AppStatusBar } from '../components/AppHeader'
import { FeatureCard } from '../components/FeatureCard'
import { Pill } from '../components/Pill'
import { features, why } from '../data'
import { headline } from '../theme'

/** Phone 3 — "Why is Blastup the best" with horizontally scrolling feature tiles. */
export function WhyScreen() {
  return (
    <>
      <AppStatusBar />
      <div className="absolute top-[109px] left-[15.3px] text-[#111]">
        <Pill tone="grey" width={164} height={27}>
          {why.badge}
        </Pill>
        <h1 className={`mt-[16px] w-[350px] ${headline}`}>{why.title}</h1>
        <p className="mt-[6px] w-[300px] text-[15.5px] leading-[22px] tracking-[-0.02em] text-[#2a2a2a]">{why.body}</p>
      </div>
      <div className="absolute top-[336.8px] left-[15.3px] flex gap-[15.4px]">
        {features.map((f) => (
          <FeatureCard key={f.title} feature={f} />
        ))}
      </div>
    </>
  )
}
