import { EllipsisVertical } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { nextAppointment } from '../data'
import { theme } from '../theme'

export interface AppointmentCardProps {
  appointment: typeof nextAppointment
}

/** Frosted card wrapping a white details panel plus a time/date footer. */
export function AppointmentCard({ appointment }: AppointmentCardProps) {
  return (
    <div
      className="rounded-[20px] border p-[3px]"
      style={{ background: theme.glass, borderColor: theme.glassBorder }}
    >
      <div className="rounded-[18px] bg-white">
        <div className="flex h-[41px] items-center justify-between border-b border-[#ececec] pl-[12px] pr-[10px] text-[13.9px] font-semibold">
          {appointment.title}
          <EllipsisVertical size={14} strokeWidth={2.4} />
        </div>
        <div className="flex h-[64px] items-center gap-[8px] px-[12px]">
          <ImagePlaceholder label="Barber avatar" className="h-[35px] w-[35px] rounded-full" />
          <div className="flex-1">
            <div className="text-[13.8px] font-semibold leading-[18px]">{appointment.barber}</div>
            <div className="text-[11px] leading-[15px]" style={{ color: theme.muted }}>
              {appointment.address}
            </div>
          </div>
          <div className="text-[12px] font-medium">{appointment.service}</div>
        </div>
      </div>
      <div className="flex h-[44px] items-center justify-between px-[10px] text-[14px] font-medium">
        <span>{appointment.time}</span>
        <span>{appointment.date}</span>
      </div>
    </div>
  )
}
