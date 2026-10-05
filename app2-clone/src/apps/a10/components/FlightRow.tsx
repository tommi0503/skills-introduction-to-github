import { ArrowDownRight, ArrowUpRight } from 'lucide-react'
import { cn } from '../../../ui'
import type { Flight, Leg } from '../data'
import { theme } from '../theme'
import { AirlineMark } from './AirlineMark'

export type FlightTone = 'live' | 'scheduled'

export interface FlightRowProps {
  flight: Flight
  tone?: FlightTone
  height?: number
  className?: string
  dividerClassName?: string
}

function LegTime({ leg, dir, tone, className }: { leg: Leg; dir: 'dep' | 'arr'; tone: FlightTone; className?: string }) {
  const Arrow = dir === 'dep' ? ArrowUpRight : ArrowDownRight
  const live = tone === 'live'
  return (
    <div className={cn('flex items-center', className)}>
      <span
        className="flex h-[15px] w-[15px] items-center justify-center rounded-full text-white"
        style={{ background: live ? theme.greenIcon : theme.greyIcon }}
      >
        <Arrow size={11} strokeWidth={3} />
      </span>
      <span className="ml-[7px] text-[15px] tracking-[-0.3px] text-[#9a9a9f]">{leg.code}</span>
      <span className="ml-[5px] text-[15px] font-medium tracking-[-0.3px]" style={{ color: live ? theme.green : theme.ink }}>
        {leg.time}
      </span>
    </div>
  )
}

/** One flight: lead countdown on the left, number/meta, route and both legs. */
export function FlightRow({ flight, tone = 'live', height = 111.5, className, dividerClassName }: FlightRowProps) {
  return (
    <div className={cn('relative flex', className)} style={{ height }}>
      <div className="flex w-[96px] shrink-0 flex-col items-center pt-[31.5px]">
        <span className="text-[34px] leading-[34px] font-normal text-black">{flight.lead}</span>
        <span className="mt-[4.5px] text-[10.5px] leading-[12px] tracking-[0.4px] text-[#8e8e93]">{flight.leadUnit}</span>
      </div>
      <div className="min-w-0 flex-1 pt-[21px] pr-[22px]">
        <div className="flex h-[17px] items-center text-[13.5px] tracking-[-0.2px] text-[#8e8e93]">
          {flight.airlineMark === 'logo' && <AirlineMark />}
          <span className={cn(flight.airlineMark === 'logo' && 'ml-[8px]')}>{flight.number}</span>
          <span className="ml-auto">
            {flight.metaLabel}
            {flight.metaValue && <span className="ml-[4px] font-semibold text-[#2f9a5c]">{flight.metaValue}</span>}
          </span>
        </div>
        <div className="mt-[6px] h-[22px] text-[17px] leading-[22px] tracking-[-0.4px] whitespace-nowrap text-black">
          <span className="font-medium">{flight.from}</span> to <span className="font-medium">{flight.to}</span>
        </div>
        <div className="mt-[5.5px] flex h-[22px] items-center">
          <LegTime leg={flight.dep} dir="dep" tone={tone} className="w-[129px]" />
          <LegTime leg={flight.arr} dir="arr" tone={tone} />
        </div>
      </div>
      <div className={cn('absolute bottom-0 h-px bg-[#e9e9ec]', dividerClassName)} />
    </div>
  )
}
