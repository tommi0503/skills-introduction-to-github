import type { CSSProperties } from 'react'
import { cn } from '../../../ui'
import type { Fixture } from '../data'
import { theme } from '../theme'
import { TeamLogo } from './TeamLogo'

const tones = {
  light: { bg: theme.card, head: 'text-[#111]', win: 'text-[#111]', lose: 'text-[#9a9ca6]', foot: 'text-[#333]', logo: undefined },
  mlb: { bg: theme.mlb, head: 'text-white', win: 'text-white', lose: 'text-white/60', foot: 'text-white/80', logo: '#5a6db8' },
  nba: { bg: theme.nba, head: 'text-white', win: 'text-white', lose: 'text-white/60', foot: 'text-white/80', logo: '#f0a07a' },
} as const

export interface FixtureCardProps {
  fixture: Pick<Fixture, 'time' | 'status' | 'league' | 'teams' | 'tone'>
  className?: string
  style?: CSSProperties
}

/** Calendar event block: status/time, two team lines, league footer. */
export function FixtureCard({ fixture, className, style }: FixtureCardProps) {
  const t = tones[fixture.tone]
  return (
    <div className={cn('flex flex-col rounded-[10px] px-[13px] pt-[14px] pb-[13px]', className)} style={{ background: t.bg, ...style }}>
      <span className={cn('text-[11.5px] leading-[16px] font-semibold', t.head)}>{fixture.time ?? fixture.status}</span>
      <div className="mt-[6px] flex flex-col gap-[5px]">
        {fixture.teams.map((tm) => (
          <div key={tm.name} className={cn('flex items-center text-[15.5px] leading-[20px] font-bold', tm.winner ? t.win : t.lose)}>
            <TeamLogo tone={t.logo} className="mr-[8px]" />
            <span className="flex-1">{tm.name}</span>
            {tm.score !== undefined && <span>{tm.score}</span>}
          </div>
        ))}
      </div>
      <span className={cn('mt-auto text-[11.5px] font-medium', t.foot)}>{fixture.league}</span>
    </div>
  )
}
