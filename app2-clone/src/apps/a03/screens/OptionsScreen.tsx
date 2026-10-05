import { ChevronLeft, MoveDiagonal, Search, Tag } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { FloatingPill } from '../components/FloatingPill'
import { PayoffCard } from '../components/PayoffCard'
import { TopBar } from '../components/TopBar'
import { options } from '../data'

export function OptionsScreen() {
  const o = options
  return (
    <AppScreen className="font-inter">
      <div className="absolute inset-x-0 top-0 border-b border-[#e4e4e6] bg-[#f5f5f6]" style={{ height: 155 }} />
      <TopBar />
      <FloatingPill left={14} top={58} height={44} width={44} className="justify-center">
        <ChevronLeft size={20} strokeWidth={2.2} />
      </FloatingPill>
      <div className="absolute flex items-center gap-[6px] rounded-full bg-[#141414] pl-[17px] text-[14.5px] font-semibold text-white" style={{ left: 71, top: 59, width: 151, height: 42 }}>
        <Search size={14} strokeWidth={2.6} />
        {o.search}
      </div>
      <FloatingPill left={279} top={59} height={42} width={94} className="justify-between pr-[18px] pl-[16px]">
        <Tag size={17} strokeWidth={2.2} fill="#111" color="#111" />
        <span className="text-[18px] font-semibold">?</span>
      </FloatingPill>
      <div className="absolute flex gap-[20.5px] text-[14.5px] whitespace-nowrap" style={{ left: 15, top: 125 }}>
        {o.tabs.map((t) => {
          const on = t === o.activeTab
          return (
            <span key={t} className="relative" style={{ color: on ? '#111' : '#8f8f94', fontWeight: on ? 600 : 500 }}>
              {t}
              {on && <span className="absolute -inset-x-[5px] top-[29px] h-[2px] bg-[#333]" />}
            </span>
          )
        })}
      </div>
      <div className="absolute inset-x-0 text-center text-[12.5px] font-semibold text-[#4f9b2a]" style={{ top: 191 }}>
        {o.priceNote}
      </div>
      <div className="absolute inset-x-0 text-center text-[19.5px] font-medium tracking-[-0.2px]" style={{ top: 212 }}>
        {o.title}
      </div>
      <div className="absolute inset-x-[15px] border-t border-dashed border-[#c9c9cc]" style={{ top: 282 }} />
      <div className="absolute flex gap-[13px]" style={{ left: 81, top: 259 }}>
        {o.directions.map(({ key, icon: Icon, color }) => (
          <span key={key} className="flex h-[47px] w-[47px] items-center justify-center rounded-full border-[1.5px] bg-white" style={{ borderColor: color, color }}>
            <Icon size={17} strokeWidth={2.2} />
          </span>
        ))}
      </div>
      <div className="absolute text-[19px] font-semibold tracking-[-0.2px]" style={{ left: 15, top: 343 }}>
        {o.section}
      </div>
      <span className="absolute flex h-[20px] w-[38px] items-center rounded-full bg-[#f2f2f4] pl-[8px] text-[11px] font-semibold text-[#555]" style={{ left: 335, top: 344 }}>
        ?
      </span>
      <div className="absolute grid grid-cols-2 gap-x-[17px] gap-y-[29px]" style={{ left: 15, top: 377 }}>
        {o.strategies.map((s) => (
          <PayoffCard key={s.key} strategy={s} zeroY={o.zeroY} />
        ))}
      </div>
      <div className="absolute inset-x-0 bottom-0 bg-white" style={{ top: 808 }} />
      <div className="absolute flex items-center justify-center gap-[7px] rounded-full bg-[#5a9b32] text-[13.5px] font-semibold text-white" style={{ left: 101, top: 770, width: 185, height: 26 }}>
        {o.currentPrice}
        <MoveDiagonal size={12} strokeWidth={2} />
      </div>
    </AppScreen>
  )
}
