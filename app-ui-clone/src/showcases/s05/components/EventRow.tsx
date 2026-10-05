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
      <span className="w-[99px] pt-[-2px] pl-[5px] text-[14.5px] leading-[18px] tracking-[-0.3px] text-[#1a1a1a]">{event.time}</span>
      <div className="flex h-[80px] w-[256px] items-center rounded-[14px] bg-[#fdfdfd] pl-[7px]">
        <ImagePlaceholder label={`${event.title} vehicle`} className="h-[18px] w-[34px] rounded-[4px]" />
        <div className="ml-[17px]">
          <p className="text-[15px] leading-[18px] tracking-[-0.4px] text-[#1a1a1a]">{event.title}</p>
          {metaRows.map(({ key, icon: Icon }) => (
            <p key={key} className="mt-[6px] flex items-center gap-[6px] text-[10.5px] leading-[13px] text-[#777]">
              <Icon size={11} strokeWidth={1.6} />
              {event[key]}
            </p>
          ))}
        </div>
      </div>
    </div>
  )
}
