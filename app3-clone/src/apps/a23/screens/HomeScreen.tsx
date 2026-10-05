import { Apple, Flame, Plus } from 'lucide-react'
import { AppScreen, HomeIndicator, StatusBar } from '../../../ui'
import { FoodCard } from '../components/FoodCard'
import { MacroCard } from '../components/MacroCard'
import { Ring } from '../components/Ring'
import { WeekStrip } from '../components/WeekStrip'
import { home } from '../data'
import { theme } from '../theme'

export function HomeScreen() {
  return (
    <AppScreen background="linear-gradient(180deg,#ebebeb 0%,#f3f3f3 35%,#fafafa 60%,#fff 100%)" className="font-dm text-[#111]">
      <StatusBar paddingTop={16} paddingX={54} fontSize={15.5} />
      <div className="absolute left-[32px] top-[81px] flex items-center gap-[3px]">
        <Apple size={24} fill={theme.ink} strokeWidth={1.5} />
        <span className="text-[23px] font-bold tracking-[-0.6px]">{home.brand}</span>
      </div>
      <div className="absolute left-[298px] top-[79px] flex h-[29px] w-[62px] items-center justify-center gap-[3px] rounded-full bg-white text-[13px] font-medium">
        <Flame size={14} color={theme.flame} fill={theme.flame} />
        {home.streak}
      </div>
      <div className="absolute left-[29px] right-[29px] top-[131px]">
        <WeekStrip days={home.week} />
      </div>
      <div
        className="absolute left-[30px] right-[30px] top-[208px] flex h-[146px] items-center justify-between rounded-[16px] bg-white pl-[31px] pr-[24px]"
        style={{ boxShadow: '0 2px 12px rgba(0,0,0,.05)' }}
      >
        <div>
          <div className="text-[41px] font-bold leading-none tracking-[-1px]">{home.calories.value}</div>
          <div className="mt-[10px] text-[11px] leading-none text-[#333]">{home.calories.label}</div>
        </div>
        <Ring size={108} stroke={7} progress={home.calories.progress} color={theme.ink} track={theme.ringTrack}>
          <span className="flex size-[38px] items-center justify-center rounded-full bg-[#f4f4f6]">
            <Flame size={15} fill={theme.ink} />
          </span>
        </Ring>
      </div>
      <div className="absolute left-[30px] right-[30px] top-[366px] flex gap-[10px]">
        {home.macros.map((m) => (
          <MacroCard key={m.name} m={m} />
        ))}
      </div>
      <div className="absolute left-0 right-0 top-[532px] flex justify-center gap-[9px]">
        {Array.from({ length: home.pages }, (_, i) => (
          <span key={i} className="size-[7px] rounded-full border" style={i === 0 ? { background: theme.ink, borderColor: theme.ink } : { borderColor: '#cfcfcf' }} />
        ))}
      </div>
      <h2 className="absolute left-[30px] top-[570px] text-[17px] font-semibold">{home.recentTitle}</h2>
      <div className="absolute left-[30px] right-[30px] top-[612px]">
        <FoodCard {...home.recent} macroDefs={home.macros} />
      </div>
      <nav className="absolute inset-x-0 bottom-0 top-[745px] bg-white" style={{ boxShadow: '0 -1px 6px rgba(0,0,0,.04)' }}>
        {home.tabs.map((t, i) => {
          const Icon = t.icon
          return (
            <div key={t.label} className="absolute flex w-[60px] -translate-x-1/2 flex-col items-center" style={{ left: 55 + i * 94, top: 15 }}>
              <Icon size={21} strokeWidth={1.6} color={t.active ? theme.ink : '#bdbdbd'} />
              <span className="mt-[6px] text-[10.5px]" style={{ color: t.active ? theme.ink : '#a8a8a8', fontWeight: t.active ? 600 : 400 }}>
                {t.label}
              </span>
            </div>
          )
        })}
      </nav>
      <div className="absolute left-[297px] top-[729px] flex size-[62px] items-center justify-center rounded-full" style={{ background: '#1b1b20' }}>
        <Plus size={24} color="#fff" strokeWidth={2} />
      </div>
      <HomeIndicator width={138} bottom={8} />
    </AppScreen>
  )
}
