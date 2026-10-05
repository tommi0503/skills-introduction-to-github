import { Volleyball, X } from 'lucide-react'
import { cn } from '../../../ui'
import { match } from '../data'
import { theme } from '../theme'
import { TeamLogo } from './TeamLogo'

/** Competition title, close button and the two team crests (sheet-relative coordinates). */
export function MatchHeader({ crestStyle }: { crestStyle: 'outline' | 'filled' }) {
  const crest = crestStyle === 'outline' ? 'border border-white/35 bg-white/8' : 'bg-white/25'
  return (
    <>
      <div className="absolute inset-x-0 top-[17px] flex flex-col items-center text-white">
        <span className="flex items-center gap-[6px] text-[13.5px] leading-[18px] font-semibold">
          <Volleyball size={13} strokeWidth={2.2} />
          {match.competition}
        </span>
        <span className="mt-[3px] text-[12px] leading-[16px] font-medium text-white/85">{match.stage}</span>
      </div>
      <div
        className="absolute top-[15px] left-[330px] flex h-[44px] w-[44px] items-center justify-center rounded-full"
        style={{ background: theme.lightBlue, color: '#1d2b70' }}
      >
        <X size={22} strokeWidth={1.8} />
      </div>
      {[match.home, match.away].map((team, i) => (
        <div key={team} className="absolute top-[89px] flex w-[100px] flex-col items-center" style={{ left: i === 0 ? 50 : 239 }}>
          <div className={cn('flex h-[100px] w-[100px] items-center justify-center rounded-full', crest)}>
            <TeamLogo size={56} tone="#d9deef" className="h-[40px]! w-[60px]! rounded-[8px]" />
          </div>
          <span className="mt-[13px] text-[16.5px] leading-[24px] font-semibold text-white">{team}</span>
        </div>
      ))}
      <span className="absolute top-[120px] left-[194px] h-[48px] w-px bg-white/15" />
    </>
  )
}
