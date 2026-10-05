import { X } from 'lucide-react'
import { AppScreen, IconButton, ImagePlaceholder } from '../../../ui'
import { BrandMark } from '../components/BrandMark'
import { Chrome } from '../components/Chrome'
import { FeatureList } from '../components/FeatureList'
import { PillButton } from '../components/PillButton'
import { PlanCard } from '../components/PlanCard'
import { RatingRow } from '../components/RatingRow'
import { paywall } from '../data'
import { theme } from '../theme'

export function PaywallScreen() {
  return (
    <AppScreen>
      <div className="absolute inset-x-0 top-0 h-[256px] bg-black" />
      <ImagePlaceholder tone={theme.photoDark} label="listener photo" className="absolute inset-x-0 top-0 h-[178px]" />
      <Chrome color="#000" chipClassName="bg-[#8d8f95]/95!" />
      <BrandMark size={40} tone="#f1f2f4" className="absolute top-[72px] left-[16px]" label="ElevenReader logo" />
      <IconButton icon={X} size={32} iconSize={18} strokeWidth={1.6} className="absolute top-[68px] right-[22px] bg-white/60 text-[#8c95a3]" />
      <h1 className="absolute top-[209px] left-[17px] text-[22.5px] leading-none font-semibold tracking-[-0.2px] text-white">
        {paywall.title}
      </h1>
      <div className="absolute inset-x-0 top-[274px] pl-[14px] pr-[19px]">
        <RatingRow stars={paywall.rating.stars} label={paywall.rating.label} />
        <FeatureList items={paywall.features} className="mt-[19px] pl-[2px]" />
        <div className="mt-[33px] flex flex-col gap-[11px]">
          {paywall.plans.map((p) => (
            <PlanCard key={p.key} plan={p} />
          ))}
        </div>
        <PillButton variant="dark" className="mt-[40px] ml-[3px] h-[60px] w-[350px]! bg-black text-[17px] font-medium">
          {paywall.cta}
        </PillButton>
        <p className="mt-[11px] text-center text-[13.5px] leading-[17px] whitespace-pre-line text-[#9a9aa0]">{paywall.footnote}</p>
      </div>
    </AppScreen>
  )
}
