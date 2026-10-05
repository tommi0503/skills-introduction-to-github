import { ArrowLeft, Navigation, X } from 'lucide-react'
import { AppScreen, Button, HomeIndicator, StatusBar } from '../../../ui'
import { streak } from '../data'
import { StreakPlanCard } from '../components/StreakPlanCard'
import { streakPalette as c } from '../theme'

export function StreakPaywallScreen() {
  return (
    <AppScreen className="font-inter">
      <StatusBar
        paddingX={22}
        paddingTop={14}
        fontSize={16}
        timeAddon={<Navigation size={12} fill="currentColor" strokeWidth={0} className="rotate-0" />}
      />
      <X size={22} strokeWidth={1.6} color="#a0a0a5" className="absolute top-[59px] right-[23px]" />
      <h1 className="mt-[7px] text-center text-[24.5px] font-bold tracking-[-0.2px]" style={{ color: c.text }}>
        {streak.title}
      </h1>
      <p className="mt-[6px] text-center text-[15.2px] leading-[18.6px] tracking-[-0.1px]" style={{ color: c.muted }}>
        {streak.description.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </p>
      <div className="mt-[40px] flex flex-col gap-[12px] px-[22px]">
        {streak.plans.map((p) => (
          <StreakPlanCard key={p.key} plan={p} selected={p.key === streak.selected} />
        ))}
      </div>
      <div className="mt-[32px] text-center text-[13px] font-semibold" style={{ color: c.muted }}>
        {streak.restore}
      </div>
      <div className="absolute inset-x-0 top-[672px] text-center text-[13.5px] font-semibold" style={{ color: c.text }}>
        <span className="font-normal line-through" style={{ color: c.muted }}>
          {streak.summaryStrike}
        </span>{' '}
        {streak.summary}
      </div>
      <Button
        className="absolute top-[699px] left-[20px] h-[59px] w-[349px] flex-col rounded-[20px] text-white"
        style={{ background: c.accent }}
      >
        <span className="text-[17.5px] leading-[21px] font-semibold">{streak.cta}</span>
        <span className="text-[12.5px] leading-[15px] font-medium opacity-60">{streak.ctaSub}</span>
      </Button>
      <div
        className="absolute inset-x-0 top-[775px] flex items-center justify-center gap-[4px] text-[13px] font-semibold"
        style={{ color: c.muted }}
      >
        <ArrowLeft size={13} strokeWidth={2.2} />
        {streak.back}
      </div>
      <HomeIndicator width={138} bottom={6} />
    </AppScreen>
  )
}
