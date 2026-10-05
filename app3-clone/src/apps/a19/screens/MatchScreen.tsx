import { CalendarDays, EyeOff, Share, TriangleAlert } from 'lucide-react'
import { AppScreen, cn } from '../../../ui'
import { MatchHeader } from '../components/MatchHeader'
import { PhoneStatus } from '../components/PhoneStatus'
import { Sheet } from '../components/Sheet'
import { TeamLogo } from '../components/TeamLogo'
import { match } from '../data'
import { theme } from '../theme'

const box = 'absolute left-[15px] w-[360px] rounded-[14px] border border-white/20 bg-white/5'

export function MatchScreen() {
  const [, total] = [0, match.innings.length - 1]
  return (
    <AppScreen background={theme.sheetBackdrop} className="font-jakarta">
      <PhoneStatus />
      <Sheet style={{ background: `linear-gradient(to bottom, ${theme.matchTop}, ${theme.matchBottom} 60%, #24378a)` }}>
        <MatchHeader crestStyle="outline" />
        <div className="absolute inset-x-0 top-[270px] flex flex-col items-center text-white">
          <span className="text-[17px] leading-[24px] font-semibold">Today</span>
          <span className="mt-[4px] flex items-center gap-[14px] text-[43px] leading-[50px] font-bold">
            2<span className="h-[4px] w-[19px] rounded bg-[#8fa2e8]" />3
          </span>
          <span className="mt-[20px] text-[13px] font-semibold">Final</span>
        </div>
        <div className={cn(box, 'top-[427px] h-[141px]')}>
          <div className="flex h-[50px] items-center border-b border-white/20 pr-[13px] pl-[56px] text-[14px] font-medium text-white">
            {match.innings.map((n) => (
              <span key={n} className="flex-1 text-center">{n}</span>
            ))}
          </div>
          {match.lines.map((l, i) => (
            <div key={l.team} className={cn('flex items-center pr-[13px] pl-[16px] text-[14.5px] font-medium text-white', i === 0 ? 'mt-[10px] h-[36px]' : 'h-[38px]')}>
              <span className="w-[40px]">
                <TeamLogo size={20} tone="#8a9ad8" className="rounded-[4px]" />
              </span>
              {l.runs.map((r, j) => (
                <span key={j} className={cn('flex-1 text-center', j === total && 'font-bold')}>{r}</span>
              ))}
            </div>
          ))}
        </div>
        <div className={cn(box, 'top-[584px] h-[98px]')}>
          {match.info.map((row, i) => (
            <div key={row.label} className={cn('flex h-[49px] items-center justify-between px-[16px] text-[14px] font-medium', i === 0 && 'border-b border-white/20')}>
              <span className="text-[#c9d1f2]">{row.label}</span>
              <span className="text-white">{row.value}</span>
            </div>
          ))}
        </div>
        <div className="absolute top-[712px] left-[28px] flex h-[48px] w-[48px] items-center justify-center rounded-full" style={{ background: theme.lightBlue, color: '#1d2b70' }}>
          <EyeOff size={22} strokeWidth={1.8} />
        </div>
        <span className="absolute top-[711px] left-[140px] flex items-center gap-[6px] text-[14px] font-medium text-[#c3cbef]">
          <TriangleAlert size={15} strokeWidth={1.8} />
          Report Event
        </span>
        <div className="absolute top-[713px] left-[255px] flex h-[46px] w-[107px] items-center justify-around rounded-full px-[10px]" style={{ background: theme.lightBlue, color: '#1d2b70' }}>
          <Share size={20} strokeWidth={1.8} />
          <CalendarDays size={20} strokeWidth={1.8} />
        </div>
      </Sheet>
    </AppScreen>
  )
}
