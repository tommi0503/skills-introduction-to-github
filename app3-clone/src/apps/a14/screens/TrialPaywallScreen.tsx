import { X } from 'lucide-react'
import { AppScreen, Button, HomeIndicator, ImagePlaceholder, StatusBar } from '../../../ui'
import { trial } from '../data'
import { FeatureRow } from '../components/FeatureRow'
import { TrialPlanTile } from '../components/TrialPlanTile'
import { trialPalette as c } from '../theme'

export function TrialPaywallScreen() {
  return (
    <AppScreen className="font-inter">
      {trial.photos.map((p, i) => (
        <ImagePlaceholder
          key={i}
          className="absolute"
          style={{ left: p.x, top: p.y, width: p.w, height: p.h, borderRadius: p.r }}
          label="food photo"
        />
      ))}
      <StatusBar paddingX={54} paddingTop={20} fontSize={16} />
      <span className="absolute top-[58px] left-[338px] flex h-[32px] w-[32px] items-center justify-center rounded-full bg-[#8e8e8e]/85">
        <X size={15} strokeWidth={3} color="#fff" />
      </span>
      <h1 className="relative mt-[60px] ml-[25px] text-[31px] leading-[41px] font-bold tracking-[-0.6px]" style={{ color: c.text }}>
        {trial.title.map((t) => (
          <div key={t}>{t}</div>
        ))}
      </h1>
      <p className="mt-[16px] ml-[26px] w-[300px] text-[13.5px] leading-[18.5px] tracking-[-0.2px]" style={{ color: c.muted }}>
        {trial.subtitle}
      </p>
      <div className="mt-[37px] ml-[25px] flex flex-col gap-[28px]">
        {trial.features.map((f) => (
          <FeatureRow key={f.title} feature={f} />
        ))}
      </div>
      <div className="mt-[48px] text-center text-[14.5px] font-semibold tracking-[-0.3px]" style={{ color: c.text }}>
        {trial.selectTitle}
      </div>
      <div className="mt-[28px] flex gap-[18px] px-[17px]">
        {trial.plans.map((p) => (
          <TrialPlanTile key={p.key} plan={p} selected={p.key === trial.selected} />
        ))}
      </div>
      <div className="mt-[24px] text-center text-[12px] tracking-[-0.2px]" style={{ color: c.muted }}>
        {trial.note}
      </div>
      <Button
        className="absolute top-[764px] left-[17px] h-[49px] w-[356px] rounded-full text-[15px] font-semibold text-white"
        style={{ background: c.blue }}
      >
        {trial.cta}
      </Button>
      <HomeIndicator width={138} bottom={6} />
    </AppScreen>
  )
}
