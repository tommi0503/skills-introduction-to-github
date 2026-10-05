import { Flame, Play, Plus, Settings, Sparkle, Trophy } from 'lucide-react'
import { AppScreen, cn } from '../../../ui'
import { BottomNav } from '../components/BottomNav'
import { HabitCard } from '../components/HabitCard'
import { NeoBox } from '../components/NeoBox'
import { StatusOverlay } from '../components/StatusOverlay'
import { habits, headerStats, today } from '../data'

const statIcon = { flame: Flame, trophy: Trophy, sparkle: Sparkle }

export function TodayScreen() {
  return (
    <AppScreen background="#f4f4f4" className="font-sora text-[#111]">
      <div className="absolute -top-[40px] left-[90px] h-[110px] w-[200px] rounded-full bg-[#f6c9a8]/60 blur-[30px]" />
      <StatusOverlay />
      <div className="absolute top-[64px] left-[20px] flex gap-[6px]">
        {headerStats.map((s) => {
          const Icon = statIcon[s.icon]
          const flame = s.icon === 'flame'
          return (
            <div key={s.key} className="relative flex h-[27px] items-center gap-[7px] rounded-[6px] bg-white/80 px-[11px] text-[13px] font-semibold">
              <Icon size={14} strokeWidth={2} fill={flame ? '#f07a2a' : '#111'} stroke={flame ? '#f07a2a' : '#111'} />
              <span className={cn(flame && 'text-[#f07a2a]')}>{s.value}</span>
              {s.dot && <span className="absolute -top-[2px] -right-[1px] h-[6px] w-[6px] rounded-full bg-[#f07a2a]" />}
            </div>
          )
        })}
      </div>
      <NeoBox className="absolute top-[63px] left-[343px] h-[29px] w-[29px] rounded-[5px] border-[#555] bg-[#ececec]" shadow="#bbb" offset={1.5}>
        <Settings size={17} strokeWidth={2.4} />
      </NeoBox>
      <div className="absolute top-[104px] left-[20px] text-[25px] leading-[30px] font-bold tracking-[-0.6px]">{today.day}</div>
      {[0, 1].map((i) => (
        <NeoBox key={i} className="absolute top-[106px] h-[24px] w-[31px] rounded-[6px] border-[2.5px] bg-white" offset={3.5} style={{ left: 290 + i * 40 }}>
          <Play size={11} fill="#111" strokeWidth={0} className={i === 0 ? 'rotate-180' : ''} />
        </NeoBox>
      ))}
      <div className="absolute top-[146px] left-[20px] text-[14px] font-semibold tracking-[-0.1px]">{today.motto}</div>
      <div className="absolute top-[189px] left-[21px] flex gap-[9.5px]">
        {today.tabs.map((t, i) => (
          <NeoBox
            key={t.key}
            shadow={i === 0 ? '#111' : '#cfcfcf'}
            className={cn(
              'h-[33px] rounded-[5px] px-[16px] text-[11.5px]',
              i === 0 ? 'bg-[#1c1c1c] font-semibold text-white' : 'border-[#cfcfcf] bg-white text-[#9a9a9a]',
            )}
          >
            {t.label}
            <sup className="ml-[2px] text-[8.5px]">{t.count}</sup>
          </NeoBox>
        ))}
      </div>
      <NeoBox className="absolute top-[193px] left-[345px] h-[25px] w-[31px] rounded-[6px] bg-white">
        <Plus size={16} strokeWidth={3} />
      </NeoBox>
      <div className="absolute top-[253px] left-[20px] flex w-[351px] flex-col gap-[12.5px]">
        {habits.map((h, i) => (
          <HabitCard key={h.id} habit={h} height={i === 0 ? 178 : 180} />
        ))}
      </div>
      <BottomNav active="home" />
    </AppScreen>
  )
}
