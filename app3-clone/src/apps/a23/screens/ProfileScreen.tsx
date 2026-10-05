import { Flag, Pencil, Settings, X } from 'lucide-react'
import { AppScreen, HomeIndicator, StatusBar } from '../../../ui'
import { ProgressBar } from '../components/ProgressBar'
import { SandCard } from '../components/SandCard'
import { profile } from '../data'
import { theme } from '../theme'

export function ProfileScreen() {
  const { activity, reviews, trial } = profile
  return (
    <AppScreen background="#000" className="font-inter text-[#141414]">
      <StatusBar color="#fff" paddingTop={20} paddingX={54} fontSize={15.5} className="pr-[35px]!" />
      <div className="absolute left-[16px] right-[17px] top-[58px] h-[30px] rounded-t-[12px] bg-[#e9e8e6]" />
      <div className="absolute inset-x-0 bottom-0 top-[68px] rounded-t-[14px]" style={{ background: theme.sheet }}>
        <Settings className="absolute left-[16px] top-[17px]" size={22} strokeWidth={1.6} />
        <span className="absolute inset-x-0 top-[15px] text-center text-[18px] font-semibold">{profile.title}</span>
        <X className="absolute right-[17px] top-[16px]" size={23} strokeWidth={1.8} />
        <h1 className="absolute left-[17px] top-[89px] font-times text-[25.5px] tracking-[-0.3px]">{profile.heading}</h1>

        <SandCard title={activity.title} className="left-[17px] right-[17px] top-[139px] h-[277px]">
          <div className="mt-[28px] flex justify-between px-[4px]">
            {activity.days.map((d, i) => (
              <div
                key={i}
                className="flex h-[42px] w-[32px] flex-col items-center justify-center gap-[8px] rounded-[4px] leading-none"
                style={d.current ? { background: '#fff', border: '1px solid #e0ded9' } : undefined}
              >
                <span className="text-[11.5px] text-[#8a8a8a]">{d.letter}</span>
                <span className="text-[13.5px] font-semibold">{d.count}</span>
              </div>
            ))}
          </div>
          <div className="mt-[14px] h-px bg-[#e4e1dc]" />
          <div className="mt-[19px] flex items-center">
            <Flag size={28} strokeWidth={1.4} color={theme.orange} fill="#f6cdb9" />
            <div className="ml-[17px] flex-1 leading-none">
              <div className="text-[15px] font-semibold">{activity.goal.title}</div>
              <div className="mt-[6px] text-[13px] text-[#8a8a8a]">{activity.goal.sub}</div>
            </div>
            <Pencil size={16} strokeWidth={1.8} className="mr-[2px]" />
          </div>
          <div className="mt-[16px]">
            <ProgressBar value={activity.goal.progress} color={theme.orange} track="#fff" height={7} />
          </div>
          <div className="mt-[24px] flex h-[43px] items-center justify-center rounded-full bg-[#141414] text-[15.5px] font-semibold text-white">
            {activity.cta}
          </div>
        </SandCard>

        <SandCard title={reviews.title} className="left-[17px] right-[17px] top-[438px] h-[260px]">
          <div className="mt-[28px] flex">
            {reviews.stats.map((s, i) => (
              <div key={s.label} className="flex-1" style={i > 0 ? { borderLeft: '1px solid #e4e1dc', paddingLeft: 32 } : { flex: '0 0 125px' }}>
                <div className="text-[13px] leading-none text-[#666]">{s.label}</div>
                <div className="mt-[17px] text-[30px] font-bold leading-none tracking-[-0.5px]">{s.value}</div>
              </div>
            ))}
          </div>
          <div className="mt-[22px] h-px bg-[#e4e1dc]" />
          <div className="mt-[17px] text-[13px] leading-none text-[#666]">{reviews.method}</div>
          <div className="mt-[18px]">
            <ProgressBar value={1} color={theme.green} track={theme.green} height={15} />
          </div>
        </SandCard>

        <div className="absolute inset-x-0 top-[673px] flex h-[72px] items-center justify-center text-[15px]" style={{ background: theme.peach }}>
          {trial.prefix}
          <b className="ml-[4px] font-bold italic">{trial.emphasis}</b>
        </div>
      </div>
      <HomeIndicator width={138} bottom={8} />
    </AppScreen>
  )
}
