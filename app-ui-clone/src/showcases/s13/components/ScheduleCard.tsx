import { ImagePlaceholder, cn } from '../../../ui'
import type { ScheduleEntry } from '../data'
import { theme } from '../theme'

/** Appointment tile in "Today Schedule" with a status chip. */
export function ScheduleCard({ entry, className }: { entry: ScheduleEntry; className?: string }) {
  return (
    <div className={cn('relative w-[139px] overflow-hidden rounded-[16px] bg-white px-[14px] pt-[14px]', className)}>
      <span
        className="absolute right-[6px] top-[7px] flex h-[19px] w-[43px] items-center justify-center rounded-full text-[10.5px] text-[#3c4a2a]"
        style={{ background: entry.status === 'Done' ? theme.doneChip : theme.activeChip }}
      >
        {entry.status}
      </span>
      <ImagePlaceholder label={`${entry.name} avatar`} className="h-[36px] w-[36px] rounded-full" />
      <div className="mt-[7px] text-[14px] font-semibold leading-[18px]">{entry.name}</div>
      <div className="mt-[2px] text-[11px] leading-[14px] text-[#aaa9a5]">{entry.time}</div>
    </div>
  )
}
