import { Calendar, ChevronRight, Moon, Sparkle, Triangle } from 'lucide-react'
import { AppScreen, ImagePlaceholder, cn } from '../../../ui'
import { MoonTabBar } from '../components/MoonTabBar'
import { PhoneStatus } from '../components/PhoneStatus'
import { horoscope, shortcuts, tabs, week } from '../data'
import { theme } from '../theme'

export function TransitsScreen() {
  return (
    <AppScreen background={theme.homeBg} className="font-figtree">
      <PhoneStatus color="#fff" />
      <Moon size={16} className="absolute top-[78px] left-[40px] -rotate-90" fill={theme.accent} color={theme.accent} />
      <h1 className="absolute top-[88px] left-[20px] font-playfair text-[39px] leading-[50px] font-bold">
        <span className="text-white">Day </span>
        <span className="text-[#4a4a4e]">Transits</span>
      </h1>
      <div className="absolute top-[155px] left-[16px] flex h-[86px] w-[295px] items-center rounded-[20px] px-[9px]" style={{ background: theme.weekCard }}>
        {week.map((d) => (
          <div
            key={d.date}
            className={cn('flex h-[80px] w-[48px] flex-col items-center justify-center rounded-[16px]', d.selected && 'border border-[#8a8a90] bg-[#22252d]')}
            style={{ marginRight: 11 }}
          >
            <span className="flex h-[14px] items-center text-[10.5px] text-[#c0c0c6]">
              {d.star ? <Sparkle size={11} fill={theme.accent} color={theme.accent} /> : d.dow}
            </span>
            <ImagePlaceholder tone="#8d93a8" label="moon phase" className="mt-[11px] h-[20px] w-[20px] rounded-full" />
            <span className="mt-[9px] text-[13px] font-semibold text-white">{d.date}</span>
          </div>
        ))}
      </div>
      <div className="absolute top-[155px] left-[319px] flex h-[86px] w-[56px] flex-col items-center justify-center gap-[8px] rounded-[18px] bg-[#28292d] text-[#e8e8ea]">
        <Calendar size={19} fill="#e8e8ea" color="#28292d" strokeWidth={2} />
        <span className="text-[9.5px] text-[#a0a0a6]">MAY</span>
      </div>
      <div className="absolute top-[258px] left-[16px] flex gap-[10px]">
        {shortcuts.map((s) => (
          <div key={s.key} className="flex h-[62px] w-[174px] items-center gap-[9px] rounded-full pl-[17px]" style={{ background: theme.pill }}>
            <ImagePlaceholder tone="#3a3b40" label={s.kicker} className="h-[24px] w-[24px] rounded-full" />
            <div className="flex flex-col">
              <span className="text-[9px] leading-[11px] text-[#8a8a90]">{s.kicker}</span>
              <span className="text-[14px] leading-[18px] font-semibold text-white">{s.title}</span>
            </div>
          </div>
        ))}
      </div>
      <ImagePlaceholder tone="#5f7187" label="previous card" className="absolute top-[333px] left-[-20px] h-[83px] w-[28px] rounded-[14px]" />
      <ImagePlaceholder tone="#375345" label="next card" className="absolute top-[333px] left-[382px] h-[83px] w-[28px] rounded-[14px]" />
      <div className="absolute top-[333px] left-[16px] flex h-[83px] w-[358px] items-center overflow-hidden rounded-[22px] pr-[18px] pl-[24px]" style={{ background: theme.eventCard }}>
        <ImagePlaceholder tone="#6a5bd4" label="tarot cards art" className="absolute top-0 left-[48px] h-[83px] w-[290px]" />
        <ImagePlaceholder tone={theme.accent} label="event icon" className="relative h-[30px] w-[8px] rounded-full" />
        <div className="relative ml-[16px] flex flex-1 flex-col">
          <span className="text-[10px] leading-[14px] text-white/70">EVENT</span>
          <span className="text-[15px] leading-[20px] font-semibold text-white">World Tarot Day</span>
        </div>
        <ChevronRight className="relative" size={18} strokeWidth={3} color="#fff" />
      </div>
      <ImagePlaceholder tone="#5d5148" label="next horoscope card" className="absolute top-[430px] left-[382px] h-[345px] w-[30px] rounded-[24px]" />
      <ImagePlaceholder tone="#5d5148" label="previous card" className="absolute top-[430px] left-[-22px] h-[345px] w-[30px] rounded-[24px]" />
      <div className="absolute top-[430px] left-[16px] h-[370px] w-[358px] overflow-hidden rounded-[26px]">
        <ImagePlaceholder tone="#6b5f55" label="horoscope photo" className="absolute inset-0" />
        <div className="absolute top-[22px] left-[24px] flex items-center gap-[19px]">
          <span className="relative h-[28px] w-[2px] rounded bg-white">
            <span className="absolute top-[9px] left-[-4px] h-[10px] w-[10px] rounded-full border-2 border-white bg-[#6b5f55]" />
          </span>
          <div className="flex flex-col">
            <span className="text-[10px] leading-[14px] text-white/60">{horoscope.kicker}</span>
            <span className="text-[14px] leading-[20px] font-semibold text-white">{horoscope.title}</span>
          </div>
        </div>
        <ChevronRight className="absolute top-[22px] right-[22px]" size={16} strokeWidth={3} color="#fff" />
        <span className="absolute top-[150px] left-[20px] text-[10.5px] font-semibold text-white">FOCUS ON</span>
        <p className="absolute top-[176px] left-[20px] w-[275px] text-[20.5px] leading-[30px] font-medium text-[#dedede]">{horoscope.focus}</p>
        <span className="absolute top-[304px] left-[20px] text-[9px] text-white/60">ME AND MYSELF</span>
        <span className="absolute top-[318px] left-[20px] flex items-start gap-[5px] text-[17px] font-medium text-white/60">
          Self-Care
          <Triangle size={8} fill="#3dbb5b" color="#3dbb5b" className="mt-[3px]" />
        </span>
        <ImagePlaceholder tone="#a593b8" label="astrologer avatar" className="absolute top-[263px] left-[275px] h-[68px] w-[68px] rounded-full" />
        <ImagePlaceholder tone="#5b9e5a" label="lotus" className="absolute top-[327px] left-[279px] h-[18px] w-[58px] rounded-t-full" />
      </div>
      <MoonTabBar tabs={tabs} active="calendar" />
    </AppScreen>
  )
}
