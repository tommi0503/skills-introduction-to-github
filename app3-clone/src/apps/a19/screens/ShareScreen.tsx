import { X } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { FixtureCard } from '../components/FixtureCard'
import { MatchHeader } from '../components/MatchHeader'
import { PhoneStatus } from '../components/PhoneStatus'
import { Sheet } from '../components/Sheet'
import { fixtures, share } from '../data'
import { theme } from '../theme'

export function ShareScreen() {
  const card = fixtures.find((f) => f.key === 'tb')!
  return (
    <AppScreen background={theme.sheetBackdrop} className="font-jakarta">
      <PhoneStatus />
      <Sheet style={{ background: `linear-gradient(to bottom, ${theme.matchTop}, ${theme.matchBottom})` }}>
        <MatchHeader crestStyle="filled" />
        <div className="absolute inset-x-0 top-[270px] flex flex-col items-center text-white/90">
          <span className="text-[17px] leading-[24px] font-semibold">Tomorrow</span>
          <span className="mt-[4px] text-[43px] leading-[50px] font-bold text-white/40">3:05 AM</span>
        </div>
      </Sheet>
      <div className="absolute top-[372px] left-[7px] h-[466px] w-[376px] rounded-[28px] bg-white">
        <div className="absolute top-[19px] left-[319px] flex h-[38px] w-[38px] items-center justify-center rounded-full bg-white" style={{ boxShadow: '0 2px 10px rgba(0,0,0,0.12)' }}>
          <X size={20} strokeWidth={1.8} />
        </div>
        <h2 className="absolute inset-x-0 top-[30px] text-center font-condensed text-[37px] leading-[30px] font-black tracking-[-1.8px] whitespace-pre-line" style={{ color: theme.ink, transform: 'scaleX(0.8)' }}>
          {share.title}
        </h2>
        <p className="absolute top-[110px] left-[40px] w-[296px] text-center text-[13.5px] leading-[19px] font-medium text-[#333]">{share.body}</p>
        <FixtureCard
          fixture={{ ...card, time: `Tomorrow - ${card.time}` }}
          className="absolute top-[188px] left-[88px] h-[168px] w-[190px] shadow-[0_6px_16px_rgba(0,0,0,0.18)]"
          style={{ transform: 'rotate(-5deg)' }}
        />
        <div className="absolute top-[395px] left-[26px] flex gap-[13px]">
          <button className="flex h-[44px] w-[154px] items-center justify-center rounded-full text-[15px] font-semibold text-white" style={{ background: theme.ink }}>
            {share.primary}
          </button>
          <button className="flex h-[44px] w-[154px] items-center justify-center rounded-full bg-white text-[15px] font-semibold text-[#222]" style={{ boxShadow: '0 2px 10px rgba(0,0,0,0.08)' }}>
            {share.secondary}
          </button>
        </div>
      </div>
    </AppScreen>
  )
}
