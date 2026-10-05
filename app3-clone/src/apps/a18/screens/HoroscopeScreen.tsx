import { ChevronLeft } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { PhoneStatus } from '../components/PhoneStatus'
import { RoundAction } from '../components/RoundAction'
import { horoscope, shareActions } from '../data'
import { theme } from '../theme'

export function HoroscopeScreen() {
  return (
    <AppScreen background={theme.articleBg} className="font-figtree">
      <ImagePlaceholder tone="#6b6560" label="woman in clouds photo" className="absolute inset-x-0 top-0 h-[600px]" />
      <div className="absolute inset-x-0 top-[380px] h-[300px]" style={{ background: `linear-gradient(to bottom, #3a332f00, #3a332fcc 50%, ${theme.articleBg})` }} />
      <PhoneStatus color="#fff" />
      <div className="absolute top-[69px] left-[19px] flex h-[35px] w-[35px] items-center justify-center rounded-full bg-white/15 text-white">
        <ChevronLeft size={20} strokeWidth={3} />
      </div>
      <div className="absolute inset-x-0 top-[69px] flex flex-col items-center">
        <span className="text-[13px] leading-[18px] font-semibold text-white">{horoscope.title}</span>
        <span className="mt-[3px] text-[10.5px] leading-[14px] font-medium text-white/60">
          {horoscope.kicker} &nbsp;·&nbsp; {horoscope.date}
        </span>
      </div>
      <h1 className="absolute top-[422px] left-[24px] w-[322px] font-playfair text-[29px] leading-[43px] font-black tracking-[0.2px] text-white">
        {horoscope.focus}
      </h1>
      <p className="absolute top-[587px] left-[24px] w-[345px] font-jakarta text-[21.3px] leading-[30.5px] font-medium tracking-[-0.2px] text-white">{horoscope.body}</p>
      <div className="absolute top-[739px] left-[219px] flex gap-[8px]">
        {shareActions.map((a) => (
          <RoundAction key={a.key} action={a} size={44} iconSize={16} className="bg-white text-black" markTone="#3a3a3a" />
        ))}
      </div>
      <div className="absolute top-[798px] left-[24px] flex h-[40px] w-[342px] items-center justify-center rounded-[20px] border border-white/25 bg-white/10 text-[13px] font-semibold text-white">
        {horoscope.cta}
      </div>
    </AppScreen>
  )
}
