import type { TimeSlot } from '../data'

export interface TimelineItemProps {
  slot: TimeSlot
}

/** One timetable entry: time | dot | title + details. The connecting rail is drawn by the panel. */
export function TimelineItem({ slot }: TimelineItemProps) {
  return (
    <div className="flex">
      <span className="w-[66px] text-right font-dohyeon text-[21px] leading-[30px] text-[#7cb888]">{slot.time}</span>
      <span className="relative w-[46px] shrink-0">
        <span className="absolute left-[18px] top-[10px] h-[11px] w-[11px] rounded-full bg-[#76b282]" />
      </span>
      <div className="flex flex-col">
        <span className="font-dohyeon text-[22px] leading-[30px] text-[#6aae78]">{slot.title}</span>
        <div className="mt-[6px] flex flex-col text-[16px] font-semibold leading-[25px] tracking-[-0.03em] text-[#46484b]">
          {slot.details.map((l) => (
            <span key={l}>{l}</span>
          ))}
        </div>
      </div>
    </div>
  )
}
