import { ShieldCheck } from 'lucide-react'
import { AppScreen, ImagePlaceholder, cn } from '../../../ui'
import { PhoneStatus } from '../components/PhoneStatus'
import { PlanRow } from '../components/PlanRow'
import { included, plans } from '../data'
import { theme } from '../theme'

export function PaywallScreen() {
  return (
    <AppScreen background={theme.paywallBg} className="font-figtree">
      <ImagePlaceholder tone={theme.photoTone} label="meditating woman photo" className="absolute inset-x-0 top-0 h-[440px]" />
      <div className="absolute inset-x-0 top-[300px] h-[140px]" style={{ background: `linear-gradient(to bottom, ${theme.paywallBg}00, ${theme.paywallBg})` }} />
      <PhoneStatus color="#fff" />
      <span className="absolute top-[62px] right-[36px] text-[13px] font-medium text-white/55">Restore</span>
      <ImagePlaceholder tone="#8a8b8e" label="moonly PLUS logo" className="absolute top-[169px] left-[20px] h-[20px] w-[109px] rounded-[4px]" />
      <h1 className="absolute top-[203px] left-[18px] font-outfit text-[43px] leading-[46px] font-medium tracking-[-0.2px] text-white">
        Your Daily Guide
        <br />
        to Self-Discovery
      </h1>
      <p className="absolute top-[306px] left-[20px] w-[355px] text-[13.3px] leading-[18px] font-semibold text-white">
        Find clarity within, align with universal rhythms, and navigate your destiny
      </p>
      <div className="absolute top-[376px] left-[20px] flex w-[348px] flex-col gap-[3px] overflow-hidden rounded-[14px]">
        {plans.map((p) => (
          <PlanRow key={p.key} plan={p} />
        ))}
      </div>
      <div className="absolute top-[583px] left-[20px] h-[300px] w-[348px] rounded-[16px] px-[24px] pt-[13px]" style={{ background: theme.includedBg }}>
        <h2 className="text-[16.5px] font-semibold text-[#9a9aa0]">What’s Included</h2>
        <div className="mt-[15px] flex flex-col gap-[9px]">
          {included.map((row, i) => (
            <div key={i} className="flex gap-[6px]">
              {row.map((c) => (
                <span
                  key={c.label}
                  className={cn('flex h-[32px] items-center gap-[4px] rounded-full px-[13px] text-[14.5px] font-medium text-[#dcdce0]')}
                  style={{ background: theme.chip }}
                >
                  {c.label}
                  {c.emoji && <ImagePlaceholder tone="#c9a64a" label="comet emoji" className="h-[16px] w-[16px] rounded-full" />}
                </span>
              ))}
            </div>
          ))}
        </div>
      </div>
      <div
        className="absolute inset-x-0 top-[680px] bottom-0"
        style={{ background: `linear-gradient(to bottom, ${theme.paywallBg}00 0%, ${theme.paywallBg}d0 40%, ${theme.paywallBg}d8 100%)` }}
      />
      <div className="absolute inset-x-0 top-[707px] flex items-center justify-center gap-[6px] text-[13px] font-medium text-white">
        <ShieldCheck size={20} fill="#3dbb5b" color="#ffffff" strokeWidth={1.8} />
        No Commitment. Cancel Anytime.
      </div>
      <button className="absolute top-[742px] left-[20px] flex h-[59px] w-[349px] items-center justify-center rounded-full bg-white text-[18px] font-bold text-black">
        Continue
      </button>
    </AppScreen>
  )
}
