import { X } from 'lucide-react'
import { PhoneStatus } from '../components/PhoneStatus'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { CircleButton } from '../components/CircleButton'
import { FeatureRow } from '../components/FeatureRow'
import { PlanCard } from '../components/PlanCard'
import { features, paywallLinks, plans } from '../data'
import { theme } from '../theme'

export function PaywallScreen() {
  return (
    <AppScreen background={theme.paywallBg}>
      <ImagePlaceholder
        tone={theme.glowTone}
        label="blue glow"
        className="absolute inset-x-0 top-0 h-[140px]"
        style={{
          WebkitMaskImage: 'radial-gradient(ellipse 230px 125px at 195px 230px, transparent 99%, #000 100%)',
          maskImage: 'radial-gradient(ellipse 230px 125px at 195px 230px, transparent 99%, #000 100%)',
        }}
      />
      <PhoneStatus color="#fff" />
      <CircleButton icon={X} variant="glass" size={34} iconSize={18} strokeWidth={2.4} className="absolute top-[67px] left-[23px]" />
      <h1 className="absolute inset-x-0 top-[130px] text-center text-[23px] leading-[30px] font-medium text-white">
        Unlock your AI phone
        <br />
        assistant today
      </h1>
      <div className="absolute top-[209px] left-[55px] flex flex-col">
        {features.map((f) => (
          <FeatureRow key={f.label} feature={f} />
        ))}
      </div>
      <div className="absolute top-[439px] left-[22px] flex h-[75px] w-[346px] items-center justify-between rounded-[14px] pr-[37px] pl-[26px]" style={{ background: theme.card }}>
        <div className="flex flex-col">
          <span className="text-[15px] leading-[20px] font-semibold text-white">Not sure yet?</span>
          <span className="text-[11px] leading-[16px] text-[#e0e0e0]">Enable free trial</span>
        </div>
        <span className="h-[22px] w-[22px] rounded-full border-[1.6px] border-[#d8d8d8]" />
      </div>
      <div className="absolute top-[549px] left-[22px] flex w-[346px] flex-col gap-[15px]">
        {plans.map((p) => (
          <PlanCard key={p.key} plan={p} />
        ))}
      </div>
      <button className="absolute top-[736px] left-[22px] flex h-[52px] w-[346px] items-center justify-center rounded-full bg-white text-[16px] font-semibold text-black">
        Continue
      </button>
      <div className="absolute inset-x-0 top-[799px] flex justify-center gap-[22px] text-[11.5px] text-[#8a8a8a]">
        {paywallLinks.map((l) => (
          <span key={l}>{l}</span>
        ))}
      </div>
    </AppScreen>
  )
}
