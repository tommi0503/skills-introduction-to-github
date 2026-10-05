import { Clock, MapPin } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { ScheduleEvent } from '../data'

const metaRows = [
  { key: 'window', icon: Clock },
  { key: 'place', icon: MapPin },
] as const

/** One timeline row: time stamp on the rail + white event card. */
export function EventRow({ event }: { event: ScheduleEvent }) {
  return (
    <div className="relative flex h-[96px]">
      <span className="absolute top-[24px] left-[27px] h-[58px] w-[2px] rounded-full bg-[#ececec]" />
      <span className="w-[67px] pl-[9px] text-[14.5px] leading-[18px] tracking-[-0.3px] text-[#1a1a1a]">{event.time}</span>
      <div className="flex -mt-[6px] h-[83px] w-[276px] items-center rounded-[14px] bg-[#fdfdfd] pl-[18px]">
        <ImagePlaceholder label={`${event.title} vehicle`} className="h-[18px] w-[34px] rounded-[4px]" />
        <div className="mt-[8px] ml-[21px]">
          <p className="-mt-[2px] mb-[9px] text-[15px] leading-[18px] tracking-[-0.4px] text-[#1a1a1a]">{event.title}</p>
          {metaRows.map(({ key, icon: Icon }) => (
            <p key={key} className="mt-[6px] flex items-center gap-[6px] text-[11px] leading-[13px] tracking-[-0.2px] text-[#666]">
              <Icon size={12} strokeWidth={1.6} />
              {event[key]}
            </p>
          ))}
        </div>
      </div>
    </div>
  )
}
