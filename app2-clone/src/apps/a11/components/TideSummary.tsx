import { ArrowDown, ArrowUp, Moon, Sunrise, Sunset, type LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'
import { fallingTide } from '../data'
import { LevelBadge } from './LevelBadge'

type SunKind = (typeof fallingTide.sun)[number]['kind']
const sunIcon: Record<SunKind, { icon: LucideIcon; bg: string; fg: string }> = {
  sunrise: { icon: Sunrise, bg: '#5d6078', fg: '#f6a742' },
  sunset: { icon: Sunset, bg: '#5d6078', fg: '#f6a742' },
  moonrise: { icon: Moon, bg: '#4d3f9a', fg: '#f3d36a' },
  moonset: { icon: Moon, bg: '#4d3f9a', fg: '#f3d36a' },
}

/** Current level headline, sun/moon times and today's tide table. */
export function TideSummary({ data = fallingTide }: { data?: typeof fallingTide }) {
  return (
    <div className="absolute inset-x-0 top-[184px] flex flex-col items-center text-white">
      <div className="flex items-center gap-[10px] pl-[24px]">
        <span className="text-[30px] leading-[38px] font-bold">{data.level}</span>
        <LevelBadge rising={false} size={26} />
      </div>
      <div className="text-[22px] leading-[28px] font-bold">{data.title}</div>
      <div className="text-[13px] leading-[18px] text-white/55">{data.subtitle}</div>
      <div className="mt-[7px] h-px w-[201px] bg-white/12" />
      <div className="mt-[11px] grid grid-cols-[97px_auto] gap-y-[7px] pl-[11px] text-[15px] leading-[18px] font-semibold">
        {data.sun.map((s) => {
          const { icon: Icon, bg, fg } = sunIcon[s.kind]
          return (
            <div key={s.kind} className="flex items-center gap-[8px]">
              <span className="flex h-[18px] w-[18px] items-center justify-center rounded-[4px]" style={{ background: bg, color: fg }}>
                <Icon size={12} strokeWidth={2.4} fill={s.kind.startsWith('moon') ? fg : 'none'} />
              </span>
              {s.time}
            </div>
          )
        })}
      </div>
      <div className="mt-[14px] flex flex-col gap-[3.5px] pr-[9px]">
        {data.tides.map((t) => {
          const Icon = t.rising ? ArrowUp : ArrowDown
          return (
            <div key={t.time} className={cn('flex h-[18px] items-center text-[14.5px]', t.past && 'opacity-40')}>
              <span className="flex h-[14px] w-[14px] items-center justify-center rounded-full bg-[#4a86d6]/45 text-[#69a8f5]">
                <Icon size={10} strokeWidth={3} />
              </span>
              <span className="ml-[11px] w-[64px] font-semibold">{t.time}</span>
              <span className="text-white/60">{t.height}</span>
            </div>
          )
        })}
      </div>
    </div>
  )
}
