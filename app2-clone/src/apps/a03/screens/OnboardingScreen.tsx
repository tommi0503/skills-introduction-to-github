import { AppScreen, ImagePlaceholder } from '../../../ui'
import { TopBar } from '../components/TopBar'
import { onboarding } from '../data'

export function OnboardingScreen() {
  return (
    <AppScreen className="font-inter" background="#000">
      <ImagePlaceholder tone="#0b0f1d" className="absolute inset-0" label="gradient artwork" />
      <TopBar color="#fff" />
      <ImagePlaceholder tone="#4a5163" className="absolute rounded-[4px]" style={{ left: 30, top: 71, width: 80, height: 25 }} label="public logo" />
      <h1 className="absolute font-times text-[40px] leading-[48px] tracking-[-0.6px] text-white" style={{ left: 30, top: 211 }}>
        {onboarding.headline.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </h1>
      <ul className="absolute flex flex-col gap-[9.5px]" style={{ left: 31, top: 336 }}>
        {onboarding.features.map(({ key, icon: Icon, label }) => (
          <li key={key} className="flex items-center gap-[8px]">
            <span className="flex h-[31.5px] w-[31.5px] items-center justify-center rounded-[4px] bg-[#3a3d46] text-white">
              <Icon size={13} strokeWidth={2.4} fill={key === 'support' ? '#fff' : 'none'} />
            </span>
            <span className="text-[14px] text-[#e6e6ea]">{label}</span>
          </li>
        ))}
      </ul>
      <div className="absolute flex items-center justify-center rounded-full bg-white text-[15px] font-semibold" style={{ left: 30, right: 34, top: 667, height: 50 }}>
        {onboarding.primary}
      </div>
      <div className="absolute inset-x-0 text-center text-[15px] font-semibold text-white" style={{ top: 751 }}>
        {onboarding.secondary}
      </div>
    </AppScreen>
  )
}
