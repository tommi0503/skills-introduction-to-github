import { MoreHorizontal } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { onboarding } from '../data'
import { BotStatusBar } from '../components/BotStatusBar'
import { FloatingButton } from '../components/FloatingButton'
import { PagerDots } from '../components/PagerDots'

export function MeetBotScreen() {
  return (
    <AppScreen>
      <BotStatusBar />
      <FloatingButton icon={MoreHorizontal} iconSize={18} className="absolute top-[64px] right-[17px]" />
      <h1 className="absolute inset-x-0 top-[129px] text-center text-[24px] leading-[32px] font-[450] tracking-[-0.2px] text-[#111]">
        {onboarding.heading}
      </h1>
      <ImagePlaceholder
        label="bot mascot"
        className="absolute"
        style={{ left: 153, top: 292, width: 88, height: 88, borderRadius: '50% 0 50% 50%', transform: 'rotate(-45deg) scale(1.42)' }}
      />
      <h2 className="absolute inset-x-0 top-[492px] text-center text-[18.5px] leading-[26px] font-semibold text-[#111]">{onboarding.botName}</h2>
      <p className="absolute inset-x-[50px] top-[524px] text-center text-[14px] leading-[19.5px] text-[#7d7d7d]">{onboarding.botBlurb}</p>
      <PagerDots count={onboarding.pages} active={onboarding.activePage} className="absolute inset-x-0 top-[693px]" />
      <button type="button" className="absolute top-[719px] left-[30px] h-[43px] w-[330px] rounded-full bg-black text-[16px] font-semibold text-white">
        {onboarding.primary}
      </button>
      <span className="absolute inset-x-0 top-[781px] text-center text-[16px] leading-[24px] text-[#777]">{onboarding.secondary}</span>
    </AppScreen>
  )
}
