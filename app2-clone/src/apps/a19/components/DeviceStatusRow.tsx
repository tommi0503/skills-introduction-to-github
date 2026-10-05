import { cn } from '../../../ui'
import type { DeviceStatus } from '../data'
import { fi } from '../theme'

/** "▭ 67% ● Online · Now" row. */
export function DeviceStatusRow({ status, className }: { status: DeviceStatus; className?: string }) {
  return (
    <div className={cn('flex items-center text-[13px] font-medium', className)} style={{ color: fi.green }}>
      <span className="relative mr-[5px] flex h-[10px] w-[17px] items-center rounded-[2.5px] border-[1.5px] border-current p-[1.5px]">
        <span className="h-full w-[45%] rounded-[1px] bg-current" />
        <span className="absolute -right-[3.5px] h-[4px] w-[1.5px] rounded-r bg-current" />
      </span>
      <span>{status.battery}</span>
      <span className="ml-[9px] mr-[4px] h-[9px] w-[9px] rounded-full bg-current" />
      <span>{status.online}</span>
      <span className="mx-[5px] text-[#8a8a8a]">·</span>
      <span className="text-[#8a8a8a]">{status.updated}</span>
    </div>
  )
}
